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
            score = similarity(documents[left], documents[right])
            if score >= threshold:
                matches.append((left, right, score))
    return matches
