# Saleasy

Saleasy is a commercial cockpit for Claude. It runs the full life of a deal from a single plugin: set up your profile once, then attract, prospect, sell and grow accounts. The surface is four skills, but each skill loads a library of detailed playbooks, so the plugin behaves like a complete sales and marketing system rather than a thin prompt wrapper.

It is profile driven. The first run interviews you and saves a profile (market, offer, persona, tone, tools). Every skill reads that profile, so the output is already adapted to your role, market and voice. The same repository works for anyone who clones it because the profile is generated per user and never committed.

## What is inside

- 4 skills that map to the real stages of a deal.
- 12 reference playbooks loaded on demand, so the model pulls only the guidance it needs for the job at hand.
- A house-style linter wired to GitHub Actions, plus contribution and issue templates.
- A compliance posture written into every skill (authorized data sources, official sending APIs, GDPR).

The skills stay short on purpose. The depth lives in the `references/` folders, which a skill opens only for the matching task. This keeps each invocation focused while giving you the full method behind it.

## The four skills

| Skill | When it runs | Reference playbooks |
| --- | --- | --- |
| `saleasy-setup` | First run or "reconfigure saleasy" | profile template and per-type presets |
| `marketing` | "écris un post LinkedIn", "plan de contenu", "audit SEO" | one playbook covering nine content jobs |
| `prospecting` | "trouve des leads", "écris un cold email", "mets en place une veille" | finding, messaging, monitoring, sending |
| `selling` | "prépare mon RDV", "revue de pipeline", "négociation", "renewal" | deals, methodologies, closing-negotiation, proposals, growth, cockpit |

## What each skill actually covers

### saleasy-setup
A short interview that detects your profile type (founder, SDR, AE, full-cycle, marketer, agency) then writes `saleasy-profile.md`. It records identity, offer, target ICP and persona, differentiation, motion, voice, connected tools, sending authorizations and proof assets. Presets seed sensible defaults per profile type so you are not starting from a blank page.

### marketing
One playbook with nine jobs: LinkedIn post, LinkedIn profile, editorial calendar, campaign one-pager, long-form copy (blog, landing, newsletter), SEO (search intent, on-page, content-gap, technical audit), repurposing a pillar into derivatives, lead magnets and positioning frames (challenger reframe, category creation, niche, jobs-to-be-done, blue-ocean). Every output ties to a buyer pain and a funnel stage. It pulls proof from the profile instead of inventing claims.

### prospecting
Four playbooks for the top of the funnel.

- finding: ICP definition, compliant discovery with a source priority order, a GDPR and ePrivacy data-protection section, cleaning and deduplication, enrichment that marks verified against inferred, a tension-signal taxonomy weighted by freshness, scoring with knockout gates and named tiers, a list-quality scorecard, lookalike and competitor sourcing, a five-axis deep dive and the pipeline file schema.
- messaging: a personalization decision gate, opener and subject-line patterns, body discipline, the J0/J3/J7/J10 cadence with guardrails, a 0 to 10 quality gate, a reply and objection map, account-based multithreading, competitive battle cards and a measurement model built on positive reply rate.
- monitoring: a watchlist, scheduled passes over legitimate sources, freshness weighting, alert promotion and a per-run digest.
- sending: the draft, validate, send approval gate, channel rules, hard limits against anti-bot circumvention, consent and regional rules, plus queued automated follow-ups that still wait for your yes.

### selling
Six playbooks from first meeting to renewal.

- methodologies: BANT, MEDDIC, SPICED and the eight-dimension POWERFUL scorecard for qualification; SPIN, Challenger and Gap Selling for discovery.
- deals: a call-prep one-pager, a structured call summary, a pipeline review that scores each deal against the chosen framework and a forecast with commit, best-case and pipeline scenarios.
- closing-negotiation: a nine-item close-readiness score, closing techniques matched to signals, objection classification with ACIR, a tiered concession ladder, a stakeholder politics map and a champion builder.
- proposals: a Good, Better, Best structure and a findings-to-ROI model with conservative, likely and optimistic columns.
- growth: expansion triggers, renewal-risk banding with a save plan and a referral track.
- cockpit: a ranked morning briefing and an honest weekly review, both able to run on a schedule.

## Profile-driven design

The first time you use it, `saleasy-setup` runs a short interview and saves a profile: market, offer, target persona, tone and connected tools. Every other skill reads that profile first, so its output is adapted to your situation from the start. Because the profile is generated per user, the same repository works for anyone who clones it.

## Compliance and sending

Saleasy follows a draft, validate, send model. Claude drafts, you approve a batch and Claude sends the approved items through your connected authorized tool (email via the official Gmail or Microsoft 365 API), then logs the result to your pipeline. Nothing is sent without your explicit yes. With monitoring and a scheduled task, Saleasy can watch accounts and prepare due follow-ups on its own, but the approval gate still applies.

Saleasy stays within platform terms. It does not automate LinkedIn connection requests or DMs through unofficial automation and does not bypass anti-bot, rate-limit or detection systems. For a channel with no compliant programmatic send, it gives you a ready-to-send draft. Contact data comes from authorized providers and public sources, handled in line with GDPR.

## Working files

Saleasy keeps two per-user files in your working folder, both git-ignored so personal data never lands in the repo.

- `saleasy-profile.md`: your market, offer, persona, tone and tools. Read by every skill.
- `saleasy-pipeline.md` (or `.csv`): the lead and deal tracker created by prospecting and updated by selling. When a CRM is connected, the CRM is the source of truth and this file is a mirror.

## Install

This repository is a Claude plugin marketplace. Add it, then install the plugin.

```
/plugin marketplace add MariusYvard/saleasy
/plugin install saleasy@saleasy
```

## Setup

No environment variables are required. Saleasy works standalone with web search and gets stronger when you connect tools: email, calendar, CRM, lead data, social, spreadsheet. See `CONNECTORS.md`. On first run, ask Saleasy to "configure saleasy". It writes `saleasy-profile.md` in your working folder, which you can edit by hand anytime.

## How to use it

Describe the moment and the right skill loads, then asks what you want if the job is not already clear. Set up once, ask `selling` for a morning brief to start the day, use `prospecting` to fill and work the funnel, `marketing` to stay visible and `selling` around meetings, at close and for renewals.

## Customization

Saleasy refers to tools by category, so it adapts to whatever you connect: email, calendar, CRM, lead data, social, spreadsheet, call notes. The `saleasy-setup` profile records your real tool in each category. See `CONNECTORS.md`.

## Repo tooling

The repository ships its own quality gate. `scripts/lint-skills.py` runs on every push and pull request through GitHub Actions and blocks a merge on any house-style violation: a comma before "and" or "or", a banned marketing superlative, a missing or malformed skill description, em dashes or curly quotes. Issue and pull-request templates plus a CONTRIBUTING guide keep additions consistent. The MIT license and a `.gitignore` that excludes your profile and pipeline complete the setup.
