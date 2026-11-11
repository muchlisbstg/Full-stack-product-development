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


## 7. ASVS v5.0.0 — semantic batch A (V1.1–V1.5)

Source catalog blob: `8e1f34ae3f80f8121f29de7fc1b6d33253d0d646`. This batch covers 29 source requirements. Dispositions below are proposed row-level semantic decisions, not approvals.

| ASVS requirement | Proposed disposition | Rationale |
|---|---|---|
| V1.1.1 | RETAIN SEC-004 | Canonical decoding and single-decoding discipline are input normalization/injection prevention. |
| V1.1.2 | RETAIN SEC-004 | Context-aware output encoding/escaping is direct injection prevention. |
| V1.2.1 | RETAIN SEC-004 | Contextual HTML/XML/CSS/header output encoding prevents interpreter context changes. |
| V1.2.2 | EXPAND SEC-004 primary; SEC-005 supporting | URL parameter encoding/protocol allowlisting is input handling plus URL/network boundary protection. |
| V1.2.3 | RETAIN SEC-004 | JavaScript/JSON context encoding is direct injection prevention. |
| V1.2.4 | RETAIN SEC-004; DB-001 conditional | Parameterized database queries prevent injection; DB-001 applies only where schema/relational constraints are separately required, not as a substitute for query parameterization. |
| V1.2.5 | RETAIN SEC-004 | OS command parameterization and contextual escaping are direct injection prevention. |
| V1.2.6 | RETAIN SEC-004 | LDAP query injection prevention is direct input/query safety. |
| V1.2.7 | RETAIN SEC-004 | XPath parameterization/precompiled queries prevent query injection. |
| V1.2.8 | RETAIN SEC-004 | Restricting LaTeX shell escape and command allowlists prevents untrusted input from crossing into command execution. |
| V1.2.9 | RETAIN SEC-004 | Regex metacharacter escaping is context-specific input handling. |
| V1.2.10 | EXPAND SEC-004 primary; SEC-006 supporting | CSV/formula injection is output-context injection; SEC-006 supports protection of exported business data. |
| V1.3.1 | RETAIN SEC-004 | Sanitizing untrusted HTML is direct input/output injection protection. |
| V1.3.2 | EXPAND SEC-004 primary; SEC-008 conditional | Avoiding dynamic execution is injection prevention; SEC-008 applies if unsafe expression engines/libraries are third-party components subject to supply-chain governance. |
| V1.3.3 | RETAIN SEC-004 | Context-specific sanitization and length constraints are input safety. |
| V1.3.4 | RETAIN SEC-004 | Scriptable SVG content requires allowlisted sanitization. |
| V1.3.5 | RETAIN SEC-004 | User-controlled template/scriptable content is an injection surface. |
| V1.3.6 | EXPAND SEC-005 primary; SEC-004 supporting | SSRF is principally a server-side network destination/access boundary; input allowlisting and normalization support the control. |
| V1.3.7 | RETAIN SEC-004 | Untrusted template construction is template injection. |
| V1.3.8 | RETAIN SEC-004 | JNDI query/input sanitization is injection prevention. |
| V1.3.9 | RETAIN SEC-004 | Cache command/data injection is input/query safety. |
| V1.3.10 | RETAIN SEC-004 | Format-string interpretation is injection/input handling. |
| V1.3.11 | RETAIN SEC-004 | SMTP/IMAP header/command injection is input handling at protocol interpreter boundaries. |
| V1.3.12 | EXPAND SEC-004 primary; SEC-011 supporting | ReDoS prevention is safe input/regex construction; SEC-011 is supporting only for availability resilience and recovery expectations. |
| V1.4.1 | GAP — no direct canonical control | Memory-safe string operations and buffer/heap/stack overflow prevention are secure coding/memory safety. SEC-004 is not an adequate semantic substitute. Consider a new canonical control or an explicitly bounded SEC-010 verification relation; do not silently force-fit. |
| V1.4.2 | PARTIAL SEC-004; GAP noted | Integer range/sign validation is input validation, but integer overflow is also a language/runtime memory-safety concern not fully expressed by SEC-004. |
| V1.4.3 | GAP — no direct canonical control | Use-after-free, dangling pointers and resource lifecycle are memory/resource safety. No current SEC/DB definition directly owns this domain. |
| V1.5.1 | RETAIN SEC-004; SEC-005 conditional | XXE parser hardening is unsafe input/deserialization handling; SEC-005 applies where external entity resolution creates outbound network access. |
| V1.5.2 | RETAIN SEC-004 | Allowlisted deserialization types and safe parsing are direct untrusted-input controls. |
| V1.5.3 | EXPAND SEC-004 primary; SEC-005 supporting | Parser differential/normalization issues are input interpretation; SSRF/RFI exploitability can involve network access controls. |

