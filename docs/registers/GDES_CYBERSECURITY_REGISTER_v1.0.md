# GDES Cybersecurity Register v1.0 — Draft for Review

| Metadata | Value |
|---|---|
| Register ID | GDES-SEC-REG-001 |
| Version | 1.0 |
| Status | DRAFT — NOT APPROVED |
| Domain priority | P1 — first domain register |
| Standards Owner | MUCHLIS BSTG |
| Parent | GDES Master Standard v1.0 — Draft for Review |
| Repository / branch | muchlisbstg/Full-stack-product-development / gdes/ai-governance-v1-pilot |
| Effective date | Not assigned |
| Independent Security Reviewer | Not yet appointed |
| Independent Database Reviewer | Not yet appointed; required for database controls |

> This is a working register and mapping baseline, not a certification, completed security audit, or approved policy. Mapping does not prove implementation, test execution, PASS, or APPROVED.

## 1. Purpose and scope

This register establishes traceable cybersecurity controls for GDES-adopting products and repositories. It maps the existing GDES-SEC-001–011 baseline provisionally to OWASP ASVS 5.0, OWASP SAMM 2.2, and the OWASP Cheat Sheet Series.

Scope includes Web, Mobile, Desktop, backend/API, identity and access, tenant/resource isolation, input/output, integrations, network, cryptography, secrets, data protection, databases, dependencies, logging, security verification, incident readiness, and evidence.

Applicability MUST be assessed per system, data classification, trust boundary, threat model, and jurisdiction. Conditional controls require a recorded applicability decision; they are not silently waived.

## 2. Classification and status

**Classification**
- Mandatory Standard — minimum GDES control proposed for adopting projects; Draft until approved.
- Recommended Practice — preferred method; not mandatory solely because it is listed.
- Optional Tool — optional technology subject to security, compatibility, license, and cost review.
- Regional Addendum — jurisdiction-specific legal or regulatory requirement.

**Evidence status**
- NOT STARTED, IN PROGRESS, NOT TESTED, PASS, FAIL, BLOCKED, NOT APPLICABLE, APPROVED, REJECTED.
- PASS requires execution and evidence against acceptance criteria.
- APPROVED / REJECTED requires an explicit decision by an authorized human.
- Initial status for all controls is NOT TESTED. No implementation or test outcome is asserted.

## 3. Reference frameworks

| Reference | Purpose | Target version | GDES classification | Boundary |
|---|---|---|---|---|
| OWASP ASVS — https://github.com/OWASP/ASVS | Primary catalogue of verifiable application security requirements | 5.0 | Mandatory GDES mapping baseline proposed | Tailor by application type and risk; do not adopt blindly |
| OWASP SAMM — https://github.com/OWASP/samm | Security maturity assessment and improvement roadmap | 2.2 | Recommended Practice | Maturity scoring is not proof that individual controls pass |
| OWASP Cheat Sheet Series — https://github.com/OWASP/CheatSheetSeries | Implementation guidance for security topics | Rolling upstream project | Recommended Practice | Guidance informs implementation; it does not replace testable GDES criteria |

The version labels are selected reference targets, not proof that exact source snapshots or license terms have been verified for this register revision. Before adoption, record exact tag/release or commit SHA, retrieval date, upstream LICENSE file, attribution/share-alike obligations, and relevant requirement identifiers. Write original GDES control wording; do not reproduce upstream material wholesale. Legal review is required before substantial redistribution or adaptation.

## 4. Control register

The following titles normalize the known GDES-SEC-001–011 baseline into an initial mapping structure. The original detailed source register was not recovered in this repository review. Therefore titles and statements below are provisional working descriptions and MUST be reconciled against the canonical source workbook before legacy wording is considered preserved.

