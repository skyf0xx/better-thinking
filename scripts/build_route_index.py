#!/usr/bin/env python3
"""Build a TF-IDF lexical index over skill descriptions for routing.

Reads skills/INDEX.json (name, one_line, triggers, category per skill) plus
each skill's "## Examples" section straight from its SKILL.md body -- the
Examples are where a lot of the sharpest disambiguating vocabulary actually
lives (e.g. "build-versus-buy" under decision-analysis), and INDEX.json
deliberately doesn't carry that much text. Writes skills/ROUTE_INDEX.json:
a vocabulary, IDF weights, and a sparse TF-IDF vector per skill.
scripts/route.py loads this file to rank skills against a free-text task
description via cosine similarity, without an LLM having to parse or
recall the full index.

No third-party dependencies -- stdlib only, so this runs in any Claude
Code environment without a package install step.

Regenerate after adding, removing, or editing any skill's one_line,
triggers, or Examples text:
    python3 scripts/build_route_index.py
"""
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT, "skills", "INDEX.json")
OUT_PATH = os.path.join(ROOT, "skills", "ROUTE_INDEX.json")

EXAMPLES_SECTION_RE = re.compile(
    r"^##\s*Examples\s*\n(.*?)(?=\n##\s|\Z)", re.MULTILINE | re.DOTALL
)
BULLET_RE = re.compile(r"^\s*-\s+", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[([^\]]+)\]\]")
MD_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")

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

TOKEN_RE = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")

# Suffix stripping only -- enough to fold "negotiating"/"negotiation",
# "deciding"/"decision"-adjacent forms, etc. onto a shared root without
# pulling in a third-party stemmer dependency. Deliberately conservative:
# false merges are worse than missed ones for a routing signal.
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


def read_examples(skill_path):
    """Extract the '## Examples' bullet list straight from a SKILL.md body.

    Returns plain text with wiki-links/markdown-links unwrapped to their
    label text, so e.g. "[[decision-analysis]]" contributes the token
    "decision analysis" rather than being dropped or left with brackets.
    """
    full_path = os.path.join(ROOT, skill_path)
    if not os.path.exists(full_path):
        return ""
    with open(full_path) as f:
        body = f.read()
    match = EXAMPLES_SECTION_RE.search(body)
    if not match:
        return ""
    section = match.group(1)
    section = BULLET_RE.sub(" ", section)
    section = WIKILINK_RE.sub(lambda m: m.group(1).replace("-", " "), section)
    section = MD_LINK_RE.sub(lambda m: m.group(1), section)
    return section


# Per-field weights for combining field-level term counts into one document.
# Fields are weighted by importance rather than concatenated as raw text --
# concatenation lets a long field (Examples) dilute a short, important one
# (name) purely by word count. name/one_line/triggers are the primary
# routing signal; Examples and category widen recall without dominating.
FIELD_WEIGHTS = {
    "name": 4.0,
    "one_line": 2.0,
    "triggers": 2.0,
    "disambiguates_from": 1.5,
    "category": 0.5,
    "examples": 1.0,
}


def build_doc_fields(skill):
    """Return {field: [tokens]} for a skill, before weighting/combining."""
    return {
        "name": tokenize(skill.get("name", "").replace("-", " ")),
        "one_line": tokenize(skill.get("one_line", "")),
        "triggers": tokenize(skill.get("triggers", "")),
        "disambiguates_from": tokenize(
            skill.get("disambiguates_from", "")
            if isinstance(skill.get("disambiguates_from"), str)
            else ""
        ),
        "category": tokenize(skill.get("category", "")),
        "examples": tokenize(read_examples(skill.get("path", ""))),
    }


def main():
    with open(INDEX_PATH) as f:
        index = json.load(f)

    # Recipes live in the same skills[] array (type: "recipe") but aren't
    # invocable skills -- exclude them from the routable set.
    skills = [s for s in index["skills"] if s.get("type") in ("atomic", "composite")]

    # Weighted term frequency per doc: each field's token counts are scaled
    # by FIELD_WEIGHTS before being summed, so a long Examples section can't
    # dilute the name/one_line signal just by contributing more raw tokens.
    doc_weighted_tf = {}
    for skill in skills:
        name = skill["name"]
        fields = build_doc_fields(skill)
        wtf = {}
        for field, tokens in fields.items():
            weight = FIELD_WEIGHTS[field]
            for t in tokens:
                wtf[t] = wtf.get(t, 0.0) + weight
        doc_weighted_tf[name] = wtf

    n_docs = len(doc_weighted_tf)
    doc_freq = {}
    for wtf in doc_weighted_tf.values():
        for term in wtf:
            doc_freq[term] = doc_freq.get(term, 0) + 1

    vocab = sorted(doc_freq.keys())
    idf = {
        term: math.log((1 + n_docs) / (1 + doc_freq[term])) + 1.0
        for term in vocab
    }

    vectors = {}
    for name, wtf in doc_weighted_tf.items():
        if not wtf:
            vectors[name] = {}
            continue
        max_tf = max(wtf.values())
        weights = {}
        for term, count in wtf.items():
            tf_weight = 0.5 + 0.5 * (count / max_tf)
            weights[term] = round(tf_weight * idf[term], 6)
        norm = math.sqrt(sum(w * w for w in weights.values())) or 1.0
        vectors[name] = {t: round(w / norm, 6) for t, w in weights.items()}

    out = {
        "$schema_note": (
            "Generated by scripts/build_route_index.py from skills/INDEX.json. "
            "Do not hand-edit -- regenerate instead. Used by scripts/route.py "
            "for lexical (TF-IDF cosine) skill retrieval at dispatch time."
        ),
        "generated_from": "skills/INDEX.json",
        "counts": {"skills": n_docs, "vocab_size": len(vocab)},
        "idf": idf,
        "vectors": vectors,
    }

    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, sort_keys=False)
        f.write("\n")

    print(f"Wrote {OUT_PATH}: {n_docs} skills, {len(vocab)} vocab terms.")


if __name__ == "__main__":
    sys.exit(main())
