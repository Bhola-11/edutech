from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import UserViewSet, UserSessionLogViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'sessions', UserSessionLogViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
