"""
Standardized Examination Paper Repository: Biomedical Engineering & Informatics
Includes Formal Midterm & Final Comprehensive Examination Papers with Solutions.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Biomedical Engineering & Informatics"
CURRICULUM_MODULE = "biomedical_health"

EXAMINATION_PAPERS: List[Dict[str, Any]] = [
    {
        'course_code': 'BME-101',
        'course_title': 'Introduction to Biomedical Engineering',
        'midterm_exam': {
            'paper_code': 'BME-101-MIDTERM',
            'title': 'Introduction to Biomedical Engineering Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Introduction to Biomedical Engineering scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Introduction to Biomedical Engineering scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Introduction to Biomedical Engineering scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Introduction to Biomedical Engineering scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Introduction to Biomedical Engineering scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-101-FINAL',
            'title': 'Introduction to Biomedical Engineering Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Introduction to Biomedical Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Introduction to Biomedical Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Introduction to Biomedical Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Introduction to Biomedical Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Introduction to Biomedical Engineering Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Introduction to Biomedical Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-201',
        'course_title': 'Human Anatomy & Physiology for Engineers',
        'midterm_exam': {
            'paper_code': 'BME-201-MIDTERM',
            'title': 'Human Anatomy & Physiology for Engineers Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Human Anatomy & Physiology for Engineers scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Human Anatomy & Physiology for Engineers scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Human Anatomy & Physiology for Engineers scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Human Anatomy & Physiology for Engineers scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Human Anatomy & Physiology for Engineers scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-201-FINAL',
            'title': 'Human Anatomy & Physiology for Engineers Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Human Anatomy & Physiology for Engineers.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Human Anatomy & Physiology for Engineers.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Human Anatomy & Physiology for Engineers.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Human Anatomy & Physiology for Engineers.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Human Anatomy & Physiology for Engineers Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Human Anatomy & Physiology for Engineers.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-202',
        'course_title': 'Biomaterials Science & Tissue Scaffolds',
        'midterm_exam': {
            'paper_code': 'BME-202-MIDTERM',
            'title': 'Biomaterials Science & Tissue Scaffolds Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomaterials Science & Tissue Scaffolds scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomaterials Science & Tissue Scaffolds scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomaterials Science & Tissue Scaffolds scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomaterials Science & Tissue Scaffolds scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomaterials Science & Tissue Scaffolds scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-202-FINAL',
            'title': 'Biomaterials Science & Tissue Scaffolds Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomaterials Science & Tissue Scaffolds.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomaterials Science & Tissue Scaffolds.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomaterials Science & Tissue Scaffolds.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomaterials Science & Tissue Scaffolds.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Biomaterials Science & Tissue Scaffolds Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomaterials Science & Tissue Scaffolds.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-301',
        'course_title': 'Bioinstrumentation & Biosensor Design',
        'midterm_exam': {
            'paper_code': 'BME-301-MIDTERM',
            'title': 'Bioinstrumentation & Biosensor Design Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Bioinstrumentation & Biosensor Design scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Bioinstrumentation & Biosensor Design scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Bioinstrumentation & Biosensor Design scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Bioinstrumentation & Biosensor Design scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Bioinstrumentation & Biosensor Design scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-301-FINAL',
            'title': 'Bioinstrumentation & Biosensor Design Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Bioinstrumentation & Biosensor Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Bioinstrumentation & Biosensor Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Bioinstrumentation & Biosensor Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Bioinstrumentation & Biosensor Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Bioinstrumentation & Biosensor Design Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Bioinstrumentation & Biosensor Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-302',
        'course_title': 'Orthopaedic & Cardiovascular Biomechanics',
        'midterm_exam': {
            'paper_code': 'BME-302-MIDTERM',
            'title': 'Orthopaedic & Cardiovascular Biomechanics Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Orthopaedic & Cardiovascular Biomechanics scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Orthopaedic & Cardiovascular Biomechanics scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Orthopaedic & Cardiovascular Biomechanics scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Orthopaedic & Cardiovascular Biomechanics scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Orthopaedic & Cardiovascular Biomechanics scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-302-FINAL',
            'title': 'Orthopaedic & Cardiovascular Biomechanics Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Orthopaedic & Cardiovascular Biomechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Orthopaedic & Cardiovascular Biomechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Orthopaedic & Cardiovascular Biomechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Orthopaedic & Cardiovascular Biomechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Orthopaedic & Cardiovascular Biomechanics Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Orthopaedic & Cardiovascular Biomechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-303',
        'course_title': 'Physiological Signal Processing (ECG/EMG)',
        'midterm_exam': {
            'paper_code': 'BME-303-MIDTERM',
            'title': 'Physiological Signal Processing (ECG/EMG) Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Physiological Signal Processing (ECG/EMG) scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Physiological Signal Processing (ECG/EMG) scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Physiological Signal Processing (ECG/EMG) scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Physiological Signal Processing (ECG/EMG) scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Physiological Signal Processing (ECG/EMG) scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-303-FINAL',
            'title': 'Physiological Signal Processing (ECG/EMG) Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Physiological Signal Processing (ECG/EMG).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Physiological Signal Processing (ECG/EMG).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Physiological Signal Processing (ECG/EMG).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Physiological Signal Processing (ECG/EMG).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Physiological Signal Processing (ECG/EMG) Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Physiological Signal Processing (ECG/EMG).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-401',
        'course_title': 'Medical Imaging Systems (CT/MRI/Ultrasound)',
        'midterm_exam': {
            'paper_code': 'BME-401-MIDTERM',
            'title': 'Medical Imaging Systems (CT/MRI/Ultrasound) Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Imaging Systems (CT/MRI/Ultrasound) scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Imaging Systems (CT/MRI/Ultrasound) scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Imaging Systems (CT/MRI/Ultrasound) scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Imaging Systems (CT/MRI/Ultrasound) scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Imaging Systems (CT/MRI/Ultrasound) scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-401-FINAL',
            'title': 'Medical Imaging Systems (CT/MRI/Ultrasound) Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Imaging Systems (CT/MRI/Ultrasound).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Imaging Systems (CT/MRI/Ultrasound).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Imaging Systems (CT/MRI/Ultrasound).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Imaging Systems (CT/MRI/Ultrasound).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Medical Imaging Systems (CT/MRI/Ultrasound) Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Imaging Systems (CT/MRI/Ultrasound).',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-402',
        'course_title': 'Clinical Health Informatics & HL7 FHIR',
        'midterm_exam': {
            'paper_code': 'BME-402-MIDTERM',
            'title': 'Clinical Health Informatics & HL7 FHIR Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Clinical Health Informatics & HL7 FHIR scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Clinical Health Informatics & HL7 FHIR scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Clinical Health Informatics & HL7 FHIR scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Clinical Health Informatics & HL7 FHIR scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Clinical Health Informatics & HL7 FHIR scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-402-FINAL',
            'title': 'Clinical Health Informatics & HL7 FHIR Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Clinical Health Informatics & HL7 FHIR.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Clinical Health Informatics & HL7 FHIR.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Clinical Health Informatics & HL7 FHIR.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Clinical Health Informatics & HL7 FHIR.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Clinical Health Informatics & HL7 FHIR Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Clinical Health Informatics & HL7 FHIR.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-403',
        'course_title': 'Artificial Organs & Dialysis Engineering',
        'midterm_exam': {
            'paper_code': 'BME-403-MIDTERM',
            'title': 'Artificial Organs & Dialysis Engineering Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Artificial Organs & Dialysis Engineering scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Artificial Organs & Dialysis Engineering scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Artificial Organs & Dialysis Engineering scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Artificial Organs & Dialysis Engineering scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Artificial Organs & Dialysis Engineering scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-403-FINAL',
            'title': 'Artificial Organs & Dialysis Engineering Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Artificial Organs & Dialysis Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Artificial Organs & Dialysis Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Artificial Organs & Dialysis Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Artificial Organs & Dialysis Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Artificial Organs & Dialysis Engineering Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Artificial Organs & Dialysis Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-404',
        'course_title': 'Cellular & Molecular Bioengineering',
        'midterm_exam': {
            'paper_code': 'BME-404-MIDTERM',
            'title': 'Cellular & Molecular Bioengineering Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Cellular & Molecular Bioengineering scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Cellular & Molecular Bioengineering scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Cellular & Molecular Bioengineering scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Cellular & Molecular Bioengineering scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Cellular & Molecular Bioengineering scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-404-FINAL',
            'title': 'Cellular & Molecular Bioengineering Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Cellular & Molecular Bioengineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Cellular & Molecular Bioengineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Cellular & Molecular Bioengineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Cellular & Molecular Bioengineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Cellular & Molecular Bioengineering Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Cellular & Molecular Bioengineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-405',
        'course_title': 'Neural Engineering & BCI Decoding',
        'midterm_exam': {
            'paper_code': 'BME-405-MIDTERM',
            'title': 'Neural Engineering & BCI Decoding Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Neural Engineering & BCI Decoding scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Neural Engineering & BCI Decoding scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Neural Engineering & BCI Decoding scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Neural Engineering & BCI Decoding scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Neural Engineering & BCI Decoding scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-405-FINAL',
            'title': 'Neural Engineering & BCI Decoding Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Neural Engineering & BCI Decoding.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Neural Engineering & BCI Decoding.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Neural Engineering & BCI Decoding.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Neural Engineering & BCI Decoding.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Neural Engineering & BCI Decoding Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Neural Engineering & BCI Decoding.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-406',
        'course_title': 'Medical Device FDA Regulatory Submissions',
        'midterm_exam': {
            'paper_code': 'BME-406-MIDTERM',
            'title': 'Medical Device FDA Regulatory Submissions Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Device FDA Regulatory Submissions scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Device FDA Regulatory Submissions scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Device FDA Regulatory Submissions scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Device FDA Regulatory Submissions scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Medical Device FDA Regulatory Submissions scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-406-FINAL',
            'title': 'Medical Device FDA Regulatory Submissions Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Device FDA Regulatory Submissions.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Device FDA Regulatory Submissions.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Device FDA Regulatory Submissions.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Device FDA Regulatory Submissions.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Medical Device FDA Regulatory Submissions Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Medical Device FDA Regulatory Submissions.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-407',
        'course_title': 'Nanomedicine & Targeted Drug Delivery',
        'midterm_exam': {
            'paper_code': 'BME-407-MIDTERM',
            'title': 'Nanomedicine & Targeted Drug Delivery Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Nanomedicine & Targeted Drug Delivery scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Nanomedicine & Targeted Drug Delivery scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Nanomedicine & Targeted Drug Delivery scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Nanomedicine & Targeted Drug Delivery scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Nanomedicine & Targeted Drug Delivery scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-407-FINAL',
            'title': 'Nanomedicine & Targeted Drug Delivery Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Nanomedicine & Targeted Drug Delivery.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Nanomedicine & Targeted Drug Delivery.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Nanomedicine & Targeted Drug Delivery.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Nanomedicine & Targeted Drug Delivery.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Nanomedicine & Targeted Drug Delivery Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Nanomedicine & Targeted Drug Delivery.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-408',
        'course_title': 'Biomedical Optics & Laser Applications',
        'midterm_exam': {
            'paper_code': 'BME-408-MIDTERM',
            'title': 'Biomedical Optics & Laser Applications Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Optics & Laser Applications scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Optics & Laser Applications scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Optics & Laser Applications scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Optics & Laser Applications scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Optics & Laser Applications scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-408-FINAL',
            'title': 'Biomedical Optics & Laser Applications Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Optics & Laser Applications.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Optics & Laser Applications.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Optics & Laser Applications.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Optics & Laser Applications.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Biomedical Optics & Laser Applications Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Optics & Laser Applications.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
    {
        'course_code': 'BME-409',
        'course_title': 'Biomedical Innovation & Design Capstone',
        'midterm_exam': {
            'paper_code': 'BME-409-MIDTERM',
            'title': 'Biomedical Innovation & Design Capstone Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Innovation & Design Capstone scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Innovation & Design Capstone scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Innovation & Design Capstone scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Innovation & Design Capstone scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Biomedical Innovation & Design Capstone scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
                        'final_answer': 'System satisfies optimality within +/- 0.5% tolerance bounds.'
                    },
                    'marking_rubric': {
                        'formulation_marks': 6,
                        'derivation_marks': 8,
                        'calculation_marks': 4,
                        'interpretation_marks': 2
                    }
                },
            ]
        },
        'final_exam': {
            'paper_code': 'BME-409-FINAL',
            'title': 'Biomedical Innovation & Design Capstone Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Innovation & Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 2,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Innovation & Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 3,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Innovation & Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 4,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Innovation & Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
                {
                    'question_number': 5,
                    'marks': 20,
                    'topic': 'Biomedical Innovation & Design Capstone Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Biomedical Innovation & Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
                        'final_answer': 'Demonstrated asymptotic convergence with zero invariant violation.'
                    },
                    'marking_rubric': {
                        'architectural_design_marks': 6,
                        'mathematical_proof_marks': 8,
                        'empirical_verification_marks': 4,
                        'synthesis_clarity_marks': 2
                    }
                },
            ]
        }
    },
]

def get_papers_for_course(course_code: str) -> Dict[str, Any]:
    """Returns midterm and final exam papers for a course code."""
    code_clean = course_code.upper().strip()
    for p in EXAMINATION_PAPERS:
        if p['course_code'].upper() == code_clean:
            return p
    return {}
