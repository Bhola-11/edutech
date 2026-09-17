"""
Generates Forms, Serializers, Views, Templates, and JS Controllers for Phase 2 apps.
"""
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_JS_DIR = os.path.join(BASE_DIR, 'static', 'js')

os.makedirs(STATIC_JS_DIR, exist_ok=True)

# 1. Assessments Views & Serializers
ASSESSMENTS_FORMS = '''from django import forms
from .models import Assessment, Question, AssessmentRubric, QuestionCategory


class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['course', 'title', 'assessment_type', 'duration_minutes', 'total_points', 'passing_percentage', 'instructions_html', 'shuffle_questions', 'shuffle_options', 'is_proctored', 'is_published']
        widgets = {
            'instructions_html': forms.Textarea(attrs={'rows': 4, 'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'assessment_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'total_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'passing_percentage': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['course', 'category', 'title', 'question_type', 'prompt_html', 'explanation_html', 'default_points', 'negative_points', 'difficulty', 'blooms_level', 'is_active']
        widgets = {
            'prompt_html': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'explanation_html': forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'question_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'difficulty': forms.Select(attrs={'class': 'form-select'}),
            'blooms_level': forms.Select(attrs={'class': 'form-select'}),
            'default_points': forms.NumberInput(attrs={'class': 'form-control'}),
            'negative_points': forms.NumberInput(attrs={'class': 'form-control'}),
        }
'''

ASSESSMENTS_SERIALIZERS = '''from rest_framework import serializers
from .models import Assessment, Question, QuestionOption, AssessmentRubric, AssessmentSection


class QuestionOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionOption
        fields = ['id', 'option_text', 'option_html', 'is_correct', 'explanation', 'display_order']


class QuestionSerializer(serializers.ModelSerializer):
    options = QuestionOptionSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'course', 'category', 'title', 'question_type', 'prompt_html', 'explanation_html', 'default_points', 'negative_points', 'difficulty', 'blooms_level', 'options', 'is_active']


class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = ['id', 'institution', 'course', 'title', 'slug', 'assessment_type', 'duration_minutes', 'total_points', 'passing_percentage', 'instructions_html', 'shuffle_questions', 'is_proctored', 'is_published', 'created_at']
'''

ASSESSMENTS_VIEWS = '''from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Assessment, Question, QuestionCategory
from .forms import AssessmentForm, QuestionForm
from .services.code_runner_service import CodeExecutionService


@login_required
def assessment_list(request):
    assessments = Assessment.objects.filter(is_deleted=False).select_related('course')
    return render(request, 'assessments/assessment_list.html', {'assessments': assessments})


@login_required
def assessment_detail(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk, is_deleted=False)
    sections = assessment.sections.prefetch_related('section_questions__question').all()
    return render(request, 'assessments/assessment_detail.html', {'assessment': assessment, 'sections': sections})


@login_required
def assessment_create(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(commit=False)
            assessment.institution = request.user.institution
            assessment.save()
            messages.success(request, 'Assessment created successfully.')
            return redirect('assessments:detail', pk=assessment.pk)
    else:
        form = AssessmentForm()
    return render(request, 'assessments/assessment_form.html', {'form': form, 'title': 'Create Assessment'})


@login_required
def code_sandbox_view(request):
    return render(request, 'assessments/code_sandbox.html')


@login_required
def run_code_api(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body.decode('utf-8'))
        code = data.get('code', '')
        input_data = data.get('input_data', '')
        expected_output = data.get('expected_output', '')
        result = CodeExecutionService.execute_python_code(code, input_data, expected_output)
        return JsonResponse(result)
    return JsonResponse({'error': 'POST required'}, status=400)
'''

ASSESSMENTS_API_VIEWS = '''from rest_framework import viewsets, permissions
from .models import Assessment, Question, AssessmentRubric
from .serializers import AssessmentSerializer, QuestionSerializer


class AssessmentViewSet(viewsets.ModelViewSet):
    queryset = Assessment.objects.filter(is_deleted=False)
    serializer_class = AssessmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.filter(is_deleted=False)
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

ASSESSMENTS_URLS = '''from django.urls import path
from . import views

app_name = 'assessments'

