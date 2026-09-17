from django.urls import path
from . import views

app_name = 'grading'

urlpatterns = [
    path('course/<int:course_id>/', views.gradebook_view, name='gradebook'),
    path('transcript/', views.transcript_view, name='transcript'),
    path('transcript/<int:student_id>/', views.transcript_view, name='student_transcript'),
]
