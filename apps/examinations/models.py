from django.db import models
from apps.core.models import TimeStampedModel, MultiTenantModel
from apps.assessments.models import Assessment, Question, QuestionOption
from apps.accounts.models import User
from apps.enrollments.models import Batch


class ExamSession(TimeStampedModel, MultiTenantModel):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('IN_PROGRESS', 'Active & In Progress'),
        ('COMPLETED', 'Session Concluded'),
        ('CANCELLED', 'Session Cancelled')
    ]

    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='exam_sessions')
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name='exam_sessions', null=True, blank=True)
    proctors = models.ManyToManyField(User, blank=True, related_name='proctored_sessions')
    session_code = models.CharField(max_length=50, unique=True)
    start_window = models.DateTimeField()
    end_window = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')
    requires_webcam = models.BooleanField(default=True)
    requires_screen_share = models.BooleanField(default=False)
    max_tab_switches = models.PositiveIntegerField(default=3)

    def __str__(self):
        return f"Session {self.session_code} - {self.assessment.title}"


class ExamAttempt(TimeStampedModel):
    STATUS_CHOICES = [
        ('STARTED', 'Attempt Initialized'),
        ('IN_PROGRESS', 'Taking Exam'),
        ('SUBMITTED', 'Submitted by Student'),
        ('AUTO_SUBMITTED', 'Auto-Submitted upon Time Expiry'),
        ('DISQUALIFIED', 'Disqualified by Proctor / Anti-Cheat'),
        ('GRADED', 'Grading Finalized')
    ]

    session = models.ForeignKey(ExamSession, on_delete=models.CASCADE, related_name='attempts')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_attempts')
    attempt_number = models.PositiveIntegerField(default=1)
    started_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='STARTED')
    score_obtained = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    percentage_obtained = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    is_passed = models.BooleanField(default=False)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=500, blank=True)
    device_fingerprint = models.CharField(max_length=255, blank=True)

    class Meta:
        unique_together = ('session', 'student', 'attempt_number')

    def __str__(self):
        return f"{self.student.username} - {self.session.assessment.title} (Attempt #{self.attempt_number})"


class StudentAnswer(TimeStampedModel):
    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name='answers')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(QuestionOption, on_delete=models.SET_NULL, null=True, blank=True)
    selected_options_json = models.JSONField(default=list, blank=True)  # for multi-select
    text_response = models.TextField(blank=True)
    code_response = models.TextField(blank=True)
    points_awarded = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    is_correct = models.BooleanField(default=False)
    evaluator_feedback = models.TextField(blank=True)
    evaluated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='graded_answers')
    evaluated_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('attempt', 'question')

    def __str__(self):
        return f"Answer by {self.attempt.student.username} for {self.question.title[:30]}"


class ProctoringEvent(TimeStampedModel):
    EVENT_TYPES = [
        ('TAB_SWITCH', 'Focus Lost / Switched Browser Tab'),
        ('FULLSCREEN_EXIT', 'Exited Fullscreen Mode'),
        ('FACE_LOST', 'Webcam: No Face Detected'),
        ('MULTIPLE_FACES', 'Webcam: Multiple Faces Detected'),
        ('SUSPICIOUS_AUDIO', 'Audio Threshold Exceeded'),
        ('COPY_PASTE_ATTEMPT', 'Clipboard Copy/Paste Attempted'),
        ('DEVTOOLS_OPENED', 'Browser Developer Tools Detected'),
        ('IP_ANOMALY', 'IP Address Changed Mid-Session')
    ]

    SEVERITY_LEVELS = [
        ('LOW', 'Low Advisory'),
        ('MEDIUM', 'Moderate Warning'),
        ('HIGH', 'Severe Incident'),
        ('CRITICAL', 'Automatic Disqualification Trigger')
    ]

    attempt = models.ForeignKey(ExamAttempt, on_delete=models.CASCADE, related_name='proctoring_events')
    event_type = models.CharField(max_length=40, choices=EVENT_TYPES)
    severity = models.CharField(max_length=20, choices=SEVERITY_LEVELS, default='MEDIUM')
    captured_at = models.DateTimeField(auto_now_add=True)
    payload_data = models.JSONField(default=dict, blank=True)
    snapshot_url = models.URLField(blank=True)
    is_reviewed = models.BooleanField(default=False)
    reviewer_notes = models.TextField(blank=True)

    def __str__(self):
        return f"[{self.severity}] {self.get_event_type_display()} - Attempt #{self.attempt.id}"


class ExamAccommodation(TimeStampedModel):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='exam_accommodations')
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='accommodations')
    extra_time_minutes = models.PositiveIntegerField(default=30)
    separate_testing_room = models.BooleanField(default=False)
    special_notes = models.TextField(blank=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='approved_accommodations')

    class Meta:
        unique_together = ('student', 'assessment')

    def __str__(self):
        return f"Accommodation for {self.student.username} on {self.assessment.title} (+{self.extra_time_minutes}m)"
