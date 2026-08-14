# Send protocol (draft, validate, send)

Saleasy can send for the user, but only through authorized channels and only after explicit validation. Claude drafts, the user validates a batch, Claude sends that batch, Claude logs the result. Nothing leaves without a human yes.

## The approval gate
1. Draft every message in the batch and run the quality gate from `messaging.md`. Embed the HTML signature in each email body (see `messaging.md`).
2. Present the batch as a numbered list: recipient, channel, subject, body, scheduled time. Nothing is sent yet.
3. The user approves all, approves a subset, edits or rejects. Treat silence as no.
4. Send only the approved items, through the authorized tool for that channel.
5. Log the result to the CRM right away (see "Pipeline traceability" below). Re-confirm if the user edits after approval or if much time has passed.

## Gmail draft limits (freeze before you create)
The Gmail connector can create a draft but cannot edit or delete one. A regenerated draft becomes a second draft the user has to clean up by hand. So:
1. Freeze the content first. Finish the quality gate and the user edits before any draft is created. The text that goes into the draft is final.
2. Check for an existing draft to the same recipient (search drafts by recipient or subject) before creating a new one. If one exists, do not create a duplicate; tell the user and let them delete or keep it.
3. Create each approved draft exactly once. Never regenerate to "improve" a draft already created. If a correction is unavoidable, ask the user to delete the old draft first, then create the new one.
4. Create drafts one batch at a time and report which were created, so a failure does not leave half a batch behind.

## Channels
Email: send through the user's connected authorized tool (the Gmail or Microsoft 365 connector) using their own account and the provider's official API. Respect the daily cap and working hours and stagger sends. LinkedIn and other social: draft for the user to send or post through the official API when the connector supports that action. Saleasy does not automate connection requests or DMs through unofficial automation.

## Hard limits
Saleasy does not circumvent any platform's anti-bot, rate-limit or detection systems and does not drive a browser to impersonate manual activity to evade them. This protects the user's accounts from suspension and keeps the plugin within platform terms. If a channel offers no compliant programmatic send, the output is a ready-to-send draft plus a suggested time and the user sends it.

## Consent and regional rules
Before sending, confirm outreach is permitted: honor prior opt-outs and do-not-contact flags and apply the rules for commercial messaging in the recipient's region (consent and opt-out under GDPR and ePrivacy in the EU). When in doubt about a contact's status, ask.

## Cadence and scheduling (standard, not optional)
Generate the whole cadence up front, not one message at a time. For a first touch, draft J0, J3, J7 and J10 together (see `messaging.md`), present them as one batch and create the J0 draft after approval. Hold J3, J7 and J10 as ready text. Then propose a scheduled reminder for the first due follow-up (a scheduled task or a calendar entry on the next_contact date) so the relance is not forgotten. Make this the default flow: full cadence, then a scheduled nudge. Only skip it if the user declines.

## Pipeline traceability (standard step after every send)
Updating the CRM after a send is a step of the protocol, not a separate task the user has to ask for. Right after the approved batch goes out (or the J0 drafts are created), write back for each contact, keyed on the email: stage, last-contact date, next-contact date, owner and channel. Use the safe routine below. If a CRM is connected by API, write through it; if the CRM is a spreadsheet, follow "CRM write safety". When no CRM is reachable, update `saleasy-pipeline` and tell the user the CRM still needs the entry.

## CRM write safety (Google Sheets)
A CRM is often a Google Sheet whose Drive connector is read-only, so writing means driving the Sheet. Writing into a live Sheet is destructive if done loosely. Follow this routine every time:
1. Prefer an API. If a Google Sheets API connector (or any CRM API) is connected, use it instead of the browser. Only drive the Sheet by hand when no write API exists.
2. Back up first. Before any write, duplicate the sheet or export a copy (File then Make a copy; or download a snapshot). No backup, no write.
3. Key every row by email. The email is the unique key. Find the row whose email matches before writing; never write by position or by visual guess. If the email is absent, append a new row at the bottom rather than overwriting an existing one.
4. Navigate by the Name box. Go to a specific cell with the Name box (the cell-reference field), for example type `D2` to land on the column you mean. Do not scroll-and-click into a cell.
5. Never Ctrl+A inside the search or find box. A select-all there can replace the live selection and overwrite cells. Use Find (Ctrl+F) to locate, read the row, close Find, then navigate by the Name box. Editing three cells by accident is exactly the failure this prevents.
6. Write one cell at a time and confirm. Enter the value, press Enter, verify the cell holds what you intended before moving on. Write only the columns that changed (stage, last-contact, next-contact, owner, channel).
7. Stop on any doubt. If the row key is ambiguous or the layout does not match the column mapping in the profile, stop and ask rather than write.

## Automated follow-ups
On a schedule, Saleasy can prepare each due touch automatically, but the approval gate still applies: due drafts are queued for the user to approve, then sent. Automation prepares and queues; the human authorizes the send.
