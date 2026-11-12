import json
import tempfile
import unittest
from pathlib import Path

from tools.office_ai_harness import prepare
from tools.office_ai_quality_gate import (
    audit_evidence,
    compare_reproducibility,
    inspect_ooxml,
    sha256,
    verify_manifest,
    visual_review_template,
    xlsx_formula_snapshot,
)


class OfficeQualityGateTests(unittest.TestCase):
    def test_generated_ooxml_packages_pass_integrity(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            prepare(root)
            for name in ("common.xlsx", "common.docx", "common.pptx"):
                result = inspect_ooxml(root / "inputs" / name)
                self.assertEqual(result["status"], "PASS", result)

    def test_xlsx_formula_and_cached_value_are_captured(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            prepare(root)
            snapshot = xlsx_formula_snapshot(root / "inputs" / "common.xlsx")
            self.assertEqual(len(snapshot["formulas"]), 1)
            self.assertEqual(snapshot["formulas"][0]["formula"], "SUM(B2:B3)")
            self.assertEqual(snapshot["formulas"][0]["cached_value"], "25")

    def test_manifest_verification_detects_tampering(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "fixture.txt"
            target.write_text("fixture", encoding="utf-8")
            manifest = root / "SHA256SUMS"
            manifest.write_text(f"{sha256(target)}  fixture.txt\n", encoding="utf-8")
            report = verify_manifest(manifest, root)
            self.assertEqual(report["status"], "PASS", report)
            target.write_text("tampered", encoding="utf-8")
            self.assertEqual(verify_manifest(manifest, root)["status"], "FAIL")

    def test_reproducibility_gate_detects_changed_semantics(self):
        a = {"fixture_manifest_sha256": "a", "semantic_content_sha256": "same"}
        b = {"fixture_manifest_sha256": "a", "semantic_content_sha256": "changed"}
        self.assertEqual(compare_reproducibility(a, b)["status"], "FAIL")

    def test_evidence_audit_blocks_without_human_visual_signoff(self):
        with tempfile.TemporaryDirectory() as tmp:
            evidence = Path(tmp)
            report = audit_evidence(evidence)
            self.assertEqual(report["status"], "BLOCKED")
            self.assertFalse(report["candidate_execution_authorized"])

    def test_visual_review_template_is_pending_not_approved(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "visual-review.json"
            visual_review_template([{"path": "page-1.png", "sha256": "abc"}], path)
            data = json.loads(path.read_text(encoding="utf-8"))
            self.assertFalse(data["approved"])
            self.assertEqual(data["review_status"], "PENDING_HUMAN_REVIEW")


if __name__ == "__main__":
    unittest.main()