urlpatterns = [
    path('', views.assessment_list, name='list'),
    path('create/', views.assessment_create, name='create'),
    path('<int:pk>/', views.assessment_detail, name='detail'),
    path('sandbox/', views.code_sandbox_view, name='sandbox'),
    path('api/run-code/', views.run_code_api, name='api_run_code'),
]
'''

ASSESSMENTS_API_URLS = '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AssessmentViewSet, QuestionViewSet

router = DefaultRouter()
router.register(r'items', AssessmentViewSet, basename='assessment')
router.register(r'questions', QuestionViewSet, basename='question')

urlpatterns = [
    path('', include(router.urls)),
]
'''

# 2. Examinations Views & Serializers
EXAMINATIONS_VIEWS = '''from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone
from .models import ExamSession, ExamAttempt, StudentAnswer, ProctoringEvent
from apps.assessments.models import Assessment
from .services.exam_timer_service import ExamTimerService
from .services.proctoring_service import ProctoringSecurityService


@login_required
def exam_session_list(request):
    sessions = ExamSession.objects.all().select_related('assessment', 'batch')
    return render(request, 'examinations/session_list.html', {'sessions': sessions})


@login_required
def exam_taker_view(request, session_id):
    session = get_object_or_404(ExamSession, pk=session_id)
    attempt, created = ExamAttempt.objects.get_or_create(
        session=session,
        student=request.user,
        defaults={
            'expires_at': timezone.now() + timezone.timedelta(minutes=session.assessment.duration_minutes),
            'status': 'IN_PROGRESS',
            'ip_address': request.META.get('REMOTE_ADDR')
        }
    )
    timer = ExamTimerService.check_time_remaining(attempt.started_at, session.assessment.duration_minutes)
    sections = session.assessment.sections.prefetch_related('section_questions__question__options').all()
    return render(request, 'examinations/exam_session.html', {
        'session': session,
        'attempt': attempt,
        'timer': timer,
        'sections': sections
    })


@login_required
def proctor_monitor_view(request, session_id):
    session = get_object_or_404(ExamSession, pk=session_id)
    attempts = ExamAttempt.objects.filter(session=session).select_related('student')
    events = ProctoringEvent.objects.filter(attempt__session=session).order_by('-captured_at')[:50]
    return render(request, 'examinations/proctor_monitor.html', {
        'session': session,
        'attempts': attempts,
        'recent_events': events
    })


@login_required
def log_proctoring_event_api(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body.decode('utf-8'))
        attempt_id = data.get('attempt_id')
        event_type = data.get('event_type')
        severity = data.get('severity', 'MEDIUM')
        attempt = get_object_or_404(ExamAttempt, pk=attempt_id, student=request.user)
        ev = ProctoringEvent.objects.create(
            attempt=attempt,
            event_type=event_type,
            severity=severity,
            payload_data=data.get('payload', {})
        )
        return JsonResponse({'status': 'logged', 'event_id': ev.id})
    return JsonResponse({'error': 'POST required'}, status=400)
'''

EXAMINATIONS_SERIALIZERS = '''from rest_framework import serializers
from .models import ExamSession, ExamAttempt, ProctoringEvent, StudentAnswer


class ExamSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamSession
        fields = '__all__'


class ExamAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamAttempt
        fields = '__all__'


class ProctoringEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProctoringEvent
        fields = '__all__'
'''

EXAMINATIONS_API_VIEWS = '''from rest_framework import viewsets, permissions
from .models import ExamSession, ExamAttempt, ProctoringEvent
from .serializers import ExamSessionSerializer, ExamAttemptSerializer, ProctoringEventSerializer


class ExamSessionViewSet(viewsets.ModelViewSet):
    queryset = ExamSession.objects.all()
    serializer_class = ExamSessionSerializer
    permission_classes = [permissions.IsAuthenticated]


class ExamAttemptViewSet(viewsets.ModelViewSet):
    queryset = ExamAttempt.objects.all()
    serializer_class = ExamAttemptSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProctoringEventViewSet(viewsets.ModelViewSet):
    queryset = ProctoringEvent.objects.all()
    serializer_class = ProctoringEventSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

EXAMINATIONS_URLS = '''from django.urls import path
from . import views

app_name = 'examinations'

