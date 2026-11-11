# GDES-REG-002 — Higgsfield Remediation Checklist v1.0

**Status:** OPEN — remediation not yet verified  
**Applies to:** HIG-01, HIG-02, HIG-03, HIG-04  
**Verification mode:** Static offline checks first; runtime evaluation only after all applicable P0 gates pass  
**Rule:** A code change, author statement, or green heuristic scan alone is not acceptance evidence.

## 1. Workflow and evidence rules

Each finding must have:
1. Remediation commit SHA and changed-file list.
2. Source-level explanation of the control and its trust boundary.
3. Positive test proving permitted behavior remains functional.
4. Negative test proving the attack or unsafe behavior is rejected.
5. Offline runner output tied to exact candidate commit and policy version.
6. Reviewer disposition: ACCEPTED, REJECTED, or NEEDS_REVIEW.

Status vocabulary: `OPEN`, `IN_PROGRESS`, `EVIDENCE_READY`, `PASS_STATIC`, `FAIL`, `NOT_RUN`, `NOT_VERIFIED`. The runner may emit only heuristic static results. A human reviewer must confirm semantic correctness.

## 2. HIG-01 — higgsfield-ai/skills

| Finding | Priority | Remediation checklist | Acceptance evidence / negative tests |
|---|---|---|---|
| HIG-01-F01 mutable curl-to-shell installer | P0 | [ ] Remove pipe-to-shell bootstrap. [ ] Pin installer to immutable commit/release. [ ] Verify detached signature or independently pinned digest before execution. [ ] Record provenance and expected digest. | [ ] Mutable branch/tag rejected. [ ] Digest/signature mismatch rejected. [ ] Valid pinned installer accepted without executing it. |
| HIG-01-F02 broad Bash authority | P0 | [ ] Remove blanket Bash permission where possible. [ ] Replace with narrowly scoped command allowlist/approval. [ ] Require isolated workspace, no secret mount, read-only source by default. [ ] Document agent-host enforcement. | [ ] Unapproved shell command denied. [ ] Write outside workspace denied. [ ] Attempt to read host credentials denied. [ ] Prompt-injection fixture cannot bypass approval. |
| HIG-01-F03 provider/network side effects | P0 | [ ] Make network egress deny-by-default. [ ] Add explicit provider/cost/data confirmation gates. [ ] Ensure no media auto-upload without user consent. [ ] Disable generation/training/deploy/publish in evaluation mode. | [ ] Offline run succeeds without DNS/network. [ ] Provider calls blocked. [ ] No billing/generation/deployment side effect. [ ] Upload requires explicit approval. |
| HIG-01-F04 DNS rebinding / TOCTOU | P1 | [ ] Bind validated DNS result to actual connection or use hardened transport. [ ] Revalidate every redirect and connection destination. [ ] Reject loopback, private, link-local, multicast, reserved and metadata IP ranges for IPv4/IPv6. | [ ] Rebinding fixture (public at validation, private at connect) rejected. [ ] Redirect to private IP rejected. [ ] IPv4 and IPv6 private-address cases rejected. |
| HIG-01-F05 manual-only evals | P1 | [ ] Add deterministic offline eval runner. [ ] Use synthetic fixtures and mocked provider responses. [ ] Mark provider-dependent scenarios as gated. | [ ] Same fixture produces reproducible result. [ ] Paid/provider scenario cannot run in offline profile. |
| HIG-01-F06 third-party Meshy API path | P1 | [ ] Disable third-party path in baseline. [ ] Add explicit provider consent, egress allowlist, secret manager, data retention and cost controls. | [ ] Missing consent blocks call. [ ] Secret absent from logs/prompts. [ ] Unapproved host blocked. |
| HIG-01-F07 SVG validation hardening | P1 | [ ] Use hardened XML parser with DTD/external entities disabled. [ ] Reject active content and external references after namespace-aware parsing. [ ] Add size, depth, node and processing limits. | [ ] XXE/DTD, entity expansion, script, foreignObject, event handler, CSS URL, namespace mutation and oversized fixtures rejected. |
| HIG-01-F08 skill-count docs mismatch | P2 | [ ] Align README/install docs and generated inventory. [ ] Add consistency test. | [ ] Inventory test confirms the same skill count in all maintained docs. |

## 3. HIG-02 — higgsfield-ai/cli

| Finding | Priority | Remediation checklist | Acceptance evidence / negative tests |
|---|---|---|---|
| HIG-02-F01 privileged/system-wide installer | P0 | [ ] Default to user-owned prefix. [ ] Remove implicit sudo escalation. [ ] Validate target path and ownership. [ ] Provide explicit opt-in for system install outside evaluation. | [ ] Unwritable target fails safely without sudo. [ ] Path traversal/symlink target rejected. [ ] User prefix install plan remains within user home. |
| HIG-02-F02 mutable latest release/checksum trust | P0 | [ ] Require pinned version/tag in governed installation. [ ] Verify signed provenance/attestation or independently trusted digest. [ ] Record archive digest, release tag, platform and source commit. | [ ] Latest-only installation rejected in strict mode. [ ] Invalid signature/digest rejected. [ ] Pinned valid release metadata accepted. |
| HIG-02-F03 binary/auth/network internals unverified | P0 | [ ] Supply complete source at pinned commit and matching release provenance. [ ] Review token storage, permissions, rotation, redaction, TLS, redirects, uploads, process execution and update path. [ ] Generate SBOM and dependency scan. | [ ] Token file permission negative test. [ ] Token never appears in logs/errors. [ ] HTTP downgrade/invalid TLS/unsafe redirect rejected. [ ] Upload path traversal and symlink tests rejected. |

