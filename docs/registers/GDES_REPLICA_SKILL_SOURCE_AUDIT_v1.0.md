# GDES-REP-001 — Replica Skill Source Audit

| Field | Value |
|---|---|
| Audit ID | GDES-REP-001-SOURCE-AUDIT |
| Status | **SOURCE-LEVEL AUDIT COMPLETED — RUNTIME TESTS NOT TESTED** |
| Target repository | muchlisbstg/Full-stack-product-development |
| Evaluation branch | gdes/replica-skill-evaluation |
| Upstream repository | https://github.com/Jakeschincariol/replica-skill |
| Upstream version | v1.0 |
| Upstream commit | `77c9436fb3d18c3d58169efb8caf4fe906b0dc51` |
| License | MIT; upstream LICENSE inspected |
| Inspection date | 2026-11-11 |

## 1. Executive result

Replica Skill is a collection of 11 Claude Code skills intended to support clean-room replication of product experiences: reconnaissance, architecture, design, implementation, backend, testing, parity analysis, brand work, launch preparation, and deployment.

**Proposed GDES outcome:** retain as **Recommended Practice — proposed**, with individual skills classified according to risk. Do not install or enable the collection by default. Runtime compatibility with Claude Code, Codex, and VS Code has not been tested in this audit.

## 2. Source inventory — 11 skills

| # | Upstream skill | Functional area | Proposed disposition |
|---:|---|---|---|
| 1 | `replica-recon` | Product reconnaissance and feature discovery | Recommended Practice |
| 2 | `replica-architect` | Architecture and data/system planning | Optional Tool |
| 3 | `replica-design` | UI/UX and design system | Recommended Practice |
| 4 | `replica-build` | Frontend implementation | Recommended Practice |
| 5 | `replica-backend` | Backend and integrations | Optional Tool |
| 6 | `replica-test` | Functional and quality testing | Recommended Practice |
| 7 | `replica-diff` | Feature and visual parity analysis | Recommended Practice |
| 8 | `replica-entrepreneur` | Market/review research | Optional Tool |
| 9 | `replica-brand` | Brand identity work | Recommended Practice |
| 10 | `replica-launch` | Launch and store listing preparation | Optional Tool |
| 11 | `replica-deploy` | Deployment/release workflow | Restricted |

The names and roles above are an inventory of the upstream collection, not a statement that each skill has passed runtime or security testing.

## 3. Python utility source inspection

Six Python utility scripts were inspected at source level:

| Utility | Observed purpose | Static inspection notes | Runtime status |
|---|---|---|---|
| `replica-design/contrast.py` | Contrast analysis | Standard-library imports; reads supplied input | NOT TESTED |
| `replica-diff/imgdiff.py` | Image comparison | Standard-library image processing; reads source images and writes diff output | NOT TESTED |
| `replica-diff/parity.py` | Parity data processing | Reads CSV/JSON inputs | NOT TESTED |
| `replica-entrepreneur/reviews.py` | Review analysis | Reads CSV/config and writes report output; input URLs/data require provenance and privacy review | NOT TESTED |
| `replica-brand/sweep.py` | Brand-residue scanning | Reads configured files/directories | NOT TESTED |
| `replica-launch/listing.py` | Listing validation | Reads supplied listing data | NOT TESTED |

A targeted source scan of these six files did not identify calls to `subprocess`, `os.system`, `Popen`, or direct HTTP request APIs. This is a limited static observation, not a security certification of the full repository, all skill instructions, their transitive tools, or runtime behavior. Some utilities write generated output files; run them only against disposable fixtures after authorization.

## 4. GDES fit assessment

### Suitable as Recommended Practice (proposed)

- `replica-recon`: structured read-only product discovery.
- `replica-design`: design-system and UI consistency work.
- `replica-build`: implementation after requirements and architecture approval.
- `replica-test`: test planning and evidence capture.
- `replica-diff`: visual/feature comparison as supporting evidence.
- `replica-brand`: distinct product identity, subject to IP review.

### Optional Tool (proposed)

