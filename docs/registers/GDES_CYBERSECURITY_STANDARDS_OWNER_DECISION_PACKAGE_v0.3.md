# GDES Cybersecurity — Standards Owner Decision Package v0.3

**Status:** FOR STANDARDS OWNER REVIEW — NOT APPROVED  
**Date:** 2026-11-11  
**Repository / branch:** `muchlisbstg/Full-stack-product-development` / `gdes/ai-governance-v1-pilot`

## 1. Decision scope

This package requests Standards Owner decisions on semantic mapping policy, control ownership boundaries and the proposed SEC-012 control. It does **not** request final approval or rollout of GDES Cybersecurity. Final approval is not recommended while the row-level exceptions remain open.

## 2. Evidence baseline

Pinned source catalogs:
- ASVS 5.0.0 — 345 requirements; blob `8e1f34ae3f80f8121f29de7fc1b6d33253d0d646`.
- TCASVS 5.0.0 — 132 requirements; blob `8410732fab232000050ee2982945eeb91b169bf6`.
- SAMM 2.2.0 — 90 activities; blob `64f452ba0c5c6790363fe1813ed5b16e276edc0e`.

Versioned crosswalks:
- `data/GDES_ASVS_SEMANTIC_CROSSWALK_v0.2.csv` — 345 rows.
- `data/GDES_TCASVS_SEMANTIC_CROSSWALK_v0.2.csv` — 132 rows.
- `data/GDES_SAMM_SEMANTIC_CROSSWALK_v0.2.csv` — 90 rows.

Row-level audit: `data/GDES_CYBERSECURITY_ROW_LEVEL_RECONCILIATION_v0.2.csv` — 567 rows.

Consolidated exceptions: `data/GDES_CYBERSECURITY_DUPLICATE_OVERLAP_CONFLICT_UNMAPPED_v0.2.csv`.

## 3. Reconciliation result

| Review outcome | Count |
|---|---:|
| AI-reviewed single primary candidate — human validation pending | 199 |
| Low semantic signal — human review required | 118 |
| AI-reviewed primary + supporting — human validation pending | 118 |
| Primary-owner conflict — human owner decision required | 115 |
| GAP — Standards Owner disposition required | 17 |
| **Total** | **567** |

GAP distribution: ASVS 5; TCASVS 12; SAMM 0.

Inventory integrity: 567/567 source IDs matched; 0 missing source IDs; 0 orphan crosswalk IDs; 0 duplicate source IDs in the pinned catalogs.

The 45 prior GAP proposals and 107 mapping QA candidates have been applied or preserved as explicit GAP/CONFLICT dispositions in v0.2. The initial 235 multi-control candidate cohort has been reviewed row by row: 118 relationships remain as proposed supporting links; 115 rows have unresolved primary-owner conflicts. Remaining outcomes were reduced to single-primary candidates or explicit GAPs.

## 4. Interpretation and limitations

This is an AI-assisted row-by-row source-text review. The evidence score is a keyword-evidence heuristic used to flag low-signal rows; it is not a probability or proof of semantic correctness. No human reviewer or Standards Owner has approved these mappings.

All single-primary candidates remain provisional. Supporting links require human confirmation of relevance and applicability. The 118 low-signal rows, 115 conflicts and 17 GAPs are open. No runtime test, implementation verification, legal interpretation, independent security/database review or compliance certification is claimed.

## 5. Decisions requested

Decision options for each item: **APPROVE / APPROVE WITH REVISION / REJECT / DEFER**.

| ID | Decision requested | Recommendation |
|---|---|---|
| SO-CYB-01 | One primary owner per source outcome; retain GAP where no defensible owner exists | APPROVE |
| SO-CYB-02 | Supporting links require row-specific rationale and applicability conditions | APPROVE |
| SO-CYB-03 | Chapter/practice and keyword candidates are discovery aids, not approval evidence | APPROVE |
| SO-CYB-04 | SEC-010 is limited to testing, assessment, verification, assurance and evidence; not generic “Verify that” wording | APPROVE |
| SO-CYB-05 | SEC-005 owns API/network/transport/service/IPC and interface abuse; SEC-011 supports explicit availability/resilience outcomes | APPROVE |
| SO-CYB-06 | Adopt SEC-012 — Secure Coding and Runtime Exploit Mitigation | APPROVE IN PRINCIPLE; final dictionary wording and owner confirmation required |
| SO-CYB-07 | Retain the 17 GAP rows until source-specific owner decisions are made | APPROVE |
| SO-CYB-08 | Effective date, rollout and compliance claims | DEFER |
| SO-CYB-09 | Final GDES Cybersecurity standard approval | DEFER pending closure of 118 low-signal rows, 115 conflicts, 17 GAPs and required independent reviews |

## 6. Proposed SEC-012 wording

**Name:** GDES-SEC-012 — Secure Coding and Runtime Exploit Mitigation.

**Scope:** memory-safe programming; memory/resource lifecycle; safe string, buffer, pointer and integer operations; prevention of use-after-free, dangling pointers and memory corruption; language/runtime/compiler hardening; ASLR, DEP/NX, CFI and platform-specific runtime exploit mitigation.

**Boundaries:**
- SEC-004 remains input/output safety, validation, sanitization and injection prevention.
- SEC-007 remains secret/key custody and secure cryptographic configuration.
- SEC-010 remains testing and assurance, not the safeguard itself.
- SEC-008 remains dependency/build/artifact provenance.
- SEC-011 remains availability, resilience, incident response and recovery.

Until an explicit Standards Owner decision is recorded, SEC-012 is proposed only and is not a canonical control. If rejected, affected source rows remain GAP; they must not be force-mapped to SEC-004 or SEC-010.

## 7. Required closure gates before final approval

1. Human adjudication of all 118 low-signal rows and 115 primary-owner conflicts.
2. Human confirmation of all 118 proposed supporting relationships.
3. Standards Owner disposition of all 17 GAPs and SEC-012.
4. Reconciliation of control dictionary definitions, duplicates, overlap and cross-framework ownership.
5. Independent Security and Database review when procurement is authorized and funded.
6. Final evidence and exception reconciliation, then explicit Standards Owner approval.

No response is approval. GDES remains DRAFT — NOT APPROVED. Procurement and independent-review activity remain deferred; no candidates have been contacted or appointed.
