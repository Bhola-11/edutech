from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.core.constants import UserRoleChoices

User = get_user_model()

class AccountsModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='testuser@edutech.edu',
            username='testuser',
            password='Password123!',
            first_name='Test',
            last_name='User',
            role=UserRoleChoices.STUDENT
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'testuser@edutech.edu')
        self.assertTrue(self.user.check_password('Password123!'))
        self.assertEqual(self.user.role, UserRoleChoices.STUDENT)
        self.assertTrue(self.user.is_student)
        self.assertFalse(self.user.is_superadmin)

    def test_superuser_creation(self):
        super_admin = User.objects.create_superuser(
            email='admin@edutech.edu',
            username='adminuser',
            password='AdminPassword123!'
        )
        self.assertTrue(super_admin.is_staff)
        self.assertTrue(super_admin.is_superuser)
        self.assertEqual(super_admin.role, UserRoleChoices.SUPERADMIN)
        self.assertTrue(super_admin.is_superadmin)
