from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('', views.assessment_list, name='list'),
    path('create/', views.assessment_create, name='create'),
    path('<int:pk>/', views.assessment_detail, name='detail'),
    path('sandbox/', views.code_sandbox_view, name='sandbox'),
    path('api/run-code/', views.run_code_api, name='api_run_code'),
]
