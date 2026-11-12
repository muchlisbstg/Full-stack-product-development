#!/usr/bin/env python3
"""Resolve and run one pinned Replica helper without relying on cwd-relative paths.

Set GDES_REPLICA_SKILLS_ROOT to the absolute root of the pinned upstream
checkout (the directory containing replica-design/, replica-diff/, etc.).
This wrapper itself performs no network access and starts no subprocess.
The selected upstream helper may read/write files according to its arguments.
"""
from pathlib import Path
import os
import runpy
import sys

ALLOWED = {
    "replica-design": {"contrast.py"},
    "replica-diff": {"imgdiff.py", "parity.py"},
    "replica-entrepreneur": {"reviews.py"},
    "replica-brand": {"sweep.py"},
    "replica-launch": {"listing.py"},
}

def check_root(root):
    missing = []
    for skill, helpers in ALLOWED.items():
        for helper in sorted(helpers):
            target = root / skill / helper
            if not target.is_file():
                missing.append(f"{skill}/{helper}")
    if missing:
        print("FAIL — missing helper(s): " + ", ".join(missing), file=sys.stderr)
        return 1
    print(f"PASS — {sum(map(len, ALLOWED.values()))} allowlisted helper files resolve from {root}")
    return 0

def main(argv):
    if len(argv) == 3 and argv[1] == "--check":
        return check_root(Path(argv[2]).expanduser().resolve())
    if len(argv) < 3:
        print(
            "usage: replica_skill_tool.py SKILL_NAME HELPER.py [HELPER_ARGS...]\n"
            "   or: replica_skill_tool.py --check UPSTREAM_SKILLS_ROOT",
            file=sys.stderr,
        )
        return 2

    skill, helper_name = argv[1], argv[2]
    if skill not in ALLOWED or helper_name not in ALLOWED[skill]:
        print("ERROR — helper is not in the GDES allowlist", file=sys.stderr)
        return 2

    configured_root = os.environ.get("GDES_REPLICA_SKILLS_ROOT")
    if not configured_root:
        print("ERROR — set GDES_REPLICA_SKILLS_ROOT to the absolute pinned skill collection root", file=sys.stderr)
        return 2

    root = Path(configured_root).expanduser().resolve()
    target = (root / skill / helper_name).resolve()
    if os.path.commonpath((str(root), str(target))) != str(root):
        print("ERROR — resolved helper escapes configured root", file=sys.stderr)
        return 2
    if not target.is_file():
        print(f"ERROR — helper not found: {target}", file=sys.stderr)
        return 2

    sys.argv = [str(target), *argv[3:]]
    runpy.run_path(str(target), run_name="__main__")
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
