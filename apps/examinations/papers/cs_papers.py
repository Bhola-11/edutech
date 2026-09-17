"""
Standardized Examination Paper Repository: Computer Science & Software Systems
Includes Formal Midterm & Final Comprehensive Examination Papers with Solutions.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Computer Science & Software Systems"
CURRICULUM_MODULE = "computer_science"

EXAMINATION_PAPERS: List[Dict[str, Any]] = [
    {
        'course_code': 'CS-101',
        'course_title': 'Intro to Computing & Python',
        'midterm_exam': {
            'paper_code': 'CS-101-MIDTERM',
            'title': 'Intro to Computing & Python Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Intro to Computing & Python Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Intro to Computing & Python scenario under boundary constraints (Part 1).',
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
                    'topic': 'Intro to Computing & Python Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Intro to Computing & Python scenario under boundary constraints (Part 2).',
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
                    'topic': 'Intro to Computing & Python Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Intro to Computing & Python scenario under boundary constraints (Part 3).',
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
                    'topic': 'Intro to Computing & Python Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Intro to Computing & Python scenario under boundary constraints (Part 4).',
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
                    'topic': 'Intro to Computing & Python Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Intro to Computing & Python scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-101-FINAL',
            'title': 'Intro to Computing & Python Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Intro to Computing & Python Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Intro to Computing & Python.',
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
                    'topic': 'Intro to Computing & Python Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Intro to Computing & Python.',
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
                    'topic': 'Intro to Computing & Python Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Intro to Computing & Python.',
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
                    'topic': 'Intro to Computing & Python Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Intro to Computing & Python.',
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
                    'topic': 'Intro to Computing & Python Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Intro to Computing & Python.',
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
        'course_code': 'CS-102',
        'course_title': 'OOP & Design Patterns',
        'midterm_exam': {
            'paper_code': 'CS-102-MIDTERM',
            'title': 'OOP & Design Patterns Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'OOP & Design Patterns Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for OOP & Design Patterns scenario under boundary constraints (Part 1).',
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
                    'topic': 'OOP & Design Patterns Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for OOP & Design Patterns scenario under boundary constraints (Part 2).',
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
                    'topic': 'OOP & Design Patterns Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for OOP & Design Patterns scenario under boundary constraints (Part 3).',
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
                    'topic': 'OOP & Design Patterns Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for OOP & Design Patterns scenario under boundary constraints (Part 4).',
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
                    'topic': 'OOP & Design Patterns Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for OOP & Design Patterns scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-102-FINAL',
            'title': 'OOP & Design Patterns Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'OOP & Design Patterns Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for OOP & Design Patterns.',
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
                    'topic': 'OOP & Design Patterns Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for OOP & Design Patterns.',
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
                    'topic': 'OOP & Design Patterns Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for OOP & Design Patterns.',
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
                    'topic': 'OOP & Design Patterns Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for OOP & Design Patterns.',
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
                    'topic': 'OOP & Design Patterns Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for OOP & Design Patterns.',
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
        'course_code': 'CS-201',
        'course_title': 'Discrete Mathematics',
        'midterm_exam': {
            'paper_code': 'CS-201-MIDTERM',
            'title': 'Discrete Mathematics Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Discrete Mathematics Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Discrete Mathematics scenario under boundary constraints (Part 1).',
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
                    'topic': 'Discrete Mathematics Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Discrete Mathematics scenario under boundary constraints (Part 2).',
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
                    'topic': 'Discrete Mathematics Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Discrete Mathematics scenario under boundary constraints (Part 3).',
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
                    'topic': 'Discrete Mathematics Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Discrete Mathematics scenario under boundary constraints (Part 4).',
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
                    'topic': 'Discrete Mathematics Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Discrete Mathematics scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-201-FINAL',
            'title': 'Discrete Mathematics Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Discrete Mathematics Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Discrete Mathematics.',
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
                    'topic': 'Discrete Mathematics Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Discrete Mathematics.',
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
                    'topic': 'Discrete Mathematics Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Discrete Mathematics.',
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
                    'topic': 'Discrete Mathematics Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Discrete Mathematics.',
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
                    'topic': 'Discrete Mathematics Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Discrete Mathematics.',
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
        'course_code': 'CS-202',
        'course_title': 'Data Structures & Algorithms',
        'midterm_exam': {
            'paper_code': 'CS-202-MIDTERM',
            'title': 'Data Structures & Algorithms Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Data Structures & Algorithms Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Data Structures & Algorithms scenario under boundary constraints (Part 1).',
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
                    'topic': 'Data Structures & Algorithms Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Data Structures & Algorithms scenario under boundary constraints (Part 2).',
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
                    'topic': 'Data Structures & Algorithms Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Data Structures & Algorithms scenario under boundary constraints (Part 3).',
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
                    'topic': 'Data Structures & Algorithms Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Data Structures & Algorithms scenario under boundary constraints (Part 4).',
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
                    'topic': 'Data Structures & Algorithms Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Data Structures & Algorithms scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-202-FINAL',
            'title': 'Data Structures & Algorithms Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Data Structures & Algorithms Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Data Structures & Algorithms.',
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
                    'topic': 'Data Structures & Algorithms Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Data Structures & Algorithms.',
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
                    'topic': 'Data Structures & Algorithms Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Data Structures & Algorithms.',
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
                    'topic': 'Data Structures & Algorithms Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Data Structures & Algorithms.',
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
                    'topic': 'Data Structures & Algorithms Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Data Structures & Algorithms.',
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
        'course_code': 'CS-203',
        'course_title': 'Computer Organization & Architecture',
        'midterm_exam': {
            'paper_code': 'CS-203-MIDTERM',
            'title': 'Computer Organization & Architecture Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Computer Organization & Architecture Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Organization & Architecture scenario under boundary constraints (Part 1).',
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
                    'topic': 'Computer Organization & Architecture Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Organization & Architecture scenario under boundary constraints (Part 2).',
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
                    'topic': 'Computer Organization & Architecture Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Organization & Architecture scenario under boundary constraints (Part 3).',
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
                    'topic': 'Computer Organization & Architecture Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Organization & Architecture scenario under boundary constraints (Part 4).',
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
                    'topic': 'Computer Organization & Architecture Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Organization & Architecture scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-203-FINAL',
            'title': 'Computer Organization & Architecture Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Computer Organization & Architecture Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Organization & Architecture.',
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
                    'topic': 'Computer Organization & Architecture Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Organization & Architecture.',
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
                    'topic': 'Computer Organization & Architecture Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Organization & Architecture.',
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
                    'topic': 'Computer Organization & Architecture Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Organization & Architecture.',
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
                    'topic': 'Computer Organization & Architecture Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Organization & Architecture.',
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
        'course_code': 'CS-204',
        'course_title': 'Design & Analysis of Algorithms',
        'midterm_exam': {
            'paper_code': 'CS-204-MIDTERM',
            'title': 'Design & Analysis of Algorithms Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Design & Analysis of Algorithms Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design & Analysis of Algorithms scenario under boundary constraints (Part 1).',
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
                    'topic': 'Design & Analysis of Algorithms Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design & Analysis of Algorithms scenario under boundary constraints (Part 2).',
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
                    'topic': 'Design & Analysis of Algorithms Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design & Analysis of Algorithms scenario under boundary constraints (Part 3).',
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
                    'topic': 'Design & Analysis of Algorithms Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design & Analysis of Algorithms scenario under boundary constraints (Part 4).',
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
                    'topic': 'Design & Analysis of Algorithms Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design & Analysis of Algorithms scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-204-FINAL',
            'title': 'Design & Analysis of Algorithms Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Design & Analysis of Algorithms Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design & Analysis of Algorithms.',
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
                    'topic': 'Design & Analysis of Algorithms Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design & Analysis of Algorithms.',
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
                    'topic': 'Design & Analysis of Algorithms Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design & Analysis of Algorithms.',
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
                    'topic': 'Design & Analysis of Algorithms Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design & Analysis of Algorithms.',
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
                    'topic': 'Design & Analysis of Algorithms Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design & Analysis of Algorithms.',
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
        'course_code': 'CS-301',
        'course_title': 'Operating Systems Principles',
        'midterm_exam': {
            'paper_code': 'CS-301-MIDTERM',
            'title': 'Operating Systems Principles Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Operating Systems Principles Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Operating Systems Principles scenario under boundary constraints (Part 1).',
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
                    'topic': 'Operating Systems Principles Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Operating Systems Principles scenario under boundary constraints (Part 2).',
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
                    'topic': 'Operating Systems Principles Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Operating Systems Principles scenario under boundary constraints (Part 3).',
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
                    'topic': 'Operating Systems Principles Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Operating Systems Principles scenario under boundary constraints (Part 4).',
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
                    'topic': 'Operating Systems Principles Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Operating Systems Principles scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-301-FINAL',
            'title': 'Operating Systems Principles Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Operating Systems Principles Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Operating Systems Principles.',
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
                    'topic': 'Operating Systems Principles Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Operating Systems Principles.',
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
                    'topic': 'Operating Systems Principles Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Operating Systems Principles.',
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
                    'topic': 'Operating Systems Principles Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Operating Systems Principles.',
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
                    'topic': 'Operating Systems Principles Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Operating Systems Principles.',
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
        'course_code': 'CS-302',
        'course_title': 'Database Management Systems',
        'midterm_exam': {
            'paper_code': 'CS-302-MIDTERM',
            'title': 'Database Management Systems Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Database Management Systems Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Database Management Systems scenario under boundary constraints (Part 1).',
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
                    'topic': 'Database Management Systems Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Database Management Systems scenario under boundary constraints (Part 2).',
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
                    'topic': 'Database Management Systems Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Database Management Systems scenario under boundary constraints (Part 3).',
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
                    'topic': 'Database Management Systems Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Database Management Systems scenario under boundary constraints (Part 4).',
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
                    'topic': 'Database Management Systems Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Database Management Systems scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-302-FINAL',
            'title': 'Database Management Systems Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Database Management Systems Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Database Management Systems.',
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
                    'topic': 'Database Management Systems Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Database Management Systems.',
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
                    'topic': 'Database Management Systems Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Database Management Systems.',
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
                    'topic': 'Database Management Systems Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Database Management Systems.',
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
                    'topic': 'Database Management Systems Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Database Management Systems.',
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
        'course_code': 'CS-303',
        'course_title': 'Computer Networks & Protocols',
        'midterm_exam': {
            'paper_code': 'CS-303-MIDTERM',
            'title': 'Computer Networks & Protocols Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Computer Networks & Protocols Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Networks & Protocols scenario under boundary constraints (Part 1).',
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
                    'topic': 'Computer Networks & Protocols Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Networks & Protocols scenario under boundary constraints (Part 2).',
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
                    'topic': 'Computer Networks & Protocols Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Networks & Protocols scenario under boundary constraints (Part 3).',
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
                    'topic': 'Computer Networks & Protocols Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Networks & Protocols scenario under boundary constraints (Part 4).',
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
                    'topic': 'Computer Networks & Protocols Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer Networks & Protocols scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-303-FINAL',
            'title': 'Computer Networks & Protocols Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Computer Networks & Protocols Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Networks & Protocols.',
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
                    'topic': 'Computer Networks & Protocols Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Networks & Protocols.',
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
                    'topic': 'Computer Networks & Protocols Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Networks & Protocols.',
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
                    'topic': 'Computer Networks & Protocols Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Networks & Protocols.',
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
                    'topic': 'Computer Networks & Protocols Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer Networks & Protocols.',
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
        'course_code': 'CS-304',
        'course_title': 'Theory of Computation & Automata',
        'midterm_exam': {
            'paper_code': 'CS-304-MIDTERM',
            'title': 'Theory of Computation & Automata Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Theory of Computation & Automata Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Theory of Computation & Automata scenario under boundary constraints (Part 1).',
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
                    'topic': 'Theory of Computation & Automata Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Theory of Computation & Automata scenario under boundary constraints (Part 2).',
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
                    'topic': 'Theory of Computation & Automata Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Theory of Computation & Automata scenario under boundary constraints (Part 3).',
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
                    'topic': 'Theory of Computation & Automata Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Theory of Computation & Automata scenario under boundary constraints (Part 4).',
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
                    'topic': 'Theory of Computation & Automata Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Theory of Computation & Automata scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-304-FINAL',
            'title': 'Theory of Computation & Automata Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Theory of Computation & Automata Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Theory of Computation & Automata.',
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
                    'topic': 'Theory of Computation & Automata Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Theory of Computation & Automata.',
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
                    'topic': 'Theory of Computation & Automata Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Theory of Computation & Automata.',
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
                    'topic': 'Theory of Computation & Automata Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Theory of Computation & Automata.',
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
                    'topic': 'Theory of Computation & Automata Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Theory of Computation & Automata.',
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
        'course_code': 'CS-401',
        'course_title': 'Compiler Design & Translation',
        'midterm_exam': {
            'paper_code': 'CS-401-MIDTERM',
            'title': 'Compiler Design & Translation Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Compiler Design & Translation Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Compiler Design & Translation scenario under boundary constraints (Part 1).',
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
                    'topic': 'Compiler Design & Translation Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Compiler Design & Translation scenario under boundary constraints (Part 2).',
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
                    'topic': 'Compiler Design & Translation Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Compiler Design & Translation scenario under boundary constraints (Part 3).',
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
                    'topic': 'Compiler Design & Translation Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Compiler Design & Translation scenario under boundary constraints (Part 4).',
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
                    'topic': 'Compiler Design & Translation Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Compiler Design & Translation scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-401-FINAL',
            'title': 'Compiler Design & Translation Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Compiler Design & Translation Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Compiler Design & Translation.',
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
                    'topic': 'Compiler Design & Translation Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Compiler Design & Translation.',
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
                    'topic': 'Compiler Design & Translation Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Compiler Design & Translation.',
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
                    'topic': 'Compiler Design & Translation Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Compiler Design & Translation.',
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
                    'topic': 'Compiler Design & Translation Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Compiler Design & Translation.',
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
        'course_code': 'CS-402',
        'course_title': 'Distributed Systems & Cloud',
        'midterm_exam': {
            'paper_code': 'CS-402-MIDTERM',
            'title': 'Distributed Systems & Cloud Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Distributed Systems & Cloud Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Distributed Systems & Cloud scenario under boundary constraints (Part 1).',
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
                    'topic': 'Distributed Systems & Cloud Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Distributed Systems & Cloud scenario under boundary constraints (Part 2).',
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
                    'topic': 'Distributed Systems & Cloud Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Distributed Systems & Cloud scenario under boundary constraints (Part 3).',
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
                    'topic': 'Distributed Systems & Cloud Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Distributed Systems & Cloud scenario under boundary constraints (Part 4).',
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
                    'topic': 'Distributed Systems & Cloud Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Distributed Systems & Cloud scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-402-FINAL',
            'title': 'Distributed Systems & Cloud Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Distributed Systems & Cloud Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Distributed Systems & Cloud.',
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
                    'topic': 'Distributed Systems & Cloud Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Distributed Systems & Cloud.',
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
                    'topic': 'Distributed Systems & Cloud Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Distributed Systems & Cloud.',
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
                    'topic': 'Distributed Systems & Cloud Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Distributed Systems & Cloud.',
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
                    'topic': 'Distributed Systems & Cloud Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Distributed Systems & Cloud.',
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
        'course_code': 'CS-403',
        'course_title': 'Software Testing & Quality Assurance',
        'midterm_exam': {
            'paper_code': 'CS-403-MIDTERM',
            'title': 'Software Testing & Quality Assurance Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Software Testing & Quality Assurance Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Software Testing & Quality Assurance scenario under boundary constraints (Part 1).',
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
                    'topic': 'Software Testing & Quality Assurance Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Software Testing & Quality Assurance scenario under boundary constraints (Part 2).',
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
                    'topic': 'Software Testing & Quality Assurance Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Software Testing & Quality Assurance scenario under boundary constraints (Part 3).',
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
                    'topic': 'Software Testing & Quality Assurance Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Software Testing & Quality Assurance scenario under boundary constraints (Part 4).',
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
                    'topic': 'Software Testing & Quality Assurance Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Software Testing & Quality Assurance scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-403-FINAL',
            'title': 'Software Testing & Quality Assurance Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Software Testing & Quality Assurance Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Software Testing & Quality Assurance.',
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
                    'topic': 'Software Testing & Quality Assurance Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Software Testing & Quality Assurance.',
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
                    'topic': 'Software Testing & Quality Assurance Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Software Testing & Quality Assurance.',
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
                    'topic': 'Software Testing & Quality Assurance Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Software Testing & Quality Assurance.',
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
                    'topic': 'Software Testing & Quality Assurance Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Software Testing & Quality Assurance.',
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
        'course_code': 'CS-404',
        'course_title': 'Modern Web Engineering & APIs',
        'midterm_exam': {
            'paper_code': 'CS-404-MIDTERM',
            'title': 'Modern Web Engineering & APIs Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Modern Web Engineering & APIs Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Modern Web Engineering & APIs scenario under boundary constraints (Part 1).',
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
                    'topic': 'Modern Web Engineering & APIs Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Modern Web Engineering & APIs scenario under boundary constraints (Part 2).',
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
                    'topic': 'Modern Web Engineering & APIs Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Modern Web Engineering & APIs scenario under boundary constraints (Part 3).',
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
                    'topic': 'Modern Web Engineering & APIs Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Modern Web Engineering & APIs scenario under boundary constraints (Part 4).',
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
                    'topic': 'Modern Web Engineering & APIs Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Modern Web Engineering & APIs scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-404-FINAL',
            'title': 'Modern Web Engineering & APIs Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Modern Web Engineering & APIs Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Modern Web Engineering & APIs.',
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
                    'topic': 'Modern Web Engineering & APIs Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Modern Web Engineering & APIs.',
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
                    'topic': 'Modern Web Engineering & APIs Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Modern Web Engineering & APIs.',
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
                    'topic': 'Modern Web Engineering & APIs Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Modern Web Engineering & APIs.',
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
                    'topic': 'Modern Web Engineering & APIs Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Modern Web Engineering & APIs.',
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
        'course_code': 'CS-405',
        'course_title': 'Senior Software Engineering Capstone',
        'midterm_exam': {
            'paper_code': 'CS-405-MIDTERM',
            'title': 'Senior Software Engineering Capstone Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Senior Software Engineering Capstone Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Software Engineering Capstone scenario under boundary constraints (Part 1).',
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
                    'topic': 'Senior Software Engineering Capstone Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Software Engineering Capstone scenario under boundary constraints (Part 2).',
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
                    'topic': 'Senior Software Engineering Capstone Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Software Engineering Capstone scenario under boundary constraints (Part 3).',
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
                    'topic': 'Senior Software Engineering Capstone Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Software Engineering Capstone scenario under boundary constraints (Part 4).',
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
                    'topic': 'Senior Software Engineering Capstone Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Software Engineering Capstone scenario under boundary constraints (Part 5).',
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
            'paper_code': 'CS-405-FINAL',
            'title': 'Senior Software Engineering Capstone Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Senior Software Engineering Capstone Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Software Engineering Capstone.',
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
                    'topic': 'Senior Software Engineering Capstone Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Software Engineering Capstone.',
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
                    'topic': 'Senior Software Engineering Capstone Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Software Engineering Capstone.',
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
                    'topic': 'Senior Software Engineering Capstone Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Software Engineering Capstone.',
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
                    'topic': 'Senior Software Engineering Capstone Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Software Engineering Capstone.',
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
