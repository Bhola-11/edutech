from django.contrib import admin
from .models import StudentProfile, InstructorProfile, AcademicCredential, SkillRecord

@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = ('roll_number', 'user', 'program', 'current_semester', 'cgpa')
    search_fields = ('roll_number', 'user__username', 'user__email')

@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'user', 'designation', 'office_room')
    search_fields = ('employee_id', 'user__username', 'user__email')

@admin.register(AcademicCredential)
class AcademicCredentialAdmin(admin.ModelAdmin):
    list_display = ('degree_name', 'institution_name', 'graduation_year', 'user')

@admin.register(SkillRecord)
class SkillRecordAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'proficiency', 'user')
