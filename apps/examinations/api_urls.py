from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ExamSessionViewSet, ExamAttemptViewSet, ProctoringEventViewSet

router = DefaultRouter()
router.register(r'sessions', ExamSessionViewSet, basename='session')
router.register(r'attempts', ExamAttemptViewSet, basename='attempt')
router.register(r'proctor-events', ProctoringEventViewSet, basename='proctor-event')

urlpatterns = [
    path('', include(router.urls)),
]