## 4. HIG-03 — higgsfield-ai/higgsfield-video-engineer

| Finding | Priority | Remediation checklist | Acceptance evidence / negative tests |
|---|---|---|---|
| HIG-03-F01 root SSH / remote command path | P0 | [ ] Exclude Runpod/remote pod tools from offline profile. [ ] Remove root SSH; use non-root ephemeral identity if separately approved. [ ] Constrain commands and upload manifest. [ ] Add teardown and secret-scrub evidence. | [ ] Remote command invocation blocked in offline mode. [ ] Root SSH rejected. [ ] Hidden/credential/symlink files cannot be uploaded. |
| HIG-03-F02 Chrome --no-sandbox remote probe | P0 | [ ] Remove no-sandbox flag. [ ] Run browser as unprivileged user in disposable sandbox. [ ] Restrict renderer network and filesystem access. | [ ] Launch policy rejects no-sandbox. [ ] Browser cannot read host secrets or write outside workspace. |
| HIG-03-F03 unsafe WebGPU flags/watchdog disable | P1 | [ ] Remove unsafe API overrides and watchdog disable from default profile. [ ] Keep sandbox enabled. [ ] Add resource/time limits and trusted scene schema. | [ ] Unsafe flags absent in default launch. [ ] Malformed/oversized scene rejected. [ ] Timeout and memory limit terminate safely. |
| HIG-03-F04 setup network dependency retrieval | P1 | [ ] Support verified pre-populated cache/offline mirror. [ ] Verify lockfile and package integrity. [ ] Keep install scripts disabled unless independently justified. | [ ] Offline setup with approved cache passes. [ ] Missing cache fails closed without registry request. [ ] Lockfile/integrity mismatch rejected. |

## 5. HIG-04 — higgsfield-ai/app-templates

| Finding | Priority | Remediation checklist | Acceptance evidence / negative tests |
|---|---|---|---|
| HIG-04-F01 raw request-body logging | P0 | [ ] Remove body/prompt logging. [ ] Replace with allowlisted operation metadata and sanitized error code. [ ] Add redaction regression tests. | [ ] Synthetic canary prompt, token, URL and filename absent from logs. [ ] Errors do not serialize raw request objects. |
| HIG-04-F02 30-day API-key cookie | P0 | [ ] Replace long-lived raw API-key cookie with server-side encrypted storage or short-lived opaque session. [ ] Enforce Secure on HTTPS. [ ] Define rotation, revocation, CSRF and logout semantics. | [ ] Cookie contains no raw API key. [ ] Expired/revoked credential rejected. [ ] Secure/SameSite/HttpOnly policy verified. |
| HIG-04-F03 raw response payload logging | P0 | [ ] Remove full response payload logging. [ ] Redact media URLs, provider metadata and error bodies. | [ ] Canary response values absent from logs. [ ] Error-path logging is allowlisted. |
| HIG-04-F04 upload URL host trust | P0 | [ ] Enforce explicit HTTPS host allowlist for upload and public URLs. [ ] Restrict allowed headers. [ ] Ensure platform credentials never reach storage host. [ ] Constrain redirects. | [ ] Arbitrary HTTPS host rejected. [ ] Userinfo, non-HTTPS, credential headers and redirect escape rejected. [ ] Approved host and MIME accepted. |
| HIG-04-F05 missing Origin accepted | P1 | [ ] Require valid Origin for browser-originated upload requests or implement a robust CSRF token design. [ ] Define trusted reverse-proxy origin handling. | [ ] Missing, null, malformed and cross-origin Origin rejected. [ ] Valid same-origin request accepted. |

## 6. Cross-candidate release gates

- [ ] Exact upstream candidate commit and remediation commit pinned.
- [ ] No secrets, production/customer data, or real media in fixtures.
- [ ] No outbound network, DNS, provider endpoint, or cloud credentials in offline test profile.
- [ ] No package installation during offline validation.
- [ ] SBOM, license inventory, vulnerability report and provenance supplied separately.
- [ ] Offline runner self-tests pass.
- [ ] Candidate negative tests pass.
- [ ] Reviewer manually validates semantic correctness and false-negative risk.
- [ ] Separate approval authorizes a later runtime evaluation.
- [ ] Runtime evaluation remains disposable, synthetic-data-only and cost-free.

## 7. Decision rule

A candidate is **NOT ELIGIBLE** for runtime evaluation while any applicable P0 finding is OPEN, FAIL, NOT_RUN or NOT_VERIFIED. P1 findings must have an approved risk disposition before runtime evaluation. The offline runner is a screening control, not a substitute for code review, SAST, dependency analysis, penetration testing or independent security review.
