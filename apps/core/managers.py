from django.db import models
from django.utils import timezone

class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        return self.update(is_deleted=True, deleted_at=timezone.now())

    def hard_delete(self):
        return super().delete()

    def restore(self):
        return self.update(is_deleted=False, deleted_at=None)

    def active(self):
        return self.filter(is_deleted=False, is_active=True)

    def deleted_only(self):
        return self.filter(is_deleted=True)

class SoftDeleteManager(models.Manager):
    def get_queryset(self):
        return SoftDeleteQuerySet(self.model, using=self._db).filter(is_deleted=False)

    def all_with_deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db)

    def deleted_only(self):
        return SoftDeleteQuerySet(self.model, using=self._db).deleted_only()

    def active(self):
        return self.get_queryset().filter(is_active=True)

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class TenantQuerySet(SoftDeleteQuerySet):
    def for_institution(self, institution):
        if not institution:
            return self.none()
        return self.filter(institution=institution)

    def for_campus(self, campus):
        if not campus:
            return self.none()
        return self.filter(campus=campus)

    def for_department(self, department):
        if not department:
            return self.none()
        return self.filter(department=department)

class TenantManager(SoftDeleteManager):
    def get_queryset(self):
        return TenantQuerySet(self.model, using=self._db).filter(is_deleted=False)

    def for_institution(self, institution):
        return self.get_queryset().for_institution(institution)

    def for_campus(self, campus):
        return self.get_queryset().for_campus(campus)

    def for_department(self, department):
        return self.get_queryset().for_department(department)
