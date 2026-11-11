# GDES Cybersecurity Source Reconciliation 001
## Draft for Review — Canonical ID and Wording Reconciliation

| Metadata | Value |
|---|---|
| Artifact ID | GDES-SEC-SOURCE-RECONCILIATION-001 |
| Version | 0.1 |
| Status | **DRAFT — SOURCE RECONCILIATION IN PROGRESS — NOT APPROVED** |
| Repository / branch | muchlisbstg/Full-stack-product-development / gdes/ai-governance-v1-pilot |
| Parent | GDES Master Standard v1.0 — Draft for Review |
| Workbook source | GDES_MUCHLIS_BSTG_v1.1_Draft.xlsx |
| Workbook edition | GDES-001 / Version 1.1 Draft |
| Workbook SHA-256 | 653a42a1748b3a64c52a301e688464518511ac03eb53a478ddb86aa660dbca67 |
| Comparison workbook | GDES_MUCHLIS_BSTG_v1.0_Draft.xlsx |
| Comparison SHA-256 | 9c4ea19ce134740ce7c1806947285a4d62a1d7069e4cf212179cf387374b3aa6 |
| Inspection method | Read-only workbook inspection; worksheet and cell content extracted |
| Approval authority | Standards Owner; independent Security and Database review remain separate |

> This artifact records source facts and identifies conflicts. It does not silently rename, delete, merge, or approve controls. The v1.1 workbook itself is marked Draft — pending approval and is a candidate master source, not an approved normative standard.

## 1. Purpose and decision boundary

Reconcile the canonical wording and identity of cybersecurity requirements across:
1. GDES Master workbook v1.1;
2. the pilot Cybersecurity Register v1.0;
3. the pilot Master Reconciliation Register v1.0; and
4. the pilot Cybersecurity External Mapping Matrix v1.0.

The immediate blocker is that the three pilot documents do not use a consistent meaning for GDES-SEC-001–011. Until the Standards Owner resolves this conflict, framework mappings and reviewer acceptance criteria that depend on those IDs cannot be treated as canonical.

No framework mapping is re-labelled in this document. Existing draft IDs are preserved as source-local identifiers until disposition.

## 2. Source inventory and workbook findings

### 2.1 GDES workbook v1.1

Workbook metadata from `00_README`:
- Standard ID: GDES-001.
- Edition: 1.1 Draft.
- Status: Draft — pending approval.
- Mandatory Standard prefix: GDES-MS.
- Recommended Practice prefix: GDES-RP.
- Regional Addendum prefix: GDES-RA.
- The workbook states it is an internal proposed standard, not an ISO/IEEE publication or certification.

Relevant source rows inspected:

**Worksheet `12_MANDATORY_STANDARD`**

| Workbook row | Standard ID | Domain | Normative requirement (faithful concise summary) | Severity |
|---:|---|---|---|---|
| 6 | GDES-MS-SEC-001 | Security | Protected operations enforce authorization server-side; client-supplied role or tenant claims alone are not authoritative. | CRITICAL |
| 7 | GDES-MS-SEC-002 | Security | Secrets are not committed to source code or exposed in client bundles/logs. | CRITICAL |
| 8 | GDES-MS-DB-001 | Database | Data integrity is enforced with appropriate database constraints and transaction boundaries. | CRITICAL |
| 9 | GDES-MS-PRIV-001 | Privacy | Personal-data processing is assessed against applicable legal requirements and documented purpose/retention controls. | HIGH |
| 10 | GDES-MS-QA-001 | Quality | A quality gate cannot be PASS without completed acceptance criteria and verifiable evidence. | HIGH |
| 11 | GDES-MS-REL-001 | Reliability | Critical services define backup, recovery and incident-response requirements. | HIGH |
| 12 | GDES-MS-REL-002 | Release | Production deployment and material production changes require authorized approval. | CRITICAL |

Workbook acceptance/evidence details for the three security/database rows:
- GDES-MS-SEC-001: negative tests deny unauthorized and cross-tenant access; evidence includes authorization tests, policy configuration and logs.
- GDES-MS-SEC-002: secret scan and configuration review show no exposed secrets; evidence includes scanner report and configuration review.
- GDES-MS-DB-001: required PK, FK, unique, check and transactional rules are documented and tested; evidence includes schema review and database tests.

