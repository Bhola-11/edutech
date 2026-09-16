from django.contrib import admin
from .models import Institution, Campus, Faculty, AcademicDepartment, AcademicSession, Semester, Classroom

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'city', 'country', 'status', 'created_at')
    list_filter = ('status', 'country')
    search_fields = ('name', 'code', 'city')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'institution', 'campus_type', 'city', 'capacity')
    list_filter = ('campus_type', 'institution')
    search_fields = ('name', 'code')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'institution', 'dean')
    search_fields = ('name', 'code')

@admin.register(AcademicDepartment)
class AcademicDepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'faculty', 'campus', 'head_of_department')
    search_fields = ('name', 'code')

@admin.register(AcademicSession)
class AcademicSessionAdmin(admin.ModelAdmin):
    list_display = ('name', 'institution', 'academic_year', 'start_date', 'end_date', 'is_current')
    list_filter = ('institution', 'is_current')

@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ('name', 'academic_session', 'term_type', 'start_date', 'end_date', 'is_current')
    list_filter = ('term_type', 'is_current')

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('room_number', 'building', 'campus', 'room_type', 'seating_capacity', 'is_active')
    list_filter = ('room_type', 'is_active')
