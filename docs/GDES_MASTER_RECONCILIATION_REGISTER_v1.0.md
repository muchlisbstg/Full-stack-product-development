# GDES Master Reconciliation Register v1.0
## Draft for Review

| Metadata | Value |
|---|---|
| Register ID | GDES-RECON-001 |
| Version | 1.0 |
| Status | **DRAFT — NOT APPROVED** |
| Parent standard | GDES Master Standard v1.0 — Draft for Review |
| Repository | muchlisbstg/Full-stack-product-development |
| Branch | gdes/ai-governance-v1-pilot |

## 1. Purpose and reconciliation rule

This register maps the existing GDES AI Governance decisions and the requested Frontend, Cybersecurity, and SDLC registers to the proposed GDES Master Standard.

The pilot repository was inspected for the master and named domain registers. The following were present on the pilot branch:
- root `AGENTS.md`;
- `docs/GDES_CODEX_PILOT_VALIDATION_PLAN.md`.

No separate source file for GDES AI Governance v1.0 or the Frontend, Cybersecurity, and SDLC Master Registers was found in the inspected pilot repository paths/search results. Therefore:
- AI Governance content below is reconciled from the existing pilot `AGENTS.md`, validation plan, and previously recorded GDES governance decisions;
- Frontend, Cybersecurity, and SDLC rows below are a normalized **initial register baseline**, not a claim that prior standalone Google Sheets/files were retrieved;
- any missing source register, external sheet, or previously approved control must be linked and checked before this register can be finalized;
- this document does not convert draft content into approved policy.

## 2. Source and authority map

| Source/artifact | Observed status | Authority after master approval | Reconciliation action |
|---|---|---|---|
| GDES Master Standard v1.0 | Draft created in this pilot | Proposed canonical normative source | Await review and explicit Standards Owner approval |
| GDES AI Governance v1.0 | Governance content exists in pilot instructions/decisions; no separate master file verified | Subordinate domain policy/register | Consolidate into Master sections 5, 6, 12–15; retain detailed test plan separately |
| Root `AGENTS.md` | Present; pilot implementation copy | Repository-level implementation only | Add master version/path after master approval; do not treat as authority |
| Codex Pilot Validation Plan | Present; runtime tests not executed | Verification plan/evidence log | Keep GAI test status NOT TESTED until real execution |
| Frontend Design Master Register | No standalone source located in inspected pilot repository | Subordinate domain register | Initial control baseline in section 4; populate with source repos, license, compatibility, owners and evidence |
| Cybersecurity Master Register | No standalone source located in inspected pilot repository | Subordinate domain register | Initial control baseline in section 5; require security evidence and independent review |
| SDLC Master Register | No standalone source located in inspected pilot repository | Subordinate domain register | Initial gate baseline in section 6; map each gate to approval evidence |

## 3. Reconciliation principles

1. The approved GDES Master Standard will be the single normative source.
2. Registers are indexes and implementation aids; they do not override the master.
3. Repository `AGENTS.md` files are implementation copies, versioned against the master.
4. Every control must have a stable ID, classification, owner, applicability, acceptance criteria, evidence, status, reviewer, and approval record.
5. **PASS** means a test was executed successfully; **APPROVED** means an authorized human decision was made.
6. No AI self-approval, fabricated evidence, automatic exception approval, or inferred authorization.
7. A register item remains DRAFT/PROPOSED until approved by the Standards Owner and relevant reviewers.

## 4. Frontend Design Register — initial baseline

| ID | Control / item | Classification | Priority | Acceptance criteria | Evidence required | Status |
|---|---|---|---|---|---|---|
| GDES-UX-001 | Design token consistency (color, typography, spacing, elevation, states) | Mandatory Standard | P1 | Tokens are defined, versioned, reused, and checked for drift | Token source, component audit, visual QA | Proposed |
| GDES-UX-002 | Responsive/adaptive layouts | Mandatory Standard | P1 | Declared viewport/device targets work without critical layout or interaction failures | Responsive test matrix and screenshots | Proposed |
| GDES-UX-003 | Accessibility | Mandatory Standard | P1 | Applicable accessibility criteria are mapped and tested; keyboard, focus, labels, contrast and semantics reviewed | Accessibility report and defect disposition | Proposed |
| GDES-UX-004 | Navigation and interaction states | Mandatory Standard | P1 | Loading, empty, error, success, disabled, focus and validation states are defined | UI inventory and state coverage | Proposed |
| GDES-UX-005 | Reusable component architecture | Mandatory Standard | P1 | Shared components have documented API, ownership, variants and usage | Component inventory/storybook or equivalent | Proposed |
| GDES-UX-006 | Visual QA | Mandatory Standard | P1 | Screens reviewed against approved design at declared viewport/device sizes | Screenshots, comparison notes, issue log | Proposed |
| GDES-UX-007 | Design documentation and traceability | Mandatory Standard | P1 | Screens and components map to approved requirements and roles | Design spec, navigation/role matrix | Proposed |
| GDES-UX-008 | Impeccable design critique practice | Recommended Practice | P2 | Used as review aid where useful; does not replace human design review | Evaluation notes | Recommended |
| GDES-UX-009 | UI/UX Pro Max | Recommended Practice — Experimental | P3 | Evaluated on isolated branch against baseline and alternative practices before adoption | Comparative report, license/compatibility review | Experimental |
| GDES-UX-010 | Taste Skill | Recommended Practice — Experimental | P3 | Evaluated separately with repeatable prompts and comparative evidence | Comparative report | Experimental |
| GDES-UX-011 | HUE color exploration | Recommended Practice | P2 | Output checked against design tokens, contrast and brand constraints | Palette and contrast evidence | Proposed |
| GDES-UX-012 | Motion/animation libraries | Optional Tool | P3 | Optional; respects reduced-motion, accessibility, performance and platform constraints | Performance/accessibility test | Optional |