### ASVS batch A findings

- The V1.1–V1.3 candidate SEC-004 mappings are generally semantically sound, but several requirements require supporting SEC-005 or SEC-006 links.
- V1.4 reveals a material canonical dictionary gap: memory safety and resource lifecycle are not explicitly owned by the current 16-control proposal. Do not hide this gap under SEC-004.
- V1.5 parser/deserialization requirements are primarily SEC-004, with network control only where external resolution or remote fetch behavior exists.

## 8. TCASVS v5.0.0 — semantic batch B

Additional row dispositions beyond the initial batch in section 2:

| Source ID | Proposed semantic disposition | Rationale |
|---|---|---|
| V1.1.2 | RETAIN SEC-001 | Data-flow diagrams, threat classification and risk-rated scenarios are threat-model artifacts. |
| V1.1.4 | EXPAND SEC-001 primary; SEC-010 supporting | Versioned threat-model artifacts are governance and traceability; SEC-010 supports review/evidence integrity. |
| V1.2.1 | EXPAND SEC-001 primary; SEC-010 supporting | Threat identification and mitigation planning are SEC-001; automated/manual validation evidence supports SEC-010. |
| V1.2.2 | RETAIN SEC-001 | Periodic and change-triggered threat-model review is threat-model governance. |
| V1.2.3 | EXPAND SEC-001 primary; SEC-010 supporting | Validating documented mitigations and finding undocumented attack surfaces is a threat-model-to-test assurance activity. |
| V2.1.1 | REVISE: SEC-008 primary; SEC-007 and SEC-010 supporting | Build environment integrity and reproducible artifacts involve supply-chain/build provenance; secrets/configuration hardening and verification are supporting. |
| V2.1.3 | REVISE: SEC-007 primary; SEC-008 conditional; SEC-010 supporting | Excluding development configuration/secrets is configuration hardening; dependency/build provenance applies only to build inputs; verification proves the release profile. |
| V2.1.5 | RETAIN SEC-008 | SBOM is direct software component inventory and supply-chain transparency. |
| V2.1.6 | EXPAND SEC-007 primary; SEC-009 supporting | Embedded credentials are secrets/configuration; verbose errors/debug strings are logging/error disclosure. |
| V2.1.7 | EXPAND SEC-008 primary; SEC-007 supporting; SEC-010 verification | Signed binaries/installers are artifact provenance; hardware protection of signing keys is secrets/key custody; validation is verification. |
| V2.1.8 | RETAIN SEC-008; SEC-007 supporting | Dependency confusion controls are supply-chain integrity; registry credentials/configuration are secrets/configuration. |
| V2.2.1 | GAP — memory safety domain; SEC-010 supporting | Compiler exploit mitigations and unsafe-operation build failures are secure build/code-hardening requirements not directly represented by existing SEC-007/008/010 candidates. SEC-010 is evidence, not the primary technical control. |
| V2.2.2 | GAP — memory safety/exploit mitigation; SEC-010 supporting | ASLR/PIE are binary exploit mitigations. Do not map to configuration or supply-chain controls merely due chapter membership. |
| V2.2.3 | GAP — memory safety/exploit mitigation; SEC-010 supporting | DEP/NX is an OS/binary execution-hardening control; current canonical dictionary lacks a direct owner. |
| V2.2.4 | GAP — memory safety/exploit mitigation; SEC-010 supporting | CFI is binary exploit mitigation, not supply-chain governance. |
| V2.2.5 | GAP — memory safety/exploit mitigation; SEC-010 supporting | Hardware exploit mitigations require platform-specific hardening and evidence. |
| V2.2.6 | REVISE: SEC-003 primary; SEC-010 supporting | Runtime weakening of OS security features violates privilege/security enforcement and needs verification evidence. |
| V2.3.1 | EXPAND SEC-008 primary; SEC-010 supporting | Installer integrity validation is artifact trust and verification. |
| V2.3.2 | EXPAND SEC-007 primary; SEC-003 supporting; SEC-010 conditional | Temporary-file permissions are configuration/secret/data exposure hardening and access control; evidence is supporting. |
| V2.3.3 | RETAIN SEC-008; SEC-010 supporting | Update package signature validation establishes artifact provenance/integrity. |
| V2.3.4 | RETAIN SEC-005; SEC-010 supporting | Update download transport and pinning are network controls; verification evidence is secondary. |
| V2.3.5 | EXPAND SEC-008 primary; SEC-003 supporting | DLL search order/sideloading is third-party binary trust and execution boundary/privilege control. |
| V2.3.6 | RETAIN SEC-003; SEC-004 supporting | Elevation minimization is least privilege; untrusted input to elevated children is input validation. |
| V2.4.1 | REVISE SEC-003 primary; SEC-005 supporting | Least privilege and minimal IPC exposure are authorization/privilege and interface boundary controls. |
| V2.4.2 | EXPAND SEC-003 primary; SEC-004 and SEC-011 conditional | Rule of 2 combines privilege, untrusted input and sandbox/availability containment; map only the applicable dimensions. |
| V2.4.3 | EXPAND SEC-003 primary; SEC-007 supporting | Filesystem ACLs are authorization/privilege; secure file/configuration permissions support SEC-007. |
| V2.4.4 | RETAIN SEC-003 | Dedicated least-privilege service identities are authorization/privilege management. |
| V2.4.5 | EXPAND SEC-007 primary; DB-002/DB-004 conditional | Configuration protection is SEC-007; local database tenant isolation or DB role privilege is DB-002/DB-004 only when the local DB stores tenant-separated data or uses distinct DB roles. |
| V2.4.6 | EXPAND SEC-003 primary; SEC-004 and SEC-005 supporting | Sandboxing limits privileges and restricts untrusted input and network capabilities. |
| V2.4.7 | EXPAND SEC-003 primary; SEC-005 supporting | IPC object permissions are access control; IPC exposure is an interface boundary. |
| V3.1.1 | RETAIN SEC-006 | Data inventory, classification and protection requirements are direct data protection/privacy controls. |
| V3.1.2 | RETAIN SEC-006 | Purpose-bound retention, deletion and anonymization are data lifecycle/privacy controls. |
| V3.2.1 | RETAIN SEC-007; SEC-006 supporting | Plaintext secrets in binaries/configuration are secrets management; sensitive-data protection is supporting. |
| V3.2.2 | RETAIN SEC-007; SEC-006 supporting | OS configuration stores must not expose secrets in plaintext. |
| V3.2.3 | EXPAND SEC-009 primary; SEC-006 and SEC-002 conditional | Log minimization/redaction is logging governance; SEC-006 applies to PII, SEC-002 to session/authentication tokens. |

