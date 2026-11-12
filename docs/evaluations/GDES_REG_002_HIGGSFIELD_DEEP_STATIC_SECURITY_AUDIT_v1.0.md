# GDES-REG-002 — Higgsfield Deep Static Security Audit v1.0

**Date:** 2026-11-12  
**Scope:** HIG-01 through HIG-04, in sequence  
**Method:** Pinned-commit source inspection through GitHub; no candidate execution  
**Environment:** GitHub source inspection only; no disposable local runner was available in this audit  
**Overall disposition:** DEFER — security/runtime evidence incomplete  
**Approval status:** NOT APPROVED for primary-environment installation, production use, or GDES standards promotion

## 1. Executive summary

The four candidates received a deeper source/configuration review, with HIG-01 receiving the broadest review of skill metadata, setup behavior, helper scripts, remote-resource handling, and documented agent instructions.

This was a static source audit, not a penetration test or runtime security assessment. No setup script, CLI binary, npm package, Python helper, renderer, upload, generation, deployment, or remote pod operation was executed. No API credentials or paid services were used.

### Risk summary

| Candidate | Material findings | Static risk posture | Disposition |
|---|---|---|---|
| HIG-01 Skills | Remote installer piped to shell; all skills grant Bash; network/provider actions and third-party API instructions; DNS resolution check is susceptible to DNS rebinding/TOCTOU in URL fetch path; manual-only evals | HIGH — broad agent execution authority and supply-chain exposure; one potential SSRF hardening gap | DEFER |
| HIG-02 CLI | Installer obtains latest release dynamically, checksum verifies archive, but default path may use sudo and installs system-wide; binary implementation was not inspectable through the available GitHub file connector paths | MEDIUM / NOT_VERIFIED — installer controls visible; binary internals and auth handling not audited | DEFER |
| HIG-03 Video Engineer | Local Chrome/WebGPU runtime; optional remote Runpod tooling can execute commands as root and uses SSH; remote probe disables Chrome sandbox; local renderer uses unsafe WebGPU flags | HIGH if remote pod path enabled; MEDIUM for local-only path with untrusted scene inputs | DEFER |
| HIG-04 App Templates | API key stored in a 30-day HttpOnly cookie; platform client logs full request bodies and response payloads, potentially including prompts and user parameters; upload ticket URLs accepted from upstream HTTPS response without host allowlist | MEDIUM-HIGH — concrete sensitive-data logging concern | DEFER |

Severity labels are source-review prioritization, not CVSS scores. Exploitability has not been demonstrated.

## 2. Evidence integrity and limitations

Pinned upstream commits:

| ID | Repository | Commit |
|---|---|---|
| HIG-01 | https://github.com/higgsfield-ai/skills | `27000402070db19d958789d05b3b52b6f4718d7c` |
| HIG-02 | https://github.com/higgsfield-ai/cli | `fd21e7cb550b5835cc00c6b4abfea0c02fe77ff2` |
| HIG-03 | https://github.com/higgsfield-ai/higgsfield-video-engineer | `082bfd7b7b0b863799fa9afcdfeb3e84ba72e015` |
| HIG-04 | https://github.com/higgsfield-ai/app-templates | `2b6343a7f2cbe9f629aeb84e7fd98e7ad32a1af3` |

Evidence was read from exact pinned refs where supported. The GitHub connector could fetch selected files but did not expose a reliable full repository tree or HIG-02 source files at guessed Go paths. HIG-02 source implementation, dependency graph, and binary internals are therefore explicitly NOT_VERIFIED.

No local SHA-256 hashes, SBOM, SAST, dependency vulnerability scan, test results, runtime traces, or network captures were generated. Do not interpret source-level controls as tested controls.

## 3. HIG-01 — higgsfield-ai/skills

### 3.1 Scope inspected

