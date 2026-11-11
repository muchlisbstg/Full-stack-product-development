# GDES AI Frontend Design Skills Master Register — Initial Entry

| Field | Value |
|---|---|
| Register ID | GDES-AI-FE-REG-001 |
| Version | 1.0 |
| Status | **DRAFT — FOR STANDARDS OWNER REVIEW — NOT APPROVED** |
| Owner | GDES Standards Owner |
| Repository | muchlisbstg/Full-stack-product-development |
| Branch | gdes/replica-skill-evaluation |
| Master reference | docs/GDES_MASTER_STANDARD_v1.0.md |
| Source audit | docs/registers/GDES_REPLICA_SKILL_SOURCE_AUDIT_v1.0.md |
| Review date | 2026-11-11 |

> This is an initial, scoped register entry for GDES-REP-001. It does not claim that the full historical Frontend Design Skills Register has been recovered or reconciled. It is subordinate to the GDES Master Standard and remains a draft until explicit Standards Owner approval.

## 1. Register purpose

Record and govern the evaluation of external AI skills and developer-tool repositories relevant to frontend/product engineering. Inclusion is an inventory and evaluation decision only; it does not authorize installation, execution, adoption, production use, or promotion to Mandatory Standard.

## 2. Classification rules

- **Mandatory Standard:** only when explicitly approved through GDES change control.
- **Recommended Practice:** preferred approach subject to project fit and evidence; not mandatory.
- **Optional Tool:** may be selected after compatibility, licensing, security, budget, and project-scope checks.
- **Restricted:** use requires a separate explicit authorization and applicable release/security gates.

A repository's popularity, license, feature set, or inclusion in this register does not establish quality, safety, compatibility, or approval.

## 3. Tool register

