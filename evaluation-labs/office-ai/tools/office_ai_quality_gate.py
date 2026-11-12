#!/usr/bin/env python3
"""Local-only Office quality gates for GDES-REG-002.

Never invokes candidate software, model endpoints, or network APIs.
LibreOffice and Poppler are local document-processing tools only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {
    "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
REQUIRED = {
    ".xlsx": ("[Content_Types].xml", "_rels/.rels", "xl/workbook.xml"),
    ".docx": ("[Content_Types].xml", "_rels/.rels", "word/document.xml"),
    ".pptx": ("[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml"),
}


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def command_log(command: list[str], log_dir: Path, label: str, timeout: int = 180) -> dict[str, Any]:
    log_dir.mkdir(parents=True, exist_ok=True)
    started = now()
    try:
        p = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        result = {"command": command, "started_at_utc": started, "finished_at_utc": now(),
                  "exit_code": p.returncode, "stdout": p.stdout, "stderr": p.stderr}
    except subprocess.TimeoutExpired as exc:
        result = {"command": command, "started_at_utc": started, "finished_at_utc": now(),
                  "exit_code": 124, "stdout": exc.stdout or "",
                  "stderr": (exc.stderr or "") + "\nTIMEOUT"}
    write_json(log_dir / f"{label}.json", result)
    return result


def verify_manifest(manifest: Path, base: Path) -> dict[str, Any]:
    checks = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        parts = line.strip().split(maxsplit=1)
        if len(parts) != 2:
            checks.append({"path": line, "status": "FAIL", "reason": "invalid SHA256SUMS line"})
            continue
        expected, relative = parts
        if relative.startswith("*"):
            relative = relative[1:]
        target = base / relative
        actual = sha256(target) if target.is_file() else None
        checks.append({"path": relative, "expected": expected, "actual": actual,
                       "status": "PASS" if actual == expected else "FAIL"})
    return {"status": "PASS" if checks and all(c["status"] == "PASS" for c in checks) else "FAIL",
            "checked_at_utc": now(), "checks": checks}


def inspect_ooxml(path: Path) -> dict[str, Any]:
    ext = path.suffix.lower()
    if ext not in REQUIRED:
        return {"status": "FAIL", "errors": ["unsupported OOXML extension"]}
    if not path.is_file() or not zipfile.is_zipfile(path):
        return {"status": "FAIL", "errors": ["missing file or invalid ZIP"]}
    errors: list[str] = []
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            bad_member = archive.testzip()
            if bad_member:
                errors.append(f"corrupt ZIP member: {bad_member}")
            for part in REQUIRED[ext]:
                if part not in names:
                    errors.append(f"required part missing: {part}")
            for name in sorted(n for n in names if n.endswith((".xml", ".rels"))):
                try:
                    ET.fromstring(archive.read(name))
                except ET.ParseError as exc:
                    errors.append(f"malformed XML {name}: {exc}")
            for rel_name in sorted(n for n in names if n.endswith(".rels")):
                try:
                    rel_root = ET.fromstring(archive.read(rel_name))
                    base = Path(".") if rel_name == "_rels/.rels" else Path(rel_name).parent.parent
                    for rel in rel_root.findall("rel:Relationship", NS):
                        if rel.attrib.get("TargetMode") == "External":
                            errors.append(f"external relationship prohibited: {rel_name}")
                            continue
                        target = rel.attrib.get("Target", "")
                        if target.startswith(("/", "http:", "https:")):
                            errors.append(f"absolute/external relationship prohibited: {rel_name} -> {target}")
                            continue
                        stack: list[str] = []
                        for part in (base / target).as_posix().split("/"):
                            if part == "..":
                                if stack:
                                    stack.pop()
                            elif part not in ("", "."):
                                stack.append(part)
                        resolved = "/".join(stack)
                        if resolved not in names:
                            errors.append(f"unresolved relationship: {rel_name} -> {target}")
                except ET.ParseError:
                    continue
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(str(exc))
    return {"status": "PASS" if not errors else "FAIL", "errors": errors,
            "sha256": sha256(path), "bytes": path.stat().st_size}


def xlsx_formula_snapshot(path: Path) -> dict[str, Any]:
    formulas = []
    with zipfile.ZipFile(path) as archive:
        for name in sorted(n for n in archive.namelist()
                           if n.startswith("xl/worksheets/") and n.endswith(".xml")):
            root = ET.fromstring(archive.read(name))
            for cell in root.findall(".//x:c", NS):
                formula, value = cell.find("x:f", NS), cell.find("x:v", NS)
                if formula is not None:
                    formulas.append({"worksheet_part": name, "cell": cell.attrib.get("r"),
                                     "formula": formula.text or "",
                                     "cached_value": value.text if value is not None else None})
    return {"sha256": sha256(path), "formulas": formulas}


def expected_sum_range(path: Path, worksheet_part: str, formula: str) -> float | None:
    """Evaluate the fixture's supported SUM(A1:B2) subset from source numeric cells."""
    match = re.fullmatch(r"SUM\(([A-Z]+[0-9]+):([A-Z]+[0-9]+)\)", formula.strip(), re.IGNORECASE)
    if not match:
        return None

    def coordinates(cell: str) -> tuple[int, int]:
        m = re.fullmatch(r"([A-Z]+)([0-9]+)", cell.upper())
        if not m:
            raise ValueError(f"Invalid A1 cell reference: {cell}")
        column = 0
        for char in m.group(1):
            column = column * 26 + ord(char) - 64
        return int(m.group(2)), column

    start_row, start_col = coordinates(match.group(1))
    end_row, end_col = coordinates(match.group(2))
    values: dict[tuple[int, int], float] = {}
    with zipfile.ZipFile(path) as archive:
        sheet = ET.fromstring(archive.read(worksheet_part))
        for cell in sheet.findall(".//x:c", NS):
            ref = cell.attrib.get("r", "")
            value = cell.find("x:v", NS)
            if not ref or value is None or value.text is None:
                continue
            try:
                values[coordinates(ref)] = float(value.text)
            except ValueError:
                continue
    total = 0.0
    for row in range(min(start_row, end_row), max(start_row, end_row) + 1):
        for col in range(min(start_col, end_col), max(start_col, end_col) + 1):
            total += values.get((row, col), 0.0)
    return total


