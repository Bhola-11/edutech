from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import StudentProfile, InstructorProfile, AcademicCredential, SkillRecord
from .forms import StudentProfileForm, InstructorProfileForm, AcademicCredentialForm
from apps.accounts.models import User

class InstructorDirectoryView(ListView):
    model = InstructorProfile
    template_name = 'profiles/faculty_directory.html'
    context_object_name = 'faculty_list'
    paginate_by = 12

    def get_queryset(self):
        return InstructorProfile.objects.select_related('user__department').filter(user__is_active=True)

class FacultyProfileDetailView(DetailView):
    model = InstructorProfile
    template_name = 'profiles/faculty_detail.html'
    context_object_name = 'faculty'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['credentials'] = self.object.user.credentials.all()
        context['skills'] = self.object.user.skills.all()
        return context

class StudentProfileDetailView(LoginRequiredMixin, DetailView):
    model = StudentProfile
    template_name = 'profiles/student_detail.html'
    context_object_name = 'student'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enrollments'] = self.object.user.enrollments.select_related('course', 'semester')
        context['skills'] = self.object.user.skills.all()
        return context
