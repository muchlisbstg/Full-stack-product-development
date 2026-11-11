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
