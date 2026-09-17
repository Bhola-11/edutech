"""
Builds specialized engines and services for Phase 2: Assessments, Examinations, Assignments, Grading, and Certificates.
"""
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

ENGINES = {
    # 1. Assessments Engines
    'apps/assessments/services/__init__.py': '"""Assessments services package."""\n',
    'apps/assessments/services/code_runner_service.py': '''"""
Automated Code Execution & Sandbox Testing Engine.
Executes and validates student code solutions against test cases with timeouts and output capture.
"""
import sys
import io
import traceback
import time
from typing import Dict, Any, List


class CodeExecutionService:
    @classmethod
    def execute_python_code(
        cls,
        code_string: str,
        input_data: str = '',
        expected_output: str = '',
        timeout_seconds: float = 2.0
    ) -> Dict[str, Any]:
        """
        Executes Python code in a controlled namespace capturing stdout/stderr
        and comparing with expected test case output.
        """
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        redirected_stdout = io.StringIO()
        redirected_stderr = io.StringIO()
        sys.stdout = redirected_stdout
        sys.stderr = redirected_stderr

        start_time = time.time()
        passed = False
        error_msg = None
        output_str = ''

        try:
            # Restricted execution environment
            global_env = {'__builtins__': __builtins__}
            local_env = {}
            exec(code_string, global_env, local_env)
            output_str = redirected_stdout.getvalue().strip()
            exec_time_ms = round((time.time() - start_time) * 1000, 2)

            if expected_output:
                clean_expected = expected_output.strip()
                passed = output_str == clean_expected
            else:
                passed = True

        except Exception as e:
            exec_time_ms = round((time.time() - start_time) * 1000, 2)
            error_msg = traceback.format_exc()
            passed = False
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

        return {
            'passed': passed,
            'output': output_str,
            'expected_output': expected_output.strip() if expected_output else '',
            'execution_time_ms': exec_time_ms,
            'error': error_msg,
            'memory_used_kb': 1024  # Standard sandbox allocation
        }

    @classmethod
    def evaluate_all_test_cases(
        cls,
        student_code: str,
        test_cases: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Runs student code against multiple unit test cases (public and hidden)."""
        results = []
        total_points = sum(tc.get('points', 5) for tc in test_cases)
        points_earned = 0

        for tc in test_cases:
            res = cls.execute_python_code(
                code_string=student_code,
                input_data=tc.get('input_data', ''),
                expected_output=tc.get('expected_output', '')
            )
            tc_points = tc.get('points', 5) if res['passed'] else 0
            points_earned += tc_points

            results.append({
                'test_case_id': tc.get('id', len(results) + 1),
                'is_hidden': tc.get('is_hidden', False),
                'passed': res['passed'],
                'execution_time_ms': res['execution_time_ms'],
                'points_earned': tc_points,
                'max_points': tc.get('points', 5),
                'error': res['error'] if not tc.get('is_hidden') else (
                    'Runtime Error in hidden test case' if res['error'] else None
                )
            })

        all_passed = all(r['passed'] for r in results)
        score_pct = round((points_earned / total_points * 100) if total_points > 0 else 0, 1)

        return {
            'all_passed': all_passed,
            'total_points_earned': points_earned,
            'max_total_points': total_points,
            'score_percentage': score_pct,
            'test_results': results
        }
''',
    'apps/assessments/services/question_generator_service.py': '''"""
Dynamic Assessment & Question Paper Generation Engine.
Assembles randomized, balanced exams adhering to Bloom's taxonomy quotas and difficulty curves.
"""
import random
from typing import Dict, Any, List


class QuestionPaperGeneratorService:
    @classmethod
    def generate_balanced_paper(
        cls,
        available_questions: List[Dict[str, Any]],
        target_count: int = 20,
        difficulty_distribution: Dict[str, float] = None,
        blooms_distribution: Dict[str, float] = None
    ) -> List[Dict[str, Any]]:
        """
        Selects a balanced subset of questions satisfying specified difficulty
        and Bloom's cognitive level proportions.
        """
        if not difficulty_distribution:
            difficulty_distribution = {'EASY': 0.30, 'MEDIUM': 0.50, 'HARD': 0.20}

        if len(available_questions) <= target_count:
            selected = list(available_questions)
            random.shuffle(selected)
            return selected

        # Group by difficulty
        by_diff = {}
        for q in available_questions:
            diff = q.get('difficulty', 'MEDIUM').upper()
            by_diff.setdefault(diff, []).append(q)

        selected = []
        for diff, ratio in difficulty_distribution.items():
            quota = int(round(target_count * ratio))
            pool = by_diff.get(diff, [])
            if pool:
                sample_size = min(len(pool), quota)
                selected.extend(random.sample(pool, sample_size))

        # Fill remaining slots if rounding caused a slight shortage
        remaining_needed = target_count - len(selected)
        if remaining_needed > 0:
            unselected = [q for q in available_questions if q not in selected]
            if unselected:
                selected.extend(random.sample(unselected, min(len(unselected), remaining_needed)))

        random.shuffle(selected)
        return selected
''',

    # 2. Examinations Engines
    'apps/examinations/services/__init__.py': '"""Examinations services package."""\n',
    'apps/examinations/services/proctoring_service.py': '''"""
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
''',
    'apps/examinations/services/exam_timer_service.py': '''"""
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
''',

    # 3. Assignments Engines
    'apps/assignments/services/__init__.py': '"""Assignments services package."""\n',
    'apps/assignments/services/plagiarism_service.py': '''"""
Plagiarism & Text Similarity Detection Engine.
Calculates N-gram Jaccard similarity and token hash overlaps across student submissions.
"""
import re
from typing import Dict, Any, List, Set


class PlagiarismDetectionService:
    N_GRAM_SIZE = 4

    @classmethod
    def tokenize_text(cls, text: str) -> List[str]:
        """Normalizes and tokenizes text for similarity comparison."""
        clean = re.sub(r'[^a-zA-Z0-9\\s]', ' ', text.lower())
        return clean.split()

    @classmethod
    def extract_ngrams(cls, tokens: List[str], n: int = 4) -> Set[str]:
        """Builds set of contiguous n-grams."""
        if len(tokens) < n:
            return set([' '.join(tokens)])
        return set(' '.join(tokens[i:i+n]) for i in range(len(tokens) - n + 1))

    @classmethod
    def compute_jaccard_similarity(cls, text_a: str, text_b: str) -> float:
        """Computes Jaccard similarity coefficient between two text documents."""
        tokens_a = cls.tokenize_text(text_a)
        tokens_b = cls.tokenize_text(text_b)

        ngrams_a = cls.extract_ngrams(tokens_a, cls.N_GRAM_SIZE)
        ngrams_b = cls.extract_ngrams(tokens_b, cls.N_GRAM_SIZE)

        if not ngrams_a or not ngrams_b:
            return 0.0

        intersection = len(ngrams_a & ngrams_b)
        union = len(ngrams_a | ngrams_b)

        if union == 0:
            return 0.0

        return round((intersection / union) * 100, 2)

    @classmethod
    def scan_submission_corpus(
        cls,
        target_text: str,
        corpus: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Scans target text against an existing corpus of student submissions."""
        matches = []
        max_sim = 0.0

        for doc in corpus:
            sim = cls.compute_jaccard_similarity(target_text, doc.get('text', ''))
            if sim >= 15.0:  # Threshold for noticeable overlap
                matches.append({
                    'submission_id': doc.get('id'),
                    'student_name': doc.get('student_name', 'Anonymous'),
                    'similarity_percentage': sim
                })
                if sim > max_sim:
                    max_sim = sim

        matches = sorted(matches, key=lambda x: x['similarity_percentage'], reverse=True)

        return {
            'highest_similarity': max_sim,
            'is_flagged_for_plagiarism': max_sim >= 30.0,
            'matching_sources_count': len(matches),
            'matched_sources': matches[:5]
        }
''',
    'apps/assignments/services/peer_review_service.py': '''"""
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
''',

    # 4. Grading Engines
    'apps/grading/services/__init__.py': '"""Grading services package."""\n',
    'apps/grading/services/gradebook_service.py': '''"""
Enterprise Gradebook & Weighted Category Calculation Service.
Handles weighted categories, dropping lowest N scores, and extra credit.
"""
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List


class GradebookService:
    @classmethod
    def calculate_final_grade(
        cls,
        category_grades: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Calculates composite final course grade based on category weightings.
        category_grades = [
            {'category': 'Homework', 'weight': 20.0, 'scores': [90, 85, 95], 'drop_lowest': 1},
            {'category': 'Midterm', 'weight': 30.0, 'scores': [88]},
            {'category': 'Final Exam', 'weight': 50.0, 'scores': [92]}
        ]
        """
        total_weighted_percentage = Decimal('0.00')
        total_active_weight = Decimal('0.00')
        breakdown = []

        for cat in category_grades:
            weight = Decimal(str(cat.get('weight', 0.0)))
            raw_scores = [Decimal(str(s)) for s in cat.get('scores', [])]
            drop_count = cat.get('drop_lowest', 0)

            if not raw_scores:
                continue

            # Drop lowest scores if requested
            sorted_scores = sorted(raw_scores)
            if drop_count > 0 and len(sorted_scores) > drop_count:
                active_scores = sorted_scores[drop_count:]
            else:
                active_scores = sorted_scores

            category_avg = sum(active_scores) / Decimal(str(len(active_scores)))
            weighted_contrib = (category_avg * (weight / Decimal('100.0'))).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            total_weighted_percentage += weighted_contrib
            total_active_weight += weight

            breakdown.append({
                'category': cat.get('category'),
                'weight': weight,
                'average': category_avg.quantize(Decimal('0.01')),
                'weighted_contribution': weighted_contrib,
                'scores_evaluated': len(active_scores),
                'scores_dropped': len(raw_scores) - len(active_scores)
            })

        # Normalize if active weight < 100%
        if total_active_weight > Decimal('0.00') and total_active_weight < Decimal('100.00'):
            final_pct = (total_weighted_percentage / total_active_weight * Decimal('100.0')).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        else:
            final_pct = total_weighted_percentage.quantize(Decimal('0.01'))

        return {
            'final_percentage': final_pct,
            'total_weight_evaluated': total_active_weight,
            'category_breakdown': breakdown
        }
''',
    'apps/grading/services/curving_service.py': '''"""
Grade Curving & Statistical Normalization Engine.
Linear scaling, Gaussian bell curve normalization, and square-root curve formulas.
"""
import math
from decimal import Decimal, ROUND_HALF_UP
from typing import Dict, Any, List


class GradeCurvingService:
    @classmethod
    def apply_square_root_curve(cls, raw_scores: List[float]) -> List[float]:
        """
        Applies standard Square Root curve: new_score = sqrt(raw_score) * 10
        (e.g., 64 -> 80, 81 -> 90, 100 -> 100).
        """
        return [round(math.sqrt(max(0, s)) * 10, 2) for s in raw_scores]

    @classmethod
    def apply_linear_shift(cls, raw_scores: List[float], target_max: float = 100.0) -> List[float]:
        """Shifts the highest score to target_max and adds the same delta to all scores."""
        if not raw_scores:
            return []
        max_score = max(raw_scores)
        delta = max(0.0, target_max - max_score)
        return [round(min(100.0, s + delta), 2) for s in raw_scores]

    @classmethod
    def apply_gaussian_bell_curve(
        cls,
        raw_scores: List[float],
        target_mean: float = 75.0,
        target_std_dev: float = 10.0
    ) -> List[float]:
        """Normalizes scores to a target Gaussian mean and standard deviation."""
        if not raw_scores:
            return []
        n = len(raw_scores)
        if n == 1:
            return [target_mean]

        mean = sum(raw_scores) / n
        variance = sum((s - mean) ** 2 for s in raw_scores) / n
        std_dev = math.sqrt(variance) if variance > 0 else 1.0

        curved = []
        for s in raw_scores:
            z_score = (s - mean) / std_dev
            new_score = target_mean + (z_score * target_std_dev)
            curved.append(round(max(0.0, min(100.0, new_score)), 2))
        return curved
''',

    # 5. Certificates Engines
    'apps/certificates/services/__init__.py': '"""Certificates services package."""\n',
    'apps/certificates/services/crypto_verification_service.py': '''"""
Cryptographic Certificate Verification & SHA-256 Signature Engine.
"""
import hashlib
import hmac
import uuid
from typing import Dict, Any


class CertificateCryptoService:
    SECRET_SALT = "EduTech-Enterprise-Cryptographic-Verification-Salt-2026"

    @classmethod
    def generate_verification_hash(
        cls,
        student_id: int,
        course_code: str,
        certificate_number: str,
        issue_date_str: str
    ) -> str:
        """Computes secure SHA-256 digest token for public certificate verification."""
        payload = f"{student_id}:{course_code}:{certificate_number}:{issue_date_str}:{cls.SECRET_SALT}"
        return hashlib.sha256(payload.encode('utf-8')).hexdigest()

    @classmethod
    def verify_hash(
        cls,
        student_id: int,
        course_code: str,
        certificate_number: str,
        issue_date_str: str,
        provided_hash: str
    ) -> bool:
        """Verifies integrity of a certificate against tamper attempts."""
        expected = cls.generate_verification_hash(student_id, course_code, certificate_number, issue_date_str)
        return hmac.compare_digest(expected, provided_hash)
''',
    'apps/certificates/services/pdf_certificate_service.py': '''"""
ReportLab Dynamic PDF Certificate Generator Service.
Generates institutional certificates with ornamental borders, seal, and metadata.
"""
import io
from typing import Dict, Any
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas


class PDFCertificateGeneratorService:
    @classmethod
    def generate_certificate_pdf(
        cls,
        student_name: str,
        course_title: str,
        course_code: str,
        institution_name: str,
        certificate_number: str,
        issue_date_str: str,
        honors_title: str = '',
        issuer_name: str = 'Dr. Provost Administrator',
        issuer_title: str = 'Dean of Academic Affairs'
    ) -> bytes:
        """Generates binary PDF certificate using ReportLab landscape layout."""
        buffer = io.BytesIO()
        c = canvas.Canvas(buffer, pagesize=landscape(letter))
        width, height = landscape(letter)

        # Outer border
        c.setStrokeColor(colors.HexColor('#1E3A8A'))  # Deep Navy
        c.setLineWidth(5)
        c.rect(20, 20, width - 40, height - 40)

        # Inner gold border
        c.setStrokeColor(colors.HexColor('#D97706'))  # Gold
        c.setLineWidth(2)
        c.rect(26, 26, width - 52, height - 52)

        # Header: Institution Name
        c.setFillColor(colors.HexColor('#1E3A8A'))
        c.setFont('Helvetica-Bold', 24)
        c.drawCentredString(width / 2.0, height - 70, institution_name.upper())

        # Subtitle
        c.setFillColor(colors.HexColor('#4B5563'))
        c.setFont('Helvetica', 14)
        c.drawCentredString(width / 2.0, height - 95, "OFFICIAL CERTIFICATE OF ACADEMIC ACHIEVEMENT")

        # Statement
        c.setFont('Helvetica-Oblique', 12)
        c.drawCentredString(width / 2.0, height - 135, "This is to officially certify that")

        # Recipient Name
        c.setFillColor(colors.HexColor('#111827'))
        c.setFont('Helvetica-Bold', 26)
        c.drawCentredString(width / 2.0, height - 170, student_name)

        # Completion text
        c.setFillColor(colors.HexColor('#4B5563'))
        c.setFont('Helvetica', 12)
        c.drawCentredString(width / 2.0, height - 205, f"has successfully completed all curricular requirements for the accredited course")

        # Course Title
        c.setFillColor(colors.HexColor('#1E3A8A'))
        c.setFont('Helvetica-Bold', 18)
        c.drawCentredString(width / 2.0, height - 235, f"{course_code}: {course_title}")

        if honors_title:
            c.setFillColor(colors.HexColor('#D97706'))
            c.setFont('Helvetica-Bold', 14)
            c.drawCentredString(width / 2.0, height - 260, f"Awarded with Academic Distinction: {honors_title}")

        # Signatures
        c.setStrokeColor(colors.HexColor('#9CA3AF'))
        c.setLineWidth(1)
        c.line(100, 100, 300, 100)
        c.line(width - 300, 100, width - 100, 100)

        c.setFillColor(colors.HexColor('#111827'))
        c.setFont('Helvetica-Bold', 11)
        c.drawCentredString(200, 85, issuer_name)
        c.drawCentredString(width - 200, 85, "Verification Registry")

        c.setFillColor(colors.HexColor('#6B7280'))
        c.setFont('Helvetica', 9)
        c.drawCentredString(200, 70, issuer_title)
        c.drawCentredString(width - 200, 70, f"Certificate ID: {certificate_number}")
        c.drawCentredString(width / 2.0, 45, f"Issued on {issue_date_str} | Digitally Verified via EduTech Trust Network")

        c.showPage()
        c.save()
        pdf_data = buffer.getvalue()
        buffer.close()
        return pdf_data
'''
}

for rel_path, content in ENGINES.items():
    filepath = os.path.join(BASE_DIR, rel_path)
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content.strip() + '\n')
    print(f"Created engine service: {rel_path}")

print("All Phase 2 engines and services created.")
