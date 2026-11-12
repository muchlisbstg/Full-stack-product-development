# HIG-01 F02 — Remediation Evidence v1.0

**Upstream:** `higgsfield-ai/skills@27000402070db19d958789d05b3b52b6f4718d7c`  
**Candidate branch:** `gdes/higgsfield-hig01-f02-least-privilege`  
**Tested commit:** `b3f43d05986ed31db18cacc409c1e3d0c67c487e`  
**Actions run:** [43090014092](https://github.com/muchlisbstg/Full-stack-product-development/actions/runs/43090014092)

## Source finding

All nine tracked skill frontmatter blocks declared `allowed-tools: Bash`. This is a skill-level broad shell tool grant.

## Candidate changes

- Added nine source overlays under `scan-targets/HIG-01/F02-remediated/`.
- Removed `allowed-tools: Bash` from all nine frontmatter blocks.
- Added a consistent execution authority section to each skill. It makes command examples reference-only, requires approval for exact command/scope/effects, prohibits implicit privileged/destructive operations, and requires sandboxed execution or manual handoff.
- Added `targets/HIG-01/F02_REMEDIATION_POLICY.md` documenting the threat model and acceptance criteria.
- Added `test_f02_policy.py` with positive and negative policy tests.
- Updated the offline workflow to execute the F02 policy test on this dedicated branch.

## Automated test evidence

GitHub Actions run `43090014092` completed successfully:
- Existing offline runner self-test: **5/5 passed**.
- F02 source policy tests: **4/4 passed**.
- The positive test checked all nine candidate skill files.
- Negative tests confirmed that a reintroduced Bash grant and a missing execution-boundary clause are rejected.
- Existing static scanner reported HIG-01-F02 as `PASS_STATIC_HEURISTIC`; other HIG-01 findings remain `NEEDS_REVIEW`.
- Overall release gate remains `BLOCKED`.

## Residual risks / not verified

1. This is source-level policy remediation. It does not prove Claude Code, Codex, Cursor, or another host actually removes/restricts Bash capability when the skill is loaded.
2. Host permission configuration, command approval prompts, sandbox filesystem/network isolation, and denial behavior have not been exercised.
3. Plugin manifest `capabilities: [Read, Write]` is product metadata and was not treated as proof of shell permission. Its host-specific semantics remain to be verified.
4. Commands embedded in the skill bodies still exist as documentation. The new boundary requires approval, but actual tool enforcement is host-owned.
5. No candidate script, CLI command, installer, provider, network request, or billing action was executed.
6. F03 provider/network controls and F01 installer references remain separate open findings; this F02 patch does not close them.

## Disposition

**F02 source remediation: PASS_SOURCE_POLICY_TESTS (4/4).**  
**F02 host-enforcement verification: NOT_RUN.**  
**F02 overall acceptance: PARTIAL / NEEDS_HOST_VERIFICATION.**  
**HIG-01 release gate: BLOCKED.**

Do not promote this to a security PASS or runtime approval until host-level least-privilege controls are independently verified.
