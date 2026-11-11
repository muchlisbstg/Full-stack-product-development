#!/usr/bin/env python3
"""Static Agent Skills metadata and native discovery-layout validation.

This validator does not load or invoke Claude Code, Codex, or VS Code agents.
It copies the pinned skill folders into disposable native discovery paths and
checks metadata there. No upstream instructions or helper scripts are run.
"""
from pathlib import Path
import re
import shutil
import sys
import tempfile

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
PLATFORM_PATHS = {
    "Claude Code": Path(".claude/skills"),
    "Codex": Path(".agents/skills"),
    "VS Code Copilot": Path(".github/skills"),
}

def parse_frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("frontmatter must start on line 1")
    try:
        end = lines.index("---", 1)
    except ValueError:
        raise ValueError("closing frontmatter delimiter missing")
    name, description, in_description = None, [], False
    for line in lines[1:end]:
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip("\\"'")
            in_description = False
        elif line.startswith("description:"):
            in_description = True
            value = line.split(":", 1)[1].strip()
            if value and value not in (">", ">-", "|", "|-"):
                description.append(value.strip("\\"'"))
        elif in_description:
            if line.startswith(" ") or not line.strip():
                description.append(line.strip())
            else:
                in_description = False
    return name, " ".join(x for x in description if x).strip(), len(lines)

def validate_skill(folder, expected_name):
    file = folder / "SKILL.md"
    if not file.is_file():
        raise ValueError("SKILL.md missing")
    name, description, line_count = parse_frontmatter(file)
    if name != expected_name:
        raise ValueError(f"frontmatter name mismatch ({name!r})")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name or ""):
        raise ValueError("invalid Agent Skills name")
    if not description:
        raise ValueError("description missing")
    if len(description) > 1024:
        raise ValueError(f"description exceeds 1,024 characters ({len(description)})")
    return line_count, len(description)

def main(root):
    errors, warnings = [], []
    for skill in EXPECTED:
        try:
            line_count, desc_len = validate_skill(root / skill, skill)
            if line_count > 500:
                warnings.append(f"{skill}: SKILL.md exceeds Claude Code 500-line guidance")
            if skill in ("replica-backend", "replica-deploy"):
                text = (root / skill / "SKILL.md").read_text(encoding="utf-8")
                if "disable-model-invocation: true" not in text:
                    warnings.append(f"{skill}: upstream source lacks Claude manual-invocation guard")
        except Exception as exc:
            errors.append(f"{skill}: {exc}")
    for rel in EXPECTED_HELPERS:
        if not (root / rel).is_file():
            errors.append(f"expected utility missing: {rel}")

    if errors:
        print("FAIL — source metadata validation")
        for item in errors:
            print("ERROR:", item)
        return 1

    print(f"PASS — {len(EXPECTED)} upstream skills: required metadata, matching folder names, description length <= 1,024")
    print(f"PASS — {len(EXPECTED_HELPERS)} expected Python helper files present")

    copied = 0
    with tempfile.TemporaryDirectory(prefix="gdes-replica-layout-") as tmp:
        workspace = Path(tmp)
        for platform, relative_root in PLATFORM_PATHS.items():
            target_root = workspace / relative_root
            target_root.mkdir(parents=True, exist_ok=True)
            for skill in EXPECTED:
                shutil.copytree(root / skill, target_root / skill)
                validate_skill(target_root / skill, skill)
                copied += 1
            print(f"PASS — {platform}: {len(EXPECTED)} skills staged at {relative_root.as_posix()}")
    print(f"PASS — {copied} disposable discovery-layout copies validated across 3 platform paths")
    for item in warnings:
        print("WARN:", item)
    print("LIMITATION: directory-layout simulation only; no Claude Code, Codex, or VS Code agent runtime was loaded or invoked.")
    print("LIMITATION: no upstream Python helper was executed by this validator.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: validate_replica_skill_metadata.py UPSTREAM_REPOSITORY_ROOT", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(Path(sys.argv[1]).resolve()))
