"""
Generator script for higher education policy engines in apps/core/policies/
"""
import os

POLICY_DIR = os.path.join(os.path.dirname(__file__), '..', 'apps', 'core', 'policies')
os.makedirs(POLICY_DIR, exist_ok=True)

# 1. Financial Aid Policy
FINANCIAL_AID_CODE = '''"""
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
'''

# 2. Faculty Workload Policy
FACULTY_WORKLOAD_CODE = '''"""
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
'''

# 3. Degree Audit Policy
DEGREE_AUDIT_CODE = '''"""
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
'''

# 4. Academic Integrity Policy
ACADEMIC_INTEGRITY_CODE = '''"""
Academic Integrity & Honor Code Policy Engine.
Adjudication tiers, sanction determination, and appeal workflows.
"""
from typing import Dict, Any, List


class AcademicIntegrityPolicy:
    LEVEL_1_MINOR = 'LEVEL_1_MINOR'
    LEVEL_2_MODERATE = 'LEVEL_2_MODERATE'
    LEVEL_3_MAJOR = 'LEVEL_3_MAJOR'
    LEVEL_4_EGREGIOUS = 'LEVEL_4_EGREGIOUS'

    CAT_PLAGIARISM = 'PLAGIARISM'
    CAT_UNAUTHORIZED_COLLABORATION = 'UNAUTHORIZED_COLLABORATION'
    CAT_FABRICATION_FALSIFICATION = 'FABRICATION_FALSIFICATION'
    CAT_EXAM_CHEATING = 'EXAM_CHEATING'
    CAT_CONTRACT_CHEATING = 'CONTRACT_CHEATING'
    CAT_RECORD_TAMPERING = 'RECORD_TAMPERING'

    SANCTIONS = {
        LEVEL_1_MINOR: {
            'academic_penalty': 'Zero on assignment; optional resubmission for max 70% credit.',
            'disciplinary_penalty': 'Official written reprimand; mandatory Academic Citation Workshop.',
            'transcript_notation': False,
            'record_retention_years': 1
        },
        LEVEL_2_MODERATE: {
            'academic_penalty': 'Grade of 0 on assessment; overall course letter grade lowered by one step.',
            'disciplinary_penalty': 'Probationary honor standing; mandatory ethics seminar completion.',
            'transcript_notation': False,
            'record_retention_years': 3
        },
        LEVEL_3_MAJOR: {
            'academic_penalty': 'Permanent grade of "XF" (failure due to academic dishonesty) for course.',
            'disciplinary_penalty': 'Suspension from institution for 1 to 2 academic semesters.',
            'transcript_notation': True,
            'record_retention_years': 7
        },
        LEVEL_4_EGREGIOUS: {
            'academic_penalty': 'Immediate expulsion and revocation of any pending degree or honors.',
            'disciplinary_penalty': 'Permanent expulsion; campus persona non grata ban.',
            'transcript_notation': True,
            'record_retention_years': 99
        }
    }

    @classmethod
    def evaluate_violation(
        cls,
        category: str,
        prior_violation_count: int,
        is_commercial_or_proxy: bool = False,
        is_formal_exam: bool = False,
        grade_weight_percentage: float = 10.0
    ) -> Dict[str, Any]:
        if prior_violation_count >= 2 or is_commercial_or_proxy:
            level = cls.LEVEL_4_EGREGIOUS
        elif prior_violation_count == 1:
            level = cls.LEVEL_3_MAJOR
        elif is_formal_exam and grade_weight_percentage >= 20.0:
            level = cls.LEVEL_3_MAJOR
        elif grade_weight_percentage >= 15.0 or category in [cls.CAT_FABRICATION_FALSIFICATION, cls.CAT_EXAM_CHEATING]:
            level = cls.LEVEL_2_MODERATE
        else:
            level = cls.LEVEL_1_MINOR

        sanction = cls.SANCTIONS[level]

        return {
            'category': category,
            'level': level,
            'prior_violations': prior_violation_count,
            'academic_penalty': sanction['academic_penalty'],
            'disciplinary_penalty': sanction['disciplinary_penalty'],
            'transcript_notation': sanction['transcript_notation'],
            'record_retention_years': sanction['record_retention_years'],
            'requires_board_hearing': level in [cls.LEVEL_3_MAJOR, cls.LEVEL_4_EGREGIOUS],
            'notice_deadline_days': 5,
            'appeal_filing_window_days': 10
        }
'''

