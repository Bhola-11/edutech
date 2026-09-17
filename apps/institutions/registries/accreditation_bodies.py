"""
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
