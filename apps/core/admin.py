from django.contrib import admin
from .models import ActivityLog, SystemNotification, ConfigurationSetting

@admin.register(ActivityLog)
class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('action', 'entity_name', 'user', 'ip_address', 'status_code', 'created_at')
    list_filter = ('action', 'request_method', 'status_code', 'created_at')
    search_fields = ('entity_name', 'entity_id', 'ip_address', 'user__username', 'user__email')
    readonly_fields = ('created_at', 'updated_at', 'details')

@admin.register(SystemNotification)
class SystemNotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient', 'priority', 'is_read', 'created_at')
    list_filter = ('priority', 'is_read', 'created_at')
    search_fields = ('title', 'message', 'recipient__username', 'recipient__email')

@admin.register(ConfigurationSetting)
class ConfigurationSettingAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'is_public', 'updated_at')
    search_fields = ('key', 'value', 'description')
