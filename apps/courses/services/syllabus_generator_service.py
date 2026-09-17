"""
Comprehensive Course Syllabus Generator Service.
Constructs standard 14-week university syllabi including grading criteria, textbooks, and policies.
"""
from typing import Dict, Any, List


class SyllabusGeneratorService:
    @classmethod
    def generate_standard_syllabus(
        cls,
        course_code: str,
        course_title: str,
        credit_hours: int,
        department_name: str,
        instructor_name: str,
        instructor_email: str,
        office_hours: str,
        prerequisites: List[str],
        course_description: str,
        weekly_topics: List[str],
        textbooks: List[str]
    ) -> Dict[str, Any]:
        """Generates a structured university syllabus matching accreditation specifications."""
        weeks = []
        for i, topic in enumerate(weekly_topics[:14], 1):
            weeks.append({
                'week_number': i,
                'topic': topic,
                'readings': f"Assigned readings for Week {i}",
                'deliverables': "Laboratory assignment / Homework" if i % 2 == 0 else "Lecture discussion & problem set"
            })

        grading_breakdown = [
            {'category': 'Midterm Examination', 'weight_percentage': 25},
            {'category': 'Final Examination', 'weight_percentage': 35},
            {'category': 'Laboratory Experiments & Projects', 'weight_percentage': 25},
            {'category': 'Homework & Problem Sets', 'weight_percentage': 10},
            {'category': 'Class Participation & Attendance', 'weight_percentage': 5}
        ]

        return {
            'course_code': course_code,
            'course_title': course_title,
            'credit_hours': credit_hours,
            'department': department_name,
            'instructor': {
                'name': instructor_name,
                'email': instructor_email,
                'office_hours': office_hours
            },
            'prerequisites': prerequisites,
            'description': course_description,
            'schedule': weeks,
            'grading_breakdown': grading_breakdown,
            'textbooks': textbooks,
            'academic_integrity_statement': "Students are expected to adhere strictly to the Institutional Honor Code."
        }
