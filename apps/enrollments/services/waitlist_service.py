"""
Dynamic Course Waitlist Priority & Auto-Enrollment Service.
Prioritizes waitlist queues based on academic class standing, GPA, and major requirement urgency.
"""
from decimal import Decimal
from typing import Dict, Any, List
from django.utils import timezone


class WaitlistPriorityService:
    @classmethod
    def calculate_waitlist_priority_score(
        cls,
        student_year_level: int,  # 4 = Senior, 3 = Junior, 2 = Soph, 1 = Frosh
        is_degree_requirement: bool,
        is_graduating_senior: bool,
        cumulative_gpa: Decimal,
        days_on_waitlist: int
    ) -> Decimal:
        """
        Computes composite priority score:
        Graduating seniors and major requirements receive weighted priority over general electives.
        """
        score = Decimal('0.00')

        # Seniority (0 - 40 points)
        score += Decimal(str(student_year_level * 10))

        # Graduation urgency (30 points)
        if is_graduating_senior:
            score += Decimal('30.00')

        # Major requirement status (20 points)
        if is_degree_requirement:
            score += Decimal('20.00')

        # GPA tiebreaker (0 - 10 points: e.g. 4.0 GPA = 10 pts)
        score += (Decimal(str(cumulative_gpa)) * Decimal('2.5')).quantize(Decimal('0.01'))

        # Time on waitlist (0.5 pt per day, capped at 10 pts)
        waitlist_days_pts = min(Decimal('10.00'), Decimal(str(days_on_waitlist)) * Decimal('0.5'))
        score += waitlist_days_pts

        return score.quantize(Decimal('0.01'))

    @classmethod
    def rank_waitlist_entries(cls, entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Sorts waitlist candidates by descending composite priority score."""
        for entry in entries:
            entry['priority_score'] = cls.calculate_waitlist_priority_score(
                student_year_level=entry.get('year_level', 1),
                is_degree_requirement=entry.get('is_degree_requirement', False),
                is_graduating_senior=entry.get('is_graduating_senior', False),
                cumulative_gpa=Decimal(str(entry.get('cumulative_gpa', 3.0))),
                days_on_waitlist=entry.get('days_on_waitlist', 0)
            )

        ranked = sorted(entries, key=lambda x: x['priority_score'], reverse=True)
        for rank, item in enumerate(ranked, 1):
            item['waitlist_position'] = rank
        return ranked
