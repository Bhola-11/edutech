"""
Enterprise Question Bank & Assessment Repository: Mechanical & Aerospace Engineering
Includes Single MCQ, Multi-Select, True/False, Short Answer, and Coding Sandbox Challenges.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Mechanical & Aerospace Engineering"
CURRICULUM_MODULE = "mechanical_engineering"

QUESTION_BANK: List[Dict[str, Any]] = [
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Statics & Vector Equilibrium - Part 1',
        'prompt_html': '<p>In the context of <strong>Engineering Statics & Vector Equilibrium</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Statics & Vector Equilibrium theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Statics & Vector Equilibrium - Part 2',
        'prompt_html': '<p>In the context of <strong>Engineering Statics & Vector Equilibrium</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Statics & Vector Equilibrium theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Statics & Vector Equilibrium - Part 3',
        'prompt_html': '<p>In the context of <strong>Engineering Statics & Vector Equilibrium</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Statics & Vector Equilibrium theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Statics & Vector Equilibrium - Part 4',
        'prompt_html': '<p>In the context of <strong>Engineering Statics & Vector Equilibrium</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Statics & Vector Equilibrium theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Engineering Statics & Vector Equilibrium #1',
        'prompt_html': '<p>True or False: In Engineering Statics & Vector Equilibrium, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Engineering Statics & Vector Equilibrium.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Engineering Statics & Vector Equilibrium #2',
        'prompt_html': '<p>True or False: In Engineering Statics & Vector Equilibrium, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Engineering Statics & Vector Equilibrium.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Engineering Statics & Vector Equilibrium #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Engineering Statics & Vector Equilibrium</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Engineering Statics & Vector Equilibrium balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Engineering Statics & Vector Equilibrium #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Engineering Statics & Vector Equilibrium</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Engineering Statics & Vector Equilibrium balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Engineering Statics & Vector Equilibrium Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Engineering Statics & Vector Equilibrium.</p>',
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
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'question_id': 'ME-101-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Engineering Statics & Vector Equilibrium Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Engineering Statics & Vector Equilibrium.</p>',
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
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Dynamics & Kinematics - Part 1',
        'prompt_html': '<p>In the context of <strong>Engineering Dynamics & Kinematics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Dynamics & Kinematics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Dynamics & Kinematics - Part 2',
        'prompt_html': '<p>In the context of <strong>Engineering Dynamics & Kinematics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Dynamics & Kinematics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Dynamics & Kinematics - Part 3',
        'prompt_html': '<p>In the context of <strong>Engineering Dynamics & Kinematics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Dynamics & Kinematics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Engineering Dynamics & Kinematics - Part 4',
        'prompt_html': '<p>In the context of <strong>Engineering Dynamics & Kinematics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Engineering Dynamics & Kinematics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Engineering Dynamics & Kinematics #1',
        'prompt_html': '<p>True or False: In Engineering Dynamics & Kinematics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Engineering Dynamics & Kinematics.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Engineering Dynamics & Kinematics #2',
        'prompt_html': '<p>True or False: In Engineering Dynamics & Kinematics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Engineering Dynamics & Kinematics.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Engineering Dynamics & Kinematics #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Engineering Dynamics & Kinematics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Engineering Dynamics & Kinematics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Engineering Dynamics & Kinematics #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Engineering Dynamics & Kinematics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Engineering Dynamics & Kinematics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Engineering Dynamics & Kinematics Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Engineering Dynamics & Kinematics.</p>',
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
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'question_id': 'ME-102-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Engineering Dynamics & Kinematics Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Engineering Dynamics & Kinematics.</p>',
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
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanics of Deformable Materials - Part 1',
        'prompt_html': '<p>In the context of <strong>Mechanics of Deformable Materials</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanics of Deformable Materials theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanics of Deformable Materials - Part 2',
        'prompt_html': '<p>In the context of <strong>Mechanics of Deformable Materials</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanics of Deformable Materials theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanics of Deformable Materials - Part 3',
        'prompt_html': '<p>In the context of <strong>Mechanics of Deformable Materials</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanics of Deformable Materials theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanics of Deformable Materials - Part 4',
        'prompt_html': '<p>In the context of <strong>Mechanics of Deformable Materials</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanics of Deformable Materials theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechanics of Deformable Materials #1',
        'prompt_html': '<p>True or False: In Mechanics of Deformable Materials, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechanics of Deformable Materials.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechanics of Deformable Materials #2',
        'prompt_html': '<p>True or False: In Mechanics of Deformable Materials, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechanics of Deformable Materials.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechanics of Deformable Materials #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechanics of Deformable Materials</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechanics of Deformable Materials balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechanics of Deformable Materials #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechanics of Deformable Materials</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechanics of Deformable Materials balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechanics of Deformable Materials Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Mechanics of Deformable Materials.</p>',
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
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'question_id': 'ME-201-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechanics of Deformable Materials Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Mechanics of Deformable Materials.</p>',
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
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Thermodynamics Principles & Cycles - Part 1',
        'prompt_html': '<p>In the context of <strong>Thermodynamics Principles & Cycles</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Thermodynamics Principles & Cycles theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Thermodynamics Principles & Cycles - Part 2',
        'prompt_html': '<p>In the context of <strong>Thermodynamics Principles & Cycles</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Thermodynamics Principles & Cycles theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Thermodynamics Principles & Cycles - Part 3',
        'prompt_html': '<p>In the context of <strong>Thermodynamics Principles & Cycles</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Thermodynamics Principles & Cycles theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Thermodynamics Principles & Cycles - Part 4',
        'prompt_html': '<p>In the context of <strong>Thermodynamics Principles & Cycles</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Thermodynamics Principles & Cycles theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Thermodynamics Principles & Cycles #1',
        'prompt_html': '<p>True or False: In Thermodynamics Principles & Cycles, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Thermodynamics Principles & Cycles.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Thermodynamics Principles & Cycles #2',
        'prompt_html': '<p>True or False: In Thermodynamics Principles & Cycles, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Thermodynamics Principles & Cycles.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Thermodynamics Principles & Cycles #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Thermodynamics Principles & Cycles</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Thermodynamics Principles & Cycles balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Thermodynamics Principles & Cycles #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Thermodynamics Principles & Cycles</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Thermodynamics Principles & Cycles balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Thermodynamics Principles & Cycles Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Thermodynamics Principles & Cycles.</p>',
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
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'question_id': 'ME-202-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Thermodynamics Principles & Cycles Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Thermodynamics Principles & Cycles.</p>',
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
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Computer-Aided Design (CAD) & SolidWorks - Part 1',
        'prompt_html': '<p>In the context of <strong>Computer-Aided Design (CAD) & SolidWorks</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Computer-Aided Design (CAD) & SolidWorks theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Computer-Aided Design (CAD) & SolidWorks - Part 2',
        'prompt_html': '<p>In the context of <strong>Computer-Aided Design (CAD) & SolidWorks</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Computer-Aided Design (CAD) & SolidWorks theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Computer-Aided Design (CAD) & SolidWorks - Part 3',
        'prompt_html': '<p>In the context of <strong>Computer-Aided Design (CAD) & SolidWorks</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Computer-Aided Design (CAD) & SolidWorks theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Computer-Aided Design (CAD) & SolidWorks - Part 4',
        'prompt_html': '<p>In the context of <strong>Computer-Aided Design (CAD) & SolidWorks</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Computer-Aided Design (CAD) & SolidWorks theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Computer-Aided Design (CAD) & SolidWorks #1',
        'prompt_html': '<p>True or False: In Computer-Aided Design (CAD) & SolidWorks, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Computer-Aided Design (CAD) & SolidWorks.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Computer-Aided Design (CAD) & SolidWorks #2',
        'prompt_html': '<p>True or False: In Computer-Aided Design (CAD) & SolidWorks, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Computer-Aided Design (CAD) & SolidWorks.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Computer-Aided Design (CAD) & SolidWorks #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Computer-Aided Design (CAD) & SolidWorks</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Computer-Aided Design (CAD) & SolidWorks balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Computer-Aided Design (CAD) & SolidWorks #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Computer-Aided Design (CAD) & SolidWorks</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Computer-Aided Design (CAD) & SolidWorks balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Computer-Aided Design (CAD) & SolidWorks Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Computer-Aided Design (CAD) & SolidWorks.</p>',
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
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'question_id': 'ME-203-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Computer-Aided Design (CAD) & SolidWorks Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Computer-Aided Design (CAD) & SolidWorks.</p>',
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
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Fluid Mechanics & Boundary Layers - Part 1',
        'prompt_html': '<p>In the context of <strong>Fluid Mechanics & Boundary Layers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Fluid Mechanics & Boundary Layers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Fluid Mechanics & Boundary Layers - Part 2',
        'prompt_html': '<p>In the context of <strong>Fluid Mechanics & Boundary Layers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Fluid Mechanics & Boundary Layers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Fluid Mechanics & Boundary Layers - Part 3',
        'prompt_html': '<p>In the context of <strong>Fluid Mechanics & Boundary Layers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Fluid Mechanics & Boundary Layers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Fluid Mechanics & Boundary Layers - Part 4',
        'prompt_html': '<p>In the context of <strong>Fluid Mechanics & Boundary Layers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Fluid Mechanics & Boundary Layers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Fluid Mechanics & Boundary Layers #1',
        'prompt_html': '<p>True or False: In Fluid Mechanics & Boundary Layers, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Fluid Mechanics & Boundary Layers.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Fluid Mechanics & Boundary Layers #2',
        'prompt_html': '<p>True or False: In Fluid Mechanics & Boundary Layers, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Fluid Mechanics & Boundary Layers.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Fluid Mechanics & Boundary Layers #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Fluid Mechanics & Boundary Layers</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Fluid Mechanics & Boundary Layers balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Fluid Mechanics & Boundary Layers #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Fluid Mechanics & Boundary Layers</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Fluid Mechanics & Boundary Layers balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Fluid Mechanics & Boundary Layers Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Fluid Mechanics & Boundary Layers.</p>',
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
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'question_id': 'ME-301-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Fluid Mechanics & Boundary Layers Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Fluid Mechanics & Boundary Layers.</p>',
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
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Heat Transfer: Conduction & Radiation - Part 1',
        'prompt_html': '<p>In the context of <strong>Heat Transfer: Conduction & Radiation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Heat Transfer: Conduction & Radiation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Heat Transfer: Conduction & Radiation - Part 2',
        'prompt_html': '<p>In the context of <strong>Heat Transfer: Conduction & Radiation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Heat Transfer: Conduction & Radiation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Heat Transfer: Conduction & Radiation - Part 3',
        'prompt_html': '<p>In the context of <strong>Heat Transfer: Conduction & Radiation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Heat Transfer: Conduction & Radiation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Heat Transfer: Conduction & Radiation - Part 4',
        'prompt_html': '<p>In the context of <strong>Heat Transfer: Conduction & Radiation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Heat Transfer: Conduction & Radiation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Heat Transfer: Conduction & Radiation #1',
        'prompt_html': '<p>True or False: In Heat Transfer: Conduction & Radiation, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Heat Transfer: Conduction & Radiation.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Heat Transfer: Conduction & Radiation #2',
        'prompt_html': '<p>True or False: In Heat Transfer: Conduction & Radiation, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Heat Transfer: Conduction & Radiation.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Heat Transfer: Conduction & Radiation #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Heat Transfer: Conduction & Radiation</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Heat Transfer: Conduction & Radiation balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Heat Transfer: Conduction & Radiation #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Heat Transfer: Conduction & Radiation</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Heat Transfer: Conduction & Radiation balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Heat Transfer: Conduction & Radiation Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Heat Transfer: Conduction & Radiation.</p>',
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
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'question_id': 'ME-302-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Heat Transfer: Conduction & Radiation Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Heat Transfer: Conduction & Radiation.</p>',
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
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Element Design & Fatigue - Part 1',
        'prompt_html': '<p>In the context of <strong>Mechanical Element Design & Fatigue</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Element Design & Fatigue theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Element Design & Fatigue - Part 2',
        'prompt_html': '<p>In the context of <strong>Mechanical Element Design & Fatigue</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Element Design & Fatigue theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Element Design & Fatigue - Part 3',
        'prompt_html': '<p>In the context of <strong>Mechanical Element Design & Fatigue</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Element Design & Fatigue theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Element Design & Fatigue - Part 4',
        'prompt_html': '<p>In the context of <strong>Mechanical Element Design & Fatigue</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Element Design & Fatigue theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechanical Element Design & Fatigue #1',
        'prompt_html': '<p>True or False: In Mechanical Element Design & Fatigue, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechanical Element Design & Fatigue.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechanical Element Design & Fatigue #2',
        'prompt_html': '<p>True or False: In Mechanical Element Design & Fatigue, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechanical Element Design & Fatigue.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechanical Element Design & Fatigue #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechanical Element Design & Fatigue</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechanical Element Design & Fatigue balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechanical Element Design & Fatigue #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechanical Element Design & Fatigue</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechanical Element Design & Fatigue balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechanical Element Design & Fatigue Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Mechanical Element Design & Fatigue.</p>',
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
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'question_id': 'ME-303-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechanical Element Design & Fatigue Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Mechanical Element Design & Fatigue.</p>',
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
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Vibrations & Modal Analysis - Part 1',
        'prompt_html': '<p>In the context of <strong>Mechanical Vibrations & Modal Analysis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Vibrations & Modal Analysis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Vibrations & Modal Analysis - Part 2',
        'prompt_html': '<p>In the context of <strong>Mechanical Vibrations & Modal Analysis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Vibrations & Modal Analysis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Vibrations & Modal Analysis - Part 3',
        'prompt_html': '<p>In the context of <strong>Mechanical Vibrations & Modal Analysis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Vibrations & Modal Analysis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechanical Vibrations & Modal Analysis - Part 4',
        'prompt_html': '<p>In the context of <strong>Mechanical Vibrations & Modal Analysis</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechanical Vibrations & Modal Analysis theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechanical Vibrations & Modal Analysis #1',
        'prompt_html': '<p>True or False: In Mechanical Vibrations & Modal Analysis, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechanical Vibrations & Modal Analysis.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechanical Vibrations & Modal Analysis #2',
        'prompt_html': '<p>True or False: In Mechanical Vibrations & Modal Analysis, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechanical Vibrations & Modal Analysis.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechanical Vibrations & Modal Analysis #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechanical Vibrations & Modal Analysis</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechanical Vibrations & Modal Analysis balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechanical Vibrations & Modal Analysis #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechanical Vibrations & Modal Analysis</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechanical Vibrations & Modal Analysis balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechanical Vibrations & Modal Analysis Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Mechanical Vibrations & Modal Analysis.</p>',
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
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'question_id': 'ME-401-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechanical Vibrations & Modal Analysis Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Mechanical Vibrations & Modal Analysis.</p>',
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
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Finite Element Analysis (FEA) Simulation - Part 1',
        'prompt_html': '<p>In the context of <strong>Finite Element Analysis (FEA) Simulation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Finite Element Analysis (FEA) Simulation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Finite Element Analysis (FEA) Simulation - Part 2',
        'prompt_html': '<p>In the context of <strong>Finite Element Analysis (FEA) Simulation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Finite Element Analysis (FEA) Simulation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Finite Element Analysis (FEA) Simulation - Part 3',
        'prompt_html': '<p>In the context of <strong>Finite Element Analysis (FEA) Simulation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Finite Element Analysis (FEA) Simulation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Finite Element Analysis (FEA) Simulation - Part 4',
        'prompt_html': '<p>In the context of <strong>Finite Element Analysis (FEA) Simulation</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Finite Element Analysis (FEA) Simulation theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Finite Element Analysis (FEA) Simulation #1',
        'prompt_html': '<p>True or False: In Finite Element Analysis (FEA) Simulation, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Finite Element Analysis (FEA) Simulation.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Finite Element Analysis (FEA) Simulation #2',
        'prompt_html': '<p>True or False: In Finite Element Analysis (FEA) Simulation, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Finite Element Analysis (FEA) Simulation.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Finite Element Analysis (FEA) Simulation #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Finite Element Analysis (FEA) Simulation</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Finite Element Analysis (FEA) Simulation balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Finite Element Analysis (FEA) Simulation #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Finite Element Analysis (FEA) Simulation</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Finite Element Analysis (FEA) Simulation balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Finite Element Analysis (FEA) Simulation Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Finite Element Analysis (FEA) Simulation.</p>',
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
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'question_id': 'ME-402-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Finite Element Analysis (FEA) Simulation Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Finite Element Analysis (FEA) Simulation.</p>',
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
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Manufacturing Processes & Metallurgy - Part 1',
        'prompt_html': '<p>In the context of <strong>Manufacturing Processes & Metallurgy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Manufacturing Processes & Metallurgy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Manufacturing Processes & Metallurgy - Part 2',
        'prompt_html': '<p>In the context of <strong>Manufacturing Processes & Metallurgy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Manufacturing Processes & Metallurgy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Manufacturing Processes & Metallurgy - Part 3',
        'prompt_html': '<p>In the context of <strong>Manufacturing Processes & Metallurgy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Manufacturing Processes & Metallurgy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Manufacturing Processes & Metallurgy - Part 4',
        'prompt_html': '<p>In the context of <strong>Manufacturing Processes & Metallurgy</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Manufacturing Processes & Metallurgy theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Manufacturing Processes & Metallurgy #1',
        'prompt_html': '<p>True or False: In Manufacturing Processes & Metallurgy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Manufacturing Processes & Metallurgy.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Manufacturing Processes & Metallurgy #2',
        'prompt_html': '<p>True or False: In Manufacturing Processes & Metallurgy, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Manufacturing Processes & Metallurgy.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Manufacturing Processes & Metallurgy #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Manufacturing Processes & Metallurgy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Manufacturing Processes & Metallurgy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Manufacturing Processes & Metallurgy #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Manufacturing Processes & Metallurgy</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Manufacturing Processes & Metallurgy balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Manufacturing Processes & Metallurgy Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Manufacturing Processes & Metallurgy.</p>',
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
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'question_id': 'ME-403-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Manufacturing Processes & Metallurgy Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Manufacturing Processes & Metallurgy.</p>',
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
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechatronics, Sensors & Actuators - Part 1',
        'prompt_html': '<p>In the context of <strong>Mechatronics, Sensors & Actuators</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechatronics, Sensors & Actuators theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechatronics, Sensors & Actuators - Part 2',
        'prompt_html': '<p>In the context of <strong>Mechatronics, Sensors & Actuators</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechatronics, Sensors & Actuators theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechatronics, Sensors & Actuators - Part 3',
        'prompt_html': '<p>In the context of <strong>Mechatronics, Sensors & Actuators</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechatronics, Sensors & Actuators theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Mechatronics, Sensors & Actuators - Part 4',
        'prompt_html': '<p>In the context of <strong>Mechatronics, Sensors & Actuators</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Mechatronics, Sensors & Actuators theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechatronics, Sensors & Actuators #1',
        'prompt_html': '<p>True or False: In Mechatronics, Sensors & Actuators, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechatronics, Sensors & Actuators.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Mechatronics, Sensors & Actuators #2',
        'prompt_html': '<p>True or False: In Mechatronics, Sensors & Actuators, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Mechatronics, Sensors & Actuators.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechatronics, Sensors & Actuators #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechatronics, Sensors & Actuators</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechatronics, Sensors & Actuators balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Mechatronics, Sensors & Actuators #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Mechatronics, Sensors & Actuators</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Mechatronics, Sensors & Actuators balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechatronics, Sensors & Actuators Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Mechatronics, Sensors & Actuators.</p>',
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
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'question_id': 'ME-404-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Mechatronics, Sensors & Actuators Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Mechatronics, Sensors & Actuators.</p>',
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
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Internal Combustion & Gas Turbines - Part 1',
        'prompt_html': '<p>In the context of <strong>Internal Combustion & Gas Turbines</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Internal Combustion & Gas Turbines theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Internal Combustion & Gas Turbines - Part 2',
        'prompt_html': '<p>In the context of <strong>Internal Combustion & Gas Turbines</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Internal Combustion & Gas Turbines theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Internal Combustion & Gas Turbines - Part 3',
        'prompt_html': '<p>In the context of <strong>Internal Combustion & Gas Turbines</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Internal Combustion & Gas Turbines theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Internal Combustion & Gas Turbines - Part 4',
        'prompt_html': '<p>In the context of <strong>Internal Combustion & Gas Turbines</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Internal Combustion & Gas Turbines theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Internal Combustion & Gas Turbines #1',
        'prompt_html': '<p>True or False: In Internal Combustion & Gas Turbines, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Internal Combustion & Gas Turbines.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Internal Combustion & Gas Turbines #2',
        'prompt_html': '<p>True or False: In Internal Combustion & Gas Turbines, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Internal Combustion & Gas Turbines.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Internal Combustion & Gas Turbines #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Internal Combustion & Gas Turbines</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Internal Combustion & Gas Turbines balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Internal Combustion & Gas Turbines #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Internal Combustion & Gas Turbines</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Internal Combustion & Gas Turbines balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Internal Combustion & Gas Turbines Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Internal Combustion & Gas Turbines.</p>',
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
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'question_id': 'ME-405-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Internal Combustion & Gas Turbines Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Internal Combustion & Gas Turbines.</p>',
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
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aerodynamics & Compressible Flow - Part 1',
        'prompt_html': '<p>In the context of <strong>Aerodynamics & Compressible Flow</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aerodynamics & Compressible Flow theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aerodynamics & Compressible Flow - Part 2',
        'prompt_html': '<p>In the context of <strong>Aerodynamics & Compressible Flow</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aerodynamics & Compressible Flow theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aerodynamics & Compressible Flow - Part 3',
        'prompt_html': '<p>In the context of <strong>Aerodynamics & Compressible Flow</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aerodynamics & Compressible Flow theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Aerodynamics & Compressible Flow - Part 4',
        'prompt_html': '<p>In the context of <strong>Aerodynamics & Compressible Flow</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Aerodynamics & Compressible Flow theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Aerodynamics & Compressible Flow #1',
        'prompt_html': '<p>True or False: In Aerodynamics & Compressible Flow, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Aerodynamics & Compressible Flow.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Aerodynamics & Compressible Flow #2',
        'prompt_html': '<p>True or False: In Aerodynamics & Compressible Flow, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Aerodynamics & Compressible Flow.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Aerodynamics & Compressible Flow #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Aerodynamics & Compressible Flow</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Aerodynamics & Compressible Flow balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Aerodynamics & Compressible Flow #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Aerodynamics & Compressible Flow</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Aerodynamics & Compressible Flow balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Aerodynamics & Compressible Flow Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Aerodynamics & Compressible Flow.</p>',
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
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'question_id': 'ME-406-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Aerodynamics & Compressible Flow Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Aerodynamics & Compressible Flow.</p>',
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
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Mechanical Engineering Capstone - Part 1',
        'prompt_html': '<p>In the context of <strong>Senior Mechanical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Mechanical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Mechanical Engineering Capstone - Part 2',
        'prompt_html': '<p>In the context of <strong>Senior Mechanical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Mechanical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Mechanical Engineering Capstone - Part 3',
        'prompt_html': '<p>In the context of <strong>Senior Mechanical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Mechanical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Senior Mechanical Engineering Capstone - Part 4',
        'prompt_html': '<p>In the context of <strong>Senior Mechanical Engineering Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Senior Mechanical Engineering Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Senior Mechanical Engineering Capstone #1',
        'prompt_html': '<p>True or False: In Senior Mechanical Engineering Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Senior Mechanical Engineering Capstone.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Senior Mechanical Engineering Capstone #2',
        'prompt_html': '<p>True or False: In Senior Mechanical Engineering Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Senior Mechanical Engineering Capstone.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Senior Mechanical Engineering Capstone #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Senior Mechanical Engineering Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Senior Mechanical Engineering Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Senior Mechanical Engineering Capstone #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Senior Mechanical Engineering Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Senior Mechanical Engineering Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Senior Mechanical Engineering Capstone Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Senior Mechanical Engineering Capstone.</p>',
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
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'question_id': 'ME-407-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Senior Mechanical Engineering Capstone Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Senior Mechanical Engineering Capstone.</p>',
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