| GDES ID | Proposed control title | Mandatory control statement — Draft | Priority |
|---|---|---|---|
| GDES-SEC-001 | Security Governance & Threat Modeling | MUST define system boundaries, assets, threat actors, trust boundaries, security assumptions, risk owners, and treatment decisions before material release or exposure changes. | P1 |
| GDES-SEC-002 | Identity & Authentication | MUST authenticate identities at trusted boundaries and protect credentials, recovery flows, sessions, and token lifecycle. | P1 |
| GDES-SEC-003 | Authorization & Privilege Control | MUST enforce authorization server-side for every protected action/resource, deny by default, and test horizontal and vertical privilege boundaries. | P1 |
| GDES-SEC-004 | Input, Output & Injection Defense | MUST validate untrusted input at trust boundaries, encode output by context, and use safe parameterization and parsing. | P1 |
| GDES-SEC-005 | API, Integration & Network Security | MUST protect service interfaces and outbound connections with authenticated, authorized, bounded, securely configured communication; assess SSRF, redirects, and DNS behavior where relevant. | P1 |
| GDES-SEC-006 | Cryptography & Sensitive Data Protection | MUST classify sensitive data and apply approved cryptographic protections and key-handling practices proportionate to sensitivity and threat. | P1 |
| GDES-SEC-007 | Secrets & Secure Configuration | MUST keep secrets out of source, client bundles, logs, and unauthorized stores; apply secure defaults and restrict administrative configuration. | P1 |
| GDES-SEC-008 | Database & Tenant Data Integrity | MUST enforce data ownership, tenant/resource isolation, integrity constraints, and transaction semantics in trusted backend/database layers; client-supplied tenant identity MUST NOT be authoritative. | P1 |
| GDES-SEC-009 | Dependency & Software Supply Chain | MUST inventory material dependencies/build inputs, assess vulnerabilities and licenses, and preserve source/build/release provenance. | P1 |
| GDES-SEC-010 | Security Logging, Monitoring & Error Handling | MUST record security-relevant events with privacy-aware retention, detect material abuse where feasible, and return safe errors without leaking secrets or sensitive internals. | P1 |
| GDES-SEC-011 | Security Verification, Resilience & Incident Readiness | MUST define risk-based security tests, negative-access cases, vulnerability disposition, incident response, backup/recovery, and rollback evidence appropriate to impact. | P1 |

Cross-reference candidates from the recovered master workbook: GDES-MS-SEC-001, GDES-MS-SEC-002, GDES-MS-DB-001, GC-04, GC-05, GC-06. Exact titles, full source wording, and one-to-one relationships remain unverified and must be reconciled against the workbook.

## 5. External mapping matrix — first-pass coverage test

Mapping relations:
- covers — upstream reference directly addresses the intent.
- partially_covers — upstream reference addresses only part of the intent.
- informs — guidance/maturity practice informs implementation but is not a direct verification requirement.
- not_applicable — assessed as irrelevant with rationale.

ASVS mappings below are chapter/domain-level only. Exact ASVS 5.0 requirement IDs are intentionally pending source pinning and reviewer verification.

