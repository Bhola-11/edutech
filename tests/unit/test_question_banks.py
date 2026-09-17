"""
Unit tests for Question Banks across all 15 disciplines.
"""
from django.test import SimpleTestCase
import importlib

BANK_MODULES = [
    'cs_questions',
    'ai_questions',
    'cybersecurity_questions',
    'data_science_questions',
    'electrical_questions',
    'mechanical_questions',
    'civil_questions',
    'biomedical_questions',
    'business_questions',
    'math_physics_questions',
    'humanities_questions',
    'psychology_questions',
    'legal_questions',
    'architecture_questions',
    'environmental_questions'
]


class QuestionBanksTestCase(SimpleTestCase):
    def test_all_question_banks_integrity(self):
        for mod_name in BANK_MODULES:
            with self.subTest(module=mod_name):
                mod = importlib.import_module(f"apps.assessments.banks.{mod_name}")
                self.assertTrue(hasattr(mod, 'QUESTION_BANK'))
                bank = mod.QUESTION_BANK
                self.assertEqual(len(bank), 150, f"{mod_name} should contain exactly 150 questions (10 per course).")

                # Verify first question structure
                first_q = bank[0]
                self.assertIn('course_code', first_q)
                self.assertIn('question_id', first_q)
                self.assertIn('question_type', first_q)
                self.assertIn('prompt_html', first_q)
                self.assertIn('blooms_level', first_q)

                # Test lookup helpers
                course_code = first_q['course_code']
                course_qs = mod.get_questions_for_course(course_code)
                self.assertEqual(len(course_qs), 10)

                lookup_q = mod.get_question_by_id(first_q['question_id'])
                self.assertEqual(lookup_q.get('question_id'), first_q['question_id'])
