from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AdmissionApplicationViewSet, StudentEnrollmentViewSet, BatchViewSet

router = DefaultRouter()
router.register(r'applications', AdmissionApplicationViewSet, basename='application')
router.register(r'enrollments', StudentEnrollmentViewSet, basename='enrollment')
router.register(r'batches', BatchViewSet, basename='batch')

urlpatterns = [
    path('', include(router.urls)),
]