| GDES ID | ASVS 5.0 domain | SAMM 2.2 practice area | Cheat Sheet guidance areas | Relation | Mapping test |
|---|---|---|---|---|---|
| GDES-SEC-001 | Architecture, security requirements, configuration, verification | Governance: Strategy & Metrics; Design: Threat Assessment | Threat Modeling; Secure Product Design | partially_covers | Partial: GDES risk ownership and approval evidence need local criteria |
| GDES-SEC-002 | Authentication, session, token and identity domains | Design: Secure Architecture; Implementation: Secure Build; Verification: Security Testing | Authentication; Password Storage; Session Management; JSON Web Token | covers | Provisional: verify exact ASVS requirement IDs and applicability |
| GDES-SEC-003 | Authorization and access-control domains | Design: Secure Architecture; Verification: Security Testing | Authorization; Access Control; REST Security | covers | Provisional: require horizontal/vertical and tenant-isolation negative tests |
| GDES-SEC-004 | Validation, encoding, injection and parser domains | Implementation: Secure Build; Verification: Security Testing | Input Validation; Cross Site Scripting Prevention; SQL Injection Prevention; Deserialization | covers | Provisional: context-specific acceptance tests required |
| GDES-SEC-005 | API/web service, secure communication, configuration and server-side request handling | Design: Secure Architecture; Implementation: Secure Deployment; Verification: Security Testing | REST Security; SSRF Prevention; TLS; DNS Rebinding | partially_covers | Partial: egress, DNS rebinding and redirect tests need explicit criteria |
| GDES-SEC-006 | Cryptography, data protection and secure communication | Design: Secure Architecture; Implementation: Secure Build | Cryptographic Storage; Key Management; Transport Layer Protection | covers | Provisional: algorithms, key lifecycle and data classification must be specified |
| GDES-SEC-007 | Configuration, secrets, deployment and secure defaults | Governance: Policy & Compliance; Implementation: Secure Deployment | Secrets Management; Docker Security; Configuration | covers | Provisional: secret scanning and effective runtime configuration evidence required |
| GDES-SEC-008 | Authorization, data protection, business logic and database-related requirements as applicable | Design: Secure Architecture; Verification: Security Testing | Database Security; Authorization; Multi Tenant Applications | partially_covers | Partial: constraints, RLS, transaction/concurrency and cross-tenant tests need explicit GDES criteria |
| GDES-SEC-009 | Architecture, dependency, configuration and secure build/release requirements as applicable | Implementation: Secure Build; Secure Deployment | Vulnerable Dependency Management; Software Supply Chain Security | partially_covers | Partial: provenance, SBOM, license review and artifact integrity need project criteria |
| GDES-SEC-010 | Logging, error handling, data protection and monitoring domains | Operations: Incident Management; Governance: Policy & Compliance | Logging; Error Handling; Logging Vocabulary | covers | Provisional: privacy-safe fields, alert thresholds and retention need system criteria |
| GDES-SEC-011 | Verification, business logic, configuration, resilience and operational security | Verification: Security Testing; Operations: Incident Management; Environment Management | Vulnerability Disclosure; Incident Response; Denial of Service Prevention | partially_covers | Partial: recovery objectives, rollback drills and evidence retention are GDES/project additions |

**Document-analysis result only:** 11/11 controls have at least one plausible reference mapping; 5/11 are marked partially_covers and 6/11 provisional covers. Zero controls are PASS. Exact upstream IDs, source pins, license snapshots, and legacy GDES source wording remain unverified. This is a plausibility/coverage test, not conformance testing or runtime security testing.

## 6. Acceptance criteria

| Test ID | Control area | Minimum acceptance criteria | Required evidence |
|---|---|---|---|
| SEC-T01 | Governance/threat model | Assets, trust boundaries, threats, severity, owner, and treatment decisions documented and reviewed | Threat model; risk register; review |
| SEC-T02 | Authentication/session | Positive/negative authentication, recovery, expiry/revocation, and token misuse cases behave as specified | Test results; redacted configuration; logs |
| SEC-T03 | Authorization | Forged identity, privilege escalation, IDOR/BOLA, cross-tenant/resource access, and unauthorized actions are denied server-side | Automated negative tests; API traces; reviewer report |
| SEC-T04 | Input/output | Injection, malformed input, encoding, parser abuse, and size-limit cases are safely handled | Test report; sanitized request/response samples |
| SEC-T05 | API/network | Authentication, authorization, TLS, timeout, redirect, destination validation, SSRF, and DNS rebinding tested where applicable | API tests; network policy/config; sanitized logs |
| SEC-T06 | Cryptography/data | Data inventory, crypto design, key storage/rotation/access, and transport protections meet documented policy | Data-flow map; crypto configuration; key-management review (no secret values) |
| SEC-T07 | Secrets/configuration | Secret scan findings are clean or dispositioned; client bundles/logs contain no secrets; runtime configuration verified without exposing values | Scanner output; bundle inspection; redacted config evidence |
| SEC-T08 | Database/tenant integrity | Constraints, transaction behavior, concurrency, temporal consistency, RLS/DB permissions where used, and cross-tenant tests meet criteria | Schema/catalog evidence; target-engine integration tests; independent DB review |
| SEC-T09 | Supply chain | Dependency inventory, vulnerability triage, license review, build provenance, artifact digest, and source-to-artifact linkage recorded | SBOM/inventory; scanner/license reports; build provenance |
| SEC-T10 | Logging/errors | Events are attributable; logs redact secrets/personal data; errors do not expose stack traces or credentials; alert/retention policy reviewed | Sanitized events; logging config; alert test; retention decision |
| SEC-T11 | Verification/resilience | Applicable tests executed; findings dispositioned; incident and recovery procedures documented and exercised at risk-appropriate level | Test matrix; findings register; incident/restore/rollback exercise |

