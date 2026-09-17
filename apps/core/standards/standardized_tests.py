"""
Standardized Examination Equivalence & Course Placement Benchmarks.
Covers Advanced Placement (AP), International Baccalaureate (IB), SAT, ACT, and GRE.
"""
from typing import Dict, Any, List

AP_EXAM_CREDIT_POLICY = {
    'AP_COMPUTER_SCIENCE_A': {
        'subject': 'Computer Science A',
        'scores': {
            5: {'credits_awarded': 4, 'equivalent_course': 'CS-101', 'placement': 'Direct enrollment into CS-102'},
            4: {'credits_awarded': 4, 'equivalent_course': 'CS-101', 'placement': 'Direct enrollment into CS-102'},
            3: {'credits_awarded': 3, 'equivalent_course': 'CS-100', 'placement': 'General Computer Science elective'}
        }
    },
    'AP_CALCULUS_BC': {
        'subject': 'Calculus BC',
        'scores': {
            5: {'credits_awarded': 8, 'equivalent_course': 'MP-101', 'placement': 'Exemption from Calculus I & II; enroll in Multivariable Calculus'},
            4: {'credits_awarded': 8, 'equivalent_course': 'MP-101', 'placement': 'Exemption from Calculus I & II'},
            3: {'credits_awarded': 4, 'equivalent_course': 'MP-101', 'placement': 'Exemption from Calculus I only'}
        }
    },
    'AP_PHYSICS_C_MECHANICS': {
        'subject': 'Physics C: Mechanics',
        'scores': {
            5: {'credits_awarded': 4, 'equivalent_course': 'MP-102', 'placement': 'Exemption from University Physics I with Lab'},
            4: {'credits_awarded': 4, 'equivalent_course': 'MP-102', 'placement': 'Exemption from University Physics I with Lab'},
            3: {'credits_awarded': 0, 'equivalent_course': None, 'placement': 'No credit awarded'}
        }
    },
    'AP_CHEMISTRY': {
        'subject': 'Chemistry',
        'scores': {
            5: {'credits_awarded': 8, 'equivalent_course': 'CHEM-101', 'placement': 'General Chemistry I & II lecture and lab waiver'},
            4: {'credits_awarded': 4, 'equivalent_course': 'CHEM-101', 'placement': 'General Chemistry I lecture and lab waiver'},
            3: {'credits_awarded': 4, 'equivalent_course': 'CHEM-100', 'placement': 'Non-majors science elective'}
        }
    },
    'AP_STATISTICS': {
        'subject': 'Statistics',
        'scores': {
            5: {'credits_awarded': 3, 'equivalent_course': 'DS-101', 'placement': 'Introductory Statistics course waiver'},
            4: {'credits_awarded': 3, 'equivalent_course': 'DS-101', 'placement': 'Introductory Statistics course waiver'},
            3: {'credits_awarded': 3, 'equivalent_course': 'MATH-110', 'placement': 'General quantitative reasoning credit'}
        }
    },
    'AP_MACROECONOMICS': {
        'subject': 'Macroeconomics',
        'scores': {
            5: {'credits_awarded': 3, 'equivalent_course': 'BA-102', 'placement': 'Principles of Macroeconomics waiver'},
            4: {'credits_awarded': 3, 'equivalent_course': 'BA-102', 'placement': 'Principles of Macroeconomics waiver'},
            3: {'credits_awarded': 3, 'equivalent_course': 'ECON-100', 'placement': 'Social science elective credit'}
        }
    },
    'AP_MICROECONOMICS': {
        'subject': 'Microeconomics',
        'scores': {
            5: {'credits_awarded': 3, 'equivalent_course': 'BA-101', 'placement': 'Principles of Microeconomics waiver'},
            4: {'credits_awarded': 3, 'equivalent_course': 'BA-101', 'placement': 'Principles of Microeconomics waiver'},
            3: {'credits_awarded': 3, 'equivalent_course': 'ECON-100', 'placement': 'Social science elective credit'}
        }
    },
    'AP_PSYCHOLOGY': {
        'subject': 'Psychology',
        'scores': {
            5: {'credits_awarded': 3, 'equivalent_course': 'PSY-101', 'placement': 'General Psychology course waiver'},
            4: {'credits_awarded': 3, 'equivalent_course': 'PSY-101', 'placement': 'General Psychology course waiver'},
            3: {'credits_awarded': 3, 'equivalent_course': 'PSY-100', 'placement': 'Social science general credit'}
        }
    },
    'AP_ENVIRONMENTAL_SCIENCE': {
        'subject': 'Environmental Science',
        'scores': {
            5: {'credits_awarded': 4, 'equivalent_course': 'ENV-101', 'placement': 'Environmental Science I with lab waiver'},
            4: {'credits_awarded': 4, 'equivalent_course': 'ENV-101', 'placement': 'Environmental Science I with lab waiver'},
            3: {'credits_awarded': 3, 'equivalent_course': 'ENV-100', 'placement': 'Natural science general elective'}
        }
    },
    'AP_ENGLISH_LANGUAGE': {
        'subject': 'English Language and Composition',
        'scores': {
            5: {'credits_awarded': 6, 'equivalent_course': 'HUM-101', 'placement': 'College Writing I & II waiver'},
            4: {'credits_awarded': 3, 'equivalent_course': 'HUM-101', 'placement': 'College Writing I waiver'},
            3: {'credits_awarded': 3, 'equivalent_course': 'ENG-100', 'placement': 'General humanities elective'}
        }
    }
}

