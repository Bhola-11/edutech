from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from apps.accounts.models import User
from apps.institutions.models import Institution
from apps.courses.models import Course, CourseCategory
from apps.core.constants import UserRoleChoices

class APIEndpointsIntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.superadmin = User.objects.create_superuser(
            email='admin@api.edu',
            username='admin_api',
            password='AdminPassword123!'
        )
        self.student = User.objects.create_user(
            email='student@api.edu',
            username='student_api',
            password='Password123!',
            role=UserRoleChoices.STUDENT
        )
        self.inst = Institution.objects.create(
            name='API Tech University',
            code='APITU',
            contact_email='info@apitu.edu',
            city='New York',
            country='US'
        )

    def test_users_api_authenticated(self):
        self.client.force_authenticate(user=self.superadmin)
        response = self.client.get('/api/v1/auth/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(response.data['count'], 2)

    def test_users_me_api(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/v1/auth/users/me/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'student@api.edu')

    def test_institutions_api(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/v1/institutions/institutions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data['results']), 1)

    def test_courses_api(self):
        self.client.force_authenticate(user=self.student)
        response = self.client.get('/api/v1/courses/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
