# GDES-RFP-DB-001 — Independent Database Reviewer

| Metadata | Value |
|---|---|
| RFP ID | GDES-RFP-DB-001 |
| Version | 1.1 |
| Status | **REVISED DRAFT — OWNER REVIEWED — PROCUREMENT DEFERRED — NOT ISSUED** |
| Owner | MUCHLIS BSTG / GDES Standards Owner |
| Repository | `muchlisbstg/Full-stack-product-development` |
| Branch | `gdes/ai-governance-v1-pilot` |
| Related artifacts | `docs/GDES_MASTER_STANDARD_v1.0.md`; `docs/registers/GDES_CYBERSECURITY_REGISTER_v1.0.md`; `docs/registers/GDES_CYBERSECURITY_MAPPING_MATRIX_v1.0.md`; Export Client database and architecture evidence supplied separately |
| Currency | IDR; indicative planning estimates only |
| Procurement authority | None; procurement and budget approval deferred |
| Standards Owner disposition | Conditional acceptance of draft structure; revisions required before issue |

> **Governance notice:** This is an internal draft request-for-proposal template. It has not been issued to vendors, does not appoint a reviewer, does not approve expenditure, and does not authorize database access, data processing, DDL, migrations, writes, staging mutation, production access, or database sign-off. GDES Master Standard and related registers remain draft / not approved.

## 1. Purpose and procurement objective

Invite qualified independent database professionals to review the database architecture, data integrity controls, tenant isolation, and database-specific security acceptance criteria relevant to GDES and Export Client.

The review must focus on whether the proposed and evidenced design can enforce tenant/site boundaries and preserve relational and transactional integrity across the declared SQLite and PostgreSQL platforms. It must distinguish schema inspection from executed target-engine tests. A document review alone cannot prove runtime RLS behavior, concurrency safety, or database parity.

This is an **independent database assurance review**, not implementation, migration, DBA operations, performance tuning, certification, or approval of GDES.

## 2. Independence and reporting line

- Reviewer must be independent of the author, implementer, database designer, migration author, and delivery team for the artifacts under review.
- Reviewer must disclose current and prior financial, employment, advisory, family, subcontracting, and material commercial relationships with the project owner, implementers, vendors, and other reviewer.
- A person who designed or implemented a schema/control under review may not independently sign off that same work.
- Reviewer reports findings directly to the Standards Owner. Material disagreements and assumptions must be recorded.
- This engagement is separate from the Security Reviewer engagement. Database-specific assurance must not be delegated to the Security Reviewer by default.
- The Standards Owner retains final GDES decision authority. Reviewer opinion is advisory evidence and does not itself make a control PASS or APPROVED.

## 3. Scope of work

### 3.1 Data model and relational integrity

Review the supplied conceptual/logical/physical models, schema definitions, and evidence for:
- entity boundaries, ownership, cardinality, nullability, uniqueness, primary keys, foreign keys, check constraints, and referential actions;
- tenant, enterprise, transaction, site, party, user, role, and assignment relationships;
- composite foreign keys and whether tenant/site scope is enforced structurally rather than assumed by application convention;
- orphan prevention, cross-tenant relationship prevention, deletion/update behavior, and consistency across related records;
- schema parity and semantic equivalence between SQLite and PostgreSQL, including differences in types, constraints, defaults, collation, null handling, and conflict behavior.

### 3.2 Tenant isolation and database authorization

Review:
- PostgreSQL Row-Level Security policies, table ownership, FORCE ROW LEVEL SECURITY applicability, policy composition, role grants, bypass privileges, views, functions, SECURITY DEFINER functions, and connection/session context handling;
- resistance to forged tenant identity, missing tenant context, stale context, connection-pool context leakage, role escalation, and cross-tenant reads/writes;
- whether privileged service roles and administrative paths are narrowly scoped and auditable;
- whether application-level authorization is incorrectly assumed to substitute for database protections, or vice versa;
- whether SQLite controls and application access paths have clearly documented limitations and equivalent negative-access expectations.

### 3.3 Transaction semantics and temporal integrity

Review:
- transaction boundaries and atomicity for business operations;
- isolation levels, locking, concurrent updates, race conditions, deadlocks, retry behavior, and idempotency;
- temporal consistency, effective dates, event ordering, audit history, immutable records, and clock/time-zone assumptions;
- consistency between contract, item, obligation, evidence, payment ledger, and goods-release authorization records where those domain records are included in the supplied scope;
- failure handling, partial completion, duplicate requests, and recovery after interruption.

