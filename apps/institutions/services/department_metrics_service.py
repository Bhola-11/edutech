"""
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
