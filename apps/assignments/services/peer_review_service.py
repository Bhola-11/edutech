"""
Double-Blind Peer Review Allocation & Calibration Service.
"""
import random
from typing import Dict, Any, List


class PeerReviewDistributionService:
    @classmethod
    def allocate_peer_reviews(
        cls,
        submissions: List[Dict[str, Any]],
        reviews_per_submission: int = 2
    ) -> List[Dict[str, Any]]:
        """
        Distributes submissions among peers such that:
        1. No student reviews their own submission.
        2. Every submission receives exactly N reviews.
        3. Review allocations are balanced.
        """
        if len(submissions) <= reviews_per_submission:
            return []  # Need more submissions than reviews requested

        student_ids = [s['student_id'] for s in submissions]
        allocations = []

        for i, s in enumerate(submissions):
            student_id = s['student_id']
            # Eligible reviewers: everyone except author
            eligible_reviewers = [sid for sid in student_ids if sid != student_id]

            # Deterministic/random offset allocation
            for r_offset in range(1, reviews_per_submission + 1):
                reviewer_id = eligible_reviewers[(i + r_offset) % len(eligible_reviewers)]
                allocations.append({
                    'submission_id': s['id'],
                    'submission_author_id': student_id,
                    'reviewer_id': reviewer_id
                })

        return allocations