**Boundary:** Impeccable is Recommended Practice, not Mandatory Standard. UI/UX Pro Max and Taste Skill remain experimental candidates. No tool is required solely by appearing in this register.

## 5. Cybersecurity Register — initial baseline

| ID | Control | Classification | Priority | Acceptance criteria | Evidence required | Status |
|---|---|---|---|---|---|---|
| GDES-SEC-001 | Authentication and identity lifecycle | Mandatory Standard | P1 | Identity is verified server-side; lifecycle and recovery are defined | Auth tests, configuration review | Proposed |
| GDES-SEC-002 | Server-side authorization and least privilege | Mandatory Standard | P0 | Forged identity, privilege escalation, IDOR and cross-tenant access are rejected where applicable | Negative tests, policy/config evidence | Proposed |
| GDES-SEC-003 | Secrets management | Mandatory Standard | P0 | No secrets in source, client bundles, logs or unauthorized stores | Secret scan and bundle/log inspection | Proposed |
| GDES-SEC-004 | Input validation and safe output | Mandatory Standard | P1 | Trust-boundary validation, output encoding and safe errors are tested | Unit/integration/security tests | Proposed |
| GDES-SEC-005 | Network/SSRF/egress security | Mandatory Standard | P0 | Outbound destinations, DNS resolution, redirects, timeouts and egress are controlled according to threat model | SSRF negative tests and network evidence | Proposed |
| GDES-SEC-006 | Data privacy and protection | Mandatory Standard | P1 | Classification, minimization, access, retention and deletion are documented and enforced | Data-flow map and privacy review | Proposed |
| GDES-SEC-007 | Dependency and supply-chain security | Mandatory Standard | P1 | Dependencies, provenance, vulnerabilities and licenses are reviewed before release | SBOM or dependency report, audit log | Proposed |
| GDES-SEC-008 | Security logging and monitoring | Mandatory Standard | P1 | Security events are observable without leaking secrets or excessive personal data | Log review, alert tests | Proposed |
| GDES-SEC-009 | Backup, recovery and incident readiness | Mandatory Standard | P1 | Recovery and incident procedures are documented and tested proportionate to impact | Restore evidence, incident runbook | Proposed |
| GDES-SEC-010 | Independent security review | Mandatory Standard | P0 | Required independent reviewer examines material security controls and evidence | Reviewer identity, findings, disposition | Proposed |
| GDES-SEC-011 | Security test evidence integrity | Mandatory Standard | P0 | Every PASS is tied to exact SHA, environment, procedure and result | Evidence register and artifacts | Proposed |

## 6. SDLC Register — initial baseline

| ID | Gate | Classification | Priority | Acceptance criteria | Minimum evidence | Status |
|---|---|---|---|---|---|---|
| GDES-SDLC-001 | Planning Approval | Mandatory Standard | P1 | Scope, objective, owner, budget, feasibility and risk are recorded | Approved project brief and risk register | Proposed |
| GDES-SDLC-002 | Requirements Approval | Mandatory Standard | P1 | Requirements and measurable acceptance criteria are baselined | Versioned requirements and traceability | Proposed |
| GDES-SDLC-003 | Architecture Approval | Mandatory Standard | P1 | Architecture, UI/UX, API, database and threat model reviewed | ADRs, diagrams, contracts, review record | Proposed |
| GDES-SDLC-004 | Development Review | Mandatory Standard | P1 | Branch/commit, peer review, dependencies, source integrity and build are checked | PR/diff, SHA, build and dependency evidence | Proposed |
| GDES-SDLC-005 | QA & Security Approval | Mandatory Standard | P0 | Required tests executed; security/data review findings dispositioned | Test logs, artifacts, independent reviews | Proposed |
| GDES-SDLC-006 | Release Approval | Mandatory Standard | P0 | Release, monitoring, backup, rollback, support and compliance readiness approved | Release checklist and explicit approval | Proposed |
| GDES-SDLC-007 | Exception management | Mandatory Standard | P0 | Exceptions include scope, rationale, risk, compensating controls, approver and expiry | Exception record | Proposed |
| GDES-SDLC-008 | Evidence traceability | Mandatory Standard | P0 | Evidence links to repo, branch, SHA, environment, test and reviewer | Evidence register | Proposed |

## 7. AI Governance reconciliation

