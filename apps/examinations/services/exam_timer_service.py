"""
Examination Countdown Timer & Auto-Submission Service.
"""
from datetime import datetime, timedelta
from django.utils import timezone
from typing import Dict, Any


class ExamTimerService:
    @classmethod
    def check_time_remaining(
        cls,
        started_at: datetime,
        duration_minutes: int,
        extra_time_minutes: int = 0
    ) -> Dict[str, Any]:
        """Calculates seconds remaining in an active exam session."""
        total_allowed_minutes = duration_minutes + extra_time_minutes
        expiry_time = started_at + timedelta(minutes=total_allowed_minutes)
        now = timezone.now()

        delta = expiry_time - now
        seconds_remaining = int(delta.total_seconds())

        is_expired = seconds_remaining <= 0

        return {
            'is_expired': is_expired,
            'seconds_remaining': max(0, seconds_remaining),
            'minutes_remaining': max(0, seconds_remaining // 60),
            'expiry_timestamp': expiry_time.isoformat(),
            'total_allowed_minutes': total_allowed_minutes
        }
