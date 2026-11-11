#!/usr/bin/env python3
"""GDES-REG-002 offline static screening runner.

Reads candidate source as inert text only. Does not import, execute, install, or
contact candidate code. Uses Python standard library only.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POLICY = ROOT / "policy.json"
EXTENSIONS = {".py", ".sh", ".ts", ".tsx", ".js", ".mjs", ".cjs", ".go", ".md", ".json", ".yml", ".yaml", ".toml", ".txt"}

def safe_read_tree(root: Path) -> list[tuple[str, str]]:
    base = root.resolve(strict=True)
    if not base.is_dir():
        raise ValueError(f"target is not a directory: {root}")
    records: list[tuple[str, str]] = []
    for path in sorted(base.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"symlink is not permitted in target tree: {path}")
        if not path.is_file() or path.suffix.lower() not in EXTENSIONS:
            continue
        resolved = path.resolve(strict=True)
        if base not in resolved.parents:
            raise ValueError(f"path escaped target root: {path}")
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            raise ValueError(f"non-UTF-8 source file: {path}") from exc
        records.append((path.relative_to(base).as_posix(), content))
    return records

def evaluate_text(records: list[tuple[str, str]], checks: list[dict]) -> list[dict]:
    corpus = "\n".join(f"\n/* FILE: {name} */\n{content}" for name, content in records)
    results = []
    for check in checks:
        forbidden = [p for p in check.get("forbidden", []) if re.search(p, corpus, re.I | re.M)]
        required = [p for p in check.get("required", []) if not re.search(p, corpus, re.I | re.M)]
        status = "FAIL" if forbidden else ("NEEDS_REVIEW" if required else "PASS_STATIC_HEURISTIC")
        results.append({
            "id": check["id"],
            "status": status,
            "forbidden_matches": forbidden,
            "missing_required_markers": required,
            "note": "Heuristic source scan only; manual semantic review and negative tests remain mandatory."
        })
    return results

def main() -> int:
    parser = argparse.ArgumentParser(description="Offline static screening; candidate code is never executed.")
    parser.add_argument("--targets", type=Path, default=ROOT / "targets", help="Directory containing HIG-01..HIG-04 subdirectories")
    parser.add_argument("--output", type=Path, default=ROOT / "results" / "latest.json")
    parser.add_argument("--self-test", action="store_true", help="Run harness self-tests against synthetic fixtures")
    args = parser.parse_args()

    if args.self_test:
        import unittest
        from test_runner import RunnerTests
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(RunnerTests)
        result = unittest.TextTestRunner(verbosity=2).run(suite)
        return 0 if result.wasSuccessful() else 1

    policy = json.loads(POLICY.read_text(encoding="utf-8"))
    all_results = []
    for candidate in policy["candidates"]:
        target = args.targets / candidate["id"]
        if not target.exists():
            all_results.append({"candidate": candidate["id"], "status": "NOT_RUN", "reason": "Target source directory missing."})
            continue
        try:
            records = safe_read_tree(target)
            checks = evaluate_text(records, candidate["checks"])
            status = "FAIL" if any(x["status"] == "FAIL" for x in checks) else (
                "NEEDS_REVIEW" if any(x["status"] == "NEEDS_REVIEW" for x in checks) else "PASS_STATIC_HEURISTIC"
            )
            all_results.append({"candidate": candidate["id"], "status": status, "files_scanned": len(records), "checks": checks})
        except Exception as exc:
            all_results.append({"candidate": candidate["id"], "status": "ERROR", "reason": str(exc)})
    payload = {
        "schema_version": "1.0",
        "runner": "GDES-REG-002-offline-static-screen",
        "policy_version": policy["policy_version"],
        "execution_mode": "inert-text-only; no candidate execution; no network; no dependency installation",
        "results": all_results,
        "release_gate": "BLOCKED" if any(x["status"] != "PASS_STATIC_HEURISTIC" for x in all_results) else "MANUAL_REVIEW_REQUIRED"
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, indent=2))
    return 0 if payload["release_gate"] != "BLOCKED" else 2

if __name__ == "__main__":
    raise SystemExit(main())
