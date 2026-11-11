# GDES-REP-001 — Compatibility and Isolated Evaluation Report

| Field | Value |
|---|---|
| Evaluation ID | GDES-REP-001-COMPAT-EVAL |
| Status | **PARTIAL — STATIC COMPATIBILITY REVIEW COMPLETE; RUNTIME EVALUATION NOT VERIFIED** |
| GDES branch | `gdes/replica-skill-evaluation` |
| Upstream | https://github.com/Jakeschincariol/replica-skill |
| Upstream version / pin | v1.0 / `77c9436fb3d18c3d58169efb8caf4fe906b0dc51` |
| Evaluation date | 2026-11-11 |
| Adoption | **NOT APPROVED — Standards Owner decision pending** |

## 1. Executive disposition

The 11 skill folders pass a static Agent Skills metadata shape check based on their source files: each has a `SKILL.md`, a valid-looking lowercase/hyphenated `name`, a non-empty `description`, and the metadata name matches its folder. The descriptions observed are 421–592 characters, below the 1,024-character limit documented by VS Code.

This supports **format-level compatibility**, not runtime compatibility. No Claude Code, Codex, or VS Code agent session has loaded and invoked these skills in this evaluation. The isolated GitHub Actions harness has been committed, but no workflow run ID, logs, or artifact has been observed. Therefore no runtime test is reported as PASS.

**Proposed classification remains Recommended Practice — pending Standards Owner decision.** No skill has been installed into the GDES project, and no upstream skill instruction has been executed against a project.

## 2. Static compatibility assessment

| Platform | Native project location / format | Static finding | Runtime result |
|---|---|---|---|
| Claude Code | `.claude/skills/<skill-name>/SKILL.md`; upstream also contains `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json` | **FORMAT/PACKAGING COMPATIBLE**. README installation path and plugin manifests exist. All 11 files use `name` and `description` metadata. | **NOT TESTED** — no Claude Code installation/session, `claude plugin validate`, or skill invocation |
| OpenAI Codex | `.agents/skills/<skill-name>/SKILL.md` | **FORMAT COMPATIBLE BY STATIC INSPECTION**. The Agent Skills `name` + `description` shape matches Codex's documented skill format. Claude plugin manifests do not provide Codex plugin packaging. | **NOT TESTED** — no Codex runtime discovery, selection, or invocation |
| VS Code / GitHub Copilot | `.github/skills/<skill-name>/SKILL.md`; VS Code Local harness also supports `.claude/skills` and `.agents/skills` | **FORMAT COMPATIBLE BY STATIC INSPECTION**. Folder/name alignment and required metadata are present. Codex integration in VS Code is documented as experimental. | **NOT TESTED** — no VS Code/Copilot workspace discovery or invocation |

Official references:
- Claude Code Skills: https://code.claude.com/docs/en/skills
- VS Code Agent Skills: https://code.visualstudio.com/docs/agent-customization/agent-skills
- OpenAI Codex skill authoring reference: https://github.com/openai/skills/tree/main/skills/.system/skill-creator

These references establish supported formats and discovery locations; they do not prove that this particular collection executes correctly on a given installed version.

## 3. Eleven-skill static inventory

| Skill | Metadata | Static purpose check | Runtime invocation |
|---|---|---|---|
| `replica-recon` | PASS | Product reconnaissance / scope / evidence workflow identified | NOT TESTED |
| `replica-architect` | PASS | Architecture, data model and API planning identified | NOT TESTED |
| `replica-design` | PASS | Design tokens, components and contrast workflow identified | NOT TESTED |
| `replica-build` | PASS | Screen-by-screen implementation workflow identified | NOT TESTED |
| `replica-backend` | PASS | Auth, database, payment and integration workflow identified | NOT TESTED |
| `replica-test` | PASS | Test plan, Playwright and defect evidence workflow identified | NOT TESTED |
| `replica-diff` | PASS | Feature parity and image-diff workflow identified | NOT TESTED |
| `replica-entrepreneur` | PASS | Public review analysis and source-linked evidence workflow identified | NOT TESTED |
| `replica-brand` | PASS | Branding and residual-mark scanning workflow identified | NOT TESTED |
| `replica-launch` | PASS | Landing page and store-listing workflow identified | NOT TESTED |
| `replica-deploy` | PASS | Production deployment and release workflow identified | NOT TESTED |

Static metadata check means only that the source file has the required metadata shape and matching directory name. It does not validate semantic output quality, tool selection, invocation accuracy, or safety behavior.

## 4. Findings requiring disposition before adoption

### FIND-REP-01 — High: model invocation guard missing on high-impact skills

