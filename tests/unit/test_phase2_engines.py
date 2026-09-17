"""
Unit tests for Phase 2 engines: Code Execution, Paper Generator, Proctoring Security,
Exam Timer, Plagiarism Detection, Peer Review Allocation, Gradebook, Grade Curving, and Certificate PDF/Crypto.
"""
from datetime import datetime, timedelta
from django.utils import timezone
from django.test import SimpleTestCase

from apps.assessments.services.code_runner_service import CodeExecutionService
from apps.assessments.services.question_generator_service import QuestionPaperGeneratorService
from apps.examinations.services.proctoring_service import ProctoringSecurityService
from apps.examinations.services.exam_timer_service import ExamTimerService
from apps.assignments.services.plagiarism_service import PlagiarismDetectionService
from apps.assignments.services.peer_review_service import PeerReviewDistributionService
from apps.grading.services.gradebook_service import GradebookService
from apps.grading.services.curving_service import GradeCurvingService
from apps.certificates.services.crypto_verification_service import CertificateCryptoService
from apps.certificates.services.pdf_certificate_service import PDFCertificateGeneratorService


class CodeExecutionServiceTestCase(SimpleTestCase):
    def test_python_code_execution_success(self):
        code = "print('Hello, World!')"
        res = CodeExecutionService.execute_python_code(code, expected_output="Hello, World!")
        self.assertTrue(res['passed'])
        self.assertEqual(res['output'], "Hello, World!")

    def test_python_code_execution_error(self):
        code = "raise ValueError('Invalid argument')"
        res = CodeExecutionService.execute_python_code(code)
        self.assertFalse(res['passed'])
        self.assertIsNotNone(res['error'])

    def test_evaluate_all_test_cases(self):
        code = "def add(a, b): return a + b\nprint(add(2, 3))"
        test_cases = [
            {'id': 1, 'expected_output': '5', 'points': 10, 'is_hidden': False},
            {'id': 2, 'expected_output': '6', 'points': 10, 'is_hidden': True}  # will fail
        ]
        res = CodeExecutionService.evaluate_all_test_cases(code, test_cases)
        self.assertFalse(res['all_passed'])
        self.assertEqual(res['total_points_earned'], 10)
        self.assertEqual(res['max_total_points'], 20)
        self.assertEqual(res['score_percentage'], 50.0)


class QuestionGeneratorTestCase(SimpleTestCase):
    def test_balanced_paper_generation(self):
        questions = [
            {'id': i, 'title': f'Q{i}', 'difficulty': 'EASY' if i < 4 else ('MEDIUM' if i < 8 else 'HARD')}
            for i in range(12)
        ]
        paper = QuestionPaperGeneratorService.generate_balanced_paper(
            available_questions=questions,
            target_count=6,
            difficulty_distribution={'EASY': 0.33, 'MEDIUM': 0.34, 'HARD': 0.33}
        )
        self.assertEqual(len(paper), 6)


class ProctoringSecurityTestCase(SimpleTestCase):
    def test_anomaly_risk_calculation(self):
        events = [
            {'event_type': 'TAB_SWITCH', 'severity': 'MEDIUM'},
            {'event_type': 'TAB_SWITCH', 'severity': 'MEDIUM'},
            {'event_type': 'DEVTOOLS_OPENED', 'severity': 'HIGH'}
        ]
        res = ProctoringSecurityService.calculate_attempt_risk_score(events)
        # 15 + 15 + 30 = 60 pts
        self.assertEqual(res['risk_score'], 60)
        self.assertEqual(res['risk_tier'], 'HIGH_RISK_SUSPICIOUS')
        self.assertTrue(res['is_flagged_for_review'])


class ExamTimerTestCase(SimpleTestCase):
    def test_timer_active_and_expiry(self):
        now = timezone.now()
        started = now - timedelta(minutes=30)
        active_res = ExamTimerService.check_time_remaining(started, duration_minutes=60)
        self.assertFalse(active_res['is_expired'])
        self.assertTrue(active_res['minutes_remaining'] >= 29)

        # Expired exam
        started_long_ago = now - timedelta(minutes=90)
        expired_res = ExamTimerService.check_time_remaining(started_long_ago, duration_minutes=60)
        self.assertTrue(expired_res['is_expired'])
        self.assertEqual(expired_res['seconds_remaining'], 0)


