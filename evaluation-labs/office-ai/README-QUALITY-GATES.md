# GDES-REG-002 Local Office Quality Gates

Status: **Experimental / Not Approved**. This extension adds local quality gates to the isolated evaluation-labs/office-ai harness. It does not change candidate source and does not execute GenOffice, Office Agent Skills, or Pi for Excel.

## Safety boundary

- No company application repository is accessed or changed.
- Candidate repositories and source snapshots remain read-only.
- No candidate runtime, plugin, skill, or model is invoked by this runner.
- No paid API, cloud inference, external search, or network call is used.
- LibreOffice and Poppler are local document-processing dependencies only.
- All input data must be synthetic.
- Candidate outputs remain untrusted; inspect in a disposable environment.

## Local prerequisites

- Python 3.11+
- LibreOffice (libreoffice or soffice)
- Poppler (pdftoppm, package commonly named poppler-utils)
- Optional Python packages: openpyxl and PyMuPDF

Install optional packages in a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install openpyxl PyMuPDF
libreoffice --version
pdftoppm -v
```

## Prepare common synthetic fixtures

From evaluation-labs/office-ai:

```bash
python tools/office_ai_harness.py prepare --output-dir .artifacts/office-ai
```

## Run local quality gates

```bash
python tools/office_ai_quality_gate.py \
  --root . \
  --check-ooxml \
    .artifacts/office-ai/inputs/common.xlsx \
    .artifacts/office-ai/inputs/common.docx \
    .artifacts/office-ai/inputs/common.pptx \
  --recalculate .artifacts/office-ai/inputs/common.xlsx \
  --render \
    .artifacts/office-ai/inputs/common.docx \
    .artifacts/office-ai/inputs/common.pptx
```

The runner writes command JSON logs (including exact argv, stdout, stderr, timestamps, and exit codes), formula snapshots, recalculated XLSX, PDFs, PNGs, and a pending human visual review template under evidence/.

## Evidence requirements

The Standards Owner evidence package must contain:

1. Execution logs and exit codes for every local command.
2. SHA-256 manifests for all fixture inputs and generated outputs.
3. XLSX formulas before and after recalculation plus cached values.
4. DOCX and PPTX rendered PDFs, PDF integrity reports, and page PNGs.
5. evidence/visual/visual-review.json completed by a human reviewer, with reviewer identity, review timestamp, every PNG listed, findings, review_status APPROVED, and approved true.
6. Two run reports and a reproducibility comparison. Compare fixture hash, formula snapshot, semantic content, page count, and toolchain. PDF byte hashes may differ because of metadata; explain such differences rather than silently ignoring them.
7. Evidence manifest and audit report.

The visual template is deliberately created with approved false. The runner does not and cannot sign off visual quality on behalf of a human reviewer.

## Evidence audit

The evidence audit is intentionally fail-closed. It returns BLOCKED when required evidence is absent or the visual reviewer has not approved every rendered page. A passing local harness test is not proof of successful LibreOffice execution, candidate quality, security, privacy, legal correctness, or Syariah compliance.

Candidate execution is a separate future authorization and is never enabled by this tool. All three candidates must remain NOT_RUN until the Standards Owner approves runner readiness and separately authorizes candidate execution.
