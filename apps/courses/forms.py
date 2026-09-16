from django import forms
from .models import Course, Program, CourseCategory, CourseModule, Lesson, CourseReview

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'department', 'category', 'programs', 'title', 'code',
            'credit_hours', 'lecture_hours', 'lab_hours', 'academic_level',
            'thumbnail', 'summary', 'description', 'prerequisites',
            'syllabus_document', 'status', 'is_featured'
        ]
        widgets = {
            'department': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'programs': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '5'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CS-101'}),
            'credit_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'lecture_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'lab_hours': forms.NumberInput(attrs={'class': 'form-control'}),
            'academic_level': forms.Select(attrs={'class': 'form-select'}),
            'thumbnail': forms.FileInput(attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'prerequisites': forms.SelectMultiple(attrs={'class': 'form-select', 'size': '4'}),
            'syllabus_document': forms.FileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'is_featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CourseModuleForm(forms.ModelForm):
    class Meta:
        model = CourseModule
        fields = ['title', 'order', 'summary', 'estimated_hours']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'estimated_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
        }

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'order', 'content_type', 'duration_minutes', 'is_free_preview', 'body_text', 'video_url', 'resource_file']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'content_type': forms.Select(attrs={'class': 'form-select'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_free_preview': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'body_text': forms.Textarea(attrs={'class': 'form-control', 'rows': 8}),
            'video_url': forms.URLInput(attrs={'class': 'form-control'}),
            'resource_file': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CourseReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ['rating', 'headline', 'comment']
        widgets = {
            'rating': forms.Select(choices=[(i, f'{i} Stars') for i in range(1, 6)], attrs={'class': 'form-select'}),
            'headline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Headline for your review'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Share your experience with this course...'}),
        }
