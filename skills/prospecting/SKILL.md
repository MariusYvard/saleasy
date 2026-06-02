---
name: prospecting
description: >
  This skill should be used for the top of the funnel: finding and qualifying
  leads, monitoring accounts for buying signals, writing outbound sequences and
  sending approved messages. Trigger on "trouve des leads", "build a lead list",
  "qualifie ces prospects", "ICP", "surveille ces comptes", "mets en place une
  veille", "alerte-moi si", "écris un cold email", "séquence outreach", "prépare
  les relances", "envoie après validation", "send the approved emails", "reach
  out to".
---

# Prospecting

Fill and work the top of the funnel: find the right people, watch for the moment to reach them, write outbound that earns replies and send it after the user validates.

## Clarify first

Read `saleasy-profile.md` and the `saleasy-pipeline` file. If no profile exists, run `saleasy-setup` first. If the user has not said which job they want, ask one short question and offer the choices:

- Find and qualify leads. Source, clean, enrich and score a list. See `references/finding.md`.
- Monitor for signals. Set up or run automated account monitoring on a schedule. See `references/monitoring.md`.
- Write outreach. Draft a message or a J0/J3/J7/J10 sequence. See `references/messaging.md`.
- Send. Send already-approved messages through an authorized tool. See `references/sending.md`.

Many requests chain these (find, then write, then send); run them in order and confirm at each handoff.

## Rules

Never fabricate contact data; mark an unknown email as "(à trouver)" and keep a source link. Personalize on a real, dated signal, never filler. Use only permitted data access and sending: authorized providers and official APIs, never methods that breach a platform's terms or evade anti-bot systems. Honor opt-outs and GDPR. Respect the writing directives: plain, no superlatives, no em dashes, straight quotes. Keep cold emails under about 90 words with one call to action.

## Output

A scored list written to `saleasy-pipeline`, a monitoring digest, ready-to-send drafts or a sent-and-logged batch, depending on the job. End with the concrete next action and the handoff (to `selling` when a reply turns into a meeting).
