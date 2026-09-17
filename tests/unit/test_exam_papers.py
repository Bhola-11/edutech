"""
Unit tests for Examination Papers (Midterms & Finals) across all 15 academic disciplines.
"""
from django.test import SimpleTestCase
import importlib

PAPER_MODULES = [
    'cs_papers',
    'ai_papers',
    'cybersecurity_papers',
    'data_science_papers',
    'electrical_papers',
    'mechanical_papers',
    'civil_papers',
    'biomedical_papers',
    'business_papers',
    'math_physics_papers',
    'humanities_papers',
    'psychology_papers',
    'legal_papers',
    'architecture_papers',
    'environmental_papers'
]


class ExamPapersTestCase(SimpleTestCase):
    def test_all_exam_paper_catalogs_integrity(self):
        for mod_name in PAPER_MODULES:
            with self.subTest(module=mod_name):
                mod = importlib.import_module(f"apps.examinations.papers.{mod_name}")
                self.assertTrue(hasattr(mod, 'EXAMINATION_PAPERS'))
                papers = mod.EXAMINATION_PAPERS
                self.assertEqual(len(papers), 15, f"{mod_name} should contain exactly 15 courses.")

                for p in papers:
                    self.assertIn('course_code', p)
                    self.assertIn('midterm_exam', p)
                    self.assertIn('final_exam', p)

                    # Check midterm
                    midterm = p['midterm_exam']
                    self.assertEqual(midterm['duration_minutes'], 90)
                    self.assertEqual(len(midterm['questions']), 5)
                    for q in midterm['questions']:
                        self.assertIn('problem_statement', q)
                        self.assertIn('model_solution', q)
                        self.assertIn('marking_rubric', q)

                    # Check final
                    final = p['final_exam']
                    self.assertEqual(final['duration_minutes'], 180)
                    self.assertEqual(len(final['questions']), 5)

                # Test lookup helper
                first_code = papers[0]['course_code']
                lookup = mod.get_papers_for_course(first_code)
                self.assertEqual(lookup.get('course_code'), first_code)
