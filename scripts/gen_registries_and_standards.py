"""
Generate course transfer equivalencies, accreditation bodies, and standardized testing benchmarks.
"""
import os

CORE_STANDARDS_DIR = os.path.join(os.path.dirname(__file__), '..', 'apps', 'core', 'standards')
INSTITUTIONS_REG_DIR = os.path.join(os.path.dirname(__file__), '..', 'apps', 'institutions', 'registries')

os.makedirs(CORE_STANDARDS_DIR, exist_ok=True)
os.makedirs(INSTITUTIONS_REG_DIR, exist_ok=True)

# 1. Standardized Tests Benchmarks
STANDARDIZED_TESTS_CODE = '''"""
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
'''

# 2. Accreditation Bodies Registry
ACCREDITATION_BODIES_CODE = '''"""
Global Higher Education Accreditation Bodies Registry.
Covers regional institutional commissions and specialized professional accreditors.
"""
from typing import Dict, Any, List

ACCREDITING_AGENCIES = [
    {
        'code': 'ABET',
        'name': 'Accreditation Board for Engineering and Technology',
        'type': 'PROGRAMMATIC_SPECIALIZED',
        'jurisdiction': 'Global / USA',
        'disciplines': ['Engineering', 'Computer Science', 'Applied Science', 'Technology'],
        'reaccreditation_cycle_years': 6,
        'standards': ['General Criteria for Baccalaureate Level Programs', 'Program Criteria for Computer Science', 'Continuous Improvement Process']
    },
    {
        'code': 'AACSB',
        'name': 'Association to Advance Collegiate Schools of Business',
        'type': 'PROGRAMMATIC_SPECIALIZED',
        'jurisdiction': 'Global',
        'disciplines': ['Business Administration', 'Accounting', 'Finance', 'Management'],
        'reaccreditation_cycle_years': 5,
        'standards': ['Strategic Management and Innovation', 'Learner Success', 'Thought Leadership and Societal Impact']
    },
    {
        'code': 'NAAB',
        'name': 'National Architectural Accrediting Board',
        'type': 'PROGRAMMATIC_SPECIALIZED',
        'jurisdiction': 'USA',
        'disciplines': ['Architecture', 'Urban Design'],
        'reaccreditation_cycle_years': 8,
        'standards': ['Program and Student Criteria', 'Health, Safety, and Welfare in the Built Environment', 'Design Integration']
    },
    {
        'code': 'ABA',
        'name': 'American Bar Association - Section of Legal Education',
        'type': 'PROGRAMMATIC_SPECIALIZED',
        'jurisdiction': 'USA',
        'disciplines': ['Jurisprudence', 'Legal Studies', 'Law'],
        'reaccreditation_cycle_years': 10,
        'standards': ['Curriculum and Learning Outcomes', 'Bar Passage Rate Compliance', 'Faculty Qualifications and Governance']
    },
    {
        'code': 'APA',
        'name': 'American Psychological Association - Commission on Accreditation',
        'type': 'PROGRAMMATIC_SPECIALIZED',
        'jurisdiction': 'USA / North America',
        'disciplines': ['Clinical Psychology', 'Counseling Psychology', 'School Psychology'],
        'reaccreditation_cycle_years': 10,
        'standards': ['Institutional and Program Resources', 'Competencies in Professional Psychology', 'Ethical and Legal Standards']
    },
    {
        'code': 'NECHE',
        'name': 'New England Commission of Higher Education',
        'type': 'REGIONAL_INSTITUTIONAL',
        'jurisdiction': 'USA (New England)',
        'disciplines': ['All Institutional Programs'],
        'reaccreditation_cycle_years': 10,
        'standards': ['Mission and Integrity', 'Teaching, Learning, and Scholarship', 'Students and Academic Support', 'Financial Resources']
    },
    {
        'code': 'MSCHE',
        'name': 'Middle States Commission on Higher Education',
        'type': 'REGIONAL_INSTITUTIONAL',
        'jurisdiction': 'USA (Mid-Atlantic)',
        'disciplines': ['All Institutional Programs'],
        'reaccreditation_cycle_years': 8,
        'standards': ['Ethics and Integrity', 'Design and Delivery of Student Learning Experience', 'Support of Student Experience', 'Governance']
    },
    {
        'code': 'HLC',
        'name': 'Higher Learning Commission',
        'type': 'REGIONAL_INSTITUTIONAL',
        'jurisdiction': 'USA (North Central)',
        'disciplines': ['All Institutional Programs'],
        'reaccreditation_cycle_years': 10,
        'standards': ['Mission', 'Integrity: Ethical and Responsible Conduct', 'Teaching and Learning: Quality, Resources, and Support']
    },
    {
        'code': 'SACSCOC',
        'name': 'Southern Association of Colleges and Schools Commission on Colleges',
        'type': 'REGIONAL_INSTITUTIONAL',
        'jurisdiction': 'USA (South)',
        'disciplines': ['All Institutional Programs'],
        'reaccreditation_cycle_years': 10,
        'standards': ['The Principle of Integrity', 'Educational Programs: Undergraduate and Graduate', 'Faculty Competency']
    },
    {
        'code': 'WSCUC',
        'name': 'WASC Senior College and University Commission',
        'type': 'REGIONAL_INSTITUTIONAL',
        'jurisdiction': 'USA (West)',
        'disciplines': ['All Institutional Programs'],
        'reaccreditation_cycle_years': 8,
        'standards': ['Defining Institutional Purposes and Ensuring Educational Objectives', 'Achieving Educational Results']
    }
]


class AccreditationRegistryService:
    @classmethod
    def get_agency_by_code(cls, code: str) -> Dict[str, Any]:
        """Looks up accreditation body by abbreviation code."""
        for agency in ACCREDITING_AGENCIES:
            if agency['code'].upper() == code.upper():
                return agency
        return {}

    @classmethod
    def get_agencies_by_discipline(cls, discipline: str) -> List[Dict[str, Any]]:
        """Retrieves specialized programmatic accrediting bodies covering a specific discipline."""
        matches = []
        for agency in ACCREDITING_AGENCIES:
            if any(discipline.lower() in d.lower() for d in agency['disciplines']):
                matches.append(agency)
        return matches
'''

