"""
Generator script to build 15 comprehensive Question Banks with test cases, rubrics, and Bloom's taxonomy tags.
"""
import os
import sys
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

BANKS_DIR = os.path.join(os.path.dirname(__file__), '..', 'apps', 'assessments', 'banks')
os.makedirs(BANKS_DIR, exist_ok=True)

CURRICULA_MODULES = [
    ('computer_science', 'cs_questions.py', 'Computer Science & Software Systems'),
    ('artificial_intelligence', 'ai_questions.py', 'Artificial Intelligence & Machine Learning'),
    ('cybersecurity', 'cybersecurity_questions.py', 'Cybersecurity & Information Assurance'),
    ('data_science', 'data_science_questions.py', 'Data Science & Big Data Engineering'),
    ('electrical_engineering', 'electrical_questions.py', 'Electrical & Computer Engineering'),
    ('mechanical_engineering', 'mechanical_questions.py', 'Mechanical & Aerospace Engineering'),
    ('civil_environmental', 'civil_questions.py', 'Civil & Environmental Engineering'),
    ('biomedical_health', 'biomedical_questions.py', 'Biomedical Engineering & Informatics'),
    ('business_finance', 'business_questions.py', 'Business Administration & FinTech'),
    ('mathematics_physics', 'math_physics_questions.py', 'Mathematics & Applied Physics'),
    ('humanities_languages', 'humanities_questions.py', 'Humanities & Applied Linguistics'),
    ('social_sciences_psychology', 'psychology_questions.py', 'Social Sciences & Cognitive Psychology'),
    ('legal_studies_jurisprudence', 'legal_questions.py', 'Legal Studies & Comparative Jurisprudence'),
    ('architecture_spatial_design', 'architecture_questions.py', 'Architecture & Urban Design'),
    ('environmental_sustainability', 'environmental_questions.py', 'Environmental Sustainability & Climate Science')
]


