from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.db.models import Avg, Count, Q
from .models import Course, Program, CourseCategory, CourseModule, Lesson, CourseReview
from .forms import CourseForm, CourseModuleForm, LessonForm, CourseReviewForm
from apps.core.permissions import InstructorRequiredMixin, AcademicStaffRequiredMixin

class CourseListView(ListView):
    model = Course
    template_name = 'courses/course_list.html'
    context_object_name = 'courses'
    paginate_by = 12

    def get_queryset(self):
        qs = Course.objects.select_related('department', 'category').prefetch_related('modules')
        q = self.request.GET.get('q')
        cat = self.request.GET.get('category')
        dept = self.request.GET.get('department')
        level = self.request.GET.get('level')

        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(code__icontains=q) | Q(description__icontains=q))
        if cat:
            qs = qs.filter(category__slug=cat)
        if dept:
            qs = qs.filter(department__slug=dept)
        if level:
            qs = qs.filter(academic_level=level)

        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CourseCategory.objects.all()
        return context

class CourseDetailView(DetailView):
    model = Course
    template_name = 'courses/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.object
        context['modules'] = course.modules.prefetch_related('lessons').all()
        context['reviews'] = course.reviews.select_related('student').filter(is_approved=True)
        context['review_form'] = CourseReviewForm()
        context['is_enrolled'] = False
        if self.request.user.is_authenticated:
            context['is_enrolled'] = self.request.user.enrollments.filter(course=course, status='ACTIVE').exists()
        return context

class CourseCreateView(LoginRequiredMixin, InstructorRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'
    success_url = reverse_lazy('courses:course_list')

    def form_valid(self, form):
        messages.success(self.request, f'Course \"{form.instance.title}\" has been successfully created.')
        return super().form_valid(form)

class CourseUpdateView(LoginRequiredMixin, InstructorRequiredMixin, UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'courses/course_form.html'

    def get_success_url(self):
        return reverse_lazy('courses:course_detail', kwargs={'slug': self.object.slug})

class ProgramListView(ListView):
    model = Program
    template_name = 'courses/program_list.html'
    context_object_name = 'programs'
    paginate_by = 10

    def get_queryset(self):
        return Program.objects.select_related('department__faculty')

class ProgramDetailView(DetailView):
    model = Program
    template_name = 'courses/program_detail.html'
    context_object_name = 'program'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['curriculum_courses'] = self.object.curriculum_courses.select_related('department').all()
        return context

class LessonPlayerView(LoginRequiredMixin, DetailView):
    model = Lesson
    template_name = 'courses/lesson_player.html'
    context_object_name = 'lesson'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lesson = self.object
        course = lesson.module.course
        context['course'] = course
        context['module'] = lesson.module
        context['all_modules'] = course.modules.prefetch_related('lessons').all()
        return context

class SubmitReviewView(LoginRequiredMixin, View):
    def post(self, request, slug, *args, **kwargs):
        course = get_object_or_404(Course, slug=slug)
        form = CourseReviewForm(request.POST)
        if form.is_valid():
            review, created = CourseReview.objects.update_or_create(
                course=course,
                student=request.user,
                defaults={
                    'rating': form.cleaned_data['rating'],
                    'headline': form.cleaned_data['headline'],
                    'comment': form.cleaned_data['comment'],
                    'is_approved': True
                }
            )
            messages.success(request, 'Your review has been successfully submitted.')
        else:
            messages.error(request, 'Error submitting review. Please check your inputs.')
        return redirect('courses:course_detail', slug=slug)
