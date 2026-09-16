from django.urls import path
from . import views

app_name = 'profiles'

urlpatterns = [
    path('faculty/', views.InstructorDirectoryView.as_view(), name='faculty_directory'),
    path('faculty/<uuid:pk>/', views.FacultyProfileDetailView.as_view(), name='faculty_detail'),
    path('student/<uuid:pk>/', views.StudentProfileDetailView.as_view(), name='student_detail'),
]
