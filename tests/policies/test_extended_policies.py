"""
Unit tests for extended higher education policy engines:
Financial Aid SAP, Faculty Workload, Degree Audit, Academic Integrity,
Disability Accommodations, and International Student Visa Compliance.
"""
from decimal import Decimal
from django.test import SimpleTestCase

from apps.core.policies.financial_aid_policy import FinancialAidPolicy
from apps.core.policies.faculty_workload_policy import FacultyWorkloadPolicy
from apps.core.policies.degree_audit_policy import DegreeAuditPolicy
from apps.core.policies.academic_integrity_policy import AcademicIntegrityPolicy
from apps.core.policies.disability_accommodations_policy import DisabilityAccommodationsPolicy
from apps.core.policies.international_student_compliance import InternationalStudentCompliancePolicy


class FinancialAidPolicyTestCase(SimpleTestCase):
    def test_sap_meeting_all_standards(self):
        result = FinancialAidPolicy.evaluate_sap(
            degree_level='BS',
            cumulative_gpa=Decimal('3.20'),
            attempted_credits=Decimal('60.0'),
            completed_credits=Decimal('54.0'),
            program_required_credits=Decimal('120.0')
        )
        self.assertTrue(result.is_eligible)
        self.assertEqual(result.status, FinancialAidPolicy.STATUS_MEETING)
        self.assertTrue(result.qualitative_pass)
        self.assertTrue(result.quantitative_pass)
        self.assertTrue(result.maximum_timeframe_pass)
        self.assertEqual(result.completion_rate, Decimal('90.00'))

    def test_sap_first_term_failure_warning(self):
        # Undergrad GPA 1.80 < 2.00, first time
        result = FinancialAidPolicy.evaluate_sap(
            degree_level='BS',
            cumulative_gpa=Decimal('1.80'),
            attempted_credits=Decimal('30.0'),
            completed_credits=Decimal('24.0'),
            program_required_credits=Decimal('120.0'),
            previous_status=FinancialAidPolicy.STATUS_MEETING
        )
        self.assertTrue(result.is_eligible)
        self.assertEqual(result.status, FinancialAidPolicy.STATUS_WARNING)

    def test_sap_consecutive_failure_suspension_and_appeal(self):
        # Second consecutive failure without appeal -> suspension
        result = FinancialAidPolicy.evaluate_sap(
            degree_level='BS',
            cumulative_gpa=Decimal('1.70'),
            attempted_credits=Decimal('45.0'),
            completed_credits=Decimal('20.0'),
            program_required_credits=Decimal('120.0'),
            previous_status=FinancialAidPolicy.STATUS_WARNING,
            has_approved_appeal=False
        )
        self.assertFalse(result.is_eligible)
        self.assertEqual(result.status, FinancialAidPolicy.STATUS_SUSPENSION)

        # Approved appeal with academic plan
        result_plan = FinancialAidPolicy.evaluate_sap(
            degree_level='BS',
            cumulative_gpa=Decimal('1.70'),
            attempted_credits=Decimal('45.0'),
            completed_credits=Decimal('20.0'),
            program_required_credits=Decimal('120.0'),
            previous_status=FinancialAidPolicy.STATUS_WARNING,
            has_approved_appeal=True,
            is_on_academic_plan=True
        )
        self.assertTrue(result_plan.is_eligible)
        self.assertEqual(result_plan.status, FinancialAidPolicy.STATUS_ACADEMIC_PLAN)

    def test_sap_maximum_timeframe_exceeded(self):
        # 120 credit program * 1.5 = 180 max allowed
        result = FinancialAidPolicy.evaluate_sap(
            degree_level='BS',
            cumulative_gpa=Decimal('3.50'),
            attempted_credits=Decimal('185.0'),
            completed_credits=Decimal('150.0'),
            program_required_credits=Decimal('120.0')
        )
        self.assertFalse(result.is_eligible)
        self.assertFalse(result.maximum_timeframe_pass)
        self.assertEqual(result.status, FinancialAidPolicy.STATUS_SUSPENSION)

    def test_pell_grant_proration(self):
        # Full time 12+ credits
        res_full = FinancialAidPolicy.calculate_pell_grant(
            scheduled_award=Decimal('7395.00'),
            enrolled_credits=15,
            student_aid_index=Decimal('0.00')
        )
        self.assertTrue(res_full['eligible'])
        self.assertEqual(res_full['term_disbursement'], Decimal('3697.50'))
        self.assertEqual(res_full['enrollment_intensity_pct'], Decimal('100.0'))

        # Half time 6 credits
        res_half = FinancialAidPolicy.calculate_pell_grant(
            scheduled_award=Decimal('7395.00'),
            enrolled_credits=6,
            student_aid_index=Decimal('0.00')
        )
        self.assertTrue(res_half['eligible'])
        self.assertEqual(res_half['term_disbursement'], Decimal('1848.75'))

        # Exceeded LEU cap (600%)
        res_capped = FinancialAidPolicy.calculate_pell_grant(
            scheduled_award=Decimal('7395.00'),
            enrolled_credits=12,
            student_aid_index=Decimal('0.00'),
            lifetime_eligibility_used_percent=Decimal('600.0')
        )
        self.assertFalse(res_capped['eligible'])


