# HIG-01 F01 Remediation Notes

The original `setup` script installed the CLI using a mutable URL and piped the response directly into a shell. This overlay removes that execution path. It does not attempt to reproduce or validate the upstream CLI installer.

## Required follow-up before runner acceptance

1. Expand the snapshot to every source file in the pinned upstream tree that participates in tool permissions, network fetches, Meshy integration, and SVG parsing.
2. Add exact-source and patch-level provenance for every file.
3. Add positive/negative fixtures for each control.
4. Update runner policy so checks are specific to source paths and semantic control boundaries; current regex policy is only a triage heuristic.
5. Run the offline self-test and candidate scan in an isolated environment with egress disabled; preserve raw output and SHA-256 hashes.
6. Have a human reviewer inspect false positives/false negatives. A regex pass is not a security acceptance.

Current F01 state: PATCH_PROPOSED, NOT_TESTED.
