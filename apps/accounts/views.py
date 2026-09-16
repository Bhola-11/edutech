from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, TemplateView, UpdateView, ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy, reverse
from django.utils.translation import gettext_lazy as _
from .models import User, UserSessionLog
from .forms import UserLoginForm, UserRegistrationForm, UserProfileUpdateForm, TwoFactorVerifyForm
from .services import AuthenticationService, TwoFactorService
from apps.core.permissions import InstitutionAdminRequiredMixin

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('core:dashboard')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('core:dashboard')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.get_user()
        remember_me = form.cleaned_data.get('remember_me', False)

        if user.two_factor_enabled:
            self.request.session['2fa_preauth_user_id'] = str(user.id)
            self.request.session['2fa_remember_me'] = remember_me
            token = TwoFactorService.generate_token(user)
            # In a production deployment, code is dispatched via SMS/Email
            messages.info(self.request, f'Security verification code generated. (Demo Code: {token.token_code})')
            return redirect('accounts:two_factor_verify')

        AuthenticationService.process_login(self.request, user, remember_me=remember_me)
        messages.success(self.request, f'Welcome back, {user.get_full_name() or user.username}!')
        return super().form_valid(form)

class TwoFactorVerifyView(FormView):
    template_name = 'accounts/two_factor_verify.html'
    form_class = TwoFactorVerifyForm
    success_url = reverse_lazy('core:dashboard')

    def form_valid(self, form):
        user_id = self.request.session.get('2fa_preauth_user_id')
        if not user_id:
            messages.error(self.request, _('Authentication session expired. Please log in again.'))
            return redirect('accounts:login')

        user = get_object_or_404(User, id=user_id)
        code = form.cleaned_data['token_code']
        if TwoFactorService.verify_token(user, code):
            remember_me = self.request.session.get('2fa_remember_me', False)
            del self.request.session['2fa_preauth_user_id']
            if '2fa_remember_me' in self.request.session:
                del self.request.session['2fa_remember_me']
            AuthenticationService.process_login(self.request, user, remember_me=remember_me)
            messages.success(self.request, _('Two-factor verification successful.'))
            return super().form_valid(form)
        else:
            messages.error(self.request, _('Invalid or expired verification code.'))
            return self.form_invalid(form)

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        AuthenticationService.process_logout(request)
        messages.info(request, _('You have been securely logged out.'))
        return redirect('accounts:login')

    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class RegisterView(FormView):
    template_name = 'accounts/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, _('Your account was registered successfully! You can now log in.'))
        return super().form_valid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['active_sessions'] = UserSessionLog.objects.filter(user=self.request.user, is_expired=False)[:5]
        return context

class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileUpdateForm
    template_name = 'accounts/profile_edit.html'
    success_url = reverse_lazy('accounts:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, _('Your profile details have been successfully updated.'))
        return super().form_valid(form)

class SecuritySettingsView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/security_settings.html'

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if action == 'toggle_2fa':
            request.user.two_factor_enabled = not request.user.two_factor_enabled
            request.user.save(update_fields=['two_factor_enabled'])
            status = 'enabled' if request.user.two_factor_enabled else 'disabled'
            messages.success(request, f'Two-factor authentication has been {status}.')
        return redirect('accounts:security_settings')

class UserListView(LoginRequiredMixin, InstitutionAdminRequiredMixin, ListView):
    model = User
    template_name = 'accounts/user_list.html'
    context_object_name = 'users'
    paginate_by = 20

    def get_queryset(self):
        qs = User.objects.select_related('institution', 'campus', 'department')
        q = self.request.GET.get('q')
        role = self.request.GET.get('role')
        if q:
            qs = qs.filter(email__icontains=q) | qs.filter(username__icontains=q) | qs.filter(first_name__icontains=q) | qs.filter(last_name__icontains=q)
        if role:
            qs = qs.filter(role=role)
        return qs

class UserDetailView(LoginRequiredMixin, InstitutionAdminRequiredMixin, DetailView):
    model = User
    template_name = 'accounts/user_detail.html'
    context_object_name = 'target_user'
