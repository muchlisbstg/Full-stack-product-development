# GDES Cybersecurity Independent Review Package v1.0
## Reviewer Handoff Index — Internal Draft Only

| Metadata | Value |
|---|---|
| Artifact ID | GDES-SEC-IRP-001 |
| Version | 1.0 |
| Status | **INTERNAL REVIEW PACKAGE — DRAFT — NOT ISSUED** |
| Repository / branch | muchlisbstg/Full-stack-product-development / gdes/ai-governance-v1-pilot |
| Procurement | DEFERRED — no approved budget ceiling |
| Security Reviewer | Not appointed |
| Database Reviewer | Not appointed |
| NDA / candidate contact | Not authorized; not started |

## 1. Purpose

Provide a controlled index of documents and review questions for future independent Security and Database review. This package is not an RFP issuance, invitation, candidate contact, NDA, appointment, purchase order or permission to disclose nonpublic material.

## 2. Document pack

| Order | Document | Reviewer use |
|---:|---|---|
| 1 | GDES Master Standard v1.0 — Draft | Normative parent and governance principles |
| 2 | GDES Master Reconciliation Register v1.0 — Draft | Domain conflicts and historical baseline |
| 3 | GDES-SEC-SOURCE-RECONCILIATION-001 | Workbook/control ID conflict analysis |
| 4 | GDES-SEC-DICT-001 | Proposed canonical SEC/DB controls and alias crosswalk |
| 5 | GDES-SEC-ACCEPTANCE-MATRIX-001 | Positive/negative acceptance criteria and evidence |
| 6 | GDES-SEC-MAP-002 | ASVS, MASVS, MASWE, MASTG, TCASVS and SAMM mapping |
| 7 | GDES-DB-SUP-001 | Database integrity, RLS, roles, concurrency and parity |
| 8 | GDES-OPS-SEC-SUP-001 | CI/CD, secrets, monitoring, incident and recovery |
| 9 | GDES-SEC-COMP-001 | Completeness result, gaps and SDLC exit conditions |
| 10 | Existing Cybersecurity Register v1.0 and Mapping Matrix v1.0 | Historical drafts; use only with source-qualified legacy IDs |
| 11 | RFP SEC-001 v1.1 and DB-001 v1.1 | Internal procurement drafts only; not issued |

## 3. Independent Security Reviewer scope

Reviewer must be independent of document authors and implementers. Required review:
- canonical control identity, source mapping and legacy aliases;
- ASVS exact requirement mapping, applicability and verification levels;
- MASVS/MASWE/MASTG test selection for Android/iOS;
- TCASVS chapter coverage and metadata discrepancy;
- SAMM practice mapping and maturity boundary;
- threat modeling, identity, authorization, SSRF/network, secrets, privacy, supply chain, logging and incident controls;
- acceptance criteria quality, negative test completeness and evidence integrity;
- framework license and attribution risks to refer to qualified legal review where needed.

Deliverables:
- reviewer identity, qualifications, independence/COI declaration and scope;
- source SHA and reviewed document versions;
- finding register with severity, evidence, impact, owner and remediation;
- coverage gaps and recommended changes;
- retest results and explicit recommendation;
- signed/attributable report.

## 4. Independent Database Reviewer scope

Reviewer must be independent of schema and application implementation. Required review:
- canonical relational model, PK/FK/unique/check/not-null and composite tenant FKs;
- PostgreSQL RLS policies, FORCE RLS, owner/BYPASSRLS behavior and pooled connection context;
- runtime/migration/admin role separation and grants;
- views, triggers, SECURITY DEFINER, functions, RPC and background workers;
- transaction isolation, concurrency, locking, idempotency, duplicate side effects and temporal consistency;
- SQLite/PostgreSQL relational and behavioral parity;
- migration/rollback, backup/restore and integrity evidence;
- database negative-access test catalogue and acceptance criteria.

Deliverables:
- reviewer identity, qualifications and independence/COI declaration;
- exact schema/engine/version and source/environment SHA;
- reproducible SQL/test procedures and outcomes;
- findings and severity;
- RLS/role bypass analysis;
- parity and transaction/concurrency report;
- retest and signed/attributable recommendation.

## 5. Evidence access and handling rules

