from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import StudentProfileViewSet, InstructorProfileViewSet, AcademicCredentialViewSet

router = DefaultRouter()
router.register(r'students', StudentProfileViewSet, basename='student')
router.register(r'instructors', InstructorProfileViewSet, basename='instructor')
router.register(r'credentials', AcademicCredentialViewSet, basename='credential')

urlpatterns = [
    path('', include(router.urls)),
]
