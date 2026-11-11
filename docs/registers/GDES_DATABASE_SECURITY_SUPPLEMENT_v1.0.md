# GDES Database Security Supplement v1.0
## Draft Control Standard and Independent Database Review Scope

| Metadata | Value |
|---|---|
| Artifact ID | GDES-DB-SUP-001 |
| Version | 1.0 |
| Status | **DRAFT — NOT APPROVED — NOT TESTED** |
| Parent | GDES-SEC-DICT-001 and GDES-SEC-ACCEPTANCE-MATRIX-001 |
| Target engines | PostgreSQL; SQLite where deployed; other engines by explicit addendum |
| Independent reviewer | Not appointed |

## 1. Objective and authority boundary

This supplement defines database-specific controls that cannot be proven by application-only security checks or generic framework mapping. It covers schema integrity, tenant isolation, database privileges, transaction/concurrency behavior, migrations, recovery and cross-engine parity.

This is a design/review specification. It does not authorize database DDL, migrations, seed/backfill, staging mutation, production operations, credentials access or data changes. Such actions require separate explicit authorization.

## 2. Canonical database controls

| ID | Control | Minimum requirement |
|---|---|---|
| GDES-DB-001 | Relational Schema & Integrity | Canonical PK/FK/unique/check/not-null constraints and composite tenant/resource keys where required; prevent orphaned and cross-tenant relations. |
| GDES-DB-002 | Tenant, Row & Resource Isolation | Enforce tenant/resource boundaries at trusted API and database layers; PostgreSQL RLS must be enabled and proven where shared-schema tenancy requires it. |
| GDES-DB-003 | Transaction, Concurrency & Temporal Consistency | Define isolation, transaction boundaries, locking, idempotency, retries, ordering, timestamp semantics and duplicate side-effect prevention. |
| GDES-DB-004 | Database Identity, Privilege & Audit | Dedicated least-privilege service roles, separation of owner/migration/runtime roles, restricted schema/function grants, credential controls and auditability. |
| GDES-DB-005 | Migration, Backup, Restore & Engine Parity | Versioned migration review, backup/restore validation, rollback strategy and explicit SQLite/PostgreSQL behavior reconciliation. |

## 3. PostgreSQL RLS requirements

Where PostgreSQL RLS is part of the tenant isolation design:

1. Enable RLS on every tenant-scoped table.
2. Evaluate FORCE ROW LEVEL SECURITY where table-owner bypass is otherwise possible and compatible with operational design.
3. Use separate runtime roles; runtime role must not own protected tables or hold BYPASSRLS/superuser privileges.
4. Derive tenant context from authenticated server-side identity. Never accept a client-provided tenant ID as authority.
5. Set tenant context transaction-locally where possible; avoid pooled-connection context leakage.
6. Ensure SELECT, INSERT, UPDATE and DELETE policies are explicit and mutually consistent.
7. Verify both USING and WITH CHECK semantics for updates/inserts.
8. Test absent, malformed, stale and forged tenant context.
9. Test table owner, migration role, service role, read-only role and administrative role separately.
10. Test views, SECURITY DEFINER functions, triggers, partitions, background workers and RPC functions for unintended bypass.
11. Confirm connection-pool reuse does not retain previous tenant context.
12. Capture catalog/policy evidence and negative test results.

SQLite does not provide equivalent PostgreSQL RLS semantics. SQLite tests cannot be represented as PostgreSQL RLS proof.

## 4. Tenant and relational integrity requirements

For multi-tenant relations:
- Use composite unique keys and composite foreign keys to bind child rows to the same tenant/enterprise where required.
- Include tenant/enterprise identity in join and lookup predicates, while relying on database constraints/policies for authoritative enforcement.
- Prevent cross-tenant foreign-key references even if the API is bypassed.
- Define ownership for every table, view, materialized view, function and background job.
- Verify nullable relationships and soft-delete semantics do not bypass ownership checks.
- Define unique constraints for tenant-scoped business identifiers.
- Define ON DELETE/ON UPDATE behavior explicitly; avoid cascade deletion that violates legal/audit retention.

Minimum negative cases:
- Insert a child row with a valid parent ID from another tenant.
- Update tenant ID on an existing row to another tenant.
- Select/update/delete a resource using another tenant's key.
- Invoke a privileged function under the runtime role.
- Query a view or RPC that could omit tenant filtering.
- Reuse pooled connection after tenant context changes.