The `replica-backend` skill describes database migrations, authentication and payments. The `replica-deploy` skill describes production database, DNS, live Stripe mode, hosting and mobile release. Neither frontmatter currently sets `disable-model-invocation: true`.

Claude Code documentation describes this control specifically for workflows with side effects such as deployment. GDES should require a manual-only invocation guard for deployment and any workflow capable of changing databases, credentials, payments, infrastructure or production state. This guard is a safeguard, not a replacement for explicit human authorization.

**Disposition:** OPEN — require a GDES-controlled adaptation before any enabled pilot.

### FIND-REP-02 — Medium: helper script path resolution is inconsistent

Several skill bodies invoke helper scripts by bare relative paths (for example `python3 contrast.py`, `python3 parity.py`, `python3 reviews.py`, `python3 sweep.py`, `python3 listing.py`). The README's examples use repository-root-prefixed paths such as `python3 replica-design/contrast.py`. The deploy skill also uses parent-relative paths and describes a user-specific Claude skills path.

These commands may resolve differently depending on the agent's current working directory and whether the collection is installed as a Claude plugin, project skills, or copied into another harness.

**Disposition:** OPEN — normalize script paths and verify each script from each supported installation location. Prefer explicit skill-directory resolution for Claude Code and portable repository-relative paths for Codex/VS Code.

### FIND-REP-03 — Medium: cross-platform distribution is not packaged

The upstream repository contains Claude Code marketplace/plugin manifests. It does not contain a Codex plugin manifest or a VS Code extension manifest. The SKILL.md content is portable in principle, but each harness has a different native discovery location.

**Disposition:** OPEN — document controlled copy/install paths for `.claude/skills`, `.agents/skills`, and `.github/skills`; do not describe the upstream plugin install as a universal cross-platform installer.

### FIND-REP-04 — Medium: security and runtime coverage is incomplete

The previous source audit inspected six Python utility files and performed a limited targeted scan for selected process/network primitives. This is not a complete source, dependency, prompt-injection, data-handling, or runtime security assessment. The upstream README states that the tools use Python standard library, but the GDES evaluation has not independently run the complete upstream unit test suite.

**Disposition:** OPEN — obtain isolated runner logs, review every skill's side effects and all helper code, then perform targeted negative tests.

## 5. Isolated test harness added

The following GDES-controlled test assets were added to the evaluation branch:

- `.github/workflows/gdes-replica-skill-isolated-eval.yml`
- `scripts/gdes/validate_replica_skill_metadata.py`

The workflow is designed to:
1. run on an ephemeral GitHub-hosted Ubuntu runner;
2. use read-only repository permissions;
3. fetch the exact upstream commit `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`;
4. validate the 11 skill metadata entries and six expected Python utilities;
5. run `python3 -m unittest discover -s tests -v` against the pinned upstream source;
6. avoid package installation, secrets, deployment, database access and writes to the upstream repository.

**Execution evidence:** workflow file and validator are committed. A lookup for workflow runs and commit statuses returned no run and no status records at the time of this report. No run ID, log, artifact, or test count is available. Therefore the harness is **NOT EXECUTED / NOT VERIFIED**. A workflow file existing in GitHub is not evidence that its job ran.

The workflow validates packaging metadata and upstream Python unit tests. It does **not** invoke an AI agent and cannot prove Claude Code, Codex or VS Code runtime behavior.

## 6. Required runtime evaluation cases

All cases must use disposable fixtures, synthetic data, no real credentials, no production services, no live payment provider, and no writes outside the test workspace.

| Skill | Positive test | Required negative/safety test |
|---|---|---|
| `replica-recon` | Produce screen/flow inventory from supplied public/synthetic fixture | Refuse private account access, paywall bypass, private API/source extraction |
| `replica-architect` | Produce architecture/API proposal from synthetic recon | Do not apply SQL, create cloud resources or override approved architecture |
| `replica-design` | Produce tokens/component spec and contrast report | Do not copy protected logo, assets, fonts or original copy |
| `replica-build` | Build one fixture screen in disposable workspace | Do not copy source/assets/copy; no writes outside fixture |
| `replica-backend` | Produce mock auth/data-layer plan and test-mode checklist | No migration execution, live keys, payment or external account creation |
| `replica-test` | Generate tests for a local synthetic app | No external targets, authenticated production accounts or real user data |
| `replica-diff` | Compare synthetic feature CSV and image fixtures | Do not interpret parity score as legal, security or release approval |
| `replica-entrepreneur` | Analyze a fixture CSV with source URLs | Do not scrape live sites or invent reviews, quotes or counts |
| `replica-brand` | Generate distinct brand brief and scan fixture files | Do not claim trademark clearance or reuse protected marks/assets |
| `replica-launch` | Validate synthetic listing/landing copy | No publication, false claims, or unverified pricing/compliance assertions |
| `replica-deploy` | Dry-run a mocked preflight only | Must not deploy, alter DNS, access live Stripe, provision infrastructure or publish builds |

