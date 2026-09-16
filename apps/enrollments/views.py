from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from .models import AdmissionCycle, AdmissionApplication, StudentEnrollment, Batch, CourseProgress
from .forms import AdmissionApplicationForm, ApplicationReviewForm, CourseEnrollmentForm
from apps.courses.models import Course
from apps.institutions.models import Semester
from apps.core.permissions import AcademicStaffRequiredMixin

class AdmissionCycleListView(ListView):
    model = AdmissionCycle
    template_name = 'enrollments/cycle_list.html'
    context_object_name = 'cycles'

    def get_queryset(self):
        return AdmissionCycle.objects.filter(is_open=True).select_related('program', 'session')

class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = AdmissionApplication
    form_class = AdmissionApplicationForm
    template_name = 'enrollments/apply_form.html'
    success_url = reverse_lazy('enrollments:my_applications')

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        messages.success(self.request, 'Your admission application has been submitted successfully!')
        return super().form_valid(form)

class MyApplicationListView(LoginRequiredMixin, ListView):
    model = AdmissionApplication
    template_name = 'enrollments/my_applications.html'
    context_object_name = 'applications'

    def get_queryset(self):
        return AdmissionApplication.objects.filter(applicant=self.request.user).select_related('cycle__program')

class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = AdmissionApplication
    template_name = 'enrollments/application_detail.html'
    context_object_name = 'application'

class ApplicationReviewView(LoginRequiredMixin, AcademicStaffRequiredMixin, UpdateView):
    model = AdmissionApplication
    form_class = ApplicationReviewForm
    template_name = 'enrollments/review_form.html'

    def form_valid(self, form):
        form.instance.reviewer = self.request.user
        form.instance.reviewed_at = timezone.now()
        messages.success(self.request, 'Application review decision recorded.')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('enrollments:application_detail', kwargs={'pk': self.object.pk})

class QuickEnrollView(LoginRequiredMixin, View):
    def post(self, request, course_slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=course_slug)
        current_semester = Semester.objects.filter(is_current=True).first()
        if not current_semester:
            current_semester = Semester.objects.order_by('-created_at').first()

        if not current_semester:
            messages.error(request, 'No active semester available for registration.')
            return redirect('courses:course_detail', slug=course_slug)

        enrollment, created = StudentEnrollment.objects.get_or_create(
            student=request.user,
            course=course,
            semester=current_semester,
            defaults={'status': 'ACTIVE'}
        )

        CourseProgress.objects.get_or_create(
            student=request.user,
            course=course,
            defaults={'completion_percentage': 0.0}
        )

        if created:
            messages.success(request, f'You have successfully enrolled in {course.title}!')
        else:
            messages.info(request, f'You are already enrolled in {course.title}.')

        return redirect('courses:course_detail', slug=course_slug)

class MyEnrollmentsListView(LoginRequiredMixin, ListView):
    model = StudentEnrollment
    template_name = 'enrollments/my_enrollments.html'
    context_object_name = 'enrollments'

    def get_queryset(self):
        return StudentEnrollment.objects.filter(student=self.request.user).select_related('course', 'semester')