### 3.4 Database security and operational integrity

Review:
- least-privilege database roles, secrets boundary, TLS/network exposure, backup and restore controls, encryption responsibilities, audit logging, retention, and privileged access;
- migration discipline and schema version provenance, rollback/recovery design, and environment separation;
- whether evidence is tied to exact schema version, commit, database engine/version, configuration, test fixture, and test result;
- operational risks and controls not covered by ASVS/MASVS/TCASVS/SAMM that require GDES-specific requirements.

### 3.5 Test design and evidence review

Assess whether the supplied test strategy covers:
- positive and negative tenant/site access;
- missing, malformed, forged, stale, and switched tenant context;
- cross-tenant SELECT, INSERT, UPDATE, DELETE, JOIN, aggregate, and indirect relationship access;
- direct SQL paths and application-mediated paths;
- constraint enforcement and attempted invalid relationships;
- transaction rollback, duplicate submission, concurrent writes, race conditions, and temporal edge cases;
- equivalent expected outcomes on SQLite and PostgreSQL;
- backup/restore and recovery claims where evidence is supplied.

For each proposed test, review preconditions, test data, expected result, actual result, engine/version, execution method, logs, and evidence digest. Do not claim a test passed merely because a test case exists.

### 3.6 Findings and closure

Produce a prioritized findings register with severity, affected table/policy/constraint/control, evidence, impact, recommendation, owner role, and retest criteria. Retest remediation only if separately included in the agreed hours and explicitly authorized.

## 4. Explicit exclusions and safety constraints

Unless separately contracted and authorized, the engagement excludes:
- executing DDL, migrations, schema changes, seeds, backfills, destructive SQL, data deletion, or production writes;
- connecting to production, live customer data, payment systems, or real-money workflows;
- changing Supabase, PostgreSQL, SQLite, cloud, hosting, network, secrets, backup, or access configuration;
- active exploitation, load testing, denial-of-service, destructive concurrency tests, or unbounded query execution;
- source-code implementation, migration authorship, remediation execution, merge, or deployment;
- legal, regulatory, privacy-counsel, or Syariah opinions;
- certification or claims of compliance with ISO/IEC or other certification schemes.

Default review mode is read-only inspection of supplied documentation, schema exports, redacted configuration, source, and existing evidence. Any target-engine test requires a separate written plan, disposable isolated database, synthetic data, named credentials with least privilege, time limits, resource limits, backup/reset plan, and explicit approval. No production or staging mutation is authorized by this RFP.

## 5. Required competencies

### 5.1 Mandatory

- Demonstrable professional experience in PostgreSQL database architecture, database security, or data integrity engineering; target minimum 7 years or equivalent depth evidenced by comparable engagements.
- Practical experience with PostgreSQL RLS, roles/grants, policies, ownership/bypass risks, functions/views, connection pooling, and tenant isolation.
- Strong understanding of relational modeling, composite foreign keys, constraints, transaction isolation, concurrency, locking, temporal data, and recovery.
- Experience assessing multi-tenant SaaS systems and application/database authorization boundaries.
- Experience comparing SQLite with PostgreSQL or other materially different database engines, including behavioral and constraint parity.
- Ability to design and independently evaluate reproducible negative-access and integrity tests.
- Experience producing evidence-based database assessment reports and retest criteria.
- Written and spoken professional English sufficient to review technical standards; Indonesian communication is preferred.
- Signed NDA, conflict-of-interest declaration, and acceptance of scope/access restrictions.

### 5.2 Preferred credentials (not substitutes for experience)

Relevant PostgreSQL/vendor certifications, EDB/PostgreSQL training, database security credentials, AWS/Azure/GCP database credentials, or CISA/CISSP where supported by hands-on database experience. Candidates must state issuer, current status, and verification method. Certification alone is not sufficient.

## 6. Deliverables

