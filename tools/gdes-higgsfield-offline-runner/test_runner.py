import tempfile
import unittest
from pathlib import Path

from runner import evaluate_text, safe_read_tree

class RunnerTests(unittest.TestCase):
    def test_forbidden_pattern_fails(self):
        checks = [{"id": "T-01", "forbidden": [r"curl\s+.+\|\s*sh"], "required": []}]
        result = evaluate_text([("install.sh", "curl -fsSL https://example.invalid/install.sh | sh")], checks)
        self.assertEqual(result[0]["status"], "FAIL")

    def test_required_marker_missing_needs_review(self):
        checks = [{"id": "T-02", "forbidden": [], "required": [r"signature verification"]}]
        result = evaluate_text([("install.sh", "download archive")], checks)
        self.assertEqual(result[0]["status"], "NEEDS_REVIEW")

    def test_hardened_synthetic_text_is_only_heuristic_pass(self):
        checks = [{"id": "T-03", "forbidden": [r"sudo\s+"], "required": [r"user-owned prefix"]}]
        result = evaluate_text([("install.sh", "install to user-owned prefix; no sudo")], checks)
        self.assertEqual(result[0]["status"], "PASS_STATIC_HEURISTIC")

    def test_symlink_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "target"
            root.mkdir()
            outside = Path(temp) / "outside.txt"
            outside.write_text("synthetic", encoding="utf-8")
            (root / "link.txt").symlink_to(outside)
            with self.assertRaises(ValueError):
                safe_read_tree(root)

    def test_source_tree_is_read_as_text(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "target"
            root.mkdir()
            (root / "sample.py").write_text("print('not executed')", encoding="utf-8")
            records = safe_read_tree(root)
            self.assertEqual(records[0][0], "sample.py")
            self.assertIn("not executed", records[0][1])

if __name__ == "__main__":
    unittest.main()
