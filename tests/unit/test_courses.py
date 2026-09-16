from django.test import TestCase
from apps.institutions.models import Institution, Faculty, AcademicDepartment
from apps.courses.models import Course, CourseCategory, Program, CourseModule, Lesson

class CoursesModelTests(TestCase):
    def setUp(self):
        self.inst = Institution.objects.create(name='Tech Univ', code='TU', contact_email='info@tu.edu', city='Boston', country='US')
        self.faculty = Faculty.objects.create(institution=self.inst, name='Computing', code='COMP')
        self.dept = AcademicDepartment.objects.create(faculty=self.faculty, name='Computer Science', code='CS')
        self.cat = CourseCategory.objects.create(name='Core', code='CORE')
        self.course = Course.objects.create(
            department=self.dept,
            category=self.cat,
            title='Intro to Algorithms',
            code='CS-101',
            credit_hours=3.0,
            description='Foundational algorithm course'
        )

    def test_course_creation(self):
        self.assertEqual(self.course.code, 'CS-101')
        self.assertTrue(self.course.slug)

    def test_module_and_lesson(self):
        mod = CourseModule.objects.create(course=self.course, title='Module 1', order=1)
        lesson = Lesson.objects.create(module=mod, title='Lesson 1', order=1, duration_minutes=30)
        self.assertEqual(mod.course, self.course)
        self.assertEqual(lesson.module, mod)
