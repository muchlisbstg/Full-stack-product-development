# GDES-SEC-ACCEPTANCE-MATRIX-001
## Canonical Cybersecurity Acceptance Criteria Matrix

| Metadata | Value |
|---|---|
| Artifact ID | GDES-SEC-ACCEPTANCE-MATRIX-001 |
| Version | 1.0 |
| Status | **DRAFT — NOT APPROVED — NOT EXECUTED** |
| Parent | GDES-SEC-DICT-001 proposed dictionary |
| Scope | Web, API, Android, iOS, Desktop, PostgreSQL and SQLite where applicable |
| Review | Independent Security and Database reviewers required |

> This matrix defines acceptance criteria and evidence requirements only. No test execution, PASS, independent review, or product conformance is asserted.

## 1. Result semantics

- PASS: exact acceptance test executed and evidence meets expected outcome.
- FAIL: test executed and expected outcome not met.
- NOT TESTED: not executed or evidence insufficient.
- BLOCKED: cannot execute because environment, permission, reviewer or prerequisite is unavailable.
- NOT APPLICABLE: authorized applicability decision with rationale.
- APPROVED: explicit decision by authorized human; never inferred from PASS or green CI.

Each evidence record must include: control/test ID, repository, branch, commit SHA, build/artifact digest, environment, tool/version, procedure, expected/actual result, timestamp, logs/artifacts, author, reviewer and limitations.

## 2. Application security acceptance matrix

| Test ID | Canonical control | Positive acceptance criteria | Negative / abuse cases and expected result | Required evidence |
|---|---|---|---|---|
| SEC-AC-001 | GDES-SEC-001 | Assets, trust boundaries, data flows, threats, severity, owner and treatment are documented for each material system/change. | Unowned critical threat, undocumented trust boundary or unapproved residual risk blocks gate. | Threat model, data-flow diagram, risk register, review record |
| SEC-AC-002 | GDES-SEC-002 | Authentication, MFA policy, recovery, session expiry/revocation, token audience/issuer and service identity are verified. | Invalid, expired, revoked, malformed, wrong-audience or replayed credential is denied; no session is issued. | Auth integration tests, redacted config, sanitized traces |
| SEC-AC-003 | GDES-SEC-003 | Every protected endpoint/action checks subject, role, tenant, site, resource ownership and action server-side. | Forged tenant/user/role/site, privilege escalation, IDOR/BOLA and cross-tenant requests are denied with no state change or sensitive disclosure. | Automated negative tests, authorization matrix, API traces |
| SEC-AC-004 | GDES-SEC-004 | Input schemas, types, size limits, parsing, output encoding and parameterized data access are verified. | SQL/NoSQL/command injection, XSS, malformed JSON, unsafe deserialization, path traversal and oversized input are rejected/safely handled. | Unit/integration/security tests, sanitized payloads |
| SEC-AC-005 | GDES-SEC-005 | TLS/endpoint validation, timeouts, redirect policy, service authentication and outbound network policy are documented and tested. | SSRF to loopback/private/link-local/metadata targets, DNS rebinding, redirect-to-internal and unauthorized egress are blocked. | API/network tests, egress policy, sanitized network traces |
| SEC-AC-006 | GDES-SEC-006 | Data classification, purpose, minimization, access, encryption, retention and deletion controls match documented policy. | Unauthorized export, excessive collection, access after deletion/retention expiry or disclosure to unapproved recipient is denied/detected. | Data inventory, flow map, privacy review, retention/deletion tests |
| SEC-AC-007 | GDES-SEC-007 | Secret injection, storage, rotation, access and environment separation are controlled. | Secret scanner, repository scan, client bundle inspection and log inspection find no exposed active secret; any exposure blocks release and triggers rotation. | Scanner reports, bundle inspection, redacted configuration and rotation record |
| SEC-AC-008 | GDES-SEC-008 | Direct/transitive dependency inventory, vulnerability and license disposition, provenance and artifact digest are recorded. | Unreviewed critical/high risk dependency, prohibited license, unverifiable artifact or source/artifact mismatch blocks release or requires authorized exception. | SBOM, scanner/license reports, build provenance, digest |
| SEC-AC-009 | GDES-SEC-009 | Security events are attributable, time-consistent, access-controlled and privacy-aware; alert paths are tested. | Logs must not contain credentials, tokens, private keys or excessive personal data; unsafe errors/stack traces are not returned to clients. | Sanitized logs, alert test, retention/access policy |
| SEC-AC-010 | GDES-SEC-010 | Risk-based test plan, findings, remediation, retest and evidence chain are complete for release scope. | Missing evidence, mismatched SHA/environment, suppressed finding, unapproved exception or untested critical path prevents PASS. | Test matrix, immutable evidence index, findings and retest records |
| SEC-AC-011 | GDES-SEC-011 | Incident roles, escalation, containment, communications, recovery objectives, backup/restore and rollback are documented and exercised. | Restore failure, missing accountable responder, inaccessible backup or untested rollback is recorded as FAIL/BLOCKED according to execution. | Incident runbook, tabletop/exercise report, restore and rollback evidence |

