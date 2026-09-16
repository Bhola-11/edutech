from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.core.constants import UserRoleChoices

User = get_user_model()

class WebWorkflowIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.student = User.objects.create_user(
            email='student@test.edu',
            username='student1',
            password='Password123!',
            role=UserRoleChoices.STUDENT
        )

    def test_homepage_renders(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'EduTech')

    def test_course_list_renders(self):
        response = self.client.get(reverse('courses:course_list'))
        self.assertEqual(response.status_code, 200)

    def test_login_flow(self):
        login_url = reverse('accounts:login')
        response = self.client.post(login_url, {
            'email': 'student@test.edu',
            'password': 'Password123!'
        })
        self.assertEqual(response.status_code, 302)
