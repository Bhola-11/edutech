"""
Generator script to produce comprehensive academic course specifications,
laboratory experiment manuals, capstone briefs, and rubrics for all 15 disciplines.
"""
import os
import sys
import importlib

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

SPECS_DIR = os.path.join(os.path.dirname(__file__), '..', 'apps', 'courses', 'specifications')
os.makedirs(SPECS_DIR, exist_ok=True)

CURRICULA_MODULES = [
    ('computer_science', 'cs_specifications.py', 'Computer Science & Software Systems'),
    ('artificial_intelligence', 'ai_specifications.py', 'Artificial Intelligence & Machine Learning'),
    ('cybersecurity', 'cybersecurity_specifications.py', 'Cybersecurity & Information Assurance'),
    ('data_science', 'data_science_specifications.py', 'Data Science & Big Data Engineering'),
    ('electrical_engineering', 'electrical_specifications.py', 'Electrical & Computer Engineering'),
    ('mechanical_engineering', 'mechanical_specifications.py', 'Mechanical & Aerospace Engineering'),
    ('civil_environmental', 'civil_specifications.py', 'Civil & Environmental Engineering'),
    ('biomedical_health', 'biomedical_specifications.py', 'Biomedical Engineering & Informatics'),
    ('business_finance', 'business_specifications.py', 'Business Administration & FinTech'),
    ('mathematics_physics', 'math_physics_specifications.py', 'Mathematics & Applied Physics'),
    ('humanities_languages', 'humanities_specifications.py', 'Humanities & Applied Linguistics'),
    ('social_sciences_psychology', 'psychology_specifications.py', 'Social Sciences & Cognitive Psychology'),
    ('legal_studies_jurisprudence', 'legal_specifications.py', 'Legal Studies & Comparative Jurisprudence'),
    ('architecture_spatial_design', 'architecture_specifications.py', 'Architecture & Urban Design'),
    ('environmental_sustainability', 'environmental_specifications.py', 'Environmental Sustainability & Climate Science')
]


