"""
Enterprise Question Bank & Assessment Repository: Biomedical Engineering & Informatics
Includes Single MCQ, Multi-Select, True/False, Short Answer, and Coding Sandbox Challenges.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Biomedical Engineering & Informatics"
CURRICULUM_MODULE = "biomedical_health"

QUESTION_BANK: List[Dict[str, Any]] = [
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Introduction to Biomedical Engineering - Part 1',
        'prompt_html': '<p>In the context of <strong>Introduction to Biomedical Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Introduction to Biomedical Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Introduction to Biomedical Engineering - Part 2',
        'prompt_html': '<p>In the context of <strong>Introduction to Biomedical Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Introduction to Biomedical Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Introduction to Biomedical Engineering - Part 3',
        'prompt_html': '<p>In the context of <strong>Introduction to Biomedical Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Introduction to Biomedical Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Introduction to Biomedical Engineering - Part 4',
        'prompt_html': '<p>In the context of <strong>Introduction to Biomedical Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Introduction to Biomedical Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Introduction to Biomedical Engineering #1',
        'prompt_html': '<p>True or False: In Introduction to Biomedical Engineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Introduction to Biomedical Engineering.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Introduction to Biomedical Engineering #2',
        'prompt_html': '<p>True or False: In Introduction to Biomedical Engineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Introduction to Biomedical Engineering.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Introduction to Biomedical Engineering #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Introduction to Biomedical Engineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Introduction to Biomedical Engineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Introduction to Biomedical Engineering #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Introduction to Biomedical Engineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Introduction to Biomedical Engineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Introduction to Biomedical Engineering Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Introduction to Biomedical Engineering.</p>',
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
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'question_id': 'BME-101-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Introduction to Biomedical Engineering Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Introduction to Biomedical Engineering.</p>',
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
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Human Anatomy & Physiology for Engineers - Part 1',
        'prompt_html': '<p>In the context of <strong>Human Anatomy & Physiology for Engineers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Human Anatomy & Physiology for Engineers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Human Anatomy & Physiology for Engineers - Part 2',
        'prompt_html': '<p>In the context of <strong>Human Anatomy & Physiology for Engineers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Human Anatomy & Physiology for Engineers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Human Anatomy & Physiology for Engineers - Part 3',
        'prompt_html': '<p>In the context of <strong>Human Anatomy & Physiology for Engineers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Human Anatomy & Physiology for Engineers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Human Anatomy & Physiology for Engineers - Part 4',
        'prompt_html': '<p>In the context of <strong>Human Anatomy & Physiology for Engineers</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Human Anatomy & Physiology for Engineers theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Human Anatomy & Physiology for Engineers #1',
        'prompt_html': '<p>True or False: In Human Anatomy & Physiology for Engineers, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Human Anatomy & Physiology for Engineers.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Human Anatomy & Physiology for Engineers #2',
        'prompt_html': '<p>True or False: In Human Anatomy & Physiology for Engineers, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Human Anatomy & Physiology for Engineers.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Human Anatomy & Physiology for Engineers #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Human Anatomy & Physiology for Engineers</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Human Anatomy & Physiology for Engineers balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Human Anatomy & Physiology for Engineers #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Human Anatomy & Physiology for Engineers</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Human Anatomy & Physiology for Engineers balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Human Anatomy & Physiology for Engineers Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Human Anatomy & Physiology for Engineers.</p>',
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
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'question_id': 'BME-201-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Human Anatomy & Physiology for Engineers Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Human Anatomy & Physiology for Engineers.</p>',
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
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomaterials Science & Tissue Scaffolds - Part 1',
        'prompt_html': '<p>In the context of <strong>Biomaterials Science & Tissue Scaffolds</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomaterials Science & Tissue Scaffolds theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomaterials Science & Tissue Scaffolds - Part 2',
        'prompt_html': '<p>In the context of <strong>Biomaterials Science & Tissue Scaffolds</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomaterials Science & Tissue Scaffolds theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomaterials Science & Tissue Scaffolds - Part 3',
        'prompt_html': '<p>In the context of <strong>Biomaterials Science & Tissue Scaffolds</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomaterials Science & Tissue Scaffolds theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomaterials Science & Tissue Scaffolds - Part 4',
        'prompt_html': '<p>In the context of <strong>Biomaterials Science & Tissue Scaffolds</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomaterials Science & Tissue Scaffolds theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Biomaterials Science & Tissue Scaffolds #1',
        'prompt_html': '<p>True or False: In Biomaterials Science & Tissue Scaffolds, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Biomaterials Science & Tissue Scaffolds.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Biomaterials Science & Tissue Scaffolds #2',
        'prompt_html': '<p>True or False: In Biomaterials Science & Tissue Scaffolds, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Biomaterials Science & Tissue Scaffolds.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Biomaterials Science & Tissue Scaffolds #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Biomaterials Science & Tissue Scaffolds</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Biomaterials Science & Tissue Scaffolds balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Biomaterials Science & Tissue Scaffolds #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Biomaterials Science & Tissue Scaffolds</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Biomaterials Science & Tissue Scaffolds balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Biomaterials Science & Tissue Scaffolds Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Biomaterials Science & Tissue Scaffolds.</p>',
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
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'question_id': 'BME-202-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Biomaterials Science & Tissue Scaffolds Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Biomaterials Science & Tissue Scaffolds.</p>',
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
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioinstrumentation & Biosensor Design - Part 1',
        'prompt_html': '<p>In the context of <strong>Bioinstrumentation & Biosensor Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioinstrumentation & Biosensor Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioinstrumentation & Biosensor Design - Part 2',
        'prompt_html': '<p>In the context of <strong>Bioinstrumentation & Biosensor Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioinstrumentation & Biosensor Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioinstrumentation & Biosensor Design - Part 3',
        'prompt_html': '<p>In the context of <strong>Bioinstrumentation & Biosensor Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioinstrumentation & Biosensor Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Bioinstrumentation & Biosensor Design - Part 4',
        'prompt_html': '<p>In the context of <strong>Bioinstrumentation & Biosensor Design</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Bioinstrumentation & Biosensor Design theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Bioinstrumentation & Biosensor Design #1',
        'prompt_html': '<p>True or False: In Bioinstrumentation & Biosensor Design, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Bioinstrumentation & Biosensor Design.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Bioinstrumentation & Biosensor Design #2',
        'prompt_html': '<p>True or False: In Bioinstrumentation & Biosensor Design, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Bioinstrumentation & Biosensor Design.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Bioinstrumentation & Biosensor Design #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Bioinstrumentation & Biosensor Design</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Bioinstrumentation & Biosensor Design balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Bioinstrumentation & Biosensor Design #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Bioinstrumentation & Biosensor Design</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Bioinstrumentation & Biosensor Design balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Bioinstrumentation & Biosensor Design Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Bioinstrumentation & Biosensor Design.</p>',
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
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'question_id': 'BME-301-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Bioinstrumentation & Biosensor Design Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Bioinstrumentation & Biosensor Design.</p>',
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
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Orthopaedic & Cardiovascular Biomechanics - Part 1',
        'prompt_html': '<p>In the context of <strong>Orthopaedic & Cardiovascular Biomechanics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Orthopaedic & Cardiovascular Biomechanics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Orthopaedic & Cardiovascular Biomechanics - Part 2',
        'prompt_html': '<p>In the context of <strong>Orthopaedic & Cardiovascular Biomechanics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Orthopaedic & Cardiovascular Biomechanics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Orthopaedic & Cardiovascular Biomechanics - Part 3',
        'prompt_html': '<p>In the context of <strong>Orthopaedic & Cardiovascular Biomechanics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Orthopaedic & Cardiovascular Biomechanics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Orthopaedic & Cardiovascular Biomechanics - Part 4',
        'prompt_html': '<p>In the context of <strong>Orthopaedic & Cardiovascular Biomechanics</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Orthopaedic & Cardiovascular Biomechanics theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Orthopaedic & Cardiovascular Biomechanics #1',
        'prompt_html': '<p>True or False: In Orthopaedic & Cardiovascular Biomechanics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Orthopaedic & Cardiovascular Biomechanics.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Orthopaedic & Cardiovascular Biomechanics #2',
        'prompt_html': '<p>True or False: In Orthopaedic & Cardiovascular Biomechanics, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Orthopaedic & Cardiovascular Biomechanics.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Orthopaedic & Cardiovascular Biomechanics #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Orthopaedic & Cardiovascular Biomechanics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Orthopaedic & Cardiovascular Biomechanics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Orthopaedic & Cardiovascular Biomechanics #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Orthopaedic & Cardiovascular Biomechanics</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Orthopaedic & Cardiovascular Biomechanics balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Orthopaedic & Cardiovascular Biomechanics Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Orthopaedic & Cardiovascular Biomechanics.</p>',
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
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'question_id': 'BME-302-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Orthopaedic & Cardiovascular Biomechanics Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Orthopaedic & Cardiovascular Biomechanics.</p>',
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
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Physiological Signal Processing (ECG/EMG) - Part 1',
        'prompt_html': '<p>In the context of <strong>Physiological Signal Processing (ECG/EMG)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Physiological Signal Processing (ECG/EMG) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Physiological Signal Processing (ECG/EMG) - Part 2',
        'prompt_html': '<p>In the context of <strong>Physiological Signal Processing (ECG/EMG)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Physiological Signal Processing (ECG/EMG) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Physiological Signal Processing (ECG/EMG) - Part 3',
        'prompt_html': '<p>In the context of <strong>Physiological Signal Processing (ECG/EMG)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Physiological Signal Processing (ECG/EMG) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Physiological Signal Processing (ECG/EMG) - Part 4',
        'prompt_html': '<p>In the context of <strong>Physiological Signal Processing (ECG/EMG)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Physiological Signal Processing (ECG/EMG) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Physiological Signal Processing (ECG/EMG) #1',
        'prompt_html': '<p>True or False: In Physiological Signal Processing (ECG/EMG), state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Physiological Signal Processing (ECG/EMG).</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Physiological Signal Processing (ECG/EMG) #2',
        'prompt_html': '<p>True or False: In Physiological Signal Processing (ECG/EMG), state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Physiological Signal Processing (ECG/EMG).</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Physiological Signal Processing (ECG/EMG) #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Physiological Signal Processing (ECG/EMG)</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Physiological Signal Processing (ECG/EMG) balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Physiological Signal Processing (ECG/EMG) #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Physiological Signal Processing (ECG/EMG)</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Physiological Signal Processing (ECG/EMG) balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Physiological Signal Processing (ECG/EMG) Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Physiological Signal Processing (ECG/EMG).</p>',
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
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'question_id': 'BME-303-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Physiological Signal Processing (ECG/EMG) Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Physiological Signal Processing (ECG/EMG).</p>',
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
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Imaging Systems (CT/MRI/Ultrasound) - Part 1',
        'prompt_html': '<p>In the context of <strong>Medical Imaging Systems (CT/MRI/Ultrasound)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Imaging Systems (CT/MRI/Ultrasound) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Imaging Systems (CT/MRI/Ultrasound) - Part 2',
        'prompt_html': '<p>In the context of <strong>Medical Imaging Systems (CT/MRI/Ultrasound)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Imaging Systems (CT/MRI/Ultrasound) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Imaging Systems (CT/MRI/Ultrasound) - Part 3',
        'prompt_html': '<p>In the context of <strong>Medical Imaging Systems (CT/MRI/Ultrasound)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Imaging Systems (CT/MRI/Ultrasound) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Imaging Systems (CT/MRI/Ultrasound) - Part 4',
        'prompt_html': '<p>In the context of <strong>Medical Imaging Systems (CT/MRI/Ultrasound)</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Imaging Systems (CT/MRI/Ultrasound) theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Medical Imaging Systems (CT/MRI/Ultrasound) #1',
        'prompt_html': '<p>True or False: In Medical Imaging Systems (CT/MRI/Ultrasound), state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Medical Imaging Systems (CT/MRI/Ultrasound).</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Medical Imaging Systems (CT/MRI/Ultrasound) #2',
        'prompt_html': '<p>True or False: In Medical Imaging Systems (CT/MRI/Ultrasound), state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Medical Imaging Systems (CT/MRI/Ultrasound).</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Medical Imaging Systems (CT/MRI/Ultrasound) #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Medical Imaging Systems (CT/MRI/Ultrasound)</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Medical Imaging Systems (CT/MRI/Ultrasound) balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Medical Imaging Systems (CT/MRI/Ultrasound) #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Medical Imaging Systems (CT/MRI/Ultrasound)</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Medical Imaging Systems (CT/MRI/Ultrasound) balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Medical Imaging Systems (CT/MRI/Ultrasound) Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Medical Imaging Systems (CT/MRI/Ultrasound).</p>',
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
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'question_id': 'BME-401-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Medical Imaging Systems (CT/MRI/Ultrasound) Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Medical Imaging Systems (CT/MRI/Ultrasound).</p>',
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
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Clinical Health Informatics & HL7 FHIR - Part 1',
        'prompt_html': '<p>In the context of <strong>Clinical Health Informatics & HL7 FHIR</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Clinical Health Informatics & HL7 FHIR theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Clinical Health Informatics & HL7 FHIR - Part 2',
        'prompt_html': '<p>In the context of <strong>Clinical Health Informatics & HL7 FHIR</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Clinical Health Informatics & HL7 FHIR theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Clinical Health Informatics & HL7 FHIR - Part 3',
        'prompt_html': '<p>In the context of <strong>Clinical Health Informatics & HL7 FHIR</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Clinical Health Informatics & HL7 FHIR theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Clinical Health Informatics & HL7 FHIR - Part 4',
        'prompt_html': '<p>In the context of <strong>Clinical Health Informatics & HL7 FHIR</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Clinical Health Informatics & HL7 FHIR theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Clinical Health Informatics & HL7 FHIR #1',
        'prompt_html': '<p>True or False: In Clinical Health Informatics & HL7 FHIR, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Clinical Health Informatics & HL7 FHIR.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Clinical Health Informatics & HL7 FHIR #2',
        'prompt_html': '<p>True or False: In Clinical Health Informatics & HL7 FHIR, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Clinical Health Informatics & HL7 FHIR.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Clinical Health Informatics & HL7 FHIR #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Clinical Health Informatics & HL7 FHIR</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Clinical Health Informatics & HL7 FHIR balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Clinical Health Informatics & HL7 FHIR #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Clinical Health Informatics & HL7 FHIR</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Clinical Health Informatics & HL7 FHIR balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Clinical Health Informatics & HL7 FHIR Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Clinical Health Informatics & HL7 FHIR.</p>',
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
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'question_id': 'BME-402-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Clinical Health Informatics & HL7 FHIR Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Clinical Health Informatics & HL7 FHIR.</p>',
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
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Artificial Organs & Dialysis Engineering - Part 1',
        'prompt_html': '<p>In the context of <strong>Artificial Organs & Dialysis Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Artificial Organs & Dialysis Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Artificial Organs & Dialysis Engineering - Part 2',
        'prompt_html': '<p>In the context of <strong>Artificial Organs & Dialysis Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Artificial Organs & Dialysis Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Artificial Organs & Dialysis Engineering - Part 3',
        'prompt_html': '<p>In the context of <strong>Artificial Organs & Dialysis Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Artificial Organs & Dialysis Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Artificial Organs & Dialysis Engineering - Part 4',
        'prompt_html': '<p>In the context of <strong>Artificial Organs & Dialysis Engineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Artificial Organs & Dialysis Engineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Artificial Organs & Dialysis Engineering #1',
        'prompt_html': '<p>True or False: In Artificial Organs & Dialysis Engineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Artificial Organs & Dialysis Engineering.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Artificial Organs & Dialysis Engineering #2',
        'prompt_html': '<p>True or False: In Artificial Organs & Dialysis Engineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Artificial Organs & Dialysis Engineering.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Artificial Organs & Dialysis Engineering #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Artificial Organs & Dialysis Engineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Artificial Organs & Dialysis Engineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Artificial Organs & Dialysis Engineering #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Artificial Organs & Dialysis Engineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Artificial Organs & Dialysis Engineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Artificial Organs & Dialysis Engineering Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Artificial Organs & Dialysis Engineering.</p>',
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
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'question_id': 'BME-403-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Artificial Organs & Dialysis Engineering Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Artificial Organs & Dialysis Engineering.</p>',
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
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Cellular & Molecular Bioengineering - Part 1',
        'prompt_html': '<p>In the context of <strong>Cellular & Molecular Bioengineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Cellular & Molecular Bioengineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Cellular & Molecular Bioengineering - Part 2',
        'prompt_html': '<p>In the context of <strong>Cellular & Molecular Bioengineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Cellular & Molecular Bioengineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Cellular & Molecular Bioengineering - Part 3',
        'prompt_html': '<p>In the context of <strong>Cellular & Molecular Bioengineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Cellular & Molecular Bioengineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Cellular & Molecular Bioengineering - Part 4',
        'prompt_html': '<p>In the context of <strong>Cellular & Molecular Bioengineering</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Cellular & Molecular Bioengineering theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Cellular & Molecular Bioengineering #1',
        'prompt_html': '<p>True or False: In Cellular & Molecular Bioengineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Cellular & Molecular Bioengineering.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Cellular & Molecular Bioengineering #2',
        'prompt_html': '<p>True or False: In Cellular & Molecular Bioengineering, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Cellular & Molecular Bioengineering.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Cellular & Molecular Bioengineering #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Cellular & Molecular Bioengineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Cellular & Molecular Bioengineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Cellular & Molecular Bioengineering #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Cellular & Molecular Bioengineering</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Cellular & Molecular Bioengineering balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Cellular & Molecular Bioengineering Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Cellular & Molecular Bioengineering.</p>',
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
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'question_id': 'BME-404-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Cellular & Molecular Bioengineering Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Cellular & Molecular Bioengineering.</p>',
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
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Neural Engineering & BCI Decoding - Part 1',
        'prompt_html': '<p>In the context of <strong>Neural Engineering & BCI Decoding</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Neural Engineering & BCI Decoding theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Neural Engineering & BCI Decoding - Part 2',
        'prompt_html': '<p>In the context of <strong>Neural Engineering & BCI Decoding</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Neural Engineering & BCI Decoding theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Neural Engineering & BCI Decoding - Part 3',
        'prompt_html': '<p>In the context of <strong>Neural Engineering & BCI Decoding</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Neural Engineering & BCI Decoding theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Neural Engineering & BCI Decoding - Part 4',
        'prompt_html': '<p>In the context of <strong>Neural Engineering & BCI Decoding</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Neural Engineering & BCI Decoding theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Neural Engineering & BCI Decoding #1',
        'prompt_html': '<p>True or False: In Neural Engineering & BCI Decoding, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Neural Engineering & BCI Decoding.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Neural Engineering & BCI Decoding #2',
        'prompt_html': '<p>True or False: In Neural Engineering & BCI Decoding, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Neural Engineering & BCI Decoding.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Neural Engineering & BCI Decoding #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Neural Engineering & BCI Decoding</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Neural Engineering & BCI Decoding balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Neural Engineering & BCI Decoding #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Neural Engineering & BCI Decoding</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Neural Engineering & BCI Decoding balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Neural Engineering & BCI Decoding Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Neural Engineering & BCI Decoding.</p>',
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
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'question_id': 'BME-405-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Neural Engineering & BCI Decoding Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Neural Engineering & BCI Decoding.</p>',
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
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Device FDA Regulatory Submissions - Part 1',
        'prompt_html': '<p>In the context of <strong>Medical Device FDA Regulatory Submissions</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Device FDA Regulatory Submissions theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Device FDA Regulatory Submissions - Part 2',
        'prompt_html': '<p>In the context of <strong>Medical Device FDA Regulatory Submissions</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Device FDA Regulatory Submissions theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Device FDA Regulatory Submissions - Part 3',
        'prompt_html': '<p>In the context of <strong>Medical Device FDA Regulatory Submissions</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Device FDA Regulatory Submissions theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Medical Device FDA Regulatory Submissions - Part 4',
        'prompt_html': '<p>In the context of <strong>Medical Device FDA Regulatory Submissions</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Medical Device FDA Regulatory Submissions theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Medical Device FDA Regulatory Submissions #1',
        'prompt_html': '<p>True or False: In Medical Device FDA Regulatory Submissions, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Medical Device FDA Regulatory Submissions.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Medical Device FDA Regulatory Submissions #2',
        'prompt_html': '<p>True or False: In Medical Device FDA Regulatory Submissions, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Medical Device FDA Regulatory Submissions.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Medical Device FDA Regulatory Submissions #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Medical Device FDA Regulatory Submissions</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Medical Device FDA Regulatory Submissions balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Medical Device FDA Regulatory Submissions #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Medical Device FDA Regulatory Submissions</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Medical Device FDA Regulatory Submissions balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Medical Device FDA Regulatory Submissions Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Medical Device FDA Regulatory Submissions.</p>',
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
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'question_id': 'BME-406-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Medical Device FDA Regulatory Submissions Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Medical Device FDA Regulatory Submissions.</p>',
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
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Nanomedicine & Targeted Drug Delivery - Part 1',
        'prompt_html': '<p>In the context of <strong>Nanomedicine & Targeted Drug Delivery</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Nanomedicine & Targeted Drug Delivery theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Nanomedicine & Targeted Drug Delivery - Part 2',
        'prompt_html': '<p>In the context of <strong>Nanomedicine & Targeted Drug Delivery</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Nanomedicine & Targeted Drug Delivery theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Nanomedicine & Targeted Drug Delivery - Part 3',
        'prompt_html': '<p>In the context of <strong>Nanomedicine & Targeted Drug Delivery</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Nanomedicine & Targeted Drug Delivery theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Nanomedicine & Targeted Drug Delivery - Part 4',
        'prompt_html': '<p>In the context of <strong>Nanomedicine & Targeted Drug Delivery</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Nanomedicine & Targeted Drug Delivery theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Nanomedicine & Targeted Drug Delivery #1',
        'prompt_html': '<p>True or False: In Nanomedicine & Targeted Drug Delivery, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Nanomedicine & Targeted Drug Delivery.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Nanomedicine & Targeted Drug Delivery #2',
        'prompt_html': '<p>True or False: In Nanomedicine & Targeted Drug Delivery, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Nanomedicine & Targeted Drug Delivery.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Nanomedicine & Targeted Drug Delivery #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Nanomedicine & Targeted Drug Delivery</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Nanomedicine & Targeted Drug Delivery balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Nanomedicine & Targeted Drug Delivery #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Nanomedicine & Targeted Drug Delivery</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Nanomedicine & Targeted Drug Delivery balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Nanomedicine & Targeted Drug Delivery Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Nanomedicine & Targeted Drug Delivery.</p>',
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
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'question_id': 'BME-407-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Nanomedicine & Targeted Drug Delivery Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Nanomedicine & Targeted Drug Delivery.</p>',
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
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Optics & Laser Applications - Part 1',
        'prompt_html': '<p>In the context of <strong>Biomedical Optics & Laser Applications</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Optics & Laser Applications theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Optics & Laser Applications - Part 2',
        'prompt_html': '<p>In the context of <strong>Biomedical Optics & Laser Applications</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Optics & Laser Applications theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Optics & Laser Applications - Part 3',
        'prompt_html': '<p>In the context of <strong>Biomedical Optics & Laser Applications</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Optics & Laser Applications theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Optics & Laser Applications - Part 4',
        'prompt_html': '<p>In the context of <strong>Biomedical Optics & Laser Applications</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Optics & Laser Applications theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Biomedical Optics & Laser Applications #1',
        'prompt_html': '<p>True or False: In Biomedical Optics & Laser Applications, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Biomedical Optics & Laser Applications.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Biomedical Optics & Laser Applications #2',
        'prompt_html': '<p>True or False: In Biomedical Optics & Laser Applications, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Biomedical Optics & Laser Applications.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Biomedical Optics & Laser Applications #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Biomedical Optics & Laser Applications</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Biomedical Optics & Laser Applications balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Biomedical Optics & Laser Applications #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Biomedical Optics & Laser Applications</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Biomedical Optics & Laser Applications balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Biomedical Optics & Laser Applications Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Biomedical Optics & Laser Applications.</p>',
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
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'question_id': 'BME-408-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Biomedical Optics & Laser Applications Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Biomedical Optics & Laser Applications.</p>',
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
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-MCQ-1',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Innovation & Design Capstone - Part 1',
        'prompt_html': '<p>In the context of <strong>Biomedical Innovation & Design Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'EASY',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Innovation & Design Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-MCQ-2',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Innovation & Design Capstone - Part 2',
        'prompt_html': '<p>In the context of <strong>Biomedical Innovation & Design Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'UNDERSTANDING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Innovation & Design Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-MCQ-3',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Innovation & Design Capstone - Part 3',
        'prompt_html': '<p>In the context of <strong>Biomedical Innovation & Design Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Innovation & Design Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-MCQ-4',
        'question_type': 'MCQ_SINGLE',
        'title': 'Conceptual Analysis of Biomedical Innovation & Design Capstone - Part 4',
        'prompt_html': '<p>In the context of <strong>Biomedical Innovation & Design Capstone</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>',
        'points': 2.0,
        'difficulty': 'HARD',
        'blooms_level': 'ANALYZING',
        'options': [
            {'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'},
            {'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'},
            {'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'},
            {'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}
        ],
        'explanation_html': '<p>The correct option adheres to established Biomedical Innovation & Design Capstone theoretical proofs and empirical benchmarks.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-TF-1',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Biomedical Innovation & Design Capstone #1',
        'prompt_html': '<p>True or False: In Biomedical Innovation & Design Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': True, 'explanation': 'Preserved invariant under closed system assumptions.'},
            {'text': 'False', 'is_correct': False, 'explanation': 'Incorrect.'}
        ],
        'explanation_html': '<p>Formal property verification for Biomedical Innovation & Design Capstone.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-TF-2',
        'question_type': 'TRUE_FALSE',
        'title': 'Axiomatic Verification in Biomedical Innovation & Design Capstone #2',
        'prompt_html': '<p>True or False: In Biomedical Innovation & Design Capstone, state transitions always preserve deterministic invariant guarantees.</p>',
        'points': 1.0,
        'difficulty': 'EASY',
        'blooms_level': 'REMEMBERING',
        'options': [
            {'text': 'True', 'is_correct': False, 'explanation': 'False due to non-deterministic external perturbations.'},
            {'text': 'False', 'is_correct': True, 'explanation': 'Violates state guarantees under open boundary conditions.'}
        ],
        'explanation_html': '<p>Formal property verification for Biomedical Innovation & Design Capstone.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-SA-1',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Biomedical Innovation & Design Capstone #1',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Biomedical Innovation & Design Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Biomedical Innovation & Design Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-SA-2',
        'question_type': 'SHORT_ANSWER',
        'title': 'Technical Synthesis Question in Biomedical Innovation & Design Capstone #2',
        'prompt_html': '<p>State and briefly justify the primary optimization criteria utilized in <strong>Biomedical Innovation & Design Capstone</strong>.</p>',
        'points': 5.0,
        'difficulty': 'MEDIUM',
        'blooms_level': 'EVALUATING',
        'model_answer': 'Optimization in Biomedical Innovation & Design Capstone balances throughput, computational complexity, error tolerance, and resource constraints.',
        'explanation_html': '<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>'
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-CODE-1',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Biomedical Innovation & Design Capstone Challenge 1',
        'prompt_html': '<p>Implement a function <code>compute_metric_1(data)</code> that calculates optimized results for Biomedical Innovation & Design Capstone.</p>',
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
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'question_id': 'BME-409-CODE-2',
        'question_type': 'CODE_CHALLENGE',
        'title': 'Computational Pipeline Implementation: Biomedical Innovation & Design Capstone Challenge 2',
        'prompt_html': '<p>Implement a function <code>compute_metric_2(data)</code> that calculates optimized results for Biomedical Innovation & Design Capstone.</p>',
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
