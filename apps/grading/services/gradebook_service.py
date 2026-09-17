"""
Enterprise Gradebook & Weighted Category Calculation Service.
Handles weighted categories, dropping lowest N scores, and extra credit.
"""
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List


class GradebookService:
    @classmethod
    def calculate_final_grade(
        cls,
        category_grades: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates composite final course grade based on category weightings.
        category_grades = [
            {'category': 'Homework', 'weight': 20.0, 'scores': [90, 85, 95], 'drop_lowest': 1},
            {'category': 'Midterm', 'weight': 30.0, 'scores': [88]},
            {'category': 'Final Exam', 'weight': 50.0, 'scores': [92]}
        ]
        """
        total_weighted_percentage = Decimal('0.00')
        total_active_weight = Decimal('0.00')
        breakdown = []

        for cat in category_grades:
            weight = Decimal(str(cat.get('weight', 0.0)))
            raw_scores = [Decimal(str(s)) for s in cat.get('scores', [])]
            drop_count = cat.get('drop_lowest', 0)

            if not raw_scores:
                continue

            # Drop lowest scores if requested
            sorted_scores = sorted(raw_scores)
            if drop_count > 0 and len(sorted_scores) > drop_count:
                active_scores = sorted_scores[drop_count:]
            else:
                active_scores = sorted_scores

            category_avg = sum(active_scores) / Decimal(str(len(active_scores)))
            weighted_contrib = (category_avg * (weight / Decimal('100.0'))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            total_weighted_percentage += weighted_contrib
            total_active_weight += weight

            breakdown.append({
                'category': cat.get('category'),
                'weight': weight,
                'average': category_avg.quantize(Decimal('0.01')),
                'weighted_contribution': weighted_contrib,
                'scores_evaluated': len(active_scores),
                'scores_dropped': len(raw_scores) - len(active_scores)
            })

        # Normalize if active weight < 100%
        if total_active_weight > Decimal('0.00') and total_active_weight < Decimal('100.00'):
            final_pct = (total_weighted_percentage / total_active_weight * Decimal('100.0')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        else:
            final_pct = total_weighted_percentage.quantize(Decimal('0.01'))

        return {
            'final_percentage': final_pct,
            'total_weight_evaluated': total_active_weight,
            'category_breakdown': breakdown
        }
