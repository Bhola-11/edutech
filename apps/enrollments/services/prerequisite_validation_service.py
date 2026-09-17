"""
Prerequisite & Corequisite Enforcement Engine.
Validates academic DAG dependencies, concurrent enrollment permissions, and minimum grade thresholds.
"""
from typing import Dict, Any, List, Set, Optional


class PrerequisiteValidationService:
    MIN_PASSING_GRADE_POINTS = {
        'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
    }

    @classmethod
    def validate_enrollment_eligibility(
        cls,
        student_completed_courses: Dict[str, str],  # {course_code: letter_grade}
        course_prerequisites: List[Dict[str, Any]],  # [{'code': 'CS101', 'min_grade': 'C'}]
        currently_enrolled_courses: Set[str],
        course_corequisites: Optional[List[str]] = None,
        has_instructor_override: bool = False
    ) -> Dict[str, Any]:
        """
        Validates whether a student satisfies all prerequisites and corequisites for course enrollment.
        """
        if has_instructor_override:
            return {
                'eligible': True,
                'reason': 'Enrollment authorized via official faculty / dean override waiver.',
                'missing_prerequisites': [],
                'missing_corequisites': []
            }

        missing_prereqs = []
        insufficient_grades = []

        for req in course_prerequisites:
            req_code = req.get('code')
            min_grade = req.get('min_grade', 'C')
            min_points = cls.MIN_PASSING_GRADE_POINTS.get(min_grade, 2.0)

            if req_code not in student_completed_courses:
                missing_prereqs.append(req_code)
            else:
                student_grade = student_completed_courses[req_code]
                student_points = cls.MIN_PASSING_GRADE_POINTS.get(student_grade, 0.0)
                if student_points < min_points:
                    insufficient_grades.append(f"{req_code} (Required: {min_grade}, Earned: {student_grade})")

        # Corequisite check
        missing_coreqs = []
        if course_corequisites:
            for coreq in course_corequisites:
                if coreq not in student_completed_courses and coreq not in currently_enrolled_courses:
                    missing_coreqs.append(coreq)

        is_eligible = len(missing_prereqs) == 0 and len(insufficient_grades) == 0 and len(missing_coreqs) == 0

        reasons = []
        if missing_prereqs:
            reasons.append(f"Missing mandatory prerequisite courses: {', '.join(missing_prereqs)}.")
        if insufficient_grades:
            reasons.append(f"Prerequisite grade below minimum standard: {', '.join(insufficient_grades)}.")
        if missing_coreqs:
            reasons.append(f"Missing concurrent corequisite registration: {', '.join(missing_coreqs)}.")

        return {
            'eligible': is_eligible,
            'reason': 'All prerequisite and corequisite requirements satisfied.' if is_eligible else ' '.join(reasons),
            'missing_prerequisites': missing_prereqs,
            'insufficient_grades': insufficient_grades,
            'missing_corequisites': missing_coreqs
        }
