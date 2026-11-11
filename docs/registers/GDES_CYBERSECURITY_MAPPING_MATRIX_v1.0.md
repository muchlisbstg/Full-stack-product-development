# GDES Cybersecurity External Mapping Matrix v1.0 — Draft for Independent Review

| Metadata | Value |
|---|---|
| Parent register | GDES-SEC-REG-001 / Cybersecurity Register v1.0 |
| Mapping artifact | GDES-SEC-MAP-001 |
| Version | 1.0 |
| Status | **TECHNICAL MAPPING DRAFT — INDEPENDENT REVIEW NOT COMPLETED** |
| Repository / branch | muchlisbstg/Full-stack-product-development / gdes/ai-governance-v1-pilot |
| Mapping source date | 2026-11-11 |
| Scope | Web/API, Android, iOS, Desktop/thick client, secure lifecycle maturity |
| Decision authority | Standards Owner; independent Security and Database reviewers required |

> This matrix records a maintainer's technical crosswalk from GDES controls to upstream requirements. It is not an independent review, certification, test execution, or approval. A mapped requirement is not automatically applicable to every product or verification level.

## 1. Source pins and source-of-truth decisions

| Framework | Selected source/version | Exact source pin used for this mapping | License | Verification note |
|---|---|---|---|---|
| OWASP ASVS | 5.0.0 stable | Tag `v5.0.0`; source CSV blob `184cf3b04a8fe1809dbed8b6e73be7a6fbaf8689` | CC BY-SA 4.0 | Official downloads and repository identify 5.0.0 as latest stable. Use version-qualified IDs `v5.0.0-Vx.y.z`. |
| OWASP MASVS | Current published control model | `OWASP_MASVS.yaml` blob `759acf74ebad2e9f06d34f7dfb92e5881e9340a2` on `master` | Verify LICENSE at pinned snapshot before redistribution | YAML metadata reports `vx.x.x`; do not invent a semantic release number. Preserve repository blob SHA. |
| OWASP MASWE | Stable 1.0.0 | Source release announced 2026-08-17; IDs MASWE-0001–MASWE-0078 | Verify LICENSE at pinned snapshot | MASWE is the weakness layer linking MASVS controls to test cases. |
| OWASP MASTG | Stable 2.0.0 | Release tag `v2.0.0`, release commit `990472d` | Verify LICENSE at pinned snapshot | Use the test case IDs from the tagged guide; do not substitute old MASTG v1 IDs without a migration mapping. |
| OWASP TCASVS | 5.0.0 | Repository commit `9c05d7ae8d7a5934688f8e396444c9e0b25a2074`; source chapter blobs listed below | CC BY-SA 4.0 | Repository README identifies 5.0.0 stable and 130+ requirements in six chapters. OWASP project card still shows 1.8; treat card as stale/conflicting metadata and pin repository release content. |
| OWASP SAMM | 2.2.0 | Release target `v2.2.0`; practice model source to be frozen at exact release commit before approval | CC BY-SA 4.0 | Model contains 5 business functions and 15 security practices. This matrix maps practices by canonical name and abbreviation; no maturity score is asserted. |

### Source files and blob identifiers

- ASVS CSV: `OWASP/ASVS/5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv` — `184cf3b04a8fe1809dbed8b6e73be7a6fbaf8689`
- MASVS YAML: `OWASP/masvs/OWASP_MASVS.yaml` — `759acf74ebad2e9f06d34f7dfb92e5881e9340a2`
- TCASVS V1: `5.0/en/0x10-V1-Architecture-and-Threat-Modeling.md` — `1665351c9a5bdd409b631907ec5a43571a2f460d`
- TCASVS V2: `5.0/en/0x11-V2-Build-Deployment-and-Environment-Hardening.md` — `d33837f97c7dcd3eda4626615997d3effc2720df`
- TCASVS V3: `5.0/en/0x12-V3-Data-Storage-and-Protection.md` — `2c88e1301a1be9f2c848285cd4d2d1dcaff95384`
- TCASVS V4: `5.0/en/0x13-V4-Code-Quality-and-Exploit-Mitigation.md` — `437e1bcb5c66f9e599dba3405b631bf1dc210b55`
- TCASVS V5: `5.0/en/0x14-V5-Cryptography.md` — `4743696b9cdee016794b7e1e9ac35979830de648`
- TCASVS V6: `5.0/en/0x15-V6-Network-Communication.md` — `136f60912405b993cc94cee62b6d3d0331e225f4`