def recalculate_xlsx(source: Path, output: Path, logs: Path) -> dict[str, Any]:
    binary = shutil.which("libreoffice") or shutil.which("soffice")
    if not binary:
        return {"status": "BLOCKED", "reason": "LibreOffice not installed"}
    if not source.is_file():
        return {"status": "FAIL", "reason": f"input missing: {source}"}
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="gdes-lo-recalc-") as temp:
        tmp = Path(temp)
        incoming, converted = tmp / "incoming", tmp / "converted"
        incoming.mkdir(); converted.mkdir()
        copy = incoming / "source.xlsx"
        copy.write_bytes(source.read_bytes())
        command = [binary, f"-env:UserInstallation={(tmp / 'profile').as_uri()}",
                   "--headless", "--convert-to", "xlsx", "--outdir", str(converted), str(copy)]
        result = command_log(command, logs, "libreoffice-recalculate")
        produced = converted / "source.xlsx"
        if result["exit_code"] != 0 or not produced.is_file():
            return {"status": "FAIL", "reason": "recalculated XLSX not produced", "command": result}
        destination = output / "recalculated.xlsx"
        shutil.copy2(produced, destination)
    before, after = xlsx_formula_snapshot(source), xlsx_formula_snapshot(destination)
    same_formula = [x["formula"] for x in before["formulas"]] == [x["formula"] for x in after["formulas"]]
    cache_present = bool(after["formulas"]) and all(x["cached_value"] is not None for x in after["formulas"])
    expected_checks = []
    for item in after["formulas"]:
        expected = expected_sum_range(source, item["worksheet_part"], item["formula"])
        cached = item["cached_value"]
        try:
            cached_number = float(cached) if cached is not None else None
        except (TypeError, ValueError):
            cached_number = None
        expected_checks.append({"cell": item["cell"], "formula": item["formula"],
                                "expected_value": expected, "cached_value": cached_number,
                                "status": "PASS" if expected is not None and cached_number is not None
                                and abs(expected - cached_number) < 1e-9 else "FAIL"})
    expected_match = bool(expected_checks) and all(x["status"] == "PASS" for x in expected_checks)
    details = {"before": before, "after": after, "output": str(destination),
               "formula_text_preserved": same_formula, "cached_values_present": cache_present,
               "expected_value_checks": expected_checks, "cached_values_match_expected": expected_match}
    try:
        from openpyxl import load_workbook
        formulas = load_workbook(destination, data_only=False, read_only=True)
        values = load_workbook(destination, data_only=True, read_only=True)
        cells = []
        for sheet in formulas.sheetnames:
            for row in formulas[sheet].iter_rows():
                for cell in row:
                    if isinstance(cell.value, str) and cell.value.startswith("="):
                        cells.append({"sheet": sheet, "cell": cell.coordinate,
                                      "formula": cell.value, "cached_value": values[sheet][cell.coordinate].value})
        details["spreadsheet_engine_values"] = cells
        formulas.close(); values.close()
    except ImportError:
        details["spreadsheet_engine_values"] = None
        details["note"] = "Install openpyxl to inspect cached values through a workbook reader."
    details["status"] = "PASS" if same_formula and cache_present and expected_match else "FAIL"
    return details


