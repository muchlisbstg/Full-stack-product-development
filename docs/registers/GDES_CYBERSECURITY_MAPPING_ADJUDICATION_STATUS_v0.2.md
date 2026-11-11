# GDES Cybersecurity Mapping Adjudication Status v0.2

**Status:** ROW-LEVEL AI-ASSISTED REVIEW COMPLETE — HUMAN / STANDARDS OWNER VALIDATION OPEN  
**Date:** 2026-11-11  
**Branch:** `gdes/ai-governance-v1-pilot`

## 1. Versioned crosswalks

- ASVS 5.0.0: `data/GDES_ASVS_SEMANTIC_CROSSWALK_v0.2.csv` — 345 rows.
- TCASVS 5.0.0: `data/GDES_TCASVS_SEMANTIC_CROSSWALK_v0.2.csv` — 132 rows.
- SAMM 2.2.0: `data/GDES_SAMM_SEMANTIC_CROSSWALK_v0.2.csv` — 90 rows.

Total: 567 source rows and 567 crosswalk rows.

## 2. Application of previous proposals

- 45/45 GAP adjudication proposals were applied to the v0.2 crosswalks (ASVS 18, TCASVS 25, SAMM 2), then reconciled against row-level QA corrections. Their status is updated in `data/GDES_CYBERSECURITY_45_GAP_ADJUDICATION_v0.1.csv`.
- 107/107 mapping QA candidates were applied or retained as explicit GAP/CONFLICT dispositions: ASVS 26, TCASVS 34, SAMM 47. The three QA registers now identify the v0.2 crosswalk disposition.
- 235 initial multi-control candidates were re-evaluated. The current row-level review records 118 proposed primary-plus-supporting relationships and 115 unresolved primary-owner conflicts; other source rows were reduced to a single candidate or retained as GAP following the correction pass.

## 3. Full row-level review status

| Row status | Count |
|---|---:|
| AI-reviewed single primary candidate — human validation pending | 199 |
| Low semantic signal — human review required | 118 |
| AI-reviewed primary + supporting — human validation pending | 118 |
| Primary-owner conflict — human owner decision required | 115 |
| GAP — Standards Owner disposition required | 17 |
| **Total** | **567** |

Framework GAP distribution: ASVS 5; TCASVS 12; SAMM 0.

The semantic evidence score is a transparent keyword-evidence heuristic used to flag weak source-text support. It is not a probability, confidence guarantee, formal semantic proof or human review result. A score below threshold does not prove the mapping is wrong; it identifies rows requiring contextual human review.

## 4. Consolidated exception register

`data/GDES_CYBERSECURITY_DUPLICATE_OVERLAP_CONFLICT_UNMAPPED_v0.2.csv` records supporting overlaps, primary-owner conflicts, GAP/unmapped rows and low-signal rows.

Source-ID reconciliation against the pinned catalogs:
- Missing source IDs: 0.
- Orphan crosswalk IDs: 0.
- Duplicate source IDs in catalogs: 0.

These are inventory-integrity checks only. No claim is made that the semantic mapping is fully correct.

## 5. Important limitations

- The row-by-row pass is AI-assisted source-text adjudication. It is not a manual human review by an independent reviewer or Standards Owner.
- The 118 low-signal rows, 115 primary-owner conflicts and 17 GAP rows remain open.
- All 118 supporting relationships require human confirmation of relevance and applicability.
- Single-primary candidates also remain provisional until human validation.
- SEC-012 remains proposed only, not canonical.
- No runtime security tests, implementation evidence, legal interpretation, independent review or compliance certification was performed.
- Procurement, candidate outreach, reviewer appointment, rollout and deployment remain outside scope.

## 6. Readiness assessment

**Not ready for final GDES Cybersecurity approval.**

The v0.2 package is ready for Standards Owner review of mapping policy, control boundaries and SEC-012 in principle. Final standard approval should be deferred until the open conflicts, low-signal rows and GAP dispositions are resolved and independently reviewed as required.
