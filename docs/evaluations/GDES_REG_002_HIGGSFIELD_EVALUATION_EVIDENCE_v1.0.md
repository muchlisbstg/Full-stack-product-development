# GDES-REG-002 — Higgsfield Evaluation Evidence Report v1.0

**Evaluation mode:** Offline-first, source/static review only  
**Evidence date:** 2026-11-12  
**Disposition:** DEFER — no adoption approval  
**Execution boundary:** No candidate installation, execution, network/provider invocation, credential use, billing, or production action was performed.

## 1. Executive summary

Four Higgsfield repositories were reviewed in the requested order. HIG-01 received the deeper static review. HIG-02 through HIG-04 received a first-pass source, README, manifest, and installation/runtime-boundary review using the same evidence categories where available.

This environment provided GitHub source inspection but no disposable offline runner with the candidate repositories materialized. Therefore, source-level observations are evidence; runtime, dependency installation, test-suite execution, compatibility invocation, and security-negative tests remain NOT_RUN. No candidate is marked PASS.

## 2. Pinned source inventory

| ID | Repository | Observed source commit | Version / license evidence | Review status |
|---|---|---|---|---|
| HIG-01 | https://github.com/higgsfield-ai/skills | `27000402070db19d958789d05b3b52b6f4718d7c` | VERSION 0.14.0; MIT LICENSE verified | Static review completed; runtime NOT_RUN |
| HIG-02 | https://github.com/higgsfield-ai/cli | `fd21e7cb550b5835cc00c6b4abfea0c02fe77ff2` | MIT LICENSE verified; CLI release version not pinned in this review | First-pass static review; runtime NOT_RUN |
| HIG-03 | https://github.com/higgsfield-ai/higgsfield-video-engineer | `082bfd7b7b0b863799fa9afcdfeb3e84ba72e015` | MIT LICENSE verified; package version 0.1.0 | First-pass static review; runtime NOT_RUN |
| HIG-04 | https://github.com/higgsfield-ai/app-templates | `2b6343a7f2cbe9f629aeb84e7fd98e7ad32a1af3` | No LICENSE file found at repository root in this review; license NOT_VERIFIED | First-pass static review; runtime NOT_RUN |

Commit refs:
- HIG-01: https://github.com/higgsfield-ai/skills/commit/27000402070db19d958789d05b3b52b6f4718d7c
- HIG-02: https://github.com/higgsfield-ai/cli/commit/fd21e7cb550b5835cc00c6b4abfea0c02fe77ff2
- HIG-03: https://github.com/higgsfield-ai/higgsfield-video-engineer/commit/082bfd7b7b0b863799fa9afcdfeb3e84ba72e015
- HIG-04: https://github.com/higgsfield-ai/app-templates/commit/2b6343a7f2cbe9f629aeb84e7fd98e7ad32a1af3

## 3. HIG-01 — higgsfield-ai/skills

### 3.1 Scope and structure

- Repository describes Markdown-based agent skills for image/video generation, 3D/audio, brand systems, product photography, marketplace cards, websites/games, explainers, and thumbnails.
- README declares 9 skills. The setup script's SKILLS array also declares 9 directories.
- All 9 fetched SKILL.md frontmatters declare version 0.14.0, a matching directory name, and `allowed-tools: Bash`.
- The fetched Claude, Codex, and Cursor plugin manifests declare version 0.14.0 and MIT metadata.
- Root VERSION is 0.14.0.
- LICENSE is MIT and was fetched at the pinned commit.

### 3.2 Static checks and findings

| Check | Result | Evidence / notes |
|---|---|---|
| Source owner and pinned SHA | OBSERVED | Official `higgsfield-ai` organization; commit pinned above |
| License | OBSERVED | Root MIT LICENSE fetched |
| Skill inventory | OBSERVED | README and setup script list 9 skills |
| Frontmatter/version consistency | PARTIAL PASS | All 9 fetched SKILL.md files show 0.14.0; plugin manifests and VERSION show 0.14.0. Automated YAML/schema validation NOT_RUN |
| Codex plugin manifest | OBSERVED | `.codex-plugin/plugin.json` exists and declares skills root `./` |
| Cross-agent install docs | OBSERVED | README/INSTALL describe Codex, Cursor, Claude and npx skills / gh skill install |
| Reference-link integrity | NOT_RUN | No automated link resolver executed |
| Evals quality | PARTIAL | `evals/README.md` and scenario files exist; no eval runner/scenarios executed |
| Setup script execution | NOT_RUN | Deliberately not run; script can install CLI, authenticate, create directories and symlink skill folders |
| Runtime invocation in Codex | NOT_RUN | No agent invocation performed |
| Runtime invocation in VS Code | NOT_RUN | No VS Code/Copilot invocation performed |
| Security negative tests | NOT_RUN | No prompt-injection, filesystem-boundary, or command-side-effect tests performed |