- Root README, INSTALL.md, INSTALL_FOR_AGENTS.md, CLAUDE.md, VERSION, LICENSE and setup script.
- Codex/Claude/Cursor plugin manifests and all nine SKILL.md frontmatters.
- `scripts/update-check.sh`.
- Website security/auth/FNF SDK guidance.
- Brandkit helper source including SVG URL retrieval and validation.
- Faceless-video assembly helper sources.
- Meshy API integration documentation.
- Evals README and scenarios.

### 3.2 Findings

#### HIG-01-F01 — Remote installer executed through an unpinned shell pipeline

**Severity: HIGH (supply-chain control gap)**  
**Evidence:** root `setup` invokes `curl -fsSL https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh` when the CLI is missing. INSTALL.md and INSTALL_FOR_AGENTS.md repeat this installation pattern. The remote ref is the mutable `main` branch rather than a pinned release/commit. The CLI installer itself checks the downloaded release archive against a release checksum, which is a positive control, but the bootstrap script that is piped into the shell is not pinned or independently verified before execution.

**Impact:** a compromised or malicious upstream change to the installer can execute arbitrary commands in the user's shell context before the binary checksum check occurs.

**Required control:** pin installer source to a reviewed commit or signed release; download to a file, verify a pinned digest/signature, inspect, then execute. Avoid pipe-to-shell in governed developer environments.

#### HIG-01-F02 — All skills request Bash capability

**Severity: HIGH (execution-authority exposure)**  
**Evidence:** all nine SKILL.md frontmatters inspected declare `allowed-tools: Bash`. Skill instructions direct agents to use the CLI, local files, FFmpeg, Python helpers, git/bun, and, in some workflows, deploy/publish operations.

**Impact:** a prompt-injected or misrouted task may cause the agent to issue shell commands with the host's available permissions. The metadata does not itself establish a sandbox or command allowlist.

**Required control:** run only with an agent host that enforces per-command approval/sandboxing; default-deny network and writes; scope working directory; require explicit approval for install, upload, training, generation, deployment, publication, secrets, and destructive operations. Test malicious document/web content before enabling.

#### HIG-01-F03 — Network and provider operations are intrinsic to several skills

**Severity: HIGH (data egress / cost boundary)**  
**Evidence:** CLAUDE.md routes primary generation through the Higgsfield CLI; authentication persists under `~/.config/higgsfield/credentials.json`. Skills document local media paths being auto-uploaded, hosted generation, profile/workspace/credits operations, website create/deploy/publish, and Soul training. Soul training documentation explicitly states it requires a paid plan. Website and marketing workflows may fetch user-supplied URLs. Website instructions document external Meshy API use with a user-configured bearer key.

**Impact:** local media, prompts, URLs, and job parameters can leave the local environment; some workflows can incur credits or third-party API charges. Offline-only operation cannot deliver the core hosted generation features.

**Required control:** no credential mounting; network egress denied by default; no external API or provider call without explicit approval, cost estimate, and data disclosure. Treat third-party API keys as separate secrets and do not pass them through model prompts or shell logs.

#### HIG-01-F04 — DNS rebinding / TOCTOU hardening gap in public-host validation

**Severity: MEDIUM (potential SSRF bypass; not exploited)**  
**Evidence:** `higgsfield-brandkit/scripts/brandkit.py` resolves a hostname with `socket.getaddrinfo` and rejects non-global addresses, then performs the HTTPS request through urllib. The HTTP client performs a new hostname resolution when connecting. This creates a potential time-of-check/time-of-use window in which DNS answers can differ between validation and connection. Redirects are revalidated, which is a positive control; TLS certificate verification is enabled.

**Impact:** a hostile DNS response that changes between the validation lookup and connection may undermine the intended private-address block.

**Required control:** connect to a validated resolved IP while preserving TLS SNI/hostname verification, or use a transport with DNS pinning; reject all non-global resolved addresses at the actual connection; add rebinding tests. This is a potential weakness, not a confirmed exploit.

#### HIG-01-F05 — Manual-only evaluation framework

