"""
ReportLab Dynamic PDF Certificate Generator Service.
Generates institutional certificates with ornamental borders, seal, and metadata.
"""
import io
from typing import Dict, Any
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


class PDFCertificateGeneratorService:
    @classmethod
    def generate_certificate_pdf(
        cls,
        student_name: str,
        course_title: str,
        course_code: str,
        institution_name: str,
        certificate_number: str,
        issue_date_str: str,
        honors_title: str = '',
        issuer_name: str = 'Dr. Provost Administrator',
        issuer_title: str = 'Dean of Academic Affairs'
    ) -> bytes:
        """Generates binary PDF certificate using ReportLab landscape layout."""
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=landscape(letter))
        width, height = landscape(letter)

        # Outer border
        c.setStrokeColor(colors.HexColor('#1E3A8A'))  # Deep Navy
        c.setLineWidth(5)
        c.rect(20, 20, width - 40, height - 40)

        # Inner gold border
        c.setStrokeColor(colors.HexColor('#D97706'))  # Gold
        c.setLineWidth(2)
        c.rect(26, 26, width - 52, height - 52)

        # Header: Institution Name
        c.setFillColor(colors.HexColor('#1E3A8A'))
        c.setFont('Helvetica-Bold', 24)
        c.drawCentredString(width / 2.0, height - 70, institution_name.upper())

        # Subtitle
        c.setFillColor(colors.HexColor('#4B5563'))
        c.setFont('Helvetica', 14)
        c.drawCentredString(width / 2.0, height - 95, "OFFICIAL CERTIFICATE OF ACADEMIC ACHIEVEMENT")

        # Statement
        c.setFont('Helvetica-Oblique', 12)
        c.drawCentredString(width / 2.0, height - 135, "This is to officially certify that")

        # Recipient Name
        c.setFillColor(colors.HexColor('#111827'))
        c.setFont('Helvetica-Bold', 26)
        c.drawCentredString(width / 2.0, height - 170, student_name)

        # Completion text
        c.setFillColor(colors.HexColor('#4B5563'))
        c.setFont('Helvetica', 12)
        c.drawCentredString(width / 2.0, height - 205, f"has successfully completed all curricular requirements for the accredited course")

        # Course Title
        c.setFillColor(colors.HexColor('#1E3A8A'))
        c.setFont('Helvetica-Bold', 18)
        c.drawCentredString(width / 2.0, height - 235, f"{course_code}: {course_title}")

        if honors_title:
            c.setFillColor(colors.HexColor('#D97706'))
            c.setFont('Helvetica-Bold', 14)
            c.drawCentredString(width / 2.0, height - 260, f"Awarded with Academic Distinction: {honors_title}")

        # Signatures
        c.setStrokeColor(colors.HexColor('#9CA3AF'))
        c.setLineWidth(1)
        c.line(100, 100, 300, 100)
        c.line(width - 300, 100, width - 100, 100)

        c.setFillColor(colors.HexColor('#111827'))
        c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(200, 85, issuer_name)
        c.drawCentredString(width - 200, 85, "Verification Registry")

        c.setFillColor(colors.HexColor('#6B7280'))
        c.setFont('Helvetica', 9)
        c.drawCentredString(200, 70, issuer_title)
        c.drawCentredString(width - 200, 70, f"Certificate ID: {certificate_number}")
        c.drawCentredString(width / 2.0, 45, f"Issued on {issue_date_str} | Digitally Verified via EduTech Trust Network")

        c.showPage()
        c.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        return pdf_data
