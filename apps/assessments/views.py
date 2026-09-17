from django.shortcuts import render, get_object_or_404, redirect
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
