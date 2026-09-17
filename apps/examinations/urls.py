from django.urls import path
from . import views

app_name = 'examinations'

urlpatterns = [
    path('', views.exam_session_list, name='list'),
    path('take/<int:session_id>/', views.exam_taker_view, name='take'),
    path('monitor/<int:session_id>/', views.proctor_monitor_view, name='monitor'),
    path('api/log-event/', views.log_proctoring_event_api, name='api_log_event'),
]
