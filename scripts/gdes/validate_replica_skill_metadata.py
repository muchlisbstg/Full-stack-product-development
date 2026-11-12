#!/usr/bin/env python3
"""Static Agent Skills metadata, adaptation and native discovery-layout validation.

No Claude Code, Codex or VS Code agent runtime is loaded. No upstream helper
script is executed. Native discovery checks use disposable directory copies.
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
ADAPTED = (
    "replica-backend", "replica-design", "replica-diff",
    "replica-entrepreneur", "replica-brand", "replica-launch",
    "replica-deploy",
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
    fields = {}
    for line in lines[1:end]:
        if ":" in line and not line.startswith(" ") and not line.startswith("\t"):
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
        if line.startswith("name:"):
            name = line.split(":", 1)[1].strip().strip(chr(34) + chr(39))
            in_description = False
        elif line.startswith("description:"):
            in_description = True
            value = line.split(":", 1)[1].strip()
            if value and value not in (">", ">-", "|", "|-"):
                description.append(value.strip(chr(34) + chr(39)))
        elif in_description:
            if line.startswith(" ") or not line.strip():
                description.append(line.strip())
            else:
                in_description = False
    return name, " ".join(x for x in description if x).strip(), len(lines), fields

def validate_skill(folder, expected_name):
    file = folder / "SKILL.md"
    if not file.is_file():
        raise ValueError("SKILL.md missing")
    name, description, line_count, fields = parse_frontmatter(file)
    if name != expected_name:
        raise ValueError(f"frontmatter name mismatch ({name!r})")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name or ""):
        raise ValueError("invalid Agent Skills name")
    if not description:
        raise ValueError("description missing")
    if len(description) > 1024:
        raise ValueError(f"description exceeds 1,024 characters ({len(description)})")
    return line_count, len(description), fields

def validate_adaptations(gdes_root):
    base = gdes_root / "docs/adaptations/replica-skill-gdes"
    errors = []
    for skill in ADAPTED:
        file = base / skill / "SKILL.md"
        if not file.is_file():
            errors.append(f"{skill}: GDES adapted SKILL.md missing")
            continue
        try:
            _, _, _, fields = parse_frontmatter(file)
            body = file.read_text(encoding="utf-8")
            if skill in ("replica-backend", "replica-deploy"):
                if fields.get("disable-model-invocation") != "true":
                    errors.append(f"{skill}: Claude manual-invocation guard missing")
                if "GDES invocation gate" not in body:
                    errors.append(f"{skill}: explicit GDES invocation gate missing")
            if skill in ("replica-design", "replica-diff", "replica-entrepreneur", "replica-brand", "replica-launch", "replica-deploy"):
                if "scripts/gdes/replica_skill_tool.py" not in body:
                    errors.append(f"{skill}: resolver path not used")
                if "python3 contrast.py" in body or "python3 parity.py" in body or "python3 imgdiff.py" in body or "python3 reviews.py" in body or "python3 sweep.py" in body or "python3 listing.py" in body:
                    errors.append(f"{skill}: bare helper invocation remains")
        except Exception as exc:
            errors.append(f"{skill}: adaptation validation error: {exc}")
    resolver = gdes_root / "scripts/gdes/replica_skill_tool.py"
    if not resolver.is_file():
        errors.append("GDES helper resolver missing")
    if errors:
        for error in errors:
            print("ERROR:", error)
        return False
    print(f"PASS — {len(ADAPTED)} GDES adaptation overlays validated")
    print("PASS — backend/deploy manual invocation guards present in adapted copies")
    print("PASS — helper-invoking adapted copies route through GDES resolver")
    return True

def main(root, gdes_root=None):
    errors, warnings = [], []
    for skill in EXPECTED:
        try:
            line_count, desc_len, _ = validate_skill(root / skill, skill)
            if line_count > 500:
                warnings.append(f"{skill}: SKILL.md exceeds Claude Code 500-line guidance")
            if skill in ("replica-backend", "replica-deploy"):
                text = (root / skill / "SKILL.md").read_text(encoding="utf-8")
                if "disable-model-invocation: true" not in text:
                    warnings.append(f"{skill}: upstream source lacks Claude manual-invocation guard; GDES overlay supplies it")
        except Exception as exc:
            errors.append(f"{skill}: {exc}")
    for rel in EXPECTED_HELPERS:
        if not (root / rel).is_file():
            errors.append(f"expected utility missing: {rel}")
    if errors:
        print("FAIL — upstream source metadata validation")
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
            print(f"PASS — {platform}: {len(EXPECTED)} static copies staged at {relative_root.as_posix()}")
    print(f"PASS — {copied} static discovery-layout copies validated across 3 platform paths")

    if gdes_root is not None and not validate_adaptations(gdes_root):
        return 1
    for item in warnings:
        print("WARN:", item)
    print("LIMITATION: directory-layout simulation only; no agent runtime was loaded or invoked.")
    print("LIMITATION: no upstream Python helper was executed by this validator.")
    return 0

if __name__ == "__main__":
    if len(sys.argv) not in (2, 3):
        print("usage: validate_replica_skill_metadata.py UPSTREAM_REPOSITORY_ROOT [GDES_BRANCH_ROOT]", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve() if len(sys.argv) == 3 else None))