**Severity: MEDIUM (quality and regression assurance gap)**  
**Evidence:** `evals/README.md` explicitly says there is no automated runner; scenarios are run manually in a fresh Claude Code session. The scenario set includes operations that can create paid generation jobs, train identity models, deploy sites, or publish games.

**Impact:** skill behavior is not reproducibly validated in CI; manual eval scenarios could trigger real provider costs or deployment if run without guardrails.

**Required control:** convert safe scenarios to deterministic offline tests; mark provider-dependent scenarios as gated; use mocks/recorded fixtures; add explicit no-billing/no-deploy safety assertions.

#### HIG-01-F06 — Third-party API key and outbound data path in website game reference

**Severity: MEDIUM (third-party secret governance)**  
**Evidence:** `higgsfield-websites/references/game-meshy-api.md` documents direct calls to `api.meshy.ai` with `Authorization: Bearer $MESHY_API_KEY`. This is an explicit exception to the root CLI convention and uses a separate third-party credential.

**Impact:** the skill can guide an agent to transmit user assets and a third-party secret to another provider. This may carry separate privacy and billing implications.

**Required control:** require explicit provider consent, secret-manager storage, no inline/prompt disclosure, least privilege, egress allowlist, retention disclosure, and cost estimate. Keep this path disabled in the GDES evaluation.

#### HIG-01-F07 — Positive SVG validation controls, but sanitizer remains untested

**Severity: INFORMATIONAL / TEST REQUIRED**  
**Evidence:** SVG helper rejects DTD/entities, script/foreignObject/iframe/object/embed/image elements, event handlers, external references, CSS imports, oversized documents, and excessive element counts. It also limits downloaded SVG size, requires HTTPS, checks public DNS addresses, and caps redirects.

**Residual concern:** validation is implemented with regular expressions rather than a full namespace-aware XML parser and has not been fuzzed. No bypass is asserted from static inspection alone.

**Required control:** parse with a hardened XML parser with external entities disabled; canonicalize namespaces; fuzz malformed SVG, case/namespace variants, CSS URL forms, and resource exhaustion.

#### HIG-01-F08 — Installation count documentation inconsistency

**Severity: LOW (documentation integrity)**  
**Evidence:** README/setup list nine skills, while INSTALL.md and INSTALL_FOR_AGENTS.md refer to eight.

**Required control:** align docs and automated inventory.

### 3.3 HIG-01 disposition

**DEFER.** The skills catalog is not safe to install into the primary developer environment based on this review. Any future evaluation must isolate Bash, prevent credential access, deny outbound network by default, and test the remote installer and skill instructions independently.

## 4. HIG-02 — higgsfield-ai/cli

### 4.1 Scope inspected

- Pinned README, LICENSE and `install.sh`.
- Source paths for common Go CLI layouts and manifests were not retrievable through the available file connector at this commit; source tree and binary implementation were not verified.

### 4.2 Findings

#### HIG-02-F01 — Installer can write to a system directory and invoke sudo

**Severity: MEDIUM (privilege boundary)**  
**Evidence:** installer defaults to `/usr/local`, creates `bin`, and uses `sudo` if it cannot write to the target directory. It installs the binary and metadata and creates command symlinks.

**Impact:** executing the installer can modify system-wide executable paths with elevated privileges.

**Required control:** use an explicit user-owned prefix such as `$HOME/.local`; do not run with sudo during evaluation; verify file ownership and permissions.

#### HIG-02-F02 — Dynamic latest-release selection

**Severity: MEDIUM (reproducibility and supply-chain)**  
**Evidence:** unless `--tag` is supplied, installer queries GitHub's latest release, downloads a platform archive and `checksums.txt`, then compares SHA-256.

**Positive control:** archive checksum is checked before extraction/install.

**Residual concern:** checksum and archive are retrieved from the same release trust domain; the installer does not independently verify a signed provenance statement or pinned digest. The mutable latest-release pointer means identical invocations can install different binaries over time.

