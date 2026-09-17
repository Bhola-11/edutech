from django.shortcuts import render, get_object_or_404, redirect
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
