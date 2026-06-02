---
name: saleasy-setup
description: >
  This skill should be used to initialize or reconfigure Saleasy. Trigger when
  the user says "configure saleasy", "initialise saleasy", "setup saleasy",
  "set up my commercial profile", "change my saleasy profile" or the first
  time any other Saleasy skill runs and no profile file exists. Interviews the
  user about their market, offer, target persona, tone and connected tools,
  then writes a shared profile file that every other Saleasy skill reads.
---

# Saleasy setup

Initialize Saleasy for this user by producing a single profile file. Every other Saleasy skill (marketing, prospecting, selling) loads this file first, so the quality of the whole plugin depends on it. Keep the conversation in plain language and in the user's language (French or English). Do not expose file paths or schema details unless asked.

## When to run

Run when the user explicitly asks to configure Saleasy OR automatically (with a one-line heads-up) when another Saleasy skill cannot find a profile. Never silently skip setup and guess a full profile.

## Profile location

The profile lives at `saleasy-profile.md` in the working folder (the connected Cowork folder or the outputs folder if none is connected). Before interviewing, check whether it already exists:

1. If it exists and the user asked for a fresh setup, read it, show a short summary and ask what to change rather than starting from zero.
2. If it does not exist, run the full interview.

## The interview

Detect the user's profile type first, because it changes which questions matter: founder or solo, SDR or BDR, Account Executive, full-cycle sales, marketer, agency or freelance. Pick the closest; the user can refine.

Collect, in as few exchanges as possible (group related questions, prefer 2 to 3 turns):

1. Identity and role. Name, role, profile type, company.
2. Offer. What they sell, in one or two sentences. Price band if relevant.
3. Target. Ideal customer profile (industry, size, geography) and buyer persona (titles, what they care about, pains).
4. Differentiation. One or two reasons prospects choose them. Main competitors if known.
5. Motion. Inbound, outbound or both. Sales cycle length. Weekly targets if any.
6. Voice. Tone for outbound and content, language(s), things to never say.
7. Tools and sending. Which tools cover email, calendar, CRM, lead data, social, spreadsheet, call notes. Which channels the user authorizes Saleasy to send through after validation. Whether to enable automated signal monitoring on a schedule. For a France market, offer the open-data pack: the API Recherche d'entreprises and the BODACC API need no key, the INSEE Sirene API needs a free token the user can paste later.
8. Proof. Reusable assets: case studies, metrics, testimonials, signature, booking link.

If the user says "whatever you think is best", propose concrete defaults for the profile type and confirm in one message. Do not stall.

## Writing the profile

Write `saleasy-profile.md` using `references/profile-template.md`. Fill every section; for anything unknown write `(à compléter)` rather than inventing facts. After writing, show a compact summary and tell the user they can edit the file directly or rerun setup anytime.

## Style

Respect the writing directives: factual and neutral, no marketing adjectives, no em dashes, straight quotes, no Oxford comma. The profile is reference data, so favor short labelled lines over paragraphs.

## After setup

Suggest the natural next step by profile type: a marketer to `marketing`, an SDR to `prospecting`, an AE to `selling`. Anyone can ask `selling` for a morning brief. Offer to schedule the brief if they want it recurring and to set up automated monitoring (in `prospecting`) if they opted in.
