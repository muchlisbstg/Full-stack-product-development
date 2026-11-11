# GDES Cybersecurity Semantic Reconciliation Notes v0.1
## CYB-04 / CYB-05 / CYB-06 — Preliminary Standards Owner Working Paper

| Metadata | Value |
|---|---|
| Artifact ID | GDES-SEC-SEM-001 |
| Version | 0.1 |
| Status | **WORKING PAPER — PRELIMINARY TRIAGE — NOT APPROVED** |
| Repository / branch | muchlisbstg/Full-stack-product-development / gdes/ai-governance-v1-pilot |
| Source baseline | Generated catalogs at commit 1e002b8f4e3386d5fb9daf8ba6e6c155b78091fd |
| Prepared | 2026-11-11 |

> This paper records an initial semantic quality-control sample. It does not replace row-by-row reconciliation of all 345 ASVS, 132 TCASVS and 90 SAMM activity rows. It is not an independent review, legal opinion, implementation test, or approval of GDES.

## 1. Reconciliation rules

1. A candidate link is accepted only when the source requirement/activity intent materially matches the canonical control's scope and required outcome.
2. Keep primary control mapping distinct from supporting/conditional mapping. Avoid mapping an entire chapter to every control.
3. Where the source requirement crosses security domains, use a justified many-to-many mapping and state the reason.
4. Use `PARTIAL`, `UNMAPPED`, `NOT APPLICABLE`, or `NEEDS DOMAIN CONTEXT` where a canonical control does not fully express the source intent.
5. Preserve source IDs and exact source text. Do not rewrite upstream requirements.
6. These are proposed semantic dispositions for Standards Owner consideration, not approved mappings.

## 2. TCASVS v5.0.0 initial semantic triage

Source catalog: `GDES_TCASVS_REQUIREMENT_CATALOG_v5.0.0.csv`, blob `8410732fab232000050ee2982945eeb91b169bf6`.

| Source ID | Existing candidate | Proposed semantic disposition | Rationale / action |
|---|---|---|---|
| V1.1.1 | SEC-001, SEC-005 | RETAIN: SEC-001 primary; SEC-005 supporting | Threat model spans client/server/network attack surfaces; SEC-005 is relevant to network boundary coverage. |
| V1.1.3 | SEC-001, SEC-008 | REVISE: SEC-001 primary; SEC-005 supporting; SEC-008 conditional | Cloud services, OIDC, storage and client/server channels are integration/network surfaces. SEC-008 applies only where dependency provenance or supply-chain risk is in scope. |
| V1.1.5 | SEC-001, SEC-003 | RETAIN | Trust boundaries and privilege-separated processes require threat modelling plus authorization/privilege controls. |
| V1.1.6 | SEC-006 | EXPAND: SEC-006 primary; SEC-005 conditional | Sensitive-data classification/protection is SEC-006; add SEC-005 where the boundary crossing is a network or service interface. |
| V1.2.4 | SEC-001, SEC-010 | RETAIN | Threat-to-test traceability spans threat modelling and security verification/evidence. |
| V1.3.1 | SEC-003 | RETAIN | Privilege separation and least privilege are direct authorization/privilege concerns. |
| V1.3.2 | SEC-001, SEC-010, SEC-011 | REVISE: SEC-001 primary; SEC-003 and SEC-007 supporting | Secure defaults and least privilege belong to authorization/configuration; SEC-010 applies only to verification evidence. SEC-011 is not a general design-principles bucket. |
| V1.3.3 | SEC-001, SEC-010, SEC-011 | REVISE: SEC-003 primary; SEC-004 and SEC-008 supporting | Plugin isolation concerns permission boundaries, unsafe scripting/input surfaces, and third-party plugin trust. SEC-010 is verification evidence, not the primary control. |
| V1.3.4 | SEC-010, SEC-011 | EXPAND: SEC-008 primary; SEC-010 and SEC-011 supporting | Update trust chain and artifact integrity are supply-chain controls; signature validation is verified under SEC-010; safe rollback/failure recovery supports SEC-011. |
| V1.3.5 | SEC-001, SEC-010, SEC-011 | NEEDS DOMAIN CONTEXT | Adversarial local environment is threat-model dependent. SEC-003/004/008/010 may apply depending on the specific local attack surface; do not retain a blanket three-control mapping. |
| V1.4.1 | SEC-005 | EXPAND: SEC-001 primary; SEC-004 and SEC-005 supporting | Attack-surface inventory is threat modelling; local input/IPC surfaces implicate SEC-004, network interfaces SEC-005. |
| V1.4.2 | SEC-003, SEC-004 | RETAIN | Caller privilege/access expectations and input validation are distinct but directly relevant controls. |
| V1.4.3 | SEC-001, SEC-003, SEC-004 | RETAIN WITH CONDITIONAL SCOPE | Threat inventory is SEC-001; local privilege escalation is SEC-003; IPC/input abuse is SEC-004. Binary tampering may require SEC-010 test evidence. |
| V1.4.4 | SEC-001 | EXPAND: SEC-001 primary; SEC-008 supporting where dependency updates change attack surface | Threat-model change control is primary; dependency update risk belongs to SEC-008. |
| V2.1.2 | SEC-011 | EXPAND: SEC-011 primary; DB-005 where persistent database restore is included | Service recovery is SEC-011; database backup/restore and engine-specific evidence are DB-005. |
| V2.1.4 | SEC-008, SEC-010 | RETAIN | Trusted repositories and artifact integrity are SEC-008; verification evidence may support SEC-010. |
| V4.6.1 | SEC-004, SEC-008, SEC-010 | REVISE: SEC-009 primary; SEC-011 supporting | Safe error handling and information disclosure are SEC-009; fail-safe recovery is SEC-011. Existing candidate set misses the direct control. |
| V5.1.1 | SEC-006 | EXPAND: SEC-006 primary; SEC-007 supporting | Cryptographic key lifecycle is data protection plus secure secret/key storage, rotation and configuration. |
| V5.1.2 | SEC-007 | EXPAND: SEC-007 primary; SEC-006 supporting | Inventory of keys/certificates embedded in binary/configuration is secrets/configuration with cryptographic protection context. |
| V5.5.1 | SEC-002, SEC-006 | RETAIN CONDITIONALLY | SEC-006 is primary for cryptographic key separation; SEC-002 only when the keys are specifically identity/session/authentication material. |
| V5.6.2 | SEC-006 | EXPAND: SEC-005 primary; SEC-006 supporting | Certificate-chain, revocation and hostname validation are transport/network trust controls with cryptographic protection context. |
| V5.6.4 | SEC-006 | REVISE: SEC-008 primary; SEC-010 supporting; SEC-007 conditional | Code signing/update integrity is supply-chain security; signature validation evidence is SEC-010; signing key custody/configuration is SEC-007. |
| V6.3.1 | SEC-005, SEC-006 | EXPAND: SEC-005 primary; SEC-006 and SEC-002 conditional | Transport protection is SEC-005; sensitive-data protection SEC-006; SEC-002 applies to identity/session tokens and credentials. |
| V6.4.1 | SEC-002 | EXPAND: SEC-002 primary; SEC-003 supporting | IPC caller authentication is SEC-002; authorization of permitted commands/resources is SEC-003. |
| V6.4.2 | SEC-003 | EXPAND: SEC-005 primary; SEC-003 and SEC-006 conditional | IPC channel integrity is an interface/channel security concern; SEC-003 applies to caller privilege and SEC-006 to sensitive payload protection. |

