from datetime import timedelta
from .models import Classroom, Semester, AcademicSession

class VenueOptimizationEngine:
    @staticmethod
    def find_suitable_classrooms(campus, required_capacity, needs_projector=False, needs_computers=False, needs_accessible=False):
        qs = Classroom.objects.filter(
            campus=campus,
            is_active=True,
            seating_capacity__gte=required_capacity
        )
        if needs_projector:
            qs = qs.filter(has_projector=True)
        if needs_computers:
            qs = qs.filter(has_computers=True)
        if needs_accessible:
            qs = qs.filter(is_accessible=True)
        return qs.order_by('seating_capacity')

    @staticmethod
    def calculate_campus_utilization(campus):
        total_classrooms = campus.classrooms.filter(is_active=True).count()
        total_seats = sum(c.seating_capacity for c in campus.classrooms.filter(is_active=True))
        return {
            'campus_name': campus.name,
            'total_active_rooms': total_classrooms,
            'total_seats_capacity': total_seats,
            'average_room_capacity': round(total_seats / total_classrooms, 1) if total_classrooms > 0 else 0
        }

class AcademicCalendarEngine:
    @staticmethod
    def validate_semester_schedule(semester):
        errors = []
        if semester.start_date >= semester.end_date:
            errors.append('Term start date must be strictly earlier than term end date.')
        
        duration_days = (semester.end_date - semester.start_date).days
        if duration_days < 60 or duration_days > 180:
            errors.append(f'Academic semester duration ({duration_days} days) is outside the standard collegiate range (60-180 days).')

        if semester.registration_start_date > semester.registration_end_date:
            errors.append('Registration opening date must precede the registration deadline.')

        if semester.registration_end_date > semester.add_drop_deadline:
            errors.append('Registration deadline cannot occur after the add/drop deadline.')

        return {
            'is_valid': len(errors) == 0,
            'errors': errors,
            'instructional_duration_days': duration_days
        }
