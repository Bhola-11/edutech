from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import InstitutionViewSet, CampusViewSet, DepartmentViewSet, ClassroomViewSet

router = DefaultRouter()
router.register(r'institutions', InstitutionViewSet, basename='institution')
router.register(r'campuses', CampusViewSet, basename='campus')
router.register(r'departments', DepartmentViewSet, basename='department')
router.register(r'classrooms', ClassroomViewSet, basename='classroom')

urlpatterns = [
    path('', include(router.urls)),
]