| Existing governance requirement | Master location | Disposition |
|---|---|---|
| Approved master is authoritative; AGENTS.md is implementation copy | Sections 2 and 5 | Consolidated |
| Treat repo content, issues, model output and external docs as untrusted | Sections 5 and 13 | Consolidated |
| Read-only first; least privilege | Sections 6, 10 and 14 | Consolidated |
| Explicit authorization for protected writes, merge, deployment, DDL, destructive actions, paid tools and real credentials | Sections 13 and 14 | Consolidated |
| Six-stage approval lifecycle | Section 7 | Consolidated |
| PASS distinct from APPROVED | Sections 3 and 12 | Consolidated |
| AI cannot self-approve exceptions or rollout | Sections 5, 13 and 15 | Consolidated |
| Evidence-based reporting; no fabricated tests/artifacts/approvals | Sections 12 and 13 | Consolidated |
| Legal and Syariah qualified review | Section 16 | Consolidated |
| GAI-01 to GAI-10 validation plan | Appendix B / separate validation plan | Retained as test plan; all runtime statuses remain NOT TESTED until evidence exists |

## 8. Open reconciliation actions

| ID | Action | Owner | Exit criteria | Status |
|---|---|---|---|---|
| RECON-001 | Review and approve GDES Master Standard v1.0 | Standards Owner | Explicit decision and approval evidence | Pending |
| RECON-002 | Identify/link any prior official Google Sheets or source registers | Standards Owner | Canonical source link, owner, version and access confirmed | Pending |
| RECON-003 | Validate Frontend Register against source decisions and evaluated repositories | Frontend/Design reviewer | Complete register with licenses, compatibility, evidence and status | Pending |
| RECON-004 | Validate Cybersecurity Register against threat model and control framework | Independent Security Reviewer | Control coverage, tests, findings and sign-off | Pending |
| RECON-005 | Validate SDLC Register with project owners | QA/Delivery owner | Gate owners, required artifacts and approval workflow | Pending |
| RECON-006 | Update root `AGENTS.md` with canonical master path/version after approval | Repository maintainer | Implementation copy references approved master without conflict | Blocked pending approval |
| RECON-007 | Run SEC-GDES-01 to SEC-GDES-08 in isolated fixture | Test operator + reviewer | Reproducible runtime evidence per test | Not tested |
| RECON-008 | Run pilot CI and retain logs/artifacts tied to commit SHA | Repository maintainer | Successful relevant workflow and evidence links | Not tested |
| RECON-009 | Independent review and rollout decision | Independent Security Reviewer + Standards Owner | Findings dispositioned and explicit human approval | Pending |

## 9. Current decision

**HOLD — Wider Rollout.** This reconciliation is an initial draft based on the files and governance decisions currently verified in the pilot context. It does not assert that the domain registers are complete, that security tests passed, that CI passed, or that independent review/approval occurred.

## 10. Infrastructure and Hosting Register — initial baseline

This section establishes the infrastructure register baseline from the Export Client RT-03 evidence already recorded in `muchlisbstg/export-client-mobile-sync`. The recovered GDES workbook v1.1 does not contain a dedicated Infrastructure Register worksheet; this section is therefore the current repository-side normalized baseline, not a previously approved Google Sheet. Provider/account access, funding, and runtime authority remain distinct facts.

| ID | Service / asset | Function and environment | Classification | Funding / provisioning | Region | Evidence and current assessment | Reviewer / approval |
|---|---|---|---|---|---|---|---|
| GDES-INF-001 | Hostinger | Intended future hosting target for Export Client | Planned target | **PLANNED — UNFUNDED**; no service plan or provisioned runtime evidenced | Not assigned | RT-03B records target intent only; no VPS, IP/SSH, API process, database, or deployment evidence | Reviewer pending; not approved |
| GDES-INF-002 | Vercel project `export-client-mobile-sync` | Existing project/deployment record; API authority unverified | Existing supporting platform | Project exists; no project environment variables were inventoried | Deployment record region iad1 | Production-target deployment is READY at recorded SHA, but no evidence establishes it as the authoritative Express API runtime; do not infer API health from deployment state | Technical review pending; not approved as API runtime |
| GDES-INF-003 | Supabase `export-client-staging` | PostgreSQL staging inventory only | Existing staging service | Active/healthy staging project; no production role inferred | ap-south-1 (Mumbai) | PostgreSQL 17.11 catalog inspection recorded 2026-11-11; 0 application relations, 0 app migrations and 0 RLS policies in the inspected snapshot. Staging only; catalog inventory is not runtime integrity proof | Independent Database review pending |
| GDES-INF-004 | Authoritative API runtime | Export Client API runtime | Required capability / not verified | Blocked pending funded hosting and connection evidence | Not established | RT-03D NOT STARTED; repository configuration and Vercel deployment metadata do not prove effective runtime configuration | Security/technical review pending |
| GDES-INF-005 | Actual application database integrity | Connected application database | Required verification / not verified | Blocked pending confirmed actual DB connection | Not established | RT-03E NOT STARTED; no full integrity check or app-data verification claimed | Independent Database review pending |

**Required register fields:** repository/service reference, function, license or vendor terms (where applicable), Web/Mobile/Desktop/backend compatibility, priority, audit status, acceptance criteria, evidence, owner, reviewer, approval, funding status, environment, region, and review date. Unknown values MUST remain `NOT VERIFIED`; do not infer licenses, compatibility, provisioning, or approval.

**RT-03 linkage:** RT-03A Source Inventory = RECORDED; RT-03B Infrastructure Target = RECORDED; RT-03C Staging Inventory = RECORDED; RT-03D Runtime Verification = NOT STARTED; RT-03E Database Integrity = NOT STARTED. RT-03 overall remains IN PROGRESS and P0 Release Readiness remains BLOCKED. The two historical Supabase catalog fingerprints (26 versus 27 RLS-enabled relations) are separate snapshots and require provenance/scope reconciliation before comparison.

