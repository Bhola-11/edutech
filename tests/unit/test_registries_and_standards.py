"""
Unit tests for standardized tests, accreditation bodies registry, and course transfer equivalencies.
"""
from django.test import SimpleTestCase

from apps.core.standards.standardized_tests import StandardizedTestPlacementService
from apps.institutions.registries.accreditation_bodies import AccreditationRegistryService
from apps.institutions.registries.course_equivalency_matrix import CourseEquivalencyService


class StandardizedTestsTestCase(SimpleTestCase):
    def test_ap_computer_science_award(self):
        res = StandardizedTestPlacementService.evaluate_ap_credits('AP_COMPUTER_SCIENCE_A', 5)
        self.assertTrue(res['eligible'])
        self.assertEqual(res['credits_awarded'], 4)
        self.assertEqual(res['equivalent_course'], 'CS-101')

    def test_ap_calculus_score_3_award(self):
        res = StandardizedTestPlacementService.evaluate_ap_credits('AP_CALCULUS_BC', 3)
        self.assertTrue(res['eligible'])
        self.assertEqual(res['credits_awarded'], 4)

    def test_ib_high_level_award(self):
        res = StandardizedTestPlacementService.evaluate_ib_credits('IB_HL_COMPUTER_SCIENCE', 7)
        self.assertTrue(res['eligible'])
        self.assertEqual(res['credits_awarded'], 8)
        self.assertEqual(res['equivalent_course'], 'CS-101')


class AccreditationRegistryTestCase(SimpleTestCase):
    def test_lookup_abet(self):
        agency = AccreditationRegistryService.get_agency_by_code('ABET')
        self.assertEqual(agency['code'], 'ABET')
        self.assertIn('Engineering', agency['disciplines'])

    def test_filter_by_discipline(self):
        agencies = AccreditationRegistryService.get_agencies_by_discipline('Architecture')
        self.assertTrue(any(a['code'] == 'NAAB' for a in agencies))


class CourseEquivalencyTestCase(SimpleTestCase):
    def test_lookup_mit_python(self):
        eq = CourseEquivalencyService.lookup_equivalency('MIT', '6.0001')
        self.assertIsNotNone(eq)
        self.assertEqual(eq['target_code'], 'CS-101')

    def test_list_equivalencies_for_cs101(self):
        matches = CourseEquivalencyService.list_equivalencies_for_course('CS-101')
        self.assertTrue(len(matches) >= 3)
