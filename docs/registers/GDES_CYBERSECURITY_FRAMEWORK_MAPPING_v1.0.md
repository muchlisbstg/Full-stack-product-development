# GDES Cybersecurity Framework Mapping v1.0
## ASVS · MASVS · MASWE · MASTG · TCASVS · SAMM

| Metadata | Value |
|---|---|
| Artifact ID | GDES-SEC-MAP-002 |
| Version | 1.0 |
| Status | **TECHNICAL CROSSWALK DRAFT — REVIEW REQUIRED** |
| Canonical dictionary | GDES-SEC-DICT-001 (proposed) |
| Scope | Web/API, Android, iOS, Desktop, database and security lifecycle |
| Mapping date | 2026-11-11 |

> Mapping is a traceability aid, not certification or evidence of control effectiveness. Upstream requirements must be selected by applicability, architecture, threat model and platform. Do not infer a GDES PASS from an upstream ID.

## 1. Pinned upstream sources

| Framework | Version/source pin | Scope and verification note |
|---|---|---|
| OWASP ASVS | v5.0.0; CSV blob `184cf3b04a8fe1809dbed8b6e73be7a6fbaf8689` | Web/API and server-side application requirements. IDs must be serialized as `v5.0.0-<section>.<requirement>`; preserve exact section reference in evidence. |
| OWASP MASVS | Repository YAML blob `759acf74ebad2e9f06d34f7dfb92e5881e9340a2`; metadata version `vx.x.x` | Do not assign an invented semantic version to the YAML. Control groups and IDs are pinned by blob. |
| OWASP MASWE | Tag v1.0.0; commit `308b82b4bbe29166934fb5a621b40471cfea61db` | 78 stable weakness IDs across eight MASVS groups. |
| OWASP MASTG | Tag v2.0.0; commit `990472dbcffe126f5556045d60270c4ffdfdde72` | Stable test IDs use `MASTG-TEST-####`; platform-specific Android/iOS tests. Test metadata links to MASWE weaknesses. |
| OWASP TCASVS | Repository commit `9c05d7ae8d7a5934688f8e396444c9e0b25a2074`; chapter blobs V1–V6 retained in Mapping Matrix v1.0 | Six chapters: architecture/threat modeling, build/deployment, data storage/protection, code quality, cryptography, network communication. Metadata discrepancy with OWASP project card remains documented. |
| OWASP SAMM | v2.2.0; selected practice blobs TA `9e7ef2a9cec41a0b9daec52699429b00ec0b73ad`, ST `bacd54e4cbdbf5c372b2474cb494c04832299b83`, SB `d7ee530c995932aaec501ae38373d3c8dee600a6` | Practice-level maturity framework; mapping is not a maturity score or proof of implementation. |

License control:
- ASVS, TCASVS and SAMM are recorded as CC BY-SA 4.0 in the existing pinned-source matrix; verify exact LICENSE snapshot before redistribution/adaptation.
- MASVS, MASWE and MASTG license files must be verified at the pinned commit before reproducing or adapting source content.
- This document uses original GDES wording and identifiers; upstream content is referenced, not reproduced wholesale.

## 2. Canonical GDES to ASVS and TCASVS crosswalk

The ranges below are candidate section-level coverage from the existing technical matrix. Reviewer must confirm exact individual requirements, exclusions, version-specific IDs and applicability before approval.

