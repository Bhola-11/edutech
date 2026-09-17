"""
Enterprise Phase 2 Generator: Builds Assessments, Examinations, Assignments, Grading, and Certificates apps.
"""
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

APPS = {
    'assessments': {
        'models': '''from django.db import models
from django.utils.text import slugify
from apps.core.models import TimeStampedModel, MultiTenantModel
from apps.institutions.models import Institution
from apps.courses.models import Course
from apps.accounts.models import User


class QuestionCategory(TimeStampedModel, MultiTenantModel):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=180, blank=True)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Question Categories'
        unique_together = ('institution', 'code')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.institution.code}-{self.code}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.code} - {self.name}"


class QuestionTag(TimeStampedModel):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AssessmentRubric(TimeStampedModel, MultiTenantModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='rubrics', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    max_total_score = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)

    def __str__(self):
        return f"{self.title} (Max: {self.max_total_score})"


class RubricCriterion(TimeStampedModel):
    rubric = models.ForeignKey(AssessmentRubric, on_delete=models.CASCADE, related_name='criteria')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    weight_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=25.00)
    max_points = models.DecimalField(max_digits=6, decimal_places=2, default=25.00)
    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.rubric.title} - {self.title} ({self.weight_percentage}%)"


class RubricLevel(TimeStampedModel):
    criterion = models.ForeignKey(RubricCriterion, on_delete=models.CASCADE, related_name='levels')
    level_name = models.CharField(max_length=100)  # Exemplary, Proficient, Developing, Unsatisfactory
    point_value = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['-point_value']

    def __str__(self):
        return f"{self.level_name} ({self.point_value} pts)"


class Question(TimeStampedModel, MultiTenantModel):
    QUESTION_TYPES = [
        ('MCQ_SINGLE', 'Multiple Choice (Single Answer)'),
        ('MCQ_MULTIPLE', 'Multiple Choice (Multiple Answers)'),
        ('TRUE_FALSE', 'True / False'),
        ('SHORT_ANSWER', 'Short Answer'),
        ('ESSAY', 'Essay / Long Response'),
        ('FILL_BLANK', 'Fill in the Blanks'),
        ('MATCHING', 'Matching Pairs'),
        ('NUMERICAL', 'Numerical Calculation'),
        ('CODE_CHALLENGE', 'Coding Challenge / Sandbox')
    ]

    DIFFICULTY_LEVELS = [
        ('EASY', 'Easy (Introductory)'),
        ('MEDIUM', 'Medium (Standard)'),
        ('HARD', 'Hard (Advanced)'),
        ('EXPERT', 'Expert (Mastery / Research)')
    ]

    BLOOMS_LEVELS = [
        ('REMEMBERING', 'Remembering'),
        ('UNDERSTANDING', 'Understanding'),
        ('APPLYING', 'Applying'),
        ('ANALYZING', 'Analyzing'),
        ('EVALUATING', 'Evaluating'),
        ('CREATING', 'Creating')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    category = models.ForeignKey(QuestionCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name='questions')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='created_questions')
    title = models.CharField(max_length=255)
    question_type = models.CharField(max_length=30, choices=QUESTION_TYPES, default='MCQ_SINGLE')
    prompt_html = models.TextField()
    explanation_html = models.TextField(blank=True)
    default_points = models.DecimalField(max_digits=6, decimal_places=2, default=1.00)
    negative_points = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_LEVELS, default='MEDIUM')
    blooms_level = models.CharField(max_length=20, choices=BLOOMS_LEVELS, default='APPLYING')
    tags = models.ManyToManyField(QuestionTag, blank=True, related_name='questions')
    rubric = models.ForeignKey(AssessmentRubric, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"[{self.course.code}] {self.title} ({self.get_question_type_display()})"


class QuestionOption(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=500)
    option_html = models.TextField(blank=True)
    is_correct = models.BooleanField(default=False)
    explanation = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.question.title} - Option: {self.option_text[:40]}"


class CodeChallengeSpec(TimeStampedModel):
    LANGUAGES = [
        ('PYTHON', 'Python 3.11'),
        ('JAVASCRIPT', 'JavaScript (Node.js)'),
        ('SQL', 'PostgreSQL / SQLite SQL'),
        ('CPP', 'C++ 20'),
        ('JAVA', 'Java 17 OpenJDK')
    ]

    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='code_spec')
    language = models.CharField(max_length=30, choices=LANGUAGES, default='PYTHON')
    starter_code = models.TextField(blank=True)
    solution_code = models.TextField()
    time_limit_ms = models.PositiveIntegerField(default=2000)
    memory_limit_mb = models.PositiveIntegerField(default=128)

    def __str__(self):
        return f"CodeSpec for {self.question.title} ({self.language})"


class CodeTestCase(TimeStampedModel):
    code_spec = models.ForeignKey(CodeChallengeSpec, on_delete=models.CASCADE, related_name='test_cases')
    input_data = models.TextField(blank=True)
    expected_output = models.TextField()
    is_hidden = models.BooleanField(default=False)  # Hidden from student during exam
    points = models.DecimalField(max_digits=5, decimal_places=2, default=5.00)
    display_order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"TestCase #{self.display_order} ({'Hidden' if self.is_hidden else 'Public'})"


class Assessment(TimeStampedModel, MultiTenantModel):
    ASSESSMENT_TYPES = [
        ('QUIZ', 'Module Quiz / Knowledge Check'),
        ('MIDTERM', 'Midterm Examination'),
        ('FINAL_EXAM', 'Comprehensive Final Examination'),
        ('PRACTICE_TEST', 'Diagnostic Practice Assessment'),
        ('LAB_EXAM', 'Laboratory Practical Exam')
    ]

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=280, blank=True)
    assessment_type = models.CharField(max_length=30, choices=ASSESSMENT_TYPES, default='QUIZ')
    duration_minutes = models.PositiveIntegerField(default=60)
    total_points = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    passing_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    instructions_html = models.TextField(blank=True)
    shuffle_questions = models.BooleanField(default=True)
    shuffle_options = models.BooleanField(default=True)
    allow_review = models.BooleanField(default=True)
    max_attempts = models.PositiveIntegerField(default=1)
    is_proctored = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.course.code}-{self.title}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.course.code}: {self.title} ({self.get_assessment_type_display()})"


class AssessmentSection(TimeStampedModel):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    display_order = models.PositiveIntegerField(default=1)
    time_limit_minutes = models.PositiveIntegerField(null=True, blank=True)
    section_points = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)

    class Meta:
        ordering = ['display_order']

    def __str__(self):
        return f"{self.assessment.title} - Section: {self.title}"


class AssessmentQuestion(TimeStampedModel):
    section = models.ForeignKey(AssessmentSection, on_delete=models.CASCADE, related_name='section_questions')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='assessment_links')
    display_order = models.PositiveIntegerField(default=1)
    points_override = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['display_order']
        unique_together = ('section', 'question')

    def __str__(self):
        return f"{self.section.title} -> {self.question.title}"
''',
    },

    'examinations': {
        'models': '''from django.db import models
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
''',
    },

    'assignments': {
        'models': '''from django.db import models
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
''',
    },

    'grading': {
        'models': '''from django.db import models
from apps.core.models import TimeStampedModel, MultiTenantModel
from apps.courses.models import Course
from apps.enrollments.models import StudentEnrollment
from apps.accounts.models import User


class GradingScale(TimeStampedModel, MultiTenantModel):
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.institution.code})"


class ScaleGradeLevel(TimeStampedModel):
    grading_scale = models.ForeignKey(GradingScale, on_delete=models.CASCADE, related_name='levels')
    letter_grade = models.CharField(max_length=10)
    min_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    max_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    grade_points = models.DecimalField(max_digits=4, decimal_places=2)  # 4.00, 3.70, etc.
    description = models.CharField(max_length=100, blank=True)

    class Meta:
        ordering = ['-min_percentage']

    def __str__(self):
        return f"{self.letter_grade} ({self.min_percentage}% - {self.max_percentage}%, GPA: {self.grade_points})"


class GradeCategory(TimeStampedModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='grade_categories')
    name = models.CharField(max_length=100)  # e.g., Homework, Midterm, Final, Labs
    weight_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    drop_lowest_scores = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Grade Categories'

    def __str__(self):
        return f"{self.course.code} - {self.name} ({self.weight_percentage}%)"


class GradeItem(TimeStampedModel):
    category = models.ForeignKey(GradeCategory, on_delete=models.CASCADE, related_name='items')
    title = models.CharField(max_length=200)
    max_points = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    is_extra_credit = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.category.name}: {self.title} (Max: {self.max_points})"


class StudentGrade(TimeStampedModel):
    item = models.ForeignKey(GradeItem, on_delete=models.CASCADE, related_name='grades')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='grade_records')
    points_earned = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    is_dropped = models.BooleanField(default=False)
    is_excused = models.BooleanField(default=False)
    feedback = models.TextField(blank=True)
    graded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        unique_together = ('item', 'student')

    def __str__(self):
        return f"{self.student.username} - {self.item.title}: {self.points_earned}/{self.item.max_points}"


class FinalCourseGrade(TimeStampedModel):
    enrollment = models.OneToOneField(StudentEnrollment, on_delete=models.CASCADE, related_name='final_grade')
    total_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    letter_grade = models.CharField(max_length=10, default='F')
    grade_points = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)
    is_curved = models.BooleanField(default=False)
    curve_offset_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    is_finalized = models.BooleanField(default=False)
    finalized_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    finalized_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.enrollment.student.username} - {self.enrollment.course.code}: {self.letter_grade} ({self.total_percentage}%)"


class GradeOverrideLog(TimeStampedModel):
    final_grade = models.ForeignKey(FinalCourseGrade, on_delete=models.CASCADE, related_name='override_logs')
    original_letter = models.CharField(max_length=10)
    new_letter = models.CharField(max_length=10)
    original_points = models.DecimalField(max_digits=4, decimal_places=2)
    new_points = models.DecimalField(max_digits=4, decimal_places=2)
    reason = models.TextField()
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='approved_grade_overrides')

    def __str__(self):
        return f"Override {self.original_letter}->{self.new_letter} for {self.final_grade.enrollment.student.username}"
''',
    },

    'certificates': {
        'models': '''import uuid
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
''',
    }
}


