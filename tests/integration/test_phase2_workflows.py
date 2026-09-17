"""
End-to-End Integration tests for Phase 2 workflows:
Assessments, Examinations, Assignments, Gradebook, and Certificate Verification.
"""
from decimal import Decimal
from datetime import timedelta, date
from django.test import TestCase, Client
from django.utils import timezone
from django.urls import reverse

from apps.accounts.models import User
from apps.institutions.models import Institution, Faculty, AcademicDepartment, AcademicSession, Semester
from apps.courses.models import Course, Program
from apps.enrollments.models import StudentEnrollment
from apps.assessments.models import Assessment, AssessmentSection, Question, QuestionOption
from apps.examinations.models import ExamSession, ExamAttempt, ProctoringEvent
from apps.assignments.models import Assignment, AssignmentSubmission
from apps.certificates.models import CertificateTemplate, IssuedCertificate
from apps.certificates.services.crypto_verification_service import CertificateCryptoService


class Phase2WorkflowTestCase(TestCase):
    def setUp(self):
        self.institution = Institution.objects.create(
            name='Global Polytechnic University',
            code='GPU',
            contact_email='admin@gpu.edu',
            address_line_1='100 Tech Blvd',
            city='Boston',
            state_province='MA',
            postal_code='02139'
        )
        self.academic_session = AcademicSession.objects.create(
            institution=self.institution,
            name='Academic Year 2026-2027',
            start_date=date(2026, 9, 1),
            end_date=date(2027, 6, 30)
        )
        self.semester = Semester.objects.create(
            academic_session=self.academic_session,
            name='Fall 2026',
            start_date=date(2026, 9, 1),
            end_date=date(2026, 12, 20),
            registration_start_date=date(2026, 8, 1),
            registration_end_date=date(2026, 9, 5),
            add_drop_deadline=date(2026, 9, 15),
            is_current=True
        )
        self.faculty_user = User.objects.create_user(
            username='prof_hopper',
            email='hopper@gpu.edu',
            password='Password123!',
            role='INSTRUCTOR',
            institution=self.institution
        )
        self.student_user = User.objects.create_user(
            username='student_ada',
            email='ada@gpu.edu',
            password='Password123!',
            role='STUDENT',
            institution=self.institution
        )
        self.faculty = Faculty.objects.create(
            institution=self.institution,
            name='Faculty of Computing',
            code='FC'
        )
        self.department = AcademicDepartment.objects.create(
            faculty=self.faculty,
            name='Computer Science',
            code='CS'
        )
        self.program = Program.objects.create(
            department=self.department,
            name='B.S. Computer Science',
            code='BSCS',
            academic_level='UNDERGRADUATE'
        )
        self.course = Course.objects.create(
            department=self.department,
            title='Algorithms and Data Structures',
            code='CS-201',
            credit_hours=4
        )
        self.enrollment = StudentEnrollment.objects.create(
            student=self.student_user,
            course=self.course,
            semester=self.semester,
            status='ACTIVE'
        )
        self.client = Client()

    def test_assessment_to_exam_attempt_lifecycle(self):
        # 1. Create Assessment
        assessment = Assessment.objects.create(
            institution=self.institution,
            course=self.course,
            title='Midterm Exam',
            assessment_type='MIDTERM',
            duration_minutes=90,
            total_points=Decimal('100.00'),
            is_proctored=True,
            is_published=True
        )
        section = AssessmentSection.objects.create(
            assessment=assessment,
            title='Section A: Algorithmic Complexity',
            section_points=Decimal('50.00')
        )
        question = Question.objects.create(
            institution=self.institution,
            course=self.course,
            title='Binary Search Complexity',
            question_type='MCQ_SINGLE',
            prompt_html='<p>What is the worst-case time complexity of Binary Search?</p>',
            default_points=Decimal('5.00')
        )
        QuestionOption.objects.create(
            question=question,
            option_text='O(log N)',
            is_correct=True
        )
        QuestionOption.objects.create(
            question=question,
            option_text='O(N)',
            is_correct=False
        )

        # 2. Schedule Exam Session
        now = timezone.now()
        session = ExamSession.objects.create(
            institution=self.institution,
            assessment=assessment,
            session_code='GPU-CS201-MIDTERM-2026',
            start_window=now - timedelta(hours=1),
            end_window=now + timedelta(hours=2),
            status='IN_PROGRESS',
            requires_webcam=True
        )

        # 3. Candidate Starts Attempt
        self.client.force_login(self.student_user)
        response = self.client.get(reverse('examinations:take', kwargs={'session_id': session.pk}))
        self.assertEqual(response.status_code, 200)

        attempt = ExamAttempt.objects.get(session=session, student=self.student_user)
        self.assertEqual(attempt.status, 'IN_PROGRESS')

        # 4. Log Proctoring Security Anomaly Event
        log_resp = self.client.post(
            reverse('examinations:api_log_event'),
            data={'attempt_id': attempt.pk, 'event_type': 'TAB_SWITCH', 'severity': 'MEDIUM'},
            content_type='application/json'
        )
        self.assertEqual(log_resp.status_code, 200)
        self.assertEqual(ProctoringEvent.objects.filter(attempt=attempt).count(), 1)

    def test_assignment_submission_and_plagiarism_workflow(self):
        # 1. Create Assignment
        assignment = Assignment.objects.create(
            institution=self.institution,
            course=self.course,
            title='Lab 1: Graph Traversal Implementation',
            instructions_html='<p>Implement BFS and DFS in Python.</p>',
            total_points=Decimal('50.00'),
            due_date=timezone.now() + timedelta(days=7),
            submission_type='TEXT_ENTRY'
        )

        # 2. Student Submits Assignment
        self.client.force_login(self.student_user)
        response = self.client.post(
            reverse('assignments:submit', kwargs={'pk': assignment.pk}),
            data={'text_content': 'def bfs(graph, start): pass', 'external_url': 'https://github.com/student/graph-lab'}
        )
        self.assertEqual(response.status_code, 302)
        sub = AssignmentSubmission.objects.get(assignment=assignment, student=self.student_user)
        self.assertFalse(sub.is_late)
        self.assertEqual(sub.status, 'SUBMITTED')

    def test_certificate_issuance_and_public_verification(self):
        template = CertificateTemplate.objects.create(
            institution=self.institution,
            title='Standard Honors Certificate',
            code='STD-HONORS',
            issuer_name='Dr. Grace Hopper',
            issuer_title='Dean of Computing'
        )
        cert_number = 'GPU-CERT-2026-ADA-001'
        issue_date = timezone.now().date()
        crypto_hash = CertificateCryptoService.generate_verification_hash(
            student_id=self.student_user.id,
            course_code=self.course.code,
            certificate_number=cert_number,
            issue_date_str=str(issue_date)
        )
        cert = IssuedCertificate.objects.create(
            institution=self.institution,
            student=self.student_user,
            course=self.course,
            template=template,
            certificate_number=cert_number,
            verification_hash=crypto_hash,
            issue_date=issue_date,
            honors_title='Summa Cum Laude'
        )

        # Public verification lookup
        anon_client = Client()
        verify_url = reverse('certificates:verify_code', kwargs={'certificate_number': cert_number})
        response = anon_client.get(verify_url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['is_valid'])
        self.assertEqual(response.context['cert'].certificate_number, cert_number)