def render_office(source: Path, output: Path, logs: Path) -> dict[str, Any]:
    binary = shutil.which("libreoffice") or shutil.which("soffice")
    if not binary:
        return {"status": "BLOCKED", "reason": "LibreOffice not installed"}
    if not source.is_file():
        return {"status": "FAIL", "reason": f"input missing: {source}"}
    output.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="gdes-lo-render-") as temp:
        command = [binary, f"-env:UserInstallation={(Path(temp) / 'profile').as_uri()}",
                   "--headless", "--convert-to", "pdf", "--outdir", str(output), str(source)]
        result = command_log(command, logs, f"render-{source.stem}")
    pdf = output / f"{source.stem}.pdf"
    ok = result["exit_code"] == 0 and pdf.is_file() and pdf.stat().st_size > 500
    return {"status": "PASS" if ok else "FAIL", "command": result, "pdf": str(pdf),
            "pdf_sha256": sha256(pdf) if pdf.is_file() else None}


def inspect_pdf(pdf: Path) -> dict[str, Any]:
    try:
        import fitz
    except ImportError:
        return {"status": "BLOCKED", "reason": "PyMuPDF missing"}
    try:
        doc = fitz.open(pdf)
        pages = [{"page": i + 1, "text_chars": len(page.get_text().strip()),
                  "width": page.rect.width, "height": page.rect.height}
                 for i, page in enumerate(doc)]
        return {"status": "PASS" if pages and all(p["text_chars"] > 0 for p in pages) else "FAIL",
                "page_count": len(pages), "pages": pages}
    except Exception as exc:
        return {"status": "FAIL", "reason": str(exc)}


def render_pngs(pdf: Path, output: Path, logs: Path) -> dict[str, Any]:
    binary = shutil.which("pdftoppm")
    if not binary:
        return {"status": "BLOCKED", "reason": "Poppler pdftoppm missing"}
    output.mkdir(parents=True, exist_ok=True)
    result = command_log([binary, "-png", "-r", "144", str(pdf), str(output / pdf.stem)],
                         logs, f"png-{pdf.stem}")
    images = sorted(output.glob(f"{pdf.stem}-*.png"))
    return {"status": "PASS" if result["exit_code"] == 0 and images else "FAIL",
            "command": result,
            "images": [{"path": str(p), "sha256": sha256(p), "bytes": p.stat().st_size} for p in images]}


def visual_review_template(images: list[dict[str, Any]], path: Path) -> None:
    existing = []
    if path.is_file():
        try:
            existing = json.loads(path.read_text(encoding="utf-8")).get("reviewed_images", [])
        except (OSError, json.JSONDecodeError):
            existing = []
    merged = {item.get("path"): item for item in existing if item.get("path")}
    for item in images:
        if item.get("path"):
            merged[item["path"]] = {**item, "reviewed": False}
    write_json(path, {"review_status": "PENDING_HUMAN_REVIEW", "reviewer": "",
                      "reviewed_at_utc": None, "reviewed_images": list(merged.values()),
                      "findings": [], "approved": False,
                      "instruction": "Inspect every listed PNG manually before approval."})


def compare_reproducibility(a: dict[str, Any], b: dict[str, Any]) -> dict[str, Any]:
    keys = ("fixture_manifest_sha256", "formula_snapshot_sha256",
            "semantic_content_sha256", "page_count", "toolchain")
    differences = {k: {"run_a": a.get(k), "run_b": b.get(k)} for k in keys if a.get(k) != b.get(k)}
    return {"status": "PASS" if not differences else "FAIL", "differences": differences,
            "compared_at_utc": now(),
            "note": "PDF byte hashes may differ due to metadata; compare semantic and visual evidence."}


def write_hash_report(paths: list[Path], destination: Path, base: Path) -> dict[str, Any]:
    entries = []
    for path in paths:
        target = path if path.is_absolute() else base / path
        entries.append({"path": str(target), "sha256": sha256(target) if target.is_file() else None,
                        "status": "PASS" if target.is_file() else "FAIL"})
    report = {"status": "PASS" if entries and all(x["status"] == "PASS" for x in entries) else "FAIL",
              "generated_at_utc": now(), "files": entries}
    write_json(destination, report)
    return report


