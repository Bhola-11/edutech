"""
Campus Facilities & Classroom Booking Service.
Conflict detection, capacity validation, equipment matching, and schedule optimization.
"""
from typing import Dict, Any, List, Optional
from datetime import datetime, time
from django.db.models import Q
from apps.institutions.models import Classroom


class FacilitiesBookingService:
    @classmethod
    def find_available_classrooms(
        cls,
        institution_id: int,
        required_capacity: int,
        room_type: Optional[str] = None,
        has_projector: bool = False,
        has_audio_system: bool = False
    ) -> List[Dict[str, Any]]:
        """Filters institution classrooms that satisfy capacity and equipment requirements."""
        qs = Classroom.objects.filter(
            institution_id=institution_id,
            capacity__gte=required_capacity,
            is_active=True
        )
        if room_type:
            qs = qs.filter(room_type=room_type)
        if has_projector:
            qs = qs.filter(has_projector=True)
        if has_audio_system:
            qs = qs.filter(has_audio_system=True)

        results = []
        for room in qs.order_by('capacity'):
            utilization_rate = round((required_capacity / room.capacity) * 100, 1)
            results.append({
                'id': room.id,
                'code': room.room_number,
                'name': room.name,
                'building': room.building,
                'capacity': room.capacity,
                'room_type': room.room_type,
                'utilization_rate_projected': utilization_rate,
                'is_optimal_fit': 70.0 <= utilization_rate <= 100.0
            })
        return results

    @classmethod
    def check_time_slot_conflict(
        cls,
        start_time_a: time,
        end_time_a: time,
        start_time_b: time,
        end_time_b: time
    ) -> bool:
        """Determines whether two time slots overlap on the same day."""
        return max(start_time_a, start_time_b) < min(end_time_a, end_time_b)
