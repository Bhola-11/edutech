from django.contrib import admin
from .models import Program, CourseCategory, Course, CourseModule, Lesson, CourseInstructorAllocation, CourseReview

class CourseModuleInline(admin.StackedInline):
    model = CourseModule
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'department', 'academic_level', 'total_credits_required', 'is_active')
    list_filter = ('academic_level', 'is_active')
    search_fields = ('name', 'code')

@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'department', 'credit_hours', 'academic_level', 'status', 'is_featured')
    list_filter = ('status', 'academic_level', 'is_featured', 'department')
    search_fields = ('title', 'code')
    inlines = [CourseModuleInline]

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order', 'estimated_hours')
    list_filter = ('course',)
    inlines = [LessonInline]

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'module', 'content_type', 'order', 'duration_minutes', 'is_free_preview')
    list_filter = ('content_type', 'is_free_preview')
    search_fields = ('title',)

@admin.register(CourseInstructorAllocation)
class CourseInstructorAllocationAdmin(admin.ModelAdmin):
    list_display = ('course', 'instructor', 'semester', 'is_lead')
    list_filter = ('semester', 'is_lead')

@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('course', 'student', 'rating', 'is_approved', 'created_at')
    list_filter = ('rating', 'is_approved')
