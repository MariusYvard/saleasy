# Saleasy

A single commercial cockpit in four skills, organized around the real life of a deal: set up once, then attract, prospect and sell. Instead of juggling separate plugins for LinkedIn, SEO, lead generation, marketing and sales, Saleasy keeps the surface small and asks what you need when you invoke it.

Saleasy is profile driven. The first time you use it, `saleasy-setup` runs a short interview and saves a profile (market, offer, target persona, tone, connected tools). Every other skill reads that profile so the output is already adapted to your situation. Because the profile is generated per user, the same repository works for anyone who clones it.

## Components

Four skills. Each one asks a short question on invocation when the job is not already clear, then loads the matching playbook from its `references/` folder.

| Skill | Trigger examples | What it does |
| --- | --- | --- |
| `saleasy-setup` | "configure saleasy", "initialise saleasy" | Interviews you and writes the shared profile. Run once, rerun anytime. |
| `marketing` | "écris un post LinkedIn", "plan de contenu", "campagne", "audit SEO" | Content and visibility: LinkedIn, editorial calendar, campaigns, long-form, SEO, repurposing, lead magnets, positioning. |
| `prospecting` | "trouve des leads", "mets en place une veille", "écris un cold email", "envoie après validation" | Top of funnel: find and qualify leads, monitor signals, write sequences, send after you validate. |
| `selling` | "prépare mon RDV", "revue de pipeline", "forecast", "négociation", "renewal", "brief du matin" | First meeting to signature and beyond: prep and summaries, pipeline, forecast, closing, negotiation, proposals, account growth, daily brief and weekly review. |

## Install

This repository is a Claude plugin marketplace. Add it, then install the plugin:

```
/plugin marketplace add MariusYvard/saleasy
/plugin install saleasy@saleasy
```

This repository is published at `MariusYvard/saleasy`.

## Setup

No environment variables are required. Saleasy works standalone with web search and gets stronger when you connect tools: email, calendar, CRM, lead data, social, spreadsheet. See `CONNECTORS.md`. On first run, ask Saleasy to "configure saleasy". It creates `saleasy-profile.md` in your working folder, which you can edit by hand anytime.

## Working files

Saleasy keeps two per-user files in your working folder, both git-ignored so personal data never lands in the repo:

- `saleasy-profile.md`: your market, offer, persona, tone and tools. Read by every skill.
- `saleasy-pipeline.md` (or `.csv`): the lead and deal tracker created by `prospecting` and updated by `selling`. When a CRM is connected, the CRM is the source of truth and this file is a mirror.

## How to use it

Describe the moment and the right skill loads, then asks what you want if needed. Set up once, ask `selling` for a morning brief to start the day, use `prospecting` to fill and work the funnel, `marketing` to stay visible and `selling` around meetings, at close and for renewals.

## Sending and automation

Saleasy follows a draft, validate, send model. Claude drafts, you approve a batch and Claude sends the approved items through your connected authorized tool (email via the official Gmail or Microsoft 365 API), then logs the result to your pipeline. Nothing is sent without your explicit yes. With monitoring and a scheduled task, Saleasy can watch accounts and prepare due follow-ups on its own, but the approval gate still applies.

Saleasy stays within platform terms: it does not automate LinkedIn connection requests or DMs through unofficial automation and does not bypass anti-bot, rate-limit or detection systems. For channels with no compliant programmatic send, it gives you a ready-to-send draft. Contact data comes from authorized providers and public sources, handled in line with GDPR.

## Customization

Saleasy refers to tools by category so it adapts to whatever you connect. See `CONNECTORS.md`. The `saleasy-setup` profile records your real tools.
