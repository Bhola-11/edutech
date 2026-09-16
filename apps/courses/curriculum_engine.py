from collections import defaultdict, deque
from decimal import Decimal
from django.core.exceptions import ValidationError
from .models import Course, Program, CourseModule, Lesson
from apps.enrollments.models import StudentEnrollment, CourseProgress

class CurriculumDAGService:
    @staticmethod
    def detect_circular_dependencies(course_id, proposed_prerequisite_id):
        if course_id == proposed_prerequisite_id:
            return True

        visited = set()
        queue = deque([proposed_prerequisite_id])

        while queue:
            curr_id = queue.popleft()
            if curr_id == course_id:
                return True
            if curr_id not in visited:
                visited.add(curr_id)
                try:
                    course = Course.objects.prefetch_related('prerequisites').get(id=curr_id)
                    for prereq in course.prerequisites.all():
                        if prereq.id not in visited:
                            queue.append(prereq.id)
                except Course.DoesNotExist:
                    continue

        return False

    @staticmethod
    def get_prerequisite_chain(course):
        chain = []
        visited = set()

        def dfs(c, depth=1):
            if c.id in visited or depth > 10:
                return
            visited.add(c.id)
            for prereq in c.prerequisites.all():
                chain.append({
                    'course_id': str(prereq.id),
                    'code': prereq.code,
                    'title': prereq.title,
                    'credits': float(prereq.credit_hours),
                    'level': depth
                })
                dfs(prereq, depth + 1)

        dfs(course)
        return chain

    @staticmethod
    def get_recommended_sequence(program):
        courses = list(program.curriculum_courses.prefetch_related('prerequisites').all())
        graph = defaultdict(list)
        in_degree = {c.id: 0 for c in courses}
        course_map = {c.id: c for c in courses}

        for c in courses:
            for prereq in c.prerequisites.all():
                if prereq.id in course_map:
                    graph[prereq.id].append(c.id)
                    in_degree[c.id] += 1

        queue = deque([cid for cid, deg in in_degree.items() if deg == 0])
        sequence = []

        while queue:
            curr_id = queue.popleft()
            sequence.append(course_map[curr_id])
            for neighbor in graph[curr_id]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return sequence

class DegreeAuditService:
    def __init__(self, student, program):
        self.student = student
        self.program = program

    def perform_audit(self):
        enrollments = StudentEnrollment.objects.filter(
            student=self.student,
            status='COMPLETED'
        ).select_related('course')

        completed_courses = {e.course.id: e for e in enrollments}
        program_courses = self.program.curriculum_courses.all()

        total_credits_earned = Decimal('0.0')
        required_courses_completed = []
        required_courses_remaining = []

        for course in program_courses:
            if course.id in completed_courses:
                enr = completed_courses[course.id]
                total_credits_earned += course.credit_hours
                required_courses_completed.append({
                    'code': course.code,
                    'title': course.title,
                    'credits': float(course.credit_hours),
                    'grade': enr.letter_grade or 'Pass',
                    'score': float(enr.final_score) if enr.final_score else 100.0
                })
            else:
                required_courses_remaining.append({
                    'code': course.code,
                    'title': course.title,
                    'credits': float(course.credit_hours),
                    'level': course.academic_level
                })

        credits_required = Decimal(str(self.program.total_credits_required))
        completion_rate = min(Decimal('100.0'), (total_credits_earned / credits_required) * Decimal('100.0')) if credits_required > 0 else Decimal('0.0')
        is_eligible_for_graduation = (total_credits_earned >= credits_required) and (len(required_courses_remaining) == 0)

        return {
            'student_name': self.student.get_full_name(),
            'program_name': self.program.name,
            'credits_required': float(credits_required),
            'credits_earned': float(total_credits_earned),
            'credits_remaining': float(max(Decimal('0.0'), credits_required - total_credits_earned)),
            'completion_percentage': round(float(completion_rate), 2),
            'is_eligible_for_graduation': is_eligible_for_graduation,
            'completed_courses_count': len(required_courses_completed),
            'remaining_courses_count': len(required_courses_remaining),
            'completed_courses': required_courses_completed,
            'remaining_courses': required_courses_remaining
        }
