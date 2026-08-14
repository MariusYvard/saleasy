#!/usr/bin/env python3
"""Lint Saleasy skills and docs.

Checks (any failure exits non-zero so CI blocks the merge):
1. Every saleasy/skills/*/SKILL.md has YAML frontmatter with name and description, the
   name matches its directory, the description is third person and carries at
   least one quoted trigger phrase.
2. No em dash or en dash and no curly quotes in any tracked markdown file.
3. No comma before "and", "or" or "et" (the house style bans the Oxford comma
   and serial commas). Add an inline "lint-allow-comma" marker to skip a line.
4. No marketing superlative from the banned list.
5. marketplace.json declares the plugin in its own subdirectory and carries no
   version of its own.
"""
import json
import os
import re
import sys

PLUGIN_NAME = "saleasy"
PLUGIN_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(PLUGIN_ROOT)
SKILLS_DIR = os.path.join(PLUGIN_ROOT, "skills")
SKILLS_LABEL = os.path.relpath(SKILLS_DIR, ROOT).replace(os.sep, "/")

BANNED_CHARS = {"—": "em dash", "–": "en dash",
                "“": "left curly quote", "”": "right curly quote",
                "‘": "left curly apostrophe", "’": "right curly apostrophe"}

# Marketing superlatives the house style rejects. Word-boundary, case-insensitive.
BANNED_WORDS = [
    "pivotal", "crucial", "emblematic", "emblematique", "incontournable",
    "revolutionary", "revolutionnaire", "visionary", "visionnaire",
    "seamless", "cutting-edge", "game-changer", "game changer",
    "best-in-class", "world-class", "unleash", "pioneering", "groundbreaking",
    "state-of-the-art", "rich tapestry", "riche tapisserie",
]

OXFORD_RE = re.compile(r",\s+(and|or|et)\b", re.IGNORECASE)
WORD_RES = [(re.compile(r"(?<![\w-])" + re.escape(w) + r"(?![\w-])", re.IGNORECASE), w)
            for w in BANNED_WORDS]

errors = []


def md_files():
    for base, _dirs, files in os.walk(ROOT):
        if os.sep + ".git" in base:
            continue
        for f in files:
            if f.endswith(".md"):
                yield os.path.join(base, f)


def check_lines():
    for path in md_files():
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            for i, line in enumerate(fh, 1):
                for ch, label in BANNED_CHARS.items():
                    if ch in line:
                        errors.append(f"{rel}:{i} contains a {label}")
                if OXFORD_RE.search(line) and "lint-allow-comma" not in line:
                    errors.append(f"{rel}:{i} has a comma before and/or/et (Oxford comma)")
                for rx, word in WORD_RES:
                    if rx.search(line):
                        errors.append(f"{rel}:{i} uses a banned superlative '{word}'")


def check_frontmatter():
    if not os.path.isdir(SKILLS_DIR):
        errors.append(f"{SKILLS_LABEL}/ directory is missing")
        return
    for name in sorted(os.listdir(SKILLS_DIR)):
        skill_path = os.path.join(SKILLS_DIR, name)
        if not os.path.isdir(skill_path):
            continue
        md = os.path.join(skill_path, "SKILL.md")
        if not os.path.isfile(md):
            errors.append(f"{SKILLS_LABEL}/{name} has no SKILL.md")
            continue
        with open(md, encoding="utf-8") as fh:
            text = fh.read()
        m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
        if not m:
            errors.append(f"{SKILLS_LABEL}/{name}/SKILL.md has no YAML frontmatter")
            continue
        fm = m.group(1)
        name_match = re.search(r"^name:\s*(\S+)", fm, re.MULTILINE)
        if not name_match:
            errors.append(f"{SKILLS_LABEL}/{name}/SKILL.md frontmatter missing name")
        elif name_match.group(1) != name:
            errors.append(
                f"{SKILLS_LABEL}/{name}/SKILL.md name '{name_match.group(1)}' "
                f"does not match directory '{name}'")
        desc_match = re.search(r"^description:\s*(.*?)(?=^\w+:|\Z)", fm,
                               re.MULTILINE | re.DOTALL)
        if not desc_match or not desc_match.group(1).strip():
            errors.append(f"{SKILLS_LABEL}/{name}/SKILL.md frontmatter missing description")
            continue
        desc = " ".join(desc_match.group(1).split())
        if not re.search(r"\bthis skill\b", desc, re.IGNORECASE):
            errors.append(f"{SKILLS_LABEL}/{name}/SKILL.md description is not third person "
                          f"(expected to start with 'This skill ...')")
        if '"' not in desc:
            errors.append(f"{SKILLS_LABEL}/{name}/SKILL.md description has no quoted trigger phrase")


def check_marketplace():
    """The plugin must live in a subdirectory so installed users get updates."""
    path = os.path.join(ROOT, ".claude-plugin", "marketplace.json")
    if not os.path.isfile(path):
        errors.append(".claude-plugin/marketplace.json is missing")
        return
    with open(path, encoding="utf-8") as fh:
        data = json.load(fh)
    entries = [p for p in data.get("plugins", []) if p.get("name") == PLUGIN_NAME]
    if not entries:
        errors.append(f"marketplace.json has no plugin entry named '{PLUGIN_NAME}'")
        return
    entry = entries[0]
    if entry.get("source") != "./" + PLUGIN_NAME:
        errors.append(f"marketplace.json source is '{entry.get('source')}', "
                      f"expected './{PLUGIN_NAME}'")
    if "version" in entry:
        errors.append("marketplace.json carries a version; it belongs in plugin.json only")
    if not os.path.isfile(os.path.join(PLUGIN_ROOT, ".claude-plugin", "plugin.json")):
        errors.append(f"{PLUGIN_NAME}/.claude-plugin/plugin.json is missing")


def main():
    check_marketplace()
    check_frontmatter()
    check_lines()
    if errors:
        print("Saleasy lint failed:")
        for e in errors:
            print("  - " + e)
        sys.exit(1)
    print("Saleasy lint passed.")


if __name__ == "__main__":
    main()