Every test record MUST identify repository, branch, commit SHA, environment, tool/version, procedure, expected/actual result, evidence link/digest, execution time, and reviewer. Static inspection, unit, disposable integration, staging, and production runtime tests MUST be distinguished.

## 7. Minimum negative-access test catalogue

| ID | Scenario | Expected outcome |
|---|---|---|
| NEG-SEC-001 | Client forges tenant, enterprise, user, role, or site identity | Server rejects/ignores forged authority; no protected access |
| NEG-SEC-002 | Lower-privilege user directly invokes privileged endpoint | Denied server-side; no state change |
| NEG-SEC-003 | User changes resource ID to another user's/tenant's object | Denied without protected data disclosure |
| NEG-SEC-004 | Expired, revoked, malformed, or wrong-audience token is replayed | Denied; no sensitive error detail |
| NEG-SEC-005 | Injection, malformed JSON, oversized body, or unexpected content type | Safely rejected/handled; no unintended state change |
| NEG-SEC-006 | Integration URL targets loopback, private, link-local, metadata, or redirected internal destination | Blocked under reviewed outbound-network policy |
| NEG-SEC-007 | Secret appears in source, browser bundle, logs, or error response | Detection/release gate fails; secret not disclosed |
| NEG-SEC-008 | Concurrent updates or duplicate requests cross transaction boundaries | Defined consistency/idempotency invariant preserved |
| NEG-SEC-009 | Database role attempts to bypass tenant/row boundary | Database policy denies unauthorized rows/actions where required |
| NEG-SEC-010 | Dependency or artifact differs from reviewed source/provenance | Release gate blocks or records an authorized exception |

These are test specifications only. No execution is claimed.

## 8. Evidence register template

| Evidence ID | Control/test | Repository/scope | Branch | Commit SHA | Environment | Tool/version | Procedure | Expected/actual | Artifact URL/digest | Result | Author | Reviewer | Date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EVD-SEC-0001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | NOT TESTED | TBD | TBD | TBD |

Preserve raw evidence where safe; redact secrets and personal data. Link evidence to exact source SHA/environment. Record exclusions, flaky tests, and unresolved findings. Empty evidence fields are not evidence of compliance.

## 9. Findings and exceptions template

| Finding ID | Control | Severity | Description/impact | Assets | Root cause | Owner | Due date | Compensating control | Residual risk | Status | Approver/expiry |
|---|---|---|---|---|---|---|---|---|---|---|
| FIND-SEC-0001 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | OPEN | Not approved |

An exception requires documented rationale, exact scope, risk, compensating controls, accountable risk owner, authorized approver, approval evidence, effective date, expiry/review date, and closure evidence. Implementers and AI agents MUST NOT approve their own exceptions.

## 10. Review and approval

| Review dimension | Required party | Current status | Exit criteria |
|---|---|---|---|
| Legacy source reconciliation | Standards Owner / maintainer | PENDING | Recover original GDES-SEC-001–011 wording and reconcile master workbook IDs |
| ASVS mapping | Independent Security Reviewer | NOT STARTED | Verify exact v5 requirement IDs, applicability, gaps, and mapping relations |
| SAMM mapping | Independent Security Reviewer | NOT STARTED | Verify exact practice/stream references and maturity boundary |
| Cheat Sheet mapping | Security Reviewer | NOT STARTED | Verify exact guidance pages and source pins |
| Database controls | Independent Database Reviewer | NOT STARTED | Review integrity, tenant isolation, transaction, RLS, and negative-access criteria |
| Legal/licensing | Authorized legal reviewer where redistribution/adaptation is proposed | NOT STARTED | Verify licenses, attribution and permitted use |
| Standards approval | Standards Owner | NOT APPROVED | Findings dispositioned and explicit approval recorded |

