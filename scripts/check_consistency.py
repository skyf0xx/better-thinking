#!/usr/bin/env python3
"""Consistency checker for the better-thinking skill library.

Checks, with no dependencies beyond the stdlib:
  1. Every skills/<name>/SKILL.md has valid frontmatter with required fields.
  2. Frontmatter type/dependency rules: atomic has no dependencies; composite does.
  3. Token budget: atomic <= 900, composite <= 1700 (chars/4 estimate).
  4. skills/INDEX.json <-> filesystem: every built skill dir has an index entry
     and vice versa; counts in INDEX.json match reality.
  5. skills/INDEX.json <-> frontmatter: name/type/category/difficulty/related
     in the index match the SKILL.md frontmatter (index is generated from it).
  6. No dangling [[wiki-links]]: every link in a built skill's body or
     frontmatter `related`/`dependencies` resolves to a built or
     cataloged_not_built name in INDEX.json.
  7. Every name mentioned in TAXONOMY.md (backtick + difficulty marker) has a
     corresponding INDEX.json entry (built or cataloged_not_built) -- names
     that exist only in prose, with nothing tracking them, are silent gaps.

Exit code 0 if clean, 1 if any errors found. Run from repo root:
    python3 scripts/check_consistency.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")
INDEX_PATH = os.path.join(SKILLS_DIR, "INDEX.json")
TAXONOMY_PATH = os.path.join(ROOT, "TAXONOMY.md")

REQUIRED_FIELDS = [
    "name", "description", "type", "category", "difficulty",
    "tokens", "dependencies", "related",
]
VALID_CATEGORIES = {
    "reasoning", "problem-solving", "decision-making", "research", "analysis",
    "systems-strategy", "forecasting", "creativity", "communication",
    "collaboration", "learning", "metacognition", "ethics",
}
TOKEN_BUDGET = {"atomic": 900, "composite": 1700}

errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


def parse_frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    raw, body = m.group(1), m.group(2)
    fm = {}
    lines = raw.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        kv = re.match(r"^([a-zA-Z_]+):\s*(.*)$", line)
        if not kv:
            i += 1
            continue
        key, val = kv.group(1), kv.group(2)
        if val == ">":
            # folded block scalar: consume indented continuation lines
            i += 1
            block = []
            while i < len(lines) and (lines[i].startswith("  ") or lines[i].strip() == ""):
                block.append(lines[i].strip())
                i += 1
            fm[key] = " ".join(b for b in block if b)
            continue
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [x.strip() for x in inner.split(",") if x.strip()] if inner else []
        elif val.startswith("["):
            # multi-line list
            items = []
            rest = val[1:]
            i += 1
            while "]" not in rest and i < len(lines):
                rest += lines[i]
                i += 1
            rest = rest.split("]")[0]
            fm[key] = [x.strip() for x in rest.split(",") if x.strip()]
            continue
        else:
            fm[key] = val.strip()
        i += 1
    return fm, body


def estimate_tokens(path):
    return len(open(path, encoding="utf-8").read()) // 4


def check_skill_files(index_by_name):
    dirs = sorted(
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d))
    )
    fm_by_name = {}

    for d in dirs:
        path = os.path.join(SKILLS_DIR, d, "SKILL.md")
        if not os.path.isfile(path):
            err(f"skills/{d}/ has no SKILL.md")
            continue

        fm, body = parse_frontmatter(path)
        if fm is None:
            err(f"skills/{d}/SKILL.md: missing or malformed frontmatter")
            continue

        for field in REQUIRED_FIELDS:
            if field not in fm:
                err(f"skills/{d}/SKILL.md: missing required frontmatter field '{field}'")

        if fm.get("name") != d:
            err(f"skills/{d}/SKILL.md: frontmatter name '{fm.get('name')}' != directory name '{d}'")

        skill_type = fm.get("type")
        if skill_type not in ("atomic", "composite"):
            err(f"skills/{d}/SKILL.md: type must be 'atomic' or 'composite', got {skill_type!r}")
        elif skill_type == "atomic" and fm.get("dependencies"):
            err(f"skills/{d}/SKILL.md: atomic skill has non-empty dependencies {fm['dependencies']}")
        elif skill_type == "composite" and not fm.get("dependencies"):
            err(f"skills/{d}/SKILL.md: composite skill has no dependencies")

        category = fm.get("category")
        if category and category not in VALID_CATEGORIES:
            err(f"skills/{d}/SKILL.md: unknown category '{category}'")

        if skill_type in TOKEN_BUDGET:
            actual = estimate_tokens(path)
            budget = TOKEN_BUDGET[skill_type]
            if actual > budget:
                warn(f"skills/{d}/SKILL.md: ~{actual} tokens exceeds {skill_type} budget of {budget}")

        fm_by_name[d] = fm

        if d not in index_by_name:
            err(f"skills/{d}/SKILL.md exists but has no entry in INDEX.json")

    return fm_by_name, set(dirs)


def check_index_sync(index_data, fm_by_name, fs_dirs):
    index_by_name = {s["name"]: s for s in index_data["skills"]}

    built = [s for s in index_data["skills"] if s["status"] == "built"]
    total = len(index_data["skills"])
    counts = index_data.get("counts", {})
    if counts.get("built") != len(built):
        err(f"INDEX.json counts.built={counts.get('built')} but {len(built)} entries have status 'built'")
    if counts.get("total") != total:
        err(f"INDEX.json counts.total={counts.get('total')} but index has {total} entries")

    for s in built:
        name = s["name"]
        if s.get("category") == "recipes":
            continue  # recipes live under recipes/, not skills/
        if name not in fs_dirs:
            err(f"INDEX.json: '{name}' has status 'built' but skills/{name}/ does not exist")
            continue
        fm = fm_by_name.get(name)
        if not fm:
            continue
        for field in ("type", "category", "difficulty"):
            idx_val, fm_val = s.get(field), fm.get(field)
            fm_val_cast = int(fm_val) if field == "difficulty" and fm_val is not None else fm_val
            if str(idx_val) != str(fm_val_cast):
                err(f"INDEX.json '{name}'.{field}={idx_val!r} != frontmatter {fm_val_cast!r}")
        idx_related = sorted(s.get("related", []))
        fm_related = sorted(fm.get("related", []))
        if idx_related != fm_related:
            err(f"INDEX.json '{name}'.related={idx_related} != frontmatter related={fm_related}")

    return index_by_name


def check_dangling_links(fm_by_name, index_by_name):
    known = set(index_by_name) | {"better-thinking"}
    for name, fm in fm_by_name.items():
        if index_by_name.get(name, {}).get("status") != "built":
            continue
        path = os.path.join(SKILLS_DIR, name, "SKILL.md")
        text = open(path, encoding="utf-8").read()
        for link in re.findall(r"\[\[([a-z0-9-]+)\]\]", text):
            if link not in known:
                err(f"skills/{name}/SKILL.md: dangling link [[{link}]] (no such skill, built or cataloged)")
        for dep in fm.get("dependencies", []):
            if dep not in known:
                err(f"skills/{name}/SKILL.md: dependency '{dep}' does not resolve to any known skill")
        for rel in fm.get("related", []):
            if rel not in known:
                err(f"skills/{name}/SKILL.md: related '{rel}' does not resolve to any known skill")


def check_taxonomy_coverage(index_by_name):
    if not os.path.isfile(TAXONOMY_PATH):
        warn("TAXONOMY.md not found, skipping taxonomy coverage check")
        return
    text = open(TAXONOMY_PATH, encoding="utf-8").read()
    tax_names = set(re.findall(r"`([a-z0-9-]+)`\s*\((?:A|C)", text))
    known = set(index_by_name)
    for name in sorted(tax_names - known):
        err(f"TAXONOMY.md mentions '{name}' but INDEX.json has no entry for it (built or cataloged_not_built)")


def main():
    if not os.path.isfile(INDEX_PATH):
        print(f"FATAL: {INDEX_PATH} not found", file=sys.stderr)
        return 1
    try:
        index_data = json.load(open(INDEX_PATH, encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"FATAL: INDEX.json is not valid JSON: {e}", file=sys.stderr)
        return 1

    index_by_name_raw = {s["name"]: s for s in index_data["skills"]}
    fm_by_name, fs_dirs = check_skill_files(index_by_name_raw)
    index_by_name = check_index_sync(index_data, fm_by_name, fs_dirs)
    check_dangling_links(fm_by_name, index_by_name)
    check_taxonomy_coverage(index_by_name)

    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  WARN: {w}")
    if errors:
        print(f"{len(errors)} error(s):")
        for e in errors:
            print(f"  ERROR: {e}")
        return 1

    print(f"OK: {len(fs_dirs)} skill dirs, {len(index_data['skills'])} index entries, no inconsistencies found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
