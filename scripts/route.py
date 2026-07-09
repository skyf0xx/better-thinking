#!/usr/bin/env python3
"""Rank skills against a free-text task description via TF-IDF cosine similarity.

Loads skills/ROUTE_INDEX.json (built by scripts/build_route_index.py) and
skills/INDEX.json, vectorizes the query with the same vocabulary/IDF, and
prints the top-k candidate skills with scores. This gives the dispatcher a
real lexical shortlist instead of relying on an LLM to parse or recall the
full 131-entry index.

Usage:
    python3 scripts/route.py "why is this test flaky sometimes"
    python3 scripts/route.py --top 5 "should we build or buy this"

Falls back to a plain instruction if ROUTE_INDEX.json is missing or stale
relative to INDEX.json (regenerate with build_route_index.py).
"""
import argparse
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT, "skills", "INDEX.json")
ROUTE_INDEX_PATH = os.path.join(ROOT, "skills", "ROUTE_INDEX.json")

TOKEN_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

# Kept identical to build_route_index.py's list -- query terms must map to
# the same vocabulary the corpus vectors were built with.
STOPWORDS = {
    "a", "an", "the", "and", "or", "but", "of", "to", "in", "on", "for",
    "with", "is", "are", "was", "were", "be", "been", "being", "it", "its",
    "this", "that", "these", "those", "as", "at", "by", "from", "into",
    "than", "then", "so", "if", "when", "than", "not", "no", "any", "each",
    "own", "same", "over", "under", "again", "further", "once", "here",
    "there", "all", "both", "other", "such", "only", "can", "will", "just",
    "use", "used", "using", "e.g", "eg",
    "we", "you", "i", "they", "he", "she", "them", "us", "your", "our",
    "should", "would", "could", "might", "must", "shall", "may", "do",
    "does", "did", "have", "has", "had", "what", "which", "who", "whom",
    "how", "why", "some", "about", "out", "up", "down", "one", "get",
}


# Kept identical to build_route_index.py's stemmer -- query terms must
# fold onto the same roots the corpus vectors were stemmed with.
_SUFFIXES = ("ational", "ization", "fulness", "ousness", "iveness",
             "ing", "edly", "ies", "ied", "ied", "ion", "ions", "ed", "es", "s")


def stem(token):
    if "-" in token or len(token) <= 4:
        return token
    for suf in sorted(_SUFFIXES, key=len, reverse=True):
        if token.endswith(suf) and len(token) - len(suf) >= 3:
            return token[: -len(suf)]
    return token


def tokenize(text):
    tokens = TOKEN_RE.findall(text.lower())
    return [stem(t) for t in tokens if t not in STOPWORDS and len(t) > 1]


def vectorize_query(tokens, idf):
    if not tokens:
        return {}
    tf = {}
    for t in tokens:
        tf[t] = tf.get(t, 0) + 1
    max_tf = max(tf.values())
    weights = {}
    for term, count in tf.items():
        weight = idf.get(term)
        if weight is None:
            continue
        tf_weight = 0.5 + 0.5 * (count / max_tf)
        weights[term] = tf_weight * weight
    norm = math.sqrt(sum(w * w for w in weights.values())) or 1.0
    return {t: w / norm for t, w in weights.items()}


def cosine(a, b):
    if not a or not b:
        return 0.0
    shared = set(a) & set(b)
    return sum(a[t] * b[t] for t in shared)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="free-text description of the task")
    parser.add_argument("--top", type=int, default=8, help="number of candidates to return")
    args = parser.parse_args()

    if not os.path.exists(ROUTE_INDEX_PATH):
        print(
            "ROUTE_INDEX.json not found. Run: python3 scripts/build_route_index.py",
            file=sys.stderr,
        )
        return 1

    with open(ROUTE_INDEX_PATH) as f:
        route_index = json.load(f)
    with open(INDEX_PATH) as f:
        index = json.load(f)

    routable_count = sum(1 for s in index["skills"] if s.get("type") in ("atomic", "composite"))
    if route_index["counts"]["skills"] != routable_count:
        print(
            "WARNING: ROUTE_INDEX.json skill count does not match INDEX.json's "
            "atomic+composite count -- it is stale. Run: "
            "python3 scripts/build_route_index.py",
            file=sys.stderr,
        )

    skills_by_name = {s["name"]: s for s in index["skills"]}

    query_tokens = tokenize(args.query)
    query_vec = vectorize_query(query_tokens, route_index["idf"])

    scored = []
    for name, vec in route_index["vectors"].items():
        score = cosine(query_vec, vec)
        scored.append((score, name))
    scored.sort(key=lambda x: x[0], reverse=True)

    top = scored[: args.top]
    results = []
    for score, name in top:
        skill = skills_by_name.get(name, {})
        results.append(
            {
                "name": name,
                "score": round(score, 4),
                "type": skill.get("type"),
                "category": skill.get("category"),
                "one_line": skill.get("one_line"),
                "path": skill.get("path"),
            }
        )

    print(json.dumps(results, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
