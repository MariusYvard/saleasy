# Changelog

## 0.5.0

Changed
- Removed serial (Oxford) commas across the skills and docs to match the house style.
- The CI linter now also blocks any comma before "and" or "or", a built-in list of marketing superlatives and a description that is not third person or has no quoted trigger phrase.
- The version is declared once in plugin.json. The per-skill metadata block was removed.

Added
- plugin.json now declares homepage and repository.

## 0.4.0

Changed
- Consolidated from eight skills to four for simplicity: `saleasy-setup`, `marketing`, `prospecting`, `selling`. Each skill asks a short question on invocation when the job is not already clear, then loads the matching playbook.
- `prospecting` now covers finding and qualifying leads, automated signal monitoring, outreach writing and the draft-validate-send protocol (formerly lead-finder, signal-monitor and outreach).
- `selling` now covers call prep and summary, pipeline, forecast, closing, negotiation, proposals, account growth and the daily brief and weekly review (formerly deal-desk, account-growth and daily-cockpit).
- `marketing` replaces content-studio with the same coverage plus repurposing, lead magnets and positioning.

Removed
- The separate content-studio, lead-finder, signal-monitor, outreach, deal-desk, account-growth and daily-cockpit skills. Their content is preserved as references inside the four skills.

## 0.3.0

Added
- A draft, validate, send protocol: Claude drafts, the user approves a batch, Claude sends through the connected authorized email tool, then logs status.
- Automated signal monitoring on a schedule from legitimate sources.
- Compliant contact discovery and a GDPR and opt-out section.

Changed
- Clarified the sending stance: authorized official APIs after explicit validation; no unofficial LinkedIn automation and no circumvention of anti-bot or detection systems.

## 0.2.0

Added
- Post-sale account growth (expansion, renewal risk, referrals).
- Advanced lead scoring (knockout gates, named tiers, list-quality scorecard, deep-dive), cold-email copywriting, account-based motions, measurement, closing and negotiation playbooks, proposals and the POWERFUL framework.
- Repo tooling: a CI linter enforcing no em dashes, straight quotes and valid skill frontmatter, plus CONTRIBUTING and templates.

Changed
- Outreach cadence standardized to J0, J3, J7, J10 with guardrails and a message quality gate.
- Defined the canonical `saleasy-pipeline` tracking file.

## 0.1.0

Added
- Initial release: profile-driven, tool-agnostic plugin with marketplace and plugin manifests and an MIT license.
