"""
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
        clean = re.sub(r'[^a-zA-Z0-9\s]', ' ', text.lower())
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
