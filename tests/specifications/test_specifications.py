"""
Automated unit tests for course specifications across all 15 academic disciplines.
"""
from django.test import SimpleTestCase
import importlib

SPEC_MODULES = [
    'cs_specifications',
    'ai_specifications',
    'cybersecurity_specifications',
    'data_science_specifications',
    'electrical_specifications',
    'mechanical_specifications',
    'civil_specifications',
    'biomedical_specifications',
    'business_specifications',
    'math_physics_specifications',
    'humanities_specifications',
    'psychology_specifications',
    'legal_specifications',
    'architecture_specifications',
    'environmental_specifications'
]


class CourseSpecificationsTestCase(SimpleTestCase):
    def test_all_specification_modules_integrity(self):
        for mod_name in SPEC_MODULES:
            with self.subTest(module=mod_name):
                mod = importlib.import_module(f"apps.courses.specifications.{mod_name}")
                self.assertTrue(hasattr(mod, 'COURSE_SPECIFICATIONS'))
                specs = mod.COURSE_SPECIFICATIONS
                self.assertEqual(len(specs), 15, f"{mod_name} should contain exactly 15 courses.")

                for course in specs:
                    self.assertIn('code', course)
                    self.assertIn('title', course)
                    self.assertIn('laboratories', course)
                    self.assertIn('term_projects', course)
                    self.assertIn('exam_problems', course)

                    # Check laboratories count and structure
                    self.assertEqual(len(course['laboratories']), 4)
                    for lab in course['laboratories']:
                        self.assertIn('lab_number', lab)
                        self.assertIn('title', lab)
                        self.assertIn('procedure_steps', lab)
                        self.assertIn('rubric', lab)

                    # Check term projects count and structure
                    self.assertEqual(len(course['term_projects']), 2)
                    for proj in course['term_projects']:
                        self.assertIn('project_number', proj)
                        self.assertIn('title', proj)
                        self.assertIn('milestones', proj)
                        self.assertIn('rubric', proj)

                    # Check exam problems
                    self.assertEqual(len(course['exam_problems']), 4)

                # Test helper functions
                first_code = specs[0]['code']
                lookup = mod.get_course_specification(first_code)
                self.assertEqual(lookup.get('code'), first_code)

                all_codes = mod.list_all_course_codes()
                self.assertEqual(len(all_codes), 15)