## 11. Source Register Recovery — workbook evidence

Two prior GDES workbook artifacts were recovered from the user's ChatGPT Library and inspected:

| Artifact | Worksheet count | Contents / disposition |
|---|---:|---|
| `GDES_MUCHLIS_BSTG_v1.0_Draft.xlsx` | 12 | Earlier draft; retained as historical baseline |
| `GDES_MUCHLIS_BSTG_v1.1_Draft.xlsx` | 16 | Latest recovered master workbook candidate; contains the three-layer architecture and compliance matrix; remains Draft |

The v1.1 workbook includes `12_MANDATORY_STANDARD`, `13_RECOMMENDED_PRACTICE`, `14_REGIONAL_ADDENDUM`, `15_COMPLIANCE_MATRIX`, quality gates, governance controls, technology baseline, engineering disciplines, seven-continent profiles, and cross-platform requirements. It does **not** contain dedicated detailed source worksheets for the separate Frontend Design, Cybersecurity, SDLC, AI Governance, or Infrastructure registers. Therefore it is the recovered **Master Standard workbook**, not proof that all domain registers were recovered.

Source recovery outcome:
- Master workbook recovery: **FOUND**; v1.1 is the latest candidate, v1.0 is retained as history.
- Separate domain-register workbooks / original Google Sheets: **NOT LOCATED** in the accessible Library search.
- Google Sheets canonical live URL / owner / sharing access: **NOT VERIFIED**; connected Drive/Sheets access is unavailable in this workspace.
- Workbook approval: **NOT APPROVED**; both artifacts are Draft.

The recovered workbook should be version-controlled as source evidence before formal adoption. Do not silently overwrite it or imply it is an approved master.

## 11.1 Infrastructure validation — read-only evidence update (2026-11-11)

The following checks were performed through the connected Vercel and Supabase read-only interfaces. No environment values were decrypted and no project settings or database objects were changed.

| Provider / component | Observed evidence | Assessment |
|---|---|---|
| Hostinger | No Hostinger account/hosting connector operation was available in this workspace; no plan, account/service ID, VPS, IP, SSH endpoint, or API runtime evidence was supplied | **NOT VERIFIED**; owner-confirmed future target remains **PLANNED — UNFUNDED** |
| Vercel project | Project `export-client-mobile-sync`, ID `prj_d7QLVAnsgo7QoDA9xha7fWkbbbC9`; `framework=null`; `nodeVersion=26.x`; `live=false`; environment inventory returned 0 records and 0 hidden production variables | Project exists, but no environment variable records are configured/visible in the inspected inventory; no effective API database connection is evidenced |
| Vercel deployment | Previously recorded deployment `dpl_7htFkCME5YMAWfPw7vemATRsc1PJ` is READY, target production, SHA `0a3c595c6697f56d0cef8536c3b93c3886cc5ab1`; latest deployment list also shows READY deployments from audit/docs branches with `target=null`, including `dpl_23PPRNb9P4Qad4DYT9HKq425YSB2` at SHA `b1f695a25204abcc1c76c35194a8195fc820742b` | READY is deployment build state, not proof that Express API is running or authoritative |
| Vercel runtime logs | Seven-day query was rejected because Hobby plan retention does not cover that range; one-hour runtime error query returned no errors | Runtime observability evidence is limited; absence of recent errors is not health proof |
| Supabase staging | Project `export-client-staging`, ref `utvxuzmtevnmrcpxfpaa`, ACTIVE_HEALTHY, PostgreSQL 17.11, region `ap-south-1`; latest read-only `public` table list returned 0 tables; migration list returned 0 entries | Staging service is active but has no observed application tables/migrations in the queried scope; not proven connected to API |
| Supabase advisors | Security advisor: `auth_leaked_password_protection` WARN — Leaked Password Protection Disabled. Performance and Health advisors returned no lints | Security configuration follow-up required; no advisor finding does not prove complete security |

**Infrastructure decision:** RT-03D remains NOT STARTED because the actual API runtime and effective connection target are not established. RT-03E remains NOT STARTED because the actual application database has not been identified. Do not run schema migrations, DDL, data operations, deployment, or environment changes as part of this validation.

## 11.2 PR #145 state reconciliation — important deviation

A fresh GitHub pull-request fetch for `muchlisbstg/export-client-mobile-sync#145` returned:
- `state=closed`, `merged=true`, `draft=false`;
- `merged_at=2026-11-11T05:24:13Z`;
- merge commit `b1f695a25204abcc1c76c35194a8195fc820742b`;
- the PR timeline includes a `COMMENTED` review with body “Approved” by the repository owner.

This conflicts with the earlier instruction/state record that PR #145 should remain Draft and unmerged. The merge has already occurred in GitHub; this audit did not perform it and will not attempt an automatic revert. The repository owner must decide whether a corrective follow-up PR is required. Preserve the merge commit and evidence; do not rewrite history.

## 12. Cross-register reconciliation status and source gaps

