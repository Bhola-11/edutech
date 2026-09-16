from decimal import Decimal

US_4_POINT_SCALE = [
    {'letter': 'A+', 'gpa': Decimal('4.00'), 'min_pct': 97.0, 'max_pct': 100.0, 'standing': 'Highest Distinction'},
    {'letter': 'A',  'gpa': Decimal('4.00'), 'min_pct': 93.0, 'max_pct': 96.99, 'standing': 'Distinction'},
    {'letter': 'A-', 'gpa': Decimal('3.70'), 'min_pct': 90.0, 'max_pct': 92.99, 'standing': 'Excellent'},
    {'letter': 'B+', 'gpa': Decimal('3.30'), 'min_pct': 87.0, 'max_pct': 89.99, 'standing': 'Very Good'},
    {'letter': 'B',  'gpa': Decimal('3.00'), 'min_pct': 83.0, 'max_pct': 86.99, 'standing': 'Good'},
    {'letter': 'B-', 'gpa': Decimal('2.70'), 'min_pct': 80.0, 'max_pct': 82.99, 'standing': 'Above Average'},
    {'letter': 'C+', 'gpa': Decimal('2.30'), 'min_pct': 77.0, 'max_pct': 79.99, 'standing': 'Average'},
    {'letter': 'C',  'gpa': Decimal('2.00'), 'min_pct': 73.0, 'max_pct': 76.99, 'standing': 'Satisfactory'},
    {'letter': 'C-', 'gpa': Decimal('1.70'), 'min_pct': 70.0, 'max_pct': 72.99, 'standing': 'Pass Minimum'},
    {'letter': 'D+', 'gpa': Decimal('1.30'), 'min_pct': 67.0, 'max_pct': 69.99, 'standing': 'Marginal Pass'},
    {'letter': 'D',  'gpa': Decimal('1.00'), 'min_pct': 60.0, 'max_pct': 66.99, 'standing': 'Poor Pass'},
    {'letter': 'F',  'gpa': Decimal('0.00'), 'min_pct': 0.0,  'max_pct': 59.99, 'standing': 'Failing Grade'}
]

ECTS_SCALE = [
    {'grade': 'A', 'definition': 'Excellent - outstanding performance with only minor errors', 'pct_top': 10},
    {'grade': 'B', 'definition': 'Very Good - above the average standard but with some errors', 'pct_top': 25},
    {'grade': 'C', 'definition': 'Good - generally sound work with a number of notable errors', 'pct_top': 30},
    {'grade': 'D', 'definition': 'Satisfactory - fair but with significant shortcomings', 'pct_top': 25},
    {'grade': 'E', 'definition': 'Sufficient - performance meets the minimum criteria', 'pct_top': 10},
    {'grade': 'FX', 'definition': 'Fail - some more work required before credit can be awarded', 'pct_top': 0},
    {'grade': 'F', 'definition': 'Fail - considerable further work is required', 'pct_top': 0}
]

UK_DEGREE_CLASSIFICATIONS = [
    {'honours': 'First Class Honours (1st)', 'min_mark': 70.0, 'gpa_equivalent': Decimal('3.80')},
    {'honours': 'Upper Second Class Honours (2:1)', 'min_mark': 60.0, 'gpa_equivalent': Decimal('3.30')},
    {'honours': 'Lower Second Class Honours (2:2)', 'min_mark': 50.0, 'gpa_equivalent': Decimal('2.70')},
    {'honours': 'Third Class Honours (3rd)', 'min_mark': 40.0, 'gpa_equivalent': Decimal('2.00')},
    {'honours': 'Fail / Non-Honours Pass', 'min_mark': 0.0, 'gpa_equivalent': Decimal('0.00')}
]

class GradeConversionEngine:
    @staticmethod
    def score_to_letter_grade(percentage):
        pct = float(percentage)
        for row in US_4_POINT_SCALE:
            if row['min_pct'] <= pct <= row['max_pct']:
                return row['letter'], row['gpa'], row['standing']
        return 'F', Decimal('0.00'), 'Failing Grade'

    @staticmethod
    def calculate_term_gpa(grades_and_credits):
        total_credit_points = Decimal('0.0')
        total_credits = Decimal('0.0')

        for grade, credits in grades_and_credits:
            cred = Decimal(str(credits))
            gpa = Decimal('0.00')
            for row in US_4_POINT_SCALE:
                if row['letter'] == grade:
                    gpa = row['gpa']
                    break
            total_credit_points += gpa * cred
            total_credits += cred

        if total_credits == 0:
            return Decimal('0.00')
        return round(total_credit_points / total_credits, 2)
