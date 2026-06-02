# Automated signal monitoring

The recurring counterpart to one-off research. Watch the accounts that matter and catch a buying signal while it is fresh.

## Set up the watch
Confirm a watchlist with the user: which accounts or segments to follow, which signal types to catch (see the taxonomy in `finding.md`) and how often to check (daily or weekly). Offer to create a scheduled task so the monitor runs on its own; the schedule prompt should re-run this skill in monitor mode.

## Run a pass
For each watched account, check legitimate sources only: web search, official company and registry pages, news, official APIs and connected providers. Capture each signal with a type, a one-line label, a source link and a date. Apply the freshness weighting. Do not breach a platform's terms and do not evade anti-bot or detection systems; if a source is not reachable by permitted means, skip it and note the gap.

## Act on a signal
Write new signals into `saleasy-pipeline` (or the CRM): update the account signal, raise its intent tier when warranted, set a suggested action and date. For a high-intent signal on a hot account, flag it for the next briefing and offer to draft outreach. Deduplicate against signals already recorded.

## Rules
Only record signals with a real source and date; never invent activity. Keep monitoring proportionate and respect the robots files and terms of the sources. Promote a signal to an alert only when it crosses the intent and freshness bar; a monitor that cries wolf is worse than none.

## Output
A short digest per run: new signals by account, the few worth acting on now and the suggested next action for each. On a schedule, push only what changed.
