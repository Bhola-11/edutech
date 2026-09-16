import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from .constants import AuditActionChoices, PriorityChoices, EntityStatusChoices
from .managers import SoftDeleteManager, TenantManager, ActiveManager

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name=_('Created At'))
    updated_at = models.DateTimeField(auto_now=True, db_index=True, verbose_name=_('Updated At'))

    class Meta:
        abstract = True
        ordering = ['-created_at']

class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class SoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(default=False, db_index=True, verbose_name=_('Is Deleted'))
    deleted_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Deleted At'))

    objects = SoftDeleteManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])

    def hard_delete(self, using=None, keep_parents=False):
        super().delete(using=using, keep_parents=keep_parents)

    def restore(self):
        self.is_deleted = False
        self.deleted_at = None
        self.save(update_fields=['is_deleted', 'deleted_at'])

class AuditableModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_created_records',
        verbose_name=_('Created By')
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_updated_records',
        verbose_name=_('Updated By')
    )

    class Meta:
        abstract = True

class SluggedModel(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name=_('Slug URL'))

    class Meta:
        abstract = True

    def get_slug_source(self):
        if hasattr(self, 'title') and getattr(self, 'title'):
            return getattr(self, 'title')
        if hasattr(self, 'name') and getattr(self, 'name'):
            return getattr(self, 'name')
        return str(uuid.uuid4())[:8]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.get_slug_source())
            unique_slug = base_slug
            counter = 1
            model_class = self.__class__
            while model_class.objects.filter(slug=unique_slug).exclude(pk=self.pk).exists():
                unique_slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = unique_slug
        super().save(*args, **kwargs)

class MultiTenantModel(SoftDeleteModel):
    institution = models.ForeignKey(
        'institutions.Institution',
        on_delete=models.CASCADE,
        related_name='%(class)s_records',
        db_index=True,
        verbose_name=_('Institution / Organization')
    )
    campus = models.ForeignKey(
        'institutions.Campus',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_records',
        verbose_name=_('Campus Location')
    )
    department = models.ForeignKey(
        'institutions.AcademicDepartment',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='%(class)s_records',
        verbose_name=_('Academic Department')
    )

    objects = TenantManager()

    class Meta:
        abstract = True

class ActivityLog(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='activity_audit_logs',
        verbose_name=_('Acting User')
    )
    action = models.CharField(max_length=40, choices=AuditActionChoices.choices, db_index=True, verbose_name=_('Action'))
    entity_name = models.CharField(max_length=120, db_index=True, verbose_name=_('Entity Affected'))
    entity_id = models.CharField(max_length=64, blank=True, null=True, db_index=True, verbose_name=_('Entity Primary Key'))
    ip_address = models.GenericIPAddressField(null=True, blank=True, verbose_name=_('IP Address'))
    user_agent = models.TextField(blank=True, null=True, verbose_name=_('Browser User Agent'))
    request_method = models.CharField(max_length=10, blank=True, null=True, verbose_name=_('HTTP Method'))
    request_path = models.CharField(max_length=500, blank=True, null=True, verbose_name=_('Request URL Path'))
    details = models.JSONField(default=dict, blank=True, verbose_name=_('Log Metadata Details'))
    status_code = models.IntegerField(null=True, blank=True, verbose_name=_('HTTP Status Code'))

    class Meta:
        verbose_name = _('Audit Activity Log')
        verbose_name_plural = _('Audit Activity Logs')
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['action', 'created_at']),
            models.Index(fields=['user', 'created_at']),
            models.Index(fields=['entity_name', 'entity_id']),
        ]

    def __str__(self):
        actor = self.user.get_full_name() if self.user else 'Anonymous'
        return f'[{self.action}] {self.entity_name} by {actor} at {self.created_at.strftime("%Y-%m-%d %H:%M")}'

class SystemNotification(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='system_notifications',
        verbose_name=_('Notification Recipient')
    )
    title = models.CharField(max_length=255, verbose_name=_('Notification Title'))
    message = models.TextField(verbose_name=_('Notification Message Content'))
    priority = models.CharField(max_length=20, choices=PriorityChoices.choices, default=PriorityChoices.MEDIUM, verbose_name=_('Priority'))
    action_url = models.CharField(max_length=500, blank=True, null=True, verbose_name=_('Destination URL'))
    is_read = models.BooleanField(default=False, db_index=True, verbose_name=_('Is Read'))
    read_at = models.DateTimeField(null=True, blank=True, verbose_name=_('Read At'))

    class Meta:
        verbose_name = _('System Notification')
        verbose_name_plural = _('System Notifications')
        ordering = ['-created_at']

    def mark_as_read(self):
        if not self.is_read:
            self.is_read = True
            self.read_at = timezone.now()
            self.save(update_fields=['is_read', 'read_at'])

class ConfigurationSetting(TimeStampedModel):
    key = models.CharField(max_length=100, unique=True, db_index=True, verbose_name=_('Configuration Key'))
    value = models.TextField(verbose_name=_('Configuration Value'))
    description = models.CharField(max_length=255, blank=True, verbose_name=_('Setting Description'))
    is_public = models.BooleanField(default=False, verbose_name=_('Publicly Accessible in Frontend'))

    class Meta:
        verbose_name = _('System Configuration Setting')
        verbose_name_plural = _('System Configuration Settings')
        ordering = ['key']

    def __str__(self):
        return f'{self.key} = {self.value[:40]}'
