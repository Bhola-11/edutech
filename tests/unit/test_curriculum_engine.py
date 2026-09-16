from django.test import TestCase
from apps.institutions.models import Institution, Faculty, AcademicDepartment
from apps.courses.models import Course, Program, CourseCategory
from apps.courses.curriculum_engine import CurriculumDAGService, DegreeAuditService
from apps.accounts.models import User
from apps.enrollments.models import StudentEnrollment

class CurriculumEngineTests(TestCase):
    def setUp(self):
        self.inst = Institution.objects.create(name='Caltech', code='CIT', contact_email='info@caltech.edu', city='Pasadena', country='US')
        self.faculty = Faculty.objects.create(institution=self.inst, name='Eng', code='ENG')
        self.dept = AcademicDepartment.objects.create(faculty=self.faculty, name='CS', code='CS')
        self.cat = CourseCategory.objects.create(name='CS Core', code='CS_CORE')

        self.c1 = Course.objects.create(department=self.dept, category=self.cat, title='CS1', code='CS1', credit_hours=3.0)
        self.c2 = Course.objects.create(department=self.dept, category=self.cat, title='CS2', code='CS2', credit_hours=3.0)
        self.c3 = Course.objects.create(department=self.dept, category=self.cat, title='CS3', code='CS3', credit_hours=3.0)

        self.c2.prerequisites.add(self.c1)
        self.c3.prerequisites.add(self.c2)

        self.prog = Program.objects.create(department=self.dept, code='BSCS', name='BS in CS', total_credits_required=6)
        self.prog.curriculum_courses.add(self.c1, self.c2)

        self.student = User.objects.create_user(email='s@cit.edu', username='scit', password='password123')

    def test_circular_dependency_detection(self):
        # Adding c3 as prerequisite to c1 would create a cycle: c1 -> c2 -> c3 -> c1
        has_cycle = CurriculumDAGService.detect_circular_dependencies(course_id=self.c1.id, proposed_prerequisite_id=self.c3.id)
        self.assertTrue(has_cycle)

        # Adding c1 as prerequisite to c3 is valid
        is_safe = CurriculumDAGService.detect_circular_dependencies(course_id=self.c3.id, proposed_prerequisite_id=self.c1.id)
        self.assertFalse(is_safe)

    def test_topological_sequence(self):
        sequence = CurriculumDAGService.get_recommended_sequence(self.prog)
        self.assertEqual(len(sequence), 2)
        self.assertEqual(sequence[0].id, self.c1.id)
        self.assertEqual(sequence[1].id, self.c2.id)

    def test_degree_audit_service(self):
        audit_engine = DegreeAuditService(self.student, self.prog)
        audit_res = audit_engine.perform_audit()
        self.assertEqual(audit_res['credits_earned'], 0.0)
        self.assertFalse(audit_res['is_eligible_for_graduation'])