| Register | Current reconciled baseline | Source completeness | Outstanding work | Status |
|---|---|---|---|---|
| AI Governance | Recovered GDES v1.1 workbook governance controls + root `AGENTS.md` and pilot validation plan | No separate AI Governance domain register workbook verified | Reconcile GAI-01–GAI-10 row-by-row against workbook and AGENTS; execute tests; independent review | Partial baseline / NOT TESTED |
| Frontend Design | Recovered workbook technology/cross-platform principles + GDES-UX-001–012 decisions; Impeccable Recommended Practice; UI/UX Pro Max experimental; Taste comparison; HUE Recommended Practice | No separate Frontend Design source register workbook verified | Validate every tool/repository row, license, platform compatibility, priority, audit status, acceptance criteria, evidence, reviewer and approval | Partial baseline only |
| Cybersecurity | Recovered workbook `GDES-MS-SEC-001/002`, `GDES-MS-DB-001`, `GC-04/05/06` plus GDES-SEC-001–011 baseline | No separate Cybersecurity source register workbook verified | Reconcile control IDs and coverage row-by-row; map threat model; attach test evidence; independent Security review | Partial baseline only |
| SDLC | Recovered workbook `03_QUALITY_GATES` QG-01–QG-12, `GC-01–GC-08`, plus GDES-SDLC-001–008 baseline | No separate SDLC source register workbook verified | Map SDLC IDs to QG and governance controls; assign gate owners and exit artifacts; verify workflow | Partial baseline only |
| Infrastructure | GDES-INF-001–005 baseline in section 10, informed by RT-03A–E | No dedicated Infrastructure worksheet in recovered v1.1 workbook; no separate source register verified | Reconcile with canonical source if later supplied; validate provider and runtime evidence; Hostinger remains PLANNED — UNFUNDED | Partial baseline only |
| Technology / Repository Evaluation | Classification rules established in master section 9 | Detailed tool inventory not reconciled in this pass | Link source catalog; validate licenses, versions, compatibility, cost, and risk | Pending |

### 11.1 Reconciliation completeness rules

- This pass reconciles the available pilot artifacts and recorded decisions; it does not claim to have retrieved missing external sheets or unlinked source registers.
- No row may be marked PASS or APPROVED without test evidence or explicit human approval, respectively.
- Tool/repository metadata (license, version, compatibility, maintenance, cost) must be verified against the actual upstream source before a recommendation is finalized.
- The master workbook itself is recovered from the user's Library; however, the canonical live Google Sheets URL, workbook owner, and sharing access remain unverified because connected Drive/Sheets access is unavailable. Separate domain register sources were not located in the accessible Library search.
- Until source artifacts are linked and domain reviewers sign off, the register is an initial normalized baseline, not a complete audit of all historical registers.

## 13. Updated action register

| ID | Action | Owner | Exit criteria | Status |
|---|---|---|---|---|
| RECON-001 | Review and approve GDES Master Standard v1.0 | Standards Owner | Explicit decision and approval evidence | Pending |
| RECON-002 | Establish recovered v1.1 workbook as controlled source candidate and locate separate domain registers / live Google Sheet | Standards Owner | v1.1 source artifact versioned; canonical URL/owner confirmed; domain source rows linked | Partial — master workbook found; domain sources and live URL not located |
| RECON-003 | Complete Frontend Register metadata and source validation | Frontend/Design reviewer | Repository, function, license, compatibility, priority, audit, acceptance, evidence, reviewer and approval fields verified | Pending |
| RECON-004 | Validate Cybersecurity Register against threat model and control framework | Independent Security Reviewer | Coverage, tests, findings and sign-off | Pending |
| RECON-005 | Validate SDLC Register with project owners | QA/Delivery owner | Gate owners, required artifacts and approval workflow | Pending |
| RECON-006 | Update root `AGENTS.md` to reference approved master version | Repository maintainer | Master approved; implementation copy reviewed and aligned | Blocked pending approval |
| RECON-007 | Run GAI-01 to GAI-10 and SEC-GDES tests in isolated fixtures | Test operator + reviewers | Reproducible evidence per test | NOT TESTED |
| RECON-008 | Run pilot CI and retain logs/artifacts tied to commit SHA | Repository maintainer | Relevant workflow logs and artifact links | NOT TESTED |
| RECON-009 | Independent review and rollout decision | Independent reviewers + Standards Owner | Findings dispositioned and explicit approval | Pending |
| RECON-010 | Reconcile GDES Infrastructure Register with canonical workbook/source | Standards Owner / Infrastructure owner | Source linked or repository register explicitly adopted; Hostinger remains PLANNED — UNFUNDED until provisioned | Pending |
| RECON-011 | Reconcile Export Client PR #145 state deviation | Repository owner / maintainer | Owner confirms whether corrective follow-up is required; preserve merge evidence and do not rewrite history | **DEVIATION — GitHub reports closed/merged; not Draft** |

## 13.1 External reference framework pairing — proposed baseline

The following upstream projects and standards are selected as **reference frames** for GDES domain registers. They are not wholesale adoption, automatic certification, or a replacement for GDES ownership and approval. Each GDES control retains its own stable ID; upstream references are mapped in separate columns and do not overwrite GDES IDs or historical evidence.