urlpatterns = [
    path('', views.exam_session_list, name='list'),
    path('take/<int:session_id>/', views.exam_taker_view, name='take'),
    path('monitor/<int:session_id>/', views.proctor_monitor_view, name='monitor'),
    path('api/log-event/', views.log_proctoring_event_api, name='api_log_event'),
]
'''

EXAMINATIONS_API_URLS = '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import ExamSessionViewSet, ExamAttemptViewSet, ProctoringEventViewSet

router = DefaultRouter()
router.register(r'sessions', ExamSessionViewSet, basename='session')
router.register(r'attempts', ExamAttemptViewSet, basename='attempt')
router.register(r'proctor-events', ProctoringEventViewSet, basename='proctor-event')

urlpatterns = [
    path('', include(router.urls)),
]
'''

# 3. Assignments Views, Forms, Serializers
ASSIGNMENTS_FORMS = '''from django import forms
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
'''

ASSIGNMENTS_SERIALIZERS = '''from rest_framework import serializers
from .models import Assignment, AssignmentSubmission, PeerReviewAssignment


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignmentSubmission
        fields = '__all__'
'''

ASSIGNMENTS_VIEWS = '''from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Assignment, AssignmentSubmission, SubmissionAttachment
from .forms import AssignmentForm, SubmissionForm


@login_required
def assignment_list(request):
    assignments = Assignment.objects.filter(is_deleted=False).select_related('course')
    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})


@login_required
def assignment_detail(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, is_deleted=False)
    submission = AssignmentSubmission.objects.filter(assignment=assignment, student=request.user).first()
    return render(request, 'assignments/assignment_detail.html', {'assignment': assignment, 'submission': submission})


@login_required
def assignment_submit(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk, is_deleted=False)
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            now = timezone.now()
            is_late = now > assignment.due_date
            sub = form.save(commit=False)
            sub.assignment = assignment
            sub.student = request.user
            sub.is_late = is_late
            sub.save()

            if request.FILES.get('file_upload'):
                f = request.FILES['file_upload']
                SubmissionAttachment.objects.create(
                    submission=sub,
                    file=f,
                    file_name=f.name,
                    file_size_bytes=f.size,
                    mime_type=f.content_type
                )
            messages.success(request, 'Assignment submitted successfully.')
            return redirect('assignments:detail', pk=assignment.pk)
    else:
        form = SubmissionForm()
    return render(request, 'assignments/assignment_submit.html', {'assignment': assignment, 'form': form})
'''

ASSIGNMENTS_API_VIEWS = '''from rest_framework import viewsets, permissions
from .models import Assignment, AssignmentSubmission
from .serializers import AssignmentSerializer, AssignmentSubmissionSerializer


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.filter(is_deleted=False)
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.all()
    serializer_class = AssignmentSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

ASSIGNMENTS_URLS = '''from django.urls import path
from . import views

app_name = 'assignments'

urlpatterns = [
    path('', views.assignment_list, name='list'),
    path('<int:pk>/', views.assignment_detail, name='detail'),
    path('<int:pk>/submit/', views.assignment_submit, name='submit'),
]
'''

ASSIGNMENTS_API_URLS = '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import AssignmentViewSet, AssignmentSubmissionViewSet

router = DefaultRouter()
router.register(r'items', AssignmentViewSet, basename='assignment')
router.register(r'submissions', AssignmentSubmissionViewSet, basename='submission')

urlpatterns = [
    path('', include(router.urls)),
]
'''

# 4. Grading Views & Serializers
GRADING_SERIALIZERS = '''from rest_framework import serializers
from .models import GradingScale, ScaleGradeLevel, GradeCategory, GradeItem, StudentGrade, FinalCourseGrade


class ScaleGradeLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScaleGradeLevel
        fields = '__all__'


class GradingScaleSerializer(serializers.ModelSerializer):
    levels = ScaleGradeLevelSerializer(many=True, read_only=True)

    class Meta:
        model = GradingScale
        fields = '__all__'


class FinalCourseGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalCourseGrade
        fields = '__all__'
'''

