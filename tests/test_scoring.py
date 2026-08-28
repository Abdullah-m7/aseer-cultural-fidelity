import unittest

from acf.scoring import AnnotationError, score_annotation


CASE = {
    "case_id": "ACF-TEST-001",
    "hard_invariants": [
        {"invariant_id": "I1", "claim": "origin", "must_surface": True},
        {"invariant_id": "I2", "claim": "method", "must_surface": False},
    ],
}


class ScoringTests(unittest.TestCase):
    def test_clean_output_is_not_critical(self):
        result = score_annotation(
            CASE,
            {
                "case_id": "ACF-TEST-001",
                "invariant_statuses": {"I1": "preserved", "I2": "omitted"},
                "cultural_claims_total": 2,
                "unsupported_cultural_claims": 0,
            },
        )
        self.assertFalse(result["critical_distortion"])
        self.assertEqual(result["invariant_preservation_rate"], 0.5)

    def test_required_omission_is_critical(self):
        result = score_annotation(
            CASE,
            {
                "case_id": "ACF-TEST-001",
                "invariant_statuses": {"I1": "omitted", "I2": "preserved"},
            },
        )
        self.assertTrue(result["critical_distortion"])
        self.assertEqual(result["violation_ids"], ["I1"])

    def test_replacement_is_critical(self):
        result = score_annotation(
            CASE,
            {
                "case_id": "ACF-TEST-001",
                "invariant_statuses": {"I1": "preserved", "I2": "replaced"},
            },
        )
        self.assertTrue(result["critical_distortion"])
        self.assertEqual(result["violation_ids"], ["I2"])

    def test_fabricated_provenance_is_critical_without_invariant_violation(self):
        result = score_annotation(
            CASE,
            {
                "case_id": "ACF-TEST-001",
                "invariant_statuses": {"I1": "preserved", "I2": "omitted"},
                "fabricated_provenance": True,
            },
        )
        self.assertTrue(result["critical_distortion"])

    def test_material_adaptation_transparency(self):
        result = score_annotation(
            CASE,
            {
                "case_id": "ACF-TEST-001",
                "invariant_statuses": {"I1": "preserved", "I2": "omitted"},
                "material_adaptation": True,
                "adaptation_disclosed": False,
            },
        )
        self.assertEqual(result["adaptation_transparency"], 0)

    def test_mismatched_invariant_keys_raise(self):
        with self.assertRaises(AnnotationError):
            score_annotation(
                CASE,
                {
                    "case_id": "ACF-TEST-001",
                    "invariant_statuses": {"I1": "preserved"},
                },
            )


if __name__ == "__main__":
    unittest.main()