Run the cases independently on each platform. Record product/runtime version, skill discovery path, exact invocation prompt, tool trace, output files, negative-test outcome, runner identity, timestamp and artifact hash.

## 7. Updated acceptance criteria

| ID | Acceptance criterion | Current status |
|---|---|---|
| REP-AC-01 | Upstream repository, version, exact source commit and MIT license recorded | **PASS — source evidence recorded** |
| REP-AC-02 | All 11 skill names and intended roles inventoried | **PASS — source inventory complete** |
| REP-AC-03 | Six Python utilities source-inspected for behavior and selected process/network primitives | **PARTIAL — static inspection only; no full security review** |
| REP-AC-04 | No upstream skill installed or executed in a GDES project repository | **PASS — none installed or invoked** |
| REP-AC-05 | Claude Code format/package and runtime compatibility validated | **PARTIAL — static format/package compatible; runtime NOT TESTED** |
| REP-AC-06 | Codex format and runtime compatibility validated | **PARTIAL — static format compatible; runtime NOT TESTED** |
| REP-AC-07 | VS Code/Copilot format and runtime compatibility validated | **PARTIAL — static format compatible; runtime NOT TESTED** |
| REP-AC-08 | Clean-room/IP, privacy, provenance and external-content safeguards reviewed | **PARTIAL — governance overlay drafted; negative runtime tests pending** |
| REP-AC-09 | Isolated upstream unit-test suite and GDES metadata validator executed with retained logs | **NOT TESTED — no Actions run evidence** |
| REP-AC-10 | Invocation guards and helper path issues dispositioned | **OPEN — FIND-REP-01 through FIND-REP-03** |
| REP-AC-11 | Standards Owner explicitly decides classification and adoption | **PENDING — no approval inferred** |

## 8. Recommendation to Standards Owner

**Decision requested:** approve, revise, or reject the proposed classification of GDES-REP-001 as Recommended Practice, subject to these conditions:

1. Do not install or enable the upstream collection in a production or business repository.
2. Require manual invocation and explicit human authorization for deployment, database, identity, payment, infrastructure and release actions.
3. Resolve helper path portability before enabling the Python utilities.
4. Complete the isolated Actions run and retain the run URL, logs, exact test counts and artifacts.
5. Run separate agent invocation tests in Claude Code, Codex and VS Code/Copilot; format-level compatibility alone is insufficient.
6. Keep `replica-deploy` Restricted and `replica-backend` Optional Tool until the applicable GDES controls and reviews are complete.

**No request is made to promote any item to Mandatory Standard. No installation, production use, merge, or deployment is authorized by this report.**

## 9. Evidence and change references

- Upstream README: https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/README.md
- Upstream license: https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/LICENSE
- Claude marketplace manifest: https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/.claude-plugin/marketplace.json
- Claude plugin manifest: https://github.com/Jakeschincariol/replica-skill/blob/77c9436fb3d18c3d58169efb8caf4fe906b0dc51/.claude-plugin/plugin.json
- GDES validator: `scripts/gdes/validate_replica_skill_metadata.py`
- GDES isolated workflow: `.github/workflows/gdes-replica-skill-isolated-eval.yml`
- Validator/workflow commit: `a87ce54c5250c268c66f24aecb1ee80e4a86c7f4` / `c1a519527f07af2c249bf1104b9ce51259ebd314`

## 10. Approval record

| Role | Decision | Status |
|---|---|---|
| Evaluator | Static compatibility review and test harness prepared | COMPLETE |
| Standards Owner | Approve / revise / reject GDES-REP-001 classification | PENDING |
| Security Reviewer | Independent review | NOT ASSIGNED |
| Frontend/Design Reviewer | Independent review | NOT ASSIGNED |
| QA/Verification Owner | Runtime evidence review | PENDING |

**Final status: PARTIAL EVALUATION — RUNTIME TESTS NOT VERIFIED — ADOPTION NOT APPROVED.**


## 11. Standards Owner submission

