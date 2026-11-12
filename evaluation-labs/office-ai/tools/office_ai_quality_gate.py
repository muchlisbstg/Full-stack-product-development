#!/usr/bin/env python3
"""Local-only Office quality gates for GDES-REG-002.

This module never invokes candidate software, model endpoints, or network APIs.
LibreOffice and Poppler are invoked only as local document-processing tools.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence"
NS_MAIN = {
    "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
    "rel": "http://schemas.openxmlformats.org/package/2006/relationships",
}
REQUIRED_OOXML = {
    ".xlsx": ("[Content_Types].xml", "_rels/.rels", "xl/workbook.xml"),
    ".docx": ("[Content_Types].xml", "_rels/.rels", "word/document.xml"),
    ".pptx": ("[Content_Types].xml", "_rels/.rels", "ppt/presentation.xml"),
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def run_command(command: list[str], log_dir: Path, label: str, timeout: int = 180) -> dict[str, Any]:
    log_dir.mkdir(parents=True, exist_ok=True)
    started = utc_now()
    try:
        proc = subprocess.run(command, capture_output=True, text=True, timeout=timeout, check=False)
        result = {
            "command": command, "started_at_utc": started, "finished_at_utc": utc_now(),
            "exit_code": proc.returncode, "stdout": proc.stdout, "stderr": proc.stderr,
        }
    except subprocess.TimeoutExpired as exc:
        result = {
            "command": command, "started_at_utc": started, "finished_at_utc": utc_now(),
            "exit_code": 124, "stdout": exc.stdout or "", "stderr": (exc.stderr or "") + "\nTIMEOUT",
        }
    write_json(log_dir / f"{label}.json", result)
    return result


def verify_manifest(manifest_path: Path, base_dir: Path) -> dict[str, Any]:
    checks = []
    for line in manifest_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        expected, rel = line.split("  ", 1)
        target = base_dir / rel
        actual = sha256(target) if target.is_file() else None
        checks.append({"path": rel, "expected_sha256": expected, "actual_sha256": actual,
                       "status": "PASS" if actual == expected else "FAIL"})
    return {"status": "PASS" if checks and all(x["status"] == "PASS" for x in checks) else "FAIL",
            "checked_at_utc": utc_now(), "checks": checks}


def inspect_ooxml(path: Path) -> dict[str, Any]:
    if path.suffix.lower() not in REQUIRED_OOXML:
        return {"status": "FAIL", "errors": ["unsupported extension"]}
    errors: list[str] = []
    if not path.is_file() or not zipfile.is_zipfile(path):
        return {"status": "FAIL", "errors": ["missing file or invalid ZIP"]}
    try:
        with zipfile.ZipFile(path) as archive:
            names = set(archive.namelist())
            bad = archive.testzip()
            if bad:
                errors.append(f"corrupt ZIP member: {bad}")
            for required in REQUIRED_OOXML[path.suffix.lower()]:
                if required not in names:
                    errors.append(f"required OOXML part missing: {required}")
            for name in sorted(names):
                if name.endswith((".xml", ".rels")):
                    try:
                        ET.fromstring(archive.read(name))
                    except ET.ParseError as exc:
                        errors.append(f"invalid XML {name}: {exc}")
            # Relationship targets must resolve within the package.
            for rel_name in sorted(n for n in names if n.endswith(".rels")):
                try:
                    rel_root = ET.fromstring(archive.read(rel_name))
                    for rel in rel_root.findall("rel:Relationship", NS_MAIN):
                        target = rel.attrib.get("Target", "")
                        if target.startswith(("http://", "https://", "/")):
                            continue
                        parent = Path(rel_name).parent
                        resolved = (parent / target).as_posix()
                        parts = []
                        for item in resolved.split("/"):
                            if item == "..":
                                if parts:
                                    parts.pop()
                            elif item not in ("", "."):
                                parts.append(item)
                        normalized = "/".join(parts)
                        if normalized not in names:
                            errors.append(f"unresolved relationship {rel_name} -> {target}")
                except ET.ParseError:
                    pass
    except (OSError, zipfile.BadZipFile) as exc:
        errors.append(str(exc))
    return {"status": "PASS" if not errors else "FAIL", "errors": errors,
            "sha256": sha256(path), "bytes": path.stat().st_size}


def xlsx_formula_snapshot(path: Path) -> dict[str, Any]:
    formulas: list[dict[str, Any]] = []
    with zipfile.ZipFile(path) as archive:
        for name in sorted(n for n in archive.namelist()
                           if n.startswith("xl/worksheets/") and n.endswith(".xml")):
            root = ET.fromstring(archive.read(name))
            for cell in root.findall(".//x:c", NS_MAIN):
                formula = cell.find("x:f", NS_MAIN)
                value = cell.find("x:v", NS_MAIN)
                if formula is not None:
                    formulas.append({
                        "worksheet_part": name, "cell": cell.attrib.get("r"),
                        "formula": formula.text or "",
                        "cached_value": value.text if value is not None else None,
                        "cell_type": cell.attrib.get("t"),
                    })
    return {"path": str(path), "sha256": sha256(path), "formulas": formulas}


def find_libreoffice() -> str | None:
    return shutil.which("libreoffice") or shutil.which("soffice")


def recalculate_xlsx(source: Path, output_dir: Path, logs: Path) -> dict[str, Any]:
    binary = find_libreoffice()
    if not binary:
        return {"status": "BLOCKED", "reason": "LibreOffice executable not found"}
    if not source.is_file():
        return {"status": "FAIL", "reason": f"input missing: {source}"}
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="gdes-lo-recalc-") as temp:
        temp_path = Path(temp)
        input_copy = temp_path / "input.xlsx"
        input_copy.write_bytes(source.read_bytes())
        converted = temp_path / "converted"
        converted.mkdir()
        profile = temp_path / "profile"
        command = [
            binary, f"-env:UserInstallation={profile.as_uri()}",
            "--headless", "--convert-to", "xlsx", "--outdir", str(converted), str(input_copy),
        ]
        result = run_command(command, logs, "libreoffice-recalculate")
        produced = converted / "input.xlsx"
        if result["exit_code"] != 0 or not produced.is_file():
            return {"status": "FAIL", "command_result": result, "reason": "recalculated XLSX not produced"}
        destination = output_dir / "recalculated.xlsx"
        shutil.copy2(produced, destination)
    before = xlsx_formula_snapshot(source)
    after = xlsx_formula_snapshot(destination)
    details: dict[str, Any] = {"before": before, "after": after, "output": str(destination)}
    try:
        from openpyxl import load_workbook
        wb_formula = load_workbook(destination, data_only=False, read_only=True)
        wb_values = load_workbook(destination, data_only=True, read_only=True)
        formula_cells = []
        for sheet_name in wb_formula.sheetnames:
            fs, vs = wb_formula[sheet_name], wb_values[sheet_name]
            for row in fs.iter_rows():
                for cell in row:
                    if isinstance(cell.value, str) and cell.value.startswith("="):
                        formula_cells.append({"sheet": sheet_name, "cell": cell.coordinate,
                                              "formula": cell.value,
                                              "cached_value": vs[cell.coordinate].value})
        details["openpyxl_formula_cells"] = formula_cells
        wb_formula.close()
        wb_values.close()
    except ImportError:
        details["openpyxl_formula_cells"] = None
        details["note"] = "Install openpyxl to read cached values through a spreadsheet library."
    formula_same = [x["formula"] for x in before["formulas"]] == [x["formula"] for x in after["formulas"]]
    cached_present = bool(after["formulas"]) and all(x["cached_value"] is not None for x in after["formulas"])
    details["status"] = "PASS" if formula_same and cached_present else "FAIL"
    details["formula_text_preserved"] = formula_same
    details["cached_values_present"] = cached_present
    return details


def render_office(source: Path, output_dir: Path, logs: Path) -> dict[str, Any]:
    binary = find_libreoffice()
    if not binary:
        return {"status": "BLOCKED", "reason": "LibreOffice executable not found"}
    if not source.is_file():
        return {"status": "FAIL", "reason": f"input missing: {source}"}
    output_dir.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="gdes-lo-render-") as temp:
        profile = (Path(temp) / "profile").as_uri()
        command = [binary, f"-env:UserInstallation={profile}", "--headless",
                   "--convert-to", "pdf", "--outdir", str(output_dir), str(source)]
        result = run_command(command, logs, f"render-{source.stem}")
    pdf = output_dir / f"{source.stem}.pdf"
    ok = result["exit_code"] == 0 and pdf.is_file() and pdf.stat().st_size > 500
    return {"status": "PASS" if ok else "FAIL", "command_result": result,
            "pdf": str(pdf), "pdf_sha256": sha256(pdf) if pdf.is_file() else None,
            "pdf_bytes": pdf.stat().st_size if pdf.is_file() else 0}


def inspect_pdf(pdf: Path) -> dict[str, Any]:
    try:
        import fitz
    except ImportError:
        return {"status": "BLOCKED", "reason": "PyMuPDF missing; install requirements"}
    try:
        doc = fitz.open(pdf)
        pages = [{"page": i + 1, "text_chars": len(page.get_text().strip()),
                  "width": page.rect.width, "height": page.rect.height}
                 for i, page in enumerate(doc)]
        ok = len(pages) > 0 and all(p["text_chars"] > 0 for p in pages)
        return {"status": "PASS" if ok else "FAIL", "pages": pages, "page_count": len(pages)}
    except Exception as exc:
        return {"status": "FAIL", "reason": str(exc)}


def render_pngs(pdf: Path, output_dir: Path, logs: Path) -> dict[str, Any]:
    binary = shutil.which("pdftoppm")
    if not binary:
        return {"status": "BLOCKED", "reason": "pdftoppm missing; install poppler-utils"}
    output_dir.mkdir(parents=True, exist_ok=True)
    prefix = output_dir / pdf.stem
    result = run_command([binary, "-png", "-r", "144", str(pdf), str(prefix)], logs,
                         f"png-{pdf.stem}")
    images = sorted(output_dir.glob(f"{pdf.stem}-*.png"))
    return {"status": "PASS" if result["exit_code"] == 0 and images else "FAIL",
            "command_result": result,
            "images": [{"path": str(p), "sha256": sha256(p), "bytes": p.stat().st_size} for p in images]}


def visual_review_template(images: list[dict[str, Any]], path: Path) -> None:
    write_json(path, {
        "review_status": "PENDING_HUMAN_REVIEW", "reviewer": "",
        "reviewed_at_utc": None, "reviewed_images": images,
        "findings": [], "approved": False,
        "review_instruction": "A human must open and inspect every listed PNG before setting approved=true.",
    })


def compare_reproducibility(run_a: dict[str, Any], run_b: dict[str, Any]) -> dict[str, Any]:
    keys = ("fixture_manifest_sha256", "formula_snapshot_sha256", "semantic_content_sha256",
            "page_count", "toolchain")
    differences = {key: {"run_a": run_a.get(key), "run_b": run_b.get(key)}
                   for key in keys if run_a.get(key) != run_b.get(key)}
    return {"status": "PASS" if not differences else "FAIL",
            "compared_at_utc": utc_now(), "differences": differences,
            "note": "Compare semantic/document evidence; PDF byte hashes may vary due to metadata."}


def audit_evidence(evidence_root: Path) -> dict[str, Any]:
    required = [
        "execution/commands", "integrity/input-sha256.json", "integrity/output-sha256.json",
        "formula/formulas-before-after.json", "rendering/docx", "rendering/pptx",
        "visual/visual-review.json", "reproducibility/comparison.json",
    ]
    missing = [item for item in required if not (evidence_root / item).exists()]
    review_path = evidence_root / "visual/visual-review.json"
    visual_ok = False
    if review_path.is_file():
        try:
            review = json.loads(review_path.read_text(encoding="utf-8"))
            visual_ok = review.get("approved") is True and review.get("review_status") == "APPROVED"
            if not review.get("reviewer") or not review.get("reviewed_images"):
                visual_ok = False
        except (OSError, json.JSONDecodeError):
            pass
    report = {"status": "PASS" if not missing and visual_ok else "BLOCKED",
              "generated_at_utc": utc_now(), "missing_evidence": missing,
              "human_visual_signoff": "PASS" if visual_ok else "BLOCKED",
              "candidate_execution_authorized": False}
    write_json(evidence_root / "audit/evidence-audit.json", report)
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check-ooxml", nargs="*", type=Path, default=[])
    parser.add_argument("--recalculate", type=Path)
    parser.add_argument("--render", nargs="*", type=Path, default=[])
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    ev = root / "evidence"
    results: dict[str, Any] = {"runner_version": "1.1.0", "created_at_utc": utc_now(), "checks": []}
    for rel in args.check_ooxml:
        path = rel if rel.is_absolute() else root / rel
        result = inspect_ooxml(path)
        results["checks"].append({"check": "ooxml_integrity", "path": str(path), **result})
    if args.recalculate:
        source = args.recalculate if args.recalculate.is_absolute() else root / args.recalculate
        results["checks"].append({"check": "formula_recalculation",
                                  **recalculate_xlsx(source, ev / "formula/recalculated", ev / "execution")})
    for rel in args.render:
        source = rel if rel.is_absolute() else root / rel
        rendered = render_office(source, ev / f"rendering/{source.suffix[1:]}", ev / "execution")
        if rendered.get("status") == "PASS":
            pdf = Path(rendered["pdf"])
            rendered["pdf_integrity"] = inspect_pdf(pdf)
            png_result = render_pngs(pdf, ev / f"visual/{source.stem}", ev / "execution")
            rendered["png_render"] = png_result
            if png_result.get("status") == "PASS":
                review_file = ev / "visual/visual-review.json"
                visual_review_template(png_result["images"], review_file)
        results["checks"].append({"check": "office_render", "source": str(source), **rendered})
    write_json(ev / "runner-results.json", results)
    if args.audit:
        report = audit_evidence(ev)
        print(json.dumps(report, indent=2))
        return 0 if report["status"] == "PASS" else 2
    print(json.dumps(results, indent=2))
    return 1 if any(x.get("status") == "FAIL" for x in results["checks"]) else 0


if __name__ == "__main__":
    sys.exit(main())
