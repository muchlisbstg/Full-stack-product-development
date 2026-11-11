# GDES Operational Security Supplement v1.0
## Draft Operational Control Requirements and Evidence

| Metadata | Value |
|---|---|
| Artifact ID | GDES-OPS-SEC-SUP-001 |
| Version | 1.0 |
| Status | **DRAFT — NOT APPROVED — NOT TESTED** |
| Parent | GDES-SEC-DICT-001 |
| Scope | CI/CD, runtime configuration, monitoring, incident response, backup/recovery and release |
| Independent review | Security review required; operational owner to be assigned |

## 1. Purpose

Define operational controls needed to make application security sustainable after implementation. These requirements supplement GDES-SEC-007–011 and the database controls. They do not imply that hosting, monitoring, backup, runtime, or incident capabilities currently exist.

## 2. Environment and trust-boundary inventory

For each environment record:
- provider/service, account/project reference, region and environment classification;
- status: EXISTING, PLANNED, PLANNED—UNFUNDED, EXPERIMENTAL or RETIRED;
- authoritative responsibility (frontend, API, worker, database, storage, identity);
- data classification and residency considerations;
- network exposure, ingress/egress and identity model;
- secret/configuration boundary and access owners;
- monitoring, logging, backup, restore and rollback capability;
- funding/provisioning state, owner and approval.

A provider listing or deployment target is not proof of an authoritative API runtime. Planned/unfunded infrastructure must not be treated as provisioned or deployable.

## 3. CI/CD and software supply-chain operations

Minimum controls:
1. Protect source branches and require review appropriate to risk.
2. Pin action dependencies and third-party build inputs where feasible.
3. Run secret, dependency, license and static security checks on declared release paths.
4. Generate and retain SBOM or equivalent dependency inventory.
5. Bind artifact digest to source commit SHA and build workflow identity.
6. Protect signing keys and release credentials; never expose them in logs.
7. Separate build, approval and deployment permissions.
8. Require explicit approval for production release and sensitive environment changes.
9. Preserve build logs, scanner output, attestations and exception decisions.
10. Define vulnerability triage SLA by severity and exploitability.

A green workflow alone does not prove runtime security or release approval.

## 4. Secrets and configuration operations

- Store secrets only in approved secret-management facilities or protected environment variables with controlled access.
- Keep credentials out of source, issue comments, artifacts, browser/mobile/desktop bundles and logs.
- Separate development, test, staging and production credentials.
- Use least-privilege credentials and rotate after exposure, staff/role changes or risk events.
- Maintain inventory, owner, purpose, scope, expiry/rotation and revocation process.
- Redact secrets and personal data from diagnostic output.
- Review effective runtime configuration without recording secret values.
- Treat client-side values as public, even if obfuscated or environment-injected at build time.

## 5. Logging, monitoring and alerting

Define:
- security event taxonomy and event ownership;
- identity, action, resource, tenant context (privacy-minimized), result and correlation ID;
- trusted timestamp and clock synchronization;
- access control, integrity protection, retention and deletion;
- alert thresholds and escalation path;
- suppression/maintenance-window governance;
- privacy and data minimization review.

Minimum alert scenarios:
- repeated authentication failure or credential stuffing indicators;
- privilege/role/tenant boundary denial spikes;
- anomalous admin or break-glass activity;
- secret exposure or suspicious secret access;
- repeated SSRF/egress policy denials;
- abnormal data export/access patterns;
- database permission/RLS failures;
- dependency or artifact integrity alert;
- backup failure and restore verification failure.

Never log passwords, bearer tokens, private keys, full payment credentials or unnecessary personal data.

## 6. Vulnerability and incident management

Incident process must define:
1. detection and intake;
2. severity and impact assessment;
3. incident commander and technical/legal/privacy contacts;
4. containment and credential revocation;
5. evidence preservation and chain of custody;
6. stakeholder/customer/regulator communication decisions by qualified owner;
7. eradication and recovery;
8. post-incident review and corrective actions.

Vulnerability records include affected component/version, exploitability, impact, exposure, owner, due date, mitigation, patch/release, retest and closure evidence. A finding cannot be closed solely because a ticket is closed.

## 7. Backup, restore and continuity

For each critical service define:
- recovery time objective (RTO) and recovery point objective (RPO);
- backup frequency, encryption, access and retention;
- geographic/administrative separation where justified;
- backup integrity and restore validation;
- dependency order and recovery runbook;
- rollback and data reconciliation after restore;
- test cadence and evidence retention.

A backup job success message is not restore proof. A restore test must record source backup, target environment, integrity checks, elapsed time, missing data, corrective action and approver.

## 8. Release and change operations

Before release:
- scope and commit SHA frozen;
- artifact digest and provenance verified;
- security findings dispositioned;
- database migration/recovery review completed where relevant;
- monitoring and support owner available;
- rollback/containment plan validated;
- legal/regulatory/Syariah gates completed where relevant;
- authorized human release decision recorded.

Production deployment, staging mutation, migrations, secret changes, access grants and paid infrastructure provisioning require explicit authorization. No approval is inferred from a merge, CI status or AI-generated checklist.

## 9. Operational evidence matrix

| Evidence ID | Control | Required artifact | Status |
|---|---|---|---|
| OPS-EVD-001 | Environment inventory | Environment/service ownership and trust-boundary register | NOT STARTED |
| OPS-EVD-002 | CI/CD provenance | Workflow, SBOM, artifact digest and source SHA linkage | NOT TESTED |
| OPS-EVD-003 | Secrets/configuration | Secret scan, redacted runtime configuration review, rotation process | NOT TESTED |
| OPS-EVD-004 | Monitoring | Sanitized event examples, alert test and escalation record | NOT TESTED |
| OPS-EVD-005 | Incident readiness | Incident runbook, roles and tabletop/exercise evidence | NOT TESTED |
| OPS-EVD-006 | Backup/restore | Backup policy and restore exercise report | NOT TESTED |
| OPS-EVD-007 | Release/rollback | Release authorization, rollback rehearsal and post-release checks | NOT TESTED |

## 10. Operational reviewer checklist

- [ ] Environment inventory is accurate and distinguishes planned from provisioned.
- [ ] Authoritative API/runtime boundary is evidenced.
- [ ] CI/CD permissions and source-to-artifact provenance are verified.
- [ ] Secrets are absent from source, artifacts and logs.
- [ ] Monitoring events are useful, attributable and privacy-aware.
- [ ] Alert ownership and escalation paths are staffed.
- [ ] Vulnerability triage and remediation are tracked.
- [ ] Incident response is exercised.
- [ ] Backup restore is tested, not merely configured.
- [ ] Release and rollback require explicit approval and have evidence.

**Current status: NOT TESTED. No deployment, infrastructure mutation, credential rotation or paid provisioning is authorized by this document.**
