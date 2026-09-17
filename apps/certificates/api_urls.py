from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import IssuedCertificateViewSet, DigitalBadgeViewSet

router = DefaultRouter()
router.register(r'credentials', IssuedCertificateViewSet, basename='credential')
router.register(r'badges', DigitalBadgeViewSet, basename='badge')

urlpatterns = [
    path('', include(router.urls)),
]
