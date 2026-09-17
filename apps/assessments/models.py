from django.db import models
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
