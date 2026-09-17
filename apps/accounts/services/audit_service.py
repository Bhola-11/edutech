"""
Enterprise Security Audit Logging Service.
Captures authentication events, IP addresses, suspicious role changes, and compliance trails.
"""
from typing import Optional, Dict, Any
from django.utils import timezone
from apps.core.models import ActivityLog


class SecurityAuditService:
    @classmethod
    def log_auth_event(
        cls,
        user,
        event_type: str,
        ip_address: str,
        user_agent: str,
        status: str = 'SUCCESS',
        metadata: Optional[Dict[str, Any]] = None
    ) -> ActivityLog:
        """Logs user authentication, login attempts, MFA challenges, and logout."""
        description = f"Auth Event: {event_type} - Status: {status} from IP {ip_address}"
        return ActivityLog.objects.create(
            actor=user,
            action=event_type,
            target_model='User',
            target_id=str(user.pk) if user else 'ANONYMOUS',
            ip_address=ip_address,
            user_agent=user_agent[:500] if user_agent else '',
            payload={
                'status': status,
                'timestamp': timezone.now().isoformat(),
                **(metadata or {})
            }
        )

    @classmethod
    def log_role_change(
        cls,
        admin_user,
        target_user,
        old_role: str,
        new_role: str,
        reason: str = ''
    ) -> ActivityLog:
        """Logs critical RBAC privilege changes and role promotions."""
        return ActivityLog.objects.create(
            actor=admin_user,
            action='ROLE_MODIFICATION',
            target_model='User',
            target_id=str(target_user.pk),
            payload={
                'target_username': target_user.username,
                'old_role': old_role,
                'new_role': new_role,
                'reason': reason,
                'elevated_by': admin_user.username if admin_user else 'SYSTEM'
            }
        )