GRADING_VIEWS = '''from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import GradingScale, GradeCategory, FinalCourseGrade
from apps.courses.models import Course
from apps.enrollments.models import StudentEnrollment


@login_required
def gradebook_view(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    categories = course.grade_categories.prefetch_related('items__grades__student').all()
    enrollments = StudentEnrollment.objects.filter(course=course, status='ACTIVE').select_related('student', 'final_grade')
    return render(request, 'grading/gradebook.html', {
        'course': course,
        'categories': categories,
        'enrollments': enrollments
    })


@login_required
def transcript_view(request, student_id=None):
    from apps.accounts.models import User
    user = request.user if not student_id else get_object_or_404(User, pk=student_id)
    grades = FinalCourseGrade.objects.filter(enrollment__student=user).select_related('enrollment__course')
    return render(request, 'grading/transcript.html', {'student': user, 'grades': grades})
'''

GRADING_API_VIEWS = '''from rest_framework import viewsets, permissions
from .models import GradingScale, FinalCourseGrade
from .serializers import GradingScaleSerializer, FinalCourseGradeSerializer


class GradingScaleViewSet(viewsets.ModelViewSet):
    queryset = GradingScale.objects.all()
    serializer_class = GradingScaleSerializer
    permission_classes = [permissions.IsAuthenticated]


class FinalCourseGradeViewSet(viewsets.ModelViewSet):
    queryset = FinalCourseGrade.objects.all()
    serializer_class = FinalCourseGradeSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

GRADING_URLS = '''from django.urls import path
from . import views

app_name = 'grading'

urlpatterns = [
    path('course/<int:course_id>/', views.gradebook_view, name='gradebook'),
    path('transcript/', views.transcript_view, name='transcript'),
    path('transcript/<int:student_id>/', views.transcript_view, name='student_transcript'),
]
'''

GRADING_API_URLS = '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import GradingScaleViewSet, FinalCourseGradeViewSet

router = DefaultRouter()
router.register(r'scales', GradingScaleViewSet, basename='scale')
router.register(r'final-grades', FinalCourseGradeViewSet, basename='final-grade')

urlpatterns = [
    path('', include(router.urls)),
]
'''

# 5. Certificates Views & Serializers
CERTIFICATES_SERIALIZERS = '''from rest_framework import serializers
from .models import CertificateTemplate, IssuedCertificate, DigitalBadge


class IssuedCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssuedCertificate
        fields = '__all__'


class DigitalBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalBadge
        fields = '__all__'
'''

CERTIFICATES_VIEWS = '''from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from .models import IssuedCertificate, DigitalBadge, CertificateVerificationLog
from .services.pdf_certificate_service import PDFCertificateGeneratorService
from .services.crypto_verification_service import CertificateCryptoService


@login_required
def certificate_list(request):
    certificates = IssuedCertificate.objects.filter(student=request.user, is_revoked=False).select_related('course', 'template')
    badges = DigitalBadge.objects.filter(student=request.user)
    return render(request, 'certificates/certificate_list.html', {'certificates': certificates, 'badges': badges})


def verify_certificate_public(request, certificate_number=None):
    cert = None
    is_valid = False
    query = certificate_number or request.GET.get('code', '').strip()

    if query:
        cert = IssuedCertificate.objects.filter(certificate_number=query, is_revoked=False).select_related('student', 'course', 'institution').first()
        if cert:
            is_valid = CertificateCryptoService.verify_hash(
                student_id=cert.student.id,
                course_code=cert.course.code if cert.course else 'GENERAL',
                certificate_number=cert.certificate_number,
                issue_date_str=str(cert.issue_date),
                provided_hash=cert.verification_hash
            )
            # Log verification lookup
            CertificateVerificationLog.objects.create(
                certificate=cert,
                verifier_ip=request.META.get('REMOTE_ADDR'),
                verifier_user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
                is_valid=is_valid
            )

    return render(request, 'certificates/verify_certificate.html', {'cert': cert, 'is_valid': is_valid, 'query': query})


@login_required
def download_certificate_pdf(request, certificate_id):
    cert = get_object_or_404(IssuedCertificate, certificate_id=certificate_id, is_revoked=False)
    pdf_bytes = PDFCertificateGeneratorService.generate_certificate_pdf(
        student_name=cert.student.get_full_name() or cert.student.username,
        course_title=cert.course.title if cert.course else 'Comprehensive Program',
        course_code=cert.course.code if cert.course else 'PROG-100',
        institution_name=cert.institution.name,
        certificate_number=cert.certificate_number,
        issue_date_str=cert.issue_date.strftime('%B %d, %Y'),
        honors_title=cert.honors_title,
        issuer_name=cert.template.issuer_name if cert.template else 'Dean of Academic Affairs',
        issuer_title=cert.template.issuer_title if cert.template else 'Office of the Registrar'
    )
    response = HttpResponse(pdf_bytes, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="Certificate-{cert.certificate_number}.pdf"'
    return response
'''

