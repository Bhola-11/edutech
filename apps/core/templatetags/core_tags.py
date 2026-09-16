from django import template
from django.utils.safestring import mark_safe
from apps.core.utils.formatting import format_currency, format_filesize, mask_email_address

register = template.Library()

@register.filter(name='currency')
def currency_filter(value, symbol='$'):
    return format_currency(value, symbol)

@register.filter(name='filesize')
def filesize_filter(value):
    return format_filesize(value)

@register.filter(name='mask_email')
def mask_email_filter(value):
    return mask_email_address(value)

@register.filter(name='badge_status')
def badge_status_filter(status):
    status = str(status).upper()
    color_map = {
        'ACTIVE': 'success',
        'APPROVED': 'success',
        'COMPLETED': 'success',
        'PUBLISHED': 'success',
        'VERIFIED': 'success',
        'PENDING': 'warning',
        'PENDING_APPROVAL': 'warning',
        'IN_PROGRESS': 'info',
        'DRAFT': 'secondary',
        'INACTIVE': 'dark',
        'ARCHIVED': 'secondary',
        'REJECTED': 'danger',
        'SUSPENDED': 'danger',
        'FAILED': 'danger',
        'CRITICAL': 'danger',
        'HIGH': 'warning',
        'MEDIUM': 'primary',
        'LOW': 'info',
    }
    badge_class = color_map.get(status, 'secondary')
    display_text = status.replace('_', ' ').title()
    return mark_safe(f'<span class=\"badge bg-{badge_class}\">{display_text}</span>')

@register.filter(name='role_badge')
def role_badge_filter(role):
    role_str = str(role).upper()
    color_map = {
        'SUPERADMIN': 'dark',
        'INSTITUTION_ADMIN': 'primary',
        'DEAN': 'info',
        'DEPARTMENT_HEAD': 'info',
        'INSTRUCTOR': 'success',
        'TEACHING_ASSISTANT': 'secondary',
        'STUDENT': 'primary',
        'PARENT': 'warning',
        'MENTOR': 'success',
        'CORPORATE_PARTNER': 'dark',
    }
    badge_class = color_map.get(role_str, 'secondary')
    display_text = role_str.replace('_', ' ').title()
    return mark_safe(f'<span class=\"badge bg-{badge_class} text-uppercase\">{display_text}</span>')
