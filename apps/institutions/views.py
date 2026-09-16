from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Institution, Campus, Faculty, AcademicDepartment, Classroom
from .forms import InstitutionForm, CampusForm, AcademicDepartmentForm, ClassroomForm
from apps.core.permissions import SuperAdminRequiredMixin, InstitutionAdminRequiredMixin

class InstitutionListView(LoginRequiredMixin, ListView):
    model = Institution
    template_name = 'institutions/institution_list.html'
    context_object_name = 'institutions'
    paginate_by = 12

    def get_queryset(self):
        qs = Institution.objects.all()
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(name__icontains=q) | qs.filter(code__icontains=q) | qs.filter(city__icontains=q)
        return qs

class InstitutionDetailView(LoginRequiredMixin, DetailView):
    model = Institution
    template_name = 'institutions/institution_detail.html'
    context_object_name = 'institution'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campuses'] = self.object.campuses.all()
        context['faculties'] = self.object.faculties.prefetch_related('departments').all()
        context['sessions'] = self.object.academic_sessions.prefetch_related('semesters').all()
        return context

class InstitutionCreateView(LoginRequiredMixin, SuperAdminRequiredMixin, CreateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'institutions/institution_form.html'
    success_url = reverse_lazy('institutions:institution_list')

    def form_valid(self, form):
        messages.success(self.request, f'Institution \"{form.instance.name}\" created successfully.')
        return super().form_valid(form)

class InstitutionUpdateView(LoginRequiredMixin, InstitutionAdminRequiredMixin, UpdateView):
    model = Institution
    form_class = InstitutionForm
    template_name = 'institutions/institution_form.html'

    def get_success_url(self):
        return reverse_lazy('institutions:institution_detail', kwargs={'slug': self.object.slug})

class CampusListView(LoginRequiredMixin, ListView):
    model = Campus
    template_name = 'institutions/campus_list.html'
    context_object_name = 'campuses'
    paginate_by = 15

    def get_queryset(self):
        qs = Campus.objects.select_related('institution', 'director')
        inst_id = self.request.GET.get('institution')
        if inst_id:
            qs = qs.filter(institution_id=inst_id)
        return qs

class CampusDetailView(LoginRequiredMixin, DetailView):
    model = Campus
    template_name = 'institutions/campus_detail.html'
    context_object_name = 'campus'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classrooms'] = self.object.classrooms.all()
        context['departments'] = self.object.departments.all()
        return context

class DepartmentListView(LoginRequiredMixin, ListView):
    model = AcademicDepartment
    template_name = 'institutions/department_list.html'
    context_object_name = 'departments'
    paginate_by = 20

    def get_queryset(self):
        return AcademicDepartment.objects.select_related('faculty__institution', 'campus', 'head_of_department')

class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = AcademicDepartment
    template_name = 'institutions/department_detail.html'
    context_object_name = 'department'

class ClassroomListView(LoginRequiredMixin, ListView):
    model = Classroom
    template_name = 'institutions/classroom_list.html'
    context_object_name = 'classrooms'
    paginate_by = 25

    def get_queryset(self):
        return Classroom.objects.select_related('campus__institution')
