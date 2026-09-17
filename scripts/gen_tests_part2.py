import os

DISCIPLINES_PART2 = [
    ('humanities_languages', 'Humanities, Philosophy & World Literature', 'HUM'),
    ('social_sciences_psychology', 'Psychological Sciences & Behavioral Analytics', 'PSY'),
    ('legal_studies_jurisprudence', 'Jurisprudence, Constitutional & Corporate Law', 'LAW'),
    ('architecture_spatial_design', 'Architecture, Urbanism & Spatial Computation', 'ARCH'),
    ('environmental_sustainability', 'Earth Systems Science & Sustainable Development', 'ENV'),
]

for slug, full_name, pfx in DISCIPLINES_PART2:
    test_path = os.path.join('tests/curricula', f'test_{slug}.py')
    with open(test_path, 'w', encoding='utf-8') as f:
        f.write(f'"""\nAutomated Test Suite for {full_name} Academic Curriculum\n"""\n\n')
        f.write('from django.test import SimpleTestCase\n')
        f.write(f'from apps.courses.curricula.{slug} import CURRICULUM_NAME, DISCIPLINE_CODE, COURSES\n\n')
        f.write(f'class {pfx}CurriculumValidationTests(SimpleTestCase):\n')
        f.write('    def test_curriculum_metadata(self):\n')
        f.write(f'        self.assertEqual(CURRICULUM_NAME, "{full_name}")\n')
        f.write(f'        self.assertEqual(DISCIPLINE_CODE, "{pfx}")\n')
        f.write('        self.assertGreaterEqual(len(COURSES), 14)\n\n')
        f.write('    def test_course_structure_integrity(self):\n')
        f.write('        for c in COURSES:\n')
        f.write('            self.assertIn("code", c)\n')
        f.write('            self.assertIn("title", c)\n')
        f.write('            self.assertIn("credit_hours", c)\n')
        f.write('            self.assertIn("lecture_hours", c)\n')
        f.write('            self.assertIn("lab_hours", c)\n')
        f.write('            self.assertIn("description", c)\n')
        f.write('            self.assertIn("learning_outcomes", c)\n')
        f.write('            self.assertIn("syllabus_weeks", c)\n')
        f.write('            self.assertIn("textbook_references", c)\n')
        f.write('            self.assertIn("assessment_questions", c)\n\n')
        f.write('            self.assertGreaterEqual(c["credit_hours"], 3.0)\n')
        f.write('            self.assertLessEqual(c["credit_hours"], 5.0)\n')
        f.write('            self.assertEqual(len(c["learning_outcomes"]), 5)\n')
        f.write('            self.assertEqual(len(c["syllabus_weeks"]), 14)\n')
        f.write('            self.assertEqual(len(c["assessment_questions"]), 5)\n\n')
        f.write('    def test_weekly_syllabus_continuity(self):\n')
        f.write('        for c in COURSES:\n')
        f.write('            for idx, week_item in enumerate(c["syllabus_weeks"], start=1):\n')
        f.write('                self.assertEqual(week_item["week"], idx)\n')
        f.write('                self.assertTrue(week_item["topic"])\n')
        f.write('                self.assertTrue(week_item["lecture_agenda"])\n')
        f.write('                self.assertTrue(week_item["reading"])\n')
        f.write('                self.assertTrue(week_item["lab_assignment"])\n\n')
        f.write('    def test_assessment_question_validity(self):\n')
        f.write('        for c in COURSES:\n')
        f.write('            for q in c["assessment_questions"]:\n')
        f.write('                self.assertIn("question_number", q)\n')
        f.write('                self.assertIn("prompt", q)\n')
        f.write('                self.assertEqual(len(q["options"]), 4)\n')
        f.write('                self.assertIn(q["correct_answer"], ["A", "B", "C", "D"])\n')
        f.write('                self.assertTrue(q["explanation"])\n')

print("Part 2 tests generated successfully.")
