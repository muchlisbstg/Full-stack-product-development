# GDES-REG-002 — Higgsfield Repository Intake Register v1.0

**Status:** INTAKE — NOT EVALUATED  
**Evaluation track:** Isolated Skills Evaluation Lab  
**Source organization:** https://github.com/higgsfield-ai  
**Date recorded:** 2026-11-12

## 1. Scope

Register four public repositories from the Higgsfield AI GitHub organization as evaluation candidates. Registration is not an endorsement, approval, installation, adoption, or authorization to use paid services.

## 2. Candidate inventory

| ID | Upstream repository | Candidate type | Evaluation priority | Intake status |
|---|---|---|---|---|
| HIG-01 | https://github.com/higgsfield-ai/skills | Agent skills / creative workflows | P0 | INTAKE |
| HIG-02 | https://github.com/higgsfield-ai/cli | Command-line integration | P0 | INTAKE |
| HIG-03 | https://github.com/higgsfield-ai/higgsfield-video-engineer | Code-based video / WebGPU workflow | P1 | INTAKE |
| HIG-04 | https://github.com/higgsfield-ai/app-templates | Application templates / UI scaffolding | P1 | INTAKE |

## 3. Evaluation gates

Each candidate must be evaluated independently in a disposable, isolated environment.

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
- No changes to product repositories, main branches, production, staging, infrastructure, DNS, or deployment.
- No adoption or standards promotion without a separate Standards Owner decision.

## 5. Initial evidence ledger

| Candidate | Source commit pinned | License verified | Static review | Runtime invocation | Security review | Cost/provider review | Result |
|---|---|---|---|---|---|---|---|
| HIG-01 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | PENDING |
| HIG-02 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | PENDING |
| HIG-03 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | PENDING |
| HIG-04 | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | NOT_RUN | PENDING |

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

**Current recommendation: DEFER — intake only.**

No candidate has passed evaluation. No repository is approved for installation, production use, or promotion to a GDES standard. A separate evidence-backed evaluation and Standards Owner review are required.