**Worksheet `09_GOVERNANCE_CONTROLS`**

| Workbook row | ID | Control | Rule | Evidence |
|---:|---|---|---|---|
| 8 | GC-04 | Secrets | No secrets in source code or logs. | Secret-scanning evidence |
| 9 | GC-05 | Access | Least privilege and server-side authorization. | Access matrix and negative tests |
| 10 | GC-06 | Independent review | Critical security and database risks receive independent review. | Reviewer sign-off |

These governance controls are related supporting controls. They are not substitutes for the normative GDES-MS requirements and must not be collapsed into them without an explicit owner decision.

**Worksheet `03_QUALITY_GATES`**
- QG-04 Security: threat review, dependency scan and required security tests; evidence includes security report and test output.
- QG-05 Database: schema integrity, access control, tenancy and migration review; evidence includes schema review and database test results.
- QG-06 API: API contract and server-side authorization verified; evidence includes OpenAPI and negative tests.

All QG statuses are NOT TESTED in the workbook.

### 2.2 Workbook v1.0 comparison

The v1.0 workbook is an earlier draft and has a different worksheet layout. The v1.1 workbook contains the explicit `12_MANDATORY_STANDARD` and `09_GOVERNANCE_CONTROLS` structures recorded above. This reconciliation uses v1.1 as the latest located candidate source, while preserving the fact that it is still Draft. The older workbook is retained as a historical comparison source, not silently discarded.

## 3. Conflicting pilot ID baselines

### 3.1 Cybersecurity Register v1.0

Source: `docs/registers/GDES_CYBERSECURITY_REGISTER_v1.0.md`, blob SHA `8bf6a6def2ab4ec6117537c74f33309eeadc5585`.

The register explicitly says its GDES-SEC-001–011 titles and statements are provisional working descriptions pending canonical workbook reconciliation. Its current meanings include:
- SEC-001 Security Governance & Threat Modeling;
- SEC-002 Identity & Authentication;
- SEC-003 Authorization & Privilege Control;
- SEC-007 Secrets & Secure Configuration;
- SEC-008 Database & Tenant Data Integrity;
- SEC-011 Security Verification, Resilience & Incident Readiness.

Its cross-reference note provisionally associates:
- GDES-MS-SEC-001 with GDES-SEC-003;
- GDES-MS-SEC-002 with GDES-SEC-007;
- GDES-MS-DB-001 with GDES-SEC-008;
- GC-04/05/06 with related controls.

### 3.2 Master Reconciliation Register v1.0

Source: `docs/GDES_MASTER_RECONCILIATION_REGISTER_v1.0.md`, blob SHA `433b0aa9ffbead41e116204f0467d154115595ee`.

Its Section 5 uses a materially different initial baseline:
- SEC-001 Authentication and identity lifecycle;
- SEC-002 Server-side authorization and least privilege;
- SEC-003 Secrets management;
- SEC-004 Input validation and safe output;
- SEC-005 Network/SSRF/egress security;
- SEC-006 Data privacy and protection;
- SEC-007 Dependency and supply-chain security;
- SEC-008 Security logging and monitoring;
- SEC-009 Backup, recovery and incident readiness;
- SEC-010 Independent security review;
- SEC-011 Security test evidence integrity.

This is also described in the Master Reconciliation Register as an initial normalized baseline, not a recovered canonical standalone source register.

### 3.3 Mapping Matrix v1.0

Source: `docs/registers/GDES_CYBERSECURITY_MAPPING_MATRIX_v1.0.md`, blob SHA `420c13485aace686756d29184eb25eb3246f7346`.

The matrix maps the Cybersecurity Register's provisional SEC-001–011 meanings. Its upstream source pins and technical crosswalk do not resolve the conflicting GDES control identity problem. Mapping details must be retained as a provisional crosswalk until the control dictionary is resolved.

## 4. Conflict register

