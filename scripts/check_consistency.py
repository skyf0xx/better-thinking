#!/usr/bin/env python3
"""Consistency checker for the better-thinking skill library.

Checks, with no dependencies beyond the stdlib:
  1. Every built skill's file (resolved via its INDEX.json `path`) has valid
     frontmatter with required fields. Entry-point skills (better-thinking,
     better-thinking-recipes) live at skills/<name>/SKILL.md; every other
     skill lives at skills/library/<name>.md.
  2. Frontmatter type/dependency rules: atomic and dispatcher have no
     dependencies; composite does. 'dispatcher' is reserved for the
     entry-point skills in ENTRY_POINT_SKILLS.
  3. Token budget: atomic <= 900, composite <= 1700, dispatcher <= 2000
     (chars/4 estimate), except per-skill overrides in
     TOKEN_BUDGET_EXCEPTIONS (documented in CONTRIBUTING.md).
  4. skills/INDEX.json <-> filesystem: every built skill's `path` resolves to
     a real file; counts in INDEX.json match reality.
  5. skills/INDEX.json <-> frontmatter: name/type/category/difficulty/related
     in the index match the skill file's frontmatter (index is generated from it).
  6. No dangling [[wiki-links]]: every link in a built skill's body or
     frontmatter `related`/`dependencies` resolves to a built name in
     INDEX.json.
  7. Every name mentioned in catalog/*.md (backtick + difficulty marker) has a
     corresponding built INDEX.json entry -- names that exist only in catalog
     prose, with nothing built, are silent gaps (see e.g. the
     scientific-method incident this script was written to catch in the
     future).

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
CATALOG_DIR = os.path.join(ROOT, "catalog")

REQUIRED_FIELDS = [
    "name", "description", "type", "category", "difficulty",
    "tokens", "dependencies", "related",
]
VALID_CATEGORIES = {
    "reasoning", "problem-solving", "decision-making", "research", "analysis",
    "systems-strategy", "forecasting", "creativity", "communication",
    "collaboration", "learning", "metacognition", "ethics",
}
TOKEN_BUDGET = {"atomic": 900, "composite": 1700, "dispatcher": 2000}
# Per-skill budget exceptions, documented in CONTRIBUTING.md's "Stay in
# budget" section. Grant sparingly -- a skill earns one by actually needing
# more procedure text for its specific job, not by category membership.
TOKEN_BUDGET_EXCEPTIONS = {"better-thinking-recipes": 2500}

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


# Entry-point skills stay at skills/<name>/SKILL.md and are real slash
# commands; every other skill lives at skills/library/<name>.md, read by
# the dispatcher as reference text rather than independently invocable.
ENTRY_POINT_SKILLS = {"better-thinking", "better-thinking-recipes"}


def check_skill_files(index_by_name):
    fm_by_name = {}
    rel_by_name = {}

    for name, entry in index_by_name.items():
        if entry.get("category") == "recipes":
            continue
        if entry.get("status") != "built":
            continue

        rel_path = entry.get("path")
        if not rel_path:
            err(f"INDEX.json: '{name}' has no 'path' field")
            continue

        expected_rel = (
            f"skills/{name}/SKILL.md" if name in ENTRY_POINT_SKILLS
            else f"skills/library/{name}.md"
        )
        if rel_path != expected_rel:
            err(f"INDEX.json: '{name}'.path={rel_path!r} does not match expected location {expected_rel!r}")

        path = os.path.join(ROOT, rel_path)
        if not os.path.isfile(path):
            err(f"'{name}': path {rel_path} does not exist")
            continue

        fm, body = parse_frontmatter(path)
        if fm is None:
            err(f"{rel_path}: missing or malformed frontmatter")
            continue

        for field in REQUIRED_FIELDS:
            if field not in fm:
                err(f"{rel_path}: missing required frontmatter field '{field}'")

        if fm.get("name") != name:
            err(f"{rel_path}: frontmatter name '{fm.get('name')}' != INDEX.json name '{name}'")

        skill_type = fm.get("type")
        if skill_type not in ("atomic", "composite", "dispatcher"):
            err(f"{rel_path}: type must be 'atomic', 'composite', or 'dispatcher', got {skill_type!r}")
        elif skill_type == "dispatcher" and name not in ENTRY_POINT_SKILLS:
            err(f"{rel_path}: type 'dispatcher' is reserved for entry-point skills {ENTRY_POINT_SKILLS}, got '{name}'")
        elif skill_type in ("atomic", "dispatcher") and fm.get("dependencies"):
            err(f"{rel_path}: {skill_type} skill has non-empty dependencies {fm['dependencies']}")
        elif skill_type == "composite" and not fm.get("dependencies"):
            err(f"{rel_path}: composite skill has no dependencies")

        category = fm.get("category")
        if category and category not in VALID_CATEGORIES:
            err(f"{rel_path}: unknown category '{category}'")

        if skill_type in TOKEN_BUDGET:
            actual = estimate_tokens(path)
            budget = TOKEN_BUDGET_EXCEPTIONS.get(name, TOKEN_BUDGET[skill_type])
            if actual > budget:
                warn(f"{rel_path}: ~{actual} tokens exceeds {skill_type} budget of {budget}")

        fm_by_name[name] = fm
        rel_by_name[name] = rel_path

    return fm_by_name, rel_by_name


def check_index_sync(index_data, fm_by_name):
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
        fm = fm_by_name.get(name)
        if not fm:
            continue  # already reported as missing/unresolvable by check_skill_files
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


def check_dangling_links(fm_by_name, rel_by_name, index_by_name):
    known = set(index_by_name) | {"better-thinking"}
    for name, fm in fm_by_name.items():
        if index_by_name.get(name, {}).get("status") != "built":
            continue
        rel_path = rel_by_name[name]
        path = os.path.join(ROOT, rel_path)
        text = open(path, encoding="utf-8").read()
        for link in re.findall(r"\[\[([a-z0-9-]+)\]\]", text):
            if link not in known:
                err(f"{rel_path}: dangling link [[{link}]] (no such skill, built or cataloged)")
        for dep in fm.get("dependencies", []):
            if dep not in known:
                err(f"{rel_path}: dependency '{dep}' does not resolve to any known skill")
        for rel in fm.get("related", []):
            if rel not in known:
                err(f"{rel_path}: related '{rel}' does not resolve to any known skill")


def check_catalog_coverage(index_by_name):
    if not os.path.isdir(CATALOG_DIR):
        warn("catalog/ not found, skipping catalog coverage check")
        return
    known = set(index_by_name)
    for fname in sorted(os.listdir(CATALOG_DIR)):
        if not fname.endswith(".md"):
            continue
        path = os.path.join(CATALOG_DIR, fname)
        text = open(path, encoding="utf-8").read()
        # full spec headers: "### skill-name `atomic · D2 · ~500 tok`"
        for name in re.findall(r"^### ([a-z0-9-]+) `(?:atomic|composite)", text, re.MULTILINE):
            if name not in known:
                err(f"catalog/{fname} fully specs '{name}' but INDEX.json has no entry for it — "
                    f"either build it (skills/library/{name}.md) or remove the catalog spec")


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
    fm_by_name, rel_by_name = check_skill_files(index_by_name_raw)
    index_by_name = check_index_sync(index_data, fm_by_name)
    check_dangling_links(fm_by_name, rel_by_name, index_by_name)
    check_catalog_coverage(index_by_name)

    if warnings:
        print(f"{len(warnings)} warning(s):")
        for w in warnings:
            print(f"  WARN: {w}")
    if errors:
        print(f"{len(errors)} error(s):")
        for e in errors:
            print(f"  ERROR: {e}")
        return 1

    print(f"OK: {len(fm_by_name)} skill files, {len(index_data['skills'])} index entries, no inconsistencies found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
