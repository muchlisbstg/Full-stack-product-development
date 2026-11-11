#!/usr/bin/env python3
"""Semantic source-policy checks for the HIG-01 F02 remediation overlay.

Reads inert UTF-8 text only. Never imports or executes candidate skill content.
"""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent
CANDIDATE_ROOT = ROOT / "scan-targets" / "HIG-01" / "F02-remediated"
SKILLS = (
    "higgsfield-generate/SKILL.md",
    "higgsfield-soul-id/SKILL.md",
    "higgsfield-product-photoshoot/SKILL.md",
    "higgsfield-brandkit/SKILL.md",
    "higgsfield-marketplace-cards/SKILL.md",
    "higgsfield-websites/SKILL.md",
    "higgsfield-faceless-video/SKILL.md",
    "higgsfield-video-explainer/SKILL.md",
    "higgsfield-youtube-thumbnail/SKILL.md",
)
REQUIRED = (
    "This skill does not grant the agent shell access.",
    "wait for explicit approval",
    "Do not use `sudo`",
    "Do not execute repository-provided scripts",
    "Prefer non-executing file inspection",
)

def frontmatter(text):
    if not text.startswith("---\n"):
        raise ValueError("frontmatter opening delimiter missing")
    end = text.find("\n---", 4)
    if end < 0:
        raise ValueError("frontmatter closing delimiter missing")
    return text[4:end]

def validate(text):
    fm = frontmatter(text)
    errors = []
    for line in fm.splitlines():
        key, sep, value = line.partition(":")
        if sep and key.strip() == "allowed-tools" and "bash" in value.lower():
            errors.append("broad Bash grant present")
    for phrase in REQUIRED:
        if phrase not in text:
            errors.append("required execution boundary missing: " + phrase)
    return errors

class F02PolicyTests(unittest.TestCase):
    def test_all_nine_candidate_skills_exist_and_pass(self):
        self.assertEqual(len(SKILLS), 9)
        for rel in SKILLS:
            path = CANDIDATE_ROOT / rel
            self.assertTrue(path.is_file(), f"missing candidate: {rel}")
            text = path.read_text(encoding="utf-8")
            self.assertEqual(validate(text), [], rel)

    def test_negative_fixture_rejects_bash_grant(self):
        sample = "---\nname: fixture\nallowed-tools: Bash\n---\n" + "\n".join(REQUIRED)
        self.assertIn("broad Bash grant present", validate(sample))

    def test_negative_fixture_rejects_missing_approval_boundary(self):
        sample = "---\nname: fixture\n---\n" + "\n".join(REQUIRED[1:])
        self.assertTrue(any("shell access" in e for e in validate(sample)))

    def test_frontmatter_is_required(self):
        with self.assertRaises(ValueError):
            frontmatter("name: fixture\n" + "\n".join(REQUIRED))

if __name__ == "__main__":
    unittest.main(verbosity=2)
