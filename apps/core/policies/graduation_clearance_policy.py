from decimal import Decimal

class GraduationClearancePolicy:
    MIN_CUMULATIVE_GPA = Decimal('2.00')

    @classmethod
    def evaluate_graduation_clearance(cls, total_credits_earned, required_credits, cumulative_gpa, has_financial_holds=False, has_library_holds=False, has_disciplinary_holds=False):
        cgpa = Decimal(str(cumulative_gpa))
        credits_earned = Decimal(str(total_credits_earned))
        req_credits = Decimal(str(required_credits))

        issues = []
        if credits_earned < req_credits:
            issues.append(f'Credit deficit: Earned {credits_earned}/{req_credits} credits.')

        if cgpa < cls.MIN_CUMULATIVE_GPA:
            issues.append(f'GPA requirement unmet: Current cumulative GPA is {cgpa} (Minimum required: 2.00).')

        if has_financial_holds:
            issues.append('Outstanding bursar/financial balance hold prevents graduation clearance.')

        if has_library_holds:
            issues.append('Unreturned library materials hold active on student record.')

        if has_disciplinary_holds:
            issues.append('Pending campus judicial or academic integrity disciplinary action.')

        is_cleared = len(issues) == 0

        honors_distinction = None
        if is_cleared:
            if cgpa >= Decimal('3.90'):
                honors_distinction = 'Summa Cum Laude (Highest Honors)'
            elif cgpa >= Decimal('3.75'):
                honors_distinction = 'Magna Cum Laude (High Honors)'
            elif cgpa >= Decimal('3.50'):
                honors_distinction = 'Cum Laude (Honors)'

        return {
            'is_cleared_for_graduation': is_cleared,
            'honors_distinction': honors_distinction,
            'outstanding_issues': issues,
            'credits_satisfied': credits_earned >= req_credits,
            'gpa_satisfied': cgpa >= cls.MIN_CUMULATIVE_GPA
        }
