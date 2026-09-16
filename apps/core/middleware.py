import time
from django.utils import timezone
from .models import ActivityLog
from .constants import AuditActionChoices

class TenantResolutionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.tenant_institution = None
        request.tenant_campus = None

        if hasattr(request, 'user') and request.user.is_authenticated:
            if hasattr(request.user, 'institution') and request.user.institution:
                request.tenant_institution = request.user.institution
            if hasattr(request.user, 'campus') and request.user.campus:
                request.tenant_campus = request.user.campus

        response = self.get_response(request)
        return response

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        ip_addr = self.get_client_ip(request)
        request.client_ip = ip_addr

        if hasattr(request, 'user') and request.user.is_authenticated:
            request.user.last_activity = timezone.now()

        response = self.get_response(request)

        duration = time.time() - start_time
        response['X-Response-Time-Ms'] = f'{duration * 1000:.2f}ms'

        if request.method in ['POST', 'PUT', 'PATCH', 'DELETE'] and hasattr(request, 'user') and request.user.is_authenticated:
            try:
                action_map = {
                    'POST': AuditActionChoices.CREATE,
                    'PUT': AuditActionChoices.UPDATE,
                    'PATCH': AuditActionChoices.UPDATE,
                    'DELETE': AuditActionChoices.DELETE,
                }
                action = action_map.get(request.method, AuditActionChoices.UPDATE)
                path = request.path
                if not path.startswith('/admin/jsi18n/'):
                    ActivityLog.objects.create(
                        user=request.user,
                        action=action,
                        entity_name=path.split('/')[1] if len(path.split('/')) > 1 else 'root',
                        ip_address=ip_addr,
                        user_agent=request.META.get('HTTP_USER_AGENT', '')[:400],
                        request_method=request.method,
                        request_path=path[:500],
                        status_code=response.status_code,
                        details={'duration_ms': round(duration * 1000, 2)}
                    )
            except Exception:
                pass

        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

class SecurityHeadersMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['X-Content-Type-Options'] = 'nosniff'
        response['X-Frame-Options'] = 'DENY'
        response['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        response['X-XSS-Protection'] = '1; mode=block'
        return response