## 2. Mapping convention

- ASVS references below use the exact section requirement ID range present in the pinned v5.0.0 CSV. Prefix each requirement with `v5.0.0-` when exported to test cases.
- MASVS IDs are control identifiers, not test cases.
- MASWE IDs describe weaknesses; select applicable weaknesses under each mapped MASVS control.
- MASTG test identifiers are executable test procedures. They must be selected from the pinned v2.0.0 guide and tied to platform (Android/iOS), app architecture, and test environment.
- TCASVS references use exact section requirement ID ranges; select verification level per threat model and risk.
- SAMM practice abbreviations: Governance (SM Strategy & Metrics; PC Policy & Compliance; EG Education & Guidance); Design (TA Threat Assessment; SR Security Requirements; SA Secure Architecture); Implementation (SB Secure Build; SD Secure Deployment; DM Defect Management); Verification (AA Architecture Assessment; RT Requirements-driven Testing; ST Security Testing); Operations (IM Incident Management; EM Environment Management; OM Operational Management).
- Relation: `covers` = directly addresses intent; `partially_covers` = only part; `informs` = maturity/guidance support, not a direct product verification requirement.

## 3. GDES-to-framework crosswalk

| GDES control | ASVS 5.0.0 requirement sections | MASVS v2 control IDs | TCASVS 5.0.0 requirement sections | SAMM 2.2 practices | Coverage disposition / GDES-only additions |
|---|---|---|---|---|---|
| GDES-SEC-001 Governance & Threat Modeling | V15.1.1–V15.1.5; V15.2.1–V15.2.5 | — | V1.1.1–V1.1.6; V1.2.1–V1.2.4; V1.3.1–V1.3.5; V1.4.1–V1.4.4 | SM, PC, TA, SR, SA, AA | PARTIAL. ASVS 5 removed the former architecture chapter and redistributed requirements; threat model governance, accountable risk ownership, and formal approval evidence remain GDES additions. |
| GDES-SEC-002 Identity & Authentication | V6.1.1–V6.8.4; V7.1.1–V7.6.2; V9.1.1–V9.2.4; V10.1.1–V10.6.2 | AUTH-1, AUTH-2, AUTH-3 | V2.4.1–V2.4.7; V3.3.1–V3.3.4 (local credentials/secrets; backend identity remains ASVS) | SR, SA, SD, RT, ST | PARTIAL. Native biometric/local authentication, backend identity proof, MFA lifecycle, recovery, and tenant identity trust must be separated. MASVS does not replace backend authorization testing. |
| GDES-SEC-003 Authorization & Privilege Control | V8.1.1–V8.4.2; V4.1.1–V4.1.5; token claims V9.2.1–V9.2.4 where applicable | AUTH-1, AUTH-3, PLATFORM-1 | V2.4.1–V2.4.7; V4.5.1–V4.5.5 | SR, SA, AA, RT, ST | PARTIAL. Server-side object/tenant/site authorization, separation of duties, deny-by-default, and cross-tenant negative tests need explicit GDES acceptance criteria. |
| GDES-SEC-004 Input, Output & Injection Defense | V1.1.1–V1.2.10; V1.3.1–V1.3.12; V1.5.1–V1.5.3; V2.1.1–V2.3.5; V5.2.1–V5.2.6 | CODE-4, PLATFORM-2, PLATFORM-3 | V4.1.1–V4.1.8; V4.3.1–V4.3.4 | SA, SB, RT, ST | PARTIAL. OS-specific parser, IPC, clipboard, file import, command-line and deserialization surfaces need per-platform test selection. |
| GDES-SEC-005 API, Integration & Network Security | V4.1.1–V4.4.4; V10.2.1–V10.6.2; V12.1.1–V12.3.5 | NETWORK-1, NETWORK-2, PLATFORM-1, PLATFORM-2 | V6.1.1–V6.5.2; V4.5.1–V4.5.5 | SA, SD, RT, ST, EM | PARTIAL. SSRF, DNS rebinding, outbound allowlists, redirect revalidation, API authorization, and service-to-service trust require explicit GDES tests. |
| GDES-SEC-006 Cryptography & Sensitive Data Protection | V11.1.1–V11.7.2; V12.1.1–V12.3.5; V14.2.1–V14.2.8 | CRYPTO-1, CRYPTO-2, STORAGE-1, STORAGE-2 | V3.1.1–V3.5.4; V5.1.1–V5.6.4; V6.1.1–V6.1.3 | SA, SB, SD, EM | PARTIAL. GDES data classification, key custody, rotation, retention, deletion, and business-sensitive evidence controls require local policy and review. |
| GDES-SEC-007 Secrets & Secure Configuration | V13.1.1–V13.4.7; V15.2.1–V15.2.5 | CODE-3, STORAGE-1, CRYPTO-2 | V2.1.1–V2.1.8; V2.3.1–V2.3.6; V2.4.5; V3.3.1–V3.3.4 | PC, SB, SD, EM | PARTIAL. CI secret scanning, deployment secret injection, environment separation, client-bundle inspection, and config drift evidence need pipeline/runtime acceptance criteria. |
| GDES-SEC-008 Database & Tenant Data Integrity | V1.2.1–V1.2.10; V2.3.1–V2.3.5; V8.1.1–V8.4.2; V14.1.1–V14.3.3; V15.4.1–V15.4.4 | STORAGE-1, STORAGE-2, AUTH-1, PRIVACY-1 | V3.1.1–V3.5.4; V2.4.5 | SA, RT, ST, EM, OM | **MAJOR GAP.** These references cover client data protection and application authorization but do not prove PostgreSQL RLS, composite tenant FKs, relational parity, transaction isolation, concurrency, temporal consistency, or authoritative server-side release decisions. Independent DB review and target-engine tests are mandatory. |
| GDES-SEC-009 Dependency & Software Supply Chain | V15.2.1–V15.2.5; V13.1.1–V13.1.4; V13.4.1–V13.4.7 | CODE-3, CODE-1, CODE-2 | V2.1.1–V2.1.8; V2.3.1–V2.3.6; V4.6.1–V4.6.8 | SB, SD, DM, EM | PARTIAL. SBOM, dependency integrity, provenance/attestation, signing custody, license policy, reproducible build and artifact-to-SHA linkage need project-level gates. |
| GDES-SEC-010 Logging, Monitoring & Error Handling | V16.1.1–V16.5.4; V13.4.1–V13.4.7 | STORAGE-2, PRIVACY-3, PRIVACY-4 | V3.5.1–V3.5.4 (local residual-data handling; not a full logging standard) | PC, DM, IM, EM, OM | PARTIAL. Security event taxonomy, alerting, log access, retention, incident correlation, and privacy-safe monitoring are primarily GDES/SAMM operational requirements. |
| GDES-SEC-011 Verification, Resilience & Incident Readiness | V2.3.1–V2.3.5; V15.1.1–V15.2.5; V15.3.1–V15.3.7; V15.4.1–V15.4.4; V16.3.1–V16.3.4 | RESILIENCE-1, RESILIENCE-2, RESILIENCE-3, RESILIENCE-4, CODE-2, CODE-3 | V1.2.1–V1.2.4; V2.1.1–V2.1.8; V2.3.1–V2.3.6; V4.4.1–V4.4.3; V4.6.1–V4.6.8 | AA, RT, ST, DM, IM, EM, OM | PARTIAL. Security test execution, vulnerability disposition, incident drills, backup/restore, RTO/RPO, rollback and release authorization need explicit evidence. |

