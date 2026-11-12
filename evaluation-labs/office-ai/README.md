# GDES-OFFICE-001 — Isolated Office AI Evaluation Harness

Status: **Experimental / Not Approved**  
Scope: Pi for Excel, GenOffice, and Office Agent Skills.  
Execution policy: synthetic data only; no production documents, credentials, paid APIs, or global installs.

## Objective

Compare candidate-produced Office files against a common, deterministic fixture set. The harness generates minimal OOXML DOCX, XLSX, and PPTX inputs using Python's standard library, records SHA-256 hashes, and validates candidate output packages without installing or invoking candidate software.

## Candidate capability coverage

| Candidate | XLSX | DOCX | PPTX | Notes |
|---|---:|---:|---:|---|
| Pi for Excel | Common comparison | — | — | Spreadsheet-only comparison; do not infer Word/PowerPoint capability |
| GenOffice | Common comparison | Extended | Extended | Candidate invocation is a separately authorized/manual step |
| Office Agent Skills | Common comparison | Extended | Extended | Candidate invocation is a separately authorized/manual step |

The XLSX fixture is the common denominator for all three candidates. DOCX and PPTX are an extended comparison between GenOffice and Office Agent Skills.

## Safety boundary

- The harness never installs or executes candidate repositories, scripts, plugins, or skills.
- It does not call external APIs, use network access, read environment credentials, or send documents to a provider.
- Candidate execution is manual and must use synthetic fixtures only.
- Do not place secrets, real contracts, personal data, financial records, or confidential company documents in this lab.
- Do not enable macros, external links, embedded objects, or remote relationships in fixtures.
- Candidate output is untrusted. Inspect it in a disposable environment before opening it in a desktop Office application.
- This harness validates package structure and selected content invariants; it does not prove visual fidelity, formula recalculation, security, privacy, legal correctness, or Syariah compliance.

## Requirements

- Python 3.11+
- No third-party Python dependencies

## Prepare the common fixture bundle

From this directory:

```bash
python tools/office_ai_harness.py prepare --output-dir .artifacts/office-ai
```

The command creates:
- `.artifacts/office-ai/inputs/common.xlsx`
- `.artifacts/office-ai/inputs/common.docx`
- `.artifacts/office-ai/inputs/common.pptx`
- `.artifacts/office-ai/fixture-manifest.json`

The fixture manifest records SHA-256 hashes. Compare the XLSX input hash across every candidate run to ensure identical inputs.

## Candidate execution protocol

Candidate execution is intentionally not automated by this repository.

1. Generate the fixture bundle once.
2. Give each candidate the exact same `common.xlsx` bytes and the task brief in the manifest.
3. For GenOffice and Office Agent Skills, also provide the same `common.docx` and `common.pptx` bytes.
4. Ask each candidate to preserve all required content and the XLSX formula while applying the task brief.
5. Export outputs to a separate folder using these exact names:
   - `results/pi-for-excel/common.xlsx`
   - `results/genoffice/common.xlsx`, `common.docx`, `common.pptx`
   - `results/office-agent-skills/common.xlsx`, `common.docx`, `common.pptx`
6. Record candidate version, invocation, provider/model (if any), date, operator, and whether network/API access was used. Never record credentials.
7. Run the verifier below.

## Verify candidate outputs

```bash
python tools/office_ai_harness.py verify --bundle-dir .artifacts/office-ai --results-dir results
```

The verifier reports each candidate/file as:
- `PASS`: package is structurally readable and required content invariants are present;
- `FAIL`: output exists but package or required invariants are invalid;
- `NOT_RUN`: expected output is absent.

A candidate is not accepted merely because this verifier passes. Visual rendering, formula recalculation in a real spreadsheet engine, security/privacy review, reproducibility, and human review remain separate gates.

## Run harness unit tests

```bash
python -m unittest discover -s tests -v
```

## Acceptance criteria

- [ ] Fixture generation is deterministic for the same harness version.
- [ ] Each generated Office package is a valid ZIP with well-formed XML parts.
- [ ] XLSX formula `SUM(B2:B3)` remains present in candidate output.
- [ ] Required synthetic content survives candidate transformation.
- [ ] All candidates receive byte-identical XLSX input (same SHA-256).
- [ ] Missing outputs are reported as `NOT_RUN`, never as PASS.
- [ ] No candidate code is executed by the harness.
- [ ] Runtime, visual, dependency, privacy, and reproducibility evidence is attached separately.

## Current status

This commit adds the fixture generator, structural verifier, tests, and CI check only. No candidate runtime invocation has been performed. No candidate is approved for adoption.
