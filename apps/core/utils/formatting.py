import re
from decimal import Decimal

def format_currency(amount, currency_symbol='$', decimal_places=2):
    if amount is None:
        return f'{currency_symbol}0.00'
    try:
        val = Decimal(str(amount))
        return f'{currency_symbol}{val:,.{decimal_places}f}'
    except Exception:
        return f'{currency_symbol}{amount}'

def format_filesize(num_bytes):
    if not num_bytes:
        return '0 B'
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if abs(num_bytes) < 1024.0:
            return f'{num_bytes:3.1f} {unit}'
        num_bytes /= 1024.0
    return f'{num_bytes:.1f} PB'

def mask_email_address(email):
    if not email or '@' not in email:
        return email
    user, domain = email.split('@', 1)
    if len(user) <= 2:
        masked_user = user[0] + '*'
    else:
        masked_user = user[0] + ('*' * (len(user) - 2)) + user[-1]
    return f'{masked_user}@{domain}'

def mask_phone_number(phone):
    if not phone or len(phone) < 4:
        return phone
    return phone[:3] + ('*' * (len(phone) - 5)) + phone[-2:]
