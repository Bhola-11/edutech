"""
Automated unit tests for enterprise services across accounts, institutions, courses, enrollments, and profiles.
"""
from decimal import Decimal
from datetime import time
from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model

from apps.accounts.services.mfa_service import MFAService
from apps.institutions.services.facilities_booking_service import FacilitiesBookingService
from apps.courses.services.clo_plo_matrix_service import LearningOutcomesMatrixService
from apps.courses.services.syllabus_generator_service import SyllabusGeneratorService
from apps.enrollments.services.waitlist_service import WaitlistPriorityService
from apps.enrollments.services.prerequisite_validation_service import PrerequisiteValidationService
from apps.profiles.services.portfolio_service import PortfolioVerificationService
from apps.profiles.services.advisor_assignment_service import AdvisorAssignmentService


class MFAServiceTestCase(SimpleTestCase):
    def test_secret_generation_and_totp_cycle(self):
        secret = MFAService.generate_secret()
        self.assertTrue(len(secret) >= 16)

        # Generate token
        token = MFAService.generate_totp_token(secret)
        self.assertEqual(len(token), 6)
        self.assertTrue(token.isdigit())

        # Verify token
        is_valid = MFAService.verify_totp(secret, token, window=1)
        self.assertTrue(is_valid)

        # Invalid token
        self.assertFalse(MFAService.verify_totp(secret, "9999999", window=1))

    def test_provisioning_uri(self):
        secret = MFAService.generate_secret()
        uri = MFAService.generate_provisioning_uri("student@edutech.edu", secret)
        self.assertTrue(uri.startswith("otpauth://totp/"))
        self.assertIn("secret=", uri)

    def test_backup_recovery_codes(self):
        codes = MFAService.generate_backup_recovery_codes()
        self.assertEqual(len(codes), 10)
        self.assertTrue(all("-" in c for c in codes))


class FacilitiesBookingServiceTestCase(SimpleTestCase):
    def test_time_slot_conflict_detection(self):
        # Overlapping slots: 10:00-11:30 and 11:00-12:00 -> conflict
        has_conflict = FacilitiesBookingService.check_time_slot_conflict(
            time(10, 0), time(11, 30),
            time(11, 0), time(12, 0)
        )
        self.assertTrue(has_conflict)

        # Non-overlapping slots: 09:00-10:00 and 10:00-11:00 -> no conflict
        no_conflict = FacilitiesBookingService.check_time_slot_conflict(
            time(9, 0), time(10, 0),
            time(10, 0), time(11, 0)
        )
        self.assertFalse(no_conflict)


class LearningOutcomesMatrixServiceTestCase(SimpleTestCase):
    def test_accreditation_coverage_evaluation(self):
        mappings = [
            {'mapped_outcomes': ['SO_1', 'SO_2'], 'blooms_level': 'APPLYING'},
            {'mapped_outcomes': ['SO_1', 'SO_3'], 'blooms_level': 'ANALYZING'},
            {'mapped_outcomes': ['SO_4', 'SO_5'], 'blooms_level': 'EVALUATING'},
            {'mapped_outcomes': ['SO_6', 'SO_7'], 'blooms_level': 'CREATING'},
        ]
        result = LearningOutcomesMatrixService.evaluate_curriculum_coverage(mappings)
        self.assertEqual(result['total_mapped_elements'], 4)
        self.assertTrue(result['is_fully_accredited'])
        self.assertEqual(len(result['uncovered_outcomes']), 0)
        self.assertEqual(result['accreditation_readiness_score'], 100.0)


class SyllabusGeneratorServiceTestCase(SimpleTestCase):
    def test_standard_syllabus_generation(self):
        syllabus = SyllabusGeneratorService.generate_standard_syllabus(
            course_code='CS101',
            course_title='Introduction to Computer Science',
            credit_hours=4,
            department_name='Computer Science',
            instructor_name='Dr. Alan Turing',
            instructor_email='a.turing@edutech.edu',
            office_hours='Mon/Wed 2:00-4:00 PM',
            prerequisites=[],
            course_description='Foundations of computation and programming.',
            weekly_topics=[f"Topic {i}" for i in range(1, 15)],
            textbooks=['Introduction to Algorithms, CLRS']
        )
        self.assertEqual(syllabus['course_code'], 'CS101')
        self.assertEqual(len(syllabus['schedule']), 14)
        self.assertEqual(len(syllabus['grading_breakdown']), 5)
        total_weight = sum(item['weight_percentage'] for item in syllabus['grading_breakdown'])
        self.assertEqual(total_weight, 100)


