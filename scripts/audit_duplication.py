#!/usr/bin/env python3
"""Measure duplication in the repository.  Standard library only.

Reports (JSON with --json, otherwise a human table):
  * exact duplicate files (SHA-256)
  * near-duplicate Markdown pairs (difflib ratio after stripping each file's own
    name; threshold configurable, default 0.80)
  * per-field uniqueness for every registry (unique values / records)
  * lines repeated in three or more Markdown files

Exit status is 0 unless --fail-on-findings is given (CI report-only phase first).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "__pycache__", "node_modules", "dist", ".pytest_cache"}


def repo_files(root: Path = ROOT):
    for p in sorted(root.rglob("*")):
        if p.is_file() and not (set(p.relative_to(root).parts) & SKIP_DIRS):
            yield p


def exact_duplicates(root: Path = ROOT):
    by_hash: dict[str, list[str]] = defaultdict(list)
    for p in repo_files(root):
        by_hash[hashlib.sha256(p.read_bytes()).hexdigest()].append(str(p.relative_to(root)))
    return [sorted(v) for v in by_hash.values() if len(v) > 1]


def _name_variants(path: Path) -> list[str]:
    stem = path.parent.name if path.name in {"SKILL.md", "STAGE_PLAYBOOK.md", "README.md"} else path.stem
    words = re.split(r"[-_\s]+", stem)
    variants = {stem, " ".join(words), " ".join(w.title() for w in words), "-".join(words)}
    return sorted((v for v in variants if len(v) > 2), key=len, reverse=True)


def normalise(text: str, path: Path) -> str:
    text = re.sub(r"(?s)^---.*?---\s*", "", text)
    for v in _name_variants(path):
        text = re.sub(re.escape(v), " ", text, flags=re.I)
    text = re.sub(r"(?m)^#{1,6}\s+.*$", " ", text)
    text = re.sub(r"[*_>#`\[\]()|-]", " ", text)
    return re.sub(r"\s+", " ", text).strip().lower()


def _shingles(text: str, n: int = 4) -> set[str]:
    w = text.split()
    return {" ".join(w[i : i + n]) for i in range(max(len(w) - n + 1, 1))}


def near_duplicates(root: Path = ROOT, threshold: float = 0.80, scope: tuple[str, ...] | None = None):
    docs = {}
    for p in repo_files(root):
        if p.suffix != ".md":
            continue
        rel = p.relative_to(root)
        if scope and rel.parts[0] not in scope:
            continue
        norm = normalise(p.read_text(encoding="utf-8", errors="ignore"), p)
        if len(norm.split()) >= 40:
            docs[str(rel)] = (norm, _shingles(norm))
    pairs = []
    for a, b in combinations(sorted(docs), 2):
        (ta, sa), (tb, sb) = docs[a], docs[b]
        union = len(sa | sb)
        # cheap prefilter: Jaccard of 4-word shingles is a lower bound proxy for ratio
        if union == 0 or len(sa & sb) / union < threshold * 0.5:
            continue
        ratio = SequenceMatcher(None, ta, tb, autojunk=False).ratio()
        if ratio >= threshold:
            pairs.append((a, b, round(ratio, 3)))
    return sorted(pairs, key=lambda x: -x[2]), len(docs)


def _records(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    for v in data.values():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return v
    return []


def field_uniqueness(root: Path = ROOT):
    out = {}
    for p in sorted((root / "registry").glob("*")):
        if p.suffix not in {".yaml", ".json"}:
            continue
        try:
            recs = _records(p)
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not recs:
            continue
        fields = {}
        for k in recs[0]:
            vals = {json.dumps(r.get(k), sort_keys=True) for r in recs}
            fields[k] = {"unique": len(vals), "records": len(recs), "ratio": round(len(vals) / len(recs), 3)}
        out[p.name] = fields
    return out


def repeated_lines(root: Path = ROOT, min_files: int = 3, min_len: int = 25):
    seen: dict[str, set[str]] = defaultdict(set)
    for p in repo_files(root):
        if p.suffix != ".md":
            continue
        for line in p.read_text(encoding="utf-8", errors="ignore").splitlines():
            t = re.sub(r"\s+", " ", line.strip().lstrip("-*> ").strip())
            if len(t) >= min_len and not t.startswith("#") and not t.startswith("|"):
                seen[t].add(str(p.relative_to(root)))
    rep = [{"line": k, "files": len(v)} for k, v in seen.items() if len(v) >= min_files]
    return sorted(rep, key=lambda x: -x["files"])


def run(root: Path = ROOT, threshold: float = 0.80):
    files = list(repo_files(root))
    pairs, md_count = near_duplicates(root, threshold)
    return {
        "files": len(files),
        "bytes": sum(p.stat().st_size for p in files),
        "exact_duplicate_groups": exact_duplicates(root),
        "near_duplicate_threshold": threshold,
        "markdown_files_compared": md_count,
        "near_duplicate_pairs": [{"a": a, "b": b, "ratio": r} for a, b, r in pairs],
        "field_uniqueness": field_uniqueness(root),
        "repeated_lines": repeated_lines(root),
    }


def render(report: dict) -> str:
    lines = [
        f"files: {report['files']}  size: {report['bytes'] / 1e6:.2f} MB",
        f"exact duplicate groups: {len(report['exact_duplicate_groups'])}",
        f"markdown files compared: {report['markdown_files_compared']}",
        f"near-duplicate pairs (>= {report['near_duplicate_threshold']}): {len(report['near_duplicate_pairs'])}",
    ]
    for p in report["near_duplicate_pairs"][:15]:
        lines.append(f"  {p['ratio']:.3f}  {p['a']}  <->  {p['b']}")
    if len(report["near_duplicate_pairs"]) > 15:
        lines.append(f"  ... {len(report['near_duplicate_pairs']) - 15} more")
    lines.append(f"lines repeated in >=3 files: {len(report['repeated_lines'])}")
    for r in report["repeated_lines"][:8]:
        lines.append(f"  x{r['files']}  {r['line'][:90]}")
    lines.append("registry field uniqueness (unique/records), fields below 0.5:")
    for name, fields in report["field_uniqueness"].items():
        low = {k: f"{v['unique']}/{v['records']}" for k, v in fields.items() if v["ratio"] < 0.5}
        lines.append(f"  {name}: " + (", ".join(f"{k}={v}" for k, v in low.items()) or "none below 0.5"))
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--threshold", type=float, default=0.80)
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--fail-on-findings", action="store_true")
    args = ap.parse_args(argv)
    report = run(ROOT, args.threshold)
    print(json.dumps(report, indent=2) if args.json else render(report))
    bad = report["exact_duplicate_groups"] or report["near_duplicate_pairs"]
    return 1 if (args.fail_on_findings and bad) else 0


if __name__ == "__main__":
    sys.exit(main())
