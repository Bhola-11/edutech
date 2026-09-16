import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel, SoftDeleteModel
from apps.core.constants import EntityStatusChoices
from apps.institutions.models import AcademicSession, Semester
from apps.courses.models import Program, Course, Lesson

class ApplicationStatusChoices(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft Application'
    SUBMITTED = 'SUBMITTED', 'Submitted & Pending Review'
    UNDER_REVIEW = 'UNDER_REVIEW', 'Under Committee Review'
    SHORTLISTED = 'SHORTLISTED', 'Shortlisted for Interview'
    ACCEPTED = 'ACCEPTED', 'Accepted / Offer Issued'
    REJECTED = 'REJECTED', 'Application Rejected'
    WAITLISTED = 'WAITLISTED', 'Waitlisted'
    ENROLLED = 'ENROLLED', 'Formally Enrolled'

class EnrollmentStatusChoices(models.TextChoices):
    PENDING = 'PENDING', 'Pending Confirmation'
    ACTIVE = 'ACTIVE', 'Actively Enrolled'
    COMPLETED = 'COMPLETED', 'Successfully Completed'
    DROPPED = 'DROPPED', 'Dropped Course'
    WITHDRAWN = 'WITHDRAWN', 'Officially Withdrawn'
    SUSPENDED = 'SUSPENDED', 'Academic Suspension'

class AdmissionCycle(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='admission_cycles')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='admission_cycles')
    name = models.CharField(max_length=150, verbose_name=_('Cycle Title (e.g. Fall 2026 Admissions)'))
    start_date = models.DateField()
    application_deadline = models.DateField()
    max_seats = models.PositiveIntegerField(default=120)
    is_open = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Admission Cycle')
        verbose_name_plural = _('Admission Cycles')
        ordering = ['-application_deadline']

    def __str__(self):
        return f'{self.program.name} - {self.name}'

class AdmissionApplication(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admission_applications')
    cycle = models.ForeignKey(AdmissionCycle, on_delete=models.CASCADE, related_name='applications')
    application_number = models.CharField(max_length=40, unique=True, db_index=True)
    statement_of_purpose = models.TextField(verbose_name=_('Statement of Purpose (SOP)'))
    prior_institution = models.CharField(max_length=255, verbose_name=_('Prior School / University'))
    prior_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=30, choices=ApplicationStatusChoices.choices, default=ApplicationStatusChoices.SUBMITTED)
    reviewer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='reviewed_applications'
    )
    review_notes = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Admission Application')
        verbose_name_plural = _('Admission Applications')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.application_number} - {self.applicant.get_full_name()} ({self.status})'

    def save(self, *args, **kwargs):
        if not self.application_number:
            self.application_number = f'APP-{timezone.now().strftime("%Y%m")}-{uuid.uuid4().hex[:6].upper()}'
        super().save(*args, **kwargs)

class Batch(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='batches')
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='batches')
    name = models.CharField(max_length=100, verbose_name=_('Batch Title (e.g. 2026-Cohort-A)'))
    section = models.CharField(max_length=10, default='A', verbose_name=_('Section'))
    max_capacity = models.PositiveIntegerField(default=60)
    current_strength = models.PositiveIntegerField(default=0)
    advisor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='advised_batches',
        verbose_name=_('Faculty Advisor / Mentor')
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Cohort / Batch')
        verbose_name_plural = _('Cohorts / Batches')
        unique_together = ['program', 'session', 'name', 'section']
        ordering = ['name']

    def __str__(self):
        return f'{self.program.code} - {self.name} (Sec {self.section})'

class StudentEnrollment(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    batch = models.ForeignKey(Batch, on_delete=models.SET_NULL, null=True, blank=True, related_name='course_enrollments')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=30, choices=EnrollmentStatusChoices.choices, default=EnrollmentStatusChoices.ACTIVE)
    final_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    letter_grade = models.CharField(max_length=5, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Student Course Enrollment')
        verbose_name_plural = _('Student Course Enrollments')
        unique_together = ['student', 'course', 'semester']
        ordering = ['-enrollment_date']

    def __str__(self):
        return f'{self.student.get_full_name()} -> {self.course.code} ({self.status})'

class CourseProgress(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_progress_records')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='progress_records')
    completion_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)
    last_accessed_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name = _('Course Progress Tracker')
        verbose_name_plural = _('Course Progress Trackers')
        unique_together = ['student', 'course']

    def __str__(self):
        return f'{self.student.email} - {self.course.code}: {self.completion_percentage}%'

class LessonProgress(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson_progress_records')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='progress_records')
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    time_spent_seconds = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = _('Lesson Progress Record')
        verbose_name_plural = _('Lesson Progress Records')
        unique_together = ['student', 'lesson']
