# GDES Cybersecurity Canonical Control Dictionary v1.0
## Draft for Standards Owner Decision and Independent Review

| Metadata | Value |
|---|---|
| Artifact ID | GDES-SEC-DICT-001 |
| Version | 1.0 |
| Status | **PROPOSED CANONICAL DICTIONARY — DRAFT — NOT APPROVED** |
| Parent | GDES Master Standard v1.0 — Draft for Review |
| Source baseline | GDES Master workbook v1.1 Draft; GDES source reconciliation 001 |
| Repository / branch | muchlisbstg/Full-stack-product-development / gdes/ai-governance-v1-pilot |
| Control namespaces | GDES-SEC-* (application/security); GDES-DB-* (database-specific) |
| Decision authority | Standards Owner; independent Security and Database review required |

> This document establishes a stable proposed control dictionary and legacy crosswalk. It does not approve the master workbook, authorize rollout, or claim implementation/test PASS. Existing identifiers remain preserved as historical aliases.

## 1. ID and traceability rules

1. GDES-MS-* IDs identify normative requirements in the Master Standard workbook.
2. GC-* IDs identify governance/quality controls and remain a separate namespace.
3. GDES-SEC-* IDs identify application, platform, API, and operational security control domains.
4. GDES-DB-* IDs identify database-specific controls requiring database-engine evidence.
5. A normative requirement may map to multiple domain controls, and a domain control may support multiple normative requirements (many-to-many traceability).
6. Legacy IDs are immutable historical references. They are never silently reassigned or reused.
7. A legacy alias is not a second active control. It resolves to the canonical control(s) in this dictionary.
8. Applicability must be assessed and recorded; NOT APPLICABLE requires rationale and authorized owner disposition.
9. Control mapping does not prove implementation, test execution, PASS, independent review, or approval.

## 2. Canonical GDES-SEC control dictionary

| Canonical ID | Control title | Draft mandatory intent | Minimum scope |
|---|---|---|---|
| GDES-SEC-001 | Security Governance & Threat Modeling | Define assets, trust boundaries, threats, security requirements, risk owners, treatment decisions and review triggers before material exposure or release changes. | All products, services, integrations and material changes |
| GDES-SEC-002 | Identity, Authentication & Session Lifecycle | Verify identities at trusted boundaries; protect credential enrollment, MFA, recovery, session/token issuance, expiry, revocation and replay resistance. | User, service, workforce and privileged identities |
| GDES-SEC-003 | Authorization & Privilege Control | Enforce deny-by-default, least-privilege authorization server-side for every protected action and resource; never trust client-supplied tenant, role, site or ownership claims. | APIs, services, admin functions, tenant/resource operations |
| GDES-SEC-004 | Input, Output & Injection Defense | Treat all external data as untrusted; validate schemas and bounds, encode output by context, parameterize queries, and prevent unsafe parsing/deserialization. | UI, API, imports, IPC, files, integrations and database queries |
| GDES-SEC-005 | API, Integration & Network Security | Authenticate and authorize service interfaces; secure transport; constrain outbound destinations, redirects, DNS resolution, timeouts and egress according to threat model. | Web/API, mobile, desktop, workers and third-party integrations |
| GDES-SEC-006 | Data Protection & Privacy | Classify and minimize sensitive data; define purpose, access, retention, deletion, encryption and disclosure controls proportionate to sensitivity and jurisdiction. | Personal, commercial, financial, credential and confidential data |
| GDES-SEC-007 | Secrets & Secure Configuration | Keep secrets out of source, client bundles, logs and unauthorized stores; inject through approved runtime boundaries; restrict and review configuration. | CI/CD, apps, services, mobile/desktop bundles, operations |
| GDES-SEC-008 | Dependency & Software Supply Chain | Inventory dependencies/build inputs; assess vulnerabilities and licenses; protect source/build provenance, artifact integrity and release inputs. | Direct/transitive dependencies, build tools, images and artifacts |
| GDES-SEC-009 | Security Logging, Monitoring & Error Handling | Record attributable security events with privacy-aware minimization; detect material abuse; provide safe errors without exposing secrets or internals. | Application, API, identity, database and infrastructure events |
| GDES-SEC-010 | Security Verification, Vulnerability & Evidence Management | Define risk-based positive/negative tests; preserve SHA/environment-bound evidence; triage findings, retest fixes and control security exceptions. | SDLC, CI, release gates, independent security review |
| GDES-SEC-011 | Incident Response & Operational Resilience | Maintain incident ownership, response, containment, recovery, backup/restore and rollback procedures proportionate to business impact; exercise them. | Production and critical non-production services |

