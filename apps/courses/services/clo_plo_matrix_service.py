"""
Course Learning Outcomes (CLO) to Program Learning Outcomes (PLO) Mapping Service.
Calculates alignment coverage matrices, ABET criteria mapping, and outcome gaps.
"""
from typing import Dict, Any, List, Set


class LearningOutcomesMatrixService:
    BLOOMS_TAXONOMY_LEVELS = [
        'REMEMBERING',
        'UNDERSTANDING',
        'APPLYING',
        'ANALYZING',
        'EVALUATING',
        'CREATING'
    ]

    ABET_STUDENT_OUTCOMES = {
        'SO_1': 'Identify, formulate, and solve complex engineering problems by applying engineering, science, and mathematics principles.',
        'SO_2': 'Apply engineering design to produce solutions meeting specified needs considering public health, safety, and welfare.',
        'SO_3': 'Communicate effectively with a range of audiences through written, oral, and graphical media.',
        'SO_4': 'Recognize ethical and professional responsibilities in engineering situations and make informed judgments.',
        'SO_5': 'Function effectively on a team whose members together provide leadership, create a collaborative environment, and meet objectives.',
        'SO_6': 'Develop and conduct appropriate experimentation, analyze and interpret data, and use engineering judgment to draw conclusions.',
        'SO_7': 'Acquire and apply new knowledge as needed, using appropriate learning strategies.'
    }

    @classmethod
    def evaluate_curriculum_coverage(
        cls,
        course_mappings: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Evaluates curriculum-wide coverage of ABET Student Outcomes (SO 1 through 7)
        and Bloom's Taxonomy cognitive progression.
        """
        outcomes_coverage = {so: 0 for so in cls.ABET_STUDENT_OUTCOMES.keys()}
        blooms_distribution = {level: 0 for level in cls.BLOOMS_TAXONOMY_LEVELS}

        for mapping in course_mappings:
            for outcome in mapping.get('mapped_outcomes', []):
                if outcome in outcomes_coverage:
                    outcomes_coverage[outcome] += 1
            b_level = mapping.get('blooms_level', '').upper()
            if b_level in blooms_distribution:
                blooms_distribution[b_level] += 1

        uncovered_outcomes = [so for so, count in outcomes_coverage.items() if count == 0]
        well_covered_outcomes = [so for so, count in outcomes_coverage.items() if count >= 3]

        return {
            'total_mapped_elements': len(course_mappings),
            'outcomes_coverage': outcomes_coverage,
            'blooms_distribution': blooms_distribution,
            'uncovered_outcomes': uncovered_outcomes,
            'is_fully_accredited': len(uncovered_outcomes) == 0,
            'accreditation_readiness_score': round((7 - len(uncovered_outcomes)) / 7 * 100, 1)
        }
