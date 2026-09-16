from django.contrib import admin
from .models import AdmissionCycle, AdmissionApplication, Batch, StudentEnrollment, CourseProgress, LessonProgress

@admin.register(AdmissionCycle)
class AdmissionCycleAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'session', 'start_date', 'application_deadline', 'max_seats', 'is_open')
    list_filter = ('is_open', 'program')

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('application_number', 'applicant', 'cycle', 'status', 'created_at')
    list_filter = ('status', 'cycle')
    search_fields = ('application_number', 'applicant__username', 'applicant__email')

@admin.register(Batch)
class BatchAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'program', 'session', 'current_strength', 'max_capacity', 'is_active')
    list_filter = ('program', 'is_active')

@admin.register(StudentEnrollment)
class StudentEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'status', 'letter_grade', 'enrollment_date')
    list_filter = ('status', 'semester', 'course')
    search_fields = ('student__username', 'student__email', 'course__title', 'course__code')

@admin.register(CourseProgress)
class CourseProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'completion_percentage', 'is_completed', 'updated_at')
    list_filter = ('is_completed',)

@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ('student', 'lesson', 'is_completed', 'completed_at')
    list_filter = ('is_completed',)