### 3.3 Material risks and constraints

1. **Network and authentication are intrinsic to the primary workflow.** README says each installation method handles CLI install/auth. The setup script downloads the CLI installer unless `--skip-cli`, checks account status unless `--skip-auth`, and links skills into the detected agent directory. This is not an offline installation path by default.
2. **Provider-dependent actions are not locally reproducible offline.** The skills route generation and other platform operations through the Higgsfield CLI. No generation, model lookup, media upload, account, credit, or deployment command was invoked.
3. **Broad tool permission.** All 9 skill frontmatters use `allowed-tools: Bash`. This is a broad execution capability; actual command restrictions depend on the host agent's permission model and must be tested, not inferred from the Markdown.
4. **Setup has filesystem side effects.** It creates the target directory and symlinks all skill folders. If a stale symlink exists at a destination, it removes that symlink and replaces it. It leaves an existing non-symlink path alone. Script was inspected but not executed.
5. **Documentation count inconsistency.** README and setup list 9 skills, while INSTALL.md contains statements that the installer installs “all eight skills.” This is a documentation defect requiring upstream clarification or correction.
6. **High-impact workflow capability.** The websites skill documents website creation/edit/deploy/publish workflows. Those operations are explicitly excluded from this evaluation.
7. **Cost boundary.** The skills are not evidence of free model inference. Platform generation, training, and other hosted actions may require account plans/credits. Paid or chargeable calls were not attempted.

### 3.4 HIG-01 disposition

**DEFER — static review only.** Suitable to continue controlled, no-execution source validation. Not approved for installation or adoption. Before runtime evaluation, prepare an isolated disposable workspace, deny outbound network by default, and test skill discovery separately from CLI/API execution. Any invocation that attempts account login, model access, upload, generation, publishing, or deployment must be blocked and recorded.

## 4. HIG-02 — higgsfield-ai/cli

### 4.1 Static observations

- README describes a terminal client for image/video/3D/audio generation and video analysis.
- MIT LICENSE fetched.
- Latest observed commit pinned in section 2.
- The documented quickstart requires `higgsfield auth login`; generation commands submit jobs to the hosted Higgsfield platform.
- The installer downloads a release archive and `checksums.txt`, verifies SHA-256, extracts the binary, then installs it under `<prefix>/bin` (default `/usr/local/bin`). It may invoke sudo to create or write the target directory.
- Installer creates `higgsfield`, `higgs`, and optionally `hf` command links. It uses a temporary directory and removes it on exit.

### 4.2 Risk and test status

| Check | Result |
|---|---|
| Source SHA / MIT license | OBSERVED |
| Installer source review | PARTIAL — checksum verification and privileged write path observed |
| Offline binary execution | NOT_RUN |
| Release checksum verification against a downloaded archive | NOT_RUN |
| Dependency / SBOM / vulnerability scan | NOT_RUN |
| CLI help and non-auth local commands | NOT_RUN |
| Authentication/API/generation | NOT_RUN — prohibited by no-credential/no-cost boundary |
| Codex / VS Code invocation | NOT_RUN |

**Finding:** installer integrity checking is a positive control, but does not establish release provenance, binary safety, or dependency security. Default installation can write to a system path and use sudo. Do not run the installer during this offline evaluation.

**Disposition:** DEFER — source review only; binary and release verification pending.

## 5. HIG-03 — higgsfield-ai/higgsfield-video-engineer

### 5.1 Static observations

- README describes a local code-based film renderer using WebGPU and the local GPU, with Node.js 22.12+, Chrome, and FFmpeg. Python 3.11+ is optional for example-film tools.
- MIT LICENSE fetched.
- package.json identifies version 0.1.0 and Node engine >=22.12.0.
- Skill package describes a local WebGPU path tracer, Node/Puppeteer tooling, Python tools, and FFmpeg encoding.
- Remote Runpod rendering is described as optional and explicitly chargeable; it is not required for local rendering.
- The pinned commit message records a security-oriented change to restrict uploaded render inputs and resolve symlinks before serving web files. This is a change-history signal, not proof that the current code passes a security audit.

### 5.2 Risk and test status