Expected result: database-enforced rejection or zero unauthorized rows, with no partial state change or sensitive disclosure.

## 5. Transaction, concurrency and temporal requirements

Document and test:
- business transaction boundary and atomicity;
- isolation level and anomaly tolerance;
- lock ordering and deadlock handling;
- optimistic/pessimistic concurrency strategy;
- idempotency key scope, expiry and uniqueness;
- duplicate/retry semantics for externally retried requests;
- event/outbox consistency if asynchronous effects are used;
- timestamp source, timezone, precision and ordering;
- effective-time vs recorded-time semantics where legally/business relevant;
- partial failure and compensation behavior.

Required test classes:
1. Two concurrent updates to the same resource.
2. Concurrent stock/quantity reservations at the last available unit.
3. Duplicate payment/settlement callback or webhook.
4. Retry after timeout when commit outcome is unknown.
5. Simultaneous approval/revocation or role change and protected action.
6. Cross-tenant concurrent access using reused pooled connections.
7. Clock skew, timezone boundary and temporal ordering where relevant.

For financial or contract workflows, invariants must preserve ledger truth, obligation/evidence traceability, authorization decisions and exactly-once business effects (or documented idempotent equivalent). No real-money test is authorized by this document.

## 6. Database role and privilege baseline

| Role class | Allowed purpose | Prohibited baseline |
|---|---|---|
| Migration/owner | Controlled schema change under approved process | Runtime customer request handling |
| Application runtime | Required CRUD/function execution only | CREATE/ALTER/DROP, ownership transfer, BYPASSRLS, superuser |
| Read-only/reporting | Approved read scope/views | Write, DDL, cross-tenant broad access |
| Backup/restore | Approved backup/restore operations | General application use |
| Auditor | Read-only catalog/log/evidence scope | Data mutation or privilege escalation |
| Emergency admin | Time-bound break-glass access with logging | Standing daily service identity |

Validate PUBLIC grants, default privileges, schema search_path, SECURITY DEFINER ownership/search_path, extension privileges, replication/log access and credential rotation. Do not place database credentials in mobile/web client bundles.

## 7. SQLite/PostgreSQL parity

Parity is behavioral, not merely matching table names.

Compare:
- tables, columns, types, nullability and defaults;
- PK/FK/unique/check constraints and indexes;
- cascade behavior and deferred constraints;
- transactions, isolation, locking and concurrency;
- JSON, timestamp, collation, case sensitivity and numeric semantics;
- generated IDs and uniqueness;
- RLS/role enforcement (PostgreSQL-specific; no false equivalence claim);
- negative tenant/resource access;
- migration ordering and rollback;
- authorization decisions and error behavior.

Any engine-specific behavior must be recorded as an explicit divergence with owner, risk, compensating control and test. SQLite-only success is not PostgreSQL PASS.

## 8. Migration and recovery governance

Before a migration:
- source and target schema snapshots;
- forward migration and rollback/recovery plan;
- data compatibility and lock/downtime analysis;
- backup verification and restore rehearsal;
- tenant isolation and privilege impact review;
- independent database review for material changes;
- explicit owner authorization.

After an authorized migration:
- verify migration ledger and schema catalog;
- verify constraints and row counts/invariants;
- run target-engine integration and negative-access tests;
- compare expected schema snapshot and actual result;
- preserve logs, SHA, environment, operator and approval.

This supplement does not authorize any migration or database mutation.

## 9. Independent Database Reviewer checklist

- [ ] Canonical entity/table ownership is documented.
- [ ] Tenant-scoped relationships use required composite constraints.
- [ ] PostgreSQL RLS enabled and policies reviewed where applicable.
- [ ] Runtime roles cannot bypass RLS or perform DDL.
- [ ] Pooled-connection tenant context is transaction-safe.
- [ ] SECURITY DEFINER, views, triggers and RPC paths reviewed.
- [ ] Transaction isolation and concurrency invariants are tested.
- [ ] Idempotency and duplicate side-effect handling verified.
- [ ] Temporal consistency and timezone semantics verified.
- [ ] SQLite/PostgreSQL differences and parity are documented.
- [ ] Backup, restore and rollback evidence inspected.
- [ ] Findings have severity, owner, disposition and retest evidence.

**Current status: NOT TESTED; independent Database Reviewer not appointed; no database change authorized.**
