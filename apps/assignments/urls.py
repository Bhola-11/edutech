from django.urls import path
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.assignment_list, name='list'),
    path('<int:pk>/', views.assignment_detail, name='detail'),
    path('<int:pk>/submit/', views.assignment_submit, name='submit'),
]
