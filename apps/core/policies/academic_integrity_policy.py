"""
Academic Integrity & Honor Code Policy Engine.
Adjudication tiers, sanction determination, and appeal workflows.
"""
from typing import Dict, Any, List


class AcademicIntegrityPolicy:
    LEVEL_1_MINOR = 'LEVEL_1_MINOR'
    LEVEL_2_MODERATE = 'LEVEL_2_MODERATE'
    LEVEL_3_MAJOR = 'LEVEL_3_MAJOR'
    LEVEL_4_EGREGIOUS = 'LEVEL_4_EGREGIOUS'

    CAT_PLAGIARISM = 'PLAGIARISM'
    CAT_UNAUTHORIZED_COLLABORATION = 'UNAUTHORIZED_COLLABORATION'
    CAT_FABRICATION_FALSIFICATION = 'FABRICATION_FALSIFICATION'
    CAT_EXAM_CHEATING = 'EXAM_CHEATING'
    CAT_CONTRACT_CHEATING = 'CONTRACT_CHEATING'
    CAT_RECORD_TAMPERING = 'RECORD_TAMPERING'

    SANCTIONS = {
        LEVEL_1_MINOR: {
            'academic_penalty': 'Zero on assignment; optional resubmission for max 70% credit.',
            'disciplinary_penalty': 'Official written reprimand; mandatory Academic Citation Workshop.',
            'transcript_notation': False,
            'record_retention_years': 1
        },
        LEVEL_2_MODERATE: {
            'academic_penalty': 'Grade of 0 on assessment; overall course letter grade lowered by one step.',
            'disciplinary_penalty': 'Probationary honor standing; mandatory ethics seminar completion.',
            'transcript_notation': False,
            'record_retention_years': 3
        },
        LEVEL_3_MAJOR: {
            'academic_penalty': 'Permanent grade of "XF" (failure due to academic dishonesty) for course.',
            'disciplinary_penalty': 'Suspension from institution for 1 to 2 academic semesters.',
            'transcript_notation': True,
            'record_retention_years': 7
        },
        LEVEL_4_EGREGIOUS: {
            'academic_penalty': 'Immediate expulsion and revocation of any pending degree or honors.',
            'disciplinary_penalty': 'Permanent expulsion; campus persona non grata ban.',
            'transcript_notation': True,
            'record_retention_years': 99
        }
    }

    @classmethod
    def evaluate_violation(
        cls,
        category: str,
        prior_violation_count: int,
        is_commercial_or_proxy: bool = False,
        is_formal_exam: bool = False,
        grade_weight_percentage: float = 10.0
    ) -> Dict[str, Any]:
        if prior_violation_count >= 2 or is_commercial_or_proxy:
            level = cls.LEVEL_4_EGREGIOUS
        elif prior_violation_count == 1:
            level = cls.LEVEL_3_MAJOR
        elif is_formal_exam and grade_weight_percentage >= 20.0:
            level = cls.LEVEL_3_MAJOR
        elif grade_weight_percentage >= 15.0 or category in [cls.CAT_FABRICATION_FALSIFICATION, cls.CAT_EXAM_CHEATING]:
            level = cls.LEVEL_2_MODERATE
        else:
            level = cls.LEVEL_1_MINOR

        sanction = cls.SANCTIONS[level]

        return {
            'category': category,
            'level': level,
            'prior_violations': prior_violation_count,
            'academic_penalty': sanction['academic_penalty'],
            'disciplinary_penalty': sanction['disciplinary_penalty'],
            'transcript_notation': sanction['transcript_notation'],
            'record_retention_years': sanction['record_retention_years'],
            'requires_board_hearing': level in [cls.LEVEL_3_MAJOR, cls.LEVEL_4_EGREGIOUS],
            'notice_deadline_days': 5,
            'appeal_filing_window_days': 10
        }
