from decimal import Decimal

class CreditTransferPolicy:
    MIN_TRANSFER_GRADE = 'C'
    MIN_GRADE_POINTS = Decimal('2.00')
    MAX_TRANSFER_PERCENTAGE = Decimal('0.50')  # Max 50% credits can be transferred

    GRADE_POINTS = {
        'A+': Decimal('4.00'), 'A': Decimal('4.00'), 'A-': Decimal('3.70'),
        'B+': Decimal('3.30'), 'B': Decimal('3.00'), 'B-': Decimal('2.70'),
        'C+': Decimal('2.30'), 'C': Decimal('2.00'), 'C-': Decimal('1.70'),
        'D+': Decimal('1.30'), 'D': Decimal('1.00'), 'F': Decimal('0.00')
    }

    @classmethod
    def evaluate_course_transfer(cls, external_course_title, external_credits, external_grade, syllabus_overlap_pct):
        earned_points = cls.GRADE_POINTS.get(external_grade.upper(), Decimal('0.00'))
        if earned_points < cls.MIN_GRADE_POINTS:
            return {
                'is_approved': False,
                'awarded_credits': Decimal('0.0'),
                'rejection_reason': f'Grade {external_grade} does not satisfy the minimum required collegiate transfer grade of {cls.MIN_TRANSFER_GRADE} (2.00 GPA).'
            }

        if syllabus_overlap_pct < 75.0:
            return {
                'is_approved': False,
                'awarded_credits': Decimal('0.0'),
                'rejection_reason': f'Syllabus alignment ({syllabus_overlap_pct}%) is below the mandatory 75% curriculum equivalence threshold.'
            }

        awarded_credits = min(Decimal(str(external_credits)), Decimal('4.0'))
        return {
            'is_approved': True,
            'awarded_credits': awarded_credits,
            'rejection_reason': None
        }

    @classmethod
    def evaluate_total_transfer_limit(cls, current_transferred_credits, proposed_credits, total_degree_credits):
        total_limit = Decimal(str(total_degree_credits)) * cls.MAX_TRANSFER_PERCENTAGE
        projected = Decimal(str(current_transferred_credits)) + Decimal(str(proposed_credits))

        if projected > total_limit:
            allowed = max(Decimal('0.0'), total_limit - Decimal(str(current_transferred_credits)))
            return {
                'is_within_limit': False,
                'max_allowable_transfer_credits': total_limit,
                'remaining_transferable_credits': allowed
            }
        return {
            'is_within_limit': True,
            'max_allowable_transfer_credits': total_limit,
            'remaining_transferable_credits': total_limit - projected
        }
