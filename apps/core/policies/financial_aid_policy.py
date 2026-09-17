"""
Financial Aid Satisfactory Academic Progress (SAP) & Federal Title IV Policy Engine.
Complies with Higher Education Act (HEA) Section 484 and 34 CFR 668.34.
"""
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class SAPEvaluationResult:
    is_eligible: bool
    status: str
    qualitative_pass: bool
    quantitative_pass: bool
    maximum_timeframe_pass: bool
    cumulative_gpa: Decimal
    completion_rate: Decimal
    attempted_credits: Decimal
    completed_credits: Decimal
    max_allowable_credits: Decimal
    reasons: List[str]
    required_actions: List[str]


class FinancialAidPolicy:
    """
    Evaluates Title IV Federal and Institutional Financial Aid eligibility,
    Satisfactory Academic Progress (SAP), Pell Grant proration, and loan amortization.
    """
    MIN_GPA_UNDERGRADUATE = Decimal('2.00')
    MIN_GPA_GRADUATE = Decimal('3.00')
    MIN_GPA_DOCTORAL = Decimal('3.20')

    MIN_COMPLETION_RATE = Decimal('67.0')  # 67% standard pace
    MAX_TIMEFRAME_MULTIPLIER = Decimal('1.50')  # 150% maximum timeframe

    STATUS_MEETING = 'MEETING_SAP'
    STATUS_WARNING = 'SAP_WARNING'
    STATUS_SUSPENSION = 'SAP_SUSPENSION'
    STATUS_PROBATION = 'SAP_PROBATION'
    STATUS_ACADEMIC_PLAN = 'SAP_ACADEMIC_PLAN'

    MAX_PELL_LEU_PERCENT = Decimal('600.0')

    @classmethod
    def evaluate_sap(
        cls,
        degree_level: str,
        cumulative_gpa: Decimal,
        attempted_credits: Decimal,
        completed_credits: Decimal,
        program_required_credits: Decimal,
        previous_status: Optional[str] = None,
        has_approved_appeal: bool = False,
        is_on_academic_plan: bool = False
    ) -> SAPEvaluationResult:
        cgpa = Decimal(str(cumulative_gpa))
        attempted = Decimal(str(attempted_credits))
        completed = Decimal(str(completed_credits))
        prog_credits = Decimal(str(program_required_credits))

        if degree_level.upper() in ['PHD', 'DOCTORAL', 'DBA', 'EDD']:
            min_gpa = cls.MIN_GPA_DOCTORAL
        elif degree_level.upper() in ['MS', 'MA', 'MBA', 'MED', 'GRADUATE', 'MASTER']:
            min_gpa = cls.MIN_GPA_GRADUATE
        else:
            min_gpa = cls.MIN_GPA_UNDERGRADUATE

        qualitative_pass = cgpa >= min_gpa

        if attempted > Decimal('0'):
            completion_rate = (completed / attempted * Decimal('100')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        else:
            completion_rate = Decimal('100.00')
        quantitative_pass = completion_rate >= cls.MIN_COMPLETION_RATE

        max_allowable_credits = (prog_credits * cls.MAX_TIMEFRAME_MULTIPLIER).quantize(Decimal('0.1'))
        max_timeframe_pass = attempted <= max_allowable_credits

        reasons = []
        required_actions = []

        if not qualitative_pass:
            reasons.append(f"Cumulative GPA {cgpa} is below minimum standard of {min_gpa} for {degree_level}.")
        if not quantitative_pass:
            reasons.append(f"Pace of completion {completion_rate}% is below federal 67% threshold.")
        if not max_timeframe_pass:
            reasons.append(f"Attempted credits {attempted} exceed 150% maximum timeframe limit ({max_allowable_credits} credits).")

        all_passed = qualitative_pass and quantitative_pass and max_timeframe_pass

        if all_passed:
            status = cls.STATUS_MEETING
            is_eligible = True
        elif not max_timeframe_pass:
            status = cls.STATUS_SUSPENSION
            is_eligible = False
            required_actions.append("File maximum timeframe appeal with comprehensive graduation plan certified by academic advisor.")
        elif previous_status == cls.STATUS_MEETING or previous_status is None:
            status = cls.STATUS_WARNING
            is_eligible = True
            required_actions.append("Financial aid warning period granted. Must achieve standard by end of upcoming semester.")
        elif previous_status == cls.STATUS_WARNING:
            if has_approved_appeal:
                if is_on_academic_plan:
                    status = cls.STATUS_ACADEMIC_PLAN
                    is_eligible = True
                    required_actions.append("Aid maintained under formal Academic Improvement Plan. Must meet plan milestones.")
                else:
                    status = cls.STATUS_PROBATION
                    is_eligible = True
                    required_actions.append("Aid reinstated on financial aid probation for one term.")
            else:
                status = cls.STATUS_SUSPENSION
                is_eligible = False
                required_actions.append("Submit formal SAP appeal with documentation of extenuating circumstances.")
        elif previous_status in [cls.STATUS_PROBATION, cls.STATUS_ACADEMIC_PLAN]:
            if has_approved_appeal and is_on_academic_plan:
                status = cls.STATUS_ACADEMIC_PLAN
                is_eligible = True
            else:
                status = cls.STATUS_SUSPENSION
                is_eligible = False
                required_actions.append("Academic plan goals not satisfied. Immediate suspension of Title IV financial aid.")
        else:
            status = cls.STATUS_SUSPENSION
            is_eligible = False
            required_actions.append("File appeal with Financial Aid Appeals Committee.")

        return SAPEvaluationResult(
            is_eligible=is_eligible,
            status=status,
            qualitative_pass=qualitative_pass,
            quantitative_pass=quantitative_pass,
            maximum_timeframe_pass=max_timeframe_pass,
            cumulative_gpa=cgpa,
            completion_rate=completion_rate,
            attempted_credits=attempted,
            completed_credits=completed,
            max_allowable_credits=max_allowable_credits,
            reasons=reasons,
            required_actions=required_actions
        )

    @classmethod
    def calculate_pell_grant(
        cls,
        scheduled_award: Decimal,
        enrolled_credits: int,
        student_aid_index: Decimal,
        lifetime_eligibility_used_percent: Decimal = Decimal('0.0')
    ) -> Dict[str, Any]:
        award = Decimal(str(scheduled_award))
        credits = int(enrolled_credits)
        sai = Decimal(str(student_aid_index))
        leu = Decimal(str(lifetime_eligibility_used_percent))

        if leu >= cls.MAX_PELL_LEU_PERCENT:
            return {
                'eligible': False,
                'term_disbursement': Decimal('0.00'),
                'enrollment_intensity_pct': Decimal('0.00'),
                'remaining_leu_percent': Decimal('0.00'),
                'reason': 'Maximum Lifetime Eligibility Used (600% LEU) reached.'
            }

        if credits >= 12:
            intensity_pct = Decimal('100.0')
        elif credits >= 9:
            intensity_pct = Decimal('75.0')
        elif credits >= 6:
            intensity_pct = Decimal('50.0')
        elif credits >= 1:
            intensity_pct = Decimal('25.0')
        else:
            intensity_pct = Decimal('0.0')

        if intensity_pct == Decimal('0.0'):
            return {
                'eligible': False,
                'term_disbursement': Decimal('0.00'),
                'enrollment_intensity_pct': Decimal('0.00'),
                'remaining_leu_percent': (cls.MAX_PELL_LEU_PERCENT - leu).quantize(Decimal('0.01')),
                'reason': 'Zero enrolled credit hours.'
            }

        semester_base = award / Decimal('2.0')
        term_disbursement = (semester_base * (intensity_pct / Decimal('100.0'))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        term_leu_impact = ((intensity_pct / Decimal('100.0')) * Decimal('50.0')).quantize(Decimal('0.01'))
        remaining_leu = max(Decimal('0.00'), cls.MAX_PELL_LEU_PERCENT - leu - term_leu_impact)

        return {
            'eligible': True,
            'term_disbursement': term_disbursement,
            'enrollment_intensity_pct': intensity_pct,
            'term_leu_impact': term_leu_impact,
            'remaining_leu_percent': remaining_leu,
            'reason': 'Eligible for Federal Pell Grant disbursement.'
        }

    @classmethod
    def evaluate_scholarship_retention(
        cls,
        scholarship_tier: str,
        cumulative_gpa: Decimal,
        annual_earned_credits: int
    ) -> Dict[str, Any]:
        cgpa = Decimal(str(cumulative_gpa))
        credits = int(annual_earned_credits)

        thresholds = {
            'PRESIDENTIAL': {'min_gpa': Decimal('3.80'), 'min_credits': 30, 'award_amount': Decimal('15000.00')},
            'PROVOST': {'min_gpa': Decimal('3.50'), 'min_credits': 30, 'award_amount': Decimal('10000.00')},
            'DEANS_EXCELLENCE': {'min_gpa': Decimal('3.20'), 'min_credits': 24, 'award_amount': Decimal('6000.00')},
            'FOUNDATION_STEM': {'min_gpa': Decimal('3.00'), 'min_credits': 24, 'award_amount': Decimal('5000.00')},
            'INSTITUTIONAL_OPPORTUNITY': {'min_gpa': Decimal('2.50'), 'min_credits': 24, 'award_amount': Decimal('3000.00')}
        }

        tier = scholarship_tier.upper()
        if tier not in thresholds:
            return {
                'retained': False,
                'status': 'UNKNOWN_TIER',
                'reason': f'Scholarship tier {tier} not recognized in institutional catalog.'
            }

        rule = thresholds[tier]
        gpa_pass = cgpa >= rule['min_gpa']
        credits_pass = credits >= rule['min_credits']

        if gpa_pass and credits_pass:
            return {
                'retained': True,
                'status': 'RENEWED',
                'award_amount': rule['award_amount'],
                'reason': f'All renewal criteria satisfied for {tier} scholarship.'
            }
        elif gpa_pass and not credits_pass:
            return {
                'retained': False,
                'status': 'CREDIT_DEFICIENCY_PROBATION',
                'award_amount': Decimal('0.00'),
                'reason': f'Earned {credits} credits; required {rule["min_credits"]} credits. Eligible for summer catch-up.'
            }
        elif not gpa_pass and credits_pass:
            return {
                'retained': False,
                'status': 'GPA_DEFICIENCY_WARNING',
                'award_amount': Decimal('0.00'),
                'reason': f'Cumulative GPA {cgpa} is below renewal minimum of {rule["min_gpa"]}.'
            }
        else:
            return {
                'retained': False,
                'status': 'REVOKED',
                'award_amount': Decimal('0.00'),
                'reason': f'Failed both GPA ({cgpa} < {rule["min_gpa"]}) and credit minimums ({credits} < {rule["min_credits"]}).'
            }