| Conflict ID | Source requirement | Cybersecurity Register v1.0 | Master Reconciliation Register v1.0 | Risk / required disposition |
|---|---|---|---|---|
| SRC-CONFLICT-001 | GDES-MS-SEC-001 = server-side authorization | SEC-003 | SEC-002 | One normative requirement maps to two different legacy IDs. Standards Owner must select canonical control identity or establish a formal alias/crosswalk. |
| SRC-CONFLICT-002 | GDES-MS-SEC-002 = secrets protection | SEC-007 | SEC-003 | Same requirement has two different legacy IDs. Preserve both source histories until decision. |
| SRC-CONFLICT-003 | GDES-MS-DB-001 = database integrity and transaction boundaries | SEC-008 | No equivalent explicit database control in the 11-row cybersecurity baseline | Database requirement must remain a first-class database/security control; do not force-fit it into a security-only ID without owner decision. |
| SRC-CONFLICT-004 | GC-04 = secrets | Cross-reference to SEC-007 | Concept overlaps SEC-003 | Governance-control ID and domain-control ID are separate namespaces. |
| SRC-CONFLICT-005 | GC-05 = least privilege and server-side authorization | Cross-reference to SEC-003 | Concept overlaps SEC-002 | Do not conflate GC and SEC identifiers. |
| SRC-CONFLICT-006 | GC-06 = independent security/database review | Cross-reference to SEC-011 | Concept overlaps SEC-010 and evidence integrity SEC-011 | Independent review governance must be distinguished from test evidence integrity. |
| SRC-CONFLICT-007 | Workbook has 7 normative rows in 12_MANDATORY_STANDARD | Register has 11 domain controls | Reconciliation baseline has 11 domain controls | The 11 controls are decomposition/domain controls, not a one-to-one copy of the workbook's 7 normative rows. Build explicit many-to-many traceability. |

## 5. Safe interim traceability model

Until Standards Owner disposition, use a three-layer traceability model:

1. **Normative source ID** — exact GDES-MS-* ID from the master workbook.
2. **Governance control ID** — exact GC-* ID from the workbook, retained in its own namespace.
3. **Domain implementation/control ID** — GDES-SEC-* or GDES-DB-* ID, explicitly marked provisional until canonicalized.

Recommended interim mappings (relationships only; not ID renames):

| Normative source ID | Related governance ID | Domain coverage candidates | Relationship status |
|---|---|---|---|
| GDES-MS-SEC-001 | GC-05 | Register SEC-003; Reconciliation SEC-002 | CONFLICT — owner decision required |
| GDES-MS-SEC-002 | GC-04 | Register SEC-007; Reconciliation SEC-003 | CONFLICT — owner decision required |
| GDES-MS-DB-001 | GC-06 where independent review applies | Register SEC-008 plus dedicated DB control decomposition | PARTIAL — DB domain decomposition required |
| GDES-MS-QA-001 | GC-01/GC-06/GC-08 only where relevant | Evidence-integrity and verification controls | PARTIAL — avoid treating governance controls as identical requirements |
| GDES-MS-REL-001 | GC-08 only where release/recovery scope overlaps | Register SEC-011 and operational controls | PARTIAL — recovery/incident criteria need explicit trace |
| GDES-MS-REL-002 | GC-02/GC-08 | Release/change authorization controls | PARTIAL — maintain release namespace and trace |

The table above is a working traceability hypothesis, not an approved mapping. GC-06 is a reviewer governance control, not a direct replacement for database integrity requirements.

## 6. Standards Owner decisions required

The following decisions must be recorded before changing any existing register IDs:

- [ ] Confirm the workbook v1.1 as the candidate source baseline for reconciliation, while keeping its overall status Draft.
- [ ] Decide whether the existing GDES-SEC-001–011 in the Cybersecurity Register or the alternative 11-row Master Reconciliation baseline is the preferred domain-control numbering history, or approve a new canonical domain-control dictionary.
- [ ] Decide whether database controls receive a separate GDES-DB-* namespace or remain explicitly cross-domain GDES-SEC-* controls with database sub-registers.
- [ ] Approve a many-to-many traceability rule between GDES-MS-*, GC-*, GDES-SEC-* and any GDES-DB-* controls.
- [ ] Decide how superseded/alias IDs are preserved for backward traceability.
- [ ] Confirm whether QG-04/QG-05/QG-06 are gate checks, not additional normative controls.

No decision is presumed by this draft.

## 7. Downstream work blocked by this reconciliation

