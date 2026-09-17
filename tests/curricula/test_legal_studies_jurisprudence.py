"""
Automated Test Suite for Jurisprudence, Constitutional & Corporate Law Academic Curriculum
"""

from django.test import SimpleTestCase
from apps.courses.curricula.legal_studies_jurisprudence import CURRICULUM_NAME, DISCIPLINE_CODE, COURSES

class LAWCurriculumValidationTests(SimpleTestCase):
    def test_curriculum_metadata(self):
        self.assertEqual(CURRICULUM_NAME, "Jurisprudence, Constitutional & Corporate Law")
        self.assertEqual(DISCIPLINE_CODE, "LAW")
        self.assertGreaterEqual(len(COURSES), 14)

    def test_course_structure_integrity(self):
        for c in COURSES:
            self.assertIn("code", c)
            self.assertIn("title", c)
            self.assertIn("credit_hours", c)
            self.assertIn("lecture_hours", c)
            self.assertIn("lab_hours", c)
            self.assertIn("description", c)
            self.assertIn("learning_outcomes", c)
            self.assertIn("syllabus_weeks", c)
            self.assertIn("textbook_references", c)
            self.assertIn("assessment_questions", c)

            self.assertGreaterEqual(c["credit_hours"], 3.0)
            self.assertLessEqual(c["credit_hours"], 5.0)
            self.assertEqual(len(c["learning_outcomes"]), 5)
            self.assertEqual(len(c["syllabus_weeks"]), 14)
            self.assertEqual(len(c["assessment_questions"]), 5)

    def test_weekly_syllabus_continuity(self):
        for c in COURSES:
            for idx, week_item in enumerate(c["syllabus_weeks"], start=1):
                self.assertEqual(week_item["week"], idx)
                self.assertTrue(week_item["topic"])
                self.assertTrue(week_item["lecture_agenda"])
                self.assertTrue(week_item["reading"])
                self.assertTrue(week_item["lab_assignment"])

    def test_assessment_question_validity(self):
        for c in COURSES:
            for q in c["assessment_questions"]:
                self.assertIn("question_number", q)
                self.assertIn("prompt", q)
                self.assertEqual(len(q["options"]), 4)
                self.assertIn(q["correct_answer"], ["A", "B", "C", "D"])
                self.assertTrue(q["explanation"])