| ID | Deliverable | Minimum content |
|---|---|---|
| DB-D01 | Inception and independence pack | Reviewer CV, credentials, COI declaration, NDA, confirmed scope, work plan |
| DB-D02 | Schema and evidence inventory | Artifact/version/SHA, engine/version, schema coverage, evidence gaps |
| DB-D03 | Relational integrity review | Entity/relationship review, PK/FK/composite FK/unique/check constraints and parity findings |
| DB-D04 | Tenant isolation and RLS review | Policy/role analysis, bypass paths, context handling, tenant/site negative-access coverage |
| DB-D05 | Transaction and temporal review | Atomicity, isolation, concurrency, idempotency, temporal consistency and recovery findings |
| DB-D06 | Cross-engine parity matrix | SQLite/PostgreSQL behavior, constraint and transaction parity, differences and test gaps |
| DB-D07 | Database findings register | Severity, affected object/control, evidence, impact, recommendation, owner role, retest criteria |
| DB-D08 | Executive report and closeout | Overall assurance, limitations, residual risks, walkthrough, unresolved disagreement log |
| DB-D09 | Retest addendum (if priced) | Retest of agreed evidence on authorized disposable target only |

Each conclusion must be labeled **verified by source inspection**, **verified by executed test**, **not verified**, **not applicable with rationale**, or **not tested**. A schema or policy file is not proof of runtime enforcement. Test results must identify exact engine/version, schema commit, environment, fixture, command/procedure, expected and actual outcomes, and evidence reference/digest.

## 7. Estimated effort and budget

All figures are planning assumptions for proposal comparison, not verified market quotations or approved expenditure.

| Work package | Estimated effort |
|---|---:|
| Inception, COI, evidence and schema inventory | 2–4 hours |
| Relational model, constraints and composite FK review | 4–6 hours |
| PostgreSQL RLS, roles, policies and tenant isolation | 5–8 hours |
| Transaction, concurrency and temporal integrity | 4–7 hours |
| SQLite/PostgreSQL parity and test-evidence review | 3–5 hours |
| Findings, report and walkthrough | 3–5 hours |
| **Indicative total** | **21–35 hours** |

| Pricing basis | Indicative range |
|---|---:|
| Target professional rate assumption | Rp1.800.000–Rp3.500.000/hour |
| Indicative base engagement | **Rp36.000.000–Rp112.000.000** |
| Approved budget / cap | **DEFERRED — NOT APPROVED** |
| Preferred commercial structure | Fixed fee with explicit hours, deliverables, assumptions, and exclusions |

No budget cap or procurement funding is approved at this stage. The rate and fee range above are non-binding market-planning assumptions only. Any future cap must be approved in writing before vendor outreach or award. A proposal that cannot meet the full agreed scope within a subsequently approved cap must be escalated; the reviewer must not silently omit RLS, composite FK, concurrency, temporal, or cross-engine parity review.

Vendor proposal must itemize professional fees, taxes, travel, platform fees, subcontracting, optional disposable-environment test work, retest, and out-of-scope rate. No expense is reimbursable without prior written approval.

## 8. Selection criteria

| Criterion | Weight |
|---|---:|
| PostgreSQL RLS, roles/policies and tenant isolation expertise | 25% |
| Relational integrity, composite FK and data modeling depth | 20% |
| Transaction, concurrency and temporal integrity experience | 20% |
| SQLite/PostgreSQL parity and reproducible testing | 15% |
| Independence, COI transparency and professional ethics | 10% |
| Evidence/report quality and commercial clarity | 10% |
| **Total** | **100%** |

Minimum recommended threshold: 75/100, with no unresolved material conflict of interest and no failure of mandatory requirements. The owner may reject all proposals. Credential claims must be checked with the issuing body or another reliable verification method where available; references must be independently contacted with the candidate's permission. Candidates should be asked to explain, using a sanitized scenario, how they would detect tenant-context leakage through pooled connections and how they would test RLS bypass paths without modifying a live database. Ask for an explicit test matrix covering at minimum: (a) missing tenant context, (b) forged tenant identifier, (c) stale context after connection reuse, (d) switching tenant context within a pooled connection, (e) table owner / BYPASSRLS / privileged-role paths, (f) SECURITY DEFINER and view/function paths, (g) cross-tenant SELECT/INSERT/UPDATE/DELETE and joins, and (h) expected-deny assertions with reproducible evidence. Tests must be proposed for an isolated disposable target only; no live database testing is authorized.

## 9. Acceptance criteria

A deliverable is accepted only when all applicable criteria below are satisfied:

