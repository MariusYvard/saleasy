---
name: selling
description: >
  This skill should be used from first meeting to signature and beyond:
  preparing and summarizing calls, reviewing the pipeline, forecasting, closing,
  negotiating, drafting proposals, growing existing accounts (expansion,
  renewal, referrals) and the daily briefing and weekly review. Trigger on
  "prépare mon RDV", "compte-rendu d'appel", "revue de pipeline", "forecast",
  "négociation", "proposition commerciale", "trouve des upsells", "risque de
  churn", "demande de recommandation", "brief du matin", "bilan de la semaine",
  "prep my call", "pipeline review", "close this deal", "renewal".
---

# Selling

Everything from the first meeting to signature and the customer life after it, plus the daily pilotage that ties it together.

## Clarify first

Read `saleasy-profile.md`. Pull deal and account data from the CRM when connected, otherwise from `saleasy-pipeline`; pull meeting context from the calendar and call-notes tools. If no profile exists, run `saleasy-setup` first. If the user has not said which job they want, ask one short question and offer the choices:

- Prepare or summarize a meeting. Call prep or turn notes into actions and a follow-up. See `references/deals.md` and `references/methodologies.md`.
- Review pipeline or forecast. Rank deals, surface risk, build a weighted forecast. See `references/deals.md`.
- Close or negotiate. Readiness check, closing technique, objection handling, concession ladder, stakeholder map. See `references/closing-negotiation.md`.
- Draft a proposal. Good, Better, Best with an ROI case. See `references/proposals.md`.
- Grow an account. Expansion, renewal risk, referrals. See `references/growth.md`.
- Daily brief or weekly review. See `references/cockpit.md`.

Pick the qualification or discovery framework that fits the deal from `references/methodologies.md` rather than applying all of them.

## Outbound writing routes to prospecting

Any cold or outbound message (a prospecting email, a follow-up, a re-engagement sequence, a J0/J3/J7/J10 cadence) is written by `prospecting`, not here, so it always passes the quality gate, the cadence and the send protocol. If a selling task needs outbound drafting, hand off to `prospecting`. Keep in `selling` only deal documents and replies inside an active thread (proposals, meeting recaps, follow-ups to a contact you already met).

## Rules

Be honest about deal health; surface risk rather than smoothing it. Every meeting output ends in a concrete next step with an owner and a date. Never fabricate CRM data, attendee facts or numbers; research or mark unknown. For account growth, never confuse activation with expansion and do not upsell an unhappy account, save it first. Respect the writing directives: factual, no superlatives, no em dashes, straight quotes.

## Output

A tight one-pager for prep and summaries, a table plus a prioritized action list for pipeline and forecast, a scannable briefing for pilotage. Always close with the single most important next action. Offer to write changes back to the CRM only with confirmation. When the CRM is a Google Sheet, follow the safe write routine in `../prospecting/references/sending.md` (back up first, key every row by email, navigate by the Name box, never Ctrl+A in the find box).
