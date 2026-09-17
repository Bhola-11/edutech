from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import GradingScaleViewSet, FinalCourseGradeViewSet

router = DefaultRouter()
router.register(r'scales', GradingScaleViewSet, basename='scale')
router.register(r'final-grades', FinalCourseGradeViewSet, basename='final-grade')

urlpatterns = [
    path('', include(router.urls)),
]