- [ ] Reviewer identity, qualifications, references, NDA, and COI declaration are complete and verified to the owner's reasonable satisfaction.
- [ ] Reviewer confirms independence and documents any limitation.
- [ ] Scope, methodology, source artifacts, database engines/versions, exclusions, and review period are explicit.
- [ ] Relevant tables, relationships, constraints, indexes, policies, roles, functions, and access paths are inventoried or omissions are stated.
- [ ] Tenant/site integrity is assessed, including composite FK requirements and cross-tenant relationship prevention.
- [ ] PostgreSQL RLS policy design, role ownership, bypass privileges, session context, pooling, and privileged paths are assessed where evidence is available.
- [ ] SQLite/PostgreSQL parity is assessed for schema constraints and relevant transaction behavior; unsupported parity claims are identified.
- [ ] Transaction atomicity, concurrency, temporal consistency, idempotency, and failure recovery are addressed.
- [ ] Positive and negative test coverage is reviewed; missing test cases and unsafe test assumptions are recorded.
- [ ] Source inspection is clearly separated from tests actually executed on a target engine.
- [ ] Every finding has a unique ID, severity rationale, affected object/control, evidence/reference, impact, recommendation, and retest condition.
- [ ] Evidence gaps, environment limitations, and untested areas are explicit; no unsupported PASS or compliance claim is made.
- [ ] Final report includes executive summary, technical detail, residual risks, limitations, and unresolved disagreements.
- [ ] Findings walkthrough is completed and owner comments are recorded.
- [ ] Final files are delivered in agreed editable and archival formats and accepted in writing by the authorized owner.

Acceptance of the report does **not** mean database controls pass, schema changes are authorized, or GDES is approved. Control closure requires target-engine evidence where applicable and authorized disposition.

## 10. NDA, confidentiality, and data handling

Before receiving non-public project material, the selected reviewer must execute a mutually reviewed NDA that includes:
- purpose limitation: use information only to perform this engagement;
- confidentiality covering schema, source code, architecture, security findings, credentials, personal data, business information, and unpublished standards;
- least-privilege access and named personnel only;
- prohibition on sharing, subcontracting, uploading to public repositories, or using project material to train public or third-party AI models without explicit written permission;
- no copying or retaining secrets; reviewer must not request production credentials;
- secure storage, encryption in transit and at rest, access logging where available, and prompt incident notification;
- no disclosure of vulnerabilities or data to third parties without written authorization, except where applicable law requires otherwise;
- return or verified deletion of project data at engagement end, subject to narrowly defined legal retention obligations;
- ownership and permitted use of deliverables, pre-existing tools, and generic know-how;
- term, permitted disclosures, breach notification, governing law, and dispute process to be completed by qualified counsel.

Use synthetic fixtures and redacted schema/configuration where possible. No live personal or customer data should be provided unless separately justified, minimized, and explicitly authorized.

## 11. Conflict-of-interest declaration

Each proposed reviewer and subcontractor must declare:
1. current or recent employment, consulting, implementation, DBA, migration, audit, investment, or commercial relationship with the owner, project, implementation vendors, and related reviewers;
2. authorship or implementation of any reviewed schema, RLS policy, migration, data model, test, or evidence;
3. financial interest in a database, hosting, security, or consulting product/service that may be recommended;
4. personal relationships or other circumstances that could reasonably impair impartiality;
5. any restriction on reporting adverse findings.

The declaration must identify parties, dates, nature of relationship, affected scope, and proposed mitigation. It must cover all current relationships and relevant relationships, engagements, and financial interests during at least the preceding 24 months; disclose any continuing or reasonably foreseeable conflict; and be updated if circumstances change. The owner may reject or narrow the engagement where independence cannot be preserved. Undisclosed material conflicts may be grounds for termination and rejection of deliverables.

## 12. Proposal submission requirements

A proposal should include:
- legal entity / individual identity and country of operation;
- named lead reviewer and all proposed personnel;
- CV, relevant credentials and verification details;
- two or more relevant anonymized database security/integrity engagements or references where disclosure is permitted;
- written response to RLS, composite FK, tenant isolation, concurrency, temporal integrity, and SQLite/PostgreSQL parity scope;
- sample redacted report or finding format;
- independence and COI declaration;
- fixed-fee quote, hours, assumptions, tax, optional disposable-environment testing/retest price, and schedule;
- NDA acceptance or proposed amendments;
- explicit exclusions, dependencies, and access requirements.

