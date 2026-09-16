from rest_framework import viewsets, permissions
from .models import Course, Program, CourseCategory, CourseModule, Lesson, CourseReview
from .serializers import CourseSerializer, ProgramSerializer, CourseModuleSerializer, LessonSerializer
from apps.core.permissions import IsAcademicStaffUser

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('department', 'category').prefetch_related('modules__lessons')
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProgramViewSet(viewsets.ModelViewSet):
    queryset = Program.objects.select_related('department').prefetch_related('curriculum_courses')
    serializer_class = ProgramSerializer
    permission_classes = [permissions.IsAuthenticated]

class CourseModuleViewSet(viewsets.ModelViewSet):
    queryset = CourseModule.objects.select_related('course').prefetch_related('lessons')
    serializer_class = CourseModuleSerializer
    permission_classes = [permissions.IsAuthenticated]

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.select_related('module__course')
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