## 9. SAMM v2.2.0 — semantic batch B

| Activity | Proposed semantic disposition | Rationale |
|---|---|---|
| D-SA-2-A — Provide preferred security solutions | EXPAND SEC-001 primary; SEC-002, SEC-003 and SEC-009 conditional | Reusable security architecture/patterns span threat-informed design, identity, authorization and logging; links depend on the specific shared service. |
| D-SA-2-B — Promote preferred tools and technologies | RETAIN SEC-008; SEC-001 supporting | Standardized technology selection is supply-chain/component governance informed by risk. |
| D-SA-3-A — Build reference architectures | EXPAND SEC-001 primary; SEC-002/003/005/006/009 conditional | Security reference architectures may contain multiple security services; do not map all controls unconditionally. |
| D-SA-3-B — Enforce the use of recommended technologies | RETAIN SEC-008; SEC-010 supporting | Technology allowlists and conformance checks are supply-chain governance; verification supports enforcement. |
| D-SR-1-A — Identify security requirements | EXPAND SEC-001 primary; SEC-006 and SEC-010 supporting | Security requirements should be risk-informed, define confidentiality/integrity/availability outcomes, and be traceable to verification. |
| D-SR-1-B — Perform vendor assessments | RETAIN SEC-008; SEC-001 supporting | Supplier capability and component/service risk assessment are supply-chain governance and risk identification. |
| D-SR-2-A — Standardize and integrate security requirements | RETAIN SEC-001; SEC-002/003 conditional | Enterprise security requirement taxonomy includes identity/authorization domains, but each requirement should map to its actual control. |
| D-SR-2-B — Discuss security responsibilities with suppliers | EXPAND SEC-008 primary; SEC-001 supporting | Contractual security obligations and supplier accountability are supply-chain governance; organizational risk criteria inform requirements. |
| D-SR-3-A — Develop a security requirements framework | RETAIN SEC-001; SEC-010 supporting | A reusable requirements framework is governance/traceability; verification criteria make requirements testable. |
| D-SR-3-B — Align security methodology with suppliers | RETAIN SEC-008; SEC-001 and SEC-010 supporting | Supplier process/toolchain alignment is supply-chain assurance, with risk governance and shared verification. |
| D-TA-1-A — Perform application risk assessments | EXPAND SEC-001 primary; SEC-006 and SEC-011 conditional | Application CIA/business impact is risk assessment; data protection and resilience are mapped where the assessment covers those dimensions. |
| D-TA-1-B — Perform basic threat modeling | RETAIN SEC-001; SEC-010 supporting | Threat identification and mitigations are primary; test evidence is supporting. |
| D-TA-2-A — Inventory risk profiles | RETAIN SEC-001; SEC-010 supporting | Risk profile inventory is governance/risk tracking; evidence and assessment validation support it. |
| D-TA-2-B — Standardize and scale threat modeling | RETAIN SEC-001 | Standardized threat modeling methodology is directly within threat governance. |
| D-TA-3-A — Periodic review of risk profiles | RETAIN SEC-001 | Periodic enterprise risk-profile review is governance and risk lifecycle. |
| D-TA-3-B — Optimize threat modeling | EXPAND SEC-001 primary; SEC-010 supporting | Threat-model optimization is primary; automated validation and threat-to-test traceability support verification. |
| G-EG-1-A — Train all stakeholders for awareness | PARTIAL SEC-001; no broad automatic SEC-002/003/006 mapping | Security awareness is organizational governance; individual technical controls should be mapped only if the training curriculum explicitly covers them. |
| G-EG-1-B — Identify security champions | RETAIN SEC-001; SEC-010 conditional | Security champion role is governance; verification applies only where champion responsibilities include assurance/test evidence. |
| G-EG-2-A — Customize security training | PARTIAL SEC-001; SEC-010 conditional | Role/technology-specific training is governance; technical controls are curriculum-dependent. |
| G-EG-2-B — Implement centers of excellence | RETAIN SEC-001; SEC-010 supporting | Security center of excellence owns guidance and governance, with verification practices as supporting capability. |
| G-EG-3-A — Standardize security guidance | RETAIN SEC-001; SEC-010 supporting | Secure development guidance is governance; conformance verification is supporting. |
| G-EG-3-B — Establish a security community | RETAIN SEC-001; SEC-011 conditional | Knowledge sharing is governance; incident/resilience links only where community operations include incident learning and resilience. |

