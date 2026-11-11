#!/usr/bin/env python3
"""Offline fixture generator and structural verifier for GDES-OFFICE-001.

Only Python's standard library is used. Candidate software is never executed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "x": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
    "p": "http://schemas.openxmlformats.org/presentationml/2006/main",
}
TASK_BRIEF = (
    "Improve readability and basic formatting without changing factual content. "
    "For XLSX, preserve the formula SUM(B2:B3) and its result. "
    "For DOCX and PPTX, preserve the title and all listed facts verbatim."
)
CANDIDATES = {
    "pi-for-excel": ("common.xlsx",),
    "genoffice": ("common.xlsx", "common.docx", "common.pptx"),
    "office-agent-skills": ("common.xlsx", "common.docx", "common.pptx"),
}
REQUIRED_TEXT = {
    "common.docx": ("GDES Synthetic Office Fixture", "Batch: DEMO-001", "Quantity: 10", "Unit price: 15"),
    "common.pptx": ("GDES Synthetic Office Fixture", "Batch: DEMO-001", "Quantity: 10", "Unit price: 15"),
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_package(path: Path, parts: dict[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for name, content in sorted(parts.items()):
            archive.writestr(name, content)


def docx_parts() -> dict[str, str]:
    return {
        "[Content_Types].xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>""",
        "_rels/.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>""",
        "word/document.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"><w:body>
<w:p><w:r><w:t>GDES Synthetic Office Fixture</w:t></w:r></w:p>
<w:p><w:r><w:t>Batch: DEMO-001</w:t></w:r></w:p>
<w:p><w:r><w:t>Quantity: 10</w:t></w:r></w:p>
<w:p><w:r><w:t>Unit price: 15</w:t></w:r></w:p>
<w:sectPr/></w:body></w:document>""",
    }


def xlsx_parts() -> dict[str, str]:
    return {
        "[Content_Types].xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/xl/workbook.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml"/>
<Override PartName="/xl/worksheets/sheet1.xml" ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml"/>
</Types>""",
        "_rels/.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="xl/workbook.xml"/>
</Relationships>""",
        "xl/workbook.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<workbook xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><sheets><sheet name="Fixture" sheetId="1" r:id="rId1"/></sheets></workbook>""",
        "xl/_rels/workbook.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet1.xml"/>
</Relationships>""",
        "xl/worksheets/sheet1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main"><sheetData>
<row r="1"><c r="A1" t="inlineStr"><is><t>GDES Synthetic Office Fixture</t></is></c></row>
<row r="2"><c r="A2" t="inlineStr"><is><t>Batch: DEMO-001</t></is></c><c r="B2"><v>10</v></c></row>
<row r="3"><c r="A3" t="inlineStr"><is><t>Unit price</t></is></c><c r="B3"><v>15</v></c></row>
<row r="4"><c r="A4" t="inlineStr"><is><t>Total</t></is></c><c r="B4"><f>SUM(B2:B3)</f><v>25</v></c></row>
</sheetData></worksheet>""",
    }


