from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('', views.CourseListView.as_view(), name='course_list'),
    path('create/', views.CourseCreateView.as_view(), name='course_create'),
    path('programs/', views.ProgramListView.as_view(), name='program_list'),
    path('programs/<slug:slug>/', views.ProgramDetailView.as_view(), name='program_detail'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
    path('<slug:slug>/edit/', views.CourseUpdateView.as_view(), name='course_update'),
    path('<slug:slug>/review/', views.SubmitReviewView.as_view(), name='course_review'),
    path('lessons/<uuid:pk>/', views.LessonPlayerView.as_view(), name='lesson_player'),
]