**Required control:** pin an explicit tag and verify a signed provenance/attestation or independently trusted digest; record release metadata.

#### HIG-02-F03 — Binary/auth/network behavior not inspected

**Severity: NOT_VERIFIED (material evidence gap)**  
**Evidence:** README documents OAuth/device-flow authentication, token inspection, hosted API generation, uploads and other platform commands. No source files or dependency manifests were successfully retrieved in this review.

**Required control:** obtain a complete source archive at the pinned commit; inspect token storage/permissions, HTTP redirects, TLS, logging/redaction, file upload path handling, process execution, update behavior and dependency inventory before runtime testing.

### 4.3 HIG-02 disposition

**DEFER.** Installer review is partial; binary internals and credential controls remain unverified. No installation or authentication performed.

## 5. HIG-03 — higgsfield-ai/higgsfield-video-engineer

### 5.1 Scope inspected

- Pinned README, MIT LICENSE, package.json, engine package-lock, skill instructions, setup.sh, engine host, render CLI, and optional Runpod helper.

### 5.2 Findings

#### HIG-03-F01 — Optional remote pod tool executes commands as root and provides remote shell

**Severity: HIGH when remote mode is enabled**  
**Evidence:** `tools/rp` SSHes to pods as `root`, exposes `rp sh <pod> '<command>'`, uploads project files, and runs Node scripts remotely. It uses an SSH private key from the user's home and `RUNPOD_API_KEY` through runpodctl. The helper includes deny/allow filters for uploaded files, including exclusions for credential-like filenames and hidden files; this is a positive control but is not a complete content-level secret scanner.

**Impact:** remote execution has broad authority over the pod and uploaded project data. A malicious project script or compromised pod can access the remote environment and any credentials available there.

**Required control:** keep remote mode disabled for this evaluation; if ever approved, use disposable pods, non-root accounts, short-lived credentials, strict egress, explicit file manifest, and teardown verification. Remote GPU rental is chargeable and prohibited here.

#### HIG-03-F02 — Remote Chrome probe disables browser sandbox

**Severity: HIGH when remote probe is enabled**  
**Evidence:** `tools/rp_pod/probe.mjs` launches Chrome with `--no-sandbox` and WebGPU-related flags.

**Impact:** browser compromise or malicious renderer content has a weaker process-isolation boundary, particularly when running as root on a remote pod.

**Required control:** do not run untrusted scene/project content in this configuration; remove `--no-sandbox` where supported and use an unprivileged account/container boundary.

#### HIG-03-F03 — Local renderer enables unsafe WebGPU and weakens watchdog behavior

**Severity: MEDIUM (local attack surface / stability)**  
**Evidence:** `engine/src/host.mjs` launches Chrome with `--enable-unsafe-webgpu`, `--disable-dawn-features=disallow_unsafe_apis`, `--disable-gpu-watchdog`, and GPU override flags. The primary local launch does not include `--no-sandbox`. The local HTTP server binds to loopback, uses a random 24-byte token for result POSTs, validates expected frame/result sizes, and resolves web asset real paths to prevent symlink escape; these are positive controls.

**Impact:** unsafe GPU API exposure and disabled GPU watchdog can increase browser/GPU stability and attack-surface risk when processing untrusted scenes or renderer code.

**Required control:** use trusted synthetic scenes only; keep Chrome sandbox enabled; avoid disabling watchdog for normal use; add resource limits and renderer input validation.

#### HIG-03-F04 — Setup requires network dependency retrieval

**Severity: LOW-MEDIUM (offline constraint)**  
**Evidence:** setup.sh checks npm registry reachability and runs `npm ci`; the command uses `--ignore-scripts`, which is a positive control. package-lock pins `puppeteer-core` and `three` and contains package integrity hashes.

**Impact:** the normal setup is not fully offline unless dependencies are pre-cached. No package installation or registry access was performed.

