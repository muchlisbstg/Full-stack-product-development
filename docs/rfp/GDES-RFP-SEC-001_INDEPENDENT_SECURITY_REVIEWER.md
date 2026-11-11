# GDES-RFP-SEC-001 — Independent Security Reviewer

| Metadata | Value |
|---|---|
| RFP ID | GDES-RFP-SEC-001 |
| Version | 1.0 |
| Status | **DRAFT FOR REVIEW — NOT ISSUED** |
| Owner | MUCHLIS BSTG / GDES Standards Owner |
| Repository | `muchlisbstg/Full-stack-product-development` |
| Branch | `gdes/ai-governance-v1-pilot` |
| Related artifacts | `docs/GDES_MASTER_STANDARD_v1.0.md`; `docs/registers/GDES_CYBERSECURITY_REGISTER_v1.0.md`; `docs/registers/GDES_CYBERSECURITY_MAPPING_MATRIX_v1.0.md` |
| Currency | IDR; indicative planning estimates only |
| Procurement authority | None granted by this draft |

> **Governance notice:** This is an internal draft request-for-proposal template. It has not been issued to vendors, does not appoint a reviewer, does not approve expenditure, and does not authorize repository access, testing, production access, or a security sign-off. GDES Master Standard and the related registers remain draft / not approved.

## 1. Purpose and procurement objective

Invite qualified independent security professionals or firms to submit a scoped proposal for an evidence-based review of the GDES Cybersecurity Register and External Mapping Matrix, with particular attention to the Export Client Web/API, Android, iOS, Desktop, and multi-tenant trust boundaries where the supplied evidence is in scope.

The engagement is an **independent assurance review**, not implementation, certification, penetration testing by default, legal opinion, or approval of GDES. The reviewer must challenge the author's mapping and conclusions, identify omissions and incorrect references, and provide a reproducible written disposition.

## 2. Independence and reporting line

- Reviewer must be independent of the author, implementer, and delivery team for the artifacts under review.
- Reviewer must disclose current and prior financial, employment, advisory, family, subcontracting, and material commercial relationships with the project owner, implementers, vendors, and other reviewer.
- A reviewer who authored or implemented a control may not independently sign off that same control.
- Reviewer reports findings directly to the Standards Owner; material disagreements must be recorded, not silently reconciled.
- Security and Database reviews are separate engagements. This RFP does not authorize the Security Reviewer to sign off database-specific assurance reserved for the Independent Database Reviewer.
- The Standards Owner retains final GDES decision authority. Reviewer opinion is advisory evidence and does not itself make a control PASS or APPROVED.

## 3. Scope of work

### 3.1 In-scope review

1. **Governance and threat modeling**
   - Review GDES-SEC-001 governance, threat-model ownership, risk acceptance, separation of duties, and evidence lifecycle.
   - Assess whether trust boundaries, assets, actors, abuse cases, and threat assumptions are explicit and traceable.

2. **Identity, authentication, authorization**
   - Review GDES-SEC-002 and GDES-SEC-003, including identity provenance, authentication lifecycle, MFA/recovery where applicable, server-side authorization, role/site scope, deny-by-default, privilege escalation, and cross-tenant access scenarios.
   - Challenge any design that trusts client-supplied tenant, role, site, or permission claims without authoritative server-side validation.
   - Review API endpoint and object-level authorization evidence supplied for the engagement.

3. **Application, API, and platform security**
   - Review GDES-SEC-004 through GDES-SEC-007 and GDES-SEC-009.
   - Assess input/output handling, injection exposure, API/integration trust, SSRF and outbound request controls where applicable, cryptography/data protection, secret handling, configuration, dependency and software-supply-chain controls.
   - Review Web/API, Android, iOS, and Desktop applicability separately; do not infer platform parity from shared source or configuration alone.

4. **External framework crosswalk**
   - Verify the mapping logic and identifiers in the pinned OWASP ASVS 5.0.0, MASVS, MASWE 1.0.0, MASTG 2.0.0, TCASVS 5.0.0, and SAMM 2.2.0 sources.
   - Challenge each `covers`, `partially_covers`, and `informs` relationship; identify overclaims, missing controls, version inconsistencies, and license/attribution issues.
   - Review ASVS applicability and verification-level selection approach.
   - Review the MASVS → MASWE → MASTG traceability method and whether selected tests match actual application features and platform surfaces.
   - Review SAMM practice mapping and identify missing stream/activity/question-level traceability.

5. **Verification, operations, and resilience**
   - Review GDES-SEC-010 and GDES-SEC-011: security logging, privacy-safe telemetry, monitoring, incident readiness, vulnerability disposition, backup/restore and rollback evidence, and release security gates.
   - Identify controls not adequately covered by upstream frameworks and propose explicit GDES acceptance criteria.

6. **Findings and closure**
   - Produce a prioritized findings register with severity, affected control, evidence/reference, impact, remediation recommendation, owner role, and retest criteria.
   - Review proposed dispositions and retest evidence only if separately included in the agreed hours.