| Canonical GDES control | ASVS 5.0.0 candidate sections | TCASVS 5.0.0 candidate sections | Coverage |
|---|---|---|---|
| GDES-SEC-001 Governance & Threat Modeling | V15.1.1–V15.1.5; V15.2.1–V15.2.5 | V1.1.1–V1.1.6; V1.2.1–V1.2.4; V1.3.1–V1.3.5; V1.4.1–V1.4.4 | Partial; risk ownership and formal approvals are GDES additions |
| GDES-SEC-002 Identity & Authentication | V6.1.1–V6.8.4; V7.1.1–V7.6.2; V9.1.1–V9.2.4; V10.1.1–V10.6.2 | V2.4.1–V2.4.7; V3.3.1–V3.3.4 for local credential protection | Partial; backend identity vs local authentication must be separated |
| GDES-SEC-003 Authorization | V8.1.1–V8.4.2; V4.1.1–V4.1.5; V9.2.1–V9.2.4 where applicable | V2.4.1–V2.4.7; V4.5.1–V4.5.5 | Partial; tenant/site/resource negative tests are GDES additions |
| GDES-SEC-004 Input/Output | V1.1.1–V1.2.10; V1.3.1–V1.3.12; V1.5.1–V1.5.3; V2.1.1–V2.3.5; V5.2.1–V5.2.6 | V4.1.1–V4.1.8; V4.3.1–V4.3.4 | Partial; platform-specific parsers/IPC/import paths need tests |
| GDES-SEC-005 API/Network | V4.1.1–V4.4.4; V10.2.1–V10.6.2; V12.1.1–V12.3.5 | V6.1.1–V6.5.2; V4.5.1–V4.5.5 | Partial; SSRF, DNS rebinding and egress controls require GDES-specific tests |
| GDES-SEC-006 Data Protection/Privacy | V11.1.1–V11.7.2; V12.1.1–V12.3.5; V14.2.1–V14.2.8 | V3.1.1–V3.5.4; V5.1.1–V5.6.4; V6.1.1–V6.1.3 | Partial; classification, retention and deletion policy are GDES additions |
| GDES-SEC-007 Secrets/Configuration | V13.1.1–V13.4.7; V15.2.1–V15.2.5 | V2.1.1–V2.1.8; V2.3.1–V2.3.6; V2.4.5; V3.3.1–V3.3.4 | Partial; pipeline/runtime/client-bundle evidence required |
| GDES-SEC-008 Supply Chain | V15.2.1–V15.2.5; V13.1.1–V13.1.4; V13.4.1–V13.4.7 | V2.1.1–V2.1.8; V2.3.1–V2.3.6; V4.6.1–V4.6.8 | Partial; SBOM/provenance/signing/license gates require project evidence |
| GDES-SEC-009 Logging/Monitoring | V7.1.1–V7.6.2; V14.1.1–V14.3.3; V15.4.1–V15.4.4 | V2.3.1–V2.3.6; V3.1.1–V3.5.4 | Partial; event attribution, alert and retention requirements need local criteria |
| GDES-SEC-010 Verification/Evidence | V1.14 and applicable V13–V15 verification/configuration requirements | V1.4 and applicable V4–V6 verification-related requirements | Partial; SHA-bound evidence, independent review and exception authority are GDES governance |
| GDES-SEC-011 Incident/Resilience | Applicable V14–V15 security logging, configuration and verification sections | V2, V3, V4 and V6 operationally applicable sections | Partial; incident ownership, recovery objectives and rollback exercises are GDES additions |
| GDES-DB-001 Relational Integrity | V1.2.1–V1.2.10; V2.3.1–V2.3.5; V14.1.1–V14.3.3 | V3.1.1–V3.5.4 | Major gap; framework references do not prove DB constraints/relational behavior |
| GDES-DB-002 Tenant/RLS Isolation | V8.1.1–V8.4.2; V14.1.1–V14.3.3 | V2.4.1–V2.4.7; V3.1.1–V3.5.4 | Major gap; native RLS and composite tenant FKs require DB tests |
| GDES-DB-003 Transactions/Concurrency | Applicable V1.2, V2.3, V14 business logic/data requirements | V3.1–V3.5 | Major gap; isolation, races, idempotency and temporal consistency need engine-native tests |
| GDES-DB-004 DB Privilege/Audit | V8.1–V8.4; V13.1–V13.4; V14.1–V14.3 | V2.4; V3.1–V3.5 | Partial; DB role/grant/bypass tests are engine-specific |
| GDES-DB-005 Migration/Recovery/Parity | Applicable V13–V15 configuration, deployment and verification requirements | V2, V3 and V4 applicable sections | Major gap; backup/restore, migrations and cross-engine parity are local GDES criteria |

## 3. MASVS control mapping

The MASVS control model defines these eight groups. Control IDs below are the exact IDs in the pinned YAML snapshot.

| MASVS group | Control IDs | Canonical GDES mapping |
|---|---|---|
| MASVS-STORAGE | MASVS-STORAGE-1, MASVS-STORAGE-2 | SEC-006, SEC-007; DB-004 where local credentials/connection data are stored |
| MASVS-CRYPTO | MASVS-CRYPTO-1, MASVS-CRYPTO-2 | SEC-006, SEC-007 |
| MASVS-AUTH | MASVS-AUTH-1, MASVS-AUTH-2, MASVS-AUTH-3 | SEC-002, SEC-003 |
| MASVS-NETWORK | MASVS-NETWORK-1, MASVS-NETWORK-2 | SEC-005 |
| MASVS-PLATFORM | MASVS-PLATFORM-1, MASVS-PLATFORM-2, MASVS-PLATFORM-3 | SEC-004, SEC-005, SEC-006, SEC-009 |
| MASVS-CODE | MASVS-CODE-1, MASVS-CODE-2, MASVS-CODE-3, MASVS-CODE-4 | SEC-004, SEC-008, SEC-010 |
| MASVS-RESILIENCE | MASVS-RESILIENCE-1 through MASVS-RESILIENCE-4 | SEC-008, SEC-010, SEC-011 |
| MASVS-PRIVACY | MASVS-PRIVACY-1 through MASVS-PRIVACY-4 | SEC-006, SEC-009 |