class WaitlistPriorityServiceTestCase(SimpleTestCase):
    def test_waitlist_priority_ranking(self):
        entries = [
            {'name': 'Frosh', 'year_level': 1, 'is_degree_requirement': False, 'is_graduating_senior': False, 'cumulative_gpa': 3.2, 'days_on_waitlist': 2},
            {'name': 'Senior Major', 'year_level': 4, 'is_degree_requirement': True, 'is_graduating_senior': True, 'cumulative_gpa': 3.8, 'days_on_waitlist': 5},
            {'name': 'Junior Major', 'year_level': 3, 'is_degree_requirement': True, 'is_graduating_senior': False, 'cumulative_gpa': 3.5, 'days_on_waitlist': 4}
        ]
        ranked = WaitlistPriorityService.rank_waitlist_entries(entries)
        self.assertEqual(ranked[0]['name'], 'Senior Major')
        self.assertEqual(ranked[0]['waitlist_position'], 1)
        self.assertEqual(ranked[2]['name'], 'Frosh')
        self.assertEqual(ranked[2]['waitlist_position'], 3)


class PrerequisiteValidationServiceTestCase(SimpleTestCase):
    def test_prerequisite_grade_enforcement(self):
        # CS101 required with min grade C (2.0)
        # Student earned C- (1.7) -> ineligible
        student_history = {'CS101': 'C-'}
        prereqs = [{'code': 'CS101', 'min_grade': 'C'}]
        result = PrerequisiteValidationService.validate_enrollment_eligibility(
            student_completed_courses=student_history,
            course_prerequisites=prereqs,
            currently_enrolled_courses=set()
        )
        self.assertFalse(result['eligible'])
        self.assertEqual(len(result['insufficient_grades']), 1)

    def test_corequisite_check(self):
        # Physics 1 requires Physics 1 Lab corequisite
        student_history = {'MATH101': 'B'}
        prereqs = [{'code': 'MATH101', 'min_grade': 'C'}]
        coreqs = ['PHYS101L']

        # Not enrolled in lab -> ineligible
        res_fail = PrerequisiteValidationService.validate_enrollment_eligibility(
            student_completed_courses=student_history,
            course_prerequisites=prereqs,
            currently_enrolled_courses=set(),
            course_corequisites=coreqs
        )
        self.assertFalse(res_fail['eligible'])

        # Enrolled concurrently in lab -> eligible
        res_pass = PrerequisiteValidationService.validate_enrollment_eligibility(
            student_completed_courses=student_history,
            course_prerequisites=prereqs,
            currently_enrolled_courses={'PHYS101L'},
            course_corequisites=coreqs
        )
        self.assertTrue(res_pass['eligible'])

    def test_instructor_override_waiver(self):
        # Completely missing prereq, but has faculty waiver
        result = PrerequisiteValidationService.validate_enrollment_eligibility(
            student_completed_courses={},
            course_prerequisites=[{'code': 'CS301', 'min_grade': 'B'}],
            currently_enrolled_courses=set(),
            has_instructor_override=True
        )
        self.assertTrue(result['eligible'])


class PortfolioVerificationServiceTestCase(SimpleTestCase):
    def test_career_readiness_scoring(self):
        artifacts = [
            {'type': 'GITHUB_REPO', 'is_capstone': True},
            {'type': 'PDF_PAPER', 'is_capstone': False},
            {'type': 'PRESENTATION', 'is_capstone': False},
        ]
        skills = ['Python', 'Django', 'PostgreSQL', 'Docker', 'AWS']
        result = PortfolioVerificationService.evaluate_portfolio_readiness(
            student_id=101,
            artifacts=artifacts,
            verified_skills=skills
        )
        self.assertTrue(result['is_career_ready'])
        self.assertEqual(result['badge_awarded'], 'GOLD_DISTINCTION')
        self.assertEqual(result['readiness_score'], 100)


class AdvisorAssignmentServiceTestCase(SimpleTestCase):
    def test_matching_specialization_and_caseload(self):
        faculty = [
            {'id': 1, 'name': 'Dr. Smith', 'specializations': ['Machine Learning', 'Data Science'], 'current_advisees': 10},
            {'id': 2, 'name': 'Dr. Jones', 'specializations': ['Cybersecurity', 'Networks'], 'current_advisees': 5},
            {'id': 3, 'name': 'Dr. Davis', 'specializations': ['Machine Learning', 'Robotics'], 'current_advisees': 25},
        ]
        match = AdvisorAssignmentService.match_advisor(
            student_major_specialization='Machine Learning',
            available_faculty=faculty
        )
        self.assertTrue(match['assigned'])
        # Dr. Smith also has ML and fewer advisees than Dr. Davis (10 vs 25)
        self.assertEqual(match['advisor']['name'], 'Dr. Smith')
        self.assertTrue(match['is_specialization_match'])
