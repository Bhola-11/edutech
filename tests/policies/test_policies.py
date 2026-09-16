from django.test import SimpleTestCase
from decimal import Decimal
from apps.core.policies.credit_transfer_policy import CreditTransferPolicy
from apps.core.policies.academic_standing_policy import AcademicStandingPolicy
from apps.core.policies.attendance_policy import AttendancePolicy
from apps.core.policies.graduation_clearance_policy import GraduationClearancePolicy

class AcademicPoliciesTests(SimpleTestCase):
    def test_credit_transfer_valid(self):
        res = CreditTransferPolicy.evaluate_course_transfer(
            external_course_title='Calculus I',
            external_credits=4.0,
            external_grade='A',
            syllabus_overlap_pct=85.0
        )
        self.assertTrue(res['is_approved'])
        self.assertEqual(res['awarded_credits'], Decimal('4.0'))

    def test_credit_transfer_low_grade(self):
        res = CreditTransferPolicy.evaluate_course_transfer(
            external_course_title='Calculus I',
            external_credits=4.0,
            external_grade='D',
            syllabus_overlap_pct=85.0
        )
        self.assertFalse(res['is_approved'])

    def test_credit_transfer_low_overlap(self):
        res = CreditTransferPolicy.evaluate_course_transfer(
            external_course_title='Calculus I',
            external_credits=4.0,
            external_grade='A',
            syllabus_overlap_pct=60.0
        )
        self.assertFalse(res['is_approved'])

    def test_academic_standing_honors(self):
        res = AcademicStandingPolicy.evaluate_academic_standing(
            cumulative_gpa=Decimal('3.95'),
            term_gpa=Decimal('3.92')
        )
        self.assertEqual(res['standing'], 'PRESIDENTS_HONORS')
        self.assertTrue(res['is_in_good_standing'])

    def test_academic_standing_probation(self):
        res = AcademicStandingPolicy.evaluate_academic_standing(
            cumulative_gpa=Decimal('1.85'),
            term_gpa=Decimal('1.80')
        )
        self.assertEqual(res['standing'], 'ACADEMIC_WARNING')
        self.assertFalse(res['is_in_good_standing'])

    def test_attendance_policy(self):
        res = AttendancePolicy.calculate_attendance_standing(
            total_sessions=40,
            attended_sessions=35
        )
        self.assertTrue(res['is_exam_eligible'])
        self.assertGreaterEqual(res['attendance_percentage'], Decimal('85.0'))

    def test_attendance_debarment(self):
        res = AttendancePolicy.calculate_attendance_standing(
            total_sessions=40,
            attended_sessions=20
        )
        self.assertFalse(res['is_exam_eligible'])
        self.assertEqual(res['status'], 'DEBARRED_ATTENDANCE_SHORTAGE')

    def test_graduation_clearance(self):
        res = GraduationClearancePolicy.evaluate_graduation_clearance(
            total_credits_earned=128,
            required_credits=120,
            cumulative_gpa=Decimal('3.92')
        )
        self.assertTrue(res['is_cleared_for_graduation'])
        self.assertEqual(res['honors_distinction'], 'Summa Cum Laude (Highest Honors)')
