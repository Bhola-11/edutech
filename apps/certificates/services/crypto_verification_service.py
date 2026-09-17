"""
Cryptographic Certificate Verification & SHA-256 Signature Engine.
"""
import hashlib
import hmac
import uuid
from typing import Dict, Any


class CertificateCryptoService:
    SECRET_SALT = "EduTech-Enterprise-Cryptographic-Verification-Salt-2026"

    @classmethod
    def generate_verification_hash(
        cls,
        student_id: int,
        course_code: str,
        certificate_number: str,
        issue_date_str: str
    ) -> str:
        """Computes secure SHA-256 digest token for public certificate verification."""
        payload = f"{student_id}:{course_code}:{certificate_number}:{issue_date_str}:{cls.SECRET_SALT}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    @classmethod
    def verify_hash(
        cls,
        student_id: int,
        course_code: str,
        certificate_number: str,
        issue_date_str: str,
        provided_hash: str
    ) -> bool:
        """Verifies integrity of a certificate against tamper attempts."""
        expected = cls.generate_verification_hash(student_id, course_code, certificate_number, issue_date_str)
        return hmac.compare_digest(expected, provided_hash)