| Check | Result |
|---|---|
| Source SHA / MIT license | OBSERVED |
| Local/offline architecture claim | DOCUMENTED; not runtime-verified |
| Node/Python dependency installation | NOT_RUN |
| GPU/WebGPU renderer test | NOT_RUN |
| Dry-run / hello / check commands | NOT_RUN |
| FFmpeg output validation | NOT_RUN |
| Filesystem/symlink/network negative tests | NOT_RUN |
| Optional Runpod cost boundary | OBSERVED; must remain disabled |

**Finding:** this is the strongest candidate for a genuinely local creative runtime, subject to dependency and GPU compatibility validation. It still requires package acquisition/setup and compatible local GPU/browser tooling. Remote GPU rental must remain disabled.

**Disposition:** DEFER — prioritize for a future isolated local-render test after HIG-01 static review is complete.

## 6. HIG-04 — higgsfield-ai/app-templates

### 6.1 Static observations

- README describes Next.js 16, Tailwind v4, shadcn registry templates, and generation through the Higgsfield platform API.
- package.json pins Next.js 16.3.8 and React/React DOM 19.2.8; test script is `node --test tests/*.test.mjs`; typecheck and build scripts are present.
- AGENTS.md documents a server-side platform key in an httpOnly cookie, server-side authenticated platform calls, signed reference-upload URLs, and browser uploads using returned headers.
- README requires an API key for generation and stores it in an httpOnly cookie.
- Root LICENSE path returned 404 in this review. This is recorded as NOT_VERIFIED, not as proof that no license exists elsewhere.

### 6.2 Risk and test status

| Check | Result |
|---|---|
| Source SHA | OBSERVED |
| License | NOT_VERIFIED |
| Package manifest / declared scripts | OBSERVED |
| Dependency installation / lockfile integrity | NOT_RUN |
| Unit tests / typecheck / build | NOT_RUN |
| Static UI without credentials | NOT_RUN |
| Platform API / upload behavior | NOT_RUN — prohibited by no-credential/no-cost boundary |
| Secret-handling and upload negative tests | NOT_RUN |
| Deploy/publish paths | NOT_RUN — explicitly prohibited |

**Finding:** the architecture documents server-side credential isolation, but no implementation test was executed. The template is not a purely offline creative tool because its generation path depends on the Higgsfield platform API.

**Disposition:** DEFER — verify license and inspect auth/upload implementation before any runtime evaluation.

## 7. Cross-candidate comparison

| Dimension | HIG-01 Skills | HIG-02 CLI | HIG-03 Video Engineer | HIG-04 App Templates |
|---|---|---|---|---|
| MIT verified | Yes | Yes | Yes | Not verified |
| Offline usefulness | Instructions/static assets; core hosted operations unavailable | Limited local CLI/help potential; generation hosted | Local renderer intended | Static UI/build potential; generation hosted |
| Network required for install/setup | Default path yes | Installer yes | Dependency setup likely | Dependency setup yes |
| Hosted API required for main product feature | Yes | Yes | No for local render; optional remote GPU | Yes |
| Broad side-effect surface | Bash + CLI + symlinks | Installer/system binary + CLI actions | Local filesystem/GPU; optional remote pods | Web app + upload + platform calls |
| Runtime evidence | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Current disposition | DEFER | DEFER | DEFER | DEFER |

## 8. Required next evidence

1. Materialize each pinned source in a disposable offline runner; verify archive/source SHA before inspection.
2. Run static parsers and validators without executing setup/install scripts.
3. Inventory lockfiles, transitive dependencies, licenses, install hooks, executable scripts, and outbound endpoints.
4. Run HIG-01 metadata/reference/eval checks with network disabled; test Codex and VS Code discovery separately from actual invocation.
5. Run HIG-02 local help/version commands only after binary provenance and checksum verification; do not authenticate.
6. Run HIG-03 local `--dry-run`, renderer check, and small local sample only after dependency review; no Runpod.
7. Run HIG-04 offline tests/build with API endpoints blocked and synthetic fixtures; test missing/invalid credentials and upload boundaries without real secrets.
8. Record logs, exit codes, environment, exact command lines, and SHA-256 output hashes.

## 9. Standards Owner recommendation

**DEFER — insufficient runtime and security evidence.**

No candidate is approved for installation into the primary development environment, production use, or promotion to a GDES standard. HIG-03 is the most promising offline-first technical candidate. HIG-01 is useful as an agent-skill catalog but its normal workflow depends on the hosted CLI and grants Bash capability. HIG-02 and HIG-04 are platform-integrated and require additional provenance/security checks.

All four remain **PENDING** until the required isolated execution and negative tests are completed and reviewed.
