import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from apps.core.models import TimeStampedModel, SoftDeleteModel, SluggedModel
from apps.core.constants import EntityStatusChoices
from apps.core.validators import validate_phone_number, validate_academic_year

class Institution(TimeStampedModel, SoftDeleteModel, SluggedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True, verbose_name=_('Institution Legal Name'))
    code = models.CharField(max_length=30, unique=True, db_index=True, verbose_name=_('Institution Code (e.g. MIT, HARVARD)'))
    logo = models.ImageField(upload_to='institutions/logos/', null=True, blank=True, verbose_name=_('Official Crest / Logo'))
    motto = models.CharField(max_length=255, blank=True, verbose_name=_('Motto / Slogan'))
    established_year = models.PositiveIntegerField(null=True, blank=True, verbose_name=_('Established Year'))
    website = models.URLField(blank=True, verbose_name=_('Official Website URL'))
    contact_email = models.EmailField(verbose_name=_('Primary Contact Email'))
    contact_phone = models.CharField(max_length=25, blank=True, validators=[validate_phone_number], verbose_name=_('Contact Phone'))
    address_line_1 = models.CharField(max_length=255, verbose_name=_('Street Address Line 1'))
    address_line_2 = models.CharField(max_length=255, blank=True, verbose_name=_('Street Address Line 2'))
    city = models.CharField(max_length=100, verbose_name=_('City / Municipality'))
    state_province = models.CharField(max_length=100, verbose_name=_('State / Province / Region'))
    postal_code = models.CharField(max_length=20, verbose_name=_('Postal / ZIP Code'))
    country = models.CharField(max_length=100, default='United States', verbose_name=_('Country'))
    accreditation_body = models.CharField(max_length=150, blank=True, verbose_name=_('Accreditation Agency'))
    accreditation_grade = models.CharField(max_length=50, blank=True, verbose_name=_('Accreditation Grade / Rating'))
    timezone = models.CharField(max_length=50, default='UTC', verbose_name=_('Default Timezone'))
    status = models.CharField(max_length=30, choices=EntityStatusChoices.choices, default=EntityStatusChoices.ACTIVE, verbose_name=_('Status'))

    class Meta:
        verbose_name = _('Institution / University')
        verbose_name_plural = _('Institutions / Universities')
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.code})'

class CampusTypeChoices(models.TextChoices):
    MAIN = 'MAIN', 'Main Campus'
    SATELLITE = 'SATELLITE', 'Satellite Campus'
    REGIONAL = 'REGIONAL', 'Regional Center'
    ONLINE = 'ONLINE', 'Virtual / Online Campus'
    AFFILIATED = 'AFFILIATED', 'Affiliated College'

class Campus(TimeStampedModel, SoftDeleteModel, SluggedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='campuses', verbose_name=_('Institution'))
    name = models.CharField(max_length=255, verbose_name=_('Campus Name'))
    code = models.CharField(max_length=30, verbose_name=_('Campus Code'))
    campus_type = models.CharField(max_length=30, choices=CampusTypeChoices.choices, default=CampusTypeChoices.MAIN)
    director = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='directed_campuses',
        verbose_name=_('Campus Director / Principal')
    )
    contact_email = models.EmailField(blank=True, verbose_name=_('Campus Contact Email'))
    contact_phone = models.CharField(max_length=25, blank=True, validators=[validate_phone_number], verbose_name=_('Campus Phone'))
    address = models.TextField(verbose_name=_('Full Physical Address'))
    city = models.CharField(max_length=100, verbose_name=_('City'))
    state = models.CharField(max_length=100, verbose_name=_('State / Province'))
    country = models.CharField(max_length=100, default='United States')
    capacity = models.PositiveIntegerField(default=5000, verbose_name=_('Maximum Student Capacity'))
    status = models.CharField(max_length=30, choices=EntityStatusChoices.choices, default=EntityStatusChoices.ACTIVE)

    class Meta:
        verbose_name = _('Campus Location')
        verbose_name_plural = _('Campuses')
        unique_together = ['institution', 'code']
        ordering = ['name']

    def __str__(self):
        return f'{self.name} - {self.institution.code}'

class Faculty(TimeStampedModel, SoftDeleteModel, SluggedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='faculties')
    name = models.CharField(max_length=255, verbose_name=_('Faculty Name (e.g. Faculty of Engineering)'))
    code = models.CharField(max_length=30, verbose_name=_('Faculty Code'))
    dean = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_faculties',
        verbose_name=_('Dean of Faculty')
    )
    description = models.TextField(blank=True, verbose_name=_('Vision & Overview'))

    class Meta:
        verbose_name = _('Faculty / School')
        verbose_name_plural = _('Faculties / Schools')
        unique_together = ['institution', 'code']
        ordering = ['name']

    def __str__(self):
        return f'{self.name} ({self.institution.code})'