| GDES domain | Primary reference frame | Supporting reference | Intended use in GDES | Classification |
|---|---|---|---|---|
| Frontend Design | W3C Design Tokens Community Group, Design Tokens Format 2025.10 | GOV.UK Design System; WCAG 2.2 | Token interchange and governance; component/pattern/accessibility reference; accessibility acceptance criteria across Web/Mobile/Desktop | DTCG/WCAG: normative or technical reference as applicable; GOV.UK: Recommended Practice, not a global UI mandate |
| Cybersecurity | OWASP ASVS 5.0 | OWASP SAMM 2.2; OWASP Cheat Sheet Series | ASVS maps verifiable application security requirements; SAMM provides maturity/roadmap assessment; Cheat Sheets provide implementation guidance | ASVS: Mandatory GDES control-mapping baseline after tailoring; SAMM/Cheat Sheets: Recommended Practice |
| SDLC | FINOS SDLC Controls Framework | GDES six approval gates; repository CI/evidence controls | Reusable control catalogue, requirement definitions, mitigations and evidence mapping; map FINOS controls to Planning, Requirements, Architecture, Development, QA/Security, Release | Recommended Practice/reference catalog; GDES gates remain company governance requirements |
| AI Governance | NIST AI RMF 1.0 + Playbook | OWASP Top 10 for LLM Applications / OWASP AI security resources | Map GAI controls to Govern, Map, Measure, Manage; assess AI system lifecycle and risks; add application/LLM threat controls | NIST AI RMF is a voluntary framework used as GDES reference; GDES-specific controls become mandatory only after approval; OWASP AI security is supporting practice |

### 13.1.1 Reference source links

- W3C Design Tokens Community Group: https://github.com/design-tokens/community-group — stable specification 2025.10 is listed by the upstream project.
- GOV.UK Design System: https://github.com/alphagov/govuk-frontend — reference components and accessibility patterns; MIT license for GOV.UK code.
- WCAG 2.2: https://www.w3.org/TR/WCAG22/
- OWASP ASVS: https://github.com/OWASP/ASVS — upstream project identifies ASVS 5.0.0 as stable; ASVS project documentation uses CC BY-SA 4.0.
- OWASP SAMM: https://github.com/OWASP/samm — maturity model; project documentation identifies CC-BY-SA-4.0.
- OWASP Cheat Sheet Series: https://github.com/OWASP/CheatSheetSeries
- FINOS SDLC Controls Framework: https://github.com/finos-labs/SDLC-Controls-Framework — CC BY 4.0, technology-agnostic shared control catalogue.
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework and Playbook https://airc.nist.gov/airmf-resources/playbook/ — voluntary guidance organized as Govern, Map, Measure, Manage.
- OWASP AI Security: https://owasp.org/www-project-top-10-for-large-language-model-applications/

### 13.1.2 Mapping and licensing rules

1. Preserve GDES IDs (GDES-UX-xxx, GDES-SEC-xxx, GDES-SDLC-xxx, GAI-xx) as canonical identifiers. Store upstream IDs/clauses in a separate `external_reference_id` field.
2. Record source repository, exact release/tag or commit SHA, source license, retrieval date, and applicable version. A repository URL alone is not immutable evidence.
3. Do not copy upstream text wholesale into GDES. Prefer original GDES control wording with concise references; comply with attribution and share-alike obligations when reproducing licensed material.
4. Verify each selected repository's current license file and release before adoption. The licenses stated above are source-level leads, not legal approval for redistribution.
5. Map each GDES control to one or more upstream references with relationship `covers`, `partially_covers`, `informs`, or `not_applicable`; document rationale and gaps.
6. A control is not PASS merely because an upstream framework contains a similar control. PASS requires project-specific implementation and test evidence; APPROVED requires an authorized human decision.
7. Cross-platform frontend acceptance must explicitly cover responsive Web, Android, iOS, and Desktop behavior; GOV.UK examples are a reference, not proof of mobile-native compliance.

### 13.1.3 Recommended domain register workbook tabs

- `00_README_VERSIONING`: purpose, owner, version, source workbook, changelog.
- `01_CONTROL_REGISTER`: stable ID, control statement, class, domain, applicability, priority, owner, reviewer, approval.
- `02_EXTERNAL_MAPPING`: GDES ID, framework, upstream ID/clause, source URL, release/SHA, mapping relation, rationale.
- `03_ACCEPTANCE_CRITERIA`: measurable criteria, positive/negative cases, platforms, test method.
- `04_EVIDENCE_REGISTER`: evidence ID, artifact/log/PR URL, repository, branch, SHA, run ID, date, integrity/hash, result.
- `05_FINDINGS_EXCEPTIONS`: finding, severity, risk owner, remediation, exception expiry, residual risk, approval.
- `06_REVIEW_APPROVAL`: reviewer independence, scope, decision, conditions, timestamp.
- `07_CHANGELOG`: prior ID/version, change type, rationale, source and approver.

These are proposed workbook schemas. They are not evidence that the four domain workbooks have already been created or approved.

## 14. Current decision

**HOLD — Wider Rollout.** The v1.1 Master Standard workbook has been recovered and is the latest candidate baseline; v1.0 is historical. The repository register maps available AI Governance, Frontend, Cybersecurity, SDLC, and Infrastructure decisions to that workbook, but the separate detailed domain source registers and canonical Google Sheets URL have not been located. Row-by-row metadata verification, runtime tests, independent reviews, and formal approval remain outstanding. This is not a declaration that all registers are fully audited or approved.

