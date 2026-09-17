"""
International Student Visa & SEVIS Compliance Policy Engine.
Full-time credit tracking, CPT/OPT eligibility, and reduced course load authorizations under 8 CFR 214.2(f).
"""
from decimal import Decimal
from typing import Dict, Any, List, Optional


class InternationalStudentCompliancePolicy:
    MIN_FULLTIME_CREDITS_UNDERGRAD = 12
    MIN_FULLTIME_CREDITS_GRAD = 9
    MAX_ONLINE_CREDITS_COUNTABLE = 3

    RCL_REASONS = [
        'INITIAL_ACADEMIC_DIFFICULTY',
        'DOCUMENTED_MEDICAL_CONDITION',
        'FINAL_SEMESTER_GRADUATION'
    ]

    @classmethod
    def evaluate_enrollment_compliance(
        cls,
        visa_type: str,
        degree_level: str,
        in_person_credits: int,
        online_credits: int,
        is_final_semester: bool = False,
        approved_rcl_reason: Optional[str] = None
    ) -> Dict[str, Any]:
        if visa_type.upper() not in ['F-1', 'F1', 'J-1', 'J1']:
            return {
                'applies': False,
                'is_compliant': True,
                'status': 'EXEMPT',
                'reason': 'Student is not on an F-1 or J-1 non-immigrant visa.'
            }

        is_grad = degree_level.upper() in ['MS', 'MA', 'MBA', 'PHD', 'GRADUATE', 'MASTER', 'DOCTORAL']
        min_required = cls.MIN_FULLTIME_CREDITS_GRAD if is_grad else cls.MIN_FULLTIME_CREDITS_UNDERGRAD

        countable_online = min(online_credits, cls.MAX_ONLINE_CREDITS_COUNTABLE)
        qualifying_credits = in_person_credits + countable_online
        total_enrolled = in_person_credits + online_credits

        if approved_rcl_reason:
            if approved_rcl_reason in cls.RCL_REASONS:
                return {
                    'applies': True,
                    'is_compliant': True,
                    'status': 'AUTHORIZED_RCL',
                    'total_enrolled': total_enrolled,
                    'qualifying_credits': qualifying_credits,
                    'reason': f'Approved Reduced Course Load under category: {approved_rcl_reason}.'
                }

        if is_final_semester and total_enrolled > 0:
            if in_person_credits >= 1:
                return {
                    'applies': True,
                    'is_compliant': True,
                    'status': 'FINAL_SEMESTER_CLEARANCE',
                    'total_enrolled': total_enrolled,
                    'qualifying_credits': qualifying_credits,
                    'reason': 'Final term enrollment verified with mandatory in-person component.'
                }
            else:
                return {
                    'applies': True,
                    'is_compliant': False,
                    'status': 'VIOLATION_ONLINE_ONLY_FINAL_TERM',
                    'total_enrolled': total_enrolled,
                    'qualifying_credits': qualifying_credits,
                    'reason': 'SEVIS violation: Student cannot take only online courses in final semester.'
                }

        is_compliant = qualifying_credits >= min_required

        return {
            'applies': True,
            'is_compliant': is_compliant,
            'status': 'IN_STATUS' if is_compliant else 'SEVIS_STATUS_JEOPARDY',
            'degree_level': degree_level,
            'min_required_credits': min_required,
            'total_enrolled': total_enrolled,
            'qualifying_credits': qualifying_credits,
            'in_person_credits': in_person_credits,
            'online_credits': online_credits,
            'reason': 'Full-time study load compliant.' if is_compliant else f'Under-enrolled: {qualifying_credits}/{min_required} qualifying credits.'
        }