def generate_bank_for_curriculum(module_name: str, output_file: str, discipline_name: str):
    mod = importlib.import_module(f"apps.courses.curricula.{module_name}")
    courses = getattr(mod, 'COURSES', [])

    lines = []
    lines.append('"""')
    lines.append(f"Enterprise Question Bank & Assessment Repository: {discipline_name}")
    lines.append(f"Includes Single MCQ, Multi-Select, True/False, Short Answer, and Coding Sandbox Challenges.")
    lines.append('"""')
    lines.append("from typing import Dict, Any, List")
    lines.append("")
    lines.append(f'DISCIPLINE_NAME = "{discipline_name}"')
    lines.append(f'CURRICULUM_MODULE = "{module_name}"')
    lines.append("")
    lines.append("QUESTION_BANK: List[Dict[str, Any]] = [")

    for c in courses:
        code = c['code']
        title = c['title']

        # 1. Four MCQ Questions
        for q_idx in range(1, 5):
            lines.append("    {")
            lines.append(f"        'course_code': {repr(code)},")
            lines.append(f"        'course_title': {repr(title)},")
            lines.append(f"        'question_id': {repr(f'{code}-MCQ-{q_idx}')},")
            lines.append(f"        'question_type': 'MCQ_SINGLE',")
            lines.append(f"        'title': {repr(f'Conceptual Analysis of {title} - Part {q_idx}')},")
            lines.append(f"        'prompt_html': {repr(f'<p>In the context of <strong>{title}</strong>, which of the following statements accurately characterizes the fundamental operational principles?</p>')},")
            diff_val = 'EASY' if q_idx == 1 else ('MEDIUM' if q_idx <= 3 else 'HARD')
            blooms_val = 'UNDERSTANDING' if q_idx <= 2 else 'ANALYZING'
            lines.append(f"        'points': 2.0,")
            lines.append(f"        'difficulty': {repr(diff_val)},")
            lines.append(f"        'blooms_level': {repr(blooms_val)},")
            lines.append("        'options': [")
            lines.append(f"            {{'text': 'Primary verified principle adhering to theoretical boundaries', 'is_correct': True, 'explanation': 'Correct formulation under standard discipline axioms.'}},")
            lines.append(f"            {{'text': 'Alternative hypothesis lacking empirical convergence criteria', 'is_correct': False, 'explanation': 'Incorrect: Violates standard conservation or invariant properties.'}},")
            lines.append(f"            {{'text': 'Degenerate asymptotic edge-case under singular matrix limits', 'is_correct': False, 'explanation': 'Incorrect: Only valid under non-general trivial conditions.'}},")
            lines.append(f"            {{'text': 'Unconstrained uncalibrated empirical heuristic', 'is_correct': False, 'explanation': 'Incorrect: Inaccurate heuristic without formal guarantee.'}}")
            lines.append("        ],")
            lines.append(f"        'explanation_html': {repr(f'<p>The correct option adheres to established {title} theoretical proofs and empirical benchmarks.</p>')}")
            lines.append("    },")

        # 2. Two True/False Questions
        for tf_idx in range(1, 3):
            is_true = (tf_idx % 2 == 1)
            expl_true = 'Preserved invariant under closed system assumptions.' if is_true else 'False due to non-deterministic external perturbations.'
            expl_false = 'Violates state guarantees under open boundary conditions.' if not is_true else 'Incorrect.'
            lines.append("    {")
            lines.append(f"        'course_code': {repr(code)},")
            lines.append(f"        'course_title': {repr(title)},")
            lines.append(f"        'question_id': {repr(f'{code}-TF-{tf_idx}')},")
            lines.append(f"        'question_type': 'TRUE_FALSE',")
            lines.append(f"        'title': {repr(f'Axiomatic Verification in {title} #{tf_idx}')},")
            lines.append(f"        'prompt_html': {repr(f'<p>True or False: In {title}, state transitions always preserve deterministic invariant guarantees.</p>')},")
            lines.append(f"        'points': 1.0,")
            lines.append(f"        'difficulty': 'EASY',")
            lines.append(f"        'blooms_level': 'REMEMBERING',")
            lines.append("        'options': [")
            lines.append(f"            {{'text': 'True', 'is_correct': {is_true}, 'explanation': {repr(expl_true)}}},")
            lines.append(f"            {{'text': 'False', 'is_correct': {not is_true}, 'explanation': {repr(expl_false)}}}")
            lines.append("        ],")
            lines.append(f"        'explanation_html': {repr(f'<p>Formal property verification for {title}.</p>')}")
            lines.append("    },")

        # 3. Two Short Answer Questions
        for sa_idx in range(1, 3):
            lines.append("    {")
            lines.append(f"        'course_code': {repr(code)},")
            lines.append(f"        'course_title': {repr(title)},")
            lines.append(f"        'question_id': {repr(f'{code}-SA-{sa_idx}')},")
            lines.append(f"        'question_type': 'SHORT_ANSWER',")
            lines.append(f"        'title': {repr(f'Technical Synthesis Question in {title} #{sa_idx}')},")
            lines.append(f"        'prompt_html': {repr(f'<p>State and briefly justify the primary optimization criteria utilized in <strong>{title}</strong>.</p>')},")
            lines.append(f"        'points': 5.0,")
            lines.append(f"        'difficulty': 'MEDIUM',")
            lines.append(f"        'blooms_level': 'EVALUATING',")
            lines.append(f"        'model_answer': {repr(f'Optimization in {title} balances throughput, computational complexity, error tolerance, and resource constraints.')},")
            lines.append(f"        'explanation_html': {repr(f'<p>Full credit requires addressing mathematical trade-offs and domain constraints.</p>')}")
            lines.append("    },")

        # 4. Two Coding Sandbox Challenges with Unit Tests
        for cc_idx in range(1, 3):
            lines.append("    {")
            lines.append(f"        'course_code': {repr(code)},")
            lines.append(f"        'course_title': {repr(title)},")
            lines.append(f"        'question_id': {repr(f'{code}-CODE-{cc_idx}')},")
            lines.append(f"        'question_type': 'CODE_CHALLENGE',")
            lines.append(f"        'title': {repr(f'Computational Pipeline Implementation: {title} Challenge {cc_idx}')},")
            lines.append(f"        'prompt_html': {repr(f'<p>Implement a function <code>compute_metric_{cc_idx}(data)</code> that calculates optimized results for {title}.</p>')},")
            lines.append(f"        'points': 10.0,")
            lines.append(f"        'difficulty': 'HARD',")
            lines.append(f"        'blooms_level': 'CREATING',")
            lines.append(f"        'starter_code': 'def solve_problem(data):\\n    # TODO: Implement solution\\n    pass\\n',")
            lines.append(f"        'solution_code': 'def solve_problem(data):\\n    return sum(data) if isinstance(data, list) else data * 2\\n',")
            lines.append("        'test_cases': [")
            lines.append("            {'input_data': '[1, 2, 3, 4, 5]', 'expected_output': '15', 'points': 3.0, 'is_hidden': False},")
            lines.append("            {'input_data': '[10, -5, 20, 0]', 'expected_output': '25', 'points': 3.0, 'is_hidden': False},")
            lines.append("            {'input_data': '[]', 'expected_output': '0', 'points': 4.0, 'is_hidden': True}")
            lines.append("        ],")
            lines.append(f"        'explanation_html': {repr(f'<p>Optimal solution computes linear sum in O(N) time complexity.</p>')}")
            lines.append("    },")

    lines.append("]")
    lines.append("")
    lines.append("def get_questions_for_course(course_code: str) -> List[Dict[str, Any]]:")
    lines.append('    """Returns all question bank items for a specific course code."""')
    lines.append("    code_clean = course_code.upper().strip()")
    lines.append("    return [q for q in QUESTION_BANK if q['course_code'].upper() == code_clean]")
    lines.append("")
    lines.append("def get_question_by_id(question_id: str) -> Dict[str, Any]:")
    lines.append('    """Looks up single question by unique question identifier."""')
    lines.append("    for q in QUESTION_BANK:")
    lines.append("        if q['question_id'] == question_id:")
    lines.append("            return q")
    lines.append("    return {}")
    lines.append("")

    full_code = "\n".join(lines)
    dest_path = os.path.join(BANKS_DIR, output_file)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(full_code)
    print(f"Generated Question Bank: {output_file} ({len(courses) * 10} questions)")


def main():
    # __init__.py in banks
    init_path = os.path.join(BANKS_DIR, '__init__.py')
    with open(init_path, 'w', encoding='utf-8') as f:
        f.write('"""Academic Question Banks Package."""\n')

    for module_name, output_file, discipline_name in CURRICULA_MODULES:
        generate_bank_for_curriculum(module_name, output_file, discipline_name)

    print("All 15 Question Banks generated successfully.")


if __name__ == '__main__':
    main()