**Required control:** use a pre-verified dependency cache or offline mirror; validate lockfile integrity and package licenses; do not execute install scripts.

### 5.3 HIG-03 disposition

**DEFER.** Local-only rendering may be suitable for a controlled offline test, but no execution was performed. Remote Runpod path is out of scope and must remain disabled.

## 6. HIG-04 — higgsfield-ai/app-templates

### 6.1 Scope inspected

- Pinned README, AGENTS.md, package.json, pnpm-lock.yaml, credentials.ts, actions.ts, platform.ts, upload route, and upload-contract.ts.

### 6.2 Findings

#### HIG-04-F01 — Sensitive prompt/request data written to server logs

**Severity: HIGH (privacy/data exposure)**  
**Evidence:** `generation/platform.ts` logs `body` for every platform request and logs parsed `payload` for responses except the upload-ticket endpoint. Generation request bodies can include prompts and model parameters. The AGENTS.md explicitly states that prompts, raw params, headers, tokens, URLs, filenames, emails, workspace names and raw bodies must not be emitted to observability.

**Impact:** prompts and potentially sensitive user-provided generation parameters may be retained in server logs and observability systems. This directly conflicts with the repository's own logging contract.

**Required control:** remove request-body and response-payload logging; use allowlisted metadata only (method, logical operation, status, safe error code); add tests that assert prompt, token, URL and filename redaction.

#### HIG-04-F02 — API key stored in long-lived cookie

**Severity: MEDIUM (credential lifecycle)**  
**Evidence:** `credentials.ts` stores the API key in a JSON cookie named `api_key`, with HttpOnly, SameSite=Lax, Secure only in production, Path=/ and maxAge 30 days. The cookie is not visibly encrypted or signed in this helper.

**Positive controls:** HttpOnly prevents ordinary client-side JavaScript access; Secure is enabled in production; cookie path is scoped to root.

**Impact:** a long-lived bearer-equivalent API key is carried as a browser cookie for up to 30 days. In development, Secure is disabled. The source inspected does not show an encryption/signing layer or rotation mechanism.

**Required control:** prefer server-side encrypted storage or short-lived credential sessions; set Secure in all HTTPS environments; use an appropriate SameSite/CSRF design; support rotation and revocation; avoid logging or returning cookie contents.

#### HIG-04-F03 — Platform client logs raw response payloads

**Severity: HIGH (privacy/data exposure)**  
**Evidence:** `platform.ts` logs parsed response payloads for non-upload requests. Status/result responses can include media URLs, status details, and error payloads.

**Impact:** sensitive media URLs, internal provider metadata, or error data may be retained in logs.

**Required control:** log status and sanitized error codes only; redact URLs and raw bodies.

#### HIG-04-F04 — Upload ticket URL trust boundary lacks host allowlist

**Severity: MEDIUM (upstream response validation)**  
**Evidence:** `upload-contract.ts` requires HTTPS, rejects URL username/password, checks content type, and rejects Authorization/Cookie upload headers. It does not restrict upload_url/public_url hostnames to a documented provider/storage allowlist.

**Impact:** if the upstream API response or API base is compromised/misconfigured, the browser may be instructed to PUT user media to an arbitrary HTTPS host. This is a defense-in-depth gap; no malicious response was tested.

**Required control:** enforce provider/storage host allowlists, validate permitted header names, constrain redirects, and test malicious ticket payloads. Ensure browser PUT requests never include platform credentials.

#### HIG-04-F05 — Upload route permits requests without Origin header

**Severity: LOW-MEDIUM (CSRF hardening gap; context-dependent)**  
**Evidence:** upload route rejects a present Origin that differs from request URL origin, but accepts requests where Origin is absent.

**Impact:** acceptance of missing-Origin requests weakens the explicit origin policy. Actual exploitability depends on browser behavior, cookie SameSite enforcement, framework protections, and deployment context; not demonstrated.

