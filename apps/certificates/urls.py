from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.certificate_list, name='list'),
    path('verify/', views.verify_certificate_public, name='verify_public'),
    path('verify/<str:certificate_number>/', views.verify_certificate_public, name='verify_code'),
    path('download/<uuid:certificate_id>/', views.download_certificate_pdf, name='download_pdf'),
]
