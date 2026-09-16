from django import forms
from .models import StudentProfile, InstructorProfile, AcademicCredential, SkillRecord

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['roll_number', 'registration_number', 'program', 'current_semester', 'blood_group', 'emergency_contact_name', 'emergency_contact_phone']
        widgets = {
            'roll_number': forms.TextInput(attrs={'class': 'form-control'}),
            'registration_number': forms.TextInput(attrs={'class': 'form-control'}),
            'program': forms.Select(attrs={'class': 'form-select'}),
            'current_semester': forms.Select(attrs={'class': 'form-select'}),
            'blood_group': forms.Select(attrs={'class': 'form-select'}),
            'emergency_contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emergency_contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
        }

class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = InstructorProfile
        fields = ['employee_id', 'designation', 'office_room', 'office_hours', 'research_interests', 'google_scholar_url']
        widgets = {
            'employee_id': forms.TextInput(attrs={'class': 'form-control'}),
            'designation': forms.Select(attrs={'class': 'form-select'}),
            'office_room': forms.TextInput(attrs={'class': 'form-control'}),
            'office_hours': forms.TextInput(attrs={'class': 'form-control'}),
            'research_interests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'google_scholar_url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class AcademicCredentialForm(forms.ModelForm):
    class Meta:
        model = AcademicCredential
        fields = ['degree_name', 'institution_name', 'graduation_year', 'score_or_grade', 'document_proof']
        widgets = {
            'degree_name': forms.TextInput(attrs={'class': 'form-control'}),
            'institution_name': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'score_or_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'document_proof': forms.FileInput(attrs={'class': 'form-control'}),
        }
