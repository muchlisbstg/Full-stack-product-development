# Three-Repository Portfolio Map

This portfolio uses three repositories with distinct responsibilities. Treat implementation status as evidence-based: a document or proposal is not proof that a feature is running in production.

## Repository boundaries

| Repository | Responsibility | Evidence to inspect | Current boundary |
| --- | --- | --- | --- |
| [Full-stack Product Development](https://github.com/muchlisbstg/Full-stack-product-development) | Portfolio, delivery approach, product engineering examples | [Portfolio evidence map](PORTFOLIO_EVIDENCE_MAP.md), [case-study switchboard](CASE_STUDY_SWITCHBOARD.md) | Present only features backed by repository files, tests, or a clearly labeled demo. |
| [Business Automation System](https://github.com/muchlisbstg/business-automation-system) | Workflow contracts, n8n orchestration patterns, CI/CD and operational safety | [Product roadmap](https://github.com/muchlisbstg/business-automation-system/blob/main/docs/PRODUCT_ROADMAP.md), [release gates](https://github.com/muchlisbstg/business-automation-system/blob/main/docs/RELEASE_GATES.md), [operations runbook](https://github.com/muchlisbstg/business-automation-system/blob/main/docs/OPERATIONS_RUNBOOK.md), [multi-repository release coordination](https://github.com/muchlisbstg/business-automation-system/blob/main/docs/MULTI_REPOSITORY_RELEASE_COORDINATION.md) | Workflow contract proposals must not be described as deployed automations. |
| [Enterprise Export Platform USA](https://github.com/muchlisbstg/enterprise-export-platform-usa) | Manufacturing/export order API and tenant-aware data foundation | [Architecture](https://github.com/muchlisbstg/enterprise-export-platform-usa/blob/main/docs/ARCHITECTURE.md), [order lifecycle policy](https://github.com/muchlisbstg/enterprise-export-platform-usa/blob/main/docs/ORDER_LIFECYCLE_AND_AUTHORIZATION.md), [identity foundation](https://github.com/muchlisbstg/enterprise-export-platform-usa/blob/main/docs/IDENTITY_AND_AUTHORIZATION_FOUNDATION.md), [OIDC ADR](https://github.com/muchlisbstg/enterprise-export-platform-usa/blob/main/docs/ADR-004-OIDC-AUTHORIZATION-BOUNDARY.md), [OIDC implementation PR](https://github.com/muchlisbstg/enterprise-export-platform-usa/pull/12), [authorization catalog PR](https://github.com/muchlisbstg/enterprise-export-platform-usa/pull/13), [transactional order transitions PR](https://github.com/muchlisbstg/enterprise-export-platform-usa/pull/14) | OIDC JWT verification, membership-derived tenant scope, permission checks, and transactional lifecycle routes are merged; provider configuration, identity provisioning, role administration, deployment, and independent security review remain outstanding. |

## Shared engineering standards

1. **Evidence first.** Every portfolio claim links to code, tests, a workflow run, or a demo that can actually be inspected.
2. **Explicit status.** Label each capability as implemented, in progress, planned, or unverified.
3. **Separate proposal from runtime.** A JSON Schema, architecture document, workflow contract, or migration is not proof of a deployed service.
4. **Security claims stay narrow.** Tests of tenant-scoped queries do not establish complete multi-tenant security. An identity schema does not authenticate users.
5. **No unsupported compliance claims.** Do not claim export-control compliance, legal compliance, certification, or Shariah certification without a verified scope and supporting evidence.
6. **Reproducibility.** Link to the exact commit or CI run when describing a tested result; do not imply every branch or release has passed.
7. **Release discipline.** Use pull requests, passing required checks, reviewed migrations, and human approval for production or destructive operations.

## Cross-repository change checklist

- [ ] Identify which repository owns the change; avoid duplicating the same implementation in multiple repos.
- [ ] Update the owner repository's tests and documentation in the same change.
- [ ] If a downstream repository depends on the change, record the dependency and minimum required commit.
- [ ] Verify CI on the proposed commit before merging.
- [ ] Update portfolio evidence only after the implementation or test evidence exists.
- [ ] Record any limitations that remain after merge.

## Current project status snapshot

- Portfolio and cross-repository evidence map: documentation merged; this map is not a live CI dashboard.
- Business automation coordination: release process and human-approval expectations documented; no claim that cross-repository automation is deployed.
- Export platform: OIDC verifier, active-membership principal resolution, seeded system role templates, and transactional order transition endpoints are merged. PR #14's PostgreSQL integration test covers submit/replay, self-approval denial, independent approval, and audit fields. A signed-JWT positive/negative test suite was merged in [PR #15](https://github.com/muchlisbstg/enterprise-export-platform-usa/pull/15) after CI passed. No deployment or export-law compliance is claimed.

Check each repository's Actions and pull requests for current run status before reporting a release as green.
