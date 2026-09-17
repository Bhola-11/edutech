"""
Grade Curving & Statistical Normalization Engine.
Linear scaling, Gaussian bell curve normalization, and square-root curve formulas.
"""
import math
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List


class GradeCurvingService:
    @classmethod
    def apply_square_root_curve(cls, raw_scores: List[float]) -> List[float]:
        """
        Applies standard Square Root curve: new_score = sqrt(raw_score) * 10
        (e.g., 64 -> 80, 81 -> 90, 100 -> 100).
        """
        return [round(math.sqrt(max(0, s)) * 10, 2) for s in raw_scores]

    @classmethod
    def apply_linear_shift(cls, raw_scores: List[float], target_max: float = 100.0) -> List[float]:
        """Shifts the highest score to target_max and adds the same delta to all scores."""
        if not raw_scores:
            return []
        max_score = max(raw_scores)
        delta = max(0.0, target_max - max_score)
        return [round(min(100.0, s + delta), 2) for s in raw_scores]

    @classmethod
    def apply_gaussian_bell_curve(
        cls,
        raw_scores: List[float],
        target_mean: float = 75.0,
        target_std_dev: float = 10.0
    ) -> List[float]:
        """Normalizes scores to a target Gaussian mean and standard deviation."""
        if not raw_scores:
            return []
        n = len(raw_scores)
        if n == 1:
            return [target_mean]

        mean = sum(raw_scores) / n
        variance = sum((s - mean) ** 2 for s in raw_scores) / n
        std_dev = math.sqrt(variance) if variance > 0 else 1.0

        curved = []
        for s in raw_scores:
            z_score = (s - mean) / std_dev
            new_score = target_mean + (z_score * target_std_dev)
            curved.append(round(max(0.0, min(100.0, new_score)), 2))
        return curved
