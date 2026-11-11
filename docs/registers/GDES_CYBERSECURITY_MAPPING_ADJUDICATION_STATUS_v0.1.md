# GDES Cybersecurity Mapping Adjudication Status v0.1

**Status:** WORKING PAPER — AI-ASSISTED SOURCE REVIEW — NOT APPROVED  
**Date:** 2026-11-11  
**Branch:** `gdes/ai-governance-v1-pilot`

## 1. Scope and evidence integrity

The pinned source inventories and first-pass crosswalks were re-read from GitHub. Exact row counts and source-ID reconciliation:
- ASVS 5.0.0: 345 source rows / 345 crosswalk rows / 0 missing IDs.
- TCASVS 5.0.0: 132 source rows / 132 crosswalk rows / 0 missing IDs.
- SAMM 2.2.0: 90 source rows / 90 crosswalk rows / 0 missing IDs.

Total: 567 source rows and 567 crosswalk rows. This confirms inventory completeness only.

## 2. GAP adjudication proposals

The 45 existing GAP / NEEDS DOMAIN CONTEXT rows have source-based proposed dispositions in:
- `data/GDES_CYBERSECURITY_45_GAP_ADJUDICATION_v0.1.csv`

Count: ASVS 18, TCASVS 25, SAMM 2. All 45 proposals identify primary owner, supporting/conditional links where applicable, rationale and caveats. SEC-012 is explicitly proposed only, not canonical. Several rows remain context-dependent even after a candidate mapping is proposed; the caveat column preserves that limitation.

**Review status:** AI-assisted adjudication proposal; Standards Owner validation pending. This is not a human manual review or approved closure of the GAP register.

## 3. Primary/supporting mapping QA findings

Candidate corrections for apparent primary-owner errors, irrelevant co-primary links and over-broad supporting links are recorded in:
- `data/GDES_ASVS_MAPPING_QA_FINDINGS_v0.1.csv` — 26 findings.
- `data/GDES_TCASVS_MAPPING_QA_FINDINGS_v0.1.csv` — 34 findings.
- `data/GDES_SAMM_MAPPING_QA_FINDINGS_v0.1.csv` — 47 findings.

Total: 107 candidate row-level corrections. Examples include:
- SEC-010 should be primary for security testing, SAST/DAST, fuzzing, penetration testing and assurance activities, rather than a supporting link behind unrelated technical controls.
- SEC-009 should be primary when the source outcome is logging, monitoring, audit trail or error reporting.
- SEC-007 should be primary for cryptographic key/secret custody and cryptographic configuration.
- SEC-008 should be primary for dependency, build, artifact and software supply-chain lifecycle outcomes.
- DB-003 must not be used for generic browser/network behavior, general application thread safety or protocol race testing unless database transaction/concurrency semantics are explicitly in scope.
- SEC-005 should own network/service/IPC interface and transport outcomes; SEC-011 is supporting when availability/resilience is an explicit outcome.
- Multi-control mappings need a distinct source-grounded rationale for every supporting link. A broad source sentence listing several controls does not make all of them co-primary.

**Review status:** Candidate corrections are recorded, but they have not yet been applied to the canonical crosswalk files. The 107 entries are not proof that all remaining rows are correct.

## 4. What is not complete

- The 567 primary assignments have not all been individually adjudicated and reconciled.
- Every one of the 235 multi-control proposals has not yet received final per-link justification.
- Remaining single-control rows have not all been independently checked for false-positive ownership.
- The 107 QA findings have not been applied to the v0.1 crosswalks.
- No independent Security Reviewer or Database Reviewer has performed a review.
- No Standards Owner decision on SEC-012 or other control boundaries is recorded.

## 5. Required closure sequence

1. Apply and verify the 45 GAP proposals in a new crosswalk revision, preserving original source IDs and marking SEC-012 references as conditional/proposed.
2. Resolve the 107 row-level mapping QA findings; where the source outcome is ambiguous, retain NEEDS DOMAIN CONTEXT rather than force-fit.
3. Review the remaining crosswalk rows, including all single-primary mappings and all supporting links, with one primary owner per source row wherever defensible.
4. Produce a duplicate/overlap/conflict register: same source row mapped to competing primaries, redundant supporting links, overlapping control definitions and unowned source outcomes.
5. Reconcile source coverage, uniqueness, control distribution, mapping rationale and exception counts after all changes.
6. Submit the resulting package to Standards Owner for APPROVE / APPROVE WITH REVISION / REJECT / DEFER.

GDES remains DRAFT — NOT APPROVED. Inventory coverage is not semantic approval, implementation evidence, compliance certification or independent review. No procurement, reviewer appointment, runtime testing, rollout or deployment is part of this work.