## 11. Mapping validation procedure

1. Recover canonical workbook rows and reconcile GDES-SEC-001–011, GDES-MS-SEC-001/002, GDES-MS-DB-001, and GC-04/05/06.
2. Pin exact ASVS 5.0 and SAMM 2.2 tags/SHAs, Cheat Sheet Series commit SHA, license files, and retrieval date.
3. Replace chapter-level placeholders with exact upstream requirement/practice IDs and titles; record mapping relation and rationale.
4. Have an independent Security Reviewer challenge every covers claim and identify missing or duplicated coverage.
5. Verify every GDES control has measurable positive/negative criteria and evidence requirements.
6. Have an independent Database Reviewer validate database-specific criteria; SQLite-only tests are not proof of PostgreSQL RLS or target-database behavior.
7. Record gaps as findings; do not weaken controls merely to achieve complete mapping.
8. Request explicit Standards Owner approval only after independent review.

Checklist:
- [ ] Legacy GDES control wording recovered and reconciled.
- [ ] ASVS source tag/SHA, license and exact requirement IDs verified.
- [ ] SAMM source tag/SHA, license and practice references verified.
- [ ] Cheat Sheet commit and relevant guidance pages pinned.
- [ ] Every mapping relation challenged by independent Security Reviewer.
- [ ] Unmapped requirements and GDES-only controls recorded as gaps.
- [ ] Database criteria reviewed independently.
- [ ] Acceptance criteria and evidence schema reviewed.
- [ ] Standards Owner decision recorded.

## 12. Current disposition and next actions

**DRAFT FOR REVIEW — MAPPING BASELINE ONLY.**

| Action ID | Action | Owner | Exit evidence | Status |
|---|---|---|---|---|
| SEC-ACT-001 | Recover and reconcile legacy GDES security source | Standards Owner / maintainer | Source rows and reconciliation log | PENDING |
| SEC-ACT-002 | Pin upstream snapshots and licenses | Register maintainer | Tags/SHAs, license evidence, retrieval date | PENDING |
| SEC-ACT-003 | Complete requirement-level mapping and coverage challenge | Independent Security Reviewer | Reviewed matrix and gap log | NOT STARTED |
| SEC-ACT-004 | Validate database/tenant acceptance criteria | Independent Database Reviewer | Written review and test requirements | NOT STARTED |
| SEC-ACT-005 | Execute project-specific security tests | Authorized test operator | Reproducible evidence tied to SHA | NOT STARTED |
| SEC-ACT-006 | Resolve findings and obtain formal approval | Control owners + Standards Owner | Dispositions and approval evidence | NOT APPROVED |

**Gate to SDLC Register:** begin SDLC Register drafting after Cybersecurity mapping review has documented coverage, unresolved gaps, and reviewer disposition. Runtime tests need not all be complete before SDLC drafting, but no security control may be called PASS or APPROVED without its own evidence and decision.

**End of GDES Cybersecurity Register v1.0 — Draft for Review.**


## 13. External source verification update — 2026-11-11

A targeted source check identified important scope and version details that refine the first-pass mapping above.

### 13.1 Verified source pins and license evidence

| Reference | Verified source detail | License | Disposition |
|---|---|---|---|
| OWASP ASVS | Stable release 5.0.0; pin to tag v5.0.0. The release is structured as 17 chapters and requirement identifiers are version-dependent. | CC BY-SA 4.0 | Verified at project/release level; exact requirements still need row-by-row mapping |
| OWASP SAMM | Release v2.2.0; release page identifies commit 21352e0 | CC-BY-SA-4.0 | Version/release and license lead verified; exact practice/stream mapping still pending |
| OWASP Cheat Sheet Series | Official project repository and published guidance confirmed | CC BY-SA 4.0 | Guidance source verified; rolling repository commit must be pinned when a sheet is used |