## 4. MASVS full control inventory and traceability requirement

The pinned MASVS YAML contains 24 controls across eight groups:

| MASVS group | Control IDs |
|---|---|
| STORAGE | MASVS-STORAGE-1, MASVS-STORAGE-2 |
| CRYPTO | MASVS-CRYPTO-1, MASVS-CRYPTO-2 |
| AUTH | MASVS-AUTH-1, MASVS-AUTH-2, MASVS-AUTH-3 |
| NETWORK | MASVS-NETWORK-1, MASVS-NETWORK-2 |
| PLATFORM | MASVS-PLATFORM-1, MASVS-PLATFORM-2, MASVS-PLATFORM-3 |
| CODE | MASVS-CODE-1, MASVS-CODE-2, MASVS-CODE-3, MASVS-CODE-4 |
| RESILIENCE | MASVS-RESILIENCE-1, MASVS-RESILIENCE-2, MASVS-RESILIENCE-3, MASVS-RESILIENCE-4 |
| PRIVACY | MASVS-PRIVACY-1, MASVS-PRIVACY-2, MASVS-PRIVACY-3, MASVS-PRIVACY-4 |

Required traceability chain for mobile controls:

`GDES-SEC-ID → MASVS control → MASWE-xxxx weakness (where applicable) → MASTG v2 test ID → Android/iOS execution record → evidence digest → reviewer disposition`