## 3. Database acceptance matrix

| Test ID | Canonical control | Positive acceptance criteria | Negative / abuse cases and expected result | Required evidence |
|---|---|---|---|---|
| DB-AC-001 | GDES-DB-001 | PK, FK, unique, check, not-null and required composite relationships match canonical data model. | Orphan, duplicate, invalid enum/range, null-required and cross-tenant FK insertion fails at authoritative DB boundary. | Schema/catalog dump, constraint tests, migration diff |
| DB-AC-002 | GDES-DB-002 | Tenant identity is derived from trusted server context; RLS and composite tenant/resource keys enforce isolation where supported. | Forged tenant context, missing tenant claim, cross-tenant SELECT/INSERT/UPDATE/DELETE, owner bypass and role escalation are denied. | RLS policies, role catalog, SQL negative tests, DB logs |
| DB-AC-003 | GDES-DB-003 | Transactions preserve documented invariants under concurrent writes, retries, duplicate requests and time boundaries. | Race condition, lost update, double settlement, duplicate side effect, stale write and partial transaction cannot violate invariant. | Target-engine concurrency tests, isolation settings, traces |
| DB-AC-004 | GDES-DB-004 | Services use dedicated least-privilege DB roles; owner/admin roles are separated; credentials are managed outside source. | Application role cannot alter schema, bypass RLS, access unrelated schemas or assume privileged role. | Role grants, privilege queries, redacted connection config, audit logs |
| DB-AC-005 | GDES-DB-005 | Migration is versioned/reviewed, backup and restore are verified, rollback strategy exists, and engine-specific differences are documented. | Unapproved DDL/destructive operation is blocked; restore mismatch, migration drift or SQLite/PostgreSQL behavioral divergence fails the relevant check. | Migration inventory, backup/restore report, schema parity and rollback evidence |

## 4. Cross-platform coverage

| Platform | Minimum verification |
|---|---|
| Web | Browser bundle secret inspection; browser session/cookie and CSRF controls; API authorization; CSP/security headers where applicable; XSS and client trust boundary |
| Android | MASVS/MASTG Android tests; secure storage/Keystore; exported components/IPC; WebView; network; backup; debug/release configuration |
| iOS | MASVS/MASTG iOS tests; Keychain/Data Protection; URL schemes/universal links; IPC/pasteboard; WebView; network; backup; debug/release configuration |
| Desktop | OS credential store; local file/IPC/deep-link/update mechanisms; code signing and update provenance; local privilege boundary; network and API |
| Backend/API | ASVS requirements; identity and object authorization; tenant/site boundaries; rate/abuse controls; secrets; outbound network |
| Database | Engine-native constraints, RLS/roles, transaction isolation, concurrency, restore and cross-engine parity |

A shared feature claim requires evidence on every declared platform. Static configuration review is not runtime proof.

## 5. Severity and release disposition

| Severity | Default treatment |
|---|---|
| Critical | Block release/approval; contain exposure; remediation and independent retest required |
| High | Block release unless documented compensating controls and explicit risk acceptance by authorized owner |
| Medium | Tracked remediation with owner/date; disposition based on exploitability and impact |
| Low/Informational | Record and disposition; aggregate patterns may elevate risk |

Exceptions require scope, rationale, impact, compensating controls, risk owner, authorized approver, effective/expiry dates and closure evidence. Implementers and AI agents cannot approve their own exceptions.

## 6. Evidence template

| Field | Required value |
|---|---|
| Evidence ID | Unique immutable ID |
| Test/control | Canonical ID and test ID |
| Source | Repository, branch, commit SHA |
| Artifact | Build identifier and digest if applicable |
| Environment | Disposable/local/CI/staging/production explicitly distinguished |
| Procedure | Exact reproducible steps and tool/version |
| Outcome | Expected, actual, PASS/FAIL/BLOCKED/NOT TESTED |
| Evidence | Logs/report/screenshot/digest, redacted |
| Accountability | Author, independent reviewer, date |
| Limitations | Coverage exclusions, flaky tests, assumptions, known gaps |

**Current status: ALL TESTS NOT TESTED unless separate execution evidence is linked.**
