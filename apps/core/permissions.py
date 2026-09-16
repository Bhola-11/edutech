from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from rest_framework import permissions
from .constants import UserRoleChoices

class RoleRequiredMixin(AccessMixin):
    allowed_roles = []

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()

        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)

        user_role = getattr(request.user, 'role', None)
        if user_role not in self.allowed_roles:
            raise PermissionDenied('You do not have the required role credentials to access this educational portal resource.')

        return super().dispatch(request, *args, **kwargs)

class SuperAdminRequiredMixin(RoleRequiredMixin):
    allowed_roles = [UserRoleChoices.SUPERADMIN]

class InstitutionAdminRequiredMixin(RoleRequiredMixin):
    allowed_roles = [UserRoleChoices.SUPERADMIN, UserRoleChoices.INSTITUTION_ADMIN]

class AcademicStaffRequiredMixin(RoleRequiredMixin):
    allowed_roles = [
        UserRoleChoices.SUPERADMIN,
        UserRoleChoices.INSTITUTION_ADMIN,
        UserRoleChoices.DEAN,
        UserRoleChoices.DEPARTMENT_HEAD,
        UserRoleChoices.INSTRUCTOR,
        UserRoleChoices.TEACHING_ASSISTANT
    ]

class InstructorRequiredMixin(RoleRequiredMixin):
    allowed_roles = [
        UserRoleChoices.SUPERADMIN,
        UserRoleChoices.INSTITUTION_ADMIN,
        UserRoleChoices.INSTRUCTOR,
        UserRoleChoices.TEACHING_ASSISTANT
    ]

class StudentRequiredMixin(RoleRequiredMixin):
    allowed_roles = [UserRoleChoices.SUPERADMIN, UserRoleChoices.STUDENT]

class ParentRequiredMixin(RoleRequiredMixin):
    allowed_roles = [UserRoleChoices.SUPERADMIN, UserRoleChoices.PARENT]

# DRF Permission Classes
class IsSuperAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (request.user.is_superuser or getattr(request.user, 'role', '') == UserRoleChoices.SUPERADMIN))

class IsInstitutionAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            request.user.is_superuser or getattr(request.user, 'role', '') in [UserRoleChoices.SUPERADMIN, UserRoleChoices.INSTITUTION_ADMIN]
        ))

class IsAcademicStaffUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            request.user.is_superuser or getattr(request.user, 'role', '') in [
                UserRoleChoices.SUPERADMIN,
                UserRoleChoices.INSTITUTION_ADMIN,
                UserRoleChoices.DEAN,
                UserRoleChoices.DEPARTMENT_HEAD,
                UserRoleChoices.INSTRUCTOR,
                UserRoleChoices.TEACHING_ASSISTANT
            ]
        ))

class IsInstructorUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            request.user.is_superuser or getattr(request.user, 'role', '') in [UserRoleChoices.SUPERADMIN, UserRoleChoices.INSTRUCTOR]
        ))

class IsStudentUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and (
            request.user.is_superuser or getattr(request.user, 'role', '') == UserRoleChoices.STUDENT
        ))

class HasTenantAccess(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        user_inst = getattr(request.user, 'institution', None)
        obj_inst = getattr(obj, 'institution', None)
        if obj_inst and user_inst and obj_inst == user_inst:
            return True
        return False