MASWE 1.0.0 is a stable catalogue with identifiers MASWE-0001 through MASWE-0078. MASTG 2.0.0 is the first stable release of the refactored test guide. The full MASWE/MASTG leaf-level mapping is intentionally not fabricated in this matrix: it must be generated from the pinned MASWE/MASVS/MASTG source data and selected for the app's actual features, permissions, storage, authentication, network, and platform APIs. Until that is completed, mobile test mapping remains **PARTIAL**.

## 5. SAMM practice coverage matrix

| SAMM business function | Practice | GDES controls informed | Relationship |
|---|---|---|---|
| Governance | Strategy & Metrics (SM) | SEC-001, SEC-011 | informs |
| Governance | Policy & Compliance (PC) | SEC-001, SEC-007, SEC-010 | informs |
| Governance | Education & Guidance (EG) | SEC-001, SEC-011 | informs |
| Design | Threat Assessment (TA) | SEC-001, SEC-011 | informs |
| Design | Security Requirements (SR) | SEC-001, SEC-002, SEC-003 | informs |
| Design | Secure Architecture (SA) | SEC-001–SEC-008 | informs |
| Implementation | Secure Build (SB) | SEC-004, SEC-006, SEC-007, SEC-009 | informs |
| Implementation | Secure Deployment (SD) | SEC-002, SEC-005, SEC-006, SEC-007, SEC-009 | informs |
| Implementation | Defect Management (DM) | SEC-009, SEC-010, SEC-011 | informs |
| Verification | Architecture Assessment (AA) | SEC-001, SEC-003, SEC-011 | informs |
| Verification | Requirements-driven Testing (RT) | SEC-002–SEC-006, SEC-008, SEC-011 | informs |
| Verification | Security Testing (ST) | SEC-002–SEC-009, SEC-011 | informs |
| Operations | Incident Management (IM) | SEC-010, SEC-011 | informs |
| Operations | Environment Management (EM) | SEC-005–SEC-010 | informs |
| Operations | Operational Management (OM) | SEC-008, SEC-010, SEC-011 | informs |

SAMM is a maturity model with five business functions and fifteen practices. This mapping identifies organizational practices that support GDES controls; it does not assert a SAMM maturity level or make SAMM a substitute for ASVS/MASVS/TCASVS test evidence.

## 6. Coverage and gap register

