from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AssignmentViewSet, AssignmentSubmissionViewSet

router = DefaultRouter()
router.register(r'items', AssignmentViewSet, basename='assignment')
router.register(r'submissions', AssignmentSubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
]