def write_evidence_manifest(evidence: Path) -> Path:
    destination = evidence / "evidence-manifest.sha256"
    lines = []
    for path in sorted(p for p in evidence.rglob("*")
                       if p.is_file() and p != destination and p.name != "evidence-audit.json"):
        lines.append(f"{sha256(path)}  {path.relative_to(evidence).as_posix()}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("\\n".join(lines) + "\\n", encoding="utf-8")
    return destination


def audit_evidence(evidence: Path) -> dict[str, Any]:
    required = ["execution", "integrity/input-sha256.json", "integrity/output-sha256.json",
                "formula/formulas-before-after.json", "rendering/docx", "rendering/pptx",
                "visual/visual-review.json", "reproducibility/comparison.json",
                "evidence-manifest.sha256"]
    missing = [p for p in required if not (evidence / p).exists()]
    review_path = evidence / "visual/visual-review.json"
    visual_ok = False
    if review_path.is_file():
        try:
            review = json.loads(review_path.read_text(encoding="utf-8"))
            reviewed = review.get("reviewed_images", [])
            visual_ok = (review.get("approved") is True and review.get("review_status") == "APPROVED"
                         and bool(review.get("reviewer")) and bool(review.get("reviewed_at_utc"))
                         and bool(reviewed) and all(item.get("reviewed") is True for item in reviewed))
        except (OSError, json.JSONDecodeError):
            pass
    manifest_path = evidence / "evidence-manifest.sha256"
    manifest_check = verify_manifest(manifest_path, evidence) if manifest_path.is_file() else {
        "status": "BLOCKED", "checks": []}
    report = {"status": "PASS" if not missing and visual_ok and manifest_check["status"] == "PASS" else "BLOCKED",
              "generated_at_utc": now(), "missing_evidence": missing,
              "manifest_verification": manifest_check,
              "human_visual_signoff": "PASS" if visual_ok else "BLOCKED",
              "candidate_execution_authorized": False}
    write_json(evidence / "audit/evidence-audit.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check-ooxml", nargs="*", type=Path, default=[])
    parser.add_argument("--recalculate", type=Path)
    parser.add_argument("--render", nargs="*", type=Path, default=[])
    parser.add_argument("--hash-inputs", nargs="*", type=Path, default=[])
    parser.add_argument("--hash-outputs", nargs="*", type=Path, default=[])
    parser.add_argument("--run-a", type=Path)
    parser.add_argument("--run-b", type=Path)
    parser.add_argument("--write-evidence-manifest", action="store_true")
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    root, evidence = args.root.resolve(), args.root.resolve() / "evidence"
    results = {"runner_version": "1.1.0", "created_at_utc": now(), "checks": []}
    for item in args.check_ooxml:
        path = item if item.is_absolute() else root / item
        results["checks"].append({"check": "ooxml_integrity", "path": str(path), **inspect_ooxml(path)})
    if args.recalculate:
        source = args.recalculate if args.recalculate.is_absolute() else root / args.recalculate
        formula_result = recalculate_xlsx(source, evidence / "formula/recalculated",
                                          evidence / "execution")
        write_json(evidence / "formula/formulas-before-after.json", formula_result)
        results["checks"].append({"check": "formula_recalculation", **formula_result})
    for item in args.render:
        source = item if item.is_absolute() else root / item
        rendered = render_office(source, evidence / f"rendering/{source.suffix[1:]}",
                                  evidence / "execution")
        if rendered.get("status") == "PASS":
            pdf = Path(rendered["pdf"])
            rendered["pdf_integrity"] = inspect_pdf(pdf)
            png = render_pngs(pdf, evidence / f"visual/{source.stem}", evidence / "execution")
            rendered["png_render"] = png
            if png.get("status") == "PASS":
                visual_review_template(png["images"], evidence / "visual/visual-review.json")
            if rendered["pdf_integrity"].get("status") != "PASS" or png.get("status") != "PASS":
                rendered["status"] = "BLOCKED" if "BLOCKED" in (
                    rendered["pdf_integrity"].get("status"), png.get("status")) else "FAIL"
        results["checks"].append({"check": "office_render", "source": str(source), **rendered})
    if args.hash_inputs:
        results["input_hash_report"] = write_hash_report(
            args.hash_inputs, evidence / "integrity/input-sha256.json", root)
    if args.hash_outputs:
        results["output_hash_report"] = write_hash_report(
            args.hash_outputs, evidence / "integrity/output-sha256.json", root)
    if args.run_a and args.run_b:
        a = json.loads(args.run_a.read_text(encoding="utf-8"))
        b = json.loads(args.run_b.read_text(encoding="utf-8"))
        write_json(evidence / "reproducibility/comparison.json", compare_reproducibility(a, b))
    write_json(evidence / "runner-results.json", results)
    if args.write_evidence_manifest:
        write_evidence_manifest(evidence)
    if args.audit:
        report = audit_evidence(evidence)
        print(json.dumps(report, indent=2))
        return 0 if report["status"] == "PASS" else 2
    print(json.dumps(results, indent=2))
    if any(x.get("status") == "FAIL" for x in results["checks"]):
        return 1
    if any(x.get("status") == "BLOCKED" for x in results["checks"]):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