- Do not provide secrets, production credentials, customer personal data or real-money data.
- Use sanitized, synthetic or disposable evidence wherever possible.
- Record all evidence links and digests against source SHA and environment.
- Keep confidential materials behind approved access controls and an executed NDA when procurement is explicitly reopened.
- Do not grant repository write, merge, deployment or database privileges to reviewers by default.
- Reviewers recommend; Standards Owner approves the standard.
- Security and Database reviewers do not approve each other's domain findings unless explicitly within qualified scope.

## 6. Readiness status

| Gate | Status |
|---|---|
| Draft document pack assembled | COMPLETED |
| Source and version inventory | PARTIAL |
| Canonical ID decision | PENDING Standards Owner |
| Framework leaf-level mapping | PARTIAL |
| License review | NOT STARTED |
| Security reviewer procurement | DEFERRED |
| Database reviewer procurement | DEFERRED |
| Candidate search/contact | NOT AUTHORIZED |
| NDA | NOT STARTED |
| Appointment | NOT STARTED |
| Independent review | BLOCKED |
| Standards Owner approval | NOT APPROVED |

## 7. Procurement and disclosure hold

The user's standing decision is that the GDES procurement ceiling is deferred and the RFPs must be revised internally first. Therefore:
- no candidate search or contact;
- no public or private solicitation;
- no NDA circulation or signature;
- no reviewer appointment;
- no sharing nonpublic evidence;
- no procurement expenditure.

Reopening requires both confirmed budget availability and explicit renewed authorization from the Standards Owner.

**Disposition: INTERNAL DRAFT PACKAGE ONLY — NOT ISSUED — NO REVIEWER APPOINTED.**


## 7. Updated source and handoff readiness — 2026-11-11

### 7.1 Immutable source and license baseline

Use the corrected source snapshot register in `GDES_CYBERSECURITY_FRAMEWORK_MAPPING_v1.0.md`:

- ASVS 5.0.0 — `OWASP/ASVS@62981c68fd06206e8afa161653943935de9a5047`
- MASVS YAML — `OWASP/masvs@bbe226fd17e6dab51927f392936deef31c816423`
- MASWE 1.0.0 — `OWASP/maswe@308b82b4bbe29166934fb5a621b40471cfea61db`
- MASTG 2.0.0 — `OWASP/mastg@990472dbcffe126f5556045d60270c4ffdfdde72`
- TCASVS 5.0.0 — `OWASP/TCASVS@f10ec111883787dd6f83e0237d0f1b2e043d55e0`
- SAMM 2.2.0 — `owaspsamm/core@21352e0fc79a6764abcd83a008690e32d2d5a3fe`

All six pinned license files were inspected and identify CC BY-SA 4.0. Reviewers must still assess attribution, ShareAlike, modifications, and whether the GDES output reproduces or adapts licensed source content.

### 7.2 Canonical ID rule for reviewers

Review against `GDES-SEC-DICT-001`, not bare IDs from the earlier provisional mapping matrix. In particular, the canonical proposed meanings for SEC-008 through SEC-011 are Supply Chain, Logging/Monitoring, Verification/Evidence, and Incident/Resilience respectively. Database review uses `GDES-DB-001–005`. Every historical alias must be qualified by its source document/version.

### 7.3 Extraction evidence status

The metadata extractor and branch-scoped Actions workflow are present, but the observed workflow attempts have not produced a successful extraction. Do not treat planned catalog paths as existing evidence. Before reviewer handoff, attach the successful Actions run URL, commit SHA, generated manifest, CSV file SHAs, row counts, missing-field checks, duplicate checks, unknown weakness references, and license-file SHA-256 values.

A MASTG inventory discrepancy must be explicitly reviewed: the pinned tree contains 292 unique test Markdown paths (200 in `tests-beta/`, 92 in legacy `tests/`), while the v2.0.0 release announcement reports 285 tests. The extractor must preserve the full tree inventory and distinguish structured metadata-linked tests from legacy pages.

### 7.4 Procurement and disclosure boundary

This package remains **INTERNAL DRAFT — NOT ISSUED**. The procurement ceiling is deferred. No candidate search/contact, NDA, appointment, non-public evidence disclosure, independent review, or expense is authorized. Reopening requires both confirmed budget availability and explicit renewed authorization from the Standards Owner.

**Handoff readiness: DOCUMENT INDEX READY — SOURCE METADATA EXTRACTION NOT VERIFIED — NOT ISSUED — REVIEWERS NOT APPOINTED.**
