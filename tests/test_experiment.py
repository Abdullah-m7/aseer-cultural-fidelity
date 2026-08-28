import unittest

from acf.experiment import FIDELITY_INSTRUCTION, response_id


class ExperimentTests(unittest.TestCase):
    def test_response_id_is_deterministic_and_condition_specific(self):
        a = response_id("C1", "m", "neutral", "en", 1)
        self.assertEqual(a, response_id("C1", "m", "neutral", "en", 1))
        self.assertNotEqual(a, response_id("C1", "m", "fidelity-aware", "en", 1))

    def test_fidelity_instruction_protects_provenance_and_discloses_adaptation(self):
        text = FIDELITY_INSTRUCTION.lower()
        self.assertIn("provenance", text)
        self.assertIn("adaptation", text)
        self.assertIn("do not invent", text)


if __name__ == "__main__":
    unittest.main()
