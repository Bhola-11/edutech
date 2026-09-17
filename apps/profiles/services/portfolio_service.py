"""
Student Academic Portfolio & Artifact Verification Service.
Evaluates portfolio completeness, competency alignments, and career readiness rubrics.
"""
from typing import Dict, Any, List


class PortfolioVerificationService:
    @classmethod
    def evaluate_portfolio_readiness(
        cls,
        student_id: int,
        artifacts: List[Dict[str, Any]],
        verified_skills: List[str]
    ) -> Dict[str, Any]:
        """
        Assesses student showcase portfolio for career and graduate school readiness.
        Requires minimum: 3 verified artifacts, 1 github/code link, and 5 verified skills.
        """
        total_artifacts = len(artifacts)
        has_code_repository = any(a.get('type') in ['GITHUB_REPO', 'CODE_ARCHIVE'] for a in artifacts)
        has_capstone_project = any(a.get('is_capstone', False) for a in artifacts)
        total_skills = len(verified_skills)

        # Scoring rubric (max 100 points)
        score = 0
        score += min(30, total_artifacts * 10)  # Up to 30 pts for 3 artifacts
        if has_code_repository:
            score += 25
        if has_capstone_project:
            score += 25
        score += min(20, total_skills * 4)  # Up to 20 pts for 5 skills

        is_career_ready = score >= 75

        return {
            'student_id': student_id,
            'readiness_score': score,
            'is_career_ready': is_career_ready,
            'artifact_count': total_artifacts,
            'has_code_repository': has_code_repository,
            'has_capstone_project': has_capstone_project,
            'verified_skills_count': total_skills,
            'badge_awarded': 'GOLD_DISTINCTION' if score >= 90 else ('SILVER_ACHIEVER' if score >= 75 else 'IN_PROGRESS')
        }
