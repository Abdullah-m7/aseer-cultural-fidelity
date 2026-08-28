import unittest

from acf.experiment import FIDELITY_INSTRUCTION, build_generation_prompt, response_id


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

    def test_grounding_adds_source_anchor_without_invariant_labels(self):
        case = {
            "prompt_en": "Do the task.",
            "source_anchor": "Aseer-specific fact.",
            "source": {"title": "Source", "authority": "Authority"},
        }
        neutral = build_generation_prompt(case, "en", "neutral")
        grounded = build_generation_prompt(case, "en", "grounded-neutral")
        self.assertEqual(neutral, "Do the task.")
        self.assertIn("Aseer-specific fact.", grounded)
        self.assertNotIn("invariant", grounded.lower())


if __name__ == "__main__":
    unittest.main()