class FacultyWorkloadPolicyTestCase(SimpleTestCase):
    def test_course_workload_calculation(self):
        # 3 credit lecture, 0 lab
        wu_lecture = FacultyWorkloadPolicy.calculate_course_workload_units(
            credit_hours=3,
            contact_hours_lecture=3,
            contact_hours_lab=0,
            is_graduate=False,
            enrolled_students=25
        )
        self.assertEqual(wu_lecture, Decimal('3.00'))

        # Graduate 3 credit lecture with 3 hour lab
        wu_grad_lab = FacultyWorkloadPolicy.calculate_course_workload_units(
            credit_hours=4,
            contact_hours_lecture=3,
            contact_hours_lab=3,
            is_graduate=True,
            enrolled_students=15
        )
        # (3*1.0 + 3*0.75) * 1.25 = 5.25 * 1.25 = 6.5625 -> 6.56
        self.assertEqual(wu_grad_lab, Decimal('6.56'))

        # Large lecture bump (> 100 students)
        wu_large = FacultyWorkloadPolicy.calculate_course_workload_units(
            credit_hours=3,
            contact_hours_lecture=3,
            contact_hours_lab=0,
            is_graduate=False,
            enrolled_students=120
        )
        self.assertEqual(wu_large, Decimal('4.00'))

    def test_faculty_term_workload_and_overload(self):
        courses = [
            {'credit_hours': 3, 'lecture_hours': 3, 'lab_hours': 0, 'is_graduate': False, 'enrolled_students': 30},
            {'credit_hours': 3, 'lecture_hours': 3, 'lab_hours': 0, 'is_graduate': False, 'enrolled_students': 30},
            {'credit_hours': 4, 'lecture_hours': 3, 'lab_hours': 3, 'is_graduate': False, 'enrolled_students': 20}
        ]
        summary = FacultyWorkloadPolicy.calculate_faculty_term_workload(
            faculty_rank='Associate Professor',
            courses=courses,
            undergrad_advisees_thesis=2,
            masters_thesis_students=2,
            phd_dissertation_chairs=1,
            administrative_role='Department Chair',
            base_annual_salary=Decimal('90000.00')
        )
        self.assertEqual(summary['status'], 'OVERLOAD')
        self.assertTrue(summary['total_workload_units'] > Decimal('12.0'))
        self.assertTrue(summary['overload_compensation'] > Decimal('0.0'))


class DegreeAuditPolicyTestCase(SimpleTestCase):
    def setUp(self):
        self.gened_all_met = {
            'COMMUNICATION': 6,
            'QUANTITATIVE': 6,
            'NATURAL_SCIENCES': 8,
            'HUMANITIES_ARTS': 6,
            'SOCIAL_BEHAVIORAL': 6,
            'GLOBAL_DIVERSITY': 3
        }
        self.core_reqs = {'CS101', 'CS102', 'CS201', 'CS301', 'CS401'}

    def test_bachelor_audit_success_summa_cum_laude(self):
        audit = DegreeAuditPolicy.audit_bachelor_degree(
            cumulative_gpa=Decimal('3.95'),
            major_gpa=Decimal('3.98'),
            earned_credits_institutional=100,
            earned_credits_transfer=24,
            gened_completed=self.gened_all_met,
            major_core_required_courses=self.core_reqs,
            major_core_completed_courses=self.core_reqs,
            major_elective_credits_required=15,
            major_elective_credits_completed=18,
            has_academic_integrity_violation=False
        )
        self.assertTrue(audit['is_cleared_for_graduation'])
        self.assertEqual(audit['latin_honors'], 'SUMMA_CUM_LAUDE')
        self.assertEqual(len(audit['deficiencies']), 0)

    def test_bachelor_audit_missing_requirements(self):
        audit = DegreeAuditPolicy.audit_bachelor_degree(
            cumulative_gpa=Decimal('2.40'),
            major_gpa=Decimal('2.30'),
            earned_credits_institutional=20,  # Below 30 credit residency
            earned_credits_transfer=80,
            gened_completed={'COMMUNICATION': 3},  # Missing gen ed
            major_core_required_courses=self.core_reqs,
            major_core_completed_courses={'CS101', 'CS102'},  # Missing 3 core courses
            major_elective_credits_required=15,
            major_elective_credits_completed=9
        )
        self.assertFalse(audit['is_cleared_for_graduation'])
        self.assertIsNone(audit['latin_honors'])
        self.assertTrue(len(audit['deficiencies']) >= 4)


