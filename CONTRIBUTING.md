# Contributing to Saleasy

Thanks for improving Saleasy. Contributions that add a skill, sharpen a playbook or fix an error are all welcome.

## Adding or editing a skill

Each skill is a directory under `skills/` with a `SKILL.md` file and optional `references/`:

```
skills/
  skill-name/
    SKILL.md
    references/
```

`SKILL.md` needs YAML frontmatter with a `name` (kebab-case, matching the directory) and a `description` written in the third person with quoted trigger phrases. Keep the body imperative and under about 2000 words; move detail into `references/`.

## House style (enforced by CI)

The linter at `scripts/lint-skills.py` runs on every push and pull request and blocks the merge on any violation:
- No em dashes or en dashes. Use parentheses or commas.
- Straight quotes and apostrophes only.
- Every skill has valid frontmatter with a matching name and a description.
- No comma before "and" or "or" (no Oxford comma). Write "A, B and C".
- No marketing superlatives (the linter blocks a built-in list).
- Each skill description is third person and includes at least one quoted trigger phrase.

Also keep a neutral and factual tone and vary list lengths rather than always grouping in threes.

Run the linter locally before opening a pull request:

```
python3 scripts/lint-skills.py
```

## Pull requests

Keep changes focused. Describe what you changed and why. If you add a skill, update the skill table in `README.md` and add a line to `CHANGELOG.md`.
