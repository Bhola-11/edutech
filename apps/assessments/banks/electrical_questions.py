"""
Enterprise Question Bank & Assessment Repository: Electrical & Computer Engineering
Includes Single MCQ, Multi-Select, True/False, Short Answer, and Coding Sandbox Challenges.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Electrical & Computer Engineering"
CURRICULUM_MODULE = "electrical_engineering"

QUESTION_BANK: List[Dict[str, Any]] = [
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis I - Part 1',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis I</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis I theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis I - Part 2',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis I</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis I theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis I - Part 3',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis I</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis I theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis I - Part 4',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis I</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis I theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Electric Circuit Analysis I #1',
        'prompt_html': '<p>True or False: In Electric Circuit Analysis I, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Electric Circuit Analysis I.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Electric Circuit Analysis I #2',
        'prompt_html': '<p>True or False: In Electric Circuit Analysis I, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Electric Circuit Analysis I.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Electric Circuit Analysis I #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Electric Circuit Analysis I</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Electric Circuit Analysis I balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Electric Circuit Analysis I #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Electric Circuit Analysis I</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Electric Circuit Analysis I balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Electric Circuit Analysis I Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Electric Circuit Analysis I.</p>',
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
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'question_id': 'EE-101-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Electric Circuit Analysis I Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Electric Circuit Analysis I.</p>',
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
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis II - Part 1',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis II</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis II theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis II - Part 2',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis II</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis II theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis II - Part 3',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis II</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis II theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electric Circuit Analysis II - Part 4',
        'prompt_html': '<p>In the context of <strong>Electric Circuit Analysis II</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electric Circuit Analysis II theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Electric Circuit Analysis II #1',
        'prompt_html': '<p>True or False: In Electric Circuit Analysis II, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Electric Circuit Analysis II.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Electric Circuit Analysis II #2',
        'prompt_html': '<p>True or False: In Electric Circuit Analysis II, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Electric Circuit Analysis II.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Electric Circuit Analysis II #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Electric Circuit Analysis II</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Electric Circuit Analysis II balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Electric Circuit Analysis II #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Electric Circuit Analysis II</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Electric Circuit Analysis II balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Electric Circuit Analysis II Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Electric Circuit Analysis II.</p>',
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
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'question_id': 'EE-102-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Electric Circuit Analysis II Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Electric Circuit Analysis II.</p>',
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
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Logic Design & Verilog - Part 1',
        'prompt_html': '<p>In the context of <strong>Digital Logic Design & Verilog</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Logic Design & Verilog theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Logic Design & Verilog - Part 2',
        'prompt_html': '<p>In the context of <strong>Digital Logic Design & Verilog</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Logic Design & Verilog theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Logic Design & Verilog - Part 3',
        'prompt_html': '<p>In the context of <strong>Digital Logic Design & Verilog</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Logic Design & Verilog theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Logic Design & Verilog - Part 4',
        'prompt_html': '<p>In the context of <strong>Digital Logic Design & Verilog</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Logic Design & Verilog theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Digital Logic Design & Verilog #1',
        'prompt_html': '<p>True or False: In Digital Logic Design & Verilog, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Digital Logic Design & Verilog.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Digital Logic Design & Verilog #2',
        'prompt_html': '<p>True or False: In Digital Logic Design & Verilog, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Digital Logic Design & Verilog.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Digital Logic Design & Verilog #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Digital Logic Design & Verilog</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Digital Logic Design & Verilog balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Digital Logic Design & Verilog #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Digital Logic Design & Verilog</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Digital Logic Design & Verilog balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Digital Logic Design & Verilog Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Digital Logic Design & Verilog.</p>',
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
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'question_id': 'EE-201-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Digital Logic Design & Verilog Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Digital Logic Design & Verilog.</p>',
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
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Signals & Linear Systems - Part 1',
        'prompt_html': '<p>In the context of <strong>Signals & Linear Systems</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Signals & Linear Systems theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Signals & Linear Systems - Part 2',
        'prompt_html': '<p>In the context of <strong>Signals & Linear Systems</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Signals & Linear Systems theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Signals & Linear Systems - Part 3',
        'prompt_html': '<p>In the context of <strong>Signals & Linear Systems</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Signals & Linear Systems theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Signals & Linear Systems - Part 4',
        'prompt_html': '<p>In the context of <strong>Signals & Linear Systems</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Signals & Linear Systems theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Signals & Linear Systems #1',
        'prompt_html': '<p>True or False: In Signals & Linear Systems, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Signals & Linear Systems.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Signals & Linear Systems #2',
        'prompt_html': '<p>True or False: In Signals & Linear Systems, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Signals & Linear Systems.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Signals & Linear Systems #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Signals & Linear Systems</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Signals & Linear Systems balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Signals & Linear Systems #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Signals & Linear Systems</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Signals & Linear Systems balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Signals & Linear Systems Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Signals & Linear Systems.</p>',
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
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'question_id': 'EE-202-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Signals & Linear Systems Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Signals & Linear Systems.</p>',
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
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiconductor Electronics & Devices - Part 1',
        'prompt_html': '<p>In the context of <strong>Semiconductor Electronics & Devices</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiconductor Electronics & Devices theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiconductor Electronics & Devices - Part 2',
        'prompt_html': '<p>In the context of <strong>Semiconductor Electronics & Devices</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiconductor Electronics & Devices theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiconductor Electronics & Devices - Part 3',
        'prompt_html': '<p>In the context of <strong>Semiconductor Electronics & Devices</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiconductor Electronics & Devices theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Semiconductor Electronics & Devices - Part 4',
        'prompt_html': '<p>In the context of <strong>Semiconductor Electronics & Devices</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Semiconductor Electronics & Devices theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Semiconductor Electronics & Devices #1',
        'prompt_html': '<p>True or False: In Semiconductor Electronics & Devices, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Semiconductor Electronics & Devices.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Semiconductor Electronics & Devices #2',
        'prompt_html': '<p>True or False: In Semiconductor Electronics & Devices, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Semiconductor Electronics & Devices.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Semiconductor Electronics & Devices #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Semiconductor Electronics & Devices</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Semiconductor Electronics & Devices balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Semiconductor Electronics & Devices #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Semiconductor Electronics & Devices</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Semiconductor Electronics & Devices balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Semiconductor Electronics & Devices Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Semiconductor Electronics & Devices.</p>',
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
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'question_id': 'EE-301-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Semiconductor Electronics & Devices Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Semiconductor Electronics & Devices.</p>',
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
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Embedded Microcontrollers & Firmware - Part 1',
        'prompt_html': '<p>In the context of <strong>Embedded Microcontrollers & Firmware</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Embedded Microcontrollers & Firmware theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Embedded Microcontrollers & Firmware - Part 2',
        'prompt_html': '<p>In the context of <strong>Embedded Microcontrollers & Firmware</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Embedded Microcontrollers & Firmware theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Embedded Microcontrollers & Firmware - Part 3',
        'prompt_html': '<p>In the context of <strong>Embedded Microcontrollers & Firmware</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Embedded Microcontrollers & Firmware theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Embedded Microcontrollers & Firmware - Part 4',
        'prompt_html': '<p>In the context of <strong>Embedded Microcontrollers & Firmware</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Embedded Microcontrollers & Firmware theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Embedded Microcontrollers & Firmware #1',
        'prompt_html': '<p>True or False: In Embedded Microcontrollers & Firmware, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Embedded Microcontrollers & Firmware.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Embedded Microcontrollers & Firmware #2',
        'prompt_html': '<p>True or False: In Embedded Microcontrollers & Firmware, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Embedded Microcontrollers & Firmware.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Embedded Microcontrollers & Firmware #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Embedded Microcontrollers & Firmware</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Embedded Microcontrollers & Firmware balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Embedded Microcontrollers & Firmware #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Embedded Microcontrollers & Firmware</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Embedded Microcontrollers & Firmware balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Embedded Microcontrollers & Firmware Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Embedded Microcontrollers & Firmware.</p>',
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
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'question_id': 'EE-302-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Embedded Microcontrollers & Firmware Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Embedded Microcontrollers & Firmware.</p>',
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
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electromagnetic Fields & Waveguides - Part 1',
        'prompt_html': '<p>In the context of <strong>Electromagnetic Fields & Waveguides</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electromagnetic Fields & Waveguides theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electromagnetic Fields & Waveguides - Part 2',
        'prompt_html': '<p>In the context of <strong>Electromagnetic Fields & Waveguides</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electromagnetic Fields & Waveguides theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electromagnetic Fields & Waveguides - Part 3',
        'prompt_html': '<p>In the context of <strong>Electromagnetic Fields & Waveguides</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electromagnetic Fields & Waveguides theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Electromagnetic Fields & Waveguides - Part 4',
        'prompt_html': '<p>In the context of <strong>Electromagnetic Fields & Waveguides</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Electromagnetic Fields & Waveguides theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Electromagnetic Fields & Waveguides #1',
        'prompt_html': '<p>True or False: In Electromagnetic Fields & Waveguides, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Electromagnetic Fields & Waveguides.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Electromagnetic Fields & Waveguides #2',
        'prompt_html': '<p>True or False: In Electromagnetic Fields & Waveguides, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Electromagnetic Fields & Waveguides.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Electromagnetic Fields & Waveguides #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Electromagnetic Fields & Waveguides</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Electromagnetic Fields & Waveguides balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Electromagnetic Fields & Waveguides #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Electromagnetic Fields & Waveguides</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Electromagnetic Fields & Waveguides balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Electromagnetic Fields & Waveguides Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Electromagnetic Fields & Waveguides.</p>',
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
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'question_id': 'EE-303-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Electromagnetic Fields & Waveguides Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Electromagnetic Fields & Waveguides.</p>',
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
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Feedback Control Systems Engineering - Part 1',
        'prompt_html': '<p>In the context of <strong>Feedback Control Systems Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Feedback Control Systems Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Feedback Control Systems Engineering - Part 2',
        'prompt_html': '<p>In the context of <strong>Feedback Control Systems Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Feedback Control Systems Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Feedback Control Systems Engineering - Part 3',
        'prompt_html': '<p>In the context of <strong>Feedback Control Systems Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Feedback Control Systems Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Feedback Control Systems Engineering - Part 4',
        'prompt_html': '<p>In the context of <strong>Feedback Control Systems Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Feedback Control Systems Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Feedback Control Systems Engineering #1',
        'prompt_html': '<p>True or False: In Feedback Control Systems Engineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Feedback Control Systems Engineering.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Feedback Control Systems Engineering #2',
        'prompt_html': '<p>True or False: In Feedback Control Systems Engineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Feedback Control Systems Engineering.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Feedback Control Systems Engineering #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Feedback Control Systems Engineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Feedback Control Systems Engineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Feedback Control Systems Engineering #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Feedback Control Systems Engineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Feedback Control Systems Engineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Feedback Control Systems Engineering Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Feedback Control Systems Engineering.</p>',
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
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'question_id': 'EE-401-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Feedback Control Systems Engineering Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Feedback Control Systems Engineering.</p>',
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
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Power Electronics & Inverters - Part 1',
        'prompt_html': '<p>In the context of <strong>Power Electronics & Inverters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Power Electronics & Inverters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Power Electronics & Inverters - Part 2',
        'prompt_html': '<p>In the context of <strong>Power Electronics & Inverters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Power Electronics & Inverters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Power Electronics & Inverters - Part 3',
        'prompt_html': '<p>In the context of <strong>Power Electronics & Inverters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Power Electronics & Inverters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Power Electronics & Inverters - Part 4',
        'prompt_html': '<p>In the context of <strong>Power Electronics & Inverters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Power Electronics & Inverters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Power Electronics & Inverters #1',
        'prompt_html': '<p>True or False: In Power Electronics & Inverters, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Power Electronics & Inverters.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Power Electronics & Inverters #2',
        'prompt_html': '<p>True or False: In Power Electronics & Inverters, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Power Electronics & Inverters.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Power Electronics & Inverters #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Power Electronics & Inverters</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Power Electronics & Inverters balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Power Electronics & Inverters #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Power Electronics & Inverters</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Power Electronics & Inverters balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Power Electronics & Inverters Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Power Electronics & Inverters.</p>',
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
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'question_id': 'EE-402-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Power Electronics & Inverters Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Power Electronics & Inverters.</p>',
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
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Analog CMOS Integrated Circuit Design - Part 1',
        'prompt_html': '<p>In the context of <strong>Analog CMOS Integrated Circuit Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Analog CMOS Integrated Circuit Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Analog CMOS Integrated Circuit Design - Part 2',
        'prompt_html': '<p>In the context of <strong>Analog CMOS Integrated Circuit Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Analog CMOS Integrated Circuit Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Analog CMOS Integrated Circuit Design - Part 3',
        'prompt_html': '<p>In the context of <strong>Analog CMOS Integrated Circuit Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Analog CMOS Integrated Circuit Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Analog CMOS Integrated Circuit Design - Part 4',
        'prompt_html': '<p>In the context of <strong>Analog CMOS Integrated Circuit Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Analog CMOS Integrated Circuit Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Analog CMOS Integrated Circuit Design #1',
        'prompt_html': '<p>True or False: In Analog CMOS Integrated Circuit Design, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Analog CMOS Integrated Circuit Design.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Analog CMOS Integrated Circuit Design #2',
        'prompt_html': '<p>True or False: In Analog CMOS Integrated Circuit Design, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Analog CMOS Integrated Circuit Design.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Analog CMOS Integrated Circuit Design #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Analog CMOS Integrated Circuit Design</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Analog CMOS Integrated Circuit Design balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Analog CMOS Integrated Circuit Design #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Analog CMOS Integrated Circuit Design</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Analog CMOS Integrated Circuit Design balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Analog CMOS Integrated Circuit Design Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Analog CMOS Integrated Circuit Design.</p>',
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
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'question_id': 'EE-403-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Analog CMOS Integrated Circuit Design Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Analog CMOS Integrated Circuit Design.</p>',
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
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Signal Processing (DSP) & Filters - Part 1',
        'prompt_html': '<p>In the context of <strong>Digital Signal Processing (DSP) & Filters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Signal Processing (DSP) & Filters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Signal Processing (DSP) & Filters - Part 2',
        'prompt_html': '<p>In the context of <strong>Digital Signal Processing (DSP) & Filters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Signal Processing (DSP) & Filters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Signal Processing (DSP) & Filters - Part 3',
        'prompt_html': '<p>In the context of <strong>Digital Signal Processing (DSP) & Filters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Signal Processing (DSP) & Filters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Digital Signal Processing (DSP) & Filters - Part 4',
        'prompt_html': '<p>In the context of <strong>Digital Signal Processing (DSP) & Filters</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Digital Signal Processing (DSP) & Filters theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Digital Signal Processing (DSP) & Filters #1',
        'prompt_html': '<p>True or False: In Digital Signal Processing (DSP) & Filters, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Digital Signal Processing (DSP) & Filters.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Digital Signal Processing (DSP) & Filters #2',
        'prompt_html': '<p>True or False: In Digital Signal Processing (DSP) & Filters, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Digital Signal Processing (DSP) & Filters.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Digital Signal Processing (DSP) & Filters #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Digital Signal Processing (DSP) & Filters</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Digital Signal Processing (DSP) & Filters balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Digital Signal Processing (DSP) & Filters #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Digital Signal Processing (DSP) & Filters</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Digital Signal Processing (DSP) & Filters balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Digital Signal Processing (DSP) & Filters Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Digital Signal Processing (DSP) & Filters.</p>',
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
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'question_id': 'EE-404-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Digital Signal Processing (DSP) & Filters Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Digital Signal Processing (DSP) & Filters.</p>',
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
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microwave Engineering & Antennas - Part 1',
        'prompt_html': '<p>In the context of <strong>Microwave Engineering & Antennas</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microwave Engineering & Antennas theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microwave Engineering & Antennas - Part 2',
        'prompt_html': '<p>In the context of <strong>Microwave Engineering & Antennas</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microwave Engineering & Antennas theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microwave Engineering & Antennas - Part 3',
        'prompt_html': '<p>In the context of <strong>Microwave Engineering & Antennas</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microwave Engineering & Antennas theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microwave Engineering & Antennas - Part 4',
        'prompt_html': '<p>In the context of <strong>Microwave Engineering & Antennas</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microwave Engineering & Antennas theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Microwave Engineering & Antennas #1',
        'prompt_html': '<p>True or False: In Microwave Engineering & Antennas, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Microwave Engineering & Antennas.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Microwave Engineering & Antennas #2',
        'prompt_html': '<p>True or False: In Microwave Engineering & Antennas, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Microwave Engineering & Antennas.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Microwave Engineering & Antennas #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Microwave Engineering & Antennas</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Microwave Engineering & Antennas balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Microwave Engineering & Antennas #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Microwave Engineering & Antennas</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Microwave Engineering & Antennas balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Microwave Engineering & Antennas Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Microwave Engineering & Antennas.</p>',
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
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'question_id': 'EE-405-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Microwave Engineering & Antennas Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Microwave Engineering & Antennas.</p>',
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
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renewable Energy Systems & Smart Grids - Part 1',
        'prompt_html': '<p>In the context of <strong>Renewable Energy Systems & Smart Grids</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renewable Energy Systems & Smart Grids theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renewable Energy Systems & Smart Grids - Part 2',
        'prompt_html': '<p>In the context of <strong>Renewable Energy Systems & Smart Grids</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renewable Energy Systems & Smart Grids theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renewable Energy Systems & Smart Grids - Part 3',
        'prompt_html': '<p>In the context of <strong>Renewable Energy Systems & Smart Grids</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renewable Energy Systems & Smart Grids theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Renewable Energy Systems & Smart Grids - Part 4',
        'prompt_html': '<p>In the context of <strong>Renewable Energy Systems & Smart Grids</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Renewable Energy Systems & Smart Grids theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Renewable Energy Systems & Smart Grids #1',
        'prompt_html': '<p>True or False: In Renewable Energy Systems & Smart Grids, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Renewable Energy Systems & Smart Grids.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Renewable Energy Systems & Smart Grids #2',
        'prompt_html': '<p>True or False: In Renewable Energy Systems & Smart Grids, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Renewable Energy Systems & Smart Grids.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Renewable Energy Systems & Smart Grids #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Renewable Energy Systems & Smart Grids</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Renewable Energy Systems & Smart Grids balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Renewable Energy Systems & Smart Grids #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Renewable Energy Systems & Smart Grids</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Renewable Energy Systems & Smart Grids balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Renewable Energy Systems & Smart Grids Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Renewable Energy Systems & Smart Grids.</p>',
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
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'question_id': 'EE-406-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Renewable Energy Systems & Smart Grids Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Renewable Energy Systems & Smart Grids.</p>',
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
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of VLSI Physical Design & Layout - Part 1',
        'prompt_html': '<p>In the context of <strong>VLSI Physical Design & Layout</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established VLSI Physical Design & Layout theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of VLSI Physical Design & Layout - Part 2',
        'prompt_html': '<p>In the context of <strong>VLSI Physical Design & Layout</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established VLSI Physical Design & Layout theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of VLSI Physical Design & Layout - Part 3',
        'prompt_html': '<p>In the context of <strong>VLSI Physical Design & Layout</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established VLSI Physical Design & Layout theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of VLSI Physical Design & Layout - Part 4',
        'prompt_html': '<p>In the context of <strong>VLSI Physical Design & Layout</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established VLSI Physical Design & Layout theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in VLSI Physical Design & Layout #1',
        'prompt_html': '<p>True or False: In VLSI Physical Design & Layout, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for VLSI Physical Design & Layout.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in VLSI Physical Design & Layout #2',
        'prompt_html': '<p>True or False: In VLSI Physical Design & Layout, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for VLSI Physical Design & Layout.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in VLSI Physical Design & Layout #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>VLSI Physical Design & Layout</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in VLSI Physical Design & Layout balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in VLSI Physical Design & Layout #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>VLSI Physical Design & Layout</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in VLSI Physical Design & Layout balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: VLSI Physical Design & Layout Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for VLSI Physical Design & Layout.</p>',
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
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'question_id': 'EE-407-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: VLSI Physical Design & Layout Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for VLSI Physical Design & Layout.</p>',
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
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Electrical Engineering Capstone - Part 1',
        'prompt_html': '<p>In the context of <strong>Senior Electrical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Electrical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Electrical Engineering Capstone - Part 2',
        'prompt_html': '<p>In the context of <strong>Senior Electrical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Electrical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Electrical Engineering Capstone - Part 3',
        'prompt_html': '<p>In the context of <strong>Senior Electrical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Electrical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Electrical Engineering Capstone - Part 4',
        'prompt_html': '<p>In the context of <strong>Senior Electrical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Electrical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Senior Electrical Engineering Capstone #1',
        'prompt_html': '<p>True or False: In Senior Electrical Engineering Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Senior Electrical Engineering Capstone.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Senior Electrical Engineering Capstone #2',
        'prompt_html': '<p>True or False: In Senior Electrical Engineering Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Senior Electrical Engineering Capstone.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Senior Electrical Engineering Capstone #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Senior Electrical Engineering Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Senior Electrical Engineering Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Senior Electrical Engineering Capstone #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Senior Electrical Engineering Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Senior Electrical Engineering Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Senior Electrical Engineering Capstone Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Senior Electrical Engineering Capstone.</p>',
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
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'question_id': 'EE-408-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Senior Electrical Engineering Capstone Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Senior Electrical Engineering Capstone.</p>',
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
