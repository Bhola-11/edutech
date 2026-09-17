"""
Standardized Examination Paper Repository: Electrical & Computer Engineering
Includes Formal Midterm & Final Comprehensive Examination Papers with Solutions.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Electrical & Computer Engineering"
CURRICULUM_MODULE = "electrical_engineering"

EXAMINATION_PAPERS: List[Dict[str, Any]] = [
    {
        'course_code': 'EE-101',
        'course_title': 'Electric Circuit Analysis I',
        'midterm_exam': {
            'paper_code': 'EE-101-MIDTERM',
            'title': 'Electric Circuit Analysis I Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Electric Circuit Analysis I Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis I scenario under boundary constraints (Part 1).',
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
                    'topic': 'Electric Circuit Analysis I Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis I scenario under boundary constraints (Part 2).',
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
                    'topic': 'Electric Circuit Analysis I Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis I scenario under boundary constraints (Part 3).',
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
                    'topic': 'Electric Circuit Analysis I Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis I scenario under boundary constraints (Part 4).',
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
                    'topic': 'Electric Circuit Analysis I Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis I scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-101-FINAL',
            'title': 'Electric Circuit Analysis I Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Electric Circuit Analysis I Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis I.',
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
                    'topic': 'Electric Circuit Analysis I Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis I.',
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
                    'topic': 'Electric Circuit Analysis I Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis I.',
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
                    'topic': 'Electric Circuit Analysis I Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis I.',
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
                    'topic': 'Electric Circuit Analysis I Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis I.',
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
        'course_code': 'EE-102',
        'course_title': 'Electric Circuit Analysis II',
        'midterm_exam': {
            'paper_code': 'EE-102-MIDTERM',
            'title': 'Electric Circuit Analysis II Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Electric Circuit Analysis II Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis II scenario under boundary constraints (Part 1).',
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
                    'topic': 'Electric Circuit Analysis II Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis II scenario under boundary constraints (Part 2).',
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
                    'topic': 'Electric Circuit Analysis II Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis II scenario under boundary constraints (Part 3).',
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
                    'topic': 'Electric Circuit Analysis II Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis II scenario under boundary constraints (Part 4).',
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
                    'topic': 'Electric Circuit Analysis II Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electric Circuit Analysis II scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-102-FINAL',
            'title': 'Electric Circuit Analysis II Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Electric Circuit Analysis II Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis II.',
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
                    'topic': 'Electric Circuit Analysis II Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis II.',
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
                    'topic': 'Electric Circuit Analysis II Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis II.',
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
                    'topic': 'Electric Circuit Analysis II Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis II.',
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
                    'topic': 'Electric Circuit Analysis II Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electric Circuit Analysis II.',
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
        'course_code': 'EE-201',
        'course_title': 'Digital Logic Design & Verilog',
        'midterm_exam': {
            'paper_code': 'EE-201-MIDTERM',
            'title': 'Digital Logic Design & Verilog Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Digital Logic Design & Verilog Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Logic Design & Verilog scenario under boundary constraints (Part 1).',
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
                    'topic': 'Digital Logic Design & Verilog Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Logic Design & Verilog scenario under boundary constraints (Part 2).',
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
                    'topic': 'Digital Logic Design & Verilog Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Logic Design & Verilog scenario under boundary constraints (Part 3).',
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
                    'topic': 'Digital Logic Design & Verilog Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Logic Design & Verilog scenario under boundary constraints (Part 4).',
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
                    'topic': 'Digital Logic Design & Verilog Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Logic Design & Verilog scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-201-FINAL',
            'title': 'Digital Logic Design & Verilog Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Digital Logic Design & Verilog Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Logic Design & Verilog.',
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
                    'topic': 'Digital Logic Design & Verilog Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Logic Design & Verilog.',
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
                    'topic': 'Digital Logic Design & Verilog Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Logic Design & Verilog.',
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
                    'topic': 'Digital Logic Design & Verilog Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Logic Design & Verilog.',
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
                    'topic': 'Digital Logic Design & Verilog Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Logic Design & Verilog.',
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
        'course_code': 'EE-202',
        'course_title': 'Signals & Linear Systems',
        'midterm_exam': {
            'paper_code': 'EE-202-MIDTERM',
            'title': 'Signals & Linear Systems Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Signals & Linear Systems Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Signals & Linear Systems scenario under boundary constraints (Part 1).',
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
                    'topic': 'Signals & Linear Systems Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Signals & Linear Systems scenario under boundary constraints (Part 2).',
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
                    'topic': 'Signals & Linear Systems Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Signals & Linear Systems scenario under boundary constraints (Part 3).',
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
                    'topic': 'Signals & Linear Systems Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Signals & Linear Systems scenario under boundary constraints (Part 4).',
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
                    'topic': 'Signals & Linear Systems Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Signals & Linear Systems scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-202-FINAL',
            'title': 'Signals & Linear Systems Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Signals & Linear Systems Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Signals & Linear Systems.',
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
                    'topic': 'Signals & Linear Systems Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Signals & Linear Systems.',
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
                    'topic': 'Signals & Linear Systems Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Signals & Linear Systems.',
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
                    'topic': 'Signals & Linear Systems Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Signals & Linear Systems.',
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
                    'topic': 'Signals & Linear Systems Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Signals & Linear Systems.',
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
        'course_code': 'EE-301',
        'course_title': 'Semiconductor Electronics & Devices',
        'midterm_exam': {
            'paper_code': 'EE-301-MIDTERM',
            'title': 'Semiconductor Electronics & Devices Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Semiconductor Electronics & Devices Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Semiconductor Electronics & Devices scenario under boundary constraints (Part 1).',
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
                    'topic': 'Semiconductor Electronics & Devices Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Semiconductor Electronics & Devices scenario under boundary constraints (Part 2).',
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
                    'topic': 'Semiconductor Electronics & Devices Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Semiconductor Electronics & Devices scenario under boundary constraints (Part 3).',
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
                    'topic': 'Semiconductor Electronics & Devices Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Semiconductor Electronics & Devices scenario under boundary constraints (Part 4).',
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
                    'topic': 'Semiconductor Electronics & Devices Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Semiconductor Electronics & Devices scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-301-FINAL',
            'title': 'Semiconductor Electronics & Devices Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Semiconductor Electronics & Devices Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Semiconductor Electronics & Devices.',
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
                    'topic': 'Semiconductor Electronics & Devices Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Semiconductor Electronics & Devices.',
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
                    'topic': 'Semiconductor Electronics & Devices Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Semiconductor Electronics & Devices.',
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
                    'topic': 'Semiconductor Electronics & Devices Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Semiconductor Electronics & Devices.',
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
                    'topic': 'Semiconductor Electronics & Devices Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Semiconductor Electronics & Devices.',
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
        'course_code': 'EE-302',
        'course_title': 'Embedded Microcontrollers & Firmware',
        'midterm_exam': {
            'paper_code': 'EE-302-MIDTERM',
            'title': 'Embedded Microcontrollers & Firmware Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Embedded Microcontrollers & Firmware Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Embedded Microcontrollers & Firmware scenario under boundary constraints (Part 1).',
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
                    'topic': 'Embedded Microcontrollers & Firmware Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Embedded Microcontrollers & Firmware scenario under boundary constraints (Part 2).',
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
                    'topic': 'Embedded Microcontrollers & Firmware Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Embedded Microcontrollers & Firmware scenario under boundary constraints (Part 3).',
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
                    'topic': 'Embedded Microcontrollers & Firmware Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Embedded Microcontrollers & Firmware scenario under boundary constraints (Part 4).',
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
                    'topic': 'Embedded Microcontrollers & Firmware Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Embedded Microcontrollers & Firmware scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-302-FINAL',
            'title': 'Embedded Microcontrollers & Firmware Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Embedded Microcontrollers & Firmware Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Embedded Microcontrollers & Firmware.',
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
                    'topic': 'Embedded Microcontrollers & Firmware Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Embedded Microcontrollers & Firmware.',
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
                    'topic': 'Embedded Microcontrollers & Firmware Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Embedded Microcontrollers & Firmware.',
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
                    'topic': 'Embedded Microcontrollers & Firmware Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Embedded Microcontrollers & Firmware.',
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
                    'topic': 'Embedded Microcontrollers & Firmware Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Embedded Microcontrollers & Firmware.',
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
        'course_code': 'EE-303',
        'course_title': 'Electromagnetic Fields & Waveguides',
        'midterm_exam': {
            'paper_code': 'EE-303-MIDTERM',
            'title': 'Electromagnetic Fields & Waveguides Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Electromagnetic Fields & Waveguides Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electromagnetic Fields & Waveguides scenario under boundary constraints (Part 1).',
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
                    'topic': 'Electromagnetic Fields & Waveguides Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electromagnetic Fields & Waveguides scenario under boundary constraints (Part 2).',
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
                    'topic': 'Electromagnetic Fields & Waveguides Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electromagnetic Fields & Waveguides scenario under boundary constraints (Part 3).',
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
                    'topic': 'Electromagnetic Fields & Waveguides Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electromagnetic Fields & Waveguides scenario under boundary constraints (Part 4).',
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
                    'topic': 'Electromagnetic Fields & Waveguides Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Electromagnetic Fields & Waveguides scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-303-FINAL',
            'title': 'Electromagnetic Fields & Waveguides Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Electromagnetic Fields & Waveguides Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electromagnetic Fields & Waveguides.',
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
                    'topic': 'Electromagnetic Fields & Waveguides Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electromagnetic Fields & Waveguides.',
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
                    'topic': 'Electromagnetic Fields & Waveguides Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electromagnetic Fields & Waveguides.',
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
                    'topic': 'Electromagnetic Fields & Waveguides Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electromagnetic Fields & Waveguides.',
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
                    'topic': 'Electromagnetic Fields & Waveguides Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Electromagnetic Fields & Waveguides.',
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
        'course_code': 'EE-401',
        'course_title': 'Feedback Control Systems Engineering',
        'midterm_exam': {
            'paper_code': 'EE-401-MIDTERM',
            'title': 'Feedback Control Systems Engineering Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Feedback Control Systems Engineering Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Feedback Control Systems Engineering scenario under boundary constraints (Part 1).',
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
                    'topic': 'Feedback Control Systems Engineering Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Feedback Control Systems Engineering scenario under boundary constraints (Part 2).',
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
                    'topic': 'Feedback Control Systems Engineering Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Feedback Control Systems Engineering scenario under boundary constraints (Part 3).',
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
                    'topic': 'Feedback Control Systems Engineering Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Feedback Control Systems Engineering scenario under boundary constraints (Part 4).',
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
                    'topic': 'Feedback Control Systems Engineering Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Feedback Control Systems Engineering scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-401-FINAL',
            'title': 'Feedback Control Systems Engineering Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Feedback Control Systems Engineering Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Feedback Control Systems Engineering.',
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
                    'topic': 'Feedback Control Systems Engineering Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Feedback Control Systems Engineering.',
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
                    'topic': 'Feedback Control Systems Engineering Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Feedback Control Systems Engineering.',
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
                    'topic': 'Feedback Control Systems Engineering Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Feedback Control Systems Engineering.',
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
                    'topic': 'Feedback Control Systems Engineering Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Feedback Control Systems Engineering.',
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
        'course_code': 'EE-402',
        'course_title': 'Power Electronics & Inverters',
        'midterm_exam': {
            'paper_code': 'EE-402-MIDTERM',
            'title': 'Power Electronics & Inverters Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Power Electronics & Inverters Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Power Electronics & Inverters scenario under boundary constraints (Part 1).',
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
                    'topic': 'Power Electronics & Inverters Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Power Electronics & Inverters scenario under boundary constraints (Part 2).',
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
                    'topic': 'Power Electronics & Inverters Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Power Electronics & Inverters scenario under boundary constraints (Part 3).',
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
                    'topic': 'Power Electronics & Inverters Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Power Electronics & Inverters scenario under boundary constraints (Part 4).',
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
                    'topic': 'Power Electronics & Inverters Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Power Electronics & Inverters scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-402-FINAL',
            'title': 'Power Electronics & Inverters Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Power Electronics & Inverters Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Power Electronics & Inverters.',
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
                    'topic': 'Power Electronics & Inverters Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Power Electronics & Inverters.',
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
                    'topic': 'Power Electronics & Inverters Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Power Electronics & Inverters.',
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
                    'topic': 'Power Electronics & Inverters Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Power Electronics & Inverters.',
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
                    'topic': 'Power Electronics & Inverters Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Power Electronics & Inverters.',
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
        'course_code': 'EE-403',
        'course_title': 'Analog CMOS Integrated Circuit Design',
        'midterm_exam': {
            'paper_code': 'EE-403-MIDTERM',
            'title': 'Analog CMOS Integrated Circuit Design Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Analog CMOS Integrated Circuit Design Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Analog CMOS Integrated Circuit Design scenario under boundary constraints (Part 1).',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Analog CMOS Integrated Circuit Design scenario under boundary constraints (Part 2).',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Analog CMOS Integrated Circuit Design scenario under boundary constraints (Part 3).',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Analog CMOS Integrated Circuit Design scenario under boundary constraints (Part 4).',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Analog CMOS Integrated Circuit Design scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-403-FINAL',
            'title': 'Analog CMOS Integrated Circuit Design Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Analog CMOS Integrated Circuit Design Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Analog CMOS Integrated Circuit Design.',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Analog CMOS Integrated Circuit Design.',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Analog CMOS Integrated Circuit Design.',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Analog CMOS Integrated Circuit Design.',
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
                    'topic': 'Analog CMOS Integrated Circuit Design Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Analog CMOS Integrated Circuit Design.',
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
        'course_code': 'EE-404',
        'course_title': 'Digital Signal Processing (DSP) & Filters',
        'midterm_exam': {
            'paper_code': 'EE-404-MIDTERM',
            'title': 'Digital Signal Processing (DSP) & Filters Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Digital Signal Processing (DSP) & Filters Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Signal Processing (DSP) & Filters scenario under boundary constraints (Part 1).',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Signal Processing (DSP) & Filters scenario under boundary constraints (Part 2).',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Signal Processing (DSP) & Filters scenario under boundary constraints (Part 3).',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Signal Processing (DSP) & Filters scenario under boundary constraints (Part 4).',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Digital Signal Processing (DSP) & Filters scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-404-FINAL',
            'title': 'Digital Signal Processing (DSP) & Filters Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Digital Signal Processing (DSP) & Filters Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Signal Processing (DSP) & Filters.',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Signal Processing (DSP) & Filters.',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Signal Processing (DSP) & Filters.',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Signal Processing (DSP) & Filters.',
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
                    'topic': 'Digital Signal Processing (DSP) & Filters Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Digital Signal Processing (DSP) & Filters.',
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
        'course_code': 'EE-405',
        'course_title': 'Microwave Engineering & Antennas',
        'midterm_exam': {
            'paper_code': 'EE-405-MIDTERM',
            'title': 'Microwave Engineering & Antennas Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Microwave Engineering & Antennas Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Microwave Engineering & Antennas scenario under boundary constraints (Part 1).',
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
                    'topic': 'Microwave Engineering & Antennas Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Microwave Engineering & Antennas scenario under boundary constraints (Part 2).',
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
                    'topic': 'Microwave Engineering & Antennas Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Microwave Engineering & Antennas scenario under boundary constraints (Part 3).',
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
                    'topic': 'Microwave Engineering & Antennas Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Microwave Engineering & Antennas scenario under boundary constraints (Part 4).',
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
                    'topic': 'Microwave Engineering & Antennas Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Microwave Engineering & Antennas scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-405-FINAL',
            'title': 'Microwave Engineering & Antennas Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Microwave Engineering & Antennas Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Microwave Engineering & Antennas.',
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
                    'topic': 'Microwave Engineering & Antennas Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Microwave Engineering & Antennas.',
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
                    'topic': 'Microwave Engineering & Antennas Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Microwave Engineering & Antennas.',
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
                    'topic': 'Microwave Engineering & Antennas Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Microwave Engineering & Antennas.',
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
                    'topic': 'Microwave Engineering & Antennas Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Microwave Engineering & Antennas.',
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
        'course_code': 'EE-406',
        'course_title': 'Renewable Energy Systems & Smart Grids',
        'midterm_exam': {
            'paper_code': 'EE-406-MIDTERM',
            'title': 'Renewable Energy Systems & Smart Grids Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Renewable Energy Systems & Smart Grids Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Renewable Energy Systems & Smart Grids scenario under boundary constraints (Part 1).',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Renewable Energy Systems & Smart Grids scenario under boundary constraints (Part 2).',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Renewable Energy Systems & Smart Grids scenario under boundary constraints (Part 3).',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Renewable Energy Systems & Smart Grids scenario under boundary constraints (Part 4).',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Renewable Energy Systems & Smart Grids scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-406-FINAL',
            'title': 'Renewable Energy Systems & Smart Grids Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Renewable Energy Systems & Smart Grids Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Renewable Energy Systems & Smart Grids.',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Renewable Energy Systems & Smart Grids.',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Renewable Energy Systems & Smart Grids.',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Renewable Energy Systems & Smart Grids.',
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
                    'topic': 'Renewable Energy Systems & Smart Grids Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Renewable Energy Systems & Smart Grids.',
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
        'course_code': 'EE-407',
        'course_title': 'VLSI Physical Design & Layout',
        'midterm_exam': {
            'paper_code': 'EE-407-MIDTERM',
            'title': 'VLSI Physical Design & Layout Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'VLSI Physical Design & Layout Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for VLSI Physical Design & Layout scenario under boundary constraints (Part 1).',
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
                    'topic': 'VLSI Physical Design & Layout Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for VLSI Physical Design & Layout scenario under boundary constraints (Part 2).',
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
                    'topic': 'VLSI Physical Design & Layout Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for VLSI Physical Design & Layout scenario under boundary constraints (Part 3).',
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
                    'topic': 'VLSI Physical Design & Layout Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for VLSI Physical Design & Layout scenario under boundary constraints (Part 4).',
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
                    'topic': 'VLSI Physical Design & Layout Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for VLSI Physical Design & Layout scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-407-FINAL',
            'title': 'VLSI Physical Design & Layout Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'VLSI Physical Design & Layout Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for VLSI Physical Design & Layout.',
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
                    'topic': 'VLSI Physical Design & Layout Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for VLSI Physical Design & Layout.',
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
                    'topic': 'VLSI Physical Design & Layout Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for VLSI Physical Design & Layout.',
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
                    'topic': 'VLSI Physical Design & Layout Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for VLSI Physical Design & Layout.',
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
                    'topic': 'VLSI Physical Design & Layout Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for VLSI Physical Design & Layout.',
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
        'course_code': 'EE-408',
        'course_title': 'Senior Electrical Engineering Capstone',
        'midterm_exam': {
            'paper_code': 'EE-408-MIDTERM',
            'title': 'Senior Electrical Engineering Capstone Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Senior Electrical Engineering Capstone Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Electrical Engineering Capstone scenario under boundary constraints (Part 1).',
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
                    'topic': 'Senior Electrical Engineering Capstone Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Electrical Engineering Capstone scenario under boundary constraints (Part 2).',
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
                    'topic': 'Senior Electrical Engineering Capstone Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Electrical Engineering Capstone scenario under boundary constraints (Part 3).',
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
                    'topic': 'Senior Electrical Engineering Capstone Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Electrical Engineering Capstone scenario under boundary constraints (Part 4).',
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
                    'topic': 'Senior Electrical Engineering Capstone Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Electrical Engineering Capstone scenario under boundary constraints (Part 5).',
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
            'paper_code': 'EE-408-FINAL',
            'title': 'Senior Electrical Engineering Capstone Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Senior Electrical Engineering Capstone Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Electrical Engineering Capstone.',
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
                    'topic': 'Senior Electrical Engineering Capstone Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Electrical Engineering Capstone.',
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
                    'topic': 'Senior Electrical Engineering Capstone Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Electrical Engineering Capstone.',
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
                    'topic': 'Senior Electrical Engineering Capstone Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Electrical Engineering Capstone.',
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
                    'topic': 'Senior Electrical Engineering Capstone Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Electrical Engineering Capstone.',
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
