# HIG-01 Source Snapshot — Remediation Candidate 0.1

**Disposition:** PARTIAL / NOT READY FOR ACCEPTANCE  
**Candidate:** HIG-01 — higgsfield-ai/skills  
**Upstream commit:** `27000402070db19d958789d05b3b52b6f4718d7c`  
**Upstream repository:** https://github.com/higgsfield-ai/skills  
**Snapshot branch:** `gdes/higgsfield-hig01-remediation-snapshot`  
**Snapshot mode:** text-only; source is inert and must not be executed.

## Snapshot contents

| Layer | File | Provenance |
|---|---|---|
| Upstream baseline | `upstream/setup` | Exact raw source at pinned upstream commit |
| Upstream baseline | `upstream/INSTALL.md` | Exact raw source at pinned upstream commit |
| Upstream baseline | `upstream/INSTALL_FOR_AGENTS.md` | Exact raw source at pinned upstream commit |
| Remediation overlay | `remediated/setup` | Proposed local candidate; not upstream-authorized |

## Finding disposition

| Finding | Current status | Evidence / next action |
|---|---|---|
| HIG-01-F01 mutable `curl | sh` | **PATCH_PROPOSED** | Candidate setup contains no curl, remote installer, CLI authentication, or provider call. CLI provisioning is explicitly external and separately reviewed. |
| HIG-01-F02 blanket Bash authority | **NOT_REMEDIATED** | Need full inventory of all skill agent manifests and tool permissions; restrict by command, workspace, sandbox and approval. |
| HIG-01-F03 provider/network side effects | **NOT_REMEDIATED** | Need full skill/prompt/script inventory and explicit deny-by-default egress + user confirmation gates. |
| HIG-01-F04 public URL fetch / DNS rebinding | **NOT_REMEDIATED** | Relevant fetch implementation has not yet been included in this curated snapshot; require DNS/IP pinning and redirect revalidation. |
| HIG-01-F05 evaluation controls | **PARTIAL** | Offline runner scaffold exists; self-test and this candidate scan are still NOT_RUN. |
| HIG-01-F06 Meshy third-party API | **NOT_REMEDIATED** | Need inventory of Meshy integration paths, secret handling, egress and cost/consent gates. |
| HIG-01-F07 SVG/XML parser hardening | **NOT_REMEDIATED** | Need exact parser inventory, safe parser implementation, DTD/entity rejection and fuzz/negative tests. |
| HIG-01-F08 skill-count documentation | **NOT_REMEDIATED** | Reconcile all manifests, docs and current skill directory count after full snapshot. |

## F01 candidate design

- The candidate setup requires explicit host selection.
- It refuses to install the CLI implicitly.
- It does not call `curl`, `sh`, `higgsfield auth login`, or any provider endpoint.
- It refuses symlinked target directories and existing destination collisions.
- CLI installation remains a separate, user-approved process requiring independently pinned and verified provenance.

## Acceptance gate

This is a curated, partial remediation snapshot—not a complete HIG-01 source tree and not evidence that HIG-01 is secure. Do not label it PASS. Do not run candidate scripts. The offline runner may read the text files only. Runtime, network, provider, API, credential, and billing tests remain prohibited until all P0 source findings are closed and a separate runtime authorization is granted.

## Reproducibility

All upstream baseline files are tied to the commit above. The original repository must remain unchanged. Any later snapshot refresh must create a new version and record a new upstream commit SHA; do not silently replace this baseline.