**Required control:** require a valid Origin for browser-originated requests or use a robust CSRF token strategy; add cross-origin and missing-Origin negative tests.

### 6.3 HIG-04 disposition

**DEFER.** The raw request/response logging is a concrete remediation blocker before adoption. Credential lifecycle and upload host validation also require review and negative tests.

## 7. Cross-candidate control matrix

| Control | HIG-01 | HIG-02 | HIG-03 | HIG-04 |
|---|---|---|---|---|
| Pinned source SHA | Yes | Yes | Yes | Yes |
| License | MIT verified | MIT verified | MIT verified | Root license not verified in earlier intake |
| Install path reviewed | Yes | Yes | Yes | Package install not executed |
| Shell/process execution | Bash authority via skill metadata | Binary internals NOT_VERIFIED | Local Node/Chrome + optional root SSH | Build scripts and server actions |
| Credential storage reviewed | CLI path documented; CLI internals not reviewed | NOT_VERIFIED | SSH/Runpod env paths documented | API key cookie reviewed |
| Network egress | Hosted CLI + direct Meshy docs + URL fetch | Hosted platform API | npm registry; optional Runpod | Platform API + signed upload URLs |
| Prompt/data logging | No runtime logs reviewed | NOT_VERIFIED | Render logs only statically reviewed | Raw body/response logs observed |
| Dependency scan | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Runtime security tests | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN |
| Overall | DEFER | DEFER | DEFER | DEFER |

## 8. Mandatory remediation and verification backlog

### P0 — before any adoption discussion
1. HIG-01: pin and verify installer source; reduce Bash permission scope or prove host sandboxing; isolate all credentials and network egress.
2. HIG-04: remove raw request/response body logging and add redaction tests.
3. HIG-02: retrieve complete source/release provenance and inspect credential storage, TLS, redirects, file uploads and logging before binary use.
4. HIG-03: disable remote Runpod scripts; prohibit root SSH and no-sandbox browser launch in any approved test environment.

### P1 — before runtime evaluation
5. HIG-01: add offline automated eval runner, fuzz SVG parser, test DNS rebinding defenses, and verify no external provider/credit operation can occur.
6. HIG-03: run local-only renderer with trusted synthetic scene, sandboxed Chrome, resource caps and no external network.
7. HIG-04: enforce upload host allowlist and CSRF/origin policy; test malicious ticket responses.
8. All candidates: generate SBOM, license inventory, dependency vulnerability report, and reproducibility manifest from pinned source.

## 9. Test execution ledger

| Test | Status | Notes |
|---|---|---|
| Static source review | PARTIAL COMPLETE | Selected files at pinned commits reviewed |
| Installer execution | NOT_RUN | Intentionally prohibited |
| Dependency installation | NOT_RUN | No package downloads |
| SAST / dependency scan / SBOM | NOT_RUN | No local source workspace/runner |
| Prompt injection tests | NOT_RUN | No agent runtime invocation |
| SSRF/DNS rebinding tests | NOT_RUN | Static concern only |
| Credential redaction tests | NOT_RUN | Source logging defect observed; no runtime test |
| Upload malicious-ticket tests | NOT_RUN | Static control review only |
| Codex / VS Code compatibility invocation | NOT_RUN | No agent runtime |
| Network egress capture | NOT_RUN | No candidate execution |
| Output reproducibility | NOT_RUN | No outputs generated |

## 10. Standards Owner recommendation

**DEFER — do not approve any of the four candidates for primary-environment installation, production use, or GDES standards promotion.**

The audit found concrete hardening work, particularly HIG-01's mutable remote installer/Bash authority and HIG-04's raw prompt/response logging. HIG-02 source internals remain materially unverified. HIG-03's local renderer is a possible isolated offline candidate only after the remote path is disabled and Chrome/GPU sandboxing is addressed.

This recommendation is based on static evidence only. It is not a certification, penetration-test result, or assertion that no additional vulnerabilities exist.
