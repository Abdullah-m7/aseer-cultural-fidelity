import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "stage002_annotator", ROOT / "scripts/annotate_stage_002_claude.py"
)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MODULE)


class AnnotationContractTests(unittest.TestCase):
    def setUp(self):
        self.row = {"response_id": "R-test", "case_id": "C-test"}
        self.cases = {
            "C-test": {
                "hard_invariants": [
                    {"invariant_id": "H1"},
                    {"invariant_id": "H2"},
                ]
            }
        }

    def base_annotation(self):
        return {
            "response_id": "R-test",
            "invariant_statuses": {"H1": "preserved", "H2": "omitted"},
            "cultural_claims_total": 1,
            "unsupported_cultural_claims": 0,
            "stereotype_intrusions": 0,
            "fabricated_provenance": False,
            "origin_reassignment": False,
            "material_adaptation": False,
            "adaptation_disclosed": False,
        }

    def test_valid_mapping_contract_passes(self):
        MODULE.validate(self.base_annotation(), self.row, self.cases)

    def test_list_shaped_invariant_statuses_is_rejected_cleanly(self):
        annotation = self.base_annotation()
        annotation["invariant_statuses"] = [{"invariant_id": "H1", "status": "preserved"}]
        with self.assertRaisesRegex(ValueError, "must be an object"):
            MODULE.validate(annotation, self.row, self.cases)


if __name__ == "__main__":
    unittest.main()
