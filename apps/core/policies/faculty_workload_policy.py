"""
Faculty Workload Allocation & Productivity Policy Engine.
Standardized Teaching Credit Units, Research Releases, Service Apportionment, and Overload Calculations.
"""
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List, Optional


class FacultyWorkloadPolicy:
    ANNUAL_STANDARD_WORKLOAD_UNITS = Decimal('24.0')
    SEMESTER_STANDARD_WORKLOAD_UNITS = Decimal('12.0')
    MAX_PERMISSIBLE_OVERLOAD_UNITS = Decimal('3.0')

    LECTURE_WU_PER_CREDIT = Decimal('1.00')
    LAB_WU_PER_CONTACT_HOUR = Decimal('0.75')
    CLINICAL_STUDIO_WU_PER_HOUR = Decimal('0.80')
    GRADUATE_COURSE_MULTIPLIER = Decimal('1.25')

    UNDERGRAD_THESIS_WU = Decimal('0.10')
    MASTERS_THESIS_WU = Decimal('0.25')
    PHD_DISSERTATION_CHAIR_WU = Decimal('0.50')
    PHD_DISSERTATION_COMMITTEE_WU = Decimal('0.15')

    RELEASE_DEPT_CHAIR = Decimal('6.0')
    RELEASE_PROGRAM_DIRECTOR = Decimal('3.0')
    RELEASE_RESEARCH_PER_50K = Decimal('3.0')

    @classmethod
    def calculate_course_workload_units(
        cls,
        credit_hours: int,
        contact_hours_lecture: int,
        contact_hours_lab: int,
        is_graduate: bool = False,
        enrolled_students: int = 0
    ) -> Decimal:
        lecture_wu = Decimal(str(contact_hours_lecture)) * cls.LECTURE_WU_PER_CREDIT
        lab_wu = Decimal(str(contact_hours_lab)) * cls.LAB_WU_PER_CONTACT_HOUR
        base_wu = lecture_wu + lab_wu

        if is_graduate:
            base_wu *= cls.GRADUATE_COURSE_MULTIPLIER

        if enrolled_students >= 200:
            base_wu += Decimal('2.0')
        elif enrolled_students >= 100:
            base_wu += Decimal('1.0')
        elif enrolled_students >= 60:
            base_wu += Decimal('0.5')

        return base_wu.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

    @classmethod
    def calculate_faculty_term_workload(
        cls,
        faculty_rank: str,
        courses: List[Dict[str, Any]],
        undergrad_advisees_thesis: int = 0,
        masters_thesis_students: int = 0,
        phd_dissertation_chairs: int = 0,
        phd_committee_memberships: int = 0,
        administrative_role: Optional[str] = None,
        sponsored_research_funding: Decimal = Decimal('0.0'),
        base_annual_salary: Decimal = Decimal('80000.00')
    ) -> Dict[str, Any]:
        teaching_wu = Decimal('0.00')
        for c in courses:
            wu = cls.calculate_course_workload_units(
                credit_hours=c.get('credit_hours', 3),
                contact_hours_lecture=c.get('lecture_hours', 3),
                contact_hours_lab=c.get('lab_hours', 0),
                is_graduate=c.get('is_graduate', False),
                enrolled_students=c.get('enrolled_students', 25)
            )
            teaching_wu += wu

        supervision_wu = (
            Decimal(str(undergrad_advisees_thesis)) * cls.UNDERGRAD_THESIS_WU +
            Decimal(str(masters_thesis_students)) * cls.MASTERS_THESIS_WU +
            Decimal(str(phd_dissertation_chairs)) * cls.PHD_DISSERTATION_CHAIR_WU +
            Decimal(str(phd_committee_memberships)) * cls.PHD_DISSERTATION_COMMITTEE_WU
        ).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        admin_wu = Decimal('0.00')
        if administrative_role:
            role = administrative_role.upper()
            if 'CHAIR' in role:
                admin_wu += cls.RELEASE_DEPT_CHAIR
            elif 'DIRECTOR' in role or 'COORDINATOR' in role:
                admin_wu += cls.RELEASE_PROGRAM_DIRECTOR
            elif 'DEAN' in role:
                admin_wu += Decimal('9.0')

        funding = Decimal(str(sponsored_research_funding))
        research_release_units = (funding / Decimal('50000.00')).quantize(Decimal('1.0')) * cls.RELEASE_RESEARCH_PER_50K
        research_release_units = min(research_release_units, Decimal('6.0'))

        total_wu = (teaching_wu + supervision_wu + admin_wu + research_release_units).quantize(Decimal('0.01'))
        workload_delta = total_wu - cls.SEMESTER_STANDARD_WORKLOAD_UNITS

        is_overload = workload_delta > Decimal('0.0')
        is_underload = workload_delta < Decimal('-0.5')

        overload_units = max(Decimal('0.00'), min(workload_delta, cls.MAX_PERMISSIBLE_OVERLOAD_UNITS))
        excess_unapproved_units = max(Decimal('0.00'), workload_delta - cls.MAX_PERMISSIBLE_OVERLOAD_UNITS)

        wu_rate = (base_annual_salary / Decimal('24.0') * Decimal('0.85')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        overload_compensation = (overload_units * wu_rate).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

        return {
            'faculty_rank': faculty_rank,
            'teaching_workload_units': teaching_wu,
            'supervision_units': supervision_wu,
            'administrative_release_units': admin_wu,
            'research_release_units': research_release_units,
            'total_workload_units': total_wu,
            'standard_target_units': cls.SEMESTER_STANDARD_WORKLOAD_UNITS,
            'workload_delta': workload_delta,
            'status': 'OVERLOAD' if is_overload else ('UNDERLOAD' if is_underload else 'BALANCED'),
            'overload_units_payable': overload_units,
            'excess_unapproved_units': excess_unapproved_units,
            'overload_compensation': overload_compensation,
            'requires_provost_waiver': excess_unapproved_units > Decimal('0.0')
        }
