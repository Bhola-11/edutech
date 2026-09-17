import uuid
from django.db import models
from apps.core.models import TimeStampedModel, MultiTenantModel
from apps.courses.models import Course, Program
from apps.accounts.models import User


class CertificateTemplate(TimeStampedModel, MultiTenantModel):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50)
    border_style = models.CharField(max_length=50, default='CLASSIC_GOLD')
    primary_color = models.CharField(max_length=20, default='#1E3A8A')
    secondary_color = models.CharField(max_length=20, default='#D97706')
    issuer_name = models.CharField(max_length=150)
    issuer_title = models.CharField(max_length=150)
    signature_title = models.CharField(max_length=150, default='Dean of Academic Affairs')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.institution.code})"


class IssuedCertificate(TimeStampedModel, MultiTenantModel):
    certificate_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='certificates')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True, related_name='issued_certificates')
    program = models.ForeignKey(Program, on_delete=models.SET_NULL, null=True, blank=True, related_name='issued_certificates')
    template = models.ForeignKey(CertificateTemplate, on_delete=models.SET_NULL, null=True)
    certificate_number = models.CharField(max_length=100, unique=True)
    verification_hash = models.CharField(max_length=64, unique=True)  # SHA-256 token
    issue_date = models.DateField()
    expiry_date = models.DateField(null=True, blank=True)
    final_grade_letter = models.CharField(max_length=10, blank=True)
    final_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    honors_title = models.CharField(max_length=100, blank=True)
    pdf_file = models.FileField(upload_to='certificates/%Y/%m/', blank=True)
    is_revoked = models.BooleanField(default=False)
    revocation_reason = models.TextField(blank=True)

    def __str__(self):
        return f"Cert {self.certificate_number} - {self.student.username}"


class CertificateVerificationLog(TimeStampedModel):
    certificate = models.ForeignKey(IssuedCertificate, on_delete=models.CASCADE, related_name='verification_logs')
    verifier_ip = models.GenericIPAddressField(null=True, blank=True)
    verifier_user_agent = models.CharField(max_length=500, blank=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return f"Verification for {self.certificate.certificate_number} at {self.created_at}"


class DigitalBadge(TimeStampedModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='digital_badges')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    badge_name = models.CharField(max_length=150)
    badge_type = models.CharField(max_length=50, default='ACADEMIC_ACHIEVEMENT')
    criteria_summary = models.TextField()
    issued_at = models.DateTimeField(auto_now_add=True)
    badge_metadata = models.JSONField(default=dict, blank=True)

    def __str__(self):
        return f"Badge: {self.badge_name} -> {self.student.username}"
