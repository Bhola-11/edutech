import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    if not value:
        return
    cleaned = re.sub(r'[\s\-\(\)\+]', '', value)
    if not cleaned.isdigit() or len(cleaned) < 7 or len(cleaned) > 15:
        raise ValidationError(
            _('Enter a valid international phone number (7 to 15 digits). Received: %(value)s'),
            params={'value': value},
            code='invalid_phone'
        )

def validate_gpa_score(value):
    if value is not None:
        if value < 0.0 or value > 10.0:
            raise ValidationError(
                _('GPA must be a valid numerical value between 0.00 and 10.00.'),
                code='invalid_gpa'
            )

def validate_percentage(value):
    if value is not None:
        if value < 0.0 or value > 100.0:
            raise ValidationError(
                _('Percentage must be between 0.00% and 100.00%.'),
                code='invalid_percentage'
            )

def validate_credit_hours(value):
    if value is not None:
        if value <= 0 or value > 30:
            raise ValidationError(
                _('Credit hours must be greater than 0 and cannot exceed 30 credits per course unit.'),
                code='invalid_credits'
            )

def validate_academic_year(value):
    if not value:
        return
    pattern = r'^\d{4}\s*-\s*\d{4}$'
    if not re.match(pattern, value):
        raise ValidationError(
            _('Academic year must follow the YYYY-YYYY format (e.g. 2026-2027).'),
            code='invalid_academic_year'
        )
    parts = [int(p.strip()) for p in value.split('-')]
    if parts[1] != parts[0] + 1:
        raise ValidationError(
            _('The ending year must be exactly one year after the beginning year.'),
            code='invalid_academic_year_sequence'
        )

def validate_alphanumeric_code(value):
    if not value:
        return
    if not re.match(r'^[A-Za-z0-9_\-]+$', value):
        raise ValidationError(
            _('Code must contain only letters, numbers, underscores, or hyphens.'),
            code='invalid_code'
        )

def validate_file_max_size(max_mb=10):
    def validator(file_obj):
        if not file_obj:
            return
        limit = max_mb * 1024 * 1024
        if file_obj.size > limit:
            raise ValidationError(
                _(f'File size must not exceed {max_mb} megabytes (MB). Uploaded file is {file_obj.size / (1024*1024):.2f} MB.'),
                code='file_too_large'
            )
    return validator