| Gap ID | Gap | Impact | Required closure evidence | Status |
|---|---|---|---|---|
| MAP-GAP-001 | Exact MASWE weakness IDs and MASTG v2 test IDs not yet mapped to all applicable MASVS controls | Mobile control coverage cannot be declared complete | Machine-readable control→weakness→test crosswalk and Android/iOS test applicability | OPEN |
| MAP-GAP-002 | SAMM exact release commit and all practice/stream activity references not frozen in this artifact | Maturity crosswalk is name-level, not activity-level | v2.2.0 source commit, stream IDs, activity/question references | OPEN |
| MAP-GAP-003 | ASVS section ranges are pinned to CSV; each project-specific applicability decision and verification level remains to be recorded | Cannot infer every requirement applies to every product | Requirement-level applicability register with L1/L2/L3, rationale and owner | OPEN |
| MAP-GAP-004 | TCASVS project card still advertises 1.8 while repository source declares 5.0.0 | Metadata ambiguity | Standards Owner acceptance of repository 5.0.0 pin and source SHA | OPEN |
| MAP-GAP-005 | Database-specific tenant integrity and PostgreSQL controls are not fully covered by the four requested frameworks | Critical database assurance gap | GDES DB control supplement; independent DB review; target-engine tests for RLS, composite FKs, transaction/concurrency, negative access | OPEN |
| MAP-GAP-006 | Logging/monitoring, incident response, backup/restore, rollback, release authority, and audit evidence are only partially covered by product standards | Operational security remains GDES-specific | Operational control supplement, drills, evidence and reviewer sign-off | OPEN |
| MAP-GAP-007 | Canonical legacy wording for GDES-SEC-001–011 and GDES-MS-SEC/DB/GC rows not yet reconciled against source workbook | Control identity and backward compatibility uncertain | Workbook row IDs, original wording, mapping decision log | OPEN |
| MAP-GAP-008 | Independent Security Reviewer and Database Reviewer are not appointed | No independent review assurance | Named reviewer acceptance, conflict-of-interest check, review comments and disposition | BLOCKED |

## 7. Independent review protocol and review record

### Required reviewers

1. **Independent Security Reviewer:** must not be the sole author/implementer of this matrix. Must challenge every direct `covers` or `partially_covers` relation, verify upstream IDs, applicability, verification levels, and missing threat scenarios.
2. **Independent Database Reviewer:** must specifically review GDES-SEC-008 and the database/tenant acceptance criteria, including PostgreSQL RLS, composite foreign keys, constraints, transaction semantics, concurrency, temporal consistency, and cross-tenant negative tests.
3. **Standards Owner:** decides whether to accept the register after reviewer findings are dispositioned. The Standards Owner cannot substitute for independent technical review.

### Review checklist

- [ ] ASVS tag v5.0.0, CSV blob SHA, license and requirement IDs verified.
- [ ] ASVS requirement applicability and verification levels selected per system.
- [ ] MASVS 24 control IDs verified against pinned YAML.
- [ ] MASWE 1.0.0 weaknesses mapped to applicable MASVS controls.
- [ ] MASTG v2.0.0 test IDs mapped to each applicable mobile weakness and Android/iOS target.
- [ ] TCASVS 5.0.0 repository release and six chapter source pins verified.
- [ ] TCASVS version-card discrepancy formally dispositioned.
- [ ] SAMM v2.2.0 commit, all 15 practices, streams and activity IDs verified.
- [ ] Database-specific gaps reviewed by independent Database Reviewer.
- [ ] Every gap has owner, due date, remediation or explicit risk disposition.
- [ ] Reviewer comments and changes are recorded.
- [ ] Standards Owner decision is explicit and versioned.

### Review result

| Review | Reviewer | Result | Date | Evidence |
|---|---|---|---|---|
| Security crosswalk review | Not appointed | **NOT STARTED / BLOCKED** | — | No independent review evidence |
| Database crosswalk review | Not appointed | **NOT STARTED / BLOCKED** | — | No independent review evidence |
| Standards Owner decision | MUCHLIS BSTG | **NOT APPROVED** | — | Awaiting independent review |

## 8. Exit gate before SDLC Register v1.0

The Cybersecurity mapping gate is **NOT CLEARED** until all of the following are true:
1. MAP-GAP-001 through MAP-GAP-007 are closed or have formally approved, time-bounded exceptions.
2. MAP-GAP-008 is resolved by appointment and completion of independent reviews.
3. Reviewers provide written coverage disposition and identify any unmapped requirements.
4. Database reviewer explicitly signs off the database scope or records blockers.
5. Standards Owner records the final decision.

Drafting SDLC may be planned, but the next formal domain register is not to be treated as authorized by this matrix until the gate is cleared.

**Current overall result: TECHNICAL CROSSWALK CREATED — COVERAGE PARTIAL — INDEPENDENT REVIEW BLOCKED — NOT APPROVED.**
