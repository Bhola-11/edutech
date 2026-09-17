"""
Enterprise Question Bank & Assessment Repository: Humanities & Applied Linguistics
Includes Single MCQ, Multi-Select, True/False, Short Answer, and Coding Sandbox Challenges.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Humanities & Applied Linguistics"
CURRICULUM_MODULE = "humanities_languages"

QUESTION_BANK: List[Dict[str, Any]] = [
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Critical Thinking & Formal Logic - Part 1',
        'prompt_html': '<p>In the context of <strong>Critical Thinking & Formal Logic</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Critical Thinking & Formal Logic theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Critical Thinking & Formal Logic - Part 2',
        'prompt_html': '<p>In the context of <strong>Critical Thinking & Formal Logic</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Critical Thinking & Formal Logic theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Critical Thinking & Formal Logic - Part 3',
        'prompt_html': '<p>In the context of <strong>Critical Thinking & Formal Logic</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Critical Thinking & Formal Logic theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Critical Thinking & Formal Logic - Part 4',
        'prompt_html': '<p>In the context of <strong>Critical Thinking & Formal Logic</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Critical Thinking & Formal Logic theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Critical Thinking & Formal Logic #1',
        'prompt_html': '<p>True or False: In Critical Thinking & Formal Logic, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Critical Thinking & Formal Logic.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Critical Thinking & Formal Logic #2',
        'prompt_html': '<p>True or False: In Critical Thinking & Formal Logic, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Critical Thinking & Formal Logic.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Critical Thinking & Formal Logic #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Critical Thinking & Formal Logic</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Critical Thinking & Formal Logic balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Critical Thinking & Formal Logic #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Critical Thinking & Formal Logic</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Critical Thinking & Formal Logic balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Critical Thinking & Formal Logic Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Critical Thinking & Formal Logic.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-101',
        'course_title': 'Critical Thinking & Formal Logic',
        'question_id': 'HUM-101-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Critical Thinking & Formal Logic Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Critical Thinking & Formal Logic.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of World History & Civilizations - Part 1',
        'prompt_html': '<p>In the context of <strong>World History & Civilizations</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established World History & Civilizations theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of World History & Civilizations - Part 2',
        'prompt_html': '<p>In the context of <strong>World History & Civilizations</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established World History & Civilizations theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of World History & Civilizations - Part 3',
        'prompt_html': '<p>In the context of <strong>World History & Civilizations</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established World History & Civilizations theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of World History & Civilizations - Part 4',
        'prompt_html': '<p>In the context of <strong>World History & Civilizations</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established World History & Civilizations theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in World History & Civilizations #1',
        'prompt_html': '<p>True or False: In World History & Civilizations, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for World History & Civilizations.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in World History & Civilizations #2',
        'prompt_html': '<p>True or False: In World History & Civilizations, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for World History & Civilizations.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in World History & Civilizations #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>World History & Civilizations</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in World History & Civilizations balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in World History & Civilizations #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>World History & Civilizations</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in World History & Civilizations balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: World History & Civilizations Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for World History & Civilizations.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-102',
        'course_title': 'World History & Civilizations',
        'question_id': 'HUM-102-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: World History & Civilizations Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for World History & Civilizations.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Epistemology & Theory of Knowledge - Part 1',
        'prompt_html': '<p>In the context of <strong>Epistemology & Theory of Knowledge</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Epistemology & Theory of Knowledge theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Epistemology & Theory of Knowledge - Part 2',
        'prompt_html': '<p>In the context of <strong>Epistemology & Theory of Knowledge</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Epistemology & Theory of Knowledge theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Epistemology & Theory of Knowledge - Part 3',
        'prompt_html': '<p>In the context of <strong>Epistemology & Theory of Knowledge</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Epistemology & Theory of Knowledge theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Epistemology & Theory of Knowledge - Part 4',
        'prompt_html': '<p>In the context of <strong>Epistemology & Theory of Knowledge</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Epistemology & Theory of Knowledge theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Epistemology & Theory of Knowledge #1',
        'prompt_html': '<p>True or False: In Epistemology & Theory of Knowledge, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Epistemology & Theory of Knowledge.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Epistemology & Theory of Knowledge #2',
        'prompt_html': '<p>True or False: In Epistemology & Theory of Knowledge, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Epistemology & Theory of Knowledge.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Epistemology & Theory of Knowledge #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Epistemology & Theory of Knowledge</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Epistemology & Theory of Knowledge balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Epistemology & Theory of Knowledge #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Epistemology & Theory of Knowledge</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Epistemology & Theory of Knowledge balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Epistemology & Theory of Knowledge Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Epistemology & Theory of Knowledge.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-201',
        'course_title': 'Epistemology & Theory of Knowledge',
        'question_id': 'HUM-201-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Epistemology & Theory of Knowledge Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Epistemology & Theory of Knowledge.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Moral Philosophy & Applied Ethics - Part 1',
        'prompt_html': '<p>In the context of <strong>Moral Philosophy & Applied Ethics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Moral Philosophy & Applied Ethics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Moral Philosophy & Applied Ethics - Part 2',
        'prompt_html': '<p>In the context of <strong>Moral Philosophy & Applied Ethics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Moral Philosophy & Applied Ethics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Moral Philosophy & Applied Ethics - Part 3',
        'prompt_html': '<p>In the context of <strong>Moral Philosophy & Applied Ethics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Moral Philosophy & Applied Ethics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Moral Philosophy & Applied Ethics - Part 4',
        'prompt_html': '<p>In the context of <strong>Moral Philosophy & Applied Ethics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Moral Philosophy & Applied Ethics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Moral Philosophy & Applied Ethics #1',
        'prompt_html': '<p>True or False: In Moral Philosophy & Applied Ethics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Moral Philosophy & Applied Ethics.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Moral Philosophy & Applied Ethics #2',
        'prompt_html': '<p>True or False: In Moral Philosophy & Applied Ethics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Moral Philosophy & Applied Ethics.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Moral Philosophy & Applied Ethics #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Moral Philosophy & Applied Ethics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Moral Philosophy & Applied Ethics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Moral Philosophy & Applied Ethics #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Moral Philosophy & Applied Ethics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Moral Philosophy & Applied Ethics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Moral Philosophy & Applied Ethics Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Moral Philosophy & Applied Ethics.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-202',
        'course_title': 'Moral Philosophy & Applied Ethics',
        'question_id': 'HUM-202-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Moral Philosophy & Applied Ethics Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Moral Philosophy & Applied Ethics.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Classical Literature & Narrative Theory - Part 1',
        'prompt_html': '<p>In the context of <strong>Classical Literature & Narrative Theory</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Classical Literature & Narrative Theory theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Classical Literature & Narrative Theory - Part 2',
        'prompt_html': '<p>In the context of <strong>Classical Literature & Narrative Theory</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Classical Literature & Narrative Theory theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Classical Literature & Narrative Theory - Part 3',
        'prompt_html': '<p>In the context of <strong>Classical Literature & Narrative Theory</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Classical Literature & Narrative Theory theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Classical Literature & Narrative Theory - Part 4',
        'prompt_html': '<p>In the context of <strong>Classical Literature & Narrative Theory</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Classical Literature & Narrative Theory theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Classical Literature & Narrative Theory #1',
        'prompt_html': '<p>True or False: In Classical Literature & Narrative Theory, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Classical Literature & Narrative Theory.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Classical Literature & Narrative Theory #2',
        'prompt_html': '<p>True or False: In Classical Literature & Narrative Theory, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Classical Literature & Narrative Theory.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Classical Literature & Narrative Theory #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Classical Literature & Narrative Theory</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Classical Literature & Narrative Theory balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Classical Literature & Narrative Theory #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Classical Literature & Narrative Theory</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Classical Literature & Narrative Theory balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Classical Literature & Narrative Theory Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Classical Literature & Narrative Theory.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-203',
        'course_title': 'Classical Literature & Narrative Theory',
        'question_id': 'HUM-203-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Classical Literature & Narrative Theory Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Classical Literature & Narrative Theory.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Mind & Cognitive Thought - Part 1',
        'prompt_html': '<p>In the context of <strong>Philosophy of Mind & Cognitive Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Mind & Cognitive Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Mind & Cognitive Thought - Part 2',
        'prompt_html': '<p>In the context of <strong>Philosophy of Mind & Cognitive Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Mind & Cognitive Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Mind & Cognitive Thought - Part 3',
        'prompt_html': '<p>In the context of <strong>Philosophy of Mind & Cognitive Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Mind & Cognitive Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Mind & Cognitive Thought - Part 4',
        'prompt_html': '<p>In the context of <strong>Philosophy of Mind & Cognitive Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Mind & Cognitive Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Philosophy of Mind & Cognitive Thought #1',
        'prompt_html': '<p>True or False: In Philosophy of Mind & Cognitive Thought, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Philosophy of Mind & Cognitive Thought.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Philosophy of Mind & Cognitive Thought #2',
        'prompt_html': '<p>True or False: In Philosophy of Mind & Cognitive Thought, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Philosophy of Mind & Cognitive Thought.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Philosophy of Mind & Cognitive Thought #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Philosophy of Mind & Cognitive Thought</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Philosophy of Mind & Cognitive Thought balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Philosophy of Mind & Cognitive Thought #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Philosophy of Mind & Cognitive Thought</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Philosophy of Mind & Cognitive Thought balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Philosophy of Mind & Cognitive Thought Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Philosophy of Mind & Cognitive Thought.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-301',
        'course_title': 'Philosophy of Mind & Cognitive Thought',
        'question_id': 'HUM-301-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Philosophy of Mind & Cognitive Thought Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Philosophy of Mind & Cognitive Thought.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Linguistics: Phonology & Syntax - Part 1',
        'prompt_html': '<p>In the context of <strong>Linguistics: Phonology & Syntax</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Linguistics: Phonology & Syntax theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Linguistics: Phonology & Syntax - Part 2',
        'prompt_html': '<p>In the context of <strong>Linguistics: Phonology & Syntax</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Linguistics: Phonology & Syntax theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Linguistics: Phonology & Syntax - Part 3',
        'prompt_html': '<p>In the context of <strong>Linguistics: Phonology & Syntax</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Linguistics: Phonology & Syntax theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Linguistics: Phonology & Syntax - Part 4',
        'prompt_html': '<p>In the context of <strong>Linguistics: Phonology & Syntax</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Linguistics: Phonology & Syntax theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Linguistics: Phonology & Syntax #1',
        'prompt_html': '<p>True or False: In Linguistics: Phonology & Syntax, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Linguistics: Phonology & Syntax.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Linguistics: Phonology & Syntax #2',
        'prompt_html': '<p>True or False: In Linguistics: Phonology & Syntax, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Linguistics: Phonology & Syntax.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Linguistics: Phonology & Syntax #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Linguistics: Phonology & Syntax</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Linguistics: Phonology & Syntax balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Linguistics: Phonology & Syntax #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Linguistics: Phonology & Syntax</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Linguistics: Phonology & Syntax balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Linguistics: Phonology & Syntax Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Linguistics: Phonology & Syntax.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-302',
        'course_title': 'Linguistics: Phonology & Syntax',
        'question_id': 'HUM-302-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Linguistics: Phonology & Syntax Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Linguistics: Phonology & Syntax.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renaissance & Enlightenment Thought - Part 1',
        'prompt_html': '<p>In the context of <strong>Renaissance & Enlightenment Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renaissance & Enlightenment Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renaissance & Enlightenment Thought - Part 2',
        'prompt_html': '<p>In the context of <strong>Renaissance & Enlightenment Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renaissance & Enlightenment Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renaissance & Enlightenment Thought - Part 3',
        'prompt_html': '<p>In the context of <strong>Renaissance & Enlightenment Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renaissance & Enlightenment Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renaissance & Enlightenment Thought - Part 4',
        'prompt_html': '<p>In the context of <strong>Renaissance & Enlightenment Thought</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renaissance & Enlightenment Thought theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Renaissance & Enlightenment Thought #1',
        'prompt_html': '<p>True or False: In Renaissance & Enlightenment Thought, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Renaissance & Enlightenment Thought.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Renaissance & Enlightenment Thought #2',
        'prompt_html': '<p>True or False: In Renaissance & Enlightenment Thought, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Renaissance & Enlightenment Thought.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Renaissance & Enlightenment Thought #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Renaissance & Enlightenment Thought</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Renaissance & Enlightenment Thought balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Renaissance & Enlightenment Thought #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Renaissance & Enlightenment Thought</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Renaissance & Enlightenment Thought balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Renaissance & Enlightenment Thought Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Renaissance & Enlightenment Thought.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-303',
        'course_title': 'Renaissance & Enlightenment Thought',
        'question_id': 'HUM-303-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Renaissance & Enlightenment Thought Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Renaissance & Enlightenment Thought.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Post-Modernism & Cultural Critique - Part 1',
        'prompt_html': '<p>In the context of <strong>Post-Modernism & Cultural Critique</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Post-Modernism & Cultural Critique theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Post-Modernism & Cultural Critique - Part 2',
        'prompt_html': '<p>In the context of <strong>Post-Modernism & Cultural Critique</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Post-Modernism & Cultural Critique theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Post-Modernism & Cultural Critique - Part 3',
        'prompt_html': '<p>In the context of <strong>Post-Modernism & Cultural Critique</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Post-Modernism & Cultural Critique theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Post-Modernism & Cultural Critique - Part 4',
        'prompt_html': '<p>In the context of <strong>Post-Modernism & Cultural Critique</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Post-Modernism & Cultural Critique theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Post-Modernism & Cultural Critique #1',
        'prompt_html': '<p>True or False: In Post-Modernism & Cultural Critique, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Post-Modernism & Cultural Critique.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Post-Modernism & Cultural Critique #2',
        'prompt_html': '<p>True or False: In Post-Modernism & Cultural Critique, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Post-Modernism & Cultural Critique.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Post-Modernism & Cultural Critique #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Post-Modernism & Cultural Critique</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Post-Modernism & Cultural Critique balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Post-Modernism & Cultural Critique #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Post-Modernism & Cultural Critique</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Post-Modernism & Cultural Critique balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Post-Modernism & Cultural Critique Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Post-Modernism & Cultural Critique.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-304',
        'course_title': 'Post-Modernism & Cultural Critique',
        'question_id': 'HUM-304-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Post-Modernism & Cultural Critique Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Post-Modernism & Cultural Critique.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiotics, Symbolism & Rhetoric - Part 1',
        'prompt_html': '<p>In the context of <strong>Semiotics, Symbolism & Rhetoric</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiotics, Symbolism & Rhetoric theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiotics, Symbolism & Rhetoric - Part 2',
        'prompt_html': '<p>In the context of <strong>Semiotics, Symbolism & Rhetoric</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiotics, Symbolism & Rhetoric theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiotics, Symbolism & Rhetoric - Part 3',
        'prompt_html': '<p>In the context of <strong>Semiotics, Symbolism & Rhetoric</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiotics, Symbolism & Rhetoric theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiotics, Symbolism & Rhetoric - Part 4',
        'prompt_html': '<p>In the context of <strong>Semiotics, Symbolism & Rhetoric</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiotics, Symbolism & Rhetoric theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Semiotics, Symbolism & Rhetoric #1',
        'prompt_html': '<p>True or False: In Semiotics, Symbolism & Rhetoric, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Semiotics, Symbolism & Rhetoric.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Semiotics, Symbolism & Rhetoric #2',
        'prompt_html': '<p>True or False: In Semiotics, Symbolism & Rhetoric, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Semiotics, Symbolism & Rhetoric.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Semiotics, Symbolism & Rhetoric #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Semiotics, Symbolism & Rhetoric</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Semiotics, Symbolism & Rhetoric balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Semiotics, Symbolism & Rhetoric #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Semiotics, Symbolism & Rhetoric</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Semiotics, Symbolism & Rhetoric balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Semiotics, Symbolism & Rhetoric Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Semiotics, Symbolism & Rhetoric.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-401',
        'course_title': 'Semiotics, Symbolism & Rhetoric',
        'question_id': 'HUM-401-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Semiotics, Symbolism & Rhetoric Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Semiotics, Symbolism & Rhetoric.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Comparative World Religions & Philosophy - Part 1',
        'prompt_html': '<p>In the context of <strong>Comparative World Religions & Philosophy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Comparative World Religions & Philosophy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Comparative World Religions & Philosophy - Part 2',
        'prompt_html': '<p>In the context of <strong>Comparative World Religions & Philosophy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Comparative World Religions & Philosophy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Comparative World Religions & Philosophy - Part 3',
        'prompt_html': '<p>In the context of <strong>Comparative World Religions & Philosophy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Comparative World Religions & Philosophy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Comparative World Religions & Philosophy - Part 4',
        'prompt_html': '<p>In the context of <strong>Comparative World Religions & Philosophy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Comparative World Religions & Philosophy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Comparative World Religions & Philosophy #1',
        'prompt_html': '<p>True or False: In Comparative World Religions & Philosophy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Comparative World Religions & Philosophy.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Comparative World Religions & Philosophy #2',
        'prompt_html': '<p>True or False: In Comparative World Religions & Philosophy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Comparative World Religions & Philosophy.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Comparative World Religions & Philosophy #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Comparative World Religions & Philosophy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Comparative World Religions & Philosophy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Comparative World Religions & Philosophy #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Comparative World Religions & Philosophy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Comparative World Religions & Philosophy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Comparative World Religions & Philosophy Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Comparative World Religions & Philosophy.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-402',
        'course_title': 'Comparative World Religions & Philosophy',
        'question_id': 'HUM-402-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Comparative World Religions & Philosophy Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Comparative World Religions & Philosophy.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Science & Scientific Method - Part 1',
        'prompt_html': '<p>In the context of <strong>Philosophy of Science & Scientific Method</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Science & Scientific Method theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Science & Scientific Method - Part 2',
        'prompt_html': '<p>In the context of <strong>Philosophy of Science & Scientific Method</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Science & Scientific Method theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Science & Scientific Method - Part 3',
        'prompt_html': '<p>In the context of <strong>Philosophy of Science & Scientific Method</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Science & Scientific Method theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Philosophy of Science & Scientific Method - Part 4',
        'prompt_html': '<p>In the context of <strong>Philosophy of Science & Scientific Method</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Philosophy of Science & Scientific Method theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Philosophy of Science & Scientific Method #1',
        'prompt_html': '<p>True or False: In Philosophy of Science & Scientific Method, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Philosophy of Science & Scientific Method.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Philosophy of Science & Scientific Method #2',
        'prompt_html': '<p>True or False: In Philosophy of Science & Scientific Method, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Philosophy of Science & Scientific Method.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Philosophy of Science & Scientific Method #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Philosophy of Science & Scientific Method</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Philosophy of Science & Scientific Method balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Philosophy of Science & Scientific Method #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Philosophy of Science & Scientific Method</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Philosophy of Science & Scientific Method balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Philosophy of Science & Scientific Method Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Philosophy of Science & Scientific Method.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-403',
        'course_title': 'Philosophy of Science & Scientific Method',
        'question_id': 'HUM-403-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Philosophy of Science & Scientific Method Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Philosophy of Science & Scientific Method.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aesthetics, Art Criticism & Meaning - Part 1',
        'prompt_html': '<p>In the context of <strong>Aesthetics, Art Criticism & Meaning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aesthetics, Art Criticism & Meaning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aesthetics, Art Criticism & Meaning - Part 2',
        'prompt_html': '<p>In the context of <strong>Aesthetics, Art Criticism & Meaning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aesthetics, Art Criticism & Meaning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aesthetics, Art Criticism & Meaning - Part 3',
        'prompt_html': '<p>In the context of <strong>Aesthetics, Art Criticism & Meaning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aesthetics, Art Criticism & Meaning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aesthetics, Art Criticism & Meaning - Part 4',
        'prompt_html': '<p>In the context of <strong>Aesthetics, Art Criticism & Meaning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aesthetics, Art Criticism & Meaning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Aesthetics, Art Criticism & Meaning #1',
        'prompt_html': '<p>True or False: In Aesthetics, Art Criticism & Meaning, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Aesthetics, Art Criticism & Meaning.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Aesthetics, Art Criticism & Meaning #2',
        'prompt_html': '<p>True or False: In Aesthetics, Art Criticism & Meaning, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Aesthetics, Art Criticism & Meaning.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Aesthetics, Art Criticism & Meaning #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Aesthetics, Art Criticism & Meaning</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Aesthetics, Art Criticism & Meaning balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Aesthetics, Art Criticism & Meaning #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Aesthetics, Art Criticism & Meaning</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Aesthetics, Art Criticism & Meaning balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Aesthetics, Art Criticism & Meaning Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Aesthetics, Art Criticism & Meaning.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-404',
        'course_title': 'Aesthetics, Art Criticism & Meaning',
        'question_id': 'HUM-404-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Aesthetics, Art Criticism & Meaning Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Aesthetics, Art Criticism & Meaning.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioethics, Technology & Human Future - Part 1',
        'prompt_html': '<p>In the context of <strong>Bioethics, Technology & Human Future</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioethics, Technology & Human Future theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioethics, Technology & Human Future - Part 2',
        'prompt_html': '<p>In the context of <strong>Bioethics, Technology & Human Future</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioethics, Technology & Human Future theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioethics, Technology & Human Future - Part 3',
        'prompt_html': '<p>In the context of <strong>Bioethics, Technology & Human Future</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioethics, Technology & Human Future theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioethics, Technology & Human Future - Part 4',
        'prompt_html': '<p>In the context of <strong>Bioethics, Technology & Human Future</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioethics, Technology & Human Future theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Bioethics, Technology & Human Future #1',
        'prompt_html': '<p>True or False: In Bioethics, Technology & Human Future, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Bioethics, Technology & Human Future.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Bioethics, Technology & Human Future #2',
        'prompt_html': '<p>True or False: In Bioethics, Technology & Human Future, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Bioethics, Technology & Human Future.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Bioethics, Technology & Human Future #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Bioethics, Technology & Human Future</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Bioethics, Technology & Human Future balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Bioethics, Technology & Human Future #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Bioethics, Technology & Human Future</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Bioethics, Technology & Human Future balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Bioethics, Technology & Human Future Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Bioethics, Technology & Human Future.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-405',
        'course_title': 'Bioethics, Technology & Human Future',
        'question_id': 'HUM-405-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Bioethics, Technology & Human Future Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Bioethics, Technology & Human Future.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Humanities Senior Research Thesis - Part 1',
        'prompt_html': '<p>In the context of <strong>Humanities Senior Research Thesis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Humanities Senior Research Thesis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Humanities Senior Research Thesis - Part 2',
        'prompt_html': '<p>In the context of <strong>Humanities Senior Research Thesis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Humanities Senior Research Thesis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Humanities Senior Research Thesis - Part 3',
        'prompt_html': '<p>In the context of <strong>Humanities Senior Research Thesis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Humanities Senior Research Thesis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Humanities Senior Research Thesis - Part 4',
        'prompt_html': '<p>In the context of <strong>Humanities Senior Research Thesis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Humanities Senior Research Thesis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Humanities Senior Research Thesis #1',
        'prompt_html': '<p>True or False: In Humanities Senior Research Thesis, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Humanities Senior Research Thesis.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Humanities Senior Research Thesis #2',
        'prompt_html': '<p>True or False: In Humanities Senior Research Thesis, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Humanities Senior Research Thesis.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Humanities Senior Research Thesis #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Humanities Senior Research Thesis</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Humanities Senior Research Thesis balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Humanities Senior Research Thesis #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Humanities Senior Research Thesis</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Humanities Senior Research Thesis balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Humanities Senior Research Thesis Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Humanities Senior Research Thesis.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
    {
        'course_code': 'HUM-406',
        'course_title': 'Humanities Senior Research Thesis',
        'question_id': 'HUM-406-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Humanities Senior Research Thesis Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Humanities Senior Research Thesis.</p>',
        'points': 10.0,
        'difficulty': 'HARD',
        'blooms_level': 'CREATING',
        'starter_code': 'def solve_problem(data):\n    # TODO: Implement solution\n    pass\n',
        'solution_code': 'def solve_problem(data):\n    return sum(data) if isinstance(data, list) else data * 2\n',
        'test_cases': [
            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},
            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}
        ],
        'explanation_html': '<p>Optimal solution computes linear sum in O(N) time complexity.</p>'
    },
]

def get_questions_for_course(course_code: str) -> List[Dict[str, Any]]:
    """Returns all question bank items for a specific course code."""
    code_clean = course_code.upper().strip()
    return [q for q in QUESTION_BANK if q['course_code'].upper() == code_clean]

def get_question_by_id(question_id: str) -> Dict[str, Any]:
    """Looks up single question by unique question identifier."""
    for q in QUESTION_BANK:
        if q['question_id'] == question_id:
            return q
    return {}