## 10. Updated reconciliation coverage snapshot

| Framework | Inventory | Row-level dispositions recorded in this paper | Remaining |
|---|---:|---:|---:|
| ASVS | 345 | 29 | 316 |
| TCASVS | 132 | 56 | 76 |
| SAMM | 90 | 24 | 66 |

Counts are paper coverage, not approved mapping counts. TCASVS includes the initial 23 rows plus 33 additional rows in batch B. SAMM includes 2 initial rows plus 22 additional rows in batch B.

## 11. Canonical dictionary change request — memory safety and secure coding

The source rows above expose a recurring coverage gap. Existing GDES-SEC-004 is defined as input/output/injection and must not be stretched to own memory-safe programming, binary exploit mitigation, safe resource lifecycle, ASLR, DEP/NX, CFI or hardware-assisted exploit mitigations.

Proposed Standards Owner consideration:
- Add a dedicated canonical control, tentatively `GDES-SEC-012 — Secure Coding and Runtime Exploit Mitigation`, covering memory/resource safety, safe language/runtime configuration, binary exploit mitigations and platform-specific hardening.
- Keep SEC-010 as verification/evidence, not the owner of the underlying technical safeguard.
- If the owner prefers not to expand the dictionary, mark these source requirements as `GAP — NO DIRECT CANONICAL CONTROL` and preserve explicit residual coverage gaps. Do not force-map them.
- This is a proposed change request only; no canonical dictionary edit or approval is made by this paper.


## 12. ASVS v5.0.0 — semantic batch B (V2.1–V2.4)

Source catalog blob: `8e1f34ae3f80f8121f29de7fc1b6d33253d0d646`.