## 3. SAMM v2.2.0 initial semantic triage

Source catalog: `GDES_SAMM_ACTIVITY_CATALOG_v2.2.0.csv`, blob `64f452ba0c5c6790363fe1813ed5b16e276edc0e`.

| Activity | Existing candidate | Proposed semantic disposition | Rationale / action |
|---|---|---|---|
| D-SA-1-A — Adhere to basic security principles | SEC-003 | EXPAND: SEC-001 primary; SEC-003, SEC-007 and SEC-011 supporting as applicable | The activity is organization-wide secure design principles, not only least privilege. Secure defaults and fail-secure are distinct supporting themes. |
| D-SA-1-B — Identify tools and technologies | SEC-001, SEC-003, SEC-004, SEC-005, SEC-006 | REVISE: SEC-001 primary; SEC-008 and SEC-005 supporting | Technology risk identification is threat/risk assessment; dependency provenance is SEC-008; integration/network exposure is SEC-005. Do not map every generic technology evaluation to all controls. |

## 4. Initial findings from semantic triage

1. TCASVS chapter fallback creates over-broad associations in some rows. Examples V1.3.2, V1.3.3 and V4.6.1 show why chapter membership cannot substitute for requirement meaning.
2. Some keyword candidates omit a direct control or assign a broad control that is not the primary outcome. Examples V4.6.1, V5.6.2 and V5.6.4.
3. Some requirements need conditional mapping based on architecture or data type, rather than unconditional one-to-many links. Examples V1.1.6, V5.5.1 and V6.3.1.
4. Database recovery requirements need explicit GDES-DB mapping where database-engine backup/restore is in scope; SEC-011 alone is insufficient for DB-005 evidence.
5. SAMM practice/activity fallback must not map every activity to every control in the practice. Activity description and expected outcome should drive mapping.
6. No source row is marked approved or closed by this paper. The full catalogs remain candidate-only until every row has an explicit disposition and rationale.

## 5. Remaining reconciliation scope

| Workstream | Inventory | Current paper coverage | Remaining |
|---|---:|---:|---:|
| ASVS v5.0.0 | 345 | 0 row dispositions in this paper | 345 |
| TCASVS v5.0.0 | 132 | 23 initial triage rows | 109 |
| SAMM v2.2.0 | 90 | 2 initial triage rows | 88 |
| MASWE / MASTG | 78 stable weaknesses / 292 test paths | Existing source-relation exceptions retained separately | Per-weakness applicability and test selection still open |

## 6. Decision boundary

- This working paper may inform a Standards Owner decision on mapping methodology and canonical control semantics.
- The Standards Owner may approve dictionary structure, many-to-many traceability and source-qualified legacy alias policy as governance decisions, while explicitly deferring effective date and rollout.
- No approval is inferred from this working paper, catalog generation, issue creation or authorship.
- The canonical dictionary and all semantic dispositions remain **DRAFT — NOT APPROVED** until the Standards Owner records an explicit decision.
- Procurement, reviewer appointment, independent review and runtime testing are outside the scope of this paper.