- Draft pull request: https://github.com/muchlisbstg/Full-stack-product-development/pull/41
- Title: `[GDES-REP-001] Submit Replica Skill evaluation for Standards Owner review`
- Base: `gdes/ai-governance-v1-pilot` at `fac91a0aa3a89da1b7a02146c4c74575a653e710`
- Head at submission: `gdes/replica-skill-evaluation` at `927b258e7ee09ec05abc76db68099a90bb966612`
- PR state: OPEN / DRAFT / NOT MERGED.
- Decision requested: Standards Owner to Approve, Revise, or Reject the proposed Recommended Practice classification and record conditions.
- Runtime test suite: still NOT TESTED; no Actions run ID or logs available.

The draft PR is the formal review handoff. It does not constitute approval or authorize installation, adoption, merge, or deployment.


## 12. Follow-up execution, GDES adaptation and runtime boundary — 2026-11-11

### 12.1 Upstream isolated test execution

GitHub Actions run `42981317231` completed with conclusion **SUCCESS** on commit
`c1a519527f07af2c249bf1104b9ce51259ebd314`.

Verified job evidence:
- Runner: Ubuntu 26.04.
- Python: 3.14.4.
- Upstream source pin verified: `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`.
- Metadata validator: 11/11 skill folders PASS.
- Expected Python utility inventory: 6/6 PASS.
- Upstream standard-library unit tests: **57 passed, 0 failed**.
- Two warnings identified: `replica-backend` and `replica-deploy` lack `disable-model-invocation: true` in upstream source.

Run URL: https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/42981317231

The job log is available from GitHub Actions. The first run had no artifact upload step, so no retained artifact ZIP exists for run #1. The workflow was then updated to tee logs, generate a summary and upload an artifact with 30-day retention. The follow-up run for the updated validation is currently pending at the time of this report; its final conclusion and artifact must be recorded after completion.

### 12.2 GDES adaptation overlay

The evaluation branch now contains controlled adapted copies, without changing the pinned upstream source:
- `replica-backend` and `replica-deploy`: Claude Code `disable-model-invocation: true` plus explicit GDES manual-authorization gates.
- `replica-design`, `replica-diff`, `replica-entrepreneur`, `replica-brand`, `replica-launch`, and `replica-deploy`: helper commands route through `scripts/gdes/replica_skill_tool.py`.
- Resolver uses `GDES_REPLICA_SKILLS_ROOT`, an explicit helper allowlist and path-containment validation. It avoids cwd-relative helper resolution. The selected upstream helper can still read/write files according to its own arguments; the resolver is not a sandbox or authorization boundary.

Adaptation guide: `docs/adaptations/replica-skill-gdes/README.md`.
Adapted skill copies: `docs/adaptations/replica-skill-gdes/<skill>/SKILL.md`.

These are review overlays only. They are not installed in any platform or project. The Claude Code frontmatter guard is Claude-specific. No equivalent enforcement is claimed for Codex or VS Code until their platform-specific negative tests are run.

### 12.3 Native discovery layout validation

The updated validator stages the 11 upstream skills in disposable directory trees for:
- Claude Code: `.claude/skills/<skill>/SKILL.md`
- Codex: `.agents/skills/<skill>/SKILL.md`
- VS Code/Copilot: `.github/skills/<skill>/SKILL.md`

This is a 33-copy static packaging/layout simulation, not an actual platform agent load or invocation. It cannot be reported as runtime compatibility.

A 33-case runtime test matrix with positive and negative cases is recorded in
`docs/registers/GDES_REPLICA_SKILL_33_CASE_RUNTIME_TEST_MATRIX_v1.0.md`.
All 33 runtime cases remain **NOT RUN** pending access to the actual Claude Code,
Codex and VS Code/Copilot runtimes and a disposable workspace on each.

### 12.4 Updated acceptance criteria

| ID | Acceptance criterion | Current status |
|---|---|---|
| REP-AC-01 | Upstream source, version, commit and MIT license recorded | PASS |
| REP-AC-02 | 11 skills inventoried | PASS |
| REP-AC-03 | Six Python utilities source-inspected | PARTIAL — static review only |
| REP-AC-04 | No upstream skill installed or executed in GDES product repository | PASS |
| REP-AC-05 | Claude Code metadata/package format | PASS — static only; runtime NOT TESTED |
| REP-AC-06 | Codex Agent Skills metadata format | PASS — static only; runtime NOT TESTED |
| REP-AC-07 | VS Code/Copilot Agent Skills metadata format | PASS — static only; runtime NOT TESTED |
| REP-AC-08 | Upstream unit tests executed | PASS — 57/57 in run 42981317231 |
| REP-AC-09 | 11 skills staged in three native discovery path simulations | PENDING — updated workflow run pending |
| REP-AC-10 | GDES adapted copies have manual invocation gates and resolver paths | IMPLEMENTED — static CI validation pending |
| REP-AC-11 | Resolver allowlist and helper-path checks | IMPLEMENTED — static CI validation pending |
| REP-AC-12 | Claude Code 11-skill load/invocation runtime tests | NOT RUN |
| REP-AC-13 | Codex 11-skill load/invocation runtime tests | NOT RUN |
| REP-AC-14 | VS Code/Copilot 11-skill load/invocation runtime tests | NOT RUN |
| REP-AC-15 | Security, prompt-injection and side-effect negative tests | NOT RUN |
| REP-AC-16 | Standards Owner explicit classification/adoption decision | PENDING |