**End of GDES Master Reconciliation Register v1.0 — Draft for Review.**



## 14. Cybersecurity Register v1.0 creation and mapping review — 2026-11-11

The first domain register has been created in the pilot branch:

- File: docs/registers/GDES_CYBERSECURITY_REGISTER_v1.0.md
- Status: DRAFT — NOT APPROVED
- Register ID: GDES-SEC-REG-001
- Commit creating the file: 906dc49bb78049b56b3a73d370961e636407a0f2
- Follow-up mapping/source review commit: 88d86cf0ed8657b09d988d1050a7ea37e45df52e
- Latest verified file blob SHA: 526a049141a41f3b1be76483bfab7594890c248a
- Scope: provisional GDES-SEC-001–011 descriptions, first-pass ASVS/SAMM/Cheat Sheet mapping, acceptance criteria, negative-access catalogue, evidence/finding templates, and review workflow.

### Mapping review disposition

- ASVS 5.0.0 stable release and CC BY-SA 4.0 source license verified.
- SAMM v2.2.0 release and commit reference identified; CC-BY-SA-4.0 source license identified.
- OWASP Cheat Sheet Series official source and CC BY-SA 4.0 license identified.
- A platform coverage gap was found: ASVS is web/web-service oriented and cannot be the sole security reference for native Android/iOS and desktop/thick-client targets.
- MASVS/MASWE/MASTG added as required mobile mapping references.
- TCASVS added as required desktop/thick-client mapping reference; its version metadata is conflicting between the OWASP project card and repository README and remains NOT RECONCILED.
- Exact ASVS requirement IDs, exact SAMM practice/stream IDs, upstream source pins for all supporting references, and canonical legacy GDES control wording remain incomplete.
- No runtime security tests were executed; all controls remain NOT TESTED.

**Overall Cybersecurity mapping result: PARTIAL — NOT APPROVED.** The 11-control first-pass mapping is a plausibility review, not proof of platform coverage, implementation, or compliance.

### Updated action register

| ID | Action | Status |
|---|---|---|
| RECON-004 | Validate Cybersecurity Register against threat model and control frameworks | IN PROGRESS — register created; independent review and exact mapping pending |
| RECON-007 | Run GAI/SEC controls in isolated fixtures | NOT TESTED |
| RECON-012 | Complete Cybersecurity exact requirement mapping, platform extensions, and independent review | OPEN |
| RECON-013 | Reconcile legacy GDES-SEC wording and master workbook security/database/governance rows | OPEN |

The SDLC Register remains next in the approved build sequence, but Cybersecurity mapping review must first produce documented coverage, unresolved gaps, and independent reviewer disposition. No SDLC Register is claimed to have been created in this update.



## 15. Detailed Cybersecurity framework crosswalk — 2026-11-11

Created:
- `docs/registers/GDES_CYBERSECURITY_MAPPING_MATRIX_v1.0.md`
- Mapping ID: GDES-SEC-MAP-001
- Creation commit: `f1a82631f313db5c22f9d5b1bd39ecb5b2e11839`
- Follow-up source-pin/identifier correction commit: `b186e066173acba674a37e2f2732bb6c03b285a0`
- Latest mapping blob SHA after correction: `420c13485aace686756d29184eb25eb3246f7346`

Mapping contents:
- ASVS v5.0.0 exact requirement section ranges for all 11 GDES-SEC controls, sourced from the tagged official CSV. Use version-qualified IDs such as `v5.0.0-1.2.5`.
- MASVS 24-control inventory across eight control groups.
- TCASVS 5.0.0 six-chapter section-level crosswalk, with chapter source blob pins.
- SAMM 2.2.0 15-practice mapping by canonical practice names/abbreviations, with selected practice blob pins.
- Coverage gaps, independent reviewer protocol, review status, and SDLC exit gate.

Source reconciliation:
- TCASVS repository README identifies stable 5.0.0 and six chapters; OWASP project card metadata still displays 1.8. The mapping pins repository v5.0 source and records the project-card discrepancy rather than treating the older card as the current source.
- MASWE v1.0.0 and MASTG v2.0.0 are stable sources; individual weakness-to-test mappings remain to be selected for actual app features/platforms.
- SAMM v2.2.0 practice mapping is at practice-name level; stream/activity/question-level traceability remains open.
- ASVS chapter/section requirement ranges are mapped but project-level applicability and verification levels still require reviewer decisions.
- Database controls remain a major GDES-specific gap and require independent Database Reviewer validation.

Review state:
- Independent Security Reviewer: NOT APPOINTED; NOT STARTED / BLOCKED.
- Independent Database Reviewer: NOT APPOINTED; NOT STARTED / BLOCKED.
- Runtime security tests: NOT TESTED.
- Standards Owner approval: NOT APPROVED.

**Gate remains NOT CLEARED.** The technical crosswalk exists, but coverage is PARTIAL and independent review has not occurred. SDLC Register v1.0 must not be represented as authorized to proceed until remaining mapping and review conditions are satisfied.


## 16. Cybersecurity canonical dictionary submission and source-pin reconciliation — 2026-11-11

The proposed canonical Cybersecurity Control Dictionary is formally submitted to the Standards Owner for disposition:

