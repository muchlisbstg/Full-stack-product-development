# GDES Cybersecurity Standards Owner Decision Memo v0.2

**Status:** DRAFT — FOR STANDARDS OWNER DECISION — NOT APPROVED  
**Date:** 2026-11-11  
**Repository / branch:** `muchlisbstg/Full-stack-product-development` / `gdes/ai-governance-v1-pilot`

## 1. Evidence baseline

Source catalogs:
- ASVS 5.0.0 blob `8e1f34ae3f80f8121f29de7fc1b6d33253d0d646` — 345 requirements.
- TCASVS 5.0.0 blob `8410732fab232000050ee2982945eeb91b169bf6` — 132 requirements.
- SAMM 2.2.0 blob `64f452ba0c5c6790363fe1813ed5b16e276edc0e` — 90 activities.

Row-level crosswalks:
- `docs/registers/data/GDES_ASVS_SEMANTIC_CROSSWALK_v0.1.csv`
- `docs/registers/data/GDES_TCASVS_SEMANTIC_CROSSWALK_v0.1.csv`
- `docs/registers/data/GDES_SAMM_SEMANTIC_CROSSWALK_v0.1.csv`

| Framework | Source rows | Crosswalk rows | Multi-control proposals | GAP / needs owner disposition |
|---|---:|---:|---:|---:|
| ASVS | 345 | 345 | 112 | 18 |
| TCASVS | 132 | 132 | 58 | 25 |
| SAMM | 90 | 90 | 65 | 2 |
| **Total** | **567** | **567** | **235** | **45** |

This is complete row-inventory coverage in a machine-assisted first-pass proposal. It is **not** 567 human-approved semantic mappings. Each row includes source ID, proposed primary/supporting controls, disposition, rationale and source excerpt. Chapter fallback remains provisional. No compliance or implementation status is inferred.

## 2. Reconciliation policy proposed for approval

1. One primary control is required where a source outcome is directly covered. If no defensible owner exists, use GAP or NEEDS DOMAIN CONTEXT.
2. Supporting links are allowed only where the source outcome materially spans multiple controls. Each link needs a row-specific rationale and applicability condition where relevant.
3. Keyword and chapter rules are discovery aids only. Source requirement/activity intent and acceptance outcome determine mapping.
4. Do not attach SEC-010 because an ASVS sentence begins with “Verify that”. SEC-010 owns actual security testing, assessment, verification, assurance and evidence activities.
5. Chapter/practice membership cannot automatically transfer all candidate controls to every source row.
6. Preserve source IDs, versions, source text and catalog blob hashes.
7. Keep gaps visible; a proposed future control ID does not itself close a gap.

## 3. Proposed GDES-SEC-012

**Name:** GDES-SEC-012 — Secure Coding and Runtime Exploit Mitigation.

**Scope:** memory-safe programming; memory/resource lifecycle; safe string, buffer, pointer and integer operations; prevention of use-after-free, dangling pointers and memory corruption; language/runtime/compiler hardening; ASLR, DEP/NX, CFI and platform-specific runtime exploit mitigation.

**Boundaries:**
- SEC-004 remains input/output safety, validation, sanitization and injection prevention; it must not absorb all memory-safety requirements.
- SEC-007 remains secret/key/configuration protection. Secret zeroization may require SEC-012 plus SEC-007 when both memory lifecycle and key custody are in scope.
- SEC-010 remains testing/assessment/evidence, not the primary owner of the safeguard being tested.
- SEC-011 remains resilience, availability, incident response and recovery.
- SEC-008 remains dependency/build/artifact provenance, not runtime exploit mitigation merely because a compiler/build tool delivers it.

**Recommendation:** APPROVE IN PRINCIPLE SEC-012, subject to final wording and owner confirmation. Until explicit approval, SEC-012 is not canonical and may appear only as a proposed gap candidate. If rejected, preserve affected rows as GAP; do not force-fit them to SEC-004 or SEC-010.

## 4. Other control-boundary clarifications

