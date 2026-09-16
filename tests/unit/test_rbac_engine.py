from django.test import TestCase
from apps.accounts.models import User
from apps.core.constants import UserRoleChoices
from apps.accounts.rbac_engine import RBACService, SystemPermissions

class RBACEngineTests(TestCase):
    def setUp(self):
        self.instructor = User.objects.create_user(email='inst@test.edu', username='inst', role=UserRoleChoices.INSTRUCTOR)
        self.student = User.objects.create_user(email='stud@test.edu', username='stud', role=UserRoleChoices.STUDENT)

    def test_instructor_permissions(self):
        can_create_course = RBACService.user_has_permission(self.instructor, SystemPermissions.COURSE_CREATE)
        can_manage_institutions = RBACService.user_has_permission(self.instructor, SystemPermissions.INSTITUTION_MANAGE)
        self.assertTrue(can_create_course)
        self.assertFalse(can_manage_institutions)

    def test_student_permissions(self):
        can_enroll = RBACService.user_has_permission(self.student, SystemPermissions.COURSE_ENROLL)
        can_assign_grade = RBACService.user_has_permission(self.student, SystemPermissions.GRADE_ASSIGN)
        self.assertTrue(can_enroll)
        self.assertFalse(can_assign_grade)
