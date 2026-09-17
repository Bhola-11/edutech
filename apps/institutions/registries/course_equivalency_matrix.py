"""
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