CERTIFICATES_API_VIEWS = '''from rest_framework import viewsets, permissions
from .models import IssuedCertificate, DigitalBadge
from .serializers import IssuedCertificateSerializer, DigitalBadgeSerializer


class IssuedCertificateViewSet(viewsets.ModelViewSet):
    queryset = IssuedCertificate.objects.filter(is_revoked=False)
    serializer_class = IssuedCertificateSerializer
    permission_classes = [permissions.IsAuthenticated]


class DigitalBadgeViewSet(viewsets.ModelViewSet):
    queryset = DigitalBadge.objects.all()
    serializer_class = DigitalBadgeSerializer
    permission_classes = [permissions.IsAuthenticated]
'''

CERTIFICATES_URLS = '''from django.urls import path
from . import views

app_name = 'certificates'

urlpatterns = [
    path('', views.certificate_list, name='list'),
    path('verify/', views.verify_certificate_public, name='verify_public'),
    path('verify/<str:certificate_number>/', views.verify_certificate_public, name='verify_code'),
    path('download/<uuid:certificate_id>/', views.download_certificate_pdf, name='download_pdf'),
]
'''

CERTIFICATES_API_URLS = '''from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import IssuedCertificateViewSet, DigitalBadgeViewSet

router = DefaultRouter()
router.register(r'credentials', IssuedCertificateViewSet, basename='credential')
router.register(r'badges', DigitalBadgeViewSet, basename='badge')

urlpatterns = [
    path('', include(router.urls)),
]
'''

CODE_MAP = {
    'apps/assessments/forms.py': ASSESSMENTS_FORMS,
    'apps/assessments/serializers.py': ASSESSMENTS_SERIALIZERS,
    'apps/assessments/views.py': ASSESSMENTS_VIEWS,
    'apps/assessments/api_views.py': ASSESSMENTS_API_VIEWS,
    'apps/assessments/urls.py': ASSESSMENTS_URLS,
    'apps/assessments/api_urls.py': ASSESSMENTS_API_URLS,

    'apps/examinations/serializers.py': EXAMINATIONS_SERIALIZERS,
    'apps/examinations/views.py': EXAMINATIONS_VIEWS,
    'apps/examinations/api_views.py': EXAMINATIONS_API_VIEWS,
    'apps/examinations/urls.py': EXAMINATIONS_URLS,
    'apps/examinations/api_urls.py': EXAMINATIONS_API_URLS,

    'apps/assignments/forms.py': ASSESSMENTS_FORMS.replace('Assessment', 'Assignment'), # placeholder replaced below
    'apps/assignments/serializers.py': ASSIGNMENTS_SERIALIZERS,
    'apps/assignments/views.py': ASSIGNMENTS_VIEWS,
    'apps/assignments/api_views.py': ASSIGNMENTS_API_VIEWS,
    'apps/assignments/urls.py': ASSIGNMENTS_URLS,
    'apps/assignments/api_urls.py': ASSIGNMENTS_API_URLS,

    'apps/grading/serializers.py': GRADING_SERIALIZERS,
    'apps/grading/views.py': GRADING_VIEWS,
    'apps/grading/api_views.py': GRADING_API_VIEWS,
    'apps/grading/urls.py': GRADING_URLS,
    'apps/grading/api_urls.py': GRADING_API_URLS,

    'apps/certificates/serializers.py': CERTIFICATES_SERIALIZERS,
    'apps/certificates/views.py': CERTIFICATES_VIEWS,
    'apps/certificates/api_views.py': CERTIFICATES_API_VIEWS,
    'apps/certificates/urls.py': CERTIFICATES_URLS,
    'apps/certificates/api_urls.py': CERTIFICATES_API_URLS,
}

# Fix assignment form
CODE_MAP['apps/assignments/forms.py'] = ASSIGNMENTS_FORMS

for rel_path, content in CODE_MAP.items():
    filepath = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Updated: {rel_path}")

print("All Phase 2 views, forms, serializers, and API endpoints configured.")