Boundary: MASVS validates mobile client controls. It does not replace ASVS/backend authorization, PostgreSQL RLS, database integrity, or desktop-specific security assessment.

## 4. MASWE v1.0.0 weakness catalogue mapping

Pinned MASWE v1.0.0 contains 78 stable IDs in eight groups. The following ranges are the complete catalogue coverage ranges; individual weakness applicability must be selected from each weakness's `masvs-v2` metadata and app threat model.

| MASWE group | Complete ID range | Count | GDES controls to assess |
|---|---:|---:|---|
| STORAGE | MASWE-0001–MASWE-0006 | 6 | SEC-006, SEC-007, SEC-009 |
| CRYPTO | MASWE-0007–MASWE-0017 | 11 | SEC-006, SEC-007 |
| AUTH | MASWE-0018–MASWE-0025 | 8 | SEC-002, SEC-003 |
| NETWORK | MASWE-0026–MASWE-0028 | 3 | SEC-005 |
| PLATFORM | MASWE-0029–MASWE-0040 | 12 | SEC-004, SEC-005, SEC-006, SEC-009 |
| CODE | MASWE-0041–MASWE-0050 | 10 | SEC-004, SEC-008, SEC-010 |
| RESILIENCE | MASWE-0051–MASWE-0065 | 15 | SEC-008, SEC-010, SEC-011 |
| PRIVACY | MASWE-0066–MASWE-0078 | 13 | SEC-006, SEC-009 |

All 78 IDs are within the pinned catalogue and no ID range is omitted. However, this table is group-level coverage, not a claim that all 78 weaknesses are applicable to every GDES product. The reviewer must validate the weakness title, requirement, platforms, profile and MASVS v2 mappings from the pinned weakness file before adding a test to the product scope.

## 5. MASTG v2.0.0 test mapping and selection rules

MASTG v2 uses atomic, platform-specific tests with metadata linking `MASTG-TEST-####` to one or more `MASWE-####` weaknesses, profiles, techniques and knowledge articles. Select tests by reading the pinned test file's frontmatter; never infer a MASWE association from the test ID number.

The pinned repository tree contains 200 platform/category test files under `tests-beta/{android,ios}/MASVS-*/`. Their paths are retained as source references below. This is the enumerated test-file subset observed in the v2.0.0 tree; it is not a statement that MASTG's entire knowledge base contains only 200 tests.

| Platform/category | Test IDs in pinned test-file subset | GDES controls |
|---|---|---|
| Android AUTH | 0326–0330 | SEC-002, SEC-003 |
| iOS AUTH | 0266–0271 | SEC-002, SEC-003 |
| Android CODE | 0222, 0223, 0245, 0272, 0274, 0337, 0339, 0372, 0374, 0375, 0382, 0392, 0398–0400 | SEC-004, SEC-008, SEC-010 |
| iOS CODE | 0228–0230, 0273, 0275, 0383, 0384, 0386 | SEC-004, SEC-008, SEC-010 |
| Android CRYPTO | 0204, 0205, 0208, 0212, 0221, 0232, 0307–0310, 0312, 0350 | SEC-006, SEC-007 |
| iOS CRYPTO | 0209–0211, 0213, 0214, 0311, 0317, 0349 | SEC-006, SEC-007 |
| Android NETWORK | 0217, 0218, 0233–0239, 0242–0244, 0282–0286, 0295 | SEC-005 |
| iOS NETWORK | 0321–0323, 0342–0345, 0348, 0385, 0396, 0397 | SEC-005 |
| Android PLATFORM | 0250–0253, 0258, 0289, 0291–0294, 0315, 0316, 0320, 0334, 0340, 0355–0357, 0364–0366, 0381, 0393, 0394 | SEC-004, SEC-005, SEC-006, SEC-009 |
| iOS PLATFORM | 0276–0280, 0290, 0331–0333, 0335, 0336, 0346, 0347, 0370, 0371, 0376–0380, 0389, 0390, 0395 | SEC-004, SEC-005, SEC-006, SEC-009 |
| Android PRIVACY | 0206, 0254–0257, 0318, 0319 | SEC-006, SEC-009 |
| iOS PRIVACY | 0281, 0360–0363 | SEC-006, SEC-009 |
| Android RESILIENCE | 0224–0227, 0247, 0249, 0263–0265, 0288, 0324, 0325, 0338, 0341, 0351–0353, 0368, 0369 | SEC-008, SEC-010, SEC-011 |
| iOS RESILIENCE | 0219, 0220, 0240, 0241, 0246, 0248, 0261, 0354, 0358, 0359, 0367, 0387, 0391, 0401, 0402 | SEC-008, SEC-010, SEC-011 |
| Android STORAGE | 0200–0203, 0207, 0216, 0231, 0262, 0287, 0304–0306 | SEC-006, SEC-007, SEC-009 |
| iOS STORAGE | 0215, 0296–0303, 0313, 0314, 0388 | SEC-006, SEC-007, SEC-009 |

