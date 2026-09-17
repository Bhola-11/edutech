"""
Degree Audit & Graduation Eligibility Policy Engine.
Validates General Education Core, Major Core, Major Electives, Residency Requirements, and Latin Honors.
"""
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List, Set


class DegreeAuditPolicy:
    MIN_BACHELOR_TOTAL_CREDITS = 120
    MIN_RESIDENCY_CREDITS_BACHELOR = 30
    MIN_FINAL_RESIDENCY_CREDITS = 30

    SUMMA_CUM_LAUDE_MIN_GPA = Decimal('3.90')
    MAGNA_CUM_LAUDE_MIN_GPA = Decimal('3.75')
    CUM_LAUDE_MIN_GPA = Decimal('3.50')

    GENED_REQUIREMENTS = {
        'COMMUNICATION': 6,
        'QUANTITATIVE': 6,
        'NATURAL_SCIENCES': 7,
        'HUMANITIES_ARTS': 6,
        'SOCIAL_BEHAVIORAL': 6,
        'GLOBAL_DIVERSITY': 3
    }
    GENED_TOTAL_MIN_CREDITS = 34

    @classmethod
    def audit_bachelor_degree(
        cls,
        cumulative_gpa: Decimal,
        major_gpa: Decimal,
        earned_credits_institutional: int,
        earned_credits_transfer: int,
        gened_completed: Dict[str, int],
        major_core_required_courses: Set[str],
        major_core_completed_courses: Set[str],
        major_elective_credits_required: int,
        major_elective_credits_completed: int,
        has_academic_integrity_violation: bool = False
    ) -> Dict[str, Any]:
        cgpa = Decimal(str(cumulative_gpa))
        mgpa = Decimal(str(major_gpa))
        total_credits = earned_credits_institutional + earned_credits_transfer

        total_credits_pass = total_credits >= cls.MIN_BACHELOR_TOTAL_CREDITS
        credits_deficit = max(0, cls.MIN_BACHELOR_TOTAL_CREDITS - total_credits)
        residency_pass = earned_credits_institutional >= cls.MIN_RESIDENCY_CREDITS_BACHELOR
        cgpa_pass = cgpa >= Decimal('2.00')
        mgpa_pass = mgpa >= Decimal('2.00')

        gened_status = {}
        gened_all_pass = True
        total_gened_credits = 0
        for category, required in cls.GENED_REQUIREMENTS.items():
            completed = gened_completed.get(category, 0)
            total_gened_credits += completed
            cat_pass = completed >= required
            if not cat_pass:
                gened_all_pass = False
            gened_status[category] = {
                'required': required,
                'completed': completed,
                'satisfied': cat_pass,
                'shortage': max(0, required - completed)
            }

        if total_gened_credits < cls.GENED_TOTAL_MIN_CREDITS:
            gened_all_pass = False

        missing_major_core = list(major_core_required_courses - major_core_completed_courses)
        major_core_pass = len(missing_major_core) == 0
        major_elective_pass = major_elective_credits_completed >= major_elective_credits_required

        is_cleared = (
            total_credits_pass and
            residency_pass and
            cgpa_pass and
            mgpa_pass and
            gened_all_pass and
            major_core_pass and
            major_elective_pass
        )

        latin_honors = None
        if is_cleared and not has_academic_integrity_violation:
            if cgpa >= cls.SUMMA_CUM_LAUDE_MIN_GPA:
                latin_honors = 'SUMMA_CUM_LAUDE'
            elif cgpa >= cls.MAGNA_CUM_LAUDE_MIN_GPA:
                latin_honors = 'MAGNA_CUM_LAUDE'
            elif cgpa >= cls.CUM_LAUDE_MIN_GPA:
                latin_honors = 'CUM_LAUDE'

        deficiencies = []
        if not total_credits_pass:
            deficiencies.append(f"Insufficient total credits: {total_credits}/{cls.MIN_BACHELOR_TOTAL_CREDITS} (Deficit: {credits_deficit}).")
        if not residency_pass:
            deficiencies.append(f"Institutional residency requirement not met: {earned_credits_institutional}/{cls.MIN_RESIDENCY_CREDITS_BACHELOR} credits.")
        if not cgpa_pass:
            deficiencies.append(f"Cumulative GPA {cgpa} below graduation threshold of 2.00.")
        if not mgpa_pass:
            deficiencies.append(f"Major GPA {mgpa} below graduation threshold of 2.00.")
        if not gened_all_pass:
            deficiencies.append("General Education curriculum requirements not fully satisfied.")
        if not major_core_pass:
            deficiencies.append(f"Missing mandatory major core courses: {', '.join(sorted(missing_major_core))}.")
        if not major_elective_pass:
            deficiencies.append(f"Major elective credits short: {major_elective_credits_completed}/{major_elective_credits_required}.")

        return {
            'is_cleared_for_graduation': is_cleared,
            'total_credits': total_credits,
            'institutional_credits': earned_credits_institutional,
            'transfer_credits': earned_credits_transfer,
            'cumulative_gpa': cgpa,
            'major_gpa': mgpa,
            'gened_status': gened_status,
            'missing_major_core': sorted(missing_major_core),
            'major_elective_satisfied': major_elective_pass,
            'latin_honors': latin_honors,
            'deficiencies': deficiencies
        }