class PlagiarismServiceTestCase(SimpleTestCase):
    def test_jaccard_similarity(self):
        text_a = "The quick brown fox jumps over the lazy dog and runs away into the forest."
        text_b = "The quick brown fox jumps over the lazy dog and runs away into the forest."
        sim = PlagiarismDetectionService.compute_jaccard_similarity(text_a, text_b)
        self.assertEqual(sim, 100.0)

    def test_scan_submission_corpus(self):
        target = "Data structures and algorithms provide efficient computation for software engineering."
        corpus = [
            {'id': 1, 'student_name': 'Alice', 'text': 'Data structures and algorithms provide efficient computation for software engineering.'},
            {'id': 2, 'student_name': 'Bob', 'text': 'Completely different topic on historical ancient Rome architecture.'}
        ]
        res = PlagiarismDetectionService.scan_submission_corpus(target, corpus)
        self.assertTrue(res['is_flagged_for_plagiarism'])
        self.assertEqual(res['highest_similarity'], 100.0)
        self.assertEqual(res['matching_sources_count'], 1)


class PeerReviewTestCase(SimpleTestCase):
    def test_peer_review_allocation(self):
        submissions = [
            {'id': 101, 'student_id': 1},
            {'id': 102, 'student_id': 2},
            {'id': 103, 'student_id': 3},
            {'id': 104, 'student_id': 4}
        ]
        allocations = PeerReviewDistributionService.allocate_peer_reviews(submissions, reviews_per_submission=2)
        self.assertEqual(len(allocations), 8)  # 4 * 2 = 8
        for a in allocations:
            self.assertNotEqual(a['submission_author_id'], a['reviewer_id'])


class GradebookTestCase(SimpleTestCase):
    def test_weighted_category_grade_with_drop(self):
        categories = [
            {'category': 'Quizzes', 'weight': 20.0, 'scores': [50, 90, 100], 'drop_lowest': 1}, # drop 50 -> avg 95 -> 19.0
            {'category': 'Midterm', 'weight': 30.0, 'scores': [90]}, # 27.0
            {'category': 'Final', 'weight': 50.0, 'scores': [90]} # 45.0
        ]
        res = GradebookService.calculate_final_grade(categories)
        # 19.0 + 27.0 + 45.0 = 91.00
        self.assertEqual(float(res['final_percentage']), 91.00)


class CurvingTestCase(SimpleTestCase):
    def test_square_root_curve(self):
        scores = [64.0, 81.0, 100.0]
        curved = GradeCurvingService.apply_square_root_curve(scores)
        self.assertEqual(curved, [80.0, 90.0, 100.0])

    def test_linear_shift(self):
        scores = [60.0, 70.0, 90.0]
        curved = GradeCurvingService.apply_linear_shift(scores, target_max=100.0)
        # max is 90 -> +10 to all
        self.assertEqual(curved, [70.0, 80.0, 100.0])


class CertificateServiceTestCase(SimpleTestCase):
    def test_crypto_hash_and_verification(self):
        h = CertificateCryptoService.generate_verification_hash(
            student_id=42,
            course_code='CS-101',
            certificate_number='CERT-2026-999',
            issue_date_str='2026-09-17'
        )
        self.assertEqual(len(h), 64)
        is_valid = CertificateCryptoService.verify_hash(
            student_id=42,
            course_code='CS-101',
            certificate_number='CERT-2026-999',
            issue_date_str='2026-09-17',
            provided_hash=h
        )
        self.assertTrue(is_valid)

    def test_pdf_generation(self):
        pdf_bytes = PDFCertificateGeneratorService.generate_certificate_pdf(
            student_name='Jane Doe',
            course_title='Advanced Artificial Intelligence',
            course_code='AI-201',
            institution_name='Apex University Institute of Technology',
            certificate_number='CERT-2026-AI-001',
            issue_date_str='September 17, 2026',
            honors_title='Summa Cum Laude'
        )
        self.assertTrue(len(pdf_bytes) > 1000)
        self.assertTrue(pdf_bytes.startswith(b'%PDF'))