Selection workflow:
1. Start from the applicable MASVS control.
2. Enumerate relevant MASWE weaknesses using the pinned weakness metadata.
3. Select Android/iOS MASTG test files whose frontmatter `weakness` exactly matches those MASWE IDs.
4. Record test ID, platform, test type, profile, prerequisite, tool/technique, expected observation and evaluation.
5. Do not mark a GDES control PASS until the selected tests are actually executed on the declared app build and environment.
6. If no platform-specific test exists, record a GDES-specific test gap; do not invent a MASTG ID.

Example source-level check: MASTG-TEST-0204 is an Android static/code/manual test whose pinned metadata identifies MASWE-0027. This illustrates the required exact frontmatter link; it must not be generalized to other tests.

## 6. SAMM v2.2.0 practice mapping

| GDES control family | SAMM practices to assess | Use |
|---|---|---|
| SEC-001 governance/threat | SM Strategy & Metrics; PC Policy & Compliance; EG Education & Guidance; TA Threat Assessment; SR Security Requirements | Governance maturity and risk assessment |
| SEC-002/003 identity/access | SR Security Requirements; SA Secure Architecture; SD Secure Deployment; RT Requirements-driven Testing; ST Security Testing | Architecture and verification maturity |
| SEC-004/005 input/API/network | SA Secure Architecture; SB Secure Build; SD Secure Deployment; RT; ST | Secure design/build/deploy/testing |
| SEC-006/007 data/secrets | PC; SA; SB; SD; EM Environment Management | Data handling and configuration maturity |
| SEC-008 supply chain | SB; SD; DM Defect Management; EM | Build/dependency and defect process maturity |
| SEC-009 logging/monitoring | IM Incident Management; EM; OM Operational Management; PC | Operational visibility and governance |
| SEC-010 verification/evidence | AA Architecture Assessment; RT; ST; DM | Independent verification and defect handling |
| SEC-011 resilience/incident | IM; EM; OM | Incident response and operational continuity |
| DB-001–005 | SA; SB; SD; RT; ST; EM; OM | Database architecture, deployment and verification maturity |

This is a practice-area mapping, not a SAMM maturity score. Full stream/activity/question mapping and source pins for every practice remain an independent reviewer task.

## 7. Mapping gaps and disposition

| Gap ID | Description | Required action | Status |
|---|---|---|---|
| MAP-002-01 | Individual ASVS requirement IDs and applicability need row-level validation against the pinned CSV. | Produce product-specific ASVS selection and verification level. | REVIEW REQUIRED |
| MAP-002-02 | MASWE range coverage is complete, but each weakness's exact title, MASVS v2 metadata and product applicability are not expanded in this matrix. | Generate product-specific weakness applicability register. | PARTIAL |
| MAP-002-03 | MASTG test catalogue subset is enumerated by platform/category; all test-to-MASWE links have not been expanded row by row here. | Extract test frontmatter and create exact test-to-weakness register. | PARTIAL |
| MAP-002-04 | MASVS metadata is vx.x.x in pinned YAML. | Preserve blob pin; do not assign semantic version. | RECORDED |
| MAP-002-05 | TCASVS project-card metadata conflicts with repository release content. | Standards Owner disposition and reviewer confirmation. | OPEN |
| MAP-002-06 | SAMM stream/activity/question mapping incomplete. | Complete exact source-level mapping. | OPEN |
| MAP-002-07 | Database RLS, composite FKs, transaction isolation, concurrency and temporal consistency are not proven by these frameworks. | Use GDES-DB supplement and target-engine tests. | OPEN |
| MAP-002-08 | MASVS/MASWE/MASTG license snapshots require verification. | Record LICENSE blob SHAs before redistribution. | OPEN |

**Disposition: Framework crosswalk assembled; not complete for independent approval until the listed row-level gaps are closed.**
