from django.test import SimpleTestCase
from apps.courses.rubrics import RUBRIC_TEMPLATES, RUBRICS_BY_CODE

class AssessmentRubricsTests(SimpleTestCase):
    def test_rubric_templates_exist(self):
        self.assertGreaterEqual(len(RUBRIC_TEMPLATES), 5)
        self.assertIn('PROGRAMMING_LAB', RUBRICS_BY_CODE)
        self.assertIn('ENGINEERING_DESIGN', RUBRICS_BY_CODE)

    def test_rubric_weights_sum_to_100(self):
        for rubric in RUBRIC_TEMPLATES:
            total_weight = sum(c['weight_percentage'] for c in rubric['criteria'])
            self.assertEqual(total_weight, 100, f"Rubric {rubric['code']} criteria weights do not sum to 100")

    def test_rubric_scales(self):
        for rubric in RUBRIC_TEMPLATES:
            for crit in rubric['criteria']:
                scales = crit['scale_levels']
                self.assertIn('EXEMPLARY', scales)
                self.assertIn('PROFICIENT', scales)
                self.assertIn('DEVELOPING', scales)
                self.assertIn('UNSATISFACTORY', scales)
                self.assertEqual(scales['EXEMPLARY']['points_multiplier'], 1.0)
