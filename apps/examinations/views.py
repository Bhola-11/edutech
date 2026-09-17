from django.shortcuts import render, get_object_or_404, redirect
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
