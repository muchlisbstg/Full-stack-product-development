# GDES Cybersecurity Findings Register v1.0 — Draft

**Register ID:** GDES-SEC-FND-001  
**Branch:** `gdes/ai-governance-v1-pilot`  
**Status:** Draft — Findings Open — Not Approved  
**Evidence baseline:** GitHub Actions run [42972384713](https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/42972384713), generated commit `7e06abbe46960e02c0bdd583111575eb96116207`.

## 1. Purpose and rules

This register tracks source-mapping, governance, database, and operational-security findings that prevent the Cybersecurity Gate from being cleared.

- A source mapping is not a GDES PASS.
- A candidate mapping is not an approved control interpretation.
- A missing test is not silently treated as a pass.
- A finding is closed only with source evidence, remediation evidence, and independent disposition where required.
- Retest evidence must identify repository, branch, commit SHA, environment, test procedure, result, and reviewer.
- No finding may be closed by changing a status label without evidence.

## 2. Findings

| ID | Severity | Finding | Evidence / current state | Required closure evidence | Status |
|---|---|---|---|---|---|
| GDES-FND-SEC-001 | Major | MASTG beta weakness `MASWE-0097` has no stable target in the official MASWE v1.0.0 release asset. | Four tests reference it: MASTG-TEST-0324, 0325, 0240, 0241. MASWE-0051 is a semantic candidate only; not source-mapped. | Obtain authoritative source correction or explicit reviewer/Standards Owner disposition; update alias crosswalk and rerun extraction. | OPEN |
| GDES-FND-SEC-002 | Moderate | Seven beta aliases map to multiple stable MASWE targets. | Official release asset lists multi-target mappings for MASWE-0002, 0012, 0013, 0032, 0059, 0108, 0109. | Security Reviewer confirms all target relationships and their applicability; retain exact source mapping and record any approved exclusions with rationale. | OPEN |
| GDES-FND-SEC-003 | Moderate | Stable MASWE weaknesses without MASTG test links exceed the published count by two. | Extractor finds 38 stable weaknesses without linked tests; MASWE v1.0.0 release article reports 36. | Reconcile the exact two additional IDs against the release source and test catalogue; record whether source drift, scope, or extraction logic explains the delta. | OPEN |
| GDES-FND-SEC-004 | Moderate | MASTG test inventory count differs from the v2.0.0 release announcement. | Pinned tree contains 292 unique test Markdown paths: 200 structured v2 tests and 92 legacy paths; release announcement reports 285 tests. | Identify and disposition the seven-path difference; preserve legacy paths and state the precise scope used for any published test count. | OPEN |
| GDES-FND-MAP-001 | Major | ASVS requirement mappings include chapter-level candidate fallback. | All 345 ASVS v5.0.0 requirements are catalogued and candidate-mapped; zero rows are unmapped. Some rows are chapter candidates, not direct section-range matches. | Independent Security Reviewer validates requirement-to-control applicability and records exceptions; Standards Owner approves the final crosswalk. | OPEN |
| GDES-FND-MAP-002 | Major | TCASVS mapping is chapter-based at requirement-row level. | All 132 TCASVS v5.0.0 requirements are individually catalogued with chapter-based candidate controls. | Independent Security Reviewer validates each requirement's target controls and applicability; record unmapped or partial relationships explicitly. | OPEN |
| GDES-FND-MAP-003 | Moderate | SAMM activity-level links are candidate mappings, not maturity evidence. | 90 activity GUIDs and 90 questions extracted; all activities have linked questions. Practice-code-to-GDES relationships remain candidate links. | Independent Security Reviewer reviews each activity/control relationship; do not infer SAMM maturity scores or GDES compliance from catalogue presence. | OPEN |
| GDES-FND-DB-001 | Gate blocker | Database security controls have not been proven in runtime. | PostgreSQL RLS, FORCE RLS/BYPASSRLS, composite tenant FKs, transaction isolation, concurrency, temporal consistency, relational parity and cross-tenant negative access remain untested. | Independent Database Reviewer approval, authorized disposable test environment, complete positive/negative test evidence, findings remediation and retest. | NOT TESTED |
| GDES-FND-OPS-001 | Gate blocker | Operational security supplement has not been validated in runtime. | CI/CD, secrets, logging, alerting, vulnerability response, incident response, backup/restore and rollback controls are specification-level only. | Independent Security Reviewer approval and environment-backed evidence for each applicable control, followed by remediation and retest. | NOT TESTED |
| GDES-FND-GOV-001 | Gate blocker | Canonical Control Dictionary has not been approved. | Decision request is open in [Issue #40](https://github.com/muchlisbstg/Full-stack-product-development/issues/40). | Explicit Standards Owner approve/revise/reject decision for SEC/DB namespaces, semantics, many-to-many links and source-qualified aliases; update version/effective date only after decision. | PENDING OWNER |
| GDES-FND-GOV-002 | Gate blocker | Independent reviewers are not appointed. | Procurement ceiling deferred; no candidate contact, NDA, appointment or review authorized. | Confirm budget availability and provide renewed explicit procurement authorization; only then identify, vet, appoint and contract independent reviewers. | BLOCKED — PROCUREMENT DEFERRED |
| GDES-FND-LIC-001 | Moderate | Legal disposition of upstream CC BY-SA 4.0 use is pending. | Six exact upstream license snapshots were inspected and identify CC BY-SA 4.0; license register contains commit, blob SHA and SHA-256. | Legal review confirms attribution, ShareAlike, modification, redistribution and notice obligations for the exact GDES artifacts. | PENDING LEGAL REVIEW |

## 3. Source evidence artifacts

All generated artifacts are stored under `docs/registers/data/` and were read back from the pilot branch:

- `GDES_SOURCE_EXTRACTION_MANIFEST_v1.0.json`
- `GDES_MASWE_CATALOG_v1.0.0.csv`
- `GDES_MASWE_BETA_ALIAS_CROSSWALK_v1.0.0.csv`
- `GDES_MASWE_BETA_ALIAS_FINDINGS_v1.0.0.csv`
- `GDES_MASTG_TEST_CATALOG_v2.0.0.csv`
- `GDES_MASWE_MASTG_TRACEABILITY_v1.0.0.csv`
- `GDES_ASVS_REQUIREMENT_CATALOG_v5.0.0.csv`
- `GDES_TCASVS_REQUIREMENT_CATALOG_v5.0.0.csv`
- `GDES_SAMM_ACTIVITY_CATALOG_v2.2.0.csv`
- `GDES_SAMM_QUESTION_CATALOG_v2.2.0.csv`
- `GDES_UPSTREAM_LICENSE_SNAPSHOT_REGISTER_v1.0.csv`
- `OWASP_MASWE_v1.0.0_BETA_MAPPING_SOURCE.yaml`

## 4. Closure and retest protocol

1. Assign a finding owner only after the relevant reviewer is appointed or the Standards Owner accepts the responsibility.
2. Record root cause and scope; do not silently alter upstream IDs or source mappings.
3. Make remediation on an isolated branch and preserve source evidence.
4. Run the relevant tests against the exact remediation commit and authorized environment.
5. Obtain independent retest evidence; unresolved findings remain OPEN or are formally risk-accepted with rationale, owner, expiry and compensating controls.
6. Reconcile the final findings register with the acceptance matrix and independent review report.
7. Cybersecurity Gate may be proposed for approval only when all gate-blocking findings are closed or explicitly risk-accepted, independent Security and Database reviews are complete, retests are evidenced, and the Standards Owner records explicit approval.

## 5. Governance disposition

- Independent Security Reviewer: NOT APPOINTED — BLOCKED.
- Independent Database Reviewer: NOT APPOINTED — BLOCKED.
- Procurement: DEFERRED — no outreach, NDA, appointment or expenditure.
- Runtime security tests: NOT EXECUTED.
- Retest: NOT STARTED.
- Cybersecurity Gate: NOT CLEARED.
- SDLC formal progression: BLOCKED.

**Final status: FINDINGS REGISTERED — SOURCE EXTRACTION COMPLETE — SOURCE MAPPING PARTIAL — INDEPENDENT REVIEW BLOCKED — NOT APPROVED.**