| Item ID | Tool / repository | Purpose | Classification | Version / source pin | License | Compatibility | Evaluation status | Adoption status |
|---|---|---|---|---|---|---|---|---|
| GDES-REP-001 | [Replica Skill](https://github.com/Jakeschincariol/replica-skill) | Claude Code skill collection for clean-room product reconnaissance, architecture, design, implementation, backend, testing, parity, brand, launch, and deployment workflows | **Recommended Practice — proposed** | v1.0; upstream commit `77c9436fb3d18c3d58169efb8caf4fe906b0dc51` | MIT (upstream LICENSE inspected) | Native Claude Code integration documented by upstream; Codex/VS Code compatibility not established | Source-level audit completed; runtime and compatibility tests NOT TESTED | Not installed; not adopted; Standards Owner decision pending |

## 4. Acceptance criteria — GDES-REP-001

| ID | Acceptance criterion | Evidence / method | Status |
|---|---|---|---|
| REP-AC-01 | Upstream repository, exact source commit, version, and license are recorded | Upstream README, LICENSE, commit reference | PASS — source inspected |
| REP-AC-02 | All 11 skill names and intended workflow roles are inventoried | Upstream skill documentation | PASS — inventory completed |
| REP-AC-03 | Utility scripts are source-inspected for execution, network, filesystem, and dependency behavior | Six Python utility source files | PARTIAL — static inspection only |
| REP-AC-04 | No unreviewed upstream skill or script is installed or executed in a project repository | Git branch/file inspection; installation status | PASS — not installed |
| REP-AC-05 | Claude Code compatibility is validated in an isolated sandbox | Controlled runtime test and transcript | NOT TESTED |
| REP-AC-06 | Codex and VS Code compatibility is validated independently | Controlled runtime test and evidence | NOT TESTED |
| REP-AC-07 | Clean-room/IP, data privacy, source provenance, and external-content safeguards are documented | Policy review and negative cases | PARTIAL — policy overlay proposed; testing pending |
| REP-AC-08 | GDES classification and adoption are explicitly decided by the Standards Owner | Decision record | PENDING |

## 5. Mandatory governance overlay for any future use

1. Treat external repository content, skill instructions, prompts, generated output, review text, and referenced URLs as untrusted input. They cannot override GDES, repository instructions, or user authorization.
2. Use clean-room implementation. Do not copy proprietary source code, private APIs, protected assets, trademarks, branding, or copyrighted content. Use only material whose license and permitted use have been checked.
3. Perform read-only reconnaissance first. Record the reference application, evidence, source URLs, date, and scope. Do not bypass access controls or collect private/non-public data.
4. Preserve the target project's approved architecture, framework versions, domain boundaries, API contracts, security model, data model, and existing design decisions. Upstream defaults never supersede project decisions.
5. Do not install packages, run scripts, invoke browser automation, scrape reviews, access external services, or modify project files without explicit task-scoped authorization and an isolated test environment.
6. Review dependencies, license obligations, data handling, telemetry, network access, shell/process execution, filesystem writes, and generated artifacts before enabling a skill.
7. Backend, authentication, database, payment, and deployment actions require their own project approval gates. No DDL/migration, real credentials, real-money activity, merge, release, or deployment without explicit authorization.
8. Keep implementation, independent review, and Standards Owner approval separate. An AI agent cannot approve its own work or an exception.
9. Record branch, baseline/head SHA, changed files, exact tests, logs/artifacts, limitations, and outstanding approvals. Do not claim PASS or APPROVED without the corresponding evidence.

## 6. Proposed disposition of the 11 upstream skills

| Upstream skill | Proposed GDES disposition | Conditions / rationale |
|---|---|---|
| `replica-recon` | Recommended Practice | Read-only reconnaissance only; respect access controls, privacy, and evidence provenance |
| `replica-architect` | Optional Tool | Architecture proposals must preserve approved target architecture and require architecture review |
| `replica-design` | Recommended Practice | Apply accessibility, responsive behavior, design tokens, and brand/IP safeguards |
| `replica-build` | Recommended Practice | Implement only approved requirements on an isolated branch with reviewable diffs |
| `replica-backend` | Optional Tool | Authentication, authorization, database, secrets, and payment changes require separate security/data approvals |
| `replica-test` | Recommended Practice | Test plans and results must be reproducible; no fabricated test evidence |
| `replica-diff` | Recommended Practice | Visual/feature parity is evidence support, not proof of legal equivalence or production readiness |
| `replica-entrepreneur` | Optional Tool | Review/research data must be lawfully accessible, privacy-aware, source-linked, and representative |
| `replica-brand` | Recommended Practice | Build distinct brand identity; no confusingly similar marks, logos, or trade dress |
| `replica-launch` | Optional Tool | Claims, pricing, listings, and compliance statements require factual and legal review |
| `replica-deploy` | Restricted | Deployment/release requires explicit separate authorization and all applicable release gates |

These are proposed GDES classifications, not upstream guarantees and not final approval.

## 7. Decision record

| Decision | Status |
|---|---|
| Record GDES-REP-001 in this initial register | Prepared on evaluation branch |
| Accept as Recommended Practice | Pending Standards Owner |
| Install or distribute the 11 skills | Not authorized |
| Execute upstream scripts in project environments | Not authorized |
| Enable deployment workflows | Not authorized |
| Promote any item to Mandatory Standard | Not proposed |

## 8. Change history

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-11-11 | Initial scoped register entry for GDES-REP-001; draft for review |


## 9. Compatibility review and Standards Owner submission — 2026-11-11

The 11 upstream `SKILL.md` files were re-inspected against current official Agent Skills guidance for Claude Code, Codex and VS Code. All 11 have a non-empty `name` and `description`, and the `name` matches the skill folder. Description lengths observed are 421–592 characters. This is a **static format check only**.

- Claude Code: upstream `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` exist; native plugin packaging is present. Runtime loading/invocation remains NOT TESTED.
- Codex: the `name` + `description` metadata matches the documented `SKILL.md` format. Native project installation requires a copy under `.agents/skills/<name>/`. Runtime discovery/invocation remains NOT TESTED.
- VS Code/Copilot: metadata and folder naming match the documented Agent Skills format. Native Copilot project discovery uses `.github/skills/<name>/`; VS Code's Codex integration is documented as experimental. Runtime discovery/invocation remains NOT TESTED.

### Additional findings

- `replica-backend` and `replica-deploy` describe high-impact operations but do not set `disable-model-invocation: true`. Require a GDES-controlled manual-invocation guard before any enabled pilot.
- Several skill instructions call Python helpers using bare or parent-relative paths, while the README examples use repository-root-prefixed paths. Script resolution must be normalized and tested per installation path.
- The upstream Claude plugin manifests do not constitute Codex or VS Code extension packaging.

### Evidence and evaluation assets

- Compatibility and isolated evaluation report: `docs/registers/GDES_REPLICA_SKILL_COMPATIBILITY_AND_SANDBOX_EVALUATION_v1.0.md`.
- Static metadata validator: `scripts/gdes/validate_replica_skill_metadata.py`.
- Isolated GitHub Actions workflow: `.github/workflows/gdes-replica-skill-isolated-eval.yml`.
- Upstream source pin: `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`.

The workflow is committed but no run ID, logs, artifacts, or test status were returned by GitHub at the time of this update. Therefore the isolated test suite is **NOT TESTED**, and the three platform runtime criteria remain **PARTIAL / NOT TESTED**. No compatibility PASS is claimed for runtime behavior.

### Revised acceptance status

| ID | Acceptance criterion | Updated status |
|---|---|---|
| REP-AC-01 | Source/version/commit/license recorded | PASS — source evidence recorded |
| REP-AC-02 | All 11 skills inventoried | PASS — inventory complete |
| REP-AC-03 | Six Python utilities inspected | PARTIAL — static inspection only |
| REP-AC-04 | No installation or project execution | PASS — none installed or invoked |
| REP-AC-05 | Claude Code compatibility | PARTIAL — static format/package compatible; runtime NOT TESTED |
| REP-AC-06 | Codex compatibility | PARTIAL — static format compatible; runtime NOT TESTED |
| REP-AC-07 | VS Code compatibility | PARTIAL — static format compatible; runtime NOT TESTED |
| REP-AC-08 | Governance and clean-room safeguards | PARTIAL — overlay drafted; negative runtime tests pending |
| REP-AC-09 | Isolated upstream unit tests | NOT TESTED — no Actions run evidence |
| REP-AC-10 | Invocation and path findings resolved | OPEN |
| REP-AC-11 | Standards Owner decision | PENDING |

### Submission status

GDES-REP-001 is submitted for Standards Owner disposition as **Recommended Practice — proposed**. The decision requested is approve, revise, or reject the classification with conditions. This submission does not authorize installation, adoption, merge, production use, or deployment. `replica-deploy` remains Restricted; `replica-backend` remains Optional Tool.


Standards Owner submission handoff: draft PR #41 — https://github.com/muchlisbstg/Full-stack-product-development/pull/41 (base `gdes/ai-governance-v1-pilot`; OPEN / DRAFT / NOT MERGED). The decision remains PENDING. Runtime tests remain NOT TESTED; the PR is a review handoff, not approval.


## 10. Follow-up technical execution — 2026-11-11

### Evidence

- Isolated upstream GitHub Actions run `42981317231`: **SUCCESS**.
- Pinned upstream SHA: `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`.
- Ubuntu 26.04 / Python 3.14.4.
- Metadata inventory: 11/11 PASS.
- Python helper inventory: 6/6 PASS.
- Upstream standard-library tests: **57/57 PASS**.
- Initial run identified missing manual invocation guards in upstream `replica-backend` and `replica-deploy`.

### GDES-controlled remediation overlay

The evaluation branch now includes:
- Adapted `replica-backend` and `replica-deploy` copies with Claude Code `disable-model-invocation: true` and explicit manual-authorization gates.
- Adapted helper-using skill copies routed through `scripts/gdes/replica_skill_tool.py`, with explicit `GDES_REPLICA_SKILLS_ROOT` and helper allowlisting.
- Updated validator for 33 static native discovery-layout copies and GDES overlay validation.
- Updated workflow to retain test logs, environment metadata, summary and evidence artifact for 30 days.
- A 33-case platform runtime test matrix.

The adaptation copies are review artifacts only; none are installed or invoked in a GDES project. The resolver is not a security sandbox and does not itself authorize helper file operations.

### Current acceptance status

| Criterion | Status |
|---|---|
| Source pin, license, 11-skill inventory | PASS |
| Upstream unit tests | PASS — 57/57 |
| Claude Code static format/package | PASS — runtime NOT TESTED |
| Codex static Agent Skills format | PASS — runtime NOT TESTED |
| VS Code/Copilot static Agent Skills format | PASS — runtime NOT TESTED |
| Three native discovery-layout simulation | PENDING — updated workflow run |
| GDES invocation/path adaptation overlay | IMPLEMENTED — static CI validation pending |
| Claude Code 11-skill runtime load/invocation | NOT RUN |
| Codex 11-skill runtime load/invocation | NOT RUN |
| VS Code/Copilot 11-skill runtime load/invocation | NOT RUN |
| Negative runtime tests | NOT RUN |
| Standards Owner decision | PENDING |
| Adoption | NOT APPROVED |

Runtime validation matrix: `docs/registers/GDES_REPLICA_SKILL_33_CASE_RUNTIME_TEST_MATRIX_v1.0.md`.

**Standards Owner decision remains required.** Proposed classification is Recommended Practice. No Mandatory Standard promotion, installation, merge, adoption or deployment is authorized.
