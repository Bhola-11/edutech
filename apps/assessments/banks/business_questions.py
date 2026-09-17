"""
Enterprise Question Bank & Assessment Repository: Business Administration & FinTech
Includes Single MCQ, Multi-Select, True/False, Short Answer, and Coding Sandbox Challenges.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Business Administration & FinTech"
CURRICULUM_MODULE = "business_finance"

QUESTION_BANK: List[Dict[str, Any]] = [
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Principles of Financial Accounting - Part 1',
        'prompt_html': '<p>In the context of <strong>Principles of Financial Accounting</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Principles of Financial Accounting theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Principles of Financial Accounting - Part 2',
        'prompt_html': '<p>In the context of <strong>Principles of Financial Accounting</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Principles of Financial Accounting theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Principles of Financial Accounting - Part 3',
        'prompt_html': '<p>In the context of <strong>Principles of Financial Accounting</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Principles of Financial Accounting theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Principles of Financial Accounting - Part 4',
        'prompt_html': '<p>In the context of <strong>Principles of Financial Accounting</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Principles of Financial Accounting theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Principles of Financial Accounting #1',
        'prompt_html': '<p>True or False: In Principles of Financial Accounting, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Principles of Financial Accounting.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Principles of Financial Accounting #2',
        'prompt_html': '<p>True or False: In Principles of Financial Accounting, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Principles of Financial Accounting.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Principles of Financial Accounting #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Principles of Financial Accounting</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Principles of Financial Accounting balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Principles of Financial Accounting #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Principles of Financial Accounting</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Principles of Financial Accounting balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Principles of Financial Accounting Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Principles of Financial Accounting.</p>',
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
        'course_code': 'BUS-101',
        'course_title': 'Principles of Financial Accounting',
        'question_id': 'BUS-101-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Principles of Financial Accounting Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Principles of Financial Accounting.</p>',
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
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microeconomic Principles for Managers - Part 1',
        'prompt_html': '<p>In the context of <strong>Microeconomic Principles for Managers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microeconomic Principles for Managers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microeconomic Principles for Managers - Part 2',
        'prompt_html': '<p>In the context of <strong>Microeconomic Principles for Managers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microeconomic Principles for Managers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microeconomic Principles for Managers - Part 3',
        'prompt_html': '<p>In the context of <strong>Microeconomic Principles for Managers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microeconomic Principles for Managers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Microeconomic Principles for Managers - Part 4',
        'prompt_html': '<p>In the context of <strong>Microeconomic Principles for Managers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Microeconomic Principles for Managers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Microeconomic Principles for Managers #1',
        'prompt_html': '<p>True or False: In Microeconomic Principles for Managers, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Microeconomic Principles for Managers.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Microeconomic Principles for Managers #2',
        'prompt_html': '<p>True or False: In Microeconomic Principles for Managers, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Microeconomic Principles for Managers.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Microeconomic Principles for Managers #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Microeconomic Principles for Managers</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Microeconomic Principles for Managers balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Microeconomic Principles for Managers #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Microeconomic Principles for Managers</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Microeconomic Principles for Managers balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Microeconomic Principles for Managers Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Microeconomic Principles for Managers.</p>',
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
        'course_code': 'BUS-102',
        'course_title': 'Microeconomic Principles for Managers',
        'question_id': 'BUS-102-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Microeconomic Principles for Managers Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Microeconomic Principles for Managers.</p>',
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
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Managerial Cost Accounting & Control - Part 1',
        'prompt_html': '<p>In the context of <strong>Managerial Cost Accounting & Control</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Managerial Cost Accounting & Control theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Managerial Cost Accounting & Control - Part 2',
        'prompt_html': '<p>In the context of <strong>Managerial Cost Accounting & Control</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Managerial Cost Accounting & Control theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Managerial Cost Accounting & Control - Part 3',
        'prompt_html': '<p>In the context of <strong>Managerial Cost Accounting & Control</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Managerial Cost Accounting & Control theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Managerial Cost Accounting & Control - Part 4',
        'prompt_html': '<p>In the context of <strong>Managerial Cost Accounting & Control</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Managerial Cost Accounting & Control theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Managerial Cost Accounting & Control #1',
        'prompt_html': '<p>True or False: In Managerial Cost Accounting & Control, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Managerial Cost Accounting & Control.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Managerial Cost Accounting & Control #2',
        'prompt_html': '<p>True or False: In Managerial Cost Accounting & Control, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Managerial Cost Accounting & Control.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Managerial Cost Accounting & Control #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Managerial Cost Accounting & Control</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Managerial Cost Accounting & Control balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Managerial Cost Accounting & Control #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Managerial Cost Accounting & Control</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Managerial Cost Accounting & Control balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Managerial Cost Accounting & Control Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Managerial Cost Accounting & Control.</p>',
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
        'course_code': 'BUS-201',
        'course_title': 'Managerial Cost Accounting & Control',
        'question_id': 'BUS-201-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Managerial Cost Accounting & Control Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Managerial Cost Accounting & Control.</p>',
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
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Macroeconomics & Global Fiscal Policy - Part 1',
        'prompt_html': '<p>In the context of <strong>Macroeconomics & Global Fiscal Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Macroeconomics & Global Fiscal Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Macroeconomics & Global Fiscal Policy - Part 2',
        'prompt_html': '<p>In the context of <strong>Macroeconomics & Global Fiscal Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Macroeconomics & Global Fiscal Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Macroeconomics & Global Fiscal Policy - Part 3',
        'prompt_html': '<p>In the context of <strong>Macroeconomics & Global Fiscal Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Macroeconomics & Global Fiscal Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Macroeconomics & Global Fiscal Policy - Part 4',
        'prompt_html': '<p>In the context of <strong>Macroeconomics & Global Fiscal Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Macroeconomics & Global Fiscal Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Macroeconomics & Global Fiscal Policy #1',
        'prompt_html': '<p>True or False: In Macroeconomics & Global Fiscal Policy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Macroeconomics & Global Fiscal Policy.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Macroeconomics & Global Fiscal Policy #2',
        'prompt_html': '<p>True or False: In Macroeconomics & Global Fiscal Policy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Macroeconomics & Global Fiscal Policy.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Macroeconomics & Global Fiscal Policy #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Macroeconomics & Global Fiscal Policy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Macroeconomics & Global Fiscal Policy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Macroeconomics & Global Fiscal Policy #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Macroeconomics & Global Fiscal Policy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Macroeconomics & Global Fiscal Policy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Macroeconomics & Global Fiscal Policy Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Macroeconomics & Global Fiscal Policy.</p>',
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
        'course_code': 'BUS-202',
        'course_title': 'Macroeconomics & Global Fiscal Policy',
        'question_id': 'BUS-202-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Macroeconomics & Global Fiscal Policy Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Macroeconomics & Global Fiscal Policy.</p>',
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
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Corporate Financial Management & Valuation - Part 1',
        'prompt_html': '<p>In the context of <strong>Corporate Financial Management & Valuation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Corporate Financial Management & Valuation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Corporate Financial Management & Valuation - Part 2',
        'prompt_html': '<p>In the context of <strong>Corporate Financial Management & Valuation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Corporate Financial Management & Valuation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Corporate Financial Management & Valuation - Part 3',
        'prompt_html': '<p>In the context of <strong>Corporate Financial Management & Valuation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Corporate Financial Management & Valuation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Corporate Financial Management & Valuation - Part 4',
        'prompt_html': '<p>In the context of <strong>Corporate Financial Management & Valuation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Corporate Financial Management & Valuation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Corporate Financial Management & Valuation #1',
        'prompt_html': '<p>True or False: In Corporate Financial Management & Valuation, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Corporate Financial Management & Valuation.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Corporate Financial Management & Valuation #2',
        'prompt_html': '<p>True or False: In Corporate Financial Management & Valuation, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Corporate Financial Management & Valuation.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Corporate Financial Management & Valuation #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Corporate Financial Management & Valuation</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Corporate Financial Management & Valuation balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Corporate Financial Management & Valuation #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Corporate Financial Management & Valuation</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Corporate Financial Management & Valuation balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Corporate Financial Management & Valuation Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Corporate Financial Management & Valuation.</p>',
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
        'course_code': 'BUS-301',
        'course_title': 'Corporate Financial Management & Valuation',
        'question_id': 'BUS-301-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Corporate Financial Management & Valuation Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Corporate Financial Management & Valuation.</p>',
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
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Marketing Strategy & Brand Positioning - Part 1',
        'prompt_html': '<p>In the context of <strong>Marketing Strategy & Brand Positioning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Marketing Strategy & Brand Positioning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Marketing Strategy & Brand Positioning - Part 2',
        'prompt_html': '<p>In the context of <strong>Marketing Strategy & Brand Positioning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Marketing Strategy & Brand Positioning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Marketing Strategy & Brand Positioning - Part 3',
        'prompt_html': '<p>In the context of <strong>Marketing Strategy & Brand Positioning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Marketing Strategy & Brand Positioning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Marketing Strategy & Brand Positioning - Part 4',
        'prompt_html': '<p>In the context of <strong>Marketing Strategy & Brand Positioning</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Marketing Strategy & Brand Positioning theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Marketing Strategy & Brand Positioning #1',
        'prompt_html': '<p>True or False: In Marketing Strategy & Brand Positioning, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Marketing Strategy & Brand Positioning.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Marketing Strategy & Brand Positioning #2',
        'prompt_html': '<p>True or False: In Marketing Strategy & Brand Positioning, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Marketing Strategy & Brand Positioning.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Marketing Strategy & Brand Positioning #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Marketing Strategy & Brand Positioning</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Marketing Strategy & Brand Positioning balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Marketing Strategy & Brand Positioning #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Marketing Strategy & Brand Positioning</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Marketing Strategy & Brand Positioning balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Marketing Strategy & Brand Positioning Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Marketing Strategy & Brand Positioning.</p>',
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
        'course_code': 'BUS-302',
        'course_title': 'Marketing Strategy & Brand Positioning',
        'question_id': 'BUS-302-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Marketing Strategy & Brand Positioning Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Marketing Strategy & Brand Positioning.</p>',
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
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Organizational Behavior & Team Leadership - Part 1',
        'prompt_html': '<p>In the context of <strong>Organizational Behavior & Team Leadership</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Organizational Behavior & Team Leadership theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Organizational Behavior & Team Leadership - Part 2',
        'prompt_html': '<p>In the context of <strong>Organizational Behavior & Team Leadership</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Organizational Behavior & Team Leadership theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Organizational Behavior & Team Leadership - Part 3',
        'prompt_html': '<p>In the context of <strong>Organizational Behavior & Team Leadership</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Organizational Behavior & Team Leadership theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Organizational Behavior & Team Leadership - Part 4',
        'prompt_html': '<p>In the context of <strong>Organizational Behavior & Team Leadership</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Organizational Behavior & Team Leadership theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Organizational Behavior & Team Leadership #1',
        'prompt_html': '<p>True or False: In Organizational Behavior & Team Leadership, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Organizational Behavior & Team Leadership.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Organizational Behavior & Team Leadership #2',
        'prompt_html': '<p>True or False: In Organizational Behavior & Team Leadership, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Organizational Behavior & Team Leadership.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Organizational Behavior & Team Leadership #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Organizational Behavior & Team Leadership</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Organizational Behavior & Team Leadership balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Organizational Behavior & Team Leadership #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Organizational Behavior & Team Leadership</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Organizational Behavior & Team Leadership balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Organizational Behavior & Team Leadership Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Organizational Behavior & Team Leadership.</p>',
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
        'course_code': 'BUS-303',
        'course_title': 'Organizational Behavior & Team Leadership',
        'question_id': 'BUS-303-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Organizational Behavior & Team Leadership Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Organizational Behavior & Team Leadership.</p>',
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
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Operations Management & Supply Chain Logistics - Part 1',
        'prompt_html': '<p>In the context of <strong>Operations Management & Supply Chain Logistics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Operations Management & Supply Chain Logistics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Operations Management & Supply Chain Logistics - Part 2',
        'prompt_html': '<p>In the context of <strong>Operations Management & Supply Chain Logistics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Operations Management & Supply Chain Logistics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Operations Management & Supply Chain Logistics - Part 3',
        'prompt_html': '<p>In the context of <strong>Operations Management & Supply Chain Logistics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Operations Management & Supply Chain Logistics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Operations Management & Supply Chain Logistics - Part 4',
        'prompt_html': '<p>In the context of <strong>Operations Management & Supply Chain Logistics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Operations Management & Supply Chain Logistics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Operations Management & Supply Chain Logistics #1',
        'prompt_html': '<p>True or False: In Operations Management & Supply Chain Logistics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Operations Management & Supply Chain Logistics.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Operations Management & Supply Chain Logistics #2',
        'prompt_html': '<p>True or False: In Operations Management & Supply Chain Logistics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Operations Management & Supply Chain Logistics.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Operations Management & Supply Chain Logistics #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Operations Management & Supply Chain Logistics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Operations Management & Supply Chain Logistics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Operations Management & Supply Chain Logistics #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Operations Management & Supply Chain Logistics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Operations Management & Supply Chain Logistics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Operations Management & Supply Chain Logistics Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Operations Management & Supply Chain Logistics.</p>',
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
        'course_code': 'BUS-304',
        'course_title': 'Operations Management & Supply Chain Logistics',
        'question_id': 'BUS-304-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Operations Management & Supply Chain Logistics Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Operations Management & Supply Chain Logistics.</p>',
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
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Investment Analysis & Portfolio Management - Part 1',
        'prompt_html': '<p>In the context of <strong>Investment Analysis & Portfolio Management</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Investment Analysis & Portfolio Management theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Investment Analysis & Portfolio Management - Part 2',
        'prompt_html': '<p>In the context of <strong>Investment Analysis & Portfolio Management</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Investment Analysis & Portfolio Management theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Investment Analysis & Portfolio Management - Part 3',
        'prompt_html': '<p>In the context of <strong>Investment Analysis & Portfolio Management</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Investment Analysis & Portfolio Management theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Investment Analysis & Portfolio Management - Part 4',
        'prompt_html': '<p>In the context of <strong>Investment Analysis & Portfolio Management</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Investment Analysis & Portfolio Management theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Investment Analysis & Portfolio Management #1',
        'prompt_html': '<p>True or False: In Investment Analysis & Portfolio Management, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Investment Analysis & Portfolio Management.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Investment Analysis & Portfolio Management #2',
        'prompt_html': '<p>True or False: In Investment Analysis & Portfolio Management, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Investment Analysis & Portfolio Management.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Investment Analysis & Portfolio Management #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Investment Analysis & Portfolio Management</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Investment Analysis & Portfolio Management balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Investment Analysis & Portfolio Management #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Investment Analysis & Portfolio Management</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Investment Analysis & Portfolio Management balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Investment Analysis & Portfolio Management Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Investment Analysis & Portfolio Management.</p>',
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
        'course_code': 'BUS-401',
        'course_title': 'Investment Analysis & Portfolio Management',
        'question_id': 'BUS-401-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Investment Analysis & Portfolio Management Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Investment Analysis & Portfolio Management.</p>',
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
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management & Business Policy - Part 1',
        'prompt_html': '<p>In the context of <strong>Strategic Management & Business Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management & Business Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management & Business Policy - Part 2',
        'prompt_html': '<p>In the context of <strong>Strategic Management & Business Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management & Business Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management & Business Policy - Part 3',
        'prompt_html': '<p>In the context of <strong>Strategic Management & Business Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management & Business Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management & Business Policy - Part 4',
        'prompt_html': '<p>In the context of <strong>Strategic Management & Business Policy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management & Business Policy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Strategic Management & Business Policy #1',
        'prompt_html': '<p>True or False: In Strategic Management & Business Policy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Strategic Management & Business Policy.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Strategic Management & Business Policy #2',
        'prompt_html': '<p>True or False: In Strategic Management & Business Policy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Strategic Management & Business Policy.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Strategic Management & Business Policy #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Strategic Management & Business Policy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Strategic Management & Business Policy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Strategic Management & Business Policy #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Strategic Management & Business Policy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Strategic Management & Business Policy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Strategic Management & Business Policy Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Strategic Management & Business Policy.</p>',
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
        'course_code': 'BUS-402',
        'course_title': 'Strategic Management & Business Policy',
        'question_id': 'BUS-402-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Strategic Management & Business Policy Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Strategic Management & Business Policy.</p>',
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
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of International Business & Multinational Trade - Part 1',
        'prompt_html': '<p>In the context of <strong>International Business & Multinational Trade</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established International Business & Multinational Trade theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of International Business & Multinational Trade - Part 2',
        'prompt_html': '<p>In the context of <strong>International Business & Multinational Trade</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established International Business & Multinational Trade theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of International Business & Multinational Trade - Part 3',
        'prompt_html': '<p>In the context of <strong>International Business & Multinational Trade</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established International Business & Multinational Trade theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of International Business & Multinational Trade - Part 4',
        'prompt_html': '<p>In the context of <strong>International Business & Multinational Trade</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established International Business & Multinational Trade theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in International Business & Multinational Trade #1',
        'prompt_html': '<p>True or False: In International Business & Multinational Trade, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for International Business & Multinational Trade.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in International Business & Multinational Trade #2',
        'prompt_html': '<p>True or False: In International Business & Multinational Trade, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for International Business & Multinational Trade.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in International Business & Multinational Trade #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>International Business & Multinational Trade</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in International Business & Multinational Trade balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in International Business & Multinational Trade #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>International Business & Multinational Trade</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in International Business & Multinational Trade balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: International Business & Multinational Trade Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for International Business & Multinational Trade.</p>',
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
        'course_code': 'BUS-403',
        'course_title': 'International Business & Multinational Trade',
        'question_id': 'BUS-403-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: International Business & Multinational Trade Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for International Business & Multinational Trade.</p>',
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
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Venture Capital & Entrepreneurial Finance - Part 1',
        'prompt_html': '<p>In the context of <strong>Venture Capital & Entrepreneurial Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Venture Capital & Entrepreneurial Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Venture Capital & Entrepreneurial Finance - Part 2',
        'prompt_html': '<p>In the context of <strong>Venture Capital & Entrepreneurial Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Venture Capital & Entrepreneurial Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Venture Capital & Entrepreneurial Finance - Part 3',
        'prompt_html': '<p>In the context of <strong>Venture Capital & Entrepreneurial Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Venture Capital & Entrepreneurial Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Venture Capital & Entrepreneurial Finance - Part 4',
        'prompt_html': '<p>In the context of <strong>Venture Capital & Entrepreneurial Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Venture Capital & Entrepreneurial Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Venture Capital & Entrepreneurial Finance #1',
        'prompt_html': '<p>True or False: In Venture Capital & Entrepreneurial Finance, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Venture Capital & Entrepreneurial Finance.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Venture Capital & Entrepreneurial Finance #2',
        'prompt_html': '<p>True or False: In Venture Capital & Entrepreneurial Finance, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Venture Capital & Entrepreneurial Finance.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Venture Capital & Entrepreneurial Finance #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Venture Capital & Entrepreneurial Finance</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Venture Capital & Entrepreneurial Finance balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Venture Capital & Entrepreneurial Finance #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Venture Capital & Entrepreneurial Finance</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Venture Capital & Entrepreneurial Finance balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Venture Capital & Entrepreneurial Finance Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Venture Capital & Entrepreneurial Finance.</p>',
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
        'course_code': 'BUS-404',
        'course_title': 'Venture Capital & Entrepreneurial Finance',
        'question_id': 'BUS-404-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Venture Capital & Entrepreneurial Finance Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Venture Capital & Entrepreneurial Finance.</p>',
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
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Commercial Law, Ethics & Corporate Governance - Part 1',
        'prompt_html': '<p>In the context of <strong>Commercial Law, Ethics & Corporate Governance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Commercial Law, Ethics & Corporate Governance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Commercial Law, Ethics & Corporate Governance - Part 2',
        'prompt_html': '<p>In the context of <strong>Commercial Law, Ethics & Corporate Governance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Commercial Law, Ethics & Corporate Governance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Commercial Law, Ethics & Corporate Governance - Part 3',
        'prompt_html': '<p>In the context of <strong>Commercial Law, Ethics & Corporate Governance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Commercial Law, Ethics & Corporate Governance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Commercial Law, Ethics & Corporate Governance - Part 4',
        'prompt_html': '<p>In the context of <strong>Commercial Law, Ethics & Corporate Governance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Commercial Law, Ethics & Corporate Governance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Commercial Law, Ethics & Corporate Governance #1',
        'prompt_html': '<p>True or False: In Commercial Law, Ethics & Corporate Governance, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Commercial Law, Ethics & Corporate Governance.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Commercial Law, Ethics & Corporate Governance #2',
        'prompt_html': '<p>True or False: In Commercial Law, Ethics & Corporate Governance, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Commercial Law, Ethics & Corporate Governance.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Commercial Law, Ethics & Corporate Governance #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Commercial Law, Ethics & Corporate Governance</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Commercial Law, Ethics & Corporate Governance balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Commercial Law, Ethics & Corporate Governance #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Commercial Law, Ethics & Corporate Governance</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Commercial Law, Ethics & Corporate Governance balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Commercial Law, Ethics & Corporate Governance Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Commercial Law, Ethics & Corporate Governance.</p>',
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
        'course_code': 'BUS-405',
        'course_title': 'Commercial Law, Ethics & Corporate Governance',
        'question_id': 'BUS-405-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Commercial Law, Ethics & Corporate Governance Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Commercial Law, Ethics & Corporate Governance.</p>',
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
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of FinTech, Digital Assets & Algo Finance - Part 1',
        'prompt_html': '<p>In the context of <strong>FinTech, Digital Assets & Algo Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established FinTech, Digital Assets & Algo Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of FinTech, Digital Assets & Algo Finance - Part 2',
        'prompt_html': '<p>In the context of <strong>FinTech, Digital Assets & Algo Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established FinTech, Digital Assets & Algo Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of FinTech, Digital Assets & Algo Finance - Part 3',
        'prompt_html': '<p>In the context of <strong>FinTech, Digital Assets & Algo Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established FinTech, Digital Assets & Algo Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of FinTech, Digital Assets & Algo Finance - Part 4',
        'prompt_html': '<p>In the context of <strong>FinTech, Digital Assets & Algo Finance</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established FinTech, Digital Assets & Algo Finance theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in FinTech, Digital Assets & Algo Finance #1',
        'prompt_html': '<p>True or False: In FinTech, Digital Assets & Algo Finance, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for FinTech, Digital Assets & Algo Finance.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in FinTech, Digital Assets & Algo Finance #2',
        'prompt_html': '<p>True or False: In FinTech, Digital Assets & Algo Finance, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for FinTech, Digital Assets & Algo Finance.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in FinTech, Digital Assets & Algo Finance #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>FinTech, Digital Assets & Algo Finance</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in FinTech, Digital Assets & Algo Finance balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in FinTech, Digital Assets & Algo Finance #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>FinTech, Digital Assets & Algo Finance</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in FinTech, Digital Assets & Algo Finance balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: FinTech, Digital Assets & Algo Finance Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for FinTech, Digital Assets & Algo Finance.</p>',
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
        'course_code': 'BUS-406',
        'course_title': 'FinTech, Digital Assets & Algo Finance',
        'question_id': 'BUS-406-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: FinTech, Digital Assets & Algo Finance Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for FinTech, Digital Assets & Algo Finance.</p>',
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
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management Consulting Capstone - Part 1',
        'prompt_html': '<p>In the context of <strong>Strategic Management Consulting Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management Consulting Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management Consulting Capstone - Part 2',
        'prompt_html': '<p>In the context of <strong>Strategic Management Consulting Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management Consulting Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management Consulting Capstone - Part 3',
        'prompt_html': '<p>In the context of <strong>Strategic Management Consulting Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management Consulting Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Strategic Management Consulting Capstone - Part 4',
        'prompt_html': '<p>In the context of <strong>Strategic Management Consulting Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Strategic Management Consulting Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Strategic Management Consulting Capstone #1',
        'prompt_html': '<p>True or False: In Strategic Management Consulting Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Strategic Management Consulting Capstone.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Strategic Management Consulting Capstone #2',
        'prompt_html': '<p>True or False: In Strategic Management Consulting Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Strategic Management Consulting Capstone.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Strategic Management Consulting Capstone #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Strategic Management Consulting Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Strategic Management Consulting Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Strategic Management Consulting Capstone #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Strategic Management Consulting Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Strategic Management Consulting Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Strategic Management Consulting Capstone Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Strategic Management Consulting Capstone.</p>',
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
        'course_code': 'BUS-407',
        'course_title': 'Strategic Management Consulting Capstone',
        'question_id': 'BUS-407-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Strategic Management Consulting Capstone Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Strategic Management Consulting Capstone.</p>',
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