IB_HIGHER_LEVEL_POLICY = {
    'IB_HL_COMPUTER_SCIENCE': {
        'subject': 'Computer Science HL',
        'scores': {
            7: {'credits_awarded': 8, 'equivalent_course': 'CS-101', 'placement': 'CS-101 and CS-102 waiver'},
            6: {'credits_awarded': 4, 'equivalent_course': 'CS-101', 'placement': 'CS-101 waiver'},
            5: {'credits_awarded': 4, 'equivalent_course': 'CS-100', 'placement': 'General CS elective'}
        }
    },
    'IB_HL_MATHEMATICS_AA': {
        'subject': 'Mathematics: Analysis & Approaches HL',
        'scores': {
            7: {'credits_awarded': 8, 'equivalent_course': 'MP-101', 'placement': 'Calculus I & II waiver'},
            6: {'credits_awarded': 8, 'equivalent_course': 'MP-101', 'placement': 'Calculus I & II waiver'},
            5: {'credits_awarded': 4, 'equivalent_course': 'MP-101', 'placement': 'Calculus I waiver'}
        }
    },
    'IB_HL_PHYSICS': {
        'subject': 'Physics HL',
        'scores': {
            7: {'credits_awarded': 8, 'equivalent_course': 'MP-102', 'placement': 'University Physics I & II with lab waiver'},
            6: {'credits_awarded': 8, 'equivalent_course': 'MP-102', 'placement': 'University Physics I & II with lab waiver'},
            5: {'credits_awarded': 4, 'equivalent_course': 'MP-102', 'placement': 'University Physics I with lab waiver'}
        }
    }
}


class StandardizedTestPlacementService:
    @classmethod
    def evaluate_ap_credits(cls, exam_code: str, score: int) -> Dict[str, Any]:
        """Evaluates Advanced Placement test score for institutional credit and placement."""
        exam = AP_EXAM_CREDIT_POLICY.get(exam_code.upper())
        if not exam:
            return {'eligible': False, 'reason': f'AP Exam {exam_code} not recognized.'}

        policy = exam['scores'].get(score)
        if not policy or policy['credits_awarded'] == 0:
            return {
                'eligible': False,
                'subject': exam['subject'],
                'score': score,
                'credits_awarded': 0,
                'reason': f'Score {score} does not satisfy institutional credit threshold.'
            }

        return {
            'eligible': True,
            'subject': exam['subject'],
            'score': score,
            'credits_awarded': policy['credits_awarded'],
            'equivalent_course': policy['equivalent_course'],
            'placement_note': policy['placement']
        }

    @classmethod
    def evaluate_ib_credits(cls, exam_code: str, score: int) -> Dict[str, Any]:
        """Evaluates International Baccalaureate Higher Level test score for credit."""
        exam = IB_HIGHER_LEVEL_POLICY.get(exam_code.upper())
        if not exam:
            return {'eligible': False, 'reason': f'IB Exam {exam_code} not recognized.'}

        policy = exam['scores'].get(score)
        if not policy:
            return {
                'eligible': False,
                'subject': exam['subject'],
                'score': score,
                'credits_awarded': 0,
                'reason': f'Score {score} does not meet minimum award threshold of 5.'
            }

        return {
            'eligible': True,
            'subject': exam['subject'],
            'score': score,
            'credits_awarded': policy['credits_awarded'],
            'equivalent_course': policy['equivalent_course'],
            'placement_note': policy['placement']
        }