def generate_specifications_for_curriculum(module_name: str, output_file: str, discipline_name: str):
    mod = importlib.import_module(f"apps.courses.curricula.{module_name}")
    courses = getattr(mod, 'COURSES', [])

    lines = []
    lines.append('"""')
    lines.append(f"Comprehensive Course Specifications, Laboratory Experiment Manuals & Capstone Briefs.")
    lines.append(f"Discipline: {discipline_name}")
    lines.append(f"Generated for EduTech Enterprise Platform - Higher Education Accreditation Compliance.")
    lines.append('"""')
    lines.append("from typing import Dict, Any, List")
    lines.append("")
    lines.append(f'DISCIPLINE_NAME = "{discipline_name}"')
    lines.append(f'CURRICULUM_MODULE = "{module_name}"')
    lines.append("")
    lines.append("COURSE_SPECIFICATIONS: List[Dict[str, Any]] = [")

    for c in courses:
        code = c['code']
        title = c['title']
        credit_hours = c.get('credit_hours', 3)
        lecture_hours = c.get('lecture_hours', 3)
        lab_hours = c.get('lab_hours', 2)
        desc = c.get('description', '')

        lines.append("    {")
        lines.append(f"        'code': {repr(code)},")
        lines.append(f"        'title': {repr(title)},")
        lines.append(f"        'credit_hours': {credit_hours},")
        lines.append(f"        'lecture_hours': {lecture_hours},")
        lines.append(f"        'lab_hours': {lab_hours},")
        lines.append(f"        'description': {repr(desc)},")
        lines.append("        'laboratories': [")

        for lab_idx in range(1, 5):
            lines.append("            {")
            lines.append(f"                'lab_number': {lab_idx},")
            lines.append(f"                'title': {repr(f'Lab {lab_idx}: Practical Investigation & Implementation in {title}')},")
            lines.append(f"                'objective': {repr(f'Empirical verification, analytical modeling, and implementation of foundational techniques in {title} (Module {lab_idx * 3}).')},")
            lines.append(f"                'theoretical_foundation': {repr(f'Core mathematical principles, axiomatic definitions, and algorithmic frameworks underpinning {title}.')},")
            lines.append(f"                'hardware_software_requirements': [")
            lines.append(f"                    'Modern high-performance workstation with multicore CPU and 16GB+ RAM',")
            lines.append(f"                    'Professional engineering tools, compilers, simulators, and runtime SDKs',")
            lines.append(f"                    'Version control (Git) and automated unit testing frameworks',")
            lines.append(f"                    'Data logging and visualization toolkits'")
            lines.append("                ],")
            lines.append("                'pre_lab_requirements': [")
            lines.append(f"                    'Review assigned reading materials and theoretical lecture proofs for Week {lab_idx * 3}',")
            lines.append(f"                    'Derive governing equations and algorithmic complexity boundaries',")
            lines.append(f"                    'Draft architectural schema and initial pseudocode implementation'")
            lines.append("                ],")
            lines.append("                'procedure_steps': [")
            lines.append(f"                    'Step 1: Configure development and simulation environment with specified dependencies.',")
            lines.append(f"                    'Step 2: Initialize experimental fixtures, baseline datasets, and parameter configurations.',")
            lines.append(f"                    'Step 3: Execute empirical trials and capture diagnostic trace measurements across 5 benchmark configurations.',")
            lines.append(f"                    'Step 4: Conduct statistical error propagation analysis, compute confidence intervals, and profile execution latency.',")
            lines.append(f"                    'Step 5: Perform comparative evaluation against baseline theoretical predictions and characterize edge-case divergence.'")
            lines.append("                ],")
            lines.append("                'expected_deliverables': [")
            lines.append(f"                    'Complete commented source code / laboratory design repository conforming to style guidelines',")
            lines.append(f"                    'Formal technical report in IEEE/ACM conference format including methodology, empirical plots, and error analysis',")
            lines.append(f"                    'Comprehensive test suite demonstrating 90%+ code coverage or experimental repeatability',")
            lines.append(f"                    'Executive summary synthesizing key empirical findings and engineering tradeoffs'")
            lines.append("                ],")
            lines.append("                'rubric': {")
            lines.append("                    'exemplary': 'Demonstrates mastery: Flawless methodology, rigorous error bounds, comprehensive test suite, insightful discussion.',")
            lines.append("                    'proficient': 'Satisfies all core requirements: Correct execution, minor formatting or numerical rounding deviations, sound analysis.',")
            lines.append("                    'developing': 'Partial completion: Noticeable gaps in experimental rigor, incomplete error analysis, or missing edge-case verification.',")
            lines.append("                    'unsatisfactory': 'Inadequate: Execution failures, uncalibrated instruments, unverified hypotheses, or unsubmitted deliverables.'")
            lines.append("                }")
            lines.append("            },")

        lines.append("        ],")
        lines.append("        'term_projects': [")
        for proj_idx in range(1, 3):
            proj_title = f"{title} - Capstone Challenge {proj_idx}"
            lines.append("            {")
            lines.append(f"                'project_number': {proj_idx},")
            lines.append(f"                'title': {repr(proj_title)},")
            lines.append(f"                'scenario': {repr(f'Industry-scale applied design challenge requiring integration of full {title} concepts into a production-grade deliverable.')},")
            lines.append("                'specifications': [")
            lines.append(f"                    'Requirement 1: Complete end-to-end implementation meeting enterprise performance and safety standards.',")
            lines.append(f"                    'Requirement 2: Modular, decoupled architecture following industry design patterns and maintainability principles.',")
            lines.append(f"                    'Requirement 3: Rigorous verification protocol including automated regression test suites and stress testing.',")
            lines.append(f"                    'Requirement 4: Full technical documentation including architectural diagrams, API schemas, and deployment guides.'")
            lines.append("                ],")
            lines.append("                'milestones': [")
            lines.append(f"                    'Milestone 1 (Week 4): Project Charter, Requirements Specification, and Feasibility Assessment',")
            lines.append(f"                    'Milestone 2 (Week 8): Architectural Design Document, High-Level Schematics, and Alpha Prototype',")
            lines.append(f"                    'Milestone 3 (Week 11): Beta Implementation, Comprehensive Benchmark Results, and Peer Code Review',")
            lines.append(f"                    'Milestone 4 (Week 14): Final Release Package, Live Technical Defense, and Executive Demonstration'")
            lines.append("                ],")
            lines.append("                'rubric': {")
            lines.append("                    'technical_rigor_weight': 40,")
            lines.append("                    'architecture_and_design_weight': 25,")
            lines.append("                    'testing_and_verification_weight': 20,")
            lines.append("                    'documentation_and_defense_weight': 15")
            lines.append("                }")
            lines.append("            },")
        lines.append("        ],")
        lines.append("        'exam_problems': [")
        for q_idx in range(1, 5):
            lines.append("            {")
            lines.append(f"                'problem_number': {q_idx},")
            lines.append(f"                'topic': {repr(f'{title} Analytical Problem {q_idx}')},")
            lines.append(f"                'question': {repr(f'Derive, analyze, and compute optimal parameters for an operational {title} scenario under constrained boundary conditions.')},")
            lines.append(f"                'max_points': 25,")
            lines.append(f"                'scoring_criteria': [")
            lines.append(f"                    'Part A (5 pts): Correct identification of governing principles and initial boundary equations.',")
            lines.append(f"                    'Part B (10 pts): Step-by-step mathematical derivation and symbolic reduction.',")
            lines.append(f"                    'Part C (5 pts): Numerical calculation with proper units, significant figures, and error tolerances.',")
            lines.append(f"                    'Part D (5 pts): Engineering interpretation of asymptotic behavior and sensitivity analysis.'")
            lines.append("                ]")
            lines.append("            },")
        lines.append("        ]")
        lines.append("    },")

    lines.append("]")
    lines.append("")
    lines.append("def get_course_specification(course_code: str) -> Dict[str, Any]:")
    lines.append('    """Retrieves full specification for a course by code."""')
    lines.append("    code_clean = course_code.upper().strip()")
    lines.append("    for spec in COURSE_SPECIFICATIONS:")
    lines.append("        if spec['code'].upper() == code_clean:")
    lines.append("            return spec")
    lines.append("    return {}")
    lines.append("")
    lines.append("def list_all_course_codes() -> List[str]:")
    lines.append('    """Lists all course codes available in this discipline specification."""')
    lines.append("    return [s['code'] for s in COURSE_SPECIFICATIONS]")
    lines.append("")

    full_code = "\n".join(lines)
    dest_path = os.path.join(SPECS_DIR, output_file)
    with open(dest_path, 'w', encoding='utf-8') as f:
        f.write(full_code)
    print(f"Generated specifications: {output_file} ({len(courses)} courses)")


def main():
    # Create __init__.py in specifications
    init_path = os.path.join(SPECS_DIR, '__init__.py')
    with open(init_path, 'w', encoding='utf-8') as f:
        f.write('"""Academic Course Specifications & Laboratory Manuals Package."""\n')

    for module_name, output_file, discipline_name in CURRICULA_MODULES:
        generate_specifications_for_curriculum(module_name, output_file, discipline_name)

    print("All 15 course specifications generated successfully.")


if __name__ == '__main__':
    main()