# 3. Course Equivalency Matrix
COURSE_EQUIVALENCY_CODE = '''"""
International & Inter-Institutional Course Equivalency Transfer Matrix.
Standardizes credit transfer mappings across prominent global universities.
"""
from typing import Dict, Any, List, Optional

GLOBAL_COURSE_EQUIVALENCY_CATALOG = [
    {
        'source_institution': 'Massachusetts Institute of Technology (MIT)',
        'source_code': '6.0001',
        'source_title': 'Introduction to Computer Science and Programming in Python',
        'target_code': 'CS-101',
        'target_title': 'Intro to Computing & Python',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Stanford University',
        'source_code': 'CS106A',
        'source_title': 'Programming Methodology',
        'target_code': 'CS-101',
        'target_title': 'Intro to Computing & Python',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'University of California, Berkeley',
        'source_code': 'CS61A',
        'source_title': 'The Structure and Interpretation of Computer Programs',
        'target_code': 'CS-101',
        'target_title': 'Intro to Computing & Python',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Stanford University',
        'source_code': 'CS106B',
        'source_title': 'Programming Abstractions (Data Structures)',
        'target_code': 'CS-102',
        'target_title': 'Object-Oriented Programming & Data Structures',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Harvard University',
        'source_code': 'CS50',
        'source_title': 'Introduction to Computer Science',
        'target_code': 'CS-101',
        'target_title': 'Intro to Computing & Python',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Carnegie Mellon University',
        'source_code': '15-122',
        'source_title': 'Principles of Imperative Computation',
        'target_code': 'CS-102',
        'target_title': 'Object-Oriented Programming & Data Structures',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'ETH Zurich',
        'source_code': '252-0002',
        'source_title': 'Data Structures and Algorithms',
        'target_code': 'CS-102',
        'target_title': 'Object-Oriented Programming & Data Structures',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'University of Oxford',
        'source_code': 'COMP001',
        'source_title': 'Functional Programming & Algorithms',
        'target_code': 'CS-102',
        'target_title': 'Object-Oriented Programming & Data Structures',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Massachusetts Institute of Technology (MIT)',
        'source_code': '18.01',
        'source_title': 'Single Variable Calculus',
        'target_code': 'MP-101',
        'target_title': 'Calculus I & Analytical Geometry',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Stanford University',
        'source_code': 'MATH51',
        'source_title': 'Linear Algebra and Differential Calculus of Several Variables',
        'target_code': 'MP-102',
        'target_title': 'Multivariable Calculus & Linear Algebra',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'MIT',
        'source_code': '8.01',
        'source_title': 'Physics I: Classical Mechanics',
        'target_code': 'MP-103',
        'target_title': 'Classical Mechanics & Thermal Physics',
        'credits': 4,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    },
    {
        'source_institution': 'Harvard University',
        'source_code': 'ECON10A',
        'source_title': 'Principles of Economics (Microeconomics)',
        'target_code': 'BA-101',
        'target_title': 'Principles of Management & Microeconomics',
        'credits': 3,
        'min_grade': 'C',
        'transfer_status': 'PRE_APPROVED'
    }
]


class CourseEquivalencyService:
    @classmethod
    def lookup_equivalency(
        cls,
        institution_name: str,
        course_code: str
    ) -> Optional[Dict[str, Any]]:
        """Looks up direct course transfer articulation agreements."""
        inst_clean = institution_name.lower().strip()
        code_clean = course_code.upper().strip()

        for entry in GLOBAL_COURSE_EQUIVALENCY_CATALOG:
            if inst_clean in entry['source_institution'].lower() and entry['source_code'].upper() == code_clean:
                return entry
        return None

    @classmethod
    def list_equivalencies_for_course(cls, target_course_code: str) -> List[Dict[str, Any]]:
        """Retrieves all external university courses that map to an institutional course."""
        target_code = target_course_code.upper().strip()
        return [
            e for e in GLOBAL_COURSE_EQUIVALENCY_CATALOG
            if e['target_code'].upper() == target_code
        ]
'''

FILES = {
    os.path.join(CORE_STANDARDS_DIR, 'standardized_tests.py'): STANDARDIZED_TESTS_CODE,
    os.path.join(INSTITUTIONS_REG_DIR, 'accreditation_bodies.py'): ACCREDITATION_BODIES_CODE,
    os.path.join(INSTITUTIONS_REG_DIR, 'course_equivalency_matrix.py'): COURSE_EQUIVALENCY_CODE
}

for path, code in FILES.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(code.strip() + '\n')
    print(f"Created file: {os.path.basename(path)}")

print("Registries and standards generation complete.")