| Control | Proposed boundary |
|---|---|
| SEC-001 | Governance, risk, threat modeling, security requirements and program direction; not a catch-all for process activities. |
| SEC-002 | Identity, authentication, credentials, sessions and identity-token lifecycle. |
| SEC-003 | Authorization, access decisions, privilege boundaries, roles and separation of duties. |
| SEC-004 | Input/output safety, validation, parsing, sanitization and injection prevention. |
| SEC-005 | API, network, transport, service/IPC boundaries, network trust and interface abuse/rate limiting. |
| SEC-006 | Data protection, privacy, classification, encryption and data lifecycle. |
| SEC-007 | Secrets, cryptographic key custody, secure configuration and protected storage. |
| SEC-008 | Dependencies, third parties, suppliers, build provenance, packages, SBOM and signed artifact/update trust. |
| SEC-009 | Logging, monitoring, audit trails, alerting, errors and security telemetry. |
| SEC-010 | Security testing, assessment, verification, assurance and evidence. |
| SEC-011 | Incident response, resilience, availability, backup/recovery and continuity. |
| DB-001 | Database schema and relational integrity constraints. |
| DB-002 | Tenant isolation and row-level security. |
| DB-003 | Transaction atomicity, concurrency, idempotency and temporal consistency. |
| DB-004 | Database identities, roles, credentials, privileges and database audit. |
| DB-005 | Database migrations, backup/restore, recovery and cross-engine parity. |

Rate limiting/anti-automation should be primarily SEC-005, with SEC-011 supporting where resource exhaustion or availability is an explicit outcome. Do not create another control unless later source-level analysis demonstrates a material uncovered domain.

## 5. Consolidated issue classes

1. **Memory safety / exploit mitigation:** ASVS V1.4.1–V1.4.3 and V17.3.2; TCASVS V2.2.x, V3.4.2, V4.2.x and V4.6.8. SEC-012 is the candidate owner; affected rows remain GAP pending decision.
2. **Business logic / domain context:** ASVS V2.x and V15.x, plus TCASVS rows in V1/V2/V4/V5. These need source-level interpretation; chapter membership is insufficient.
3. **Mobile platform/runtime safeguards:** TCASVS memory, platform, sandbox, IPC and application lifecycle requirements need architecture-specific interpretation before primary ownership is set.
4. **Security program metrics and defect management:** SAMM must distinguish governance (SEC-001), assurance (SEC-010), and operational monitoring (SEC-009); avoid assigning all three indiscriminately.
5. **Database safeguards:** map DB-001–DB-005 only where the source actually concerns database structure, tenant isolation, transactions, database access or database recovery.

## 6. Standards Owner decision record

Decision options: APPROVE / APPROVE WITH REVISION / REJECT / DEFER.

| Decision ID | Decision requested | Recommendation |
|---|---|---|
| SO-CYB-01 | One primary plus justified supporting/conditional links | APPROVE |
| SO-CYB-02 | Chapter/practice fallback is not approval evidence | APPROVE |
| SO-CYB-03 | SEC-010 is not mapped from generic “verify” wording | APPROVE |
| SO-CYB-04 | Add SEC-012 Secure Coding and Runtime Exploit Mitigation | APPROVE IN PRINCIPLE; finalize wording |
| SO-CYB-05 | SEC-005 owns rate limiting/interface abuse; SEC-011 supports availability | APPROVE |
| SO-CYB-06 | Keep all 45 GAP/context rows open pending owner disposition | APPROVE |
| SO-CYB-07 | Effective date, rollout and compliance claims | DEFER |

No response is approval. The dictionary, crosswalks and GDES remain DRAFT until an explicit Standards Owner decision is recorded. The 45 GAP/context rows remain unresolved even if the mapping policy is approved.

## 7. Limitations and next work

- The crosswalks are a complete machine-assisted first-pass row inventory, not completed human semantic adjudication.
- Primary/supporting assignments require row-by-row validation against full source text and architecture applicability before finalization.
- Candidate overlaps are not automatically conflicts. Conflicts exist where ownership is incompatible or a source has no clear primary owner; the 45 GAP/context rows are unresolved.
- No runtime tests, implementation verification, legal interpretation, independent review or compliance certification was performed.
- Procurement and independent review are outside this work package.
