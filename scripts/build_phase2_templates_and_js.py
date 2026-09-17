"""
Generates UI Templates and JavaScript Controllers for Phase 2: Assessments, Examinations, Assignments, Grading, Certificates.
"""
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_JS_DIR = os.path.join(BASE_DIR, 'static', 'js')

FILES = {
    # 1. Assessments Templates
    'templates/assessments/assessment_list.html': '''{% extends 'base.html' %}
{% block title %}Assessments & Quizzes - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h2 class="h3 fw-bold mb-1"><i class="bi bi-patch-question text-primary me-2"></i>Assessments & Quizzes</h2>
            <p class="text-muted mb-0">Module quizzes, proctored midterm exams, and laboratory practical assessments.</p>
        </div>
        <div class="btn-group">
            <a href="{% url 'assessments:create' %}" class="btn btn-primary"><i class="bi bi-plus-circle me-1"></i>Create Assessment</a>
            <a href="{% url 'assessments:sandbox' %}" class="btn btn-outline-secondary"><i class="bi bi-terminal me-1"></i>Coding Sandbox</a>
        </div>
    </div>
    <div class="card shadow-sm border-0">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th>Assessment Title</th>
                            <th>Course</th>
                            <th>Type</th>
                            <th>Duration</th>
                            <th>Points</th>
                            <th>Proctored</th>
                            <th>Status</th>
                            <th class="text-end">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for item in assessments %}
                        <tr>
                            <td>
                                <a href="{% url 'assessments:detail' item.pk %}" class="fw-bold text-decoration-none">{{ item.title }}</a>
                            </td>
                            <td><span class="badge bg-light text-dark">{{ item.course.code }}</span></td>
                            <td><span class="badge bg-secondary">{{ item.get_assessment_type_display }}</span></td>
                            <td><i class="bi bi-clock me-1 text-muted"></i>{{ item.duration_minutes }} mins</td>
                            <td>{{ item.total_points }} pts</td>
                            <td>
                                {% if item.is_proctored %}
                                <span class="badge bg-warning text-dark"><i class="bi bi-shield-lock me-1"></i>Proctored</span>
                                {% else %}
                                <span class="badge bg-light text-muted">Standard</span>
                                {% endif %}
                            </td>
                            <td>
                                {% if item.is_published %}
                                <span class="badge bg-success">Published</span>
                                {% else %}
                                <span class="badge bg-secondary">Draft</span>
                                {% endif %}
                            </td>
                            <td class="text-end">
                                <a href="{% url 'assessments:detail' item.pk %}" class="btn btn-sm btn-outline-primary">View</a>
                            </td>
                        </tr>
                        {% empty %}
                        <tr><td colspan="8" class="text-center py-4 text-muted">No assessments created yet.</td></tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/assessments/assessment_detail.html': '''{% extends 'base.html' %}
{% block title %}{{ assessment.title }} - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item"><a href="{% url 'assessments:list' %}">Assessments</a></li>
            <li class="breadcrumb-item active">{{ assessment.title }}</li>
        </ol>
    </nav>
    <div class="row g-4">
        <div class="col-lg-8">
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-body">
                    <h3 class="fw-bold">{{ assessment.title }}</h3>
                    <p class="text-muted">{{ assessment.course.title }} ({{ assessment.course.code }})</p>
                    <hr>
                    <div class="row g-3 text-center my-2">
                        <div class="col-3"><div class="p-2 border rounded"><small class="text-muted d-block">Duration</small><span class="fw-bold">{{ assessment.duration_minutes }}m</span></div></div>
                        <div class="col-3"><div class="p-2 border rounded"><small class="text-muted d-block">Total Points</small><span class="fw-bold">{{ assessment.total_points }}</span></div></div>
                        <div class="col-3"><div class="p-2 border rounded"><small class="text-muted d-block">Passing Pct</small><span class="fw-bold">{{ assessment.passing_percentage }}%</span></div></div>
                        <div class="col-3"><div class="p-2 border rounded"><small class="text-muted d-block">Max Attempts</small><span class="fw-bold">{{ assessment.max_attempts }}</span></div></div>
                    </div>
                    {% if assessment.instructions_html %}
                    <h5 class="fw-bold mt-4">Instructions</h5>
                    <div class="p-3 bg-light rounded">{{ assessment.instructions_html|safe }}</div>
                    {% endif %}
                </div>
            </div>
            <h4 class="fw-bold mb-3">Sections & Questions</h4>
            {% for sec in sections %}
            <div class="card shadow-sm border-0 mb-3">
                <div class="card-header bg-light d-flex justify-content-between align-items-center">
                    <span class="fw-bold">{{ sec.title }}</span>
                    <span class="badge bg-primary">{{ sec.section_points }} pts</span>
                </div>
                <ul class="list-group list-group-flush">
                    {% for sq in sec.section_questions.all %}
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        <div>
                            <span class="fw-bold">{{ sq.question.title }}</span>
                            <small class="text-muted d-block">{{ sq.question.get_question_type_display }} &bull; {{ sq.question.difficulty }} &bull; Bloom's: {{ sq.question.blooms_level }}</small>
                        </div>
                        <span class="badge bg-secondary">{{ sq.points_override|default:sq.question.default_points }} pts</span>
                    </li>
                    {% endfor %}
                </ul>
            </div>
            {% empty %}
            <div class="alert alert-info">No sections configured for this assessment.</div>
            {% endfor %}
        </div>
        <div class="col-lg-4">
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-header bg-light fw-bold">Assessment Controls</div>
                <div class="card-body">
                    <div class="d-grid gap-2">
                        <a href="{% url 'assessments:sandbox' %}" class="btn btn-outline-primary"><i class="bi bi-code-square me-1"></i>Open Sandbox</a>
                        <a href="{% url 'examinations:list' %}" class="btn btn-success"><i class="bi bi-play-circle me-1"></i>Schedule Exam Session</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/assessments/assessment_form.html': '''{% extends 'base.html' %}
{% block title %}{{ title }} - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container py-4">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card shadow-sm border-0">
                <div class="card-header bg-light fw-bold">{{ title }}</div>
                <div class="card-body">
                    <form method="post">
                        {% csrf_token %}
                        {{ form.as_p }}
                        <div class="d-flex justify-content-end gap-2 mt-4">
                            <a href="{% url 'assessments:list' %}" class="btn btn-outline-secondary">Cancel</a>
                            <button type="submit" class="btn btn-primary">Save Assessment</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/assessments/code_sandbox.html': '''{% extends 'base.html' %}
{% block title %}Interactive Coding Sandbox - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <h3 class="fw-bold mb-3"><i class="bi bi-terminal text-primary me-2"></i>Interactive Coding Sandbox</h3>
    <div class="row g-4">
        <div class="col-lg-7">
            <div class="card shadow-sm border-0 h-100">
                <div class="card-header bg-dark text-white d-flex justify-content-between align-items-center">
                    <span>Python 3.11 Sandbox</span>
                    <button id="runCodeBtn" class="btn btn-sm btn-success"><i class="bi bi-play-fill me-1"></i>Execute Code</button>
                </div>
                <div class="card-body p-0">
                    <textarea id="codeEditor" class="form-control font-monospace border-0 p-3" style="height: 400px; resize: none;" placeholder="# Write your Python code here...
def solve_problem():
    print('Hello from EduTech Sandbox!')

solve_problem()
"></textarea>
                </div>
            </div>
        </div>
        <div class="col-lg-5">
            <div class="card shadow-sm border-0 h-100">
                <div class="card-header bg-light fw-bold">Console Output & Test Results</div>
                <div class="card-body">
                    <div id="outputConsole" class="p-3 bg-dark text-light font-monospace rounded" style="height: 350px; overflow-y: auto;">
                        <span class="text-muted">&gt; Ready to execute code...</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
{% block extra_js %}
<script src="/static/js/code_sandbox.js"></script>
{% endblock %}
''',

    # 2. Examinations Templates
    'templates/examinations/session_list.html': '''{% extends 'base.html' %}
{% block title %}Examination Sessions - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h2 class="h3 fw-bold mb-1"><i class="bi bi-journal-check text-primary me-2"></i>Examination Sessions</h2>
            <p class="text-muted mb-0">Active proctored exam sessions and scheduled examination windows.</p>
        </div>
    </div>
    <div class="card shadow-sm border-0">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th>Session Code</th>
                            <th>Assessment</th>
                            <th>Window</th>
                            <th>Status</th>
                            <th>Security</th>
                            <th class="text-end">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for s in sessions %}
                        <tr>
                            <td class="fw-bold font-monospace">{{ s.session_code }}</td>
                            <td>{{ s.assessment.title }}</td>
                            <td><small>{{ s.start_window|date:"M d, H:i" }} - {{ s.end_window|date:"M d, H:i" }}</small></td>
                            <td><span class="badge bg-primary">{{ s.get_status_display }}</span></td>
                            <td>
                                {% if s.requires_webcam %}<span class="badge bg-danger"><i class="bi bi-camera-video me-1"></i>Webcam</span>{% endif %}
                            </td>
                            <td class="text-end">
                                <a href="{% url 'examinations:take' s.pk %}" class="btn btn-sm btn-success"><i class="bi bi-box-arrow-in-right me-1"></i>Start Exam</a>
                                <a href="{% url 'examinations:monitor' s.pk %}" class="btn btn-sm btn-outline-dark"><i class="bi bi-display me-1"></i>Proctor</a>
                            </td>
                        </tr>
                        {% empty %}
                        <tr><td colspan="6" class="text-center py-4 text-muted">No examination sessions active.</td></tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/examinations/exam_session.html': '''{% extends 'base.html' %}
{% block title %}Active Examination: {{ session.assessment.title }}{% endblock %}
{% block content %}
<div class="container-fluid py-3" id="examContainer" data-attempt-id="{{ attempt.id }}">
    <div class="card shadow-sm border-0 mb-3 bg-dark text-white">
        <div class="card-body d-flex justify-content-between align-items-center py-2">
            <div>
                <h5 class="fw-bold mb-0">{{ session.assessment.title }}</h5>
                <small class="text-muted">{{ request.user.get_full_name }} &bull; Attempt #{{ attempt.attempt_number }}</small>
            </div>
            <div class="d-flex align-items-center gap-3">
                <div class="text-end">
                    <small class="text-muted d-block">Time Remaining</small>
                    <span id="countdownTimer" class="h4 fw-bold font-monospace text-warning mb-0" data-seconds="{{ timer.seconds_remaining }}">--:--</span>
                </div>
                <button id="submitExamBtn" class="btn btn-danger btn-sm"><i class="bi bi-check-circle me-1"></i>Submit Exam</button>
            </div>
        </div>
    </div>
    <div class="row g-3">
        <div class="col-lg-9">
            {% for sec in sections %}
            <div class="card shadow-sm border-0 mb-3">
                <div class="card-header bg-light fw-bold">{{ sec.title }} ({{ sec.section_points }} pts)</div>
                <div class="card-body">
                    {% for sq in sec.section_questions.all %}
                    <div class="mb-4 pb-3 border-bottom question-block" data-question-id="{{ sq.question.id }}">
                        <p class="fw-bold mb-2">Q{{ forloop.counter }}. {{ sq.question.prompt_html|safe }}</p>
                        {% if sq.question.question_type == 'MCQ_SINGLE' or sq.question.question_type == 'TRUE_FALSE' %}
                        {% for opt in sq.question.options.all %}
                        <div class="form-check my-2">
                            <input class="form-check-input" type="radio" name="q_{{ sq.question.id }}" id="opt_{{ opt.id }}" value="{{ opt.id }}">
                            <label class="form-check-label" for="opt_{{ opt.id }}">{{ opt.option_text }}</label>
                        </div>
                        {% endfor %}
                        {% elif sq.question.question_type == 'SHORT_ANSWER' or sq.question.question_type == 'ESSAY' %}
                        <textarea class="form-control" rows="3" placeholder="Type your response here..."></textarea>
                        {% endif %}
                    </div>
                    {% endfor %}
                </div>
            </div>
            {% endfor %}
        </div>
        <div class="col-lg-3">
            <div class="card shadow-sm border-0 sticky-top" style="top: 20px;">
                <div class="card-header bg-light fw-bold">Proctoring & Security</div>
                <div class="card-body">
                    <div class="alert alert-warning py-2 mb-2"><small><i class="bi bi-shield-exclamation me-1"></i>Tab switches & fullscreen exits are monitored.</small></div>
                    <div class="d-grid mt-3">
                        <button id="fullscreenBtn" class="btn btn-outline-primary btn-sm"><i class="bi bi-arrows-fullscreen me-1"></i>Enter Fullscreen</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
{% block extra_js %}
<script src="/static/js/exam_runner.js"></script>
{% endblock %}
''',

    'templates/examinations/proctor_monitor.html': '''{% extends 'base.html' %}
{% block title %}Proctor Live Monitor - {{ session.session_code }}{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h3 class="fw-bold mb-1"><i class="bi bi-shield-check text-primary me-2"></i>Live Proctoring Dashboard</h3>
            <p class="text-muted mb-0">Monitoring Session {{ session.session_code }} &bull; {{ session.assessment.title }}</p>
        </div>
    </div>
    <div class="row g-4">
        <div class="col-lg-8">
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-header bg-light fw-bold">Active Candidates ({{ attempts.count }})</div>
                <div class="card-body p-0">
                    <div class="table-responsive">
                        <table class="table table-hover align-middle mb-0">
                            <thead class="table-light">
                                <tr>
                                    <th>Candidate</th>
                                    <th>Started At</th>
                                    <th>Status</th>
                                    <th>IP Address</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for a in attempts %}
                                <tr>
                                    <td><strong>{{ a.student.get_full_name|default:a.student.username }}</strong></td>
                                    <td>{{ a.started_at|date:"H:i:s" }}</td>
                                    <td><span class="badge bg-primary">{{ a.get_status_display }}</span></td>
                                    <td><small class="font-monospace text-muted">{{ a.ip_address }}</small></td>
                                    <td><button class="btn btn-sm btn-outline-danger">Flag Disqualify</button></td>
                                </tr>
                                {% empty %}
                                <tr><td colspan="5" class="text-center py-3 text-muted">No active candidate sessions.</td></tr>
                                {% endfor %}
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-lg-4">
            <div class="card shadow-sm border-0">
                <div class="card-header bg-light fw-bold">Live Security Incident Stream</div>
                <div class="card-body p-0">
                    <ul class="list-group list-group-flush">
                        {% for ev in recent_events %}
                        <li class="list-group-item d-flex justify-content-between align-items-center">
                            <div>
                                <span class="badge bg-danger me-1">{{ ev.severity }}</span>
                                <small class="fw-bold">{{ ev.get_event_type_display }}</small>
                                <small class="text-muted d-block">{{ ev.attempt.student.username }} &bull; {{ ev.captured_at|date:"H:i:s" }}</small>
                            </div>
                        </li>
                        {% empty %}
                        <li class="list-group-item text-center py-3 text-muted">No security incidents captured.</li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    # 3. Assignments Templates
    'templates/assignments/assignment_list.html': '''{% extends 'base.html' %}
{% block title %}Assignments & Projects - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h2 class="h3 fw-bold mb-1"><i class="bi bi-file-earmark-code text-primary me-2"></i>Assignments & Term Projects</h2>
            <p class="text-muted mb-0">Course deliverables, lab problem sets, and peer evaluation workflows.</p>
        </div>
    </div>
    <div class="card shadow-sm border-0">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-hover align-middle mb-0">
                    <thead class="table-light">
                        <tr>
                            <th>Assignment Title</th>
                            <th>Course</th>
                            <th>Type</th>
                            <th>Points</th>
                            <th>Due Date</th>
                            <th class="text-end">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for a in assignments %}
                        <tr>
                            <td><a href="{% url 'assignments:detail' a.pk %}" class="fw-bold text-decoration-none">{{ a.title }}</a></td>
                            <td><span class="badge bg-light text-dark">{{ a.course.code }}</span></td>
                            <td><span class="badge bg-secondary">{{ a.get_submission_type_display }}</span></td>
                            <td>{{ a.total_points }} pts</td>
                            <td>{{ a.due_date|date:"M d, Y H:i" }}</td>
                            <td class="text-end">
                                <a href="{% url 'assignments:submit' a.pk %}" class="btn btn-sm btn-primary">Submit</a>
                            </td>
                        </tr>
                        {% empty %}
                        <tr><td colspan="6" class="text-center py-4 text-muted">No assignments posted yet.</td></tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/assignments/assignment_detail.html': '''{% extends 'base.html' %}
{% block title %}{{ assignment.title }} - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <div class="row g-4">
        <div class="col-lg-8">
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-body">
                    <h3 class="fw-bold">{{ assignment.title }}</h3>
                    <p class="text-muted">{{ assignment.course.title }} ({{ assignment.course.code }})</p>
                    <hr>
                    <h5 class="fw-bold">Instructions & Specifications</h5>
                    <div class="p-3 bg-light rounded">{{ assignment.instructions_html|safe }}</div>
                </div>
            </div>
        </div>
        <div class="col-lg-4">
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-header bg-light fw-bold">Submission Status</div>
                <div class="card-body">
                    {% if submission %}
                    <div class="alert alert-success">Submitted on {{ submission.created_at|date:"M d, H:i" }}</div>
                    <p><strong>Status:</strong> {{ submission.get_status_display }}</p>
                    {% if submission.final_score %}
                    <p><strong>Score:</strong> {{ submission.final_score }} / {{ assignment.total_points }}</p>
                    {% endif %}
                    {% else %}
                    <p class="text-muted">No submission recorded for this assignment.</p>
                    <a href="{% url 'assignments:submit' assignment.pk %}" class="btn btn-primary w-100">Submit Work</a>
                    {% endif %}
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/assignments/assignment_submit.html': '''{% extends 'base.html' %}
{% block title %}Submit Assignment: {{ assignment.title }}{% endblock %}
{% block content %}
<div class="container py-4">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="card shadow-sm border-0">
                <div class="card-header bg-light fw-bold">Submit Assignment: {{ assignment.title }}</div>
                <div class="card-body">
                    <form method="post" enctype="multipart/form-data">
                        {% csrf_token %}
                        {{ form.as_p }}
                        <div class="d-flex justify-content-end gap-2 mt-4">
                            <a href="{% url 'assignments:detail' assignment.pk %}" class="btn btn-outline-secondary">Cancel</a>
                            <button type="submit" class="btn btn-primary">Submit Deliverable</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    # 4. Grading Templates
    'templates/grading/gradebook.html': '''{% extends 'base.html' %}
{% block title %}Gradebook - {{ course.code }}{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <div class="d-flex justify-content-between align-items-center mb-4">
        <div>
            <h2 class="h3 fw-bold mb-1"><i class="bi bi-calculator text-primary me-2"></i>Course Gradebook</h2>
            <p class="text-muted mb-0">{{ course.code }}: {{ course.title }}</p>
        </div>
    </div>
    <div class="card shadow-sm border-0">
        <div class="card-body p-0">
            <div class="table-responsive">
                <table class="table table-bordered align-middle mb-0 text-center">
                    <thead class="table-light">
                        <tr>
                            <th class="text-start">Student Name</th>
                            {% for cat in categories %}
                            <th>{{ cat.name }} ({{ cat.weight_percentage }}%)</th>
                            {% endfor %}
                            <th>Total %</th>
                            <th>Letter</th>
                        </tr>
                    </thead>
                    <tbody>
                        {% for enr in enrollments %}
                        <tr>
                            <td class="text-start fw-bold">{{ enr.student.get_full_name|default:enr.student.username }}</td>
                            {% for cat in categories %}
                            <td>--</td>
                            {% endfor %}
                            <td class="fw-bold">{{ enr.final_grade.total_percentage|default:"--" }}%</td>
                            <td><span class="badge bg-primary">{{ enr.final_grade.letter_grade|default:"--" }}</span></td>
                        </tr>
                        {% empty %}
                        <tr><td colspan="6" class="text-center py-4 text-muted">No enrolled students in course.</td></tr>
                        {% endfor %}
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</div>
{% endblock %}
''',

    'templates/grading/transcript.html': '''{% extends 'base.html' %}
{% block title %}Official Academic Transcript - {{ student.username }}{% endblock %}
{% block content %}
<div class="container py-4">
    <div class="card shadow-sm border-0">
        <div class="card-body p-5">
            <div class="d-flex justify-content-between border-bottom pb-3 mb-4">
                <div>
                    <h3 class="fw-bold text-primary">OFFICIAL ACADEMIC TRANSCRIPT</h3>
                    <p class="text-muted mb-0">EduTech Institute of Higher Learning &amp; Research</p>
                </div>
                <div class="text-end">
                    <p class="mb-0"><strong>Student:</strong> {{ student.get_full_name|default:student.username }}</p>
                    <p class="mb-0 text-muted">ID: #{{ student.id }}</p>
                </div>
            </div>
            <table class="table table-striped align-middle">
                <thead>
                    <tr>
                        <th>Course Code</th>
                        <th>Course Title</th>
                        <th>Credit Hours</th>
                        <th>Letter Grade</th>
                        <th>Grade Points</th>
                    </tr>
                </thead>
                <tbody>
                    {% for g in grades %}
                    <tr>
                        <td class="fw-bold">{{ g.enrollment.course.code }}</td>
                        <td>{{ g.enrollment.course.title }}</td>
                        <td>{{ g.enrollment.course.credit_hours }}</td>
                        <td><span class="badge bg-secondary">{{ g.letter_grade }}</span></td>
                        <td>{{ g.grade_points }}</td>
                    </tr>
                    {% empty %}
                    <tr><td colspan="5" class="text-center py-3 text-muted">No completed course grades recorded.</td></tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    </div>
</div>
{% endblock %}
''',

    # 5. Certificates Templates
    'templates/certificates/certificate_list.html': '''{% extends 'base.html' %}
{% block title %}My Academic Certificates & Badges - EduTech Enterprise{% endblock %}
{% block content %}
<div class="container-fluid py-4">
    <h2 class="h3 fw-bold mb-3"><i class="bi bi-award text-warning me-2"></i>My Earned Certificates &amp; Digital Badges</h2>
    <div class="row g-4">
        {% for cert in certificates %}
        <div class="col-md-6 col-lg-4">
            <div class="card shadow-sm border-0 h-100">
                <div class="card-body text-center p-4">
                    <i class="bi bi-patch-check-fill text-warning display-4 mb-3"></i>
                    <h5 class="fw-bold">{{ cert.course.title }}</h5>
                    <p class="text-muted small">Certificate #{{ cert.certificate_number }}</p>
                    <p class="text-muted small">Issued on {{ cert.issue_date|date:"F d, Y" }}</p>
                    <div class="d-grid gap-2 mt-4">
                        <a href="{% url 'certificates:download_pdf' cert.certificate_id %}" class="btn btn-primary btn-sm"><i class="bi bi-file-earmark-pdf me-1"></i>Download PDF</a>
                        <a href="{% url 'certificates:verify_code' cert.certificate_number %}" class="btn btn-outline-secondary btn-sm" target="_blank"><i class="bi bi-shield-check me-1"></i>Verify</a>
                    </div>
                </div>
            </div>
        </div>
        {% empty %}
        <div class="col-12"><div class="alert alert-info">No certificates earned yet. Complete courses to receive accredited certificates.</div></div>
        {% endfor %}
    </div>
</div>
{% endblock %}
''',

    'templates/certificates/verify_certificate.html': '''{% extends 'base.html' %}
{% block title %}Public Certificate Verification Portal - EduTech Trust{% endblock %}
{% block content %}
<div class="container py-5">
    <div class="row justify-content-center">
        <div class="col-lg-8">
            <div class="text-center mb-4">
                <i class="bi bi-shield-lock-fill text-primary display-4 mb-2"></i>
                <h2 class="fw-bold">EduTech Trust Network</h2>
                <p class="text-muted">Public Cryptographic Certificate Verification Registry</p>
            </div>
            <div class="card shadow-sm border-0 mb-4">
                <div class="card-body p-4">
                    <form method="get" class="d-flex gap-2">
                        <input type="text" name="code" class="form-control form-control-lg font-monospace" placeholder="Enter Certificate ID (e.g. CERT-2026-...)" value="{{ query }}">
                        <button type="submit" class="btn btn-primary btn-lg">Verify</button>
                    </form>
                </div>
            </div>
            {% if query %}
            {% if cert and is_valid %}
            <div class="card shadow-sm border-0 border-success border-top border-4">
                <div class="card-body p-4">
                    <div class="d-flex align-items-center mb-3">
                        <i class="bi bi-check-circle-fill text-success fs-2 me-3"></i>
                        <div>
                            <h4 class="fw-bold mb-0 text-success">Official Verified Credential</h4>
                            <small class="text-muted">Cryptographic SHA-256 Signature Confirmed</small>
                        </div>
                    </div>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item d-flex justify-content-between"><span>Recipient:</span><strong>{{ cert.student.get_full_name|default:cert.student.username }}</strong></li>
                        <li class="list-group-item d-flex justify-content-between"><span>Course / Program:</span><strong>{{ cert.course.title }} ({{ cert.course.code }})</strong></li>
                        <li class="list-group-item d-flex justify-content-between"><span>Issuing Institution:</span><strong>{{ cert.institution.name }}</strong></li>
                        <li class="list-group-item d-flex justify-content-between"><span>Issue Date:</span><strong>{{ cert.issue_date }}</strong></li>
                        <li class="list-group-item d-flex justify-content-between"><span>Certificate Number:</span><strong class="font-monospace">{{ cert.certificate_number }}</strong></li>
                    </ul>
                </div>
            </div>
            {% else %}
            <div class="alert alert-danger p-4 text-center">
                <i class="bi bi-x-circle-fill fs-2 d-block mb-2"></i>
                <h5 class="fw-bold">Certificate Not Found or Invalid</h5>
                <p class="mb-0">The provided certificate ID could not be validated in the institutional verification registry.</p>
            </div>
            {% endif %}
            {% endif %}
        </div>
    </div>
</div>
{% endblock %}
''',

    # Client-side JavaScript Controllers
    'static/js/exam_runner.js': '''/**
 * Exam Runner & Anti-Cheat Monitor Controller
 */
document.addEventListener('DOMContentLoaded', () => {
    const timerElem = document.getElementById('countdownTimer');
    const container = document.getElementById('examContainer');
    const attemptId = container ? container.dataset.attemptId : null;

    if (timerElem) {
        let seconds = parseInt(timerElem.dataset.seconds, 10) || 3600;
        const updateTimer = () => {
            if (seconds <= 0) {
                timerElem.textContent = '00:00 - TIME EXPIRED';
                timerElem.classList.add('text-danger');
                alert('Time expired! Your examination will be submitted automatically.');
                return;
            }
            const mins = Math.floor(seconds / 60);
            const secs = seconds % 60;
            timerElem.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            seconds--;
        };
        updateTimer();
        setInterval(updateTimer, 1000);
    }

    // Tab switch detector
    document.addEventListener('visibilitychange', () => {
        if (document.hidden && attemptId) {
            console.warn('[Security] Tab focus lost');
            fetch('/examinations/api/log-event/', {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
                body: JSON.stringify({attempt_id: attemptId, event_type: 'TAB_SWITCH', severity: 'MEDIUM'})
            }).catch(err => console.error(err));
        }
    });

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
''',

    'static/js/code_sandbox.js': '''/**
 * Interactive Code Sandbox Execution Controller
 */
document.addEventListener('DOMContentLoaded', () => {
    const runBtn = document.getElementById('runCodeBtn');
    const editor = document.getElementById('codeEditor');
    const consoleBox = document.getElementById('outputConsole');

    if (runBtn && editor && consoleBox) {
        runBtn.addEventListener('click', () => {
            const code = editor.value;
            consoleBox.innerHTML = '<span class="text-warning">&gt; Executing in Python sandbox...</span>';

            fetch('/assessments/api/run-code/', {
                method: 'POST',
                headers: {'Content-Type': 'application/json', 'X-CSRFToken': getCookie('csrftoken')},
                body: JSON.stringify({code: code})
            })
            .then(res => res.json())
            .then(data => {
                if (data.error) {
                    consoleBox.innerHTML = `<span class="text-danger">Error:\n${data.error}</span>`;
                } else {
                    consoleBox.innerHTML = `<span class="text-success">&gt; Execution Succeeded (${data.execution_time_ms}ms):\n</span><pre class="text-white mt-2">${data.output || '(No output)'}</pre>`;
                }
            })
            .catch(err => {
                consoleBox.innerHTML = `<span class="text-danger">&gt; Network Error: ${err}</span>`;
            });
        });
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
'''
}

for rel_path, content in FILES.items():
    filepath = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Generated UI template/script: {rel_path}")

print("All Phase 2 templates and JavaScript controllers created.")
