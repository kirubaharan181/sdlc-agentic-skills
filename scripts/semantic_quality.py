"""Semantic similarity helpers for detecting name-only document duplication."""
from __future__ import annotations
from difflib import SequenceMatcher
import re


def normalized_content(value: str) -> str:
    value = re.sub(r"(?s)^---.*?---\s*", "", value)
    value = re.sub(r"(?m)^#{1,6}\s+.*$", " ", value)
    value = re.sub(r"[*_>#\-\[\]()]", " ", value)
    value = re.sub(r"\b(agent_id|skill_id|workflow_id)\s*:\s*\S+", " ", value, flags=re.I)
    value = re.sub(r"\s+", " ", value).strip().lower()
    return value


def shingles(text: str, n: int = 4) -> frozenset:
    words = text.split()
    return frozenset(" ".join(words[i:i + n]) for i in range(max(len(words) - n + 1, 1)))


def may_be_similar(a: str, b: str, threshold: float, sa: frozenset | None = None, sb: frozenset | None = None) -> bool:
    """Cheap prefilter. Two texts whose character-level ratio reaches `threshold` share most of their words in
    order, so their 4-word shingles overlap strongly; a Jaccard under 0.3 * threshold means the exact (slow)
    ratio cannot plausibly reach the threshold and can be skipped."""
    sa = sa if sa is not None else shingles(a)
    sb = sb if sb is not None else shingles(b)
    union = len(sa | sb)
    return union == 0 or len(sa & sb) / union >= 0.3 * threshold


def similarity(left: str, right: str) -> float:
    a, b = normalized_content(left), normalized_content(right)
    if not a or not b:
        return 1.0 if a == b else 0.0
    return SequenceMatcher(None, a, b, autojunk=False).ratio()


def find_near_duplicates(documents: dict[str, str], threshold: float = 0.88):
    names = sorted(documents)
    matches = []
    for index, left in enumerate(names):
        for right in names[index + 1:]:
            if not may_be_similar(normalized_content(documents[left]), normalized_content(documents[right]), threshold):
                continue
            score = similarity(documents[left], documents[right])
            if score >= threshold:
                matches.append((left, right, score))
    return matches
