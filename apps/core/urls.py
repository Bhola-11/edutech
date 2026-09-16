from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('dashboard/', views.DashboardRedirectView.as_view(), name='dashboard'),
    path('dashboard/superadmin/', views.SuperAdminDashboardView.as_view(), name='superadmin_dashboard'),
    path('dashboard/admin/', views.InstitutionAdminDashboardView.as_view(), name='admin_dashboard'),
    path('dashboard/instructor/', views.InstructorDashboardView.as_view(), name='instructor_dashboard'),
    path('dashboard/student/', views.StudentDashboardView.as_view(), name='student_dashboard'),
    path('dashboard/parent/', views.ParentDashboardView.as_view(), name='parent_dashboard'),
    path('dashboard/corporate/', views.CorporateDashboardView.as_view(), name='corporate_dashboard'),
    path('notifications/', views.NotificationListView.as_view(), name='notifications'),
    path('notifications/<uuid:pk>/read/', views.MarkNotificationReadView.as_view(), name='notification_mark_read'),
    path('health/', views.HealthCheckView.as_view(), name='health_check'),
]