## 3. Canonical GDES-DB control dictionary

| Canonical ID | Control title | Draft mandatory intent | Minimum scope |
|---|---|---|---|
| GDES-DB-001 | Relational Schema & Integrity Constraints | Enforce correct primary/foreign/unique/check/not-null constraints and tenant/resource relationships in the authoritative database schema. | All persistent relational data |
| GDES-DB-002 | Tenant, Row & Resource Isolation | Enforce tenant and row boundaries in trusted server/database layers; validate PostgreSQL RLS policies, role bypass resistance and composite tenant keys where applicable. | Multi-tenant databases and shared schemas |
| GDES-DB-003 | Transaction, Concurrency & Temporal Consistency | Define transaction boundaries, isolation, locking, idempotency, duplicate handling, ordering and time consistency; test concurrent and retry behavior. | Financial, inventory, contract, authorization and stateful workflows |
| GDES-DB-004 | Database Identity, Privilege & Audit | Use dedicated least-privilege database identities, safe credential rotation, restricted schema/function privileges and auditable privileged access. | Database roles, service connections and administrative access |
| GDES-DB-005 | Migration, Backup, Restore & Engine Parity | Control schema evolution and rollback; verify backup/restore; reconcile behavior across declared database engines; prohibit unapproved destructive operations. | Schema lifecycle, SQLite/PostgreSQL parity and recovery |

## 4. Normative source traceability

| Normative / governance source | Canonical target(s) | Relationship |
|---|---|---|
| GDES-MS-SEC-001 (server-side authorization) | GDES-SEC-003 | Direct |
| GDES-MS-SEC-002 (secrets protection) | GDES-SEC-007 | Direct |
| GDES-MS-DB-001 (integrity and transaction boundaries) | GDES-DB-001, GDES-DB-003 | Direct; split by concern |
| GC-04 (no secrets in source/logs) | GDES-SEC-007, GDES-SEC-009 | Supporting governance control |
| GC-05 (least privilege/server-side authorization) | GDES-SEC-002, GDES-SEC-003, GDES-DB-004 | Supporting governance control |
| GC-06 (independent review) | Review gate across GDES-SEC-010 and GDES-DB-001–005 | Governance/review requirement; not a substitute for technical controls |
| QG-04 Security | GDES-SEC-001–010 as applicable | Quality gate, not a separate control ID |
| QG-05 Database | GDES-DB-001–005 | Quality gate, not a separate control ID |
| QG-06 API | GDES-SEC-002–005 | Quality gate, not a separate control ID |

## 5. Legacy crosswalk — Cybersecurity Register v1.0

Source: `docs/registers/GDES_CYBERSECURITY_REGISTER_v1.0.md`, blob `8bf6a6def2ab4ec6117537c74f33309eeadc5585`.

