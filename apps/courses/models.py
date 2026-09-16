import uuid
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel, SoftDeleteModel, SluggedModel
from apps.core.constants import AcademicLevelChoices, EntityStatusChoices
from apps.core.validators import validate_credit_hours
from apps.institutions.models import AcademicDepartment, Semester

class Program(TimeStampedModel, SoftDeleteModel, SluggedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(AcademicDepartment, on_delete=models.CASCADE, related_name='programs')
    name = models.CharField(max_length=255, verbose_name=_('Program Name (e.g. B.Tech Computer Science)'))
    code = models.CharField(max_length=30, unique=True, verbose_name=_('Program Code (e.g. BSCS)'))
    academic_level = models.CharField(max_length=30, choices=AcademicLevelChoices.choices, default=AcademicLevelChoices.UNDERGRADUATE)
    total_credits_required = models.PositiveIntegerField(default=120, verbose_name=_('Total Credits Required for Graduation'))
    duration_semesters = models.PositiveSmallIntegerField(default=8, verbose_name=_('Standard Duration (Semesters)'))
    description = models.TextField(blank=True, verbose_name=_('Program Overview'))
    learning_outcomes = models.TextField(blank=True, verbose_name=_('Program Educational Objectives'))
    career_pathways = models.TextField(blank=True, verbose_name=_('Career Opportunities'))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Academic Program / Degree')
        verbose_name_plural = _('Academic Programs / Degrees')
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.code})'

class CourseCategory(TimeStampedModel, SluggedModel):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = _('Course Category')
        verbose_name_plural = _('Course Categories')
        ordering = ['name']

    def __str__(self):
        return self.name

class Course(TimeStampedModel, SoftDeleteModel, SluggedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    department = models.ForeignKey(AcademicDepartment, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(CourseCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='courses')
    programs = models.ManyToManyField(Program, blank=True, related_name='curriculum_courses')
    title = models.CharField(max_length=255, verbose_name=_('Course Title'))
    code = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=_('Course Code (e.g. CS-101)'))
    credit_hours = models.DecimalField(max_digits=4, decimal_places=1, default=3.0, validators=[validate_credit_hours])
    lecture_hours = models.PositiveSmallIntegerField(default=3, verbose_name=_('Weekly Lecture Hours'))
    lab_hours = models.PositiveSmallIntegerField(default=0, verbose_name=_('Weekly Practical/Lab Hours'))
    academic_level = models.CharField(max_length=30, choices=AcademicLevelChoices.choices, default=AcademicLevelChoices.UNDERGRADUATE)
    thumbnail = models.ImageField(upload_to='courses/thumbnails/%Y/%m/', null=True, blank=True)
    summary = models.CharField(max_length=500, blank=True, verbose_name=_('Short Summary'))
    description = models.TextField(verbose_name=_('Detailed Course Syllabus & Overview'))
    prerequisites = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='dependent_courses')
    syllabus_document = models.FileField(upload_to='courses/syllabi/%Y/', null=True, blank=True)
    status = models.CharField(max_length=30, choices=EntityStatusChoices.choices, default=EntityStatusChoices.ACTIVE)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('Course')
        verbose_name_plural = _('Courses')
        ordering = ['code']

    def __str__(self):
        return f'{self.code} - {self.title}'

    @property
    def total_modules_count(self):
        return self.modules.count()

class CourseModule(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=255, verbose_name=_('Module Title (e.g. Unit 1: Graph Theory)'))
    order = models.PositiveSmallIntegerField(default=1, verbose_name=_('Module Order'))
    summary = models.TextField(blank=True, verbose_name=_('Module Summary'))
    estimated_hours = models.DecimalField(max_digits=4, decimal_places=1, default=5.0)

    class Meta:
        verbose_name = _('Course Module / Unit')
        verbose_name_plural = _('Course Modules / Units')
        ordering = ['order', 'created_at']

    def __str__(self):
        return f'{self.course.code} - Mod {self.order}: {self.title}'

class LessonContentTypeChoices(models.TextChoices):
    VIDEO = 'VIDEO', 'Streaming Video Lesson'
    ARTICLE = 'ARTICLE', 'Interactive Reading & Markdown'
    SCORM = 'SCORM', 'SCORM / e-Learning Package'
    CODE_SANDBOX = 'CODE_SANDBOX', 'Coding Exercise'
    DOWNLOADABLE = 'DOWNLOADABLE', 'Downloadable Lecture Notes'
    QUIZ = 'QUIZ', 'Module Checkpoint Quiz'

class Lesson(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    module = models.ForeignKey(CourseModule, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=255, verbose_name=_('Lesson Title'))
    order = models.PositiveSmallIntegerField(default=1)
    content_type = models.CharField(max_length=30, choices=LessonContentTypeChoices.choices, default=LessonContentTypeChoices.ARTICLE)
    duration_minutes = models.PositiveIntegerField(default=30)
    is_free_preview = models.BooleanField(default=False, verbose_name=_('Allow Free Preview'))
    body_text = models.TextField(blank=True, verbose_name=_('Lesson Content / Article Text'))
    video_url = models.URLField(blank=True, verbose_name=_('Video URL (YouTube/Vimeo/HLS)'))
    resource_file = models.FileField(upload_to='courses/lessons/resources/%Y/%m/', null=True, blank=True)

    class Meta:
        verbose_name = _('Lesson')
        verbose_name_plural = _('Lessons')
        ordering = ['order', 'created_at']

    def __str__(self):
        return f'{self.module.title} -> Lesson {self.order}: {self.title}'

class CourseInstructorAllocation(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='instructor_allocations')
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='allocated_courses')
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='course_allocations')
    is_lead = models.BooleanField(default=False, verbose_name=_('Lead Instructor / Primary Coordinator'))

    class Meta:
        verbose_name = _('Course Faculty Allocation')
        verbose_name_plural = _('Course Faculty Allocations')
        unique_together = ['course', 'instructor', 'semester']

    def __str__(self):
        return f'{self.course.code} - {self.instructor.get_full_name()} ({self.semester.name})'

class CourseReview(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews')
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_reviews')
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    headline = models.CharField(max_length=150, blank=True)
    comment = models.TextField()
    is_approved = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Course Review')
        verbose_name_plural = _('Course Reviews')
        unique_together = ['course', 'student']
        ordering = ['-created_at']