| ASVS requirement | Proposed disposition | Rationale |
|---|---|---|
| V2.1.1 | RETAIN SEC-004 | Documented structural input validation rules are direct input-handling controls. |
| V2.1.2 | EXPAND SEC-004 primary; SEC-003 conditional | Cross-field consistency is input validation; SEC-003 applies when the relationship encodes authorization or ownership constraints. |
| V2.1.3 | EXPAND SEC-004 primary; SEC-003 conditional | Documented business limits are validation; per-user entitlement/quota enforcement may require authorization. |
| V2.2.1 | RETAIN SEC-004 | Positive/allowlist validation and business constraints are direct input validation. |
| V2.2.2 | EXPAND SEC-004 primary; SEC-003 supporting | Trusted server-side validation is mandatory; authorization checks must also be server-side when input affects protected actions. |
| V2.2.3 | RETAIN SEC-004 | Consistency of related input values is validation/business-rule integrity. |
| V2.3.1 | EXPAND SEC-003 primary; SEC-004 and SEC-010 supporting | Workflow sequencing is authorization/state-transition control; input integrity and test evidence support it. |
| V2.3.2 | EXPAND SEC-003 primary; SEC-004 and SEC-010 supporting | Business limits may encode user entitlement/authorization; validation and verification are supporting. |
| V2.3.3 | EXPAND DB-003 primary; SEC-010 supporting | Atomic business transactions and rollback are transaction/concurrency/temporal integrity, not generic input validation. |
| V2.3.4 | EXPAND DB-003 primary; SEC-003 supporting | Locking against double booking is concurrency/consistency; access control protects who may reserve or modify the resource. |
| V2.3.5 | EXPAND SEC-003 primary; SEC-010 supporting | Multi-user approval and separation of duties are authorization controls; verification evidence is supporting. |
| V2.4.1 | EXPAND SEC-005 primary; SEC-003 and SEC-011 supporting | Rate limiting/anti-automation protects service interfaces and resource availability; authorization and resilience apply to scoped actions and outage behavior. |
| V2.4.2 | EXPAND SEC-003 primary; DB-003 conditional | Human-timing checks are anti-abuse/business authorization; DB-003 applies where rapid duplicate submissions threaten transaction consistency/idempotency. |

### ASVS batch B findings

- V2.3.3 and V2.3.4 should map to DB-003 where atomicity, locking and concurrency are the actual source requirement outcomes.
- Existing candidate SEC-004/SEC-010 for business-logic requirements is incomplete; authorization and database transaction integrity are first-class dimensions.
- Rate limiting is primarily an API/network and availability concern, not merely input sanitization.

## 13. TCASVS v5.0.0 — semantic batch C (V3 data protection)

| Source ID | Proposed semantic disposition | Rationale |
|---|---|---|
| V3.2.4 | EXPAND SEC-007 primary; SEC-006 and SEC-010 supporting | Embedded secrets/key material are secrets/configuration; protection context and static-analysis evidence are supporting. |
| V3.2.5 | EXPAND DB-004 primary; DB-005 and SEC-006 supporting | Local database file access is database privilege/credential governance; encryption and backup/restore are conditional based on platform capabilities and data sensitivity. |
| V3.2.6 | EXPAND DB-005 primary; SEC-006 and SEC-011 supporting | Database/application backup-export integrity and restore handling belong to DB-005 where database data is involved; data protection and resilience support. |
| V3.3.1 | EXPAND SEC-002 primary; SEC-007 supporting | Session/authentication token storage is identity/session protection; OS secure storage is secrets/configuration. |
| V3.3.2 | RETAIN SEC-006; SEC-007 supporting | Encryption at rest and key-management practice are data protection and secret/key custody. |
| V3.3.3 | RETAIN SEC-007; SEC-002 conditional | OS credential APIs are secure secret storage; SEC-002 applies where stored material is authentication/session identity. |
| V3.3.4 | RETAIN SEC-007; SEC-006 supporting | Hardware-backed key custody and non-exportability are secrets/key management with cryptographic data-protection context. |
| V3.4.1 | GAP — secure memory/resource lifecycle; SEC-006/007 conditional | Zeroization and short-lived secret memory are not fully owned by the current dictionary; SEC-006/007 identify protected data/secret types but not memory-safe lifecycle. |
| V3.4.2 | GAP — secure memory/runtime hardening; SEC-006/007 conditional | Non-pageable memory is a platform/runtime hardening requirement; do not force-map it to generic encryption or secret storage. |
| V3.4.3 | RETAIN SEC-006; SEC-009 conditional | Clipboard leakage is sensitive-data exposure; logging/monitoring is not primary unless clipboard events are logged. |
| V3.4.4 | RETAIN SEC-006; SEC-009 conditional | Crash-dump minimization prevents sensitive-data disclosure; SEC-009 applies only to crash telemetry/error handling. |
| V3.5.1 | RETAIN SEC-006; DB-005 conditional | Secure removal of temporary sensitive data is data lifecycle protection; DB-005 applies if the temporary files are database backup/export artifacts. |
| V3.5.2 | EXPAND SEC-007 primary; SEC-003 supporting; DB-004 conditional | Temporary-file directory permissions are secure configuration and access control; DB-004 applies only to local DB files/credentials. |

