from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, MultiTenantModel
from apps.courses.models import Course
from apps.assessments.models import AssessmentRubric
from apps.accounts.models import User


class Assignment(TimeStampedModel, MultiTenantModel):
    SUBMISSION_TYPES = [
        ('FILE_UPLOAD', 'File Attachment Upload (PDF, ZIP, DOCX)'),
        ('TEXT_ENTRY', 'Rich Text Form Submission'),
        ('URL_LINK', 'Live URL / Git Repository Link'),
        ('CODE_ARCHIVE', 'Source Code Archive with Manifest')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, blank=True)
    instructions_html = models.TextField()
    total_points = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    weight_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    submission_type = models.CharField(max_length=30, choices=SUBMISSION_TYPES, default='FILE_UPLOAD')
    allowed_extensions = models.CharField(max_length=200, default='pdf,zip,docx,py,ipynb')
    max_file_size_mb = models.PositiveIntegerField(default=25)
    due_date = models.DateTimeField()
    late_deadline = models.DateTimeField(null=True, blank=True)
    late_penalty_per_day = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)
    rubric = models.ForeignKey(AssessmentRubric, on_delete=models.SET_NULL, null=True, blank=True)
    peer_review_enabled = models.BooleanField(default=False)
    peer_reviews_required = models.PositiveIntegerField(default=2)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.course.code}-{self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.code}: {self.title}"


class AssignmentSubmission(TimeStampedModel):
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted on Time'),
        ('LATE_SUBMITTED', 'Submitted Late'),
        ('UNDER_REVIEW', 'Under Faculty / TA Review'),
        ('GRADED', 'Graded & Feedback Available'),
        ('RESUBMIT_REQUESTED', 'Revision Requested')
    ]

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignment_submissions')
    submission_number = models.PositiveIntegerField(default=1)
    text_content = models.TextField(blank=True)
    external_url = models.URLField(blank=True)
    is_late = models.BooleanField(default=False)
    late_days = models.PositiveIntegerField(default=0)
    raw_score = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    late_penalty_applied = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    final_score = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='SUBMITTED')
    faculty_feedback = models.TextField(blank=True)
    graded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='graded_submissions')
    graded_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('assignment', 'student', 'submission_number')

    def __str__(self):
        return f"{self.student.username} - {self.assignment.title} (Sub #{self.submission_number})"


class SubmissionAttachment(TimeStampedModel):
    submission = models.ForeignKey(AssignmentSubmission, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='submissions/%Y/%m/')
    file_name = models.CharField(max_length=255)
    file_size_bytes = models.BigIntegerField(default=0)
    mime_type = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.file_name


class PlagiarismReport(TimeStampedModel):
    submission = models.OneToOneField(AssignmentSubmission, on_delete=models.CASCADE, related_name='plagiarism_report')
    similarity_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    matched_sources = models.JSONField(default=list, blank=True)
    report_summary = models.TextField(blank=True)
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"Similarity {self.similarity_percentage}% on Sub #{self.submission.id}"


class PeerReviewAssignment(TimeStampedModel):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Peer Review'),
        ('COMPLETED', 'Review Completed'),
        ('EXPIRED', 'Review Window Expired')
    ]

    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='peer_reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_peer_reviews')
    submission = models.ForeignKey(AssignmentSubmission, on_delete=models.CASCADE, related_name='peer_reviews')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    score_awarded = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    feedback_strengths = models.TextField(blank=True)
    feedback_improvements = models.TextField(blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('reviewer', 'submission')

    def __str__(self):
        return f"PeerReview by {self.reviewer.username} for Sub #{self.submission.id}"
