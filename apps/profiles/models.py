import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel, SoftDeleteModel
from apps.core.constants import BloodGroupChoices
from apps.core.validators import validate_gpa_score, validate_phone_number
from apps.courses.models import Program
from apps.institutions.models import Semester

class StudentProfile(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student_profile')
    roll_number = models.CharField(max_length=40, unique=True, db_index=True)
    registration_number = models.CharField(max_length=50, blank=True, unique=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True, related_name='enrolled_students')
    current_semester = models.ForeignKey(Semester, on_delete=models.SET_NULL, null=True, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, default=0.0, validators=[validate_gpa_score])
    admission_date = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=10, choices=BloodGroupChoices.choices, default=BloodGroupChoices.UNKNOWN)
    emergency_contact_name = models.CharField(max_length=150, blank=True)
    emergency_contact_phone = models.CharField(max_length=25, blank=True, validators=[validate_phone_number])

    class Meta:
        verbose_name = _('Student Academic Profile')
        verbose_name_plural = _('Student Academic Profiles')

    def __str__(self):
        return f'{self.roll_number} - {self.user.get_full_name()}'

class FacultyDesignationChoices(models.TextChoices):
    PROFESSOR = 'PROFESSOR', 'Full Professor'
    ASSOCIATE_PROFESSOR = 'ASSOCIATE_PROFESSOR', 'Associate Professor'
    ASSISTANT_PROFESSOR = 'ASSISTANT_PROFESSOR', 'Assistant Professor'
    SENIOR_LECTURER = 'SENIOR_LECTURER', 'Senior Lecturer'
    LECTURER = 'LECTURER', 'Lecturer'
    ADJUNCT_FACULTY = 'ADJUNCT_FACULTY', 'Adjunct Faculty'
    VISITING_SCHOLAR = 'VISITING_SCHOLAR', 'Visiting Scholar'
    TEACHING_FELLOW = 'TEACHING_FELLOW', 'Teaching Fellow'

class InstructorProfile(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor_profile')
    employee_id = models.CharField(max_length=40, unique=True, db_index=True)
    designation = models.CharField(max_length=40, choices=FacultyDesignationChoices.choices, default=FacultyDesignationChoices.ASSISTANT_PROFESSOR)
    office_room = models.CharField(max_length=100, blank=True)
    office_hours = models.CharField(max_length=200, blank=True, help_text='e.g. Mon & Wed 2:00 PM - 4:00 PM')
    research_interests = models.TextField(blank=True)
    google_scholar_url = models.URLField(blank=True)
    hire_date = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = _('Instructor / Faculty Profile')
        verbose_name_plural = _('Instructor / Faculty Profiles')

    def __str__(self):
        return f'{self.user.get_full_name()} ({self.get_designation_display()})'

class AcademicCredential(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='credentials')
    degree_name = models.CharField(max_length=200)
    institution_name = models.CharField(max_length=255)
    graduation_year = models.PositiveIntegerField()
    score_or_grade = models.CharField(max_length=50, blank=True)
    document_proof = models.FileField(upload_to='profiles/credentials/%Y/', null=True, blank=True)

    class Meta:
        verbose_name = _('Academic Credential')
        verbose_name_plural = _('Academic Credentials')
        ordering = ['-graduation_year']

class SkillProficiencyChoices(models.TextChoices):
    BEGINNER = 'BEGINNER', 'Beginner'
    INTERMEDIATE = 'INTERMEDIATE', 'Intermediate'
    ADVANCED = 'ADVANCED', 'Advanced'
    EXPERT = 'EXPERT', 'Expert'

class SkillRecord(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='skills')
    skill_name = models.CharField(max_length=100)
    proficiency = models.CharField(max_length=30, choices=SkillProficiencyChoices.choices, default=SkillProficiencyChoices.INTERMEDIATE)

    class Meta:
        verbose_name = _('Skill Record')
        verbose_name_plural = _('Skill Records')
        unique_together = ['user', 'skill_name']
