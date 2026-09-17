from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .models import IssuedCertificate, DigitalBadge, CertificateVerificationLog
from .services.pdf_certificate_service import PDFCertificateGeneratorService
from .services.crypto_verification_service import CertificateCryptoService


@login_required
def certificate_list(request):
    certificates = IssuedCertificate.objects.filter(student=request.user, is_revoked=False).select_related('course', 'template')
    badges = DigitalBadge.objects.filter(student=request.user)
    return render(request, 'certificates/certificate_list.html', {'certificates': certificates, 'badges': badges})


def verify_certificate_public(request, certificate_number=None):
    cert = None
    is_valid = False
    query = certificate_number or request.GET.get('code', '').strip()

    if query:
        cert = IssuedCertificate.objects.filter(certificate_number=query, is_revoked=False).select_related('student', 'course', 'institution').first()
        if cert:
            is_valid = CertificateCryptoService.verify_hash(
                student_id=cert.student.id,
                course_code=cert.course.code if cert.course else 'GENERAL',
                certificate_number=cert.certificate_number,
                issue_date_str=str(cert.issue_date),
                provided_hash=cert.verification_hash
            )
            # Log verification lookup
            CertificateVerificationLog.objects.create(
                certificate=cert,
                verifier_ip=request.META.get('REMOTE_ADDR'),
                verifier_user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
                is_valid=is_valid
            )

    return render(request, 'certificates/verify_certificate.html', {'cert': cert, 'is_valid': is_valid, 'query': query})


@login_required
def download_certificate_pdf(request, certificate_id):
    cert = get_object_or_404(IssuedCertificate, certificate_id=certificate_id, is_revoked=False)
    pdf_bytes = PDFCertificateGeneratorService.generate_certificate_pdf(
        student_name=cert.student.get_full_name() or cert.student.username,
        course_title=cert.course.title if cert.course else 'Comprehensive Program',
        course_code=cert.course.code if cert.course else 'PROG-100',
        institution_name=cert.institution.name,
        certificate_number=cert.certificate_number,
        issue_date_str=cert.issue_date.strftime('%B %d, %Y'),
        honors_title=cert.honors_title,
        issuer_name=cert.template.issuer_name if cert.template else 'Dean of Academic Affairs',
        issuer_title=cert.template.issuer_title if cert.template else 'Office of the Registrar'
    )
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Certificate-{cert.certificate_number}.pdf"'
    return response
