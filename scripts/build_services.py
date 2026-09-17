"""
Build enterprise services across accounts, institutions, courses, enrollments, and profiles.
"""
import os

SERVICES = {
    # 1. Accounts Services
    'apps/accounts/services/__init__.py': '"""Accounts services package."""\n',
    'apps/accounts/services/mfa_service.py': '''"""
Multi-Factor Authentication (MFA / 2FA) Service.
Implements RFC 6238 TOTP generation, validation, drift windows, and backup codes.
"""
import hmac
import hashlib
import time
import base64
import struct
import secrets
from typing import Tuple, List, Optional
from django.utils import timezone


class MFAService:
    DIGITS = 6
    INTERVAL = 30  # 30-second TOTP step
    BACKUP_CODE_COUNT = 10
    BACKUP_CODE_LENGTH = 10

    @classmethod
    def generate_secret(cls) -> str:
        """Generates a secure 32-character base32 secret key."""
        random_bytes = secrets.token_bytes(20)
        return base64.b32encode(random_bytes).decode('utf-8').rstrip('=')

    @classmethod
    def generate_provisioning_uri(cls, username: str, secret: str, issuer: str = 'EduTech Enterprise') -> str:
        """Generates otpauth URI for authenticator apps (Google Authenticator, Authy, 1Password)."""
        import urllib.parse
        encoded_issuer = urllib.parse.quote(issuer)
        encoded_user = urllib.parse.quote(username)
        return f"otpauth://totp/{encoded_issuer}:{encoded_user}?secret={secret}&issuer={encoded_issuer}&algorithm=SHA1&digits={cls.DIGITS}&period={cls.INTERVAL}"

    @classmethod
    def generate_totp_token(cls, secret: str, time_step: Optional[int] = None) -> str:
        """Computes current RFC 6238 TOTP code."""
        if time_step is None:
            time_step = int(time.time()) // cls.INTERVAL

        # Normalize secret padding
        padded_secret = secret.upper() + '=' * ((8 - len(secret) % 8) % 8)
        key = base64.b32decode(padded_secret, casefold=True)

        counter_bytes = struct.pack('>Q', time_step)
        hmac_digest = hmac.new(key, counter_bytes, hashlib.sha1).digest()

        offset = hmac_digest[-1] & 0x0F
        binary = struct.unpack('>I', hmac_digest[offset:offset+4])[0] & 0x7FFFFFFF
        code = binary % (10 ** cls.DIGITS)
        return str(code).zfill(cls.DIGITS)

    @classmethod
    def verify_totp(cls, secret: str, token: str, window: int = 1) -> bool:
        """Verifies code allowing for time drift (window * 30 seconds back and forward)."""
        clean_token = token.strip().replace(' ', '')
        if len(clean_token) != cls.DIGITS or not clean_token.isdigit():
            return False

        current_step = int(time.time()) // cls.INTERVAL
        for drift in range(-window, window + 1):
            valid_code = cls.generate_totp_token(secret, time_step=current_step + drift)
            if hmac.compare_digest(clean_token, valid_code):
                return True
        return False

    @classmethod
    def generate_backup_recovery_codes(cls) -> List[str]:
        """Generates single-use alphanumeric emergency recovery codes."""
        codes = []
        for _ in range(cls.BACKUP_CODE_COUNT):
            code = secrets.token_hex(cls.BACKUP_CODE_LENGTH // 2).upper()
            formatted = f"{code[:5]}-{code[5:]}"
            codes.append(formatted)
        return codes
''',
    'apps/accounts/services/audit_service.py': '''"""
Enterprise Security Audit Logging Service.
Captures authentication events, IP addresses, suspicious role changes, and compliance trails.
"""
from typing import Optional, Dict, Any
from django.utils import timezone
from apps.core.models import ActivityLog


class SecurityAuditService:
    @classmethod
    def log_auth_event(
        cls,
        user,
        event_type: str,
        ip_address: str,
        user_agent: str,
        status: str = 'SUCCESS',
        metadata: Optional[Dict[str, Any]] = None
    ) -> ActivityLog:
        """Logs user authentication, login attempts, MFA challenges, and logout."""
        description = f"Auth Event: {event_type} - Status: {status} from IP {ip_address}"
        return ActivityLog.objects.create(
            actor=user,
            action=event_type,
            target_model='User',
            target_id=str(user.pk) if user else 'ANONYMOUS',
            ip_address=ip_address,
            user_agent=user_agent[:500] if user_agent else '',
            payload={
                'status': status,
                'timestamp': timezone.now().isoformat(),
                **(metadata or {})
            }
        )

    @classmethod
    def log_role_change(
        cls,
        admin_user,
        target_user,
        old_role: str,
        new_role: str,
        reason: str = ''
    ) -> ActivityLog:
        """Logs critical RBAC privilege changes and role promotions."""
        return ActivityLog.objects.create(
            actor=admin_user,
            action='ROLE_MODIFICATION',
            target_model='User',
            target_id=str(target_user.pk),
            payload={
                'target_username': target_user.username,
                'old_role': old_role,
                'new_role': new_role,
                'reason': reason,
                'elevated_by': admin_user.username if admin_user else 'SYSTEM'
            }
        )
''',

    # 2. Institutions Services
    'apps/institutions/services/__init__.py': '"""Institutions services package."""\n',
    'apps/institutions/services/facilities_booking_service.py': '''"""
Campus Facilities & Classroom Booking Service.
Conflict detection, capacity validation, equipment matching, and schedule optimization.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, time
from django.db.models import Q
from apps.institutions.models import Classroom


class FacilitiesBookingService:
    @classmethod
    def find_available_classrooms(
        cls,
        institution_id: int,
        required_capacity: int,
        room_type: Optional[str] = None,
        has_projector: bool = False,
        has_audio_system: bool = False
    ) -> List[Dict[str, Any]]:
        """Filters institution classrooms that satisfy capacity and equipment requirements."""
        qs = Classroom.objects.filter(
            institution_id=institution_id,
            capacity__gte=required_capacity,
            is_active=True
        )
        if room_type:
            qs = qs.filter(room_type=room_type)
        if has_projector:
            qs = qs.filter(has_projector=True)
        if has_audio_system:
            qs = qs.filter(has_audio_system=True)

        results = []
        for room in qs.order_by('capacity'):
            utilization_rate = round((required_capacity / room.capacity) * 100, 1)
            results.append({
                'id': room.id,
                'code': room.room_number,
                'name': room.name,
                'building': room.building,
                'capacity': room.capacity,
                'room_type': room.room_type,
                'utilization_rate_projected': utilization_rate,
                'is_optimal_fit': 70.0 <= utilization_rate <= 100.0
            })
        return results

    @classmethod
    def check_time_slot_conflict(
        cls,
        start_time_a: time,
        end_time_a: time,
        start_time_b: time,
        end_time_b: time
    ) -> bool:
        """Determines whether two time slots overlap on the same day."""
        return max(start_time_a, start_time_b) < min(end_time_a, end_time_b)
''',
    'apps/institutions/services/department_metrics_service.py': '''"""
Academic Department Performance & Faculty Allocation Metrics Service.
Computes Student-to-Faculty ratios, course fill rates, and credit distribution.
"""
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any
from apps.institutions.models import AcademicDepartment
from apps.courses.models import Course, CourseInstructorAllocation
from apps.enrollments.models import StudentEnrollment


class DepartmentMetricsService:
    @classmethod
    def calculate_department_kpis(cls, department_id: int) -> Dict[str, Any]:
        """Calculates key institutional performance indicators for an academic department."""
        dept = AcademicDepartment.objects.filter(id=department_id).first()
        if not dept:
            return {'error': 'Department not found'}

        courses_count = Course.objects.filter(department=dept, is_active=True).count()
        total_faculty_allocated = CourseInstructorAllocation.objects.filter(
            course__department=dept,
            is_active=True
        ).values('instructor').distinct().count()

        total_enrollments = StudentEnrollment.objects.filter(
            course__department=dept,
            status='ACTIVE'
        ).count()

        if total_faculty_allocated > 0:
            student_faculty_ratio = round(total_enrollments / total_faculty_allocated, 1)
        else:
            student_faculty_ratio = 0.0

        return {
            'department_name': dept.name,
            'department_code': dept.code,
            'active_courses': courses_count,
            'allocated_faculty_count': total_faculty_allocated,
            'active_student_enrollments': total_enrollments,
            'student_faculty_ratio': student_faculty_ratio,
            'is_ratio_healthy': 10.0 <= student_faculty_ratio <= 25.0
        }
''',

    # 3. Courses Services
    'apps/courses/services/__init__.py': '"""Courses services package."""\n',
    'apps/courses/services/clo_plo_matrix_service.py': '''"""
Course Learning Outcomes (CLO) to Program Learning Outcomes (PLO) Mapping Service.
Calculates alignment coverage matrices, ABET criteria mapping, and outcome gaps.
"""
from typing import Dict, Any, List, Set


class LearningOutcomesMatrixService:
    BLOOMS_TAXONOMY_LEVELS = [
        'REMEMBERING',
        'UNDERSTANDING',
        'APPLYING',
        'ANALYZING',
        'EVALUATING',
        'CREATING'
    ]

    ABET_STUDENT_OUTCOMES = {
        'SO_1': 'Identify, formulate, and solve complex engineering problems by applying engineering, science, and mathematics principles.',
        'SO_2': 'Apply engineering design to produce solutions meeting specified needs considering public health, safety, and welfare.',
        'SO_3': 'Communicate effectively with a range of audiences through written, oral, and graphical media.',
        'SO_4': 'Recognize ethical and professional responsibilities in engineering situations and make informed judgments.',
        'SO_5': 'Function effectively on a team whose members together provide leadership, create a collaborative environment, and meet objectives.',
        'SO_6': 'Develop and conduct appropriate experimentation, analyze and interpret data, and use engineering judgment to draw conclusions.',
        'SO_7': 'Acquire and apply new knowledge as needed, using appropriate learning strategies.'
    }

    @classmethod
    def evaluate_curriculum_coverage(
        cls,
        course_mappings: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Evaluates curriculum-wide coverage of ABET Student Outcomes (SO 1 through 7)
        and Bloom's Taxonomy cognitive progression.
        """
        outcomes_coverage = {so: 0 for so in cls.ABET_STUDENT_OUTCOMES.keys()}
        blooms_distribution = {level: 0 for level in cls.BLOOMS_TAXONOMY_LEVELS}

        for mapping in course_mappings:
            for outcome in mapping.get('mapped_outcomes', []):
                if outcome in outcomes_coverage:
                    outcomes_coverage[outcome] += 1
            b_level = mapping.get('blooms_level', '').upper()
            if b_level in blooms_distribution:
                blooms_distribution[b_level] += 1

        uncovered_outcomes = [so for so, count in outcomes_coverage.items() if count == 0]
        well_covered_outcomes = [so for so, count in outcomes_coverage.items() if count >= 3]

        return {
            'total_mapped_elements': len(course_mappings),
            'outcomes_coverage': outcomes_coverage,
            'blooms_distribution': blooms_distribution,
            'uncovered_outcomes': uncovered_outcomes,
            'is_fully_accredited': len(uncovered_outcomes) == 0,
            'accreditation_readiness_score': round((7 - len(uncovered_outcomes)) / 7 * 100, 1)
        }
''',
    'apps/courses/services/syllabus_generator_service.py': '''"""
Comprehensive Course Syllabus Generator Service.
Constructs standard 14-week university syllabi including grading criteria, textbooks, and policies.
"""
from typing import Dict, Any, List


class SyllabusGeneratorService:
    @classmethod
    def generate_standard_syllabus(
        cls,
        course_code: str,
        course_title: str,
        credit_hours: int,
        department_name: str,
        instructor_name: str,
        instructor_email: str,
        office_hours: str,
        prerequisites: List[str],
        course_description: str,
        weekly_topics: List[str],
        textbooks: List[str]
    ) -> Dict[str, Any]:
        """Generates a structured university syllabus matching accreditation specifications."""
        weeks = []
        for i, topic in enumerate(weekly_topics[:14], 1):
            weeks.append({
                'week_number': i,
                'topic': topic,
                'readings': f"Assigned readings for Week {i}",
                'deliverables': "Laboratory assignment / Homework" if i % 2 == 0 else "Lecture discussion & problem set"
            })

        grading_breakdown = [
            {'category': 'Midterm Examination', 'weight_percentage': 25},
            {'category': 'Final Examination', 'weight_percentage': 35},
            {'category': 'Laboratory Experiments & Projects', 'weight_percentage': 25},
            {'category': 'Homework & Problem Sets', 'weight_percentage': 10},
            {'category': 'Class Participation & Attendance', 'weight_percentage': 5}
        ]

        return {
            'course_code': course_code,
            'course_title': course_title,
            'credit_hours': credit_hours,
            'department': department_name,
            'instructor': {
                'name': instructor_name,
                'email': instructor_email,
                'office_hours': office_hours
            },
            'prerequisites': prerequisites,
            'description': course_description,
            'schedule': weeks,
            'grading_breakdown': grading_breakdown,
            'textbooks': textbooks,
            'academic_integrity_statement': "Students are expected to adhere strictly to the Institutional Honor Code."
        }
''',

    # 4. Enrollments Services
    'apps/enrollments/services/__init__.py': '"""Enrollments services package."""\n',
    'apps/enrollments/services/waitlist_service.py': '''"""
Dynamic Course Waitlist Priority & Auto-Enrollment Service.
Prioritizes waitlist queues based on academic class standing, GPA, and major requirement urgency.
"""
from decimal import Decimal
from typing import Dict, Any, List
from django.utils import timezone


class WaitlistPriorityService:
    @classmethod
    def calculate_waitlist_priority_score(
        cls,
        student_year_level: int,  # 4 = Senior, 3 = Junior, 2 = Soph, 1 = Frosh
        is_degree_requirement: bool,
        is_graduating_senior: bool,
        cumulative_gpa: Decimal,
        days_on_waitlist: int
    ) -> Decimal:
        """
        Computes composite priority score:
        Graduating seniors and major requirements receive weighted priority over general electives.
        """
        score = Decimal('0.00')

        # Seniority (0 - 40 points)
        score += Decimal(str(student_year_level * 10))

        # Graduation urgency (30 points)
        if is_graduating_senior:
            score += Decimal('30.00')

        # Major requirement status (20 points)
        if is_degree_requirement:
            score += Decimal('20.00')

        # GPA tiebreaker (0 - 10 points: e.g. 4.0 GPA = 10 pts)
        score += (Decimal(str(cumulative_gpa)) * Decimal('2.5')).quantize(Decimal('0.01'))

        # Time on waitlist (0.5 pt per day, capped at 10 pts)
        waitlist_days_pts = min(Decimal('10.00'), Decimal(str(days_on_waitlist)) * Decimal('0.5'))
        score += waitlist_days_pts

        return score.quantize(Decimal('0.01'))

    @classmethod
    def rank_waitlist_entries(cls, entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Sorts waitlist candidates by descending composite priority score."""
        for entry in entries:
            entry['priority_score'] = cls.calculate_waitlist_priority_score(
                student_year_level=entry.get('year_level', 1),
                is_degree_requirement=entry.get('is_degree_requirement', False),
                is_graduating_senior=entry.get('is_graduating_senior', False),
                cumulative_gpa=Decimal(str(entry.get('cumulative_gpa', 3.0))),
                days_on_waitlist=entry.get('days_on_waitlist', 0)
            )

        ranked = sorted(entries, key=lambda x: x['priority_score'], reverse=True)
        for rank, item in enumerate(ranked, 1):
            item['waitlist_position'] = rank
        return ranked
''',
    'apps/enrollments/services/prerequisite_validation_service.py': '''"""
Prerequisite & Corequisite Enforcement Engine.
Validates academic DAG dependencies, concurrent enrollment permissions, and minimum grade thresholds.
"""
from typing import Dict, Any, List, Set, Optional


class PrerequisiteValidationService:
    MIN_PASSING_GRADE_POINTS = {
        'A': 4.0, 'A-': 3.7,
        'B+': 3.3, 'B': 3.0, 'B-': 2.7,
        'C+': 2.3, 'C': 2.0, 'C-': 1.7,
        'D+': 1.3, 'D': 1.0, 'F': 0.0
    }

    @classmethod
    def validate_enrollment_eligibility(
        cls,
        student_completed_courses: Dict[str, str],  # {course_code: letter_grade}
        course_prerequisites: List[Dict[str, Any]],  # [{'code': 'CS101', 'min_grade': 'C'}]
        currently_enrolled_courses: Set[str],
        course_corequisites: Optional[List[str]] = None,
        has_instructor_override: bool = False
    ) -> Dict[str, Any]:
        """
        Validates whether a student satisfies all prerequisites and corequisites for course enrollment.
        """
        if has_instructor_override:
            return {
                'eligible': True,
                'reason': 'Enrollment authorized via official faculty / dean override waiver.',
                'missing_prerequisites': [],
                'missing_corequisites': []
            }

        missing_prereqs = []
        insufficient_grades = []

        for req in course_prerequisites:
            req_code = req.get('code')
            min_grade = req.get('min_grade', 'C')
            min_points = cls.MIN_PASSING_GRADE_POINTS.get(min_grade, 2.0)

            if req_code not in student_completed_courses:
                missing_prereqs.append(req_code)
            else:
                student_grade = student_completed_courses[req_code]
                student_points = cls.MIN_PASSING_GRADE_POINTS.get(student_grade, 0.0)
                if student_points < min_points:
                    insufficient_grades.append(f"{req_code} (Required: {min_grade}, Earned: {student_grade})")

        # Corequisite check
        missing_coreqs = []
        if course_corequisites:
            for coreq in course_corequisites:
                if coreq not in student_completed_courses and coreq not in currently_enrolled_courses:
                    missing_coreqs.append(coreq)

        is_eligible = len(missing_prereqs) == 0 and len(insufficient_grades) == 0 and len(missing_coreqs) == 0

        reasons = []
        if missing_prereqs:
            reasons.append(f"Missing mandatory prerequisite courses: {', '.join(missing_prereqs)}.")
        if insufficient_grades:
            reasons.append(f"Prerequisite grade below minimum standard: {', '.join(insufficient_grades)}.")
        if missing_coreqs:
            reasons.append(f"Missing concurrent corequisite registration: {', '.join(missing_coreqs)}.")

        return {
            'eligible': is_eligible,
            'reason': 'All prerequisite and corequisite requirements satisfied.' if is_eligible else ' '.join(reasons),
            'missing_prerequisites': missing_prereqs,
            'insufficient_grades': insufficient_grades,
            'missing_corequisites': missing_coreqs
        }
''',

    # 5. Profiles Services
    'apps/profiles/services/__init__.py': '"""Profiles services package."""\n',
    'apps/profiles/services/portfolio_service.py': '''"""
Student Academic Portfolio & Artifact Verification Service.
Evaluates portfolio completeness, competency alignments, and career readiness rubrics.
"""
from typing import Dict, Any, List


class PortfolioVerificationService:
    @classmethod
    def evaluate_portfolio_readiness(
        cls,
        student_id: int,
        artifacts: List[Dict[str, Any]],
        verified_skills: List[str]
    ) -> Dict[str, Any]:
        """
        Assesses student showcase portfolio for career and graduate school readiness.
        Requires minimum: 3 verified artifacts, 1 github/code link, and 5 verified skills.
        """
        total_artifacts = len(artifacts)
        has_code_repository = any(a.get('type') in ['GITHUB_REPO', 'CODE_ARCHIVE'] for a in artifacts)
        has_capstone_project = any(a.get('is_capstone', False) for a in artifacts)
        total_skills = len(verified_skills)

        # Scoring rubric (max 100 points)
        score = 0
        score += min(30, total_artifacts * 10)  # Up to 30 pts for 3 artifacts
        if has_code_repository:
            score += 25
        if has_capstone_project:
            score += 25
        score += min(20, total_skills * 4)  # Up to 20 pts for 5 skills

        is_career_ready = score >= 75

        return {
            'student_id': student_id,
            'readiness_score': score,
            'is_career_ready': is_career_ready,
            'artifact_count': total_artifacts,
            'has_code_repository': has_code_repository,
            'has_capstone_project': has_capstone_project,
            'verified_skills_count': total_skills,
            'badge_awarded': 'GOLD_DISTINCTION' if score >= 90 else ('SILVER_ACHIEVER' if score >= 75 else 'IN_PROGRESS')
        }
''',
    'apps/profiles/services/advisor_assignment_service.py': '''"""
Academic Advisor Matching & Load Balancing Service.
Matches students to departmental faculty advisors balancing caseloads and specialization areas.
"""
from typing import Dict, Any, List


class AdvisorAssignmentService:
    MAX_ADVISEE_CAPACITY = 35

    @classmethod
    def match_advisor(
        cls,
        student_major_specialization: str,
        available_faculty: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Finds the optimal advisor for a student:
        1. Prioritizes matching specialization area.
        2. Selects faculty member with lowest existing advisee caseload.
        """
        candidates = [
            f for f in available_faculty
            if f.get('current_advisees', 0) < cls.MAX_ADVISEE_CAPACITY
        ]

        if not candidates:
            return {
                'assigned': False,
                'advisor': None,
                'reason': 'All departmental faculty advisors are at maximum advisee capacity.'
            }

        # Filter by matching specialization
        specialists = [
            f for f in candidates
            if student_major_specialization.lower() in [s.lower() for s in f.get('specializations', [])]
        ]

        pool = specialists if specialists else candidates
        # Pick least loaded advisor
        chosen = min(pool, key=lambda f: f.get('current_advisees', 0))

        return {
            'assigned': True,
            'advisor': chosen,
            'is_specialization_match': bool(specialists),
            'projected_caseload': chosen.get('current_advisees', 0) + 1
        }
'''
}

for rel_path, content in SERVICES.items():
    filepath = os.path.join(os.path.dirname(__file__), '..', rel_path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created service: {rel_path}")

print("All enterprise services created successfully.")
