from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AssessmentViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'items', AssessmentViewSet, basename='assessment')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
]