### 3.2 Explicit exclusions

Unless separately contracted and authorized, the engagement excludes:
- active penetration testing, exploitation, fuzzing, scanning, social engineering, phishing, denial-of-service, or production traffic testing;
- access to production systems, live customer data, real credentials, payment systems, or real-money workflows;
- source-code implementation, pull-request approval, merge, deployment, configuration changes, or remediation execution;
- database sign-off reserved for the Independent Database Reviewer;
- legal, regulatory, privacy-counsel, or Syariah opinions;
- certification, audit attestation, or claims of compliance with ISO/IEC or other certification schemes.

Any technical test requires a separately approved written test plan, authorized target, environment, time window, rules of engagement, and stop conditions. Default mode is read-only document/source/evidence review.

## 4. Required competencies

### 4.1 Mandatory

- Demonstrable professional experience in application security, security architecture, or product security; target minimum 7 years or equivalent depth evidenced by comparable engagements.
- Practical experience reviewing multi-tenant SaaS/API authorization and web application trust boundaries.
- Working knowledge of OWASP ASVS, MASVS, MASTG, SAMM, threat modeling, secure SDLC, and software supply-chain security.
- Ability to review Android and iOS security applicability and distinguish mobile client controls from backend authorization.
- Experience producing evidence-based security assessment reports with traceable findings and retest criteria.
- Written and spoken professional English sufficient to interpret upstream standards; Indonesian communication is preferred.
- Signed NDA, conflict-of-interest declaration, and acceptance of the scope/access restrictions.

### 4.2 Preferred credentials (not substitutes for experience)

CISSP, CSSLP, CISM, CISA, OSCP, OSWE, CREST-related credentials, or equivalent relevant qualifications. Vendor must identify credential issuer, current status, and verification method. No single certificate guarantees selection.

## 5. Deliverables

| ID | Deliverable | Minimum content |
|---|---|---|
| SEC-D01 | Inception and independence pack | Confirmed scope, reviewer CV, credentials, COI declaration, NDA, work plan |
| SEC-D02 | Evidence inventory | Artifact/version/SHA, review method, evidence gaps, limitations |
| SEC-D03 | Control-by-control review matrix | GDES-SEC-001–011 disposition; framework reference validation; applicability and coverage rationale |
| SEC-D04 | Security findings register | Severity, control, evidence, impact, recommendation, owner role, remediation and retest criteria |
| SEC-D05 | Executive report | Scope, methodology, overall coverage, material risks, exclusions, residual risk |
| SEC-D06 | Review meeting and closeout | Findings walkthrough, written responses, unresolved disagreement log |
| SEC-D07 | Retest addendum (if priced) | Retest of agreed remediation evidence; no blanket PASS |

Reports must distinguish **verified**, **not verified**, **not applicable with rationale**, **partially covered**, and **not tested**. Each claim must cite a file path, version/SHA, requirement ID, evidence identifier, or other reproducible reference.

## 6. Estimated effort and budget

All figures are planning assumptions for proposal comparison, not verified market quotations or approved expenditure.

| Work package | Estimated effort |
|---|---:|
| Inception, COI, evidence inventory | 2–3 hours |
| Governance, threat model, identity and authorization review | 4–6 hours |
| API, web, mobile, desktop, secrets and supply-chain review | 4–7 hours |
| Framework crosswalk and traceability review | 3–5 hours |
| Findings, report, walkthrough | 3–3 hours |
| **Indicative total** | **16–24 hours** |

| Pricing basis | Indicative range |
|---|---:|
| Target professional rate assumption | Rp1.800.000–Rp3.000.000/hour |
| Indicative base engagement | **Rp28.800.000–Rp72.000.000** |
| Internal target allocation for planning | **Rp32.000.000** |
| Preferred commercial structure | Fixed fee with explicit hours, deliverables, assumptions, and exclusions |

The internal target allocation is not a price commitment. If a credible proposal exceeds it, the owner must reduce scope or separately approve a revised budget; the reviewer must not silently reduce assurance coverage.

Vendor proposal must itemize professional fees, taxes, travel, platform fees, subcontracting, optional retest, and any out-of-scope rate. No expense is reimbursable without prior written approval.

## 7. Selection criteria

| Criterion | Weight |
|---|---:|
| Relevant application/API security and multi-tenant review experience | 25% |
| OWASP framework and source-mapping competence | 20% |
| Independence, COI transparency, and professional ethics | 20% |
| Evidence quality and report/retest methodology | 15% |
| Mobile and cross-platform security experience | 10% |
| Commercial clarity and value | 10% |
| **Total** | **100%** |

Minimum recommended threshold: 75/100, with no unresolved material conflict of interest and no failure of mandatory requirements. The owner may reject all proposals.

## 8. Acceptance criteria

A deliverable is accepted only when all applicable criteria below are satisfied:

