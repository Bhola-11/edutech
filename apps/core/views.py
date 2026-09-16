from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q, Count
from django.db import connection
from .constants import UserRoleChoices
from .models import ActivityLog, SystemNotification
from .permissions import RoleRequiredMixin, SuperAdminRequiredMixin

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to EduTech Enterprise Platform'
        return context

class DashboardRedirectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        role = getattr(request.user, 'role', None)
        if request.user.is_superuser or role == UserRoleChoices.SUPERADMIN:
            return redirect('core:superadmin_dashboard')
        elif role == UserRoleChoices.INSTITUTION_ADMIN:
            return redirect('core:admin_dashboard')
        elif role in [UserRoleChoices.DEAN, UserRoleChoices.DEPARTMENT_HEAD, UserRoleChoices.INSTRUCTOR, UserRoleChoices.TEACHING_ASSISTANT]:
            return redirect('core:instructor_dashboard')
        elif role == UserRoleChoices.STUDENT:
            return redirect('core:student_dashboard')
        elif role == UserRoleChoices.PARENT:
            return redirect('core:parent_dashboard')
        elif role == UserRoleChoices.CORPORATE_PARTNER:
            return redirect('core:corporate_dashboard')
        return redirect('accounts:profile')

class SuperAdminDashboardView(LoginRequiredMixin, SuperAdminRequiredMixin, TemplateView):
    template_name = 'dashboards/superadmin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Global SuperAdmin Console'
        context['recent_audit_logs'] = ActivityLog.objects.select_related('user')[:10]
        return context

class InstitutionAdminDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/admin_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Institution Administration Dashboard'
        return context

class InstructorDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/instructor_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Faculty & Instructor Portal'
        return context

class StudentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/student_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Student Learning Hub'
        return context

class ParentDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/parent_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Parent & Guardian Portal'
        return context

class CorporateDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboards/corporate_dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Corporate Workforce Training'
        return context

class NotificationListView(LoginRequiredMixin, ListView):
    model = SystemNotification
    template_name = 'core/notification_list.html'
    context_object_name = 'notifications'
    paginate_by = 20

    def get_queryset(self):
        return SystemNotification.objects.filter(recipient=self.request.user)

class MarkNotificationReadView(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        notification = get_object_or_404(SystemNotification, pk=pk, recipient=request.user)
        notification.mark_as_read()
        return JsonResponse({'status': 'success', 'notification_id': str(notification.id)})

class HealthCheckView(View):
    def get(self, request, *args, **kwargs):
        db_status = 'ok'
        try:
            with connection.cursor() as cursor:
                cursor.execute('SELECT 1')
        except Exception as e:
            db_status = f'error: {str(e)}'

        return JsonResponse({
            'status': 'healthy' if db_status == 'ok' else 'degraded',
            'database': db_status,
            'version': '2.5.0-Enterprise',
            'platform': 'EduTech Enterprise',
        })
