from apps.core.constants import UserRoleChoices

class SystemPermissions:
    # Course Permissions
    COURSE_CREATE = 'course.create'
    COURSE_EDIT = 'course.edit'
    COURSE_DELETE = 'course.delete'
    COURSE_PUBLISH = 'course.publish'
    COURSE_ENROLL = 'course.enroll'
    COURSE_VIEW = 'course.view'
    
    # Institution Permissions
    INSTITUTION_MANAGE = 'institution.manage'
    CAMPUS_CREATE = 'campus.create'
    DEPARTMENT_MANAGE = 'department.manage'
    CLASSROOM_ALLOCATE = 'classroom.allocate'
    
    # Admissions & Enrollment Permissions
    ADMISSION_CYCLE_MANAGE = 'admission.cycle_manage'
    APPLICATION_REVIEW = 'application.review'
    APPLICATION_SUBMIT = 'application.submit'
    GRADE_ASSIGN = 'grade.assign'
    TRANSCRIPT_GENERATE = 'transcript.generate'

    # Security & Audit
    AUDIT_LOG_VIEW = 'audit.view'
    USER_MANAGE = 'user.manage'
    CONFIG_EDIT = 'config.edit'

ROLE_PERMISSIONS_MAP = {
    UserRoleChoices.SUPERADMIN: {
        SystemPermissions.COURSE_CREATE, SystemPermissions.COURSE_EDIT, SystemPermissions.COURSE_DELETE,
        SystemPermissions.COURSE_PUBLISH, SystemPermissions.COURSE_ENROLL, SystemPermissions.COURSE_VIEW,
        SystemPermissions.INSTITUTION_MANAGE, SystemPermissions.CAMPUS_CREATE, SystemPermissions.DEPARTMENT_MANAGE,
        SystemPermissions.CLASSROOM_ALLOCATE, SystemPermissions.ADMISSION_CYCLE_MANAGE, SystemPermissions.APPLICATION_REVIEW,
        SystemPermissions.APPLICATION_SUBMIT, SystemPermissions.GRADE_ASSIGN, SystemPermissions.TRANSCRIPT_GENERATE,
        SystemPermissions.AUDIT_LOG_VIEW, SystemPermissions.USER_MANAGE, SystemPermissions.CONFIG_EDIT
    },
    UserRoleChoices.INSTITUTION_ADMIN: {
        SystemPermissions.COURSE_CREATE, SystemPermissions.COURSE_EDIT, SystemPermissions.COURSE_PUBLISH,
        SystemPermissions.COURSE_VIEW, SystemPermissions.CAMPUS_CREATE, SystemPermissions.DEPARTMENT_MANAGE,
        SystemPermissions.CLASSROOM_ALLOCATE, SystemPermissions.ADMISSION_CYCLE_MANAGE, SystemPermissions.APPLICATION_REVIEW,
        SystemPermissions.TRANSCRIPT_GENERATE, SystemPermissions.USER_MANAGE
    },
    UserRoleChoices.DEAN: {
        SystemPermissions.COURSE_CREATE, SystemPermissions.COURSE_EDIT, SystemPermissions.COURSE_PUBLISH,
        SystemPermissions.COURSE_VIEW, SystemPermissions.DEPARTMENT_MANAGE, SystemPermissions.CLASSROOM_ALLOCATE,
        SystemPermissions.APPLICATION_REVIEW, SystemPermissions.GRADE_ASSIGN, SystemPermissions.TRANSCRIPT_GENERATE
    },
    UserRoleChoices.DEPARTMENT_HEAD: {
        SystemPermissions.COURSE_CREATE, SystemPermissions.COURSE_EDIT, SystemPermissions.COURSE_VIEW,
        SystemPermissions.CLASSROOM_ALLOCATE, SystemPermissions.APPLICATION_REVIEW, SystemPermissions.GRADE_ASSIGN
    },
    UserRoleChoices.INSTRUCTOR: {
        SystemPermissions.COURSE_CREATE, SystemPermissions.COURSE_EDIT, SystemPermissions.COURSE_VIEW,
        SystemPermissions.GRADE_ASSIGN
    },
    UserRoleChoices.TEACHING_ASSISTANT: {
        SystemPermissions.COURSE_VIEW, SystemPermissions.GRADE_ASSIGN
    },
    UserRoleChoices.STUDENT: {
        SystemPermissions.COURSE_VIEW, SystemPermissions.COURSE_ENROLL, SystemPermissions.APPLICATION_SUBMIT
    },
    UserRoleChoices.PARENT: {
        SystemPermissions.COURSE_VIEW
    },
    UserRoleChoices.CORPORATE_PARTNER: {
        SystemPermissions.COURSE_VIEW, SystemPermissions.COURSE_ENROLL
    }
}

class RBACService:
    @staticmethod
    def user_has_permission(user, permission_code):
        if not user or not user.is_authenticated:
            return False
        if user.is_superuser:
            return True
        user_role = getattr(user, 'role', None)
        granted_permissions = ROLE_PERMISSIONS_MAP.get(user_role, set())
        return permission_code in granted_permissions

    @staticmethod
    def get_all_permissions_for_user(user):
        if not user or not user.is_authenticated:
            return set()
        if user.is_superuser:
            return set(getattr(SystemPermissions, attr) for attr in dir(SystemPermissions) if not attr.startswith('__'))
        user_role = getattr(user, 'role', None)
        return ROLE_PERMISSIONS_MAP.get(user_role, set())
