# GDES-REG-002 Isolated Offline Test Runner

**Version:** 1.0.0  
**Mode:** Static screening of inert source text only  
**Runtime target:** Python 3.11+ standard library  
**Network:** No network APIs are used by the runner. Run in an OS/container/network namespace with outbound networking disabled for defense in depth.

## Safety contract

- Candidate code is read as UTF-8 text only; it is never imported, executed, installed, built, or evaluated.
- No dependency installation is required. No package manager is invoked.
- The runner scans only known source/text extensions under each target directory.
- Symlinks are rejected; resolved files must remain inside the candidate target directory.
- Do not place credentials, customer data, proprietary production media, or secrets in fixtures.
- Keep targets separate from the runner and from the product repositories.
- The runner's regular-expression checks are heuristic. A green result is `PASS_STATIC_HEURISTIC`, not security approval.

## Directory layout

```
tools/gdes-higgsfield-offline-runner/
  README.md
  runner.py
  policy.json
  test_runner.py
  targets/
    HIG-01/   # reviewed remediation source snapshot, text only
    HIG-02/
    HIG-03/
    HIG-04/
  results/
    latest.json
```

The `targets/` directories are intentionally empty in this governance change. Add only source snapshots of remediation commits after review. Do not fetch dependencies or execute repository scripts.

## Run in VS Code terminal

From this directory, using Python already present in the development environment:

```bash
python -I -S -B runner.py --self-test
python -I -S -B runner.py --targets ./targets --output ./results/latest.json
```

Flags:
- `-I`: isolated Python mode (ignores user site and Python environment variables).
- `-S`: do not import site packages.
- `-B`: do not write bytecode cache.
- `--self-test`: tests the runner against synthetic vulnerable/hardened text fixtures.
- Normal run returns exit code 2 while any candidate is missing, blocked, or needs review.

## Prepare candidate inputs

1. Export the exact remediation commit's source files through GitHub into a review snapshot.
2. Record repository, source commit, remediation commit, export date, and SHA-256 manifest outside the candidate directory.
3. Copy only source/configuration text files into `targets/HIG-0X/`.
4. Do not copy `.env`, credential files, tokens, media, node_modules, virtualenvs, binaries, archives, or generated output.
5. Run the scanner. Preserve JSON output with commit metadata.
6. A human reviewer inspects each finding and its tests. Missing required markers or pattern hits require triage; patterns can be bypassed or produce false positives.

## Expected outputs

- `FAIL`: a configured forbidden pattern was found.
- `NEEDS_REVIEW`: one or more expected hardening markers were not found.
- `PASS_STATIC_HEURISTIC`: no configured forbidden pattern found and required markers present; manual review is still mandatory.
- `NOT_RUN`: candidate target directory missing.
- `ERROR`: unsafe input tree, symlink, path escape, or read error.
- Release gate stays `BLOCKED` unless all candidate scans return heuristic pass; even then the report says `MANUAL_REVIEW_REQUIRED`.

## What this runner does not prove

It does not prove absence of vulnerabilities, semantic correctness, dependency safety, binary provenance, runtime isolation, network isolation, credential non-disclosure, or exploit resistance. It does not replace SAST, SBOM, dependency scanning, fuzzing, penetration testing, independent Security review, or Standards Owner approval.

## Next stage — separate authorization

Only after all P0 remediation items have source and negative-test evidence, and a reviewer accepts the evidence, request explicit approval for a disposable runtime test. That runtime stage must use synthetic data, no credentials, no provider endpoints, no billing, and no production systems.