class AcademicDepartment(TimeStampedModel, SoftDeleteModel, SluggedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='departments')
    campus = models.ForeignKey(Campus, on_delete=models.SET_NULL, null=True, blank=True, related_name='departments')
    name = models.CharField(max_length=255, verbose_name=_('Department Name (e.g. Computer Science & Engineering)'))
    code = models.CharField(max_length=30, verbose_name=_('Department Code'))
    head_of_department = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_departments',
        verbose_name=_('Head of Department (HOD)')
    )
    contact_email = models.EmailField(blank=True)
    office_location = models.CharField(max_length=150, blank=True, verbose_name=_('Office Building / Room'))

    class Meta:
        verbose_name = _('Academic Department')
        verbose_name_plural = _('Academic Departments')
        unique_together = ['faculty', 'code']
        ordering = ['name']

    def __str__(self):
        return f'{self.name} [{self.code}]'

class AcademicSession(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='academic_sessions')
    name = models.CharField(max_length=100, verbose_name=_('Session Label (e.g. 2026-2027 Academic Year)'))
    academic_year = models.CharField(max_length=20, validators=[validate_academic_year], verbose_name=_('Year Range (YYYY-YYYY)'))
    start_date = models.DateField(verbose_name=_('Session Start Date'))
    end_date = models.DateField(verbose_name=_('Session End Date'))
    is_current = models.BooleanField(default=False, verbose_name=_('Is Currently Active Session'))

    class Meta:
        verbose_name = _('Academic Session')
        verbose_name_plural = _('Academic Sessions')
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.institution.code} - {self.name}'

class TermTypeChoices(models.TextChoices):
    FALL = 'FALL', 'Fall Semester'
    SPRING = 'SPRING', 'Spring Semester'
    SUMMER = 'SUMMER', 'Summer Term'
    WINTER = 'WINTER', 'Winter Intersession'
    TRIMESTER_1 = 'TRIMESTER_1', 'Trimester 1'
    TRIMESTER_2 = 'TRIMESTER_2', 'Trimester 2'
    TRIMESTER_3 = 'TRIMESTER_3', 'Trimester 3'

class Semester(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    academic_session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='semesters')
    name = models.CharField(max_length=100, verbose_name=_('Term Name (e.g. Fall 2026)'))
    term_type = models.CharField(max_length=30, choices=TermTypeChoices.choices, default=TermTypeChoices.FALL)
    start_date = models.DateField(verbose_name=_('Term Start Date'))
    end_date = models.DateField(verbose_name=_('Term End Date'))
    registration_start_date = models.DateField(verbose_name=_('Course Registration Open'))
    registration_end_date = models.DateField(verbose_name=_('Course Registration Deadline'))
    add_drop_deadline = models.DateField(verbose_name=_('Add/Drop Period Ends'))
    is_current = models.BooleanField(default=False, verbose_name=_('Is Current Active Term'))

    class Meta:
        verbose_name = _('Semester / Term')
        verbose_name_plural = _('Semesters / Terms')
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.academic_session.name} - {self.name}'

class RoomTypeChoices(models.TextChoices):
    LECTURE_HALL = 'LECTURE_HALL', 'Lecture Hall (Tiered)'
    CLASSROOM = 'CLASSROOM', 'Standard Classroom'
    COMPUTER_LAB = 'COMPUTER_LAB', 'Computer & Software Lab'
    SCIENCE_LAB = 'SCIENCE_LAB', 'Science / Wet Lab'
    AUDITORIUM = 'AUDITORIUM', 'Grand Auditorium'
    SEMINAR_ROOM = 'SEMINAR_ROOM', 'Seminar & Conference Room'
    VIRTUAL_ROOM = 'VIRTUAL_ROOM', 'Virtual Online Room'

class Classroom(TimeStampedModel, SoftDeleteModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='classrooms')
    building = models.CharField(max_length=100, verbose_name=_('Building Name / Block'))
    room_number = models.CharField(max_length=50, verbose_name=_('Room / Hall Number'))
    room_type = models.CharField(max_length=30, choices=RoomTypeChoices.choices, default=RoomTypeChoices.CLASSROOM)
    seating_capacity = models.PositiveIntegerField(default=60, verbose_name=_('Seating Capacity'))
    has_projector = models.BooleanField(default=True)
    has_computers = models.BooleanField(default=False)
    has_audio_system = models.BooleanField(default=True)
    is_accessible = models.BooleanField(default=True, verbose_name=_('Wheelchair Accessible'))
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('Classroom / Venue')
        verbose_name_plural = _('Classrooms / Venues')
        unique_together = ['campus', 'building', 'room_number']
        ordering = ['building', 'room_number']

    def __str__(self):
        return f'{self.campus.code} | {self.building} - Rm {self.room_number} ({self.seating_capacity} seats)'