## 14. SAMM v2.2.0 — semantic batch C

| Activity | Proposed semantic disposition | Rationale |
|---|---|---|
| G-PC-1-A — Define policies and standards | RETAIN SEC-001; SEC-008 supporting | Organization security policy baseline is governance; supply-chain standards are a subset where relevant. |
| G-PC-1-B — Identify compliance requirements | EXPAND SEC-001 primary; SEC-006/SEC-008 conditional | Compliance applicability is governance; privacy/data protection and supplier/component obligations depend on the applicable regime. |
| G-PC-2-A — Develop test procedures | RETAIN SEC-010; SEC-001 supporting | Security test procedure design is verification; policy requirements provide traceable criteria. |
| G-PC-2-B — Standardize policy and compliance requirements | EXPAND SEC-001 primary; SEC-010 supporting; SEC-006 conditional | Policy requirement libraries are governance and test guidance; privacy/data protection is included only where relevant. |
| G-PC-3-A — Measure compliance to policies and standards | EXPAND SEC-001 primary; SEC-010 supporting | Compliance measurement is governance and assurance evidence, not generic logging or configuration. |
| G-PC-3-B — Measure compliance to external requirements | EXPAND SEC-001 primary; SEC-010 supporting; SEC-006 conditional | External compliance status is governance and verification; privacy/data requirements apply when the regulation concerns protected data. |
| G-SM-1-A — Identify the organization's risk appetite | RETAIN SEC-001 | Risk appetite and security prioritization are governance/threat-risk management. |
| G-SM-1-B — Define basic security metrics | EXPAND SEC-001 primary; SEC-010 supporting | Program metrics are governance; measurement of assurance effectiveness is verification evidence. |
| G-SM-2-A — Define the security strategy | RETAIN SEC-001; SEC-010 supporting | Security strategy and milestones are governance; assurance metrics are supporting. |
| G-SM-2-B — Set strategic KPIs | EXPAND SEC-001 primary; SEC-010 supporting | Security program KPI targets are governance and assurance measurement, not ordinary operational logging. |
| G-SM-3-A — Align security and business strategies | RETAIN SEC-001 | Security strategy alignment and periodic review are governance. |
| G-SM-3-B — Drive the security program through metrics | EXPAND SEC-001 primary; SEC-010 supporting | Program improvement based on metrics is governance with verification/assurance evidence. |
| I-DM-1-A — Track security defects centrally | RETAIN SEC-010; SEC-009 supporting | Defect identification, triage and evidence are security verification; monitoring/alerting supports workflow. |
| I-DM-1-B — Define basic defect metrics | RETAIN SEC-010; SEC-001 supporting | Defect metrics are assurance evidence and governance reporting. |
| I-DM-2-A — Rate and track security defects | RETAIN SEC-010; SEC-001 supporting | Severity/risk scoring and defect tracking are verification and risk governance. |
| I-DM-2-B — Define advanced defect metrics | RETAIN SEC-010; SEC-001 supporting | Assurance and defect trend metrics are verification evidence and governance. |
| I-DM-3-A — Enforce an SLA for defect management | EXPAND SEC-010 primary; SEC-009 supporting; SEC-001 conditional | Defect closure and escalation are assurance workflow; alerting supports operational tracking; risk governance applies to escalations. |
| I-DM-3-B — Use metrics to improve the security strategy | EXPAND SEC-001 primary; SEC-010 supporting | Strategic adjustment from defect metrics is governance informed by assurance evidence. |
| I-SB-1-A — Define a consistent build process | EXPAND SEC-008 primary; SEC-007 supporting; SEC-010 supporting | Repeatable build process governs artifact provenance and configuration; verification demonstrates reproducibility. |
| I-SB-1-B — Identify application dependencies | RETAIN SEC-008; SEC-007 conditional | Dependency inventory is supply-chain governance; credentials/configuration are conditional and not inherent to a BOM. |