def build_app(app_name, config):
    app_dir = os.path.join(BASE_DIR, 'apps', app_name)
    os.makedirs(app_dir, exist_ok=True)

    # __init__.py
    with open(os.path.join(app_dir, '__init__.py'), 'w', encoding='utf-8') as f:
        f.write(f'"""{app_name.capitalize()} application package."""\n')

    # apps.py
    with open(os.path.join(app_dir, 'apps.py'), 'w', encoding='utf-8') as f:
        f.write(f'''from django.apps import AppConfig


class {app_name.capitalize()}Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.{app_name}'
''')

    # models.py
    with open(os.path.join(app_dir, 'models.py'), 'w', encoding='utf-8') as f:
        f.write(config['models'].strip() + '\n')

    # admin.py
    with open(os.path.join(app_dir, 'admin.py'), 'w', encoding='utf-8') as f:
        f.write(f'''from django.contrib import admin
from . import models

# Register all models in app
for name, cls in models.__dict__.items():
    if isinstance(cls, type) and issubclass(cls, models.models.Model) and not cls._meta.abstract:
        try:
            admin.site.register(cls)
        except admin.sites.AlreadyRegistered:
            pass
''')

    # urls.py
    with open(os.path.join(app_dir, 'urls.py'), 'w', encoding='utf-8') as f:
        f.write(f'''from django.urls import path
from . import views

app_name = '{app_name}'

urlpatterns = [
    path('', views.index, name='index'),
]
''')

    # views.py
    with open(os.path.join(app_dir, 'views.py'), 'w', encoding='utf-8') as f:
        f.write(f'''from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse


@login_required
def index(request):
    return render(request, '{app_name}/index.html', {{'title': '{app_name.capitalize()}'}})
''')

    # api_views.py
    with open(os.path.join(app_dir, 'api_views.py'), 'w', encoding='utf-8') as f:
        f.write(f'''from rest_framework import viewsets, permissions


class Base{app_name.capitalize()}ViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
''')

    # api_urls.py
    with open(os.path.join(app_dir, 'api_urls.py'), 'w', encoding='utf-8') as f:
        f.write(f'''from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
]
''')

    print(f"Created app: apps.{app_name}")


def main():
    for app_name, config in APPS.items():
        build_app(app_name, config)
    print("All Phase 2 app scaffolds generated successfully.")


if __name__ == '__main__':
    main()
