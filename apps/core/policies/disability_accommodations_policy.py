"""
Disability Accommodations & Section 504 / ADA Compliance Policy Engine.
Evaluates reasonable academic accommodations, exam adaptations, and documentation cycles.
"""
from decimal import Decimal
from typing import Dict, Any, List


class DisabilityAccommodationsPolicy:
    TIME_AND_A_HALF = Decimal('1.50')
    DOUBLE_TIME = Decimal('2.00')

    APPROVED_ACCOMMODATIONS = {
        'EXTENDED_EXAM_TIME_1_5X': '50% additional time on all timed quizzes, midterms, and final examinations.',
        'EXTENDED_EXAM_TIME_2_0X': '100% additional time on all timed quizzes, midterms, and final examinations.',
        'DISTRACTION_REDUCED_ROOM': 'Testing in proctored, distraction-reduced testing environment (max 10 occupants).',
        'SCREEN_READER_COMPATIBLE': 'Exams and course materials in screen-reader accessible digital format (WCAG 2.1 AA).',
        'SCRIBE_ASSISTANCE': 'Provision of human scribe for recorded verbal examination responses.',
        'PEER_NOTETAKER': 'Access to designated peer note-taker or automated AI lecture audio transcription.',
        'RECORDING_AUTHORIZATION': 'Authorization to record lecture audio for personal study purposes only.',
        'PREFERENTIAL_SEATING': 'Reserved seating in front row near whiteboard and audio amplification.',
        'ATTENDANCE_FLEXIBILITY': 'Reasonable consideration for short-term episodic disability flare-up absences.'
    }

    @classmethod
    def calculate_exam_duration(
        cls,
        standard_duration_minutes: int,
        accommodation_codes: List[str]
    ) -> Dict[str, Any]:
        multiplier = Decimal('1.00')
        if 'EXTENDED_EXAM_TIME_2_0X' in accommodation_codes:
            multiplier = cls.DOUBLE_TIME
        elif 'EXTENDED_EXAM_TIME_1_5X' in accommodation_codes:
            multiplier = cls.TIME_AND_A_HALF

        adjusted_minutes = int(Decimal(str(standard_duration_minutes)) * multiplier)
        needs_separate_room = 'DISTRACTION_REDUCED_ROOM' in accommodation_codes
        needs_assistive_tech = any(code in accommodation_codes for code in ['SCREEN_READER_COMPATIBLE', 'SCRIBE_ASSISTANCE'])

        return {
            'standard_minutes': standard_duration_minutes,
            'multiplier': float(multiplier),
            'adjusted_minutes': adjusted_minutes,
            'requires_separate_testing_room': needs_separate_room,
            'requires_assistive_technology': needs_assistive_tech
        }
