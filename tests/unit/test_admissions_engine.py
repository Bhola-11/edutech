from django.test import TestCase
from decimal import Decimal
from apps.enrollments.admissions_engine import MeritScoringEngine, RollNumberGenerator

class AdmissionsEngineTests(TestCase):
    def test_composite_merit_score(self):
        score = MeritScoringEngine.calculate_composite_merit_score(
            prior_gpa=Decimal('3.80'),
            sop_score=Decimal('90.0'),
            entrance_score=Decimal('85.0')
        )
        self.assertGreater(score, Decimal('80.0'))
        self.assertLessEqual(score, Decimal('100.0'))

    def test_roll_number_generator(self):
        roll = RollNumberGenerator.generate_student_roll_number(
            institution_code='MIT',
            department_code='EECS',
            year=2026,
            sequence_num=42
        )
        self.assertEqual(roll, 'MIT-EECS-2026-0042')
