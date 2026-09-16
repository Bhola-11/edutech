from django.urls import path
from . import views

app_name = 'institutions'

urlpatterns = [
    path('', views.InstitutionListView.as_view(), name='institution_list'),
    path('create/', views.InstitutionCreateView.as_view(), name='institution_create'),
    path('<slug:slug>/', views.InstitutionDetailView.as_view(), name='institution_detail'),
    path('<slug:slug>/edit/', views.InstitutionUpdateView.as_view(), name='institution_update'),
    path('campuses/all/', views.CampusListView.as_view(), name='campus_list'),
    path('campuses/<slug:slug>/', views.CampusDetailView.as_view(), name='campus_detail'),
    path('departments/all/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/<slug:slug>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('classrooms/all/', views.ClassroomListView.as_view(), name='classroom_list'),
]