- Artifact: `docs/registers/GDES_CYBERSECURITY_CONTROL_DICTIONARY_v1.0.md`
- Artifact ID: `GDES-SEC-DICT-001`
- Decision issue: https://github.com/muchlisbstg/Full-stack-product-development/issues/40
- Current issue state: OPEN — Pending Standards Owner decision
- Current artifact state: DRAFT — NOT APPROVED
- Effective date: Not assigned.

### Source and licensing correction

The corrected immutable upstream source commits and license-file blob references are recorded in `docs/registers/GDES_CYBERSECURITY_FRAMEWORK_MAPPING_v1.0.md`. The v2.2.0 SAMM source is `owaspsamm/core`, not the archived `OWASP/samm` repository. All six selected source license files were inspected and identify CC BY-SA 4.0; legal review of redistribution/adaptation remains separate.

### ID integrity decision

The new dictionary defines `GDES-SEC-008` as Dependency & Software Supply Chain, `GDES-SEC-009` as Logging/Monitoring, `GDES-SEC-010` as Verification/Evidence, and `GDES-SEC-011` as Incident/Resilience. Database controls are `GDES-DB-001–005`. Historical GDES-SEC IDs from the Cybersecurity Register and the Master Reconciliation Register have different meanings and must be qualified by source document/version. The old mapping matrix has been explicitly marked legacy/provisional.

### Automated extraction status

The extractor and branch-scoped workflow have been committed. No successful Actions run or generated catalog read-back has been verified. Therefore MASWE/MASTG, ASVS, TCASVS, SAMM activity/question catalogs are still **NOT EXECUTED / NOT VERIFIED**. The MASTG pinned tree count discrepancy (292 unique test paths versus 285 reported in the v2.0.0 release announcement) remains open.

### Updated reconciliation actions

| ID | Action | Exit criteria | Status |
|---|---|---|---|
| RECON-014 | Complete pinned framework metadata extraction and generated-catalog validation | Successful Actions run; generated CSV/JSON files read back; counts, duplicates, missing metadata, unknown references and license hashes reconciled | OPEN — workflow execution not verified |
| RECON-015 | Standards Owner decision on GDES-SEC-DICT-001 | Written approve/revise/reject disposition for namespaces, semantics, aliases and source baseline | PENDING — Issue #40 |
| RECON-016 | Independent Security and Database review | Confirmed budget, renewed procurement authorization, appointed independent reviewers, written findings and dispositions | BLOCKED — procurement deferred |
| RECON-017 | Findings remediation and retest | Every finding closed or formally risk-accepted with expiry; retest evidence tied to commit/environment | NOT STARTED |
| RECON-018 | Cybersecurity Gate decision | Mapping completeness, independent reviews, tests, findings closure/retest and explicit Standards Owner approval | NOT CLEARED — SDLC blocked |

**Current decision:** Cybersecurity documentation is advanced, upstream source/license snapshots are verified, canonical dictionary is submitted but not approved, metadata extraction is not verified, procurement remains deferred, independent review has not started, and SDLC formal progression remains blocked.


## 17. Cybersecurity extraction result and current gate disposition — 2026-11-11

This addendum supersedes the earlier RECON-014 note that the extraction workflow had not yet executed successfully.

### 17.1 Verified execution

- Actions run [42972384713](https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/42972384713) completed successfully.
- Generated catalog commit: `7e06abbe46960e02c0bdd583111575eb96116207`.
- Remote read-back verified for generated catalogs, manifest, official MASWE beta mapping asset, and six-row license register.
- Counts: 24 MASVS controls; 78 MASWE; 118 beta aliases; 292 MASTG paths (200 structured and 92 legacy); 345 ASVS requirements; 132 TCASVS requirements; 90 SAMM activities and 90 questions; six license snapshots.

### 17.2 Source-mapping exceptions

The generated manifest reports:
- One unresolved beta weakness ID `MASWE-0097` in four MASTG tests; stable `MASWE-0051` is only a semantic candidate, not a source-backed alias.
- Seven beta aliases have multiple stable targets in the official release asset.
- 38 stable MASWE entries have no MASTG test link versus 36 reported in the release article.
- 292 unique MASTG test Markdown paths versus 285 tests reported in the v2.0.0 release announcement.
- ASVS and TCASVS catalogs have candidate mappings, not approved semantic mappings.
- SAMM activity-level relationships are candidates, not maturity scores or GDES compliance results.

Detailed finding records: `docs/registers/GDES_CYBERSECURITY_FINDINGS_REGISTER_v1.0.md`.

### 17.3 Updated action status

| ID | Action | Updated status |
|---|---|---|
| RECON-014 | Pinned framework metadata extraction and generated-catalog validation | **EXTRACTION COMPLETE — REMOTE VERIFIED**; source mapping exceptions remain OPEN in findings register |
| RECON-015 | Standards Owner decision on GDES-SEC-DICT-001 | PENDING — Issue #40 OPEN |
| RECON-016 | Independent Security and Database review | BLOCKED — procurement deferred; no reviewers appointed |
| RECON-017 | Findings remediation and retest | NOT STARTED |
| RECON-018 | Cybersecurity Gate decision | NOT CLEARED — SDLC formal progression remains blocked |

**Current decision:** source extraction and license snapshot verification are complete; candidate mappings and source exceptions remain under review; canonical dictionary is not approved; independent review has not started; runtime tests and retests have not started; Cybersecurity Gate is not cleared.
