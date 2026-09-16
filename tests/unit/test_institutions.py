import datetime
from django.test import TestCase
from apps.institutions.models import Institution, Campus, Faculty, AcademicDepartment, AcademicSession, Semester

class InstitutionsModelTests(TestCase):
    def setUp(self):
        self.inst = Institution.objects.create(
            name='Test University',
            code='TU',
            contact_email='info@tu.edu',
            city='Boston',
            country='United States'
        )

    def test_institution_creation(self):
        self.assertEqual(self.inst.name, 'Test University')
        self.assertTrue(self.inst.slug)
        self.assertEqual(str(self.inst), 'Test University (TU)')

    def test_campus_creation(self):
        campus = Campus.objects.create(
            institution=self.inst,
            name='Boston Campus',
            code='BOS',
            address='123 Beacon St',
            city='Boston',
            state='MA'
        )
        self.assertEqual(campus.institution, self.inst)
        self.assertTrue(campus.slug)