## 15. Updated reconciliation coverage snapshot

| Framework | Inventory | Row-level dispositions recorded in this paper | Remaining |
|---|---:|---:|---:|
| ASVS | 345 | 42 | 303 |
| TCASVS | 132 | 69 | 63 |
| SAMM | 90 | 44 | 46 |

Counts are cumulative distinct source rows represented in sections 2, 7–9 and 12–14. They are documentary triage coverage only; they are not approval, compliance evidence, runtime test results or independent review.

## 16. Additional canonical control gap proposal

The latest batches show two distinct control domains not fully represented by the proposed 16-control dictionary:

1. **Secure coding and runtime exploit mitigation** — memory safety, resource lifecycle, binary mitigations (ASLR, DEP/NX, CFI), platform exploit hardening and secret-memory lifecycle. This remains a proposed `GDES-SEC-012` change request.
2. **Abuse resistance and service availability** — anti-automation, rate limiting, resource exhaustion and service-interface abuse. Existing SEC-005/SEC-011 cover parts, but their definitions should be checked to ensure rate-limit and abuse controls have an explicit owner.

Do not approve either extension by inference. Keep the source rows explicitly marked GAP or PARTIAL until the Standards Owner decides the canonical dictionary scope.


## 17. Complete inventory-level crosswalks — 2026-11-11

Three row-level first-pass crosswalk files were generated from the pinned source catalogs:
- `data/GDES_ASVS_SEMANTIC_CROSSWALK_v0.1.csv` — 345 unique ASVS source IDs.
- `data/GDES_TCASVS_SEMANTIC_CROSSWALK_v0.1.csv` — 132 unique TCASVS source IDs.
- `data/GDES_SAMM_SEMANTIC_CROSSWALK_v0.1.csv` — 90 unique SAMM activity codes.

| Framework | Rows | Proposed multi-control rows | GAP / needs owner disposition |
|---|---:|---:|---:|
| ASVS | 345 | 112 | 18 |
| TCASVS | 132 | 58 | 25 |
| SAMM | 90 | 65 | 2 |
| Total | 567 | 235 | 45 |

These are complete row inventories with machine-assisted first-pass proposed primary/supporting relationships and source excerpts. They are **not human-approved semantic mappings**. Generic “verify” wording was explicitly removed as a reason to map SEC-010. A source row must have a defensible primary owner; no chapter/practice fallback is approval evidence.

The crosswalks retain unresolved rows and identify SEC-012 only as a non-canonical proposal. See `GDES_CYBERSECURITY_STANDARDS_OWNER_DECISION_MEMO_v0.2.md` for the consolidated decision request and control boundaries.

### Updated status

- Source-row inventory coverage: 567 / 567.
- Human semantic adjudication: NOT COMPLETE.
- Standards Owner approval: NOT RECORDED.
- SEC-012: PROPOSED ONLY; NOT CANONICAL.
- GDES: DRAFT — NOT APPROVED.


## 18. Adjudication follow-up — 2026-11-11

A source-based AI-assisted proposal register has been created for all 45 GAP/context rows:
`data/GDES_CYBERSECURITY_45_GAP_ADJUDICATION_v0.1.csv`.

Initial row-level primary/supporting QA findings have also been recorded:
- `data/GDES_ASVS_MAPPING_QA_FINDINGS_v0.1.csv` — 26 candidate corrections.
- `data/GDES_TCASVS_MAPPING_QA_FINDINGS_v0.1.csv` — 34 candidate corrections.
- `data/GDES_SAMM_MAPPING_QA_FINDINGS_v0.1.csv` — 47 candidate corrections.

These 107 findings are candidate corrections, not yet applied to the v0.1 crosswalks. They reveal over-broad multi-primary mappings, incorrect primary owners and irrelevant supporting links. The 567-row inventory is complete, but every remaining primary and supporting mapping has not yet been individually adjudicated. See `GDES_CYBERSECURITY_MAPPING_ADJUDICATION_STATUS_v0.1.md` for exact completion boundaries and closure sequence.

Status remains AI-assisted working review; Standards Owner validation pending; GDES DRAFT — NOT APPROVED.
