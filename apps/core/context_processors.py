from django.conf import settings
from .constants import UserRoleChoices

def global_context(request):
    unread_notifications_count = 0
    recent_notifications = []
    if hasattr(request, 'user') and request.user.is_authenticated:
        try:
            unread_notifications_count = request.user.system_notifications.filter(is_read=False).count()
            recent_notifications = request.user.system_notifications.filter(is_read=False)[:5]
        except Exception:
            pass

    return {
        'APP_NAME': 'EduTech Enterprise LMS',
        'APP_VERSION': '2.5.0-Enterprise',
        'USER_ROLES': UserRoleChoices,
        'unread_notifications_count': unread_notifications_count,
        'recent_notifications': recent_notifications,
        'current_tenant': getattr(request, 'tenant_institution', None),
        'current_campus': getattr(request, 'tenant_campus', None),
    }
