from decimal import Decimal

class AcademicStandingPolicy:
    DEANS_LIST_MIN_GPA = Decimal('3.75')
    PRESIDENTS_HONORS_MIN_GPA = Decimal('3.90')
    GOOD_STANDING_MIN_GPA = Decimal('2.00')
    ACADEMIC_WARNING_MIN_GPA = Decimal('1.75')
    ACADEMIC_PROBATION_THRESHOLD = Decimal('2.00')

    @classmethod
    def evaluate_academic_standing(cls, cumulative_gpa, term_gpa, consecutive_probation_terms=0):
        cgpa = Decimal(str(cumulative_gpa))
        tgpa = Decimal(str(term_gpa))

        if cgpa >= cls.PRESIDENTS_HONORS_MIN_GPA and tgpa >= cls.PRESIDENTS_HONORS_MIN_GPA:
            return {
                'standing': 'PRESIDENTS_HONORS',
                'description': 'President\'s Academic Honor Roll with Highest Distinction',
                'action_required': None,
                'is_in_good_standing': True
            }
        elif cgpa >= cls.DEANS_LIST_MIN_GPA and tgpa >= Decimal('3.50'):
            return {
                'standing': 'DEANS_LIST',
                'description': 'Dean\'s Academic Honor List',
                'action_required': None,
                'is_in_good_standing': True
            }
        elif cgpa >= cls.GOOD_STANDING_MIN_GPA:
            return {
                'standing': 'GOOD_STANDING',
                'description': 'Regular Satisfactory Academic Standing',
                'action_required': None,
                'is_in_good_standing': True
            }
        elif cgpa >= cls.ACADEMIC_WARNING_MIN_GPA:
            return {
                'standing': 'ACADEMIC_WARNING',
                'description': 'Academic Warning - Mandatory Faculty Advising Session',
                'action_required': 'Schedule mandatory academic counseling session with class advisor.',
                'is_in_good_standing': False
            }
        else:
            if consecutive_probation_terms >= 2:
                return {
                    'standing': 'ACADEMIC_SUSPENSION',
                    'description': 'Formal Academic Suspension for Two Consecutive Terms Below GPA Threshold',
                    'action_required': 'Student must file formal academic grievance or appeal for reinstatement.',
                    'is_in_good_standing': False
                }
            return {
                'standing': 'ACADEMIC_PROBATION',
                'description': 'Formal Academic Probation - Course Load Capped at 12 Credits',
                'action_required': 'Course enrollment capped at 12 credit hours maximum for the subsequent term.',
                'is_in_good_standing': False
            }
