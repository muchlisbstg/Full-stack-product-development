#!/usr/bin/env python3
"""Read-only structural validation for the pinned Replica Skill collection.

This validator checks the Agent Skills metadata contract and expected helper
inventory. It does not execute SKILL.md instructions or Python helper scripts.
"""
from pathlib import Path
import re
import sys

EXPECTED = (
    "replica-recon", "replica-architect", "replica-design", "replica-build",
    "replica-backend", "replica-test", "replica-diff", "replica-entrepreneur",
    "replica-brand", "replica-launch", "replica-deploy",
)
EXPECTED_HELPERS = (
    "replica-design/contrast.py",
    "replica-diff/imgdiff.py",
    "replica-diff/parity.py",
    "replica-entrepreneur/reviews.py",
    "replica-brand/sweep.py",
    "replica-launch/listing.py",
)

def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("frontmatter must start on line 1")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("closing frontmatter delimiter missing")
    block = lines[1:end]
    name = None
    description = []
    in_description = False
    for line in block:
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip("\"'")
            in_description = False
        elif line.startswith("description:"):
            in_description = True
            value = line.split(":", 1)[1].strip()
            if value and value not in (">", ">-", "|", "|-"):
                description.append(value.strip("\"'"))
        elif in_description:
            if line.startswith(" ") or not line.strip():
                description.append(line.strip())
            else:
                in_description = False
    return name, " ".join(x for x in description if x).strip(), text

def main(root):
    errors = []
    warnings = []
    for skill in EXPECTED:
        folder = root / skill
        file = folder / "SKILL.md"
        if not file.is_file():
            errors.append(f"{skill}: SKILL.md missing")
            continue
        try:
            name, description, body = parse_frontmatter(file)
        except Exception as exc:
            errors.append(f"{skill}: frontmatter error: {exc}")
            continue
        if name != skill:
            errors.append(f"{skill}: frontmatter name mismatch ({name!r})")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", name or ""):
            errors.append(f"{skill}: invalid Agent Skills name")
        if not description:
            errors.append(f"{skill}: description missing")
        if len(description) > 1024:
            errors.append(f"{skill}: description exceeds VS Code 1024-char limit")
        if len(body.splitlines()) > 500:
            warnings.append(f"{skill}: SKILL.md exceeds Claude Code 500-line guidance")
        if skill in ("replica-backend", "replica-deploy") and "disable-model-invocation: true" not in body:
            warnings.append(f"{skill}: side-effect-capable workflow has no disable-model-invocation: true guard")
    for rel in EXPECTED_HELPERS:
        if not (root / rel).is_file():
            errors.append(f"expected utility missing: {rel}")
    if errors:
        print("FAIL — structural validation")
        for item in errors:
            print("ERROR:", item)
        return 1
    print(f"PASS — {len(EXPECTED)} skill folders have required name/description metadata and matching folder names")
    print(f"PASS — {len(EXPECTED_HELPERS)} expected Python helper files are present")
    for item in warnings:
        print("WARN:", item)
    print("NOTE: this is a structural check only; no agent runtime, skill instruction, or helper execution is performed here.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: validate_replica_skill_metadata.py UPSTREAM_REPOSITORY_ROOT", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
