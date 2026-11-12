# HIG-01 Remediation Snapshot — Execution Status

**Snapshot branch:** `gdes/higgsfield-hig01-remediation-snapshot`  
**Upstream source:** `higgsfield-ai/skills@27000402070db19d958789d05b3b52b6f4718d7c`  
**Candidate commit tested:** `c43c6379b491a860371245f7fd6cbae2213fcfd0`  
**Disposition:** PARTIAL / BLOCKED

## Evidence status

| Control | Status |
|---|---|
| Pinned upstream baseline captured | COMPLETE |
| Baseline blob SHA parity | VERIFIED for setup, INSTALL.md, INSTALL_FOR_AGENTS.md |
| Proposed F01 setup overlay | CREATED |
| Runner self-test | PASS — 5/5 synthetic harness tests |
| HIG-01 static scan | NEEDS_REVIEW — 1 remediated source file scanned |
| F01 mutable installer control | PASS_STATIC_HEURISTIC |
| F02 Bash authority | NEEDS_REVIEW |
| F03 provider/network side effects | NEEDS_REVIEW |
| F04 public URL fetch / DNS rebinding | NEEDS_REVIEW |
| F07 SVG/XML parser hardening | NEEDS_REVIEW |
| F05/F06/F08 full-source assessment | NOT_VERIFIED — source inventory incomplete |
| HIG-02/HIG-03/HIG-04 | NOT_RUN |
| Runtime/provider/network tests | NOT_AUTHORIZED |

## Actions evidence

- Workflow: [HIG-01 Offline Remediation Snapshot](https://github.com/muchlisbstg/Full-stack-product-development/actions/workflows/gdes-higgsfield-hig01-offline.yml)
- Run: [43088896162](https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/43088896162)
- Tested commit: `c43c6379b491a860371245f7fd6cbae2213fcfd0`
- Job: `130760414952`
- Runner self-test: 5 tests, all successful.
- Static result: HIG-01 `NEEDS_REVIEW`; F01 `PASS_STATIC_HEURISTIC`; F02/F03/F04/F07 `NEEDS_REVIEW`.
- Release gate: `BLOCKED`.
- The workflow job conclusion is success because the expected blocked result is recorded as evidence; this is not a security PASS.

## Scope and limitations

The workflow hashes the pinned source files, runs the harness self-tests against synthetic fixtures, and reads candidate source as inert text. It does not import or execute candidate scripts, install dependencies, call external providers, use credentials, or perform runtime/network testing.

The upstream baseline remains under `targets/HIG-01/upstream/`. Only the separate `scan-targets/HIG-01/` remediation overlay is scanned. This separation prevents known-vulnerable baseline examples from being misclassified as candidate regressions.

The current runner is regex-based and only supports triage. It can miss semantic vulnerabilities and can produce false positives/negatives. F01 still requires manual review of installer provenance and the complete installation pathway. The other findings remain open.

## Next evidence required

1. Expand the snapshot to every relevant HIG-01 source file, including all agent tool-permission manifests, network/URL-fetch implementations, Meshy API paths, and SVG/XML parser paths.
2. Implement source-level remediation and positive/negative tests for F02–F04 and F06–F08.
3. Improve runner path-aware rules and test against known-positive and known-negative fixtures.
4. Preserve each exact Actions run URL, commit SHA, raw result JSON and file hashes.
5. Keep runtime evaluation disabled until all P0 source findings are closed and separately authorized.


## Source inventory expansion — 2026-11-12

- Pinned upstream recursive tree retrieved successfully: **161 tracked blobs**, `truncated=false`, commit `27000402070db19d958789d05b3b52b6f4718d7c`.
- Added [SOURCE_INVENTORY_v1.0.md](./SOURCE_INVENTORY_v1.0.md), recording all 161 paths and Git blob SHAs plus F02–F08 source mapping.
- Inventory confirms **nine** `*/SKILL.md` files, not eight. Multiple skill instructions repeat the mutable CLI installer command; F01 remediation must therefore cover every affected instruction, not only root `setup`.
- Direct source inspection found `higgsfield-faceless-video/scripts/assemble_blocks.sh` uses `curl -fsSL` for HTTP(S) media inputs. URL handling and redirect/SSRF constraints need review.
- `higgsfield-websites/references/game-meshy-api.md` documents Meshy API calls with `MESHY_API_KEY` bearer authorization and POST/GET/DELETE polling examples. This is a provider integration instruction path, not proof that the API was executed.
- `higgsfield-websites/references/security.md` contains SSRF/fetch security guidance and example code; this must be distinguished from production runtime implementation.
- Inventory is complete for tracked paths and Git blob identifiers, but not yet a complete byte-for-byte body snapshot of all 161 files. Full callsite review remains open.
- Runner self-test and previous candidate scan evidence remain as recorded above; this inventory commit itself has not yet been tested by Actions.


## F02 source remediation evidence — 2026-11-12

- All nine pinned `*/SKILL.md` files declared `allowed-tools: Bash` in upstream frontmatter.
- Created nine F02 remediation overlays under `scan-targets/HIG-01/F02-remediated/`; removed the broad Bash grant and added a per-skill execution approval boundary.
- Added `targets/HIG-01/F02_REMEDIATION_POLICY.md` and `targets/HIG-01/F02_REMEDIATION_EVIDENCE_v1.0.md`.
- Added semantic source-policy test `test_f02_policy.py`: 4/4 passed in Actions run [43090014092](https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/43090014092).
- Existing offline harness self-test: 5/5 passed in the same run.
- Static scanner result for F02: `PASS_STATIC_HEURISTIC`; F02 source policy tests: `PASS_SOURCE_POLICY_TESTS`.
- F02 host-enforcement verification: `NOT_RUN`. Codex/Claude/Cursor permission prompts, tool availability, and sandbox behavior are not yet proven.
- F03 provider/network side effects, F01 installer command removal, and other HIG-01 findings remain open. Overall release gate remains `BLOCKED`.
- No candidate shell/CLI scripts, installers, network calls, provider APIs, credentials, or billing actions were executed.