class AcademicIntegrityPolicyTestCase(SimpleTestCase):
    def test_minor_violation(self):
        res = AcademicIntegrityPolicy.evaluate_violation(
            category=AcademicIntegrityPolicy.CAT_UNAUTHORIZED_COLLABORATION,
            prior_violation_count=0,
            grade_weight_percentage=5.0
        )
        self.assertEqual(res['level'], AcademicIntegrityPolicy.LEVEL_1_MINOR)
        self.assertFalse(res['transcript_notation'])

    def test_exam_cheating_escalation(self):
        res = AcademicIntegrityPolicy.evaluate_violation(
            category=AcademicIntegrityPolicy.CAT_EXAM_CHEATING,
            prior_violation_count=0,
            is_formal_exam=True,
            grade_weight_percentage=30.0
        )
        self.assertEqual(res['level'], AcademicIntegrityPolicy.LEVEL_3_MAJOR)
        self.assertTrue(res['transcript_notation'])
        self.assertTrue(res['requires_board_hearing'])

    def test_contract_cheating_egregious(self):
        res = AcademicIntegrityPolicy.evaluate_violation(
            category=AcademicIntegrityPolicy.CAT_CONTRACT_CHEATING,
            prior_violation_count=0,
            is_commercial_or_proxy=True
        )
        self.assertEqual(res['level'], AcademicIntegrityPolicy.LEVEL_4_EGREGIOUS)
        self.assertTrue(res['transcript_notation'])


class DisabilityAccommodationsPolicyTestCase(SimpleTestCase):
    def test_exam_duration_time_and_a_half(self):
        result = DisabilityAccommodationsPolicy.calculate_exam_duration(
            standard_duration_minutes=60,
            accommodation_codes=['EXTENDED_EXAM_TIME_1_5X', 'DISTRACTION_REDUCED_ROOM']
        )
        self.assertEqual(result['adjusted_minutes'], 90)
        self.assertTrue(result['requires_separate_testing_room'])

    def test_exam_duration_double_time(self):
        result = DisabilityAccommodationsPolicy.calculate_exam_duration(
            standard_duration_minutes=120,
            accommodation_codes=['EXTENDED_EXAM_TIME_2_0X', 'SCREEN_READER_COMPATIBLE']
        )
        self.assertEqual(result['adjusted_minutes'], 240)
        self.assertTrue(result['requires_assistive_technology'])


class InternationalStudentCompliancePolicyTestCase(SimpleTestCase):
    def test_undergrad_f1_fulltime_compliance(self):
        # 9 in-person + 3 online = 12 qualifying
        res = InternationalStudentCompliancePolicy.evaluate_enrollment_compliance(
            visa_type='F-1',
            degree_level='BS',
            in_person_credits=9,
            online_credits=3
        )
        self.assertTrue(res['is_compliant'])
        self.assertEqual(res['status'], 'IN_STATUS')

    def test_undergrad_f1_excessive_online_credits(self):
        # 6 in-person + 6 online -> only 3 online countable -> 9 qualifying < 12
        res = InternationalStudentCompliancePolicy.evaluate_enrollment_compliance(
            visa_type='F-1',
            degree_level='BS',
            in_person_credits=6,
            online_credits=6
        )
        self.assertFalse(res['is_compliant'])
        self.assertEqual(res['status'], 'SEVIS_STATUS_JEOPARDY')

    def test_f1_medical_reduced_course_load(self):
        res = InternationalStudentCompliancePolicy.evaluate_enrollment_compliance(
            visa_type='F-1',
            degree_level='MS',
            in_person_credits=3,
            online_credits=0,
            approved_rcl_reason='DOCUMENTED_MEDICAL_CONDITION'
        )
        self.assertTrue(res['is_compliant'])
        self.assertEqual(res['status'], 'AUTHORIZED_RCL')
