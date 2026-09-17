"""
Proctoring Security & Anti-Cheat Analytics Service.
Aggregates suspicious behavior events and computes anomaly risk scores.
"""
from typing import Dict, Any, List


class ProctoringSecurityService:
    SEVERITY_WEIGHTS = {
        'LOW': 5,
        'MEDIUM': 15,
        'HIGH': 30,
        'CRITICAL': 50
    }

    DISQUALIFICATION_THRESHOLD = 75

    @classmethod
    def calculate_attempt_risk_score(cls, events: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Computes cumulative anomaly risk score (0 to 100) based on proctoring incidents
        (tab switches, face loss, multiple faces, clipboard operations).
        """
        total_risk = 0
        incident_counts = {}

        for event in events:
            ev_type = event.get('event_type', 'UNKNOWN')
            severity = event.get('severity', 'MEDIUM').upper()
            weight = cls.SEVERITY_WEIGHTS.get(severity, 15)

            total_risk += weight
            incident_counts[ev_type] = incident_counts.get(ev_type, 0) + 1

        capped_risk = min(100, total_risk)
        is_disqualified = capped_risk >= cls.DISQUALIFICATION_THRESHOLD

        if capped_risk >= 60:
            risk_tier = 'HIGH_RISK_SUSPICIOUS'
        elif capped_risk >= 30:
            risk_tier = 'MODERATE_WARNING'
        else:
            risk_tier = 'NORMAL_SECURE'

        return {
            'total_events_count': len(events),
            'risk_score': capped_risk,
            'risk_tier': risk_tier,
            'is_flagged_for_review': capped_risk >= 30,
            'is_recommended_disqualification': is_disqualified,
            'incident_breakdown': incident_counts
        }
