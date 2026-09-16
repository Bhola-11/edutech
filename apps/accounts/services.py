import random
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password, make_password
from .models import User, UserSessionLog, PasswordHistory, TwoFactorToken
from apps.core.models import ActivityLog
from apps.core.constants import AuditActionChoices

class AuthenticationService:
    @staticmethod
    def process_login(request, user, remember_me=False):
        login(request, user)
        if not remember_me:
            request.session.set_expiry(0)
        else:
            request.session.set_expiry(1209600) # 2 weeks

        session_key = request.session.session_key or ''
        ip_addr = request.META.get('HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', ''))
        if ip_addr and ',' in ip_addr:
            ip_addr = ip_addr.split(',')[0].strip()

        UserSessionLog.objects.create(
            user=user,
            session_key=session_key,
            ip_address=ip_addr,
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:250],
            device_info='Web Browser'
        )

        ActivityLog.objects.create(
            user=user,
            action=AuditActionChoices.LOGIN_SUCCESS,
            entity_name='UserSession',
            entity_id=str(user.id),
            ip_address=ip_addr,
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:250],
            request_method=request.method,
            request_path=request.path,
            details={'email': user.email, 'role': user.role}
        )

    @staticmethod
    def process_logout(request):
        if request.user.is_authenticated:
            session_key = request.session.session_key
            if session_key:
                UserSessionLog.objects.filter(user=request.user, session_key=session_key, is_expired=False).update(
                    is_expired=True,
                    logged_out_at=timezone.now()
                )
            ActivityLog.objects.create(
                user=request.user,
                action=AuditActionChoices.LOGOUT,
                entity_name='UserSession',
                entity_id=str(request.user.id),
                ip_address=request.META.get('REMOTE_ADDR', ''),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:250],
                request_method=request.method,
                request_path=request.path
            )
        logout(request)

class TwoFactorService:
    @staticmethod
    def generate_token(user):
        TwoFactorToken.objects.filter(user=user, is_used=False).update(is_used=True)
        code = f'{random.randint(100000, 999999)}'
        expires_at = timezone.now() + timedelta(minutes=10)
        token = TwoFactorToken.objects.create(
            user=user,
            token_code=code,
            expires_at=expires_at
        )
        return token

    @staticmethod
    def verify_token(user, code):
        tokens = TwoFactorToken.objects.filter(user=user, is_used=False).order_by('-created_at')
        if not tokens.exists():
            return False
        latest_token = tokens.first()
        if not latest_token.is_valid():
            return False
        if latest_token.token_code == code.strip():
            latest_token.is_used = True
            latest_token.save()
            return True
        else:
            latest_token.attempts += 1
            latest_token.save()
            return False

class PasswordSecurityService:
    @staticmethod
    def record_password_history(user, raw_password):
        PasswordHistory.objects.create(
            user=user,
            password_hash=make_password(raw_password)
        )

    @staticmethod
    def is_password_reused(user, raw_password, limit=5):
        recent_passwords = PasswordHistory.objects.filter(user=user).order_by('-created_at')[:limit]
        for history in recent_passwords:
            if check_password(raw_password, history.password_hash):
                return True
        return False
