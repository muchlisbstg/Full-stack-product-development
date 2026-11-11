# GDES-REG-002 — Higgsfield Repository Intake Register v1.0

**Status:** EVALUATION IN PROGRESS — STATIC REVIEW ONLY  
**Evaluation track:** Isolated Skills Evaluation Lab  
**Source organization:** https://github.com/higgsfield-ai  
**Date recorded:** 2026-11-12

## 1. Scope

Register four public repositories from the Higgsfield AI GitHub organization as evaluation candidates. Registration is not an endorsement, approval, installation, adoption, or authorization to use paid services.

## 2. Candidate inventory

| ID | Upstream repository | Candidate type | Evaluation priority | Pinned source SHA | Current status |
|---|---|---|---|---|---|
| HIG-01 | https://github.com/higgsfield-ai/skills | Agent skills / creative workflows | P0 | `27000402070db19d958789d05b3b52b6f4718d7c` | Static review completed; runtime NOT_RUN |
| HIG-02 | https://github.com/higgsfield-ai/cli | Command-line integration | P0 | `fd21e7cb550b5835cc00c6b4abfea0c02fe77ff2` | First-pass static review; runtime NOT_RUN |
| HIG-03 | https://github.com/higgsfield-ai/higgsfield-video-engineer | Code-based video / WebGPU workflow | P1 | `082bfd7b7b0b863799fa9afcdfeb3e84ba72e015` | First-pass static review; runtime NOT_RUN |
| HIG-04 | https://github.com/higgsfield-ai/app-templates | Application templates / UI scaffolding | P1 | `2b6343a7f2cbe9f629aeb84e7fd98e7ad32a1af3` | First-pass static review; runtime NOT_RUN |

## 3. Evaluation gates

Each candidate is evaluated independently in a disposable, isolated environment.

1. **Source integrity:** upstream owner, repository visibility, default branch, pinned commit SHA, release/tag, and license verification.
2. **Structure and quality:** repository inventory, skill metadata and instructions (where applicable), scripts, configuration, and documentation.
3. **Compatibility:** Codex and VS Code discovery/invocation compatibility; distinguish static layout checks from actual runtime invocation.
4. **Security:** dependency and install-script review, permission scope, credential handling, prompt-injection exposure, filesystem/network access, and side-effect controls.
5. **Cost and provider dependency:** identify API/provider requirements, network calls, quotas, and paid features. Do not incur charges.
6. **Reproducibility:** record exact commands, environment, versions, source SHA, logs, output hashes, and repeatability.
7. **Output quality:** assess generated artifacts against deterministic synthetic fixtures where applicable.

## 4. Mandatory execution constraints

- Offline-first. Use network access only where source retrieval or a candidate's documented function genuinely requires it.
- No paid API, subscription, billing activation, or chargeable provider invocation.
- No personal API keys, production credentials, private business documents, or real customer data.
- Use synthetic fixtures and disposable workspaces only.
- Do not install candidates into the primary development environment.
- Do not execute unreviewed scripts with elevated privileges or unrestricted filesystem/network access.
- Unsupported or unexecuted checks must be recorded as **NOT_RUN**, not PASS.
- No changes to product repositories, main branches, production, staging, infrastructure, DNS, release, or deployment.
- No adoption or standards promotion without a separate Standards Owner decision.

## 5. Evidence ledger

| Candidate | Source pinned | License | Static review | Runtime | Security negative tests | Cost/provider | Result |
|---|---|---|---|---|---|---|---|
| HIG-01 | OBSERVED | MIT verified | PARTIAL — source/docs/setup/manifests reviewed; automated validators NOT_RUN | NOT_RUN | NOT_RUN | Hosted CLI/API required for primary generation workflows; no calls made | DEFER |
| HIG-02 | OBSERVED | MIT verified | PARTIAL — README and installer reviewed | NOT_RUN | NOT_RUN | Hosted API/auth required for generation; no calls made | DEFER |
| HIG-03 | OBSERVED | MIT verified | PARTIAL — README, package manifest, skill workflow reviewed | NOT_RUN | NOT_RUN | Local rendering documented; optional Runpod is chargeable and excluded | DEFER |
| HIG-04 | OBSERVED | NOT_VERIFIED | PARTIAL — README, package manifest, AGENTS contract reviewed | NOT_RUN | NOT_RUN | Hosted API/key required for generation; no calls made | DEFER |

Detailed evidence: [GDES_REG_002_HIGGSFIELD_EVALUATION_EVIDENCE_v1.0.md](../evaluations/GDES_REG_002_HIGGSFIELD_EVALUATION_EVIDENCE_v1.0.md).

## 6. Required evidence bundle

For every candidate retain:
- source URL and pinned commit SHA;
- license and dependency inventory;
- environment and tool versions;
- exact invocation commands;
- network/provider observations and cost disposition;
- stdout/stderr logs and exit codes;
- output artifacts and SHA-256 hashes;
- security findings and negative-test results;
- compatibility matrix for Codex and VS Code;
- reproducibility notes and final disposition.

## 7. Governance disposition

**Current recommendation: DEFER — insufficient runtime and security evidence.**

The present evidence is source/static review only. No candidate has passed runtime, compatibility, dependency-security, or negative-side-effect testing. No candidate is approved for installation into the primary development environment, production use, or promotion to a GDES standard. Continue only in an isolated disposable offline runner and submit the resulting evidence for Standards Owner review.
