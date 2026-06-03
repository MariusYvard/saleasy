# Changelog

## 0.7.0

Changed
- `prospecting` now owns every outbound writing job. Its description triggers on "rédige un mail", "écris une relance", "draft an email" and "write a follow-up". Now `selling` and `marketing` route any cold or outbound drafting to it so each message passes the quality gate, the cadence and the send protocol.
- The cadence is now standard, not optional: draft J0, J3, J7 and J10 together, then propose a scheduled reminder for the first follow-up.
- Pipeline traceability is a step of the send protocol: after a send Saleasy writes stage, contact dates, owner and channel back to the CRM, keyed on the email.

Added
- A safe Google Sheets CRM write routine in `sending.md`: prefer a Sheets API connector, back up before writing, key every row by email, navigate by the Name box, never Ctrl+A in the find box and write one cell at a time. Referenced from `selling` and `CONNECTORS.md`.
- Gmail draft limits: the connector creates but cannot edit or delete a draft, so freeze the content first, check for an existing draft and never regenerate.
- A signature rule: `saleasy-setup` collects a light inline HTML signature up front and `messaging.md` embeds it in every draft, because connector drafts do not inherit the Gmail signature.
- Reinforced multi-contact deduplication: one live thread per company at a time, spaced sends when a company has two contacts.
- Profile-template fields for signature (HTML), CRM URL, CRM column mapping, CRM write mode and authorized send channels.

## 0.6.0

Added
- A France open-data pack. Finding can use the API Recherche d'entreprises and the INSEE Sirene API for compliant firmographics. Monitoring can use the BODACC API for dated company-event signals. Setup offers it for a French market and CONNECTORS lists the sources.

## 0.5.0

Changed
- Removed serial (Oxford) commas across the skills and docs to match the house style.
- The CI linter now also blocks any comma before "and" or "or", a built-in list of marketing superlatives and a description that is not third person or has no quoted trigger phrase.
- The version is declared once in plugin.json. The per-skill metadata block was removed.
- Rewrote the README to document the four skills, the twelve playbooks and the repo tooling.

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