Until the owner decisions above are recorded:
- Do not publish a final canonical GDES-SEC-001–011 dictionary.
- Do not renumber existing controls or rewrite the existing Register/Mapping Matrix.
- Do not mark ASVS/MASVS/MASTG/TCASVS/SAMM mappings complete based on provisional IDs.
- Do not claim acceptance criteria are final for independent reviewers.
- Do not progress the SDLC Register formally beyond its existing draft baseline.

Safe work may continue on framework source-pin verification, license verification, and technical gap discovery if each finding is kept linked to the relevant source requirement and labelled provisional.

## 8. Review and approval state

| Review / decision | Required authority | Status |
|---|---|---|
| Source extraction and comparison | Maintainer | COMPLETED — document analysis only |
| Canonical ID disposition | Standards Owner | PENDING |
| Security mapping challenge | Independent Security Reviewer | BLOCKED — not appointed |
| Database coverage challenge | Independent Database Reviewer | BLOCKED — not appointed |
| Legal/licensing disposition | Qualified legal reviewer if adaptation/redistribution requires it | NOT STARTED |
| Final approval | Standards Owner after reviews | NOT APPROVED |

**Current disposition: DRAFT — SOURCE RECONCILIATION IN PROGRESS — NOT APPROVED.**

No runtime test, independent review, legal review, procurement, or approval is claimed.


## 6. Final pinned-source extraction result — 2026-11-11

The corrected extraction pipeline completed successfully in [GitHub Actions run 42972384713](https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/42972384713). Generated catalogs were committed at `7e06abbe46960e02c0bdd583111575eb96116207` and read back from the pilot branch.

### 6.1 Source record counts

| Source | Records |
|---|---:|
| MASVS controls | 24 |
| MASWE v1.0.0 stable weaknesses | 78 |
| MASWE v1.0.0 beta alias IDs | 118 |
| MASTG test paths | 292 (200 structured v2 tests; 92 legacy paths) |
| ASVS v5.0.0 requirements | 345 |
| TCASVS v5.0.0 requirements | 132 |
| SAMM v2.2.0 activities | 90 |
| SAMM v2.2.0 questions | 90 |
| Upstream license snapshots | 6 |

### 6.2 MASWE beta alias reconciliation

The official MASWE v1.0.0 release asset `OWASP_MASWE.yaml` was downloaded by the extractor and preserved in `docs/registers/data/OWASP_MASWE_v1.0.0_BETA_MAPPING_SOURCE.yaml`.

- Asset SHA-256: `55288b0ff60003691a877a693f28f07455a5352d5c0f9163b434b5a9e4b563d7`.
- 118 beta IDs map to stable weaknesses.
- Seven beta IDs map to multiple stable weaknesses; all source targets are preserved.
- `MASWE-0097` is referenced by four MASTG tests but is absent from the official stable alias mapping. Stable `MASWE-0051` is a semantic candidate only, not a source-backed alias.
- 38 stable weaknesses have no linked MASTG test in the extracted tree, versus 36 in the release article.

### 6.3 Count and mapping exceptions

- MASTG v2.0.0 tree: 292 unique test Markdown paths, while the release announcement reports 285 tests. The seven-path difference remains open.
- ASVS: 345 requirement rows; 282 use section-range candidate mappings and 63 use chapter-level fallback. All are candidates, not approved mappings.
- TCASVS: 132 requirement rows with chapter-level candidate mappings.
- SAMM: 90 activity GUIDs and 90 linked questions; practice-to-GDES mappings remain candidates.
- All six exact upstream license snapshots identify CC BY-SA 4.0; legal review of attribution and ShareAlike obligations remains separate.

### 6.4 Source artifacts

See `docs/registers/data/GDES_SOURCE_EXTRACTION_MANIFEST_v1.0.json` for counts and checks, `GDES_MASWE_BETA_ALIAS_CROSSWALK_v1.0.0.csv` for the official alias map, and `GDES_MASWE_BETA_ALIAS_FINDINGS_v1.0.0.csv` for unresolved/multi-target items.

**Final source disposition: EXTRACTED AND REMOTE-VERIFIED — CANONICAL GDES MAPPING PARTIAL — OPEN FINDINGS RETAINED — NOT APPROVED.**