ASVS 5.0.0 requirements use version-qualified identifiers such as v5.0.0-1.2.5. GDES MUST preserve the version prefix in all future mappings because ASVS identifiers can change between major releases.

ASVS 5.0.0 chapter index:
- V1 Encoding and Sanitization
- V2 Validation and Business Logic
- V3 Web Frontend Security
- V4 API and Web Service
- V5 File Handling
- V6 Authentication
- V7 Session Management
- V8 Authorization
- V9 Self-contained Tokens
- V10 OAuth and OIDC
- V11 Cryptography
- V12 Secure Communication
- V13 Configuration
- V14 Data Protection
- V15 Secure Coding and Architecture
- V16 Security Logging and Error Handling
- V17 WebRTC

### 13.2 Cross-platform coverage gap — mandatory mapping extension

ASVS is scoped to web applications and web services. It is not sufficient as the only security verification reference for a product that also ships native Android/iOS applications and desktop/thick-client software.

Add these supplementary reference frames:
- **Mobile:** OWASP MASVS, with MASWE as the mobile weakness taxonomy and MASTG as the test procedure library. Apply to Android and iOS clients. Exact release/tag and source license must be pinned in the next mapping revision.
- **Desktop / thick client:** OWASP TCASVS. Its repository and OWASP project card currently expose differing version labels (repository README identifies 5.0.0 while the OWASP project card identifies 1.8). Treat the version as **NOT RECONCILED**; do not assert a single adopted release until source maintainers' release metadata is checked. License is identified as CC BY-SA 4.0 in the project metadata.

This adds a clear scope condition to the mapping matrix in Section 5: its initial ASVS/SAMM/Cheat Sheet relationships are **web/API-oriented reference coverage only**. For the full GDES Web/Mobile/Desktop scope, every cross-platform control remains **PARTIAL / NOT TESTED** until MASVS/MASTG and TCASVS mappings are added and reviewed. The prior 11/11 plausibility count is not an end-to-end platform coverage score.

### 13.3 Mapping quality findings

| Finding ID | Severity | Finding | Required action | Status |
|---|---|---|---|---|
| FIND-SEC-MAP-001 | High | ASVS alone does not cover native mobile and thick-client desktop security scope | Add MASVS/MASWE/MASTG and TCASVS mapping tracks | OPEN |
| FIND-SEC-MAP-002 | Medium | Initial matrix uses chapter/domain-level ASVS references, not exact requirement IDs | Pin v5.0.0 source and map exact version-qualified IDs | OPEN |
| FIND-SEC-MAP-003 | Medium | TCASVS version metadata conflicts between OWASP project card and repository README | Reconcile release tag and source of truth before pinning | OPEN |
| FIND-SEC-MAP-004 | Medium | Initial GDES-SEC-001–011 descriptions are provisional because canonical legacy source rows were not recovered | Reconcile against recovered master workbook and any canonical source register | OPEN |
| FIND-SEC-MAP-005 | Medium | SAMM and Cheat Sheet mappings are practice/guidance references, not direct control verification | Record exact practice/stream or sheet URL and keep relation as informs unless direct coverage is justified | OPEN |

### 13.4 Updated mapping test outcome

- Source verification: ASVS 5.0.0 release and CC BY-SA 4.0 verified; SAMM v2.2.0 release/commit and CC-BY-SA-4.0 identified; Cheat Sheet Series official guidance and CC BY-SA 4.0 identified.
- Cross-platform scope: **GAP FOUND** — MASVS and TCASVS are required supplementary references for the declared mobile and desktop product scope.
- Requirement-level mapping: **NOT TESTED / INCOMPLETE** — exact ASVS requirement IDs and SAMM practice/stream IDs are not yet mapped.
- Legacy GDES control wording: **NOT RECONCILED**.
- Overall mapping result: **PARTIAL — NOT APPROVED**.
- No runtime security tests were executed as part of this source-mapping review.

