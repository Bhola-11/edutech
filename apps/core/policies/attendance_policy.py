from decimal import Decimal

class AttendancePolicy:
    MIN_ATTENDANCE_PERCENT = Decimal('75.0')
    WARNING_ATTENDANCE_PERCENT = Decimal('80.0')
    MEDICAL_EXEMPTION_ALLOWANCE_PCT = Decimal('10.0')

    @classmethod
    def calculate_attendance_standing(cls, total_sessions, attended_sessions, approved_medical_leaves=0):
        if total_sessions <= 0:
            return {
                'attendance_percentage': Decimal('100.0'),
                'is_exam_eligible': True,
                'status': 'FULL_ATTENDANCE',
                'warning_issued': False
            }

        effective_attended = attended_sessions + min(
            approved_medical_leaves,
            int(total_sessions * (cls.MEDICAL_EXEMPTION_ALLOWANCE_PCT / Decimal('100.0')))
        )
        pct = round((Decimal(str(effective_attended)) / Decimal(str(total_sessions))) * Decimal('100.0'), 1)

        if pct >= cls.WARNING_ATTENDANCE_PERCENT:
            return {
                'attendance_percentage': pct,
                'is_exam_eligible': True,
                'status': 'SATISFACTORY',
                'warning_issued': False
            }
        elif pct >= cls.MIN_ATTENDANCE_PERCENT:
            return {
                'attendance_percentage': pct,
                'is_exam_eligible': True,
                'status': 'ATTENDANCE_WARNING',
                'warning_issued': True,
                'message': 'Attendance has dipped close to the statutory 75% minimum examination threshold.'
            }
        else:
            return {
                'attendance_percentage': pct,
                'is_exam_eligible': False,
                'status': 'DEBARRED_ATTENDANCE_SHORTAGE',
                'warning_issued': True,
                'message': 'Student attendance is below 75%. Student is formally debarred from end-semester examination.'
            }