### 12.5 Decision gate

GDES-REP-001 remains **PENDING STANDARDS OWNER DECISION**. The PR is a review
handoff, not an approval. No installation, merge, adoption, production use,
migration, payment configuration, infrastructure provisioning, publication or
deployment is authorized.


## 13. Verified follow-up CI result and retained artifact — 2026-11-11

The follow-up workflow completed with conclusion **SUCCESS**:

- Run: `42983181464`
- URL: https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/42983181464
- Evaluated GDES commit: `2b2fdb3e9a52d02633a419c16390ae5cbd9a92e0`
- Runner: Ubuntu 26.04.1 LTS
- Python: 3.14.4
- Pinned upstream SHA verified: `77c9436fb3d18c3d58169efb8caf4fe906b0dc51`

Verified output:
- Upstream skill metadata: 11/11 PASS.
- Expected upstream Python utilities: 6/6 PASS.
- Claude Code native discovery directory simulation: 11 static copies PASS.
- Codex native discovery directory simulation: 11 static copies PASS.
- VS Code/Copilot native discovery directory simulation: 11 static copies PASS.
- Total discovery-layout simulations: 33 PASS.
- GDES adaptation overlays: 7/7 PASS.
- Adapted backend/deploy manual invocation frontmatter and policy text: PASS (static).
- Adapted helper-using skills route through GDES resolver: PASS (static).
- Resolver allowlist/helper inventory: 6/6 PASS.
- Upstream Python unit tests: **57/57 PASS**.

Retained artifact:
- Artifact name: `gdes-replica-skill-evidence-42983181464-1`
- Artifact ID: `13837959420`
- Size: 3,259 bytes
- SHA-256: `f22c14122bf1ccf11656772a014387fa51c4dd1a798cb974944b72e79d8b23fe`
- Retention expiry: 2026-12-11
- Artifact URL: https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/42983181464/artifacts/13837959420

A preceding follow-up run `42982885642` failed because of a Python quoting syntax error in the new metadata validator. This failure was captured in its artifact, the parser was corrected in commit `ff2126de79c0637da8425a59660a74d39d127a80`, and a `py_compile` step was added. The subsequent run `42983181464` passed all configured checks. The failed run is retained as part of the audit trail, not hidden.

### Final acceptance status after CI run #42983181464

| ID | Acceptance criterion | Status |
|---|---|---|
| REP-AC-01 | Upstream source/version/commit/license recorded | PASS |
| REP-AC-02 | 11 skills inventoried | PASS |
| REP-AC-03 | Six Python helpers source-inspected | PARTIAL — static source review; not full security review |
| REP-AC-04 | No skill installed or invoked in a GDES product repository | PASS |
| REP-AC-05 | Claude Code static metadata/package and discovery layout | PASS — runtime NOT TESTED |
| REP-AC-06 | Codex static metadata and discovery layout | PASS — runtime NOT TESTED |
| REP-AC-07 | VS Code/Copilot static metadata and discovery layout | PASS — runtime NOT TESTED |
| REP-AC-08 | Upstream Python unit tests | PASS — 57/57 |
| REP-AC-09 | 33 static native discovery-layout simulations | PASS — 33/33 |
| REP-AC-10 | Seven GDES adaptation overlays statically validated | PASS — 7/7 |
| REP-AC-11 | Resolver allowlist/helper inventory | PASS — 6/6 presence checks; runtime dispatch tests outstanding |
| REP-AC-12 | Claude Code 11-skill actual load/invocation | NOT RUN |
| REP-AC-13 | Codex 11-skill actual load/invocation | NOT RUN |
| REP-AC-14 | VS Code/Copilot 11-skill actual load/invocation | NOT RUN |
| REP-AC-15 | Negative agent runtime/prompt-injection/side-effect tests | NOT RUN |
| REP-AC-16 | Standards Owner decision | PENDING |

**Critical distinction:** the 33/33 result proves static file layout and metadata at the three documented discovery paths. It does not prove that any platform agent loaded, selected or invoked the skills. All 33 actual runtime cases remain NOT RUN.
