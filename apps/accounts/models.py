import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from apps.core.constants import UserRoleChoices, GenderChoices
from apps.core.models import TimeStampedModel
from apps.core.validators import validate_phone_number
from .managers import CustomUserManager

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True, db_index=True, verbose_name=_('Email Address'))
    role = models.CharField(
        max_length=30,
        choices=UserRoleChoices.choices,
        default=UserRoleChoices.STUDENT,
        db_index=True,
        verbose_name=_('System Role')
    )
    institution = models.ForeignKey(
        'institutions.Institution',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name=_('Affiliated Institution')
    )
    campus = models.ForeignKey(
        'institutions.Campus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='users',
        verbose_name=_('Campus Location')
    )
    department = models.ForeignKey(
        'institutions.AcademicDepartment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='department_members',
        verbose_name=_('Academic Department')
    )
    phone_number = models.CharField(
        max_length=25,
        blank=True,
        validators=[validate_phone_number],
        verbose_name=_('Phone Number')
    )
    profile_photo = models.ImageField(
        upload_to='profiles/avatars/%Y/%m/',
        null=True,
        blank=True,
        verbose_name=_('Profile Picture')
    )
    date_of_birth = models.DateField(null=True, blank=True, verbose_name=_('Date of Birth'))
    gender = models.CharField(
        max_length=25,
        choices=GenderChoices.choices,
        default=GenderChoices.PREFER_NOT_TO_SAY,
        verbose_name=_('Gender')
    )
    bio = models.TextField(blank=True, verbose_name=_('Biography / About'))
    is_verified = models.BooleanField(default=False, verbose_name=_('Identity Verified'))
    two_factor_enabled = models.BooleanField(default=False, verbose_name=_('Two-Factor Authentication Enabled'))
    last_activity = models.DateTimeField(null=True, blank=True, verbose_name=_('Last Recorded Activity'))

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    class Meta:
        verbose_name = _('User Account')
        verbose_name_plural = _('User Accounts')
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['email', 'role']),
            models.Index(fields=['institution', 'role']),
        ]

    def __str__(self):
        full_name = self.get_full_name()
        return f'{full_name} ({self.email}) - {self.get_role_display()}' if full_name else f'{self.username} ({self.email})'

    @property
    def is_superadmin(self):
        return self.role == UserRoleChoices.SUPERADMIN or self.is_superuser

    @property
    def is_institution_admin(self):
        return self.role in [UserRoleChoices.SUPERADMIN, UserRoleChoices.INSTITUTION_ADMIN]

    @property
    def is_instructor(self):
        return self.role in [UserRoleChoices.INSTRUCTOR, UserRoleChoices.TEACHING_ASSISTANT]

    @property
    def is_student(self):
        return self.role == UserRoleChoices.STUDENT

    @property
    def is_parent(self):
        return self.role == UserRoleChoices.PARENT

    @property
    def is_mentor(self):
        return self.role == UserRoleChoices.MENTOR

class UserSessionLog(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='session_logs')
    session_key = models.CharField(max_length=40, db_index=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    device_info = models.CharField(max_length=255, blank=True)
    logged_out_at = models.DateTimeField(null=True, blank=True)
    is_expired = models.BooleanField(default=False)

    class Meta:
        verbose_name = _('User Session Log')
        verbose_name_plural = _('User Session Logs')
        ordering = ['-created_at']

    def close_session(self):
        if not self.logged_out_at:
            self.logged_out_at = timezone.now()
            self.is_expired = True
            self.save(update_fields=['logged_out_at', 'is_expired'])

class PasswordHistory(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_histories')
    password_hash = models.CharField(max_length=255)

    class Meta:
        verbose_name = _('Password History')
        verbose_name_plural = _('Password Histories')
        ordering = ['-created_at']

class TwoFactorToken(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='two_factor_tokens')
    token_code = models.CharField(max_length=6, db_index=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)
    attempts = models.PositiveSmallIntegerField(default=0)

    class Meta:
        verbose_name = _('Two-Factor Authentication Token')
        verbose_name_plural = _('Two-Factor Authentication Tokens')
        ordering = ['-created_at']

    def is_valid(self):
        return not self.is_used and self.attempts < 3 and timezone.now() < self.expires_at
