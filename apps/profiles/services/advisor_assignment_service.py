"""
Academic Advisor Matching & Load Balancing Service.
Matches students to departmental faculty advisors balancing caseloads and specialization areas.
"""
from typing import Dict, Any, List


class AdvisorAssignmentService:
    MAX_ADVISEE_CAPACITY = 35

    @classmethod
    def match_advisor(
        cls,
        student_major_specialization: str,
        available_faculty: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Finds the optimal advisor for a student:
        1. Prioritizes matching specialization area.
        2. Selects faculty member with lowest existing advisee caseload.
        """
        candidates = [
            f for f in available_faculty
            if f.get('current_advisees', 0) < cls.MAX_ADVISEE_CAPACITY
        ]

        if not candidates:
            return {
                'assigned': False,
                'advisor': None,
                'reason': 'All departmental faculty advisors are at maximum advisee capacity.'
            }

        # Filter by matching specialization
        specialists = [
            f for f in candidates
            if student_major_specialization.lower() in [s.lower() for s in f.get('specializations', [])]
        ]

        pool = specialists if specialists else candidates
        # Pick least loaded advisor
        chosen = min(pool, key=lambda f: f.get('current_advisees', 0))

        return {
            'assigned': True,
            'advisor': chosen,
            'is_specialization_match': bool(specialists),
            'projected_caseload': chosen.get('current_advisees', 0) + 1
        }
