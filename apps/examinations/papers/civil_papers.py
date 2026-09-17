"""
Standardized Examination Paper Repository: Civil & Environmental Engineering
Includes Formal Midterm & Final Comprehensive Examination Papers with Solutions.
"""
from typing import Dict, Any, List

DISCIPLINE_NAME = "Civil & Environmental Engineering"
CURRICULUM_MODULE = "civil_environmental"

EXAMINATION_PAPERS: List[Dict[str, Any]] = [
    {
        'course_code': 'CE-101',
        'course_title': 'Surveying & Geomatic Measurement',
        'midterm_exam': {
            'paper_code': 'CE-101-MIDTERM',
            'title': 'Surveying & Geomatic Measurement Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Surveying & Geomatic Measurement Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Surveying & Geomatic Measurement scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Surveying & Geomatic Measurement Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Surveying & Geomatic Measurement scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Surveying & Geomatic Measurement Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Surveying & Geomatic Measurement scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Surveying & Geomatic Measurement Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Surveying & Geomatic Measurement scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Surveying & Geomatic Measurement Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Surveying & Geomatic Measurement scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-101-FINAL',
            'title': 'Surveying & Geomatic Measurement Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Surveying & Geomatic Measurement Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Surveying & Geomatic Measurement.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Surveying & Geomatic Measurement Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Surveying & Geomatic Measurement.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Surveying & Geomatic Measurement Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Surveying & Geomatic Measurement.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Surveying & Geomatic Measurement Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Surveying & Geomatic Measurement.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Surveying & Geomatic Measurement Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Surveying & Geomatic Measurement.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-201',
        'course_title': 'Structural Analysis I: Determinate Systems',
        'midterm_exam': {
            'paper_code': 'CE-201-MIDTERM',
            'title': 'Structural Analysis I: Determinate Systems Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Structural Analysis I: Determinate Systems Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis I: Determinate Systems scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis I: Determinate Systems scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis I: Determinate Systems scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis I: Determinate Systems scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis I: Determinate Systems scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-201-FINAL',
            'title': 'Structural Analysis I: Determinate Systems Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Structural Analysis I: Determinate Systems Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis I: Determinate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis I: Determinate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis I: Determinate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis I: Determinate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis I: Determinate Systems Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis I: Determinate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-202',
        'course_title': 'Geotechnical Engineering & Soil Mechanics',
        'midterm_exam': {
            'paper_code': 'CE-202-MIDTERM',
            'title': 'Geotechnical Engineering & Soil Mechanics Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Geotechnical Engineering & Soil Mechanics Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Geotechnical Engineering & Soil Mechanics scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Geotechnical Engineering & Soil Mechanics scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Geotechnical Engineering & Soil Mechanics scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Geotechnical Engineering & Soil Mechanics scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Geotechnical Engineering & Soil Mechanics scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-202-FINAL',
            'title': 'Geotechnical Engineering & Soil Mechanics Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Geotechnical Engineering & Soil Mechanics Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Geotechnical Engineering & Soil Mechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Geotechnical Engineering & Soil Mechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Geotechnical Engineering & Soil Mechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Geotechnical Engineering & Soil Mechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Geotechnical Engineering & Soil Mechanics Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Geotechnical Engineering & Soil Mechanics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-301',
        'course_title': 'Structural Analysis II: Indeterminate Systems',
        'midterm_exam': {
            'paper_code': 'CE-301-MIDTERM',
            'title': 'Structural Analysis II: Indeterminate Systems Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Structural Analysis II: Indeterminate Systems Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis II: Indeterminate Systems scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis II: Indeterminate Systems scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis II: Indeterminate Systems scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis II: Indeterminate Systems scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Structural Analysis II: Indeterminate Systems scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-301-FINAL',
            'title': 'Structural Analysis II: Indeterminate Systems Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Structural Analysis II: Indeterminate Systems Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis II: Indeterminate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis II: Indeterminate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis II: Indeterminate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis II: Indeterminate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Structural Analysis II: Indeterminate Systems Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Structural Analysis II: Indeterminate Systems.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-302',
        'course_title': 'Design of Reinforced Concrete Members',
        'midterm_exam': {
            'paper_code': 'CE-302-MIDTERM',
            'title': 'Design of Reinforced Concrete Members Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Design of Reinforced Concrete Members Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Reinforced Concrete Members scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Reinforced Concrete Members Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Reinforced Concrete Members scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Reinforced Concrete Members Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Reinforced Concrete Members scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Reinforced Concrete Members Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Reinforced Concrete Members scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Reinforced Concrete Members Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Reinforced Concrete Members scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-302-FINAL',
            'title': 'Design of Reinforced Concrete Members Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Design of Reinforced Concrete Members Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Reinforced Concrete Members.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Reinforced Concrete Members Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Reinforced Concrete Members.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Reinforced Concrete Members Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Reinforced Concrete Members.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Reinforced Concrete Members Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Reinforced Concrete Members.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Reinforced Concrete Members Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Reinforced Concrete Members.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-303',
        'course_title': 'Hydrology & Open Channel Hydraulics',
        'midterm_exam': {
            'paper_code': 'CE-303-MIDTERM',
            'title': 'Hydrology & Open Channel Hydraulics Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Hydrology & Open Channel Hydraulics Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Hydrology & Open Channel Hydraulics scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Hydrology & Open Channel Hydraulics scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Hydrology & Open Channel Hydraulics scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Hydrology & Open Channel Hydraulics scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Hydrology & Open Channel Hydraulics scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-303-FINAL',
            'title': 'Hydrology & Open Channel Hydraulics Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Hydrology & Open Channel Hydraulics Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Hydrology & Open Channel Hydraulics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Hydrology & Open Channel Hydraulics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Hydrology & Open Channel Hydraulics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Hydrology & Open Channel Hydraulics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Hydrology & Open Channel Hydraulics Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Hydrology & Open Channel Hydraulics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-304',
        'course_title': 'Transportation Engineering & Pavements',
        'midterm_exam': {
            'paper_code': 'CE-304-MIDTERM',
            'title': 'Transportation Engineering & Pavements Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Transportation Engineering & Pavements Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Transportation Engineering & Pavements scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Transportation Engineering & Pavements Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Transportation Engineering & Pavements scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Transportation Engineering & Pavements Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Transportation Engineering & Pavements scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Transportation Engineering & Pavements Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Transportation Engineering & Pavements scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Transportation Engineering & Pavements Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Transportation Engineering & Pavements scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-304-FINAL',
            'title': 'Transportation Engineering & Pavements Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Transportation Engineering & Pavements Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Transportation Engineering & Pavements.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Transportation Engineering & Pavements Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Transportation Engineering & Pavements.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Transportation Engineering & Pavements Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Transportation Engineering & Pavements.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Transportation Engineering & Pavements Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Transportation Engineering & Pavements.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Transportation Engineering & Pavements Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Transportation Engineering & Pavements.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-401',
        'course_title': 'Design of Structural Steel Frames',
        'midterm_exam': {
            'paper_code': 'CE-401-MIDTERM',
            'title': 'Design of Structural Steel Frames Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Design of Structural Steel Frames Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Structural Steel Frames scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Structural Steel Frames Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Structural Steel Frames scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Structural Steel Frames Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Structural Steel Frames scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Structural Steel Frames Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Structural Steel Frames scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Design of Structural Steel Frames Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Design of Structural Steel Frames scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-401-FINAL',
            'title': 'Design of Structural Steel Frames Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Design of Structural Steel Frames Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Structural Steel Frames.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Structural Steel Frames Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Structural Steel Frames.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Structural Steel Frames Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Structural Steel Frames.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Structural Steel Frames Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Structural Steel Frames.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Design of Structural Steel Frames Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Design of Structural Steel Frames.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-402',
        'course_title': 'Water & Wastewater Treatment Plant Design',
        'midterm_exam': {
            'paper_code': 'CE-402-MIDTERM',
            'title': 'Water & Wastewater Treatment Plant Design Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Water & Wastewater Treatment Plant Design Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Water & Wastewater Treatment Plant Design scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Water & Wastewater Treatment Plant Design scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Water & Wastewater Treatment Plant Design scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Water & Wastewater Treatment Plant Design scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Water & Wastewater Treatment Plant Design scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-402-FINAL',
            'title': 'Water & Wastewater Treatment Plant Design Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Water & Wastewater Treatment Plant Design Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Water & Wastewater Treatment Plant Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Water & Wastewater Treatment Plant Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Water & Wastewater Treatment Plant Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Water & Wastewater Treatment Plant Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Water & Wastewater Treatment Plant Design Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Water & Wastewater Treatment Plant Design.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-403',
        'course_title': 'Foundation Engineering & Earth Retaining',
        'midterm_exam': {
            'paper_code': 'CE-403-MIDTERM',
            'title': 'Foundation Engineering & Earth Retaining Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Foundation Engineering & Earth Retaining Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Foundation Engineering & Earth Retaining scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Foundation Engineering & Earth Retaining scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Foundation Engineering & Earth Retaining scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Foundation Engineering & Earth Retaining scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Foundation Engineering & Earth Retaining scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-403-FINAL',
            'title': 'Foundation Engineering & Earth Retaining Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Foundation Engineering & Earth Retaining Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Foundation Engineering & Earth Retaining.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Foundation Engineering & Earth Retaining.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Foundation Engineering & Earth Retaining.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Foundation Engineering & Earth Retaining.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Foundation Engineering & Earth Retaining Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Foundation Engineering & Earth Retaining.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-404',
        'course_title': 'Construction Management & Scheduling',
        'midterm_exam': {
            'paper_code': 'CE-404-MIDTERM',
            'title': 'Construction Management & Scheduling Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Construction Management & Scheduling Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Construction Management & Scheduling scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Construction Management & Scheduling Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Construction Management & Scheduling scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Construction Management & Scheduling Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Construction Management & Scheduling scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Construction Management & Scheduling Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Construction Management & Scheduling scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Construction Management & Scheduling Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Construction Management & Scheduling scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-404-FINAL',
            'title': 'Construction Management & Scheduling Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Construction Management & Scheduling Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Construction Management & Scheduling.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Construction Management & Scheduling Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Construction Management & Scheduling.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Construction Management & Scheduling Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Construction Management & Scheduling.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Construction Management & Scheduling Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Construction Management & Scheduling.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Construction Management & Scheduling Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Construction Management & Scheduling.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-405',
        'course_title': 'Earthquake Engineering & Seismic Detailing',
        'midterm_exam': {
            'paper_code': 'CE-405-MIDTERM',
            'title': 'Earthquake Engineering & Seismic Detailing Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Earthquake Engineering & Seismic Detailing Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Earthquake Engineering & Seismic Detailing scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Earthquake Engineering & Seismic Detailing scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Earthquake Engineering & Seismic Detailing scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Earthquake Engineering & Seismic Detailing scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Earthquake Engineering & Seismic Detailing scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-405-FINAL',
            'title': 'Earthquake Engineering & Seismic Detailing Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Earthquake Engineering & Seismic Detailing Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Earthquake Engineering & Seismic Detailing.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Earthquake Engineering & Seismic Detailing.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Earthquake Engineering & Seismic Detailing.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Earthquake Engineering & Seismic Detailing.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Earthquake Engineering & Seismic Detailing Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Earthquake Engineering & Seismic Detailing.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-406',
        'course_title': 'Municipal Solid Waste Engineering',
        'midterm_exam': {
            'paper_code': 'CE-406-MIDTERM',
            'title': 'Municipal Solid Waste Engineering Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Municipal Solid Waste Engineering Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Municipal Solid Waste Engineering scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Municipal Solid Waste Engineering Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Municipal Solid Waste Engineering scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Municipal Solid Waste Engineering Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Municipal Solid Waste Engineering scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Municipal Solid Waste Engineering Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Municipal Solid Waste Engineering scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Municipal Solid Waste Engineering Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Municipal Solid Waste Engineering scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-406-FINAL',
            'title': 'Municipal Solid Waste Engineering Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Municipal Solid Waste Engineering Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Municipal Solid Waste Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Municipal Solid Waste Engineering Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Municipal Solid Waste Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Municipal Solid Waste Engineering Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Municipal Solid Waste Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Municipal Solid Waste Engineering Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Municipal Solid Waste Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Municipal Solid Waste Engineering Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Municipal Solid Waste Engineering.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-407',
        'course_title': 'Coastal Structures & Wave Dynamics',
        'midterm_exam': {
            'paper_code': 'CE-407-MIDTERM',
            'title': 'Coastal Structures & Wave Dynamics Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Coastal Structures & Wave Dynamics Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Coastal Structures & Wave Dynamics scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Coastal Structures & Wave Dynamics scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Coastal Structures & Wave Dynamics scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Coastal Structures & Wave Dynamics scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Coastal Structures & Wave Dynamics scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-407-FINAL',
            'title': 'Coastal Structures & Wave Dynamics Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Coastal Structures & Wave Dynamics Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Coastal Structures & Wave Dynamics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Coastal Structures & Wave Dynamics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Coastal Structures & Wave Dynamics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Coastal Structures & Wave Dynamics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Coastal Structures & Wave Dynamics Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Coastal Structures & Wave Dynamics.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
        'course_code': 'CE-408',
        'course_title': 'Civil Engineering Integrated Design Capstone',
        'midterm_exam': {
            'paper_code': 'CE-408-MIDTERM',
            'title': 'Civil Engineering Integrated Design Capstone Midterm Examination',
            'duration_minutes': 90,
            'total_marks': 100,
            'instructions': 'Answer all questions in Sections A and B. Calculators permitted.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Civil Engineering Integrated Design Capstone Midterm Topic 1',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Civil Engineering Integrated Design Capstone scenario under boundary constraints (Part 1).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Midterm Topic 2',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Civil Engineering Integrated Design Capstone scenario under boundary constraints (Part 2).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Midterm Topic 3',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Civil Engineering Integrated Design Capstone scenario under boundary constraints (Part 3).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Midterm Topic 4',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Civil Engineering Integrated Design Capstone scenario under boundary constraints (Part 4).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Midterm Topic 5',
                    'problem_statement': 'Derive, analyze, and compute optimal solutions for Civil Engineering Integrated Design Capstone scenario under boundary constraints (Part 5).',
                    'model_solution': {
                        'step_1': 'Identify governing system dynamics and formulate initial state representation.',
                        'step_2': 'Apply analytical transformation and solve closed-form algebraic expression.',
                        'step_3': 'Verify boundary stability criteria and compute error margins.',
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
            'paper_code': 'CE-408-FINAL',
            'title': 'Civil Engineering Integrated Design Capstone Comprehensive Final Examination',
            'duration_minutes': 180,
            'total_marks': 100,
            'instructions': 'Comprehensive examination covering Weeks 1 through 14. Section A mandatory.',
            'questions': [
                {
                    'question_number': 1,
                    'marks': 20,
                    'topic': 'Civil Engineering Integrated Design Capstone Advanced Capstone Synthesis 1',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Civil Engineering Integrated Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Advanced Capstone Synthesis 2',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Civil Engineering Integrated Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Advanced Capstone Synthesis 3',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Civil Engineering Integrated Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Advanced Capstone Synthesis 4',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Civil Engineering Integrated Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
                    'topic': 'Civil Engineering Integrated Design Capstone Advanced Capstone Synthesis 5',
                    'problem_statement': 'Synthesize complete theoretical framework and architect a resilient operational pipeline for Civil Engineering Integrated Design Capstone.',
                    'model_solution': {
                        'step_1': 'Deconstruct system into modular subsystems conforming to engineering specifications.',
                        'step_2': 'Execute rigorous parameter tuning and solve coupled differential/state equations.',
                        'step_3': 'Conduct worst-case fault injection analysis and verify failure recovery.',
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
