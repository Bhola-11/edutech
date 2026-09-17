from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('accounts/', include('apps.accounts.urls')),
    path('institutions/', include('apps.institutions.urls')),
    path('courses/', include('apps.courses.urls')),
    path('enrollments/', include('apps.enrollments.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('assessments/', include('apps.assessments.urls')),
    path('examinations/', include('apps.examinations.urls')),
    path('assignments/', include('apps.assignments.urls')),
    path('grading/', include('apps.grading.urls')),
    path('certificates/', include('apps.certificates.urls')),

    # REST Framework API Endpoints
    path('api/v1/auth/', include('apps.accounts.api_urls')),
    path('api/v1/institutions/', include('apps.institutions.api_urls')),
    path('api/v1/courses/', include('apps.courses.api_urls')),
    path('api/v1/enrollments/', include('apps.enrollments.api_urls')),
    path('api/v1/profiles/', include('apps.profiles.api_urls')),
    path('api/v1/assessments/', include('apps.assessments.api_urls')),
    path('api/v1/examinations/', include('apps.examinations.api_urls')),
    path('api/v1/assignments/', include('apps.assignments.api_urls')),
    path('api/v1/grading/', include('apps.grading.api_urls')),
    path('api/v1/certificates/', include('apps.certificates.api_urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
