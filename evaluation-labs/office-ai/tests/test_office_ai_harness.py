import json
import tempfile
import unittest
from pathlib import Path

from tools.office_ai_harness import CANDIDATES, prepare, validate_package, verify


class OfficeAIHarnessTests(unittest.TestCase):
    def test_prepare_creates_three_valid_deterministic_fixtures(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "bundle"
            first = prepare(root)
            hashes = {name: data["sha256"] for name, data in first["fixtures"].items()}
            second = prepare(root)
            self.assertEqual(hashes, {
                name: data["sha256"] for name, data in second["fixtures"].items()
            })
            for name in ("common.docx", "common.xlsx", "common.pptx"):
                self.assertEqual(validate_package(root / "inputs" / name, name), [])

    def test_xlsx_formula_is_present(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            prepare(root)
            self.assertEqual(validate_package(root / "inputs" / "common.xlsx", "common.xlsx"), [])

    def test_missing_candidate_outputs_are_not_run_not_pass(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = root / "bundle"
            prepare(bundle)
            report = verify(bundle, root / "results")
            self.assertEqual(report["overall_status"], "NOT_RUN")
            self.assertEqual(set(report["candidates"]), set(CANDIDATES))
            for candidate in report["candidates"].values():
                for item in candidate.values():
                    self.assertEqual(item["status"], "NOT_RUN")

    def test_corrupt_output_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            bundle = root / "bundle"
            prepare(bundle)
            output = root / "results" / "pi-for-excel" / "common.xlsx"
            output.parent.mkdir(parents=True)
            output.write_text("not an OOXML package", encoding="utf-8")
            report = verify(bundle, root / "results")
            self.assertEqual(
                report["candidates"]["pi-for-excel"]["common.xlsx"]["status"], "FAIL"
            )


if __name__ == "__main__":
    unittest.main()
