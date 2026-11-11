#!/usr/bin/env python3
"""Reproducible, pinned extraction of OWASP metadata for GDES crosswalks.

This script downloads only public source files at immutable commit SHAs, parses
metadata (not prose guesses), and writes machine-readable catalogs under
docs/registers/data/. All mapping outputs are explicitly marked as candidates
for reviewer disposition; source metadata is never treated as GDES PASS.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import urllib.request
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "docs" / "registers" / "data"
OUT.mkdir(parents=True, exist_ok=True)
HEADERS = {"User-Agent": "GDES-Cybersecurity-Metadata-Extractor/1.0", "Accept": "application/vnd.github+json"}

SOURCES = {
    "ASVS": {"repo": "OWASP/ASVS", "ref": "62981c68fd06206e8afa161653943935de9a5047", "version": "5.0.0",
             "data": "5.0/docs_en/OWASP_Application_Security_Verification_Standard_5.0.0_en.csv", "license": "LICENSE.md"},
    "MASVS": {"repo": "OWASP/masvs", "ref": "bbe226fd17e6dab51927f392936deef31c816423", "version": "metadata vx.x.x",
              "data": "OWASP_MASVS.yaml", "license": "License.md"},
    "MASWE": {"repo": "OWASP/maswe", "ref": "308b82b4bbe29166934fb5a621b40471cfea61db", "version": "1.0.0",
              "license": "License.md"},
    "MASTG": {"repo": "OWASP/mastg", "ref": "990472dbcffe126f5556045d60270c4ffdfdde72", "version": "2.0.0",
              "license": "License.md"},
    "TCASVS": {"repo": "OWASP/TCASVS", "ref": "f10ec111883787dd6f83e0237d0f1b2e043d55e0", "version": "5.0.0",
               "chapters": [f"5.0/en/0x{n:02x}-V{i}-{name}.md" for i, n, name in [
                   (1, 0x10, "Architecture-and-Threat-Modeling"),
                   (2, 0x11, "Build-Deployment-and-Environment-Hardening"),
                   (3, 0x12, "Data-Storage-and-Protection"),
                   (4, 0x13, "Code-Quality-and-Exploit-Mitigation"),
                   (5, 0x14, "Cryptography"),
                   (6, 0x15, "Network-Communication")]], "license": "LICENSE.md"},
    "SAMM": {"repo": "owaspsamm/core", "ref": "21352e0fc79a6764abcd83a008690e32d2d5a3fe", "version": "2.2.0",
             "license": "license.txt"},
}

# Existing GDES crosswalk section ranges. Each matched requirement is emitted
# as a candidate link, not a normative mapping or compliance assertion.
ASVS_RANGES = {
    "GDES-SEC-001": ["15.1.1-15.1.5", "15.2.1-15.2.5"],
    "GDES-SEC-002": ["6.1.1-6.8.4", "7.1.1-7.6.2", "9.1.1-9.2.4", "10.1.1-10.6.2"],
    "GDES-SEC-003": ["8.1.1-8.4.2", "4.1.1-4.1.5", "9.2.1-9.2.4"],
    "GDES-SEC-004": ["1.1.1-1.2.10", "1.3.1-1.3.12", "1.5.1-1.5.3", "2.1.1-2.3.5", "5.2.1-5.2.6"],
    "GDES-SEC-005": ["4.1.1-4.4.4", "10.2.1-10.6.2", "12.1.1-12.3.5"],
    "GDES-SEC-006": ["11.1.1-11.7.2", "12.1.1-12.3.5", "14.2.1-14.2.8"],
    "GDES-SEC-007": ["13.1.1-13.4.7", "15.2.1-15.2.5"],
    "GDES-SEC-008": ["15.2.1-15.2.5", "13.1.1-13.1.4", "13.4.1-13.4.7"],
    "GDES-SEC-009": ["16.1.1-16.5.4", "13.4.1-13.4.7"],
    "GDES-SEC-010": ["2.3.1-2.3.5", "15.1.1-15.2.5", "15.3.1-15.3.7", "15.4.1-15.4.4", "16.3.1-16.3.4"],
    "GDES-SEC-011": ["15.3.1-15.3.7", "16.3.1-16.3.4"],
}
ASVS_CHAPTER_TO_GDES = {
    "V1": ["GDES-SEC-004"],
    "V2": ["GDES-SEC-003", "GDES-SEC-004"],
    "V3": ["GDES-SEC-004", "GDES-SEC-005", "GDES-SEC-006", "GDES-SEC-009"],
    "V4": ["GDES-SEC-002", "GDES-SEC-003", "GDES-SEC-005"],
    "V5": ["GDES-SEC-004", "GDES-SEC-006", "GDES-SEC-008"],
    "V6": ["GDES-SEC-002"], "V7": ["GDES-SEC-002"], "V8": ["GDES-SEC-003"],
    "V9": ["GDES-SEC-002", "GDES-SEC-003"], "V10": ["GDES-SEC-002", "GDES-SEC-003", "GDES-SEC-005"],
    "V11": ["GDES-SEC-006"], "V12": ["GDES-SEC-005"],
    "V13": ["GDES-SEC-007", "GDES-SEC-008", "GDES-SEC-009"],
    "V14": ["GDES-SEC-006", "GDES-SEC-009"],
    "V15": ["GDES-SEC-001", "GDES-SEC-004", "GDES-SEC-008", "GDES-SEC-010"],
    "V16": ["GDES-SEC-009", "GDES-SEC-011"], "V17": ["GDES-SEC-005", "GDES-SEC-006"],
}
MASVS_TO_GDES = {
    "MASVS-STORAGE": ["GDES-SEC-006", "GDES-SEC-009"],
    "MASVS-CRYPTO": ["GDES-SEC-006"],
    "MASVS-AUTH": ["GDES-SEC-002", "GDES-SEC-003"],
    "MASVS-NETWORK": ["GDES-SEC-005", "GDES-SEC-006"],
    "MASVS-PLATFORM": ["GDES-SEC-003", "GDES-SEC-004", "GDES-SEC-005"],
    "MASVS-CODE": ["GDES-SEC-004", "GDES-SEC-007", "GDES-SEC-008"],
    "MASVS-RESILIENCE": ["GDES-SEC-010", "GDES-SEC-011"],
    "MASVS-PRIVACY": ["GDES-SEC-006", "GDES-SEC-009"],
}
TCASVS_TO_GDES = {
    "V1": ["GDES-SEC-001", "GDES-SEC-010", "GDES-SEC-011"],
    "V2": ["GDES-SEC-007", "GDES-SEC-008", "GDES-SEC-010"],
    "V3": ["GDES-SEC-006"],
    "V4": ["GDES-SEC-004", "GDES-SEC-008", "GDES-SEC-010"],
    "V5": ["GDES-SEC-006"],
    "V6": ["GDES-SEC-005", "GDES-SEC-006"],
}
SAMM_TO_GDES = {
    "D-SA": ["GDES-SEC-001", "GDES-SEC-003", "GDES-SEC-004", "GDES-SEC-005", "GDES-SEC-006"],
    "D-SR": ["GDES-SEC-001", "GDES-SEC-002", "GDES-SEC-003"],
    "D-TA": ["GDES-SEC-001", "GDES-SEC-011"],
    "G-EG": ["GDES-SEC-001", "GDES-SEC-011"],
    "G-PC": ["GDES-SEC-001", "GDES-SEC-007", "GDES-SEC-009"],
    "G-SM": ["GDES-SEC-001", "GDES-SEC-010"],
    "I-DM": ["GDES-SEC-008", "GDES-SEC-009", "GDES-SEC-010"],
    "I-SB": ["GDES-SEC-004", "GDES-SEC-006", "GDES-SEC-007", "GDES-SEC-008"],
    "I-SD": ["GDES-SEC-002", "GDES-SEC-005", "GDES-SEC-006", "GDES-SEC-007", "GDES-SEC-008"],
    "O-EM": ["GDES-SEC-005", "GDES-SEC-006", "GDES-SEC-007", "GDES-SEC-009", "GDES-SEC-011"],
    "O-IM": ["GDES-SEC-009", "GDES-SEC-011"],
    "O-OM": ["GDES-SEC-009", "GDES-SEC-011"],
    "V-AA": ["GDES-SEC-001", "GDES-SEC-003", "GDES-SEC-010"],
    "V-RT": ["GDES-SEC-002", "GDES-SEC-003", "GDES-SEC-004", "GDES-SEC-005", "GDES-SEC-006", "GDES-SEC-010"],
    "V-ST": ["GDES-SEC-002", "GDES-SEC-003", "GDES-SEC-004", "GDES-SEC-005", "GDES-SEC-006", "GDES-SEC-007", "GDES-SEC-008", "GDES-SEC-010"],
}

def get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=60) as response:
        return response.read()

def api_tree(repo: str, ref: str) -> list[dict]:
    obj = json.loads(get(f"https://api.github.com/repos/{repo}/git/trees/{ref}?recursive=1"))
    if obj.get("truncated"):
        raise RuntimeError(f"Git tree truncated: {repo}@{ref}")
    return obj["tree"]

def raw(repo: str, ref: str, path: str) -> bytes:
    return get(f"https://raw.githubusercontent.com/{repo}/{ref}/{path}")

def text_of(repo: str, ref: str, path: str) -> str:
    return raw(repo, ref, path).decode("utf-8-sig")

def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (OUT / name).open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        for row in rows:
            w.writerow({k: json.dumps(row.get(k), ensure_ascii=False) if isinstance(row.get(k), (list, dict)) else row.get(k, "") for k in fields})

def yaml_doc(content: str) -> dict:
    match = re.match(r"\A---\s*\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)", content)
    if not match:
        return {}
    value = yaml.safe_load(match.group(1)) or {}
    return value if isinstance(value, dict) else {}

def norm_list(value) -> list:
    if value is None:
        return []
    return value if isinstance(value, list) else [value]

def in_ranges(req: str, ranges: list[str]) -> bool:
    nums = req.removeprefix("V")
    for spec in ranges:
        lo, hi = spec.split("-", 1)
        if tuple(map(int, lo.split("."))) <= tuple(map(int, nums.split("."))) <= tuple(map(int, hi.split("."))):
            return True
    return False

def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def main() -> None:
    manifest = {"generated_at_utc": datetime.now(timezone.utc).isoformat(), "sources": {}, "counts": {}, "checks": {}}
    trees = {key: api_tree(v["repo"], v["ref"]) for key, v in SOURCES.items()}

    # MASVS control inventory
    cfg = yaml.safe_load(text_of(SOURCES["MASVS"]["repo"], SOURCES["MASVS"]["ref"], SOURCES["MASVS"]["data"]))
    masvs_rows = []
    for group in cfg.get("groups", []):
        gid = group.get("id", "")
        for control in group.get("controls", []):
            masvs_rows.append({"group_id": gid, "group_title": group.get("title", ""), "control_id": control.get("id", ""),
                               "statement": control.get("statement", ""), "description": control.get("description", ""),
                               "candidate_gdes_controls": MASVS_TO_GDES.get(gid, []),
                               "mapping_status": "CANDIDATE — REVIEW REQUIRED",
                               "source_path": SOURCES["MASVS"]["data"]})
    write_csv("GDES_MASVS_CONTROL_CATALOG_v1.0.csv",
              ["group_id", "group_title", "control_id", "statement", "description", "candidate_gdes_controls", "mapping_status", "source_path"], masvs_rows)

    # MASWE catalogue: every weakness markdown file at the immutable v1.0.0 commit.
    maswe_files = [x for x in trees["MASWE"] if x["type"] == "blob" and re.match(r"weaknesses/.*/MASWE-\d+\.md$", x["path"])]
    maswe_rows = []
    for f in sorted(maswe_files, key=lambda x: x["path"]):
        d = yaml_doc(text_of(SOURCES["MASWE"]["repo"], SOURCES["MASWE"]["ref"], f["path"]))
        group = f["path"].split("/")[-2]
        masvs_ids = norm_list((d.get("mappings") or {}).get("masvs-v2"))
        maswe_rows.append({"id": d.get("id", ""), "title": d.get("title", ""), "alias": d.get("alias", ""),
                           "requirement": d.get("requirement", ""), "platforms": d.get("platform", []),
                           "profiles": d.get("profiles", []), "threat": d.get("threat", ""),
                           "attacks": d.get("attacks", []), "masvs_group": group, "masvs_v2_controls": masvs_ids,
                           "candidate_gdes_controls": MASVS_TO_GDES.get(group, []), "cwe": (d.get("mappings") or {}).get("cwe", []),
                           "maswe_beta_ids": norm_list((d.get("mappings") or {}).get("maswe-beta")),
                           "source_path": f["path"], "source_blob_sha": f["sha"]})
    maswe_by_id = {r["id"]: r for r in maswe_rows}
    beta_to_stable = defaultdict(list)
    for weakness in maswe_rows:
        for beta_id in weakness["maswe_beta_ids"]:
            beta_to_stable[str(beta_id)].append(weakness["id"])
    beta_asset_url = "https://github.com/OWASP/maswe/releases/download/v1.0.0/OWASP_MASWE.yaml"
    beta_asset_bytes = get(beta_asset_url)
    beta_asset_doc = yaml.safe_load(beta_asset_bytes.decode("utf-8"))
    (OUT / "OWASP_MASWE_v1.0.0_BETA_MAPPING_SOURCE.yaml").write_bytes(beta_asset_bytes)
    asset_weaknesses = beta_asset_doc.get("weaknesses", {}) if isinstance(beta_asset_doc, dict) else {}
    asset_beta_to_stable = defaultdict(list)
    for stable_id, entry in asset_weaknesses.items():
        for beta_id in norm_list((entry.get("mappings") or {}).get("maswe-beta")):
            asset_beta_to_stable[str(beta_id)].append(stable_id)
    frontmatter_beta_to_stable = {k: sorted(set(v)) for k, v in beta_to_stable.items()}
    beta_to_stable = asset_beta_to_stable
    beta_asset_sha256 = sha256(beta_asset_bytes)
    manifest["maswe_beta_mapping_asset"] = {
        "url": beta_asset_url, "sha256": beta_asset_sha256,
        "root_type": type(beta_asset_doc).__name__,
        "root_keys": list(beta_asset_doc.keys()) if isinstance(beta_asset_doc, dict) else [],
        "stable_weakness_count": len(asset_weaknesses),
        "beta_alias_id_count": len(beta_to_stable),
        "beta_0097_targets": beta_to_stable.get("MASWE-0097", []),
        "frontmatter_asset_mapping_differences": sorted(
            k for k in set(frontmatter_beta_to_stable) | set(beta_to_stable)
            if frontmatter_beta_to_stable.get(k, []) != sorted(set(beta_to_stable.get(k, [])))
        ),
    }
    beta_alias_rows = [{"beta_id": beta_id, "stable_maswe_ids": sorted(set(targets)),
                        "mapping_source": "OWASP MASWE v1.0.0 release asset mappings.maswe-beta",
                        "mapping_status": "SOURCE-MAPPED" if len(set(targets)) == 1 else "SOURCE-MAPPED — MULTIPLE TARGETS"}
                       for beta_id, targets in sorted(beta_to_stable.items())]
    write_csv("GDES_MASWE_BETA_ALIAS_CROSSWALK_v1.0.0.csv",
              ["beta_id", "stable_maswe_ids", "mapping_source", "mapping_status"], beta_alias_rows)
    print(json.dumps({"maswe_beta_asset_stable_weaknesses": len(asset_weaknesses),
                      "maswe_beta_asset_alias_ids": len(beta_to_stable),
                      "maswe_beta_0097_targets": beta_to_stable.get("MASWE-0097", []),
                      "maswe_beta_asset_sha256": beta_asset_sha256}, ensure_ascii=False))
    write_csv("GDES_MASWE_CATALOG_v1.0.0.csv",
              ["id", "title", "alias", "requirement", "platforms", "profiles", "threat", "attacks", "masvs_group",
               "masvs_v2_controls", "candidate_gdes_controls", "cwe", "maswe_beta_ids", "source_path", "source_blob_sha"], maswe_rows)

    # MASTG: retain both structured v2 tests and legacy test files; never silently drop old paths.
    mastg_files = [x for x in trees["MASTG"] if x["type"] == "blob" and re.search(r"MASTG-TEST-\d+\.md$", x["path"])]
    test_rows = []
    for f in sorted(mastg_files, key=lambda x: x["path"]):
        d = yaml_doc(text_of(SOURCES["MASTG"]["repo"], SOURCES["MASTG"]["ref"], f["path"]))
        parts = f["path"].split("/")
        platform = d.get("platform") or (parts[1] if len(parts) > 2 and parts[0] in ("tests", "tests-beta") else "")
        test_id = d.get("id") or Path(f["path"]).stem
        weakness = d.get("weakness", "")
        source_weakness_ids = [str(x) for x in norm_list(weakness) if str(x).strip()]
        stable_ids = []
        unmapped_beta_ids = []
        for source_id in source_weakness_ids:
            targets = [source_id] if source_id in maswe_by_id else beta_to_stable.get(source_id, [])
            if targets:
                stable_ids.extend(targets)
            else:
                unmapped_beta_ids.append(source_id)
        has_frontmatter = bool(d)
        test_rows.append({"test_id": test_id, "title": d.get("title", ""), "platform": platform,
                          "test_type": d.get("type", []), "source_weakness_ids": source_weakness_ids,
                          "stable_maswe_ids": sorted(set(stable_ids)), "unmapped_beta_ids": sorted(set(unmapped_beta_ids)),
                          "profiles": d.get("profiles", []), "apis": d.get("apis", []), "knowledge_ids": d.get("knowledge", []),
                          "best_practice_ids": d.get("best-practices", []),
                          "metadata_status": "STRUCTURED_WEAKNESS_LINK" if source_weakness_ids else ("STRUCTURED_NO_WEAKNESS_LINK" if has_frontmatter else "LEGACY_NO_FRONTMATTER"),
                          "source_path": f["path"], "source_blob_sha": f["sha"]})
    tests_by_weakness = defaultdict(list)
    for row in test_rows:
        for wid in row["stable_maswe_ids"]:
            tests_by_weakness[str(wid)].append(row)
    write_csv("GDES_MASTG_TEST_CATALOG_v2.0.0.csv",
              ["test_id", "title", "platform", "test_type", "source_weakness_ids", "stable_maswe_ids", "unmapped_beta_ids",
               "profiles", "apis", "knowledge_ids", "best_practice_ids", "metadata_status", "source_path", "source_blob_sha"], test_rows)

    relation_rows = []
    for wid, w in sorted(maswe_by_id.items()):
        linked = tests_by_weakness.get(wid, [])
        if not linked:
            relation_rows.append({"maswe_id": wid, "maswe_title": w["title"], "masvs_group": w["masvs_group"],
                                  "masvs_controls": w["masvs_v2_controls"], "mastg_test_id": "",
                                  "platform": "", "profiles": [], "test_type": [], "relation": "NO_MASTG_TEST_LINK_IN_PINNED_TREE",
                                  "gdes_controls_candidate": w["candidate_gdes_controls"]})
        for t in linked:
            source_refs = [source_id for source_id in t["source_weakness_ids"]
                           if wid in ([source_id] if source_id in maswe_by_id else beta_to_stable.get(source_id, []))]
            relation_rows.append({"maswe_id": wid, "maswe_title": w["title"], "maswe_beta_ids": w["maswe_beta_ids"],
                                  "masvs_group": w["masvs_group"], "masvs_controls": w["masvs_v2_controls"],
                                  "mastg_test_id": t["test_id"], "mastg_source_weakness_ids": source_refs,
                                  "platform": t["platform"], "profiles": t["profiles"], "test_type": t["test_type"],
                                  "relation": "MASTG_WEAKNESS_METADATA_RESOLVED_THROUGH_MASWE_V1_BETA_ALIAS",
                                  "gdes_controls_candidate": w["candidate_gdes_controls"]})
    unknown_weaknesses = sorted({str(w) for t in test_rows for w in t["unmapped_beta_ids"] if str(w).strip()})
    alias_finding_rows = []
    for beta_id, targets in sorted(beta_to_stable.items()):
        unique_targets = sorted(set(targets))
        if len(unique_targets) > 1:
            alias_finding_rows.append({"beta_id": beta_id, "stable_targets": unique_targets,
                                       "candidate_stable_id": "", "status": "MULTI_TARGET_SOURCE_MAPPING",
                                       "rationale": "The official v1.0.0 release asset maps this beta ID to multiple stable weaknesses; preserve all source targets pending reviewer disposition."})
    for beta_id in unknown_weaknesses:
        candidate = "MASWE-0051" if beta_id == "MASWE-0097" else ""
        rationale = ("MASTG-TEST-0324/0325 titles describe root/jailbreak detection and stable MASWE-0051 has the matching title; the release asset has no explicit alias for this beta ID. Candidate only; do not treat as source-mapped."
                     if candidate else "No stable target is present in the pinned MASWE v1.0.0 release asset.")
        alias_finding_rows.append({"beta_id": beta_id, "stable_targets": [], "candidate_stable_id": candidate,
                                   "status": "UNRESOLVED_SOURCE_BETA_ID", "rationale": rationale})
    write_csv("GDES_MASWE_BETA_ALIAS_FINDINGS_v1.0.0.csv",
              ["beta_id", "stable_targets", "candidate_stable_id", "status", "rationale"], alias_finding_rows)
    write_csv("GDES_MASWE_MASTG_TRACEABILITY_v1.0.0.csv",
              ["maswe_id", "maswe_title", "maswe_beta_ids", "masvs_group", "masvs_controls", "mastg_test_id",
               "mastg_source_weakness_ids", "platform", "profiles", "test_type", "relation", "gdes_controls_candidate"], relation_rows)

    # ASVS requirement-level catalogue and candidate mapping based on existing explicit section ranges.
    asvs_text = text_of(SOURCES["ASVS"]["repo"], SOURCES["ASVS"]["ref"], SOURCES["ASVS"]["data"])
    asvs_rows = []
    for row in csv.DictReader(io.StringIO(asvs_text)):
        rid = row.get("req_id", "")
        candidates = [gid for gid, ranges in ASVS_RANGES.items() if in_ranges(rid, ranges)]
        mapping_method = "SECTION_RANGE_CANDIDATE"
        if not candidates:
            candidates = ASVS_CHAPTER_TO_GDES.get(row.get("chapter_id", ""), [])
            mapping_method = "CHAPTER_CANDIDATE"
        asvs_rows.append({"requirement_id": "v5.0.0-" + rid, "chapter_id": row.get("chapter_id", ""),
                          "chapter_name": row.get("chapter_name", ""), "section_id": row.get("section_id", ""),
                          "section_name": row.get("section_name", ""), "requirement": row.get("req_description", ""),
                          "verification_level": row.get("L", ""), "candidate_gdes_controls": candidates,
                          "mapping_method": mapping_method,
                          "mapping_status": "CANDIDATE — REVIEW REQUIRED" if candidates else "UNMAPPED — REVIEW REQUIRED",
                          "source_path": SOURCES["ASVS"]["data"]})
    write_csv("GDES_ASVS_REQUIREMENT_CATALOG_v5.0.0.csv",
              ["requirement_id", "chapter_id", "chapter_name", "section_id", "section_name", "requirement",
               "verification_level", "candidate_gdes_controls", "mapping_method", "mapping_status", "source_path"], asvs_rows)

    # TCASVS requirement-level catalogue from all six tagged chapter source files.
    tcasvs_rows = []
    for chapter_path in SOURCES["TCASVS"]["chapters"]:
        content = text_of(SOURCES["TCASVS"]["repo"], SOURCES["TCASVS"]["ref"], chapter_path)
        chapter = re.search(r"\b(V[1-6])\b", Path(chapter_path).name).group(1)
        for line in content.splitlines():
            m = re.match(r"^\|\s*(V[1-6]\.\d+\.\d+)\s*\|\s*(.*?)\s*\|\s*([123])\s*\|\s*(.*?)\s*\|$", line)
            if m:
                candidates = TCASVS_TO_GDES.get(chapter, [])
                tcasvs_rows.append({"requirement_id": m.group(1), "description": m.group(2).strip(),
                                    "verification_level": m.group(3), "source": m.group(4).strip(),
                                    "chapter": chapter, "candidate_gdes_controls": candidates,
                                    "mapping_status": "CHAPTER-BASED CANDIDATE — REVIEW REQUIRED",
                                    "source_path": chapter_path})
    write_csv("GDES_TCASVS_REQUIREMENT_CATALOG_v5.0.0.csv",
              ["requirement_id", "chapter", "description", "verification_level", "source",
               "candidate_gdes_controls", "mapping_status", "source_path"], tcasvs_rows)

    # SAMM 2.2.0: every practice activity, maturity-level, and coverage question.
    samm_tree = trees["SAMM"]
    activity_files = [x for x in samm_tree if x["type"] == "blob" and x["path"].startswith("model/activities/") and x["path"].endswith(".yml")]
    question_files = [x for x in samm_tree if x["type"] == "blob" and x["path"].startswith("model/questions/") and x["path"].endswith(".yml")]
    questions_by_activity = defaultdict(list)
    questions = []
    for f in question_files:
        d = yaml.safe_load(text_of(SOURCES["SAMM"]["repo"], SOURCES["SAMM"]["ref"], f["path"])) or {}
        questions.append({"question_id": d.get("id", ""), "activity_guid": d.get("activity", ""), "question": d.get("text", ""),
                          "order": d.get("order", ""), "quality_criteria": d.get("quality", []),
                          "source_path": f["path"], "source_blob_sha": f["sha"]})
        questions_by_activity[d.get("activity", "")].append(questions[-1])
    samm_rows = []
    for f in activity_files:
        d = yaml.safe_load(text_of(SOURCES["SAMM"]["repo"], SOURCES["SAMM"]["ref"], f["path"])) or {}
        code = Path(f["path"]).stem[:4]
        qs = sorted(questions_by_activity.get(d.get("id", ""), []), key=lambda x: str(x["order"]))
        samm_rows.append({"activity_guid": d.get("id", ""), "activity_code": Path(f["path"]).stem,
                          "practice_code": code, "title": d.get("title", ""), "benefit": d.get("benefit", ""),
                          "short_description": d.get("shortDescription", ""), "long_description": d.get("longDescription", ""),
                          "results": d.get("results", ""), "metrics": d.get("metrics", ""), "costs": d.get("costs", ""),
                          "personnel": d.get("personnel", ""), "related_activities": d.get("relatedActivities", []),
                          "question_ids": [q["question_id"] for q in qs], "questions": [q["question"] for q in qs],
                          "candidate_gdes_controls": SAMM_TO_GDES.get(code, []),
                          "mapping_status": "PRACTICE/ACTIVITY CANDIDATE — REVIEW REQUIRED",
                          "source_path": f["path"], "source_blob_sha": f["sha"]})
    write_csv("GDES_SAMM_ACTIVITY_CATALOG_v2.2.0.csv",
              ["activity_guid", "activity_code", "practice_code", "title", "benefit", "short_description",
               "long_description", "results", "metrics", "costs", "personnel", "related_activities",
               "question_ids", "questions", "candidate_gdes_controls", "mapping_status", "source_path", "source_blob_sha"], samm_rows)
    write_csv("GDES_SAMM_QUESTION_CATALOG_v2.2.0.csv",
              ["question_id", "activity_guid", "question", "order", "quality_criteria", "source_path", "source_blob_sha"], questions)

    # License snapshot: hash the exact license file bytes at each immutable source pin.
    license_rows = []
    for key, spec in SOURCES.items():
        data = raw(spec["repo"], spec["ref"], spec["license"])
        lower = data.decode("utf-8", errors="replace").lower()
        match = "CC-BY-SA-4.0" if ("attribution-sharealike 4.0" in lower or "cc-by-sa-4.0" in lower) else "UNVERIFIED"
        license_blob_sha = next(x["sha"] for x in trees[key] if x["path"] == spec["license"])
        license_rows.append({"framework": key, "version": spec["version"], "repository": spec["repo"],
                             "source_commit": spec["ref"], "license_path": spec["license"],
                             "license_blob_sha": license_blob_sha, "license_sha256": sha256(data), "license_spdx_candidate": match,
                             "verification_status": "SOURCE FILE VERIFIED" if match == "CC-BY-SA-4.0" else "LEGAL/LICENSING REVIEW REQUIRED",
                             "source_url": f"https://github.com/{spec['repo']}/blob/{spec['ref']}/{spec['license']}"})
    write_csv("GDES_UPSTREAM_LICENSE_SNAPSHOT_REGISTER_v1.0.csv",
              ["framework", "version", "repository", "source_commit", "license_path", "license_blob_sha", "license_sha256",
               "license_spdx_candidate", "verification_status", "source_url"], license_rows)

    # Manifest: counts and explicit gaps make source drift visible.
    duplicate_test_ids = [k for k, v in Counter(x["test_id"] for x in test_rows).items() if v > 1]
    manifest["sources"] = {k: {"repository": v["repo"], "version": v["version"], "commit": v["ref"]} for k, v in SOURCES.items()}
    manifest["counts"] = {"masvs_controls": len(masvs_rows), "maswe_weaknesses": len(maswe_rows),
                          "mastg_test_files": len(test_rows), "mastg_structured_weakness_tests": sum(1 for x in test_rows if x["source_weakness_ids"]),
                          "maswe_beta_alias_ids": len(beta_to_stable),
                          "maswe_beta_aliases_multi_target": sum(1 for v in beta_to_stable.values() if len(set(v)) > 1),
                          "maswe_mastg_relation_rows": len(relation_rows), "asvs_requirements": len(asvs_rows),
                          "tcasvs_requirements": len(tcasvs_rows), "samm_activities": len(samm_rows), "samm_questions": len(questions)}
    manifest["checks"] = {"maswe_missing_id_or_title": [x["source_path"] for x in maswe_rows if not x["id"] or not x["title"]],
                          "mastg_missing_id": [x["source_path"] for x in test_rows if not x["test_id"]],
                          "mastg_duplicate_ids": duplicate_test_ids, "mastg_unknown_weakness_refs": unknown_weaknesses,
                          "maswe_beta_aliases_with_multiple_targets": {k: sorted(set(v)) for k, v in beta_to_stable.items() if len(set(v)) > 1},
                          "maswe_beta_alias_findings": alias_finding_rows,
                          "maswe_without_test_link": [x["id"] for x in maswe_rows if not tests_by_weakness.get(x["id"])],
                          "maswe_without_test_link_release_note_expected": 36,
                          "maswe_without_test_link_count_delta": sum(1 for x in maswe_rows if not tests_by_weakness.get(x["id"])) - 36,
                          "asvs_unmapped_requirement_count": sum(1 for x in asvs_rows if not x["candidate_gdes_controls"]),
                          "license_rows_unverified": [x["framework"] for x in license_rows if x["verification_status"] != "SOURCE FILE VERIFIED"],
                          "samm_activity_without_questions": [x["activity_code"] for x in samm_rows if not x["question_ids"]]}
    (OUT / "GDES_SOURCE_EXTRACTION_MANIFEST_v1.0.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps({"counts": manifest["counts"], "checks": manifest["checks"]}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
