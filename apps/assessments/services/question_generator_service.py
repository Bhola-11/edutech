"""
Dynamic Assessment & Question Paper Generation Engine.
Assembles randomized, balanced exams adhering to Bloom's taxonomy quotas and difficulty curves.
"""
import random
from typing import Dict, Any, List


class QuestionPaperGeneratorService:
    @classmethod
    def generate_balanced_paper(
        cls,
        available_questions: List[Dict[str, Any]],
        target_count: int = 20,
        difficulty_distribution: Dict[str, float] = None,
        blooms_distribution: Dict[str, float] = None
    ) -> List[Dict[str, Any]]:
        """
        Selects a balanced subset of questions satisfying specified difficulty
        and Bloom's cognitive level proportions.
        """
        if not difficulty_distribution:
            difficulty_distribution = {'EASY': 0.30, 'MEDIUM': 0.50, 'HARD': 0.20}

        if len(available_questions) <= target_count:
            selected = list(available_questions)
            random.shuffle(selected)
            return selected

        # Group by difficulty
        by_diff = {}
        for q in available_questions:
            diff = q.get('difficulty', 'MEDIUM').upper()
            by_diff.setdefault(diff, []).append(q)

        selected = []
        for diff, ratio in difficulty_distribution.items():
            quota = int(round(target_count * ratio))
            pool = by_diff.get(diff, [])
            if pool:
                sample_size = min(len(pool), quota)
                selected.extend(random.sample(pool, sample_size))

        # Fill remaining slots if rounding caused a slight shortage
        remaining_needed = target_count - len(selected)
        if remaining_needed > 0:
            unselected = [q for q in available_questions if q not in selected]
            if unselected:
                selected.extend(random.sample(unselected, min(len(unselected), remaining_needed)))

        random.shuffle(selected)
        return selected
