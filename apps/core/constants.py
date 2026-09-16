from django.db import models

class UserRoleChoices(models.TextChoices):
    SUPERADMIN = 'SUPERADMIN', 'Super Administrator'
    INSTITUTION_ADMIN = 'INSTITUTION_ADMIN', 'Institution Administrator'
    DEAN = 'DEAN', 'Dean / Faculty Head'
    DEPARTMENT_HEAD = 'DEPARTMENT_HEAD', 'Head of Department'
    INSTRUCTOR = 'INSTRUCTOR', 'Faculty / Instructor'
    TEACHING_ASSISTANT = 'TEACHING_ASSISTANT', 'Teaching Assistant'
    STUDENT = 'STUDENT', 'Student / Learner'
    PARENT = 'PARENT', 'Parent / Guardian'
    MENTOR = 'MENTOR', 'Career Mentor / Advisor'
    CORPORATE_PARTNER = 'CORPORATE_PARTNER', 'Corporate Training Partner'
    ALUMNI = 'ALUMNI', 'Alumni Member'
    AUDITOR = 'AUDITOR', 'Academic Auditor'

class EntityStatusChoices(models.TextChoices):
    DRAFT = 'DRAFT', 'Draft'
    PENDING_APPROVAL = 'PENDING_APPROVAL', 'Pending Approval'
    ACTIVE = 'ACTIVE', 'Active'
    INACTIVE = 'INACTIVE', 'Inactive'
    ARCHIVED = 'ARCHIVED', 'Archived'
    SUSPENDED = 'SUSPENDED', 'Suspended'
    DELETED = 'DELETED', 'Soft Deleted'

class AcademicLevelChoices(models.TextChoices):
    PRIMARY = 'PRIMARY', 'Primary Education'
    SECONDARY = 'SECONDARY', 'Secondary Education'
    HIGHER_SECONDARY = 'HIGHER_SECONDARY', 'Higher Secondary'
    UNDERGRADUATE = 'UNDERGRADUATE', 'Undergraduate Degree (Bachelor)'
    POSTGRADUATE = 'POSTGRADUATE', 'Postgraduate Degree (Master)'
    DOCTORATE = 'DOCTORATE', 'Doctorate (Ph.D.)'
    DIPLOMA = 'DIPLOMA', 'Post-Secondary Diploma'
    CERTIFICATE = 'CERTIFICATE', 'Professional Certification'
    EXECUTIVE_EDUCATION = 'EXECUTIVE_EDUCATION', 'Executive Education'

class GenderChoices(models.TextChoices):
    MALE = 'MALE', 'Male'
    FEMALE = 'FEMALE', 'Female'
    NON_BINARY = 'NON_BINARY', 'Non-Binary'
    PREFER_NOT_TO_SAY = 'PREFER_NOT_TO_SAY', 'Prefer Not to Say'
    OTHER = 'OTHER', 'Other'

class BloodGroupChoices(models.TextChoices):
    A_POSITIVE = 'A+', 'A Positive (A+)'
    A_NEGATIVE = 'A-', 'A Negative (A-)'
    B_POSITIVE = 'B+', 'B Positive (B+)'
    B_NEGATIVE = 'B-', 'B Negative (B-)'
    AB_POSITIVE = 'AB+', 'AB Positive (AB+)'
    AB_NEGATIVE = 'AB-', 'AB Negative (AB-)'
    O_POSITIVE = 'O+', 'O Positive (O+)'
    O_NEGATIVE = 'O-', 'O Negative (O-)'
    UNKNOWN = 'UNKNOWN', 'Unknown'

class PriorityChoices(models.TextChoices):
    LOW = 'LOW', 'Low Priority'
    MEDIUM = 'MEDIUM', 'Medium Priority'
    HIGH = 'HIGH', 'High Priority'
    CRITICAL = 'CRITICAL', 'Critical / Urgent'

class AuditActionChoices(models.TextChoices):
    CREATE = 'CREATE', 'Created Record'
    UPDATE = 'UPDATE', 'Updated Record'
    DELETE = 'DELETE', 'Deleted Record'
    SOFT_DELETE = 'SOFT_DELETE', 'Soft-Deleted Record'
    RESTORE = 'RESTORE', 'Restored Record'
    LOGIN_SUCCESS = 'LOGIN_SUCCESS', 'Successful Authentication'
    LOGIN_FAILED = 'LOGIN_FAILED', 'Failed Authentication Attempt'
    LOGOUT = 'LOGOUT', 'User Logout'
    PASSWORD_CHANGE = 'PASSWORD_CHANGE', 'Password Changed'
    PASSWORD_RESET = 'PASSWORD_RESET', 'Password Reset Requested'
    PERMISSION_CHANGE = 'PERMISSION_CHANGE', 'Role / Permissions Altered'
    DATA_EXPORT = 'DATA_EXPORT', 'Sensitive Data Exported'
    IMPERSONATION_START = 'IMPERSONATION_START', 'Admin Impersonation Started'
    IMPERSONATION_END = 'IMPERSONATION_END', 'Admin Impersonation Ended'
