from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GradingScale, GradeCategory, FinalCourseGrade
from apps.courses.models import Course
from apps.enrollments.models import StudentEnrollment


@login_required
def gradebook_view(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    categories = course.grade_categories.prefetch_related('items__grades__student').all()
    enrollments = StudentEnrollment.objects.filter(course=course, status='ACTIVE').select_related('student', 'final_grade')
    return render(request, 'grading/gradebook.html', {
        'course': course,
        'categories': categories,
        'enrollments': enrollments
    })


@login_required
def transcript_view(request, student_id=None):
    from apps.accounts.models import User
    user = request.user if not student_id else get_object_or_404(User, pk=student_id)
    grades = FinalCourseGrade.objects.filter(enrollment__student=user).select_related('enrollment__course')
    return render(request, 'grading/transcript.html', {'student': user, 'grades': grades})
