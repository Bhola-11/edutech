from django.db import models
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