- [ ] Reviewer identity, qualifications, references, NDA, and COI declaration are complete and verified to the owner's reasonable satisfaction.
- [ ] Reviewer confirms independence and documents any limitation.
- [ ] Scope, methodology, evidence sources, exclusions, and review period are explicit.
- [ ] GDES-SEC-001–011 are individually assessed; no control is silently omitted.
- [ ] Upstream identifiers and version pins are checked against the supplied source pins or a documented authoritative source.
- [ ] Mapping relationships and coverage claims are challenged with written rationale.
- [ ] Multi-tenant, identity, authorization, API, and platform-specific risks are addressed where evidence is supplied.
- [ ] Every finding has a unique ID, severity rationale, affected control, evidence/reference, impact, recommendation, and retest condition.
- [ ] Evidence gaps and untested areas are explicitly recorded; no unsupported PASS or compliance claim is made.
- [ ] Final report includes executive summary, technical detail, residual risks, limitations, and unresolved disagreements.
- [ ] Findings walkthrough is completed and owner comments are recorded.
- [ ] Final files are delivered in agreed editable and archival formats and accepted in writing by the authorized owner.

Acceptance of the report does **not** mean GDES is approved, all controls pass, or remediation is complete. Control closure requires evidence and authorized disposition.

## 9. NDA, confidentiality, and data handling

Before receiving non-public project material, the selected reviewer must execute a mutually reviewed NDA that includes:
- purpose limitation: use information only to perform this engagement;
- confidentiality covering source code, architecture, security findings, credentials, personal data, business information, and unpublished standards;
- least-privilege access and named personnel only;
- prohibition on sharing, subcontracting, uploading to public repositories, or using project material to train public or third-party AI models without explicit written permission;
- no copying or retaining secrets; credentials must not be requested unless specifically authorized and necessary;
- secure storage, encryption in transit and at rest, access logging where available, and prompt incident notification;
- no disclosure of vulnerabilities to third parties without written authorization, except where applicable law requires otherwise;
- return or verified deletion of project data at engagement end, subject to narrowly defined legal retention obligations;
- ownership and permitted use of deliverables, pre-existing tools, and generic know-how;
- term, permitted disclosures, breach notification, governing law, and dispute process to be completed by qualified counsel.

Do not include secrets or real customer data in the review pack. Use redacted, synthetic, or disposable test evidence wherever possible.

## 10. Conflict-of-interest declaration

Each proposed reviewer and subcontractor must declare:
1. current or recent employment, consulting, implementation, audit, investment, or commercial relationship with the owner, project, implementation vendors, and related reviewers;
2. authorship or implementation of any reviewed control, architecture, code, or evidence;
3. financial interest in a product or service that may be recommended;
4. personal relationships or other circumstances that could reasonably impair impartiality;
5. any restriction on reporting adverse findings.

The declaration must identify parties, dates, nature of relationship, affected scope, and proposed mitigation. The owner may reject or narrow the engagement where independence cannot be preserved. Undisclosed material conflicts may be grounds for termination and rejection of deliverables.

## 11. Proposal submission requirements

A proposal should include:
- legal entity / individual identity and country of operation;
- named lead reviewer and all proposed personnel;
- CV, relevant credentials and verification details;
- two or more relevant anonymized engagement examples or references where disclosure is permitted;
- written response to scope and methodology;
- sample redacted report or finding format;
- independence and COI declaration;
- fixed-fee quote, hours, assumptions, tax, optional retest price, and schedule;
- NDA acceptance or proposed amendments;
- explicit exclusions, dependencies, and access requirements.

**Submission channel and deadline:** Not assigned. This draft is not an invitation to submit until separately authorized and issued.

## 12. Schedule and governance

Indicative schedule after a separate award:
- kickoff and evidence inventory: 1–2 business days;
- desk review: 3–5 business days;
- draft findings and owner factual review: 2 business days;
- final report and walkthrough: 1–2 business days.

Dates are indicative and depend on reviewer availability and evidence completeness. Owner factual review may correct factual errors but must not suppress independent findings.

## 13. Commercial and authorization conditions

- No work starts before a signed statement of work / purchase authorization and approved budget.
- This RFP does not authorize payment, vendor contact, account creation, tool installation, or paid subscriptions.
- No production, staging mutation, database write, migration, deployment, merge, or destructive testing is authorized.
- Any expansion of scope, hours, access, or cost requires written approval in advance.
- The owner may pause or terminate the engagement for independence, confidentiality, safety, budget, or scope reasons.

## 14. Approval record

| Decision | Status | Authority / evidence |
|---|---|---|
| Draft prepared | DRAFT | Repository commit evidence |
| RFP review | NOT STARTED | Standards Owner |
| Budget approval | NOT APPROVED | Separate owner decision required |
| Vendor selection | NOT STARTED | Competitive evaluation required |
| NDA execution | NOT EXECUTED | Before non-public disclosure |
| Engagement award | NOT AUTHORIZED | Separate written authorization |
| Security review | NOT STARTED | Reviewer not appointed |
| GDES approval | NOT APPROVED | Standards Owner after review |

**End of GDES-RFP-SEC-001.**
