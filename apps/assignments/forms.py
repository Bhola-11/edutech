from django import forms
from .models import Assignment, AssignmentSubmission


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['course', 'title', 'instructions_html', 'total_points', 'weight_percentage', 'submission_type', 'allowed_extensions', 'max_file_size_mb', 'due_date', 'late_deadline', 'late_penalty_per_day', 'peer_review_enabled', 'is_published']
        widgets = {
            'instructions_html': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'submission_type': forms.Select(attrs={'class': 'form-select'}),
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'late_deadline': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }


class SubmissionForm(forms.ModelForm):
    file_upload = forms.FileField(required=False, widget=forms.FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = AssignmentSubmission
        fields = ['text_content', 'external_url']
        widgets = {
            'text_content': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'external_url': forms.URLInput(attrs={'class': 'form-control'}),
        }
