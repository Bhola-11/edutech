from django import forms
from .models import Institution, Campus, Faculty, AcademicDepartment, AcademicSession, Semester, Classroom

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = [
            'name', 'code', 'logo', 'motto', 'established_year', 'website',
            'contact_email', 'contact_phone', 'address_line_1', 'address_line_2',
            'city', 'state_province', 'postal_code', 'country', 'accreditation_body',
            'accreditation_grade', 'timezone', 'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HARVARD'}),
            'logo': forms.FileInput(attrs={'class': 'form-control'}),
            'motto': forms.TextInput(attrs={'class': 'form-control'}),
            'established_year': forms.NumberInput(attrs={'class': 'form-control'}),
            'website': forms.URLInput(attrs={'class': 'form-control'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_1': forms.TextInput(attrs={'class': 'form-control'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state_province': forms.TextInput(attrs={'class': 'form-control'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'accreditation_body': forms.TextInput(attrs={'class': 'form-control'}),
            'accreditation_grade': forms.TextInput(attrs={'class': 'form-control'}),
            'timezone': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['institution', 'name', 'code', 'campus_type', 'director', 'contact_email', 'contact_phone', 'address', 'city', 'state', 'country', 'capacity', 'status']
        widgets = {
            'institution': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'campus_type': forms.Select(attrs={'class': 'form-select'}),
            'director': forms.Select(attrs={'class': 'form-select'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact_phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class AcademicDepartmentForm(forms.ModelForm):
    class Meta:
        model = AcademicDepartment
        fields = ['faculty', 'campus', 'name', 'code', 'head_of_department', 'contact_email', 'office_location']
        widgets = {
            'faculty': forms.Select(attrs={'class': 'form-select'}),
            'campus': forms.Select(attrs={'class': 'form-select'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
            'head_of_department': forms.Select(attrs={'class': 'form-select'}),
            'contact_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'office_location': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ClassroomForm(forms.ModelForm):
    class Meta:
        model = Classroom
        fields = ['campus', 'building', 'room_number', 'room_type', 'seating_capacity', 'has_projector', 'has_computers', 'has_audio_system', 'is_accessible', 'is_active']
        widgets = {
            'campus': forms.Select(attrs={'class': 'form-select'}),
            'building': forms.TextInput(attrs={'class': 'form-control'}),
            'room_number': forms.TextInput(attrs={'class': 'form-control'}),
            'room_type': forms.Select(attrs={'class': 'form-select'}),
            'seating_capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'has_projector': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_computers': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'has_audio_system': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_accessible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