### 13.5 Source links

- ASVS 5.0.0 downloads and release: https://asvs.owasp.org/downloads/
- ASVS v5.0.0 source and identifier guidance: https://github.com/OWASP/ASVS/tree/v5.0.0
- SAMM v2.2.0 release: https://github.com/owaspsamm/core/releases/tag/v2.2.0
- SAMM model: https://owaspsamm.org/model/
- Cheat Sheet Series: https://github.com/OWASP/CheatSheetSeries
- Cheat Sheet Series license/guidance: https://cheatsheetseries.owasp.org/
- MASVS: https://github.com/OWASP/masvs
- MASVS use and control groups: https://mas.owasp.org/MASVS/03-Using_the_MASVS/
- MASTG / MASWE project: https://mas.owasp.org/
- TCASVS: https://github.com/OWASP/TCASVS
- TCASVS OWASP project card: https://owasp.org/projects/thick-client-application-security-verification-standard



## 14. Detailed crosswalk and independent review gate — 2026-11-11

The detailed framework crosswalk is maintained separately to keep the control register readable:

- Mapping artifact: [GDES Cybersecurity Mapping Matrix v1.0](GDES_CYBERSECURITY_MAPPING_MATRIX_v1.0.md)
- Mapping ID: GDES-SEC-MAP-001
- Status: TECHNICAL MAPPING DRAFT — INDEPENDENT REVIEW NOT COMPLETED
- Matrix source pin includes ASVS v5.0.0 CSV, MASVS control YAML, TCASVS 5.0.0 six chapter sources, and SAMM v2.2.0 practice sources.

### Corrections and clarified source decisions

1. **ASVS:** exact requirement sections are now mapped for all 11 GDES controls using the v5.0.0 CSV. Serialized requirement identifiers MUST use OWASP's version-qualified format, e.g. `v5.0.0-1.2.5`. Section ranges in the mapping matrix preserve the chapter and section context.
2. **MASVS:** 24 controls across STORAGE, CRYPTO, AUTH, NETWORK, PLATFORM, CODE, RESILIENCE, and PRIVACY were extracted from the pinned YAML source. The exact MASWE-to-MASTG test leaf mapping remains open and must be selected per actual mobile feature/platform.
3. **TCASVS:** repository source declares stable 5.0.0, with six chapters and 130+ requirements. The OWASP project card still shows 1.8; the matrix resolves this by pinning the 5.0.0 repository chapter source and records the discrepancy for Standards Owner disposition.
4. **SAMM:** v2.2.0 practice sources were checked, including Threat Assessment (TA), Security Testing (ST), and Secure Build (SB). The matrix maps all 15 practice names; complete stream/activity/question source pins remain open.
5. **Database scope:** none of these mappings alone proves PostgreSQL RLS, composite tenant FKs, transaction isolation, concurrency, temporal consistency, or SQLite/PostgreSQL parity. These remain explicit GDES database acceptance requirements.

### Current gate outcome

- ASVS section-level requirement crosswalk: CREATED.
- MASVS 24-control crosswalk: CREATED.
- TCASVS 5.0.0 chapter/section crosswalk: CREATED.
- SAMM 15-practice crosswalk: CREATED at practice-name level.
- MASWE/MASTG leaf test selection: OPEN.
- SAMM stream/activity/question-level mapping: OPEN.
- Independent Security Review: NOT STARTED / BLOCKED — reviewer not appointed.
- Independent Database Review: NOT STARTED / BLOCKED — reviewer not appointed.
- Standards Owner approval: NOT APPROVED.
- Runtime testing: NOT TESTED.

**Overall: TECHNICAL MAPPING SUBSTANTIALLY STRUCTURED; COVERAGE PARTIAL; INDEPENDENT REVIEW BLOCKED; NOT APPROVED.**

Do not start the formal SDLC Register v1.0 gate until the mapping matrix's independent review, mobile leaf-test selection, SAMM stream/activity traceability, and database gap disposition are complete.