def pptx_parts() -> dict[str, str]:
    return {
        "[Content_Types].xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/ppt/presentation.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml"/>
<Override PartName="/ppt/slides/slide1.xml" ContentType="application/vnd.openxmlformats-officedocument.presentationml.slide+xml"/>
</Types>""",
        "_rels/.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="ppt/presentation.xml"/>
</Relationships>""",
        "ppt/presentation.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:presentation xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><p:sldIdLst><p:sldId id="256" r:id="rId1"/></p:sldIdLst><p:sldSz cx="9144000" cy="5143500"/></p:presentation>""",
        "ppt/_rels/presentation.xml.rels": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/slide" Target="slides/slide1.xml"/>
</Relationships>""",
        "ppt/slides/slide1.xml": """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<p:sld xmlns:p="http://schemas.openxmlformats.org/presentationml/2006/main" xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><p:cSld><p:spTree>
<p:nvGrpSpPr><p:cNvPr id="1" name=""/><p:cNvGrpSpPr/><p:nvPr/></p:nvGrpSpPr><p:grpSpPr/>
<p:sp><p:nvSpPr><p:cNvPr id="2" name="Title"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/><a:p><a:r><a:rPr/><a:t>GDES Synthetic Office Fixture</a:t></a:r></a:p></p:txBody></p:sp>
<p:sp><p:nvSpPr><p:cNvPr id="3" name="Details"/><p:cNvSpPr/><p:nvPr/></p:nvSpPr><p:spPr/><p:txBody><a:bodyPr/><a:lstStyle/>
<a:p><a:r><a:rPr/><a:t>Batch: DEMO-001</a:t></a:r></a:p>
<a:p><a:r><a:rPr/><a:t>Quantity: 10</a:t></a:r></a:p>
<a:p><a:r><a:rPr/><a:t>Unit price: 15</a:t></a:r></a:p>
</p:txBody></p:sp></p:spTree></p:cSld></p:sld>""",
    }


def xml_text_from_package(path: Path) -> str:
    chunks: list[str] = []
    with zipfile.ZipFile(path) as archive:
        bad_member = archive.testzip()
        if bad_member:
            raise ValueError(f"Corrupt ZIP member: {bad_member}")
        for name in archive.namelist():
            if name.endswith(".xml"):
                raw = archive.read(name)
                root = ET.fromstring(raw)
                chunks.extend(root.itertext())
    return " ".join(chunks)


def validate_package(path: Path, filename: str) -> list[str]:
    errors: list[str] = []
    if not path.is_file():
        return ["output missing"]
    if not zipfile.is_zipfile(path):
        return ["not a ZIP/OOXML package"]
    try:
        text = xml_text_from_package(path)
    except (zipfile.BadZipFile, ET.ParseError, OSError, ValueError) as exc:
        return [f"package/XML invalid: {exc}"]

    if filename == "common.xlsx":
        try:
            with zipfile.ZipFile(path) as archive:
                sheet = ET.fromstring(archive.read("xl/worksheets/sheet1.xml"))
            formulas = [node.text or "" for node in sheet.findall(".//x:f", NS)]
            if "SUM(B2:B3)" not in formulas:
                errors.append("required formula SUM(B2:B3) missing")
            if "GDES Synthetic Office Fixture" not in text or "DEMO-001" not in text:
                errors.append("required XLSX fixture text missing")
        except (KeyError, ET.ParseError, zipfile.BadZipFile) as exc:
            errors.append(f"worksheet validation failed: {exc}")
    elif filename in REQUIRED_TEXT:
        for required in REQUIRED_TEXT[filename]:
            if required not in text:
                errors.append(f"required text missing: {required}")
    return errors


def prepare(output_dir: Path) -> dict:
    inputs = output_dir / "inputs"
    builders = {
        "common.docx": docx_parts,
        "common.xlsx": xlsx_parts,
        "common.pptx": pptx_parts,
    }
    for filename, builder in builders.items():
        write_package(inputs / filename, builder())
    manifest = {
        "schema_version": 1,
        "evaluation": "GDES-OFFICE-001",
        "data_classification": "synthetic-public-demo",
        "task_brief": TASK_BRIEF,
        "candidate_coverage": {name: list(files) for name, files in CANDIDATES.items()},
        "fixtures": {
            filename: {
                "path": f"inputs/{filename}",
                "sha256": sha256(inputs / filename),
                "bytes": (inputs / filename).stat().st_size,
            }
            for filename in sorted(builders)
        },
        "limitations": [
            "Package-level OOXML/XML checks only; no visual rendering assertion.",
            "No formula recalculation engine is invoked.",
            "Candidate tools are never installed or executed by this harness.",
        ],
    }
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "fixture-manifest.json").write_text(
        json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def verify(bundle_dir: Path, results_dir: Path) -> dict:
    manifest_path = bundle_dir / "fixture-manifest.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Missing fixture manifest: {manifest_path}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    report = {
        "schema_version": 1,
        "evaluation": "GDES-OFFICE-001",
        "candidates": {},
        "input_hashes": {},
    }
    for filename, details in manifest["fixtures"].items():
        input_path = bundle_dir / details["path"]
        actual_hash = sha256(input_path) if input_path.is_file() else None
        report["input_hashes"][filename] = {
            "expected": details["sha256"],
            "actual": actual_hash,
            "match": actual_hash == details["sha256"],
        }

    for candidate, filenames in CANDIDATES.items():
        candidate_report = {}
        for filename in filenames:
            output_path = results_dir / candidate / filename
            errors = validate_package(output_path, filename)
            candidate_report[filename] = {
                "status": "NOT_RUN" if errors == ["output missing"] else ("FAIL" if errors else "PASS"),
                "sha256": sha256(output_path) if output_path.is_file() else None,
                "errors": errors,
            }
        report["candidates"][candidate] = candidate_report
    report["overall_status"] = (
        "FAIL" if any(
            item["status"] == "FAIL"
            for candidate in report["candidates"].values()
            for item in candidate.values()
        )
        else "NOT_RUN" if any(
            item["status"] == "NOT_RUN"
            for candidate in report["candidates"].values()
            for item in candidate.values()
        )
        else "STRUCTURAL_CHECKS_ONLY"
    )
    return report


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    prepare_parser = sub.add_parser("prepare", help="generate deterministic synthetic OOXML fixtures")
    prepare_parser.add_argument("--output-dir", type=Path, required=True)
    verify_parser = sub.add_parser("verify", help="verify candidate-produced OOXML outputs")
    verify_parser.add_argument("--bundle-dir", type=Path, required=True)
    verify_parser.add_argument("--results-dir", type=Path, required=True)
    args = parser.parse_args(argv)

    if args.command == "prepare":
        manifest = prepare(args.output_dir)
        print(json.dumps(manifest, indent=2))
        return 0
    report = verify(args.bundle_dir, args.results_dir)
    print(json.dumps(report, indent=2))
    return 1 if report["overall_status"] == "FAIL" else 0


if __name__ == "__main__":
    sys.exit(main())