# 5. Disability Accommodations Policy
DISABILITY_ACCOMMODATIONS_CODE = '''"""
Disability Accommodations & Section 504 / ADA Compliance Policy Engine.
Evaluates reasonable academic accommodations, exam adaptations, and documentation cycles.
"""
from decimal import Decimal
from typing import Dict, Any, List


class DisabilityAccommodationsPolicy:
    TIME_AND_A_HALF = Decimal('1.50')
    DOUBLE_TIME = Decimal('2.00')

    APPROVED_ACCOMMODATIONS = {
        'EXTENDED_EXAM_TIME_1_5X': '50% additional time on all timed quizzes, midterms, and final examinations.',
        'EXTENDED_EXAM_TIME_2_0X': '100% additional time on all timed quizzes, midterms, and final examinations.',
        'DISTRACTION_REDUCED_ROOM': 'Testing in proctored, distraction-reduced testing environment (max 10 occupants).',
        'SCREEN_READER_COMPATIBLE': 'Exams and course materials in screen-reader accessible digital format (WCAG 2.1 AA).',
        'SCRIBE_ASSISTANCE': 'Provision of human scribe for recorded verbal examination responses.',
        'PEER_NOTETAKER': 'Access to designated peer note-taker or automated AI lecture audio transcription.',
        'RECORDING_AUTHORIZATION': 'Authorization to record lecture audio for personal study purposes only.',
        'PREFERENTIAL_SEATING': 'Reserved seating in front row near whiteboard and audio amplification.',
        'ATTENDANCE_FLEXIBILITY': 'Reasonable consideration for short-term episodic disability flare-up absences.'
    }

    @classmethod
    def calculate_exam_duration(
        cls,
        standard_duration_minutes: int,
        accommodation_codes: List[str]
    ) -> Dict[str, Any]:
        multiplier = Decimal('1.00')
        if 'EXTENDED_EXAM_TIME_2_0X' in accommodation_codes:
            multiplier = cls.DOUBLE_TIME
        elif 'EXTENDED_EXAM_TIME_1_5X' in accommodation_codes:
            multiplier = cls.TIME_AND_A_HALF

        adjusted_minutes = int(Decimal(str(standard_duration_minutes)) * multiplier)
        needs_separate_room = 'DISTRACTION_REDUCED_ROOM' in accommodation_codes
        needs_assistive_tech = any(code in accommodation_codes for code in ['SCREEN_READER_COMPATIBLE', 'SCRIBE_ASSISTANCE'])

        return {
            'standard_minutes': standard_duration_minutes,
            'multiplier': float(multiplier),
            'adjusted_minutes': adjusted_minutes,
            'requires_separate_testing_room': needs_separate_room,
            'requires_assistive_technology': needs_assistive_tech
        }
'''

# 6. International Student Compliance Policy
INTERNATIONAL_STUDENT_CODE = '''"""
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
'''

POLICIES = {
    'financial_aid_policy.py': FINANCIAL_AID_CODE,
    'faculty_workload_policy.py': FACULTY_WORKLOAD_CODE,
    'degree_audit_policy.py': DEGREE_AUDIT_CODE,
    'academic_integrity_policy.py': ACADEMIC_INTEGRITY_CODE,
    'disability_accommodations_policy.py': DISABILITY_ACCOMMODATIONS_CODE,
    'international_student_compliance.py': INTERNATIONAL_STUDENT_CODE,
}

for filename, content in POLICIES.items():
    filepath = os.path.join(POLICY_DIR, filename)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created policy: {filename}")

print("Policy engine generation complete.")
