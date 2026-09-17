from django import forms
from .models import Assessment, Question, AssessmentRubric, QuestionCategory


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['course', 'title', 'assessment_type', 'duration_minutes', 'total_points', 'passing_percentage', 'instructions_html', 'shuffle_questions', 'shuffle_options', 'is_proctored', 'is_published']
        widgets = {
            'instructions_html': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'assessment_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'passing_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['course', 'category', 'title', 'question_type', 'prompt_html', 'explanation_html', 'default_points', 'negative_points', 'difficulty', 'blooms_level', 'is_active']
        widgets = {
            'prompt_html': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'explanation_html': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'question_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
            'blooms_level': forms.Select(attrs={'class': 'form-select'}),
            'default_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'negative_points': forms.NumberInput(attrs={'class': 'form-control'}),
        }