| Legacy ID | Legacy title | Canonical resolution | Treatment |
|---|---|---|---|
| GDES-SEC-001 | Security Governance & Threat Modeling | GDES-SEC-001 | Same semantic intent; retain as legacy alias |
| GDES-SEC-002 | Identity & Authentication | GDES-SEC-002 | Expand to session/token lifecycle |
| GDES-SEC-003 | Authorization & Privilege Control | GDES-SEC-003 | Same semantic intent |
| GDES-SEC-004 | Input, Output & Injection Defense | GDES-SEC-004 | Same semantic intent |
| GDES-SEC-005 | API, Integration & Network Security | GDES-SEC-005 | Same semantic intent |
| GDES-SEC-006 | Cryptography & Sensitive Data Protection | GDES-SEC-006 | Expand to privacy/data lifecycle; cryptographic details remain explicit |
| GDES-SEC-007 | Secrets & Secure Configuration | GDES-SEC-007 | Same semantic intent |
| GDES-SEC-008 | Database & Tenant Data Integrity | GDES-DB-001–005 and GDES-SEC-003 | Split into database sub-controls and server-side authorization; do not retain as an active duplicate |
| GDES-SEC-009 | Dependency & Software Supply Chain | GDES-SEC-008 | Canonical numbering differs; alias only |
| GDES-SEC-010 | Security Logging, Monitoring & Error Handling | GDES-SEC-009 | Canonical numbering differs; alias only |
| GDES-SEC-011 | Security Verification, Resilience & Incident Readiness | GDES-SEC-010 and GDES-SEC-011 | Split verification/evidence from incident and resilience |

## 6. Legacy crosswalk — Master Reconciliation Register v1.0

Source: `docs/GDES_MASTER_RECONCILIATION_REGISTER_v1.0.md`, blob `433b0aa9ffbead41e116204f0467d154115595ee`.

| Legacy ID | Legacy meaning | Canonical resolution |
|---|---|---|
| GDES-SEC-001 | Authentication and identity lifecycle | GDES-SEC-002 |
| GDES-SEC-002 | Server-side authorization and least privilege | GDES-SEC-003 |
| GDES-SEC-003 | Secrets management | GDES-SEC-007 |
| GDES-SEC-004 | Input validation and safe output | GDES-SEC-004 |
| GDES-SEC-005 | Network/SSRF/egress security | GDES-SEC-005 |
| GDES-SEC-006 | Data privacy and protection | GDES-SEC-006 |
| GDES-SEC-007 | Dependency and supply-chain security | GDES-SEC-008 |
| GDES-SEC-008 | Security logging and monitoring | GDES-SEC-009 |
| GDES-SEC-009 | Backup, recovery and incident readiness | GDES-SEC-011 |
| GDES-SEC-010 | Independent security review | GC-06 review governance; implementation evidence under GDES-SEC-010 |
| GDES-SEC-011 | Security test evidence integrity | GDES-SEC-010 |

Because the same textual IDs have different meanings in two historical documents, all historical references MUST be qualified by source document/version. Bare legacy GDES-SEC IDs are ambiguous and must not be used for new requirements.

## 7. Standards Owner disposition

The proposed dictionary and crosswalk are prepared. The following are still explicit approval items:
- [ ] Approve the new GDES-SEC/GDES-DB namespace and semantic dictionary.
- [ ] Approve the many-to-many traceability rule.
- [ ] Approve the historical alias policy and source-qualified legacy ID rule.
- [ ] Approve v1.1 workbook as the selected candidate baseline while preserving its Draft status.
- [ ] Approve the canonical dictionary version/effective date after independent review.

**Disposition: PROPOSED CANONICAL DICTIONARY — DRAFT — NOT APPROVED.**


## 8. Formal Standards Owner decision submission

- Decision request: [Issue #40 — Standards Owner Decision: GDES-SEC-DICT-001](https://github.com/muchlisbstg/Full-stack-product-development/issues/40)
- Submission date: 2026-11-11
- Issue state at submission: OPEN
- Requested disposition: Pending Standards Owner decision
- Dictionary state: **PROPOSED — DRAFT — NOT APPROVED**
- Effective date: Not assigned
- Rollout authority: Not granted

The issue requests an explicit decision on the canonical GDES-SEC/GDES-DB namespaces and semantics, many-to-many traceability, source-qualified legacy aliases, and the v1.1 workbook's candidate-source status. It expressly defers effective status until independent Security and Database review is complete and findings are dispositioned.

No approval is inferred from issue creation or from the Standards Owner's identity. A written disposition must be recorded in the issue and reflected in a versioned dictionary revision.

**Current disposition: SUBMITTED FOR STANDARDS OWNER DECISION — PENDING — NOT APPROVED.**