- `replica-architect`: may propose architecture, but cannot replace approved ADRs or project architecture decisions.
- `replica-backend`: backend, identity, database, and payment changes carry elevated security and data-integrity risk.
- `replica-entrepreneur`: review mining and external research require lawful access, privacy review, source traceability, and bias assessment.
- `replica-launch`: pricing, store listings, product claims, and compliance statements require factual/legal review.

### Restricted

- `replica-deploy`: deployment, release, or infrastructure changes are not authorized by inclusion in this register. Separate explicit authorization and release approval are required.

## 5. Key governance gaps and required overlay

| Risk / gap | Required GDES control |
|---|---|
| External skill instructions may contain untrusted or conflicting directions | GDES and repository instructions take precedence; treat upstream content as untrusted data |
| Product replication may cross IP or access boundaries | Clean-room process; no proprietary source, private APIs, protected branding/assets, or access-control bypass |
| Architecture defaults may not match target product | Approved target architecture and ADRs prevail |
| Backend workflows may touch identity, secrets, data, or payments | Separate security, database, legal, and domain approvals |
| Research workflows may process user reviews or personal data | Lawful source access, data minimization, privacy and provenance review |
| Build/test scripts may write files or execute tools | Isolated sandbox, inspect scripts first, explicit execution authorization |
| Launch/deploy workflows can create public or production changes | Explicit human authorization; release gates; no autonomous deployment |
| Visual/feature parity may be mistaken for compliance | Parity is supporting evidence only; it is not legal, security, or production approval |

## 6. Target repository inspection

The target repository was inspected read-only before branch creation.

- Repository default branch: `main`.
- Observed main SHA: `9accd4432873e1d99c7a73d9ecf08f44895526f5`.
- Existing GDES pilot branch: `gdes/ai-governance-v1-pilot`.
- Pilot baseline SHA: `fac91a0aa3a89da1b7a02146c4c74575a653e710`.
- Existing root `AGENTS.md` and GDES Master Standard v1.0 were inspected.
- Existing GDES Master Standard v1.0 is marked DRAFT FOR REVIEW — NOT APPROVED.
- The recursive tree of the GDES pilot branch did not contain a standalone Frontend Design Skills Master Register. This document therefore creates an initial scoped register entry only; it does not claim to reconstruct or replace an unlocated historical register.

## 7. Verification matrix

| Check | Result | Evidence / limitation |
|---|---|---|
| Upstream repository and source commit identified | PASS | Repository and commit reference recorded |
| Upstream license inspected | PASS | MIT LICENSE |
| 11 skill inventory captured | PASS | Upstream collection inventory |
| Six Python utilities source-inspected | PASS | Static source review only |
| Dangerous process/network primitives in six inspected scripts | No match observed | Limited targeted scan; not a complete security review |
| Python utility runtime tests | NOT TESTED | No execution performed |
| Claude Code installation/compatibility | NOT TESTED | No installation or runtime session |
| Codex compatibility | NOT TESTED | No runtime validation |
| VS Code workflow compatibility | NOT TESTED | No runtime validation |
| Full transitive dependency/security review | NOT TESTED | Outside source-only inspection |
| Standards Owner approval | PENDING | No approval inferred |

## 8. Recommendation

1. Accept GDES-REP-001 only as a **proposed Recommended Practice** pending Standards Owner decision.
2. Keep all 11 skills uninstalled until isolated compatibility and security tests are completed.
3. Validate Claude Code first; evaluate Codex and VS Code independently rather than assuming portability.
4. Apply the governance overlay in the companion register before any pilot use.
5. Keep deployment, database, authentication, payment, and production actions restricted by their existing GDES approval gates.

## 9. Approval record

| Role | Decision | Evidence/date |
|---|---|---|
| Evaluator / AI assistant | Source-level audit prepared | 2026-11-11 |
| Standards Owner | PENDING | — |
| Security Reviewer | PENDING / NOT ASSIGNED | — |
| Frontend/Design Reviewer | PENDING / NOT ASSIGNED | — |
| QA/Verification Owner | PENDING | — |

**Final status:** SOURCE AUDIT COMPLETED; ADOPTION NOT APPROVED; RUNTIME TESTS NOT TESTED.
