from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserSessionLog, PasswordHistory, TwoFactorToken

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'institution', 'is_staff', 'is_verified')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active', 'is_verified', 'institution')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('-date_joined',)
    fieldsets = UserAdmin.fieldsets + (
        ('EdTech Academic Affiliation', {
            'fields': ('role', 'institution', 'campus', 'department', 'phone_number', 'profile_photo', 'date_of_birth', 'gender', 'bio', 'is_verified', 'two_factor_enabled')
        }),
    )

@admin.register(UserSessionLog)
class UserSessionLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'session_key', 'ip_address', 'device_info', 'created_at', 'is_expired')
    list_filter = ('is_expired', 'created_at')
    search_fields = ('user__username', 'user__email', 'ip_address', 'session_key')

@admin.register(TwoFactorToken)
class TwoFactorTokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token_code', 'expires_at', 'is_used', 'attempts', 'created_at')
    list_filter = ('is_used', 'created_at')
    search_fields = ('user__username', 'user__email', 'token_code')
