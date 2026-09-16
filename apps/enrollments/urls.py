from django.urls import path
from . import views

app_name = 'enrollments'

urlpatterns = [
    path('admissions/', views.AdmissionCycleListView.as_view(), name='cycle_list'),
    path('admissions/apply/', views.ApplicationCreateView.as_view(), name='apply'),
    path('admissions/my-applications/', views.MyApplicationListView.as_view(), name='my_applications'),
    path('admissions/applications/<uuid:pk>/', views.ApplicationDetailView.as_view(), name='application_detail'),
    path('admissions/applications/<uuid:pk>/review/', views.ApplicationReviewView.as_view(), name='application_review'),
    path('enroll/<slug:course_slug>/', views.QuickEnrollView.as_view(), name='quick_enroll'),
    path('my-courses/', views.MyEnrollmentsListView.as_view(), name='my_enrollments'),
]
