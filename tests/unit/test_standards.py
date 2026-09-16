from django.test import SimpleTestCase
from apps.core.standards.grading_scales import GradeConversionEngine, US_4_POINT_SCALE, ECTS_SCALE
from apps.core.standards.cip_codes import CIP_DIRECTORY
from apps.core.standards.countries_iso import COUNTRIES, COUNTRIES_BY_ISO2
from apps.courses.accreditation import BLOOMS_TAXONOMY, ABET_STUDENT_OUTCOMES

class EducationalStandardsTests(SimpleTestCase):
    def test_grade_conversion(self):
        letter, gpa, standing = GradeConversionEngine.score_to_letter_grade(95.5)
        self.assertEqual(letter, 'A')
        self.assertEqual(standing, 'Distinction')

    def test_term_gpa_calculation(self):
        grades = [('A', 4.0), ('B+', 3.0), ('A-', 3.0)]
        gpa = GradeConversionEngine.calculate_term_gpa(grades)
        self.assertGreaterEqual(gpa, 3.5)

    def test_cip_directory(self):
        self.assertIn('11.0701', CIP_DIRECTORY)
        cs_cip = CIP_DIRECTORY['11.0701']
        self.assertEqual(cs_cip['title'], 'Computer Science')
        self.assertTrue(cs_cip['stem_designated'])

    def test_countries_iso(self):
        self.assertGreaterEqual(len(COUNTRIES), 90)
        us = COUNTRIES_BY_ISO2.get('US')
        self.assertIsNotNone(us)
        self.assertEqual(us['currency'], 'USD')

    def test_blooms_taxonomy(self):
        self.assertEqual(len(BLOOMS_TAXONOMY), 6)
        self.assertIn('REMEMBER', BLOOMS_TAXONOMY)
        self.assertIn('CREATE', BLOOMS_TAXONOMY)

    def test_abet_student_outcomes(self):
        self.assertEqual(len(ABET_STUDENT_OUTCOMES), 7)
        self.assertIn('SO-1', ABET_STUDENT_OUTCOMES)
        self.assertIn('SO-7', ABET_STUDENT_OUTCOMES)
