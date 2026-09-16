from decimal import Decimal
from django.utils import timezone
from .models import AdmissionApplication, AdmissionCycle, StudentEnrollment
from apps.courses.models import Course

class MeritScoringEngine:
    WEIGHT_PRIOR_GPA = Decimal('0.40')
    WEIGHT_SOP_EVAL = Decimal('0.30')
    WEIGHT_ENTRANCE_SCORE = Decimal('0.30')

    @classmethod
    def calculate_composite_merit_score(cls, prior_gpa, sop_score, entrance_score=None):
        normalized_gpa = Decimal('0.0')
        if prior_gpa:
            # Normalize 4.0 scale to 100.0
            normalized_gpa = min(Decimal('100.0'), (Decimal(str(prior_gpa)) / Decimal('4.0')) * Decimal('100.0'))

        norm_sop = Decimal(str(sop_score or 75.0))
        norm_entrance = Decimal(str(entrance_score or 80.0))

        composite_score = (
            (normalized_gpa * cls.WEIGHT_PRIOR_GPA) +
            (norm_sop * cls.WEIGHT_SOP_EVAL) +
            (norm_entrance * cls.WEIGHT_ENTRANCE_SCORE)
        )
        return round(composite_score, 2)

    @classmethod
    def rank_applications_for_cycle(cls, cycle):
        applications = list(cycle.applications.filter(status__in=['SUBMITTED', 'UNDER_REVIEW', 'SHORTLISTED']))
        scored_apps = []

        for app in applications:
            score = cls.calculate_composite_merit_score(
                prior_gpa=app.prior_gpa,
                sop_score=85.0 if len(app.statement_of_purpose) > 200 else 60.0
            )
            scored_apps.append((score, app))

        scored_apps.sort(key=lambda x: x[0], reverse=True)

        seats_available = cycle.max_seats
        admitted = []
        waitlisted = []

        for rank, (score, app) in enumerate(scored_apps, start=1):
            if rank <= seats_available:
                app.status = 'ACCEPTED'
                admitted.append(app)
            else:
                app.status = 'WAITLISTED'
                waitlisted.append(app)
            app.review_notes = f'Merit Rank #{rank} (Composite Score: {score}/100)'
            app.reviewed_at = timezone.now()
            app.save(update_fields=['status', 'review_notes', 'reviewed_at'])

        return {
            'total_evaluated': len(scored_apps),
            'accepted_count': len(admitted),
            'waitlisted_count': len(waitlisted)
        }

class RollNumberGenerator:
    @staticmethod
    def generate_student_roll_number(institution_code, department_code, year=None, sequence_num=1):
        if not year:
            year = timezone.now().year
        padded_seq = f'{sequence_num:04d}'
        return f'{institution_code.upper()}-{department_code.upper()}-{year}-{padded_seq}'
