"""
Standardized Examination Paper Repository: Mechanical & Aerospace Engineering
Includes Formal Midterm & Final Comprehensive Examination Papers with Solutions.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Mechanical & Aerospace Engineering"
CURRICULUM_MODULE = "mechanical_engineering"

EXAMINATION_PAPERS: List[Dict[str, Any]] = [
    {
        'course_code': 'ME-101',
        'course_title': 'Engineering Statics & Vector Equilibrium',
        'midterm_exam': {
            'paper_code': 'ME-101-MIDTERM',
            'title': 'Engineering Statics & Vector Equilibrium Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Engineering Statics & Vector Equilibrium Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Statics & Vector Equilibrium scenario under boundary constraints (Part 1).',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Statics & Vector Equilibrium scenario under boundary constraints (Part 2).',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Statics & Vector Equilibrium scenario under boundary constraints (Part 3).',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Statics & Vector Equilibrium scenario under boundary constraints (Part 4).',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Statics & Vector Equilibrium scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-101-FINAL',
            'title': 'Engineering Statics & Vector Equilibrium Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Engineering Statics & Vector Equilibrium Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Statics & Vector Equilibrium.',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Statics & Vector Equilibrium.',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Statics & Vector Equilibrium.',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Statics & Vector Equilibrium.',
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
                    'topic': 'Engineering Statics & Vector Equilibrium Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Statics & Vector Equilibrium.',
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
        'course_code': 'ME-102',
        'course_title': 'Engineering Dynamics & Kinematics',
        'midterm_exam': {
            'paper_code': 'ME-102-MIDTERM',
            'title': 'Engineering Dynamics & Kinematics Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Engineering Dynamics & Kinematics Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Dynamics & Kinematics scenario under boundary constraints (Part 1).',
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
                    'topic': 'Engineering Dynamics & Kinematics Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Dynamics & Kinematics scenario under boundary constraints (Part 2).',
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
                    'topic': 'Engineering Dynamics & Kinematics Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Dynamics & Kinematics scenario under boundary constraints (Part 3).',
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
                    'topic': 'Engineering Dynamics & Kinematics Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Dynamics & Kinematics scenario under boundary constraints (Part 4).',
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
                    'topic': 'Engineering Dynamics & Kinematics Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Engineering Dynamics & Kinematics scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-102-FINAL',
            'title': 'Engineering Dynamics & Kinematics Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Engineering Dynamics & Kinematics Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Dynamics & Kinematics.',
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
                    'topic': 'Engineering Dynamics & Kinematics Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Dynamics & Kinematics.',
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
                    'topic': 'Engineering Dynamics & Kinematics Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Dynamics & Kinematics.',
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
                    'topic': 'Engineering Dynamics & Kinematics Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Dynamics & Kinematics.',
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
                    'topic': 'Engineering Dynamics & Kinematics Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Engineering Dynamics & Kinematics.',
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
        'course_code': 'ME-201',
        'course_title': 'Mechanics of Deformable Materials',
        'midterm_exam': {
            'paper_code': 'ME-201-MIDTERM',
            'title': 'Mechanics of Deformable Materials Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechanics of Deformable Materials Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanics of Deformable Materials scenario under boundary constraints (Part 1).',
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
                    'topic': 'Mechanics of Deformable Materials Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanics of Deformable Materials scenario under boundary constraints (Part 2).',
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
                    'topic': 'Mechanics of Deformable Materials Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanics of Deformable Materials scenario under boundary constraints (Part 3).',
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
                    'topic': 'Mechanics of Deformable Materials Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanics of Deformable Materials scenario under boundary constraints (Part 4).',
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
                    'topic': 'Mechanics of Deformable Materials Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanics of Deformable Materials scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-201-FINAL',
            'title': 'Mechanics of Deformable Materials Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechanics of Deformable Materials Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanics of Deformable Materials.',
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
                    'topic': 'Mechanics of Deformable Materials Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanics of Deformable Materials.',
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
                    'topic': 'Mechanics of Deformable Materials Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanics of Deformable Materials.',
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
                    'topic': 'Mechanics of Deformable Materials Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanics of Deformable Materials.',
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
                    'topic': 'Mechanics of Deformable Materials Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanics of Deformable Materials.',
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
        'course_code': 'ME-202',
        'course_title': 'Thermodynamics Principles & Cycles',
        'midterm_exam': {
            'paper_code': 'ME-202-MIDTERM',
            'title': 'Thermodynamics Principles & Cycles Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Thermodynamics Principles & Cycles Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Thermodynamics Principles & Cycles scenario under boundary constraints (Part 1).',
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
                    'topic': 'Thermodynamics Principles & Cycles Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Thermodynamics Principles & Cycles scenario under boundary constraints (Part 2).',
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
                    'topic': 'Thermodynamics Principles & Cycles Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Thermodynamics Principles & Cycles scenario under boundary constraints (Part 3).',
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
                    'topic': 'Thermodynamics Principles & Cycles Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Thermodynamics Principles & Cycles scenario under boundary constraints (Part 4).',
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
                    'topic': 'Thermodynamics Principles & Cycles Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Thermodynamics Principles & Cycles scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-202-FINAL',
            'title': 'Thermodynamics Principles & Cycles Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Thermodynamics Principles & Cycles Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Thermodynamics Principles & Cycles.',
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
                    'topic': 'Thermodynamics Principles & Cycles Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Thermodynamics Principles & Cycles.',
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
                    'topic': 'Thermodynamics Principles & Cycles Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Thermodynamics Principles & Cycles.',
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
                    'topic': 'Thermodynamics Principles & Cycles Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Thermodynamics Principles & Cycles.',
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
                    'topic': 'Thermodynamics Principles & Cycles Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Thermodynamics Principles & Cycles.',
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
        'course_code': 'ME-203',
        'course_title': 'Computer-Aided Design (CAD) & SolidWorks',
        'midterm_exam': {
            'paper_code': 'ME-203-MIDTERM',
            'title': 'Computer-Aided Design (CAD) & SolidWorks Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer-Aided Design (CAD) & SolidWorks scenario under boundary constraints (Part 1).',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer-Aided Design (CAD) & SolidWorks scenario under boundary constraints (Part 2).',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer-Aided Design (CAD) & SolidWorks scenario under boundary constraints (Part 3).',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer-Aided Design (CAD) & SolidWorks scenario under boundary constraints (Part 4).',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Computer-Aided Design (CAD) & SolidWorks scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-203-FINAL',
            'title': 'Computer-Aided Design (CAD) & SolidWorks Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer-Aided Design (CAD) & SolidWorks.',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer-Aided Design (CAD) & SolidWorks.',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer-Aided Design (CAD) & SolidWorks.',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer-Aided Design (CAD) & SolidWorks.',
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
                    'topic': 'Computer-Aided Design (CAD) & SolidWorks Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Computer-Aided Design (CAD) & SolidWorks.',
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
        'course_code': 'ME-301',
        'course_title': 'Fluid Mechanics & Boundary Layers',
        'midterm_exam': {
            'paper_code': 'ME-301-MIDTERM',
            'title': 'Fluid Mechanics & Boundary Layers Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Fluid Mechanics & Boundary Layers Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Fluid Mechanics & Boundary Layers scenario under boundary constraints (Part 1).',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Fluid Mechanics & Boundary Layers scenario under boundary constraints (Part 2).',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Fluid Mechanics & Boundary Layers scenario under boundary constraints (Part 3).',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Fluid Mechanics & Boundary Layers scenario under boundary constraints (Part 4).',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Fluid Mechanics & Boundary Layers scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-301-FINAL',
            'title': 'Fluid Mechanics & Boundary Layers Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Fluid Mechanics & Boundary Layers Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Fluid Mechanics & Boundary Layers.',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Fluid Mechanics & Boundary Layers.',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Fluid Mechanics & Boundary Layers.',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Fluid Mechanics & Boundary Layers.',
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
                    'topic': 'Fluid Mechanics & Boundary Layers Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Fluid Mechanics & Boundary Layers.',
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
        'course_code': 'ME-302',
        'course_title': 'Heat Transfer: Conduction & Radiation',
        'midterm_exam': {
            'paper_code': 'ME-302-MIDTERM',
            'title': 'Heat Transfer: Conduction & Radiation Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Heat Transfer: Conduction & Radiation Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Heat Transfer: Conduction & Radiation scenario under boundary constraints (Part 1).',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Heat Transfer: Conduction & Radiation scenario under boundary constraints (Part 2).',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Heat Transfer: Conduction & Radiation scenario under boundary constraints (Part 3).',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Heat Transfer: Conduction & Radiation scenario under boundary constraints (Part 4).',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Heat Transfer: Conduction & Radiation scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-302-FINAL',
            'title': 'Heat Transfer: Conduction & Radiation Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Heat Transfer: Conduction & Radiation Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Heat Transfer: Conduction & Radiation.',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Heat Transfer: Conduction & Radiation.',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Heat Transfer: Conduction & Radiation.',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Heat Transfer: Conduction & Radiation.',
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
                    'topic': 'Heat Transfer: Conduction & Radiation Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Heat Transfer: Conduction & Radiation.',
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
        'course_code': 'ME-303',
        'course_title': 'Mechanical Element Design & Fatigue',
        'midterm_exam': {
            'paper_code': 'ME-303-MIDTERM',
            'title': 'Mechanical Element Design & Fatigue Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechanical Element Design & Fatigue Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Element Design & Fatigue scenario under boundary constraints (Part 1).',
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
                    'topic': 'Mechanical Element Design & Fatigue Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Element Design & Fatigue scenario under boundary constraints (Part 2).',
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
                    'topic': 'Mechanical Element Design & Fatigue Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Element Design & Fatigue scenario under boundary constraints (Part 3).',
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
                    'topic': 'Mechanical Element Design & Fatigue Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Element Design & Fatigue scenario under boundary constraints (Part 4).',
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
                    'topic': 'Mechanical Element Design & Fatigue Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Element Design & Fatigue scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-303-FINAL',
            'title': 'Mechanical Element Design & Fatigue Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechanical Element Design & Fatigue Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Element Design & Fatigue.',
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
                    'topic': 'Mechanical Element Design & Fatigue Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Element Design & Fatigue.',
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
                    'topic': 'Mechanical Element Design & Fatigue Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Element Design & Fatigue.',
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
                    'topic': 'Mechanical Element Design & Fatigue Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Element Design & Fatigue.',
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
                    'topic': 'Mechanical Element Design & Fatigue Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Element Design & Fatigue.',
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
        'course_code': 'ME-401',
        'course_title': 'Mechanical Vibrations & Modal Analysis',
        'midterm_exam': {
            'paper_code': 'ME-401-MIDTERM',
            'title': 'Mechanical Vibrations & Modal Analysis Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechanical Vibrations & Modal Analysis Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Vibrations & Modal Analysis scenario under boundary constraints (Part 1).',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Vibrations & Modal Analysis scenario under boundary constraints (Part 2).',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Vibrations & Modal Analysis scenario under boundary constraints (Part 3).',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Vibrations & Modal Analysis scenario under boundary constraints (Part 4).',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechanical Vibrations & Modal Analysis scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-401-FINAL',
            'title': 'Mechanical Vibrations & Modal Analysis Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechanical Vibrations & Modal Analysis Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Vibrations & Modal Analysis.',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Vibrations & Modal Analysis.',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Vibrations & Modal Analysis.',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Vibrations & Modal Analysis.',
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
                    'topic': 'Mechanical Vibrations & Modal Analysis Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechanical Vibrations & Modal Analysis.',
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
        'course_code': 'ME-402',
        'course_title': 'Finite Element Analysis (FEA) Simulation',
        'midterm_exam': {
            'paper_code': 'ME-402-MIDTERM',
            'title': 'Finite Element Analysis (FEA) Simulation Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Finite Element Analysis (FEA) Simulation Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Finite Element Analysis (FEA) Simulation scenario under boundary constraints (Part 1).',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Finite Element Analysis (FEA) Simulation scenario under boundary constraints (Part 2).',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Finite Element Analysis (FEA) Simulation scenario under boundary constraints (Part 3).',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Finite Element Analysis (FEA) Simulation scenario under boundary constraints (Part 4).',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Finite Element Analysis (FEA) Simulation scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-402-FINAL',
            'title': 'Finite Element Analysis (FEA) Simulation Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Finite Element Analysis (FEA) Simulation Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Finite Element Analysis (FEA) Simulation.',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Finite Element Analysis (FEA) Simulation.',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Finite Element Analysis (FEA) Simulation.',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Finite Element Analysis (FEA) Simulation.',
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
                    'topic': 'Finite Element Analysis (FEA) Simulation Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Finite Element Analysis (FEA) Simulation.',
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
        'course_code': 'ME-403',
        'course_title': 'Manufacturing Processes & Metallurgy',
        'midterm_exam': {
            'paper_code': 'ME-403-MIDTERM',
            'title': 'Manufacturing Processes & Metallurgy Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Manufacturing Processes & Metallurgy Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Manufacturing Processes & Metallurgy scenario under boundary constraints (Part 1).',
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
                    'topic': 'Manufacturing Processes & Metallurgy Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Manufacturing Processes & Metallurgy scenario under boundary constraints (Part 2).',
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
                    'topic': 'Manufacturing Processes & Metallurgy Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Manufacturing Processes & Metallurgy scenario under boundary constraints (Part 3).',
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
                    'topic': 'Manufacturing Processes & Metallurgy Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Manufacturing Processes & Metallurgy scenario under boundary constraints (Part 4).',
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
                    'topic': 'Manufacturing Processes & Metallurgy Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Manufacturing Processes & Metallurgy scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-403-FINAL',
            'title': 'Manufacturing Processes & Metallurgy Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Manufacturing Processes & Metallurgy Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Manufacturing Processes & Metallurgy.',
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
                    'topic': 'Manufacturing Processes & Metallurgy Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Manufacturing Processes & Metallurgy.',
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
                    'topic': 'Manufacturing Processes & Metallurgy Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Manufacturing Processes & Metallurgy.',
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
                    'topic': 'Manufacturing Processes & Metallurgy Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Manufacturing Processes & Metallurgy.',
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
                    'topic': 'Manufacturing Processes & Metallurgy Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Manufacturing Processes & Metallurgy.',
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
        'course_code': 'ME-404',
        'course_title': 'Mechatronics, Sensors & Actuators',
        'midterm_exam': {
            'paper_code': 'ME-404-MIDTERM',
            'title': 'Mechatronics, Sensors & Actuators Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechatronics, Sensors & Actuators Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechatronics, Sensors & Actuators scenario under boundary constraints (Part 1).',
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
                    'topic': 'Mechatronics, Sensors & Actuators Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechatronics, Sensors & Actuators scenario under boundary constraints (Part 2).',
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
                    'topic': 'Mechatronics, Sensors & Actuators Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechatronics, Sensors & Actuators scenario under boundary constraints (Part 3).',
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
                    'topic': 'Mechatronics, Sensors & Actuators Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechatronics, Sensors & Actuators scenario under boundary constraints (Part 4).',
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
                    'topic': 'Mechatronics, Sensors & Actuators Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Mechatronics, Sensors & Actuators scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-404-FINAL',
            'title': 'Mechatronics, Sensors & Actuators Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Mechatronics, Sensors & Actuators Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechatronics, Sensors & Actuators.',
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
                    'topic': 'Mechatronics, Sensors & Actuators Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechatronics, Sensors & Actuators.',
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
                    'topic': 'Mechatronics, Sensors & Actuators Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechatronics, Sensors & Actuators.',
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
                    'topic': 'Mechatronics, Sensors & Actuators Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechatronics, Sensors & Actuators.',
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
                    'topic': 'Mechatronics, Sensors & Actuators Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Mechatronics, Sensors & Actuators.',
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
        'course_code': 'ME-405',
        'course_title': 'Internal Combustion & Gas Turbines',
        'midterm_exam': {
            'paper_code': 'ME-405-MIDTERM',
            'title': 'Internal Combustion & Gas Turbines Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Internal Combustion & Gas Turbines Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Internal Combustion & Gas Turbines scenario under boundary constraints (Part 1).',
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
                    'topic': 'Internal Combustion & Gas Turbines Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Internal Combustion & Gas Turbines scenario under boundary constraints (Part 2).',
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
                    'topic': 'Internal Combustion & Gas Turbines Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Internal Combustion & Gas Turbines scenario under boundary constraints (Part 3).',
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
                    'topic': 'Internal Combustion & Gas Turbines Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Internal Combustion & Gas Turbines scenario under boundary constraints (Part 4).',
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
                    'topic': 'Internal Combustion & Gas Turbines Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Internal Combustion & Gas Turbines scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-405-FINAL',
            'title': 'Internal Combustion & Gas Turbines Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Internal Combustion & Gas Turbines Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Internal Combustion & Gas Turbines.',
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
                    'topic': 'Internal Combustion & Gas Turbines Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Internal Combustion & Gas Turbines.',
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
                    'topic': 'Internal Combustion & Gas Turbines Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Internal Combustion & Gas Turbines.',
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
                    'topic': 'Internal Combustion & Gas Turbines Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Internal Combustion & Gas Turbines.',
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
                    'topic': 'Internal Combustion & Gas Turbines Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Internal Combustion & Gas Turbines.',
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
        'course_code': 'ME-406',
        'course_title': 'Aerodynamics & Compressible Flow',
        'midterm_exam': {
            'paper_code': 'ME-406-MIDTERM',
            'title': 'Aerodynamics & Compressible Flow Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Aerodynamics & Compressible Flow Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Aerodynamics & Compressible Flow scenario under boundary constraints (Part 1).',
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
                    'topic': 'Aerodynamics & Compressible Flow Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Aerodynamics & Compressible Flow scenario under boundary constraints (Part 2).',
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
                    'topic': 'Aerodynamics & Compressible Flow Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Aerodynamics & Compressible Flow scenario under boundary constraints (Part 3).',
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
                    'topic': 'Aerodynamics & Compressible Flow Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Aerodynamics & Compressible Flow scenario under boundary constraints (Part 4).',
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
                    'topic': 'Aerodynamics & Compressible Flow Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Aerodynamics & Compressible Flow scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-406-FINAL',
            'title': 'Aerodynamics & Compressible Flow Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Aerodynamics & Compressible Flow Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Aerodynamics & Compressible Flow.',
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
                    'topic': 'Aerodynamics & Compressible Flow Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Aerodynamics & Compressible Flow.',
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
                    'topic': 'Aerodynamics & Compressible Flow Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Aerodynamics & Compressible Flow.',
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
                    'topic': 'Aerodynamics & Compressible Flow Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Aerodynamics & Compressible Flow.',
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
                    'topic': 'Aerodynamics & Compressible Flow Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Aerodynamics & Compressible Flow.',
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
        'course_code': 'ME-407',
        'course_title': 'Senior Mechanical Engineering Capstone',
        'midterm_exam': {
            'paper_code': 'ME-407-MIDTERM',
            'title': 'Senior Mechanical Engineering Capstone Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Senior Mechanical Engineering Capstone Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Mechanical Engineering Capstone scenario under boundary constraints (Part 1).',
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
                    'topic': 'Senior Mechanical Engineering Capstone Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Mechanical Engineering Capstone scenario under boundary constraints (Part 2).',
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
                    'topic': 'Senior Mechanical Engineering Capstone Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Mechanical Engineering Capstone scenario under boundary constraints (Part 3).',
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
                    'topic': 'Senior Mechanical Engineering Capstone Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Mechanical Engineering Capstone scenario under boundary constraints (Part 4).',
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
                    'topic': 'Senior Mechanical Engineering Capstone Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Senior Mechanical Engineering Capstone scenario under boundary constraints (Part 5).',
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
            'paper_code': 'ME-407-FINAL',
            'title': 'Senior Mechanical Engineering Capstone Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Senior Mechanical Engineering Capstone Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Mechanical Engineering Capstone.',
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
                    'topic': 'Senior Mechanical Engineering Capstone Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Mechanical Engineering Capstone.',
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
                    'topic': 'Senior Mechanical Engineering Capstone Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Mechanical Engineering Capstone.',
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
                    'topic': 'Senior Mechanical Engineering Capstone Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Mechanical Engineering Capstone.',
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
                    'topic': 'Senior Mechanical Engineering Capstone Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Senior Mechanical Engineering Capstone.',
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