**Submission channel and deadline:** Not assigned. This draft is not an invitation to submit until separately authorized and issued.

## 13. Schedule and governance

Indicative schedule after a separate award:
- kickoff and evidence inventory: 1–2 business days;
- schema, policy, and architecture desk review: 3–5 business days;
- test-design/evidence review and findings: 2–4 business days;
- final report and walkthrough: 1–2 business days.

Any disposable database execution is a separately approved work package. Owner factual review may correct factual errors but must not suppress independent findings.

## 14. Commercial and authorization conditions

- No work starts before a signed statement of work / purchase authorization and approved budget.
- This RFP does not authorize payment, vendor contact, account creation, tool installation, or paid subscriptions.
- No production or staging mutation, DDL, migration, seed, backfill, data deletion, deployment, merge, or destructive test is authorized.
- Any target-engine test must be performed only on a disposable isolated environment with synthetic data and explicit written authorization.
- Any expansion of scope, hours, access, or cost requires written approval in advance.
- The owner may pause or terminate the engagement for independence, confidentiality, safety, budget, or scope reasons.

## 15. Severity classification and test-evidence rubric

Use the following severity definitions consistently; the reviewer must explain the rationale and business impact for every rating:

| Severity | Definition | Expected handling |
|---|---|---|
| Critical | Exploitable condition with severe systemic impact, such as broad cross-tenant data exposure, RLS bypass, or corruption of authoritative records | Immediate owner escalation; no routine acceptance without explicit risk decision and remediation plan |
| High | Material integrity/confidentiality risk, tenant/site boundary weakness, or credible unauthorized write/read path | Prioritized remediation and documented retest or formal risk disposition |
| Medium | Meaningful integrity or isolation weakness with constrained exploitability/impact, or material missing defense-in-depth control | Remediation plan, owner, and target date required |
| Low | Limited-impact weakness or improvement with low exploitability | Track and disposition proportionately |
| Informational | Observation, clarification, or hardening recommendation without a demonstrated vulnerability | Record rationale and optional improvement |

For every test-evidence item, record test ID, requirement/control, engine and exact version, schema commit/SHA, disposable environment identifier, fixture/data classification, role used, tenant/site context, preconditions, operation, expected result, actual result, execution timestamp, logs/result digest, and reviewer conclusion. Distinguish source/schema inspection from tests actually executed. Never label a test PASS because a test case exists or because SQLite behavior is assumed to prove PostgreSQL behavior.

## 16. Standards Owner review disposition and procurement hold

| Item | Decision |
|---|---|
| Standards Owner review | Reviewed; conditional acceptance of the RFP structure |
| Required revisions | RLS/tenant-context test matrix; source-inspection vs executed-test distinction; severity and evidence rubric; corrected report effort; 24-month COI lookback; credential/reference verification |
| Procurement decision | **DEFERRED** |
| Budget ceiling / funding | **NOT APPROVED — NO CAP AUTHORIZED** |
| Vendor discovery or contact | **NOT AUTHORIZED** |
| RFP issue / public posting | **NOT AUTHORIZED** |
| NDA execution | Not started; required before non-public disclosure to a selected candidate |
| Appointment / SOW | Not authorized |
| Review execution | Not started |

This owner review authorizes document revision only. It does not authorize candidate searches, vendor outreach, proposal solicitation, expense, payment, NDA execution, repository access for external parties, database connections, or technical testing. A new explicit owner decision is required to lift the procurement hold.

## 17. Approval record

| Decision | Status | Authority / evidence |
|---|---|---|
| Draft prepared | DRAFT | Repository commit evidence |
| RFP review | REVIEWED — REVISIONS REQUIRED | Standards Owner |
| Budget approval | DEFERRED — NOT APPROVED | Owner decision required before procurement |
| Vendor contact / RFP issue | NOT AUTHORIZED | No outreach permitted |
| Vendor selection | NOT STARTED | Competitive evaluation required |
| NDA execution | NOT EXECUTED | Before non-public disclosure |
| Engagement award | NOT AUTHORIZED | Separate written authorization |
| Database review | NOT STARTED | Reviewer not appointed |
| GDES approval | NOT APPROVED | Standards Owner after review |

**End of GDES-RFP-DB-001.**
