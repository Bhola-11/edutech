"""
Multi-Factor Authentication (MFA / 2FA) Service.
Implements RFC 6238 TOTP generation, validation, drift windows, and backup codes.
"""
import hmac
import hashlib
import time
import base64
import struct
import secrets
from typing import Tuple, List, Optional
from django.utils import timezone


class MFAService:
    DIGITS = 6
    INTERVAL = 30  # 30-second TOTP step
    BACKUP_CODE_COUNT = 10
    BACKUP_CODE_LENGTH = 10

    @classmethod
    def generate_secret(cls) -> str:
        """Generates a secure 32-character base32 secret key."""
        random_bytes = secrets.token_bytes(20)
        return base64.b32encode(random_bytes).decode('utf-8').rstrip('=')

    @classmethod
    def generate_provisioning_uri(cls, username: str, secret: str, issuer: str = 'EduTech Enterprise') -> str:
        """Generates otpauth URI for authenticator apps (Google Authenticator, Authy, 1Password)."""
        import urllib.parse
        encoded_issuer = urllib.parse.quote(issuer)
        encoded_user = urllib.parse.quote(username)
        return f"otpauth://totp/{encoded_issuer}:{encoded_user}?secret={secret}&issuer={encoded_issuer}&algorithm=SHA1&digits={cls.DIGITS}&period={cls.INTERVAL}"

    @classmethod
    def generate_totp_token(cls, secret: str, time_step: Optional[int] = None) -> str:
        """Computes current RFC 6238 TOTP code."""
        if time_step is None:
            time_step = int(time.time()) // cls.INTERVAL

        # Normalize secret padding
        padded_secret = secret.upper() + '=' * ((8 - len(secret) % 8) % 8)
        key = base64.b32decode(padded_secret, casefold=True)

        counter_bytes = struct.pack('>Q', time_step)
        hmac_digest = hmac.new(key, counter_bytes, hashlib.sha1).digest()

        offset = hmac_digest[-1] & 0x0F
        binary = struct.unpack('>I', hmac_digest[offset:offset+4])[0] & 0x7FFFFFFF
        code = binary % (10 ** cls.DIGITS)
        return str(code).zfill(cls.DIGITS)

    @classmethod
    def verify_totp(cls, secret: str, token: str, window: int = 1) -> bool:
        """Verifies code allowing for time drift (window * 30 seconds back and forward)."""
        clean_token = token.strip().replace(' ', '')
        if len(clean_token) != cls.DIGITS or not clean_token.isdigit():
            return False

        current_step = int(time.time()) // cls.INTERVAL
        for drift in range(-window, window + 1):
            valid_code = cls.generate_totp_token(secret, time_step=current_step + drift)
            if hmac.compare_digest(clean_token, valid_code):
                return True
        return False

    @classmethod
    def generate_backup_recovery_codes(cls) -> List[str]:
        """Generates single-use alphanumeric emergency recovery codes."""
        codes = []
        for _ in range(cls.BACKUP_CODE_COUNT):
            code = secrets.token_hex(cls.BACKUP_CODE_LENGTH // 2).upper()
            formatted = f"{code[:5]}-{code[5:]}"
            codes.append(formatted)
        return codes
