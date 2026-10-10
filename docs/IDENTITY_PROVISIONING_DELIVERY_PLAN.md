# Identity Provisioning Delivery Plan

## Scope

Coordinate the next security milestone for the Enterprise Export Platform USA across product, API, automation, and portfolio evidence. This is a delivery plan, not a claim that onboarding or production deployment is complete.

## Current implementation evidence

- OIDC access-token signature and claim validation has automated tests.
- API principal resolution uses the verified issuer/subject pair and active tenant membership.
- Tenant-scoped permission checks and transactional order lifecycle transitions are implemented with audit fields and separation-of-duties checks.
- Permission/role templates are seeded, but no customer role assignments are granted by the seed migration.
- A customer identity onboarding flow, administrative role-grant workflow, provider-specific staging configuration, and production deployment remain outstanding.

## Delivery sequence

1. Policy and threat model — define tenant admin capabilities, role-grant permissions, separation-of-duties policy, audit retention, and emergency access.
2. Schema — add reviewed audit records for identity/membership/role changes, grant reason and request idempotency, with tenant-safe foreign keys and transactional writes.
3. Service layer — implement identity reconciliation, invitation/activation, role grants and revocation in a service that cannot bypass the authorization principal.
4. HTTP boundary — expose only explicit admin routes protected by OIDC and dedicated tenant-scoped permissions; do not accept actor IDs from request bodies.
5. Integration tests — cover unauthorized grantors, self-grants, duplicate retries, suspended/revoked membership, cross-tenant access, rollback, and audit integrity.
6. Operational bootstrap — document a one-time, out-of-band first-admin procedure with two-person review and no default production credentials.
7. Staging — select an identity provider, configure issuer/audience/secrets through environment management, test with real provider-issued tokens, and run security review.
8. Release — require CI green, migration rehearsal/rollback plan, approved deployment, smoke tests, and evidence update.

## Definition of done

- Every identity and role mutation is authorized, tenant-scoped, transactional, idempotent where appropriate, and auditable.
- No user can grant themselves privileges or alter system-managed permissions.
- Negative authorization tests pass in PostgreSQL-backed CI.
- Real-provider staging evidence is recorded without exposing tokens or secrets.
- Portfolio claims distinguish implemented code, automated test evidence, staging evidence, and production status.
- No legal/export compliance certification is claimed without separate qualified review.

## Repository coordination

- enterprise-export-platform-usa: implementation, database migrations, API contract, and integration tests.
- business-automation-system: release orchestration, approval gates, evidence capture, and cross-repository status.
- Full-stack-product-development: architecture decisions, case-study evidence, delivery plan, and public-facing portfolio narrative.

## Status labels

Use Implemented only for merged code; CI verified only for observed passing workflow runs; Staging verified only after real-provider staging tests; and Production deployed only after an approved deployment and post-deploy verification.
