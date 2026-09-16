from django import forms
from .models import AdmissionApplication, StudentEnrollment, Batch

class AdmissionApplicationForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ['cycle', 'statement_of_purpose', 'prior_institution', 'prior_gpa']
        widgets = {
            'cycle': forms.Select(attrs={'class': 'form-select'}),
            'statement_of_purpose': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your academic background, objectives, and why you are applying to this program...'}),
            'prior_institution': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Springfield High School / Boston University'}),
            'prior_gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'placeholder': '3.85'}),
        }

class ApplicationReviewForm(forms.ModelForm):
    class Meta:
        model = AdmissionApplication
        fields = ['status', 'review_notes']
        widgets = {
            'status': forms.Select(attrs={'class': 'form-select'}),
            'review_notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Committee review notes and decision rationale...'}),
        }

class CourseEnrollmentForm(forms.ModelForm):
    class Meta:
        model = StudentEnrollment
        fields = ['course', 'semester', 'batch']
        widgets = {
            'course': forms.Select(attrs={'class': 'form-select'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'batch': forms.Select(attrs={'class': 'form-select'}),
        }
