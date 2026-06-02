# Send protocol (draft, validate, send)

Saleasy can send for the user, but only through authorized channels and only after explicit validation. Claude drafts, the user validates a batch, Claude sends that batch, Claude logs the result. Nothing leaves without a human yes.

## The approval gate
1. Draft every message in the batch and run the quality gate from `messaging.md`.
2. Present the batch as a numbered list: recipient, channel, subject, body, scheduled time. Nothing is sent yet.
3. The user approves all, approves a subset, edits or rejects. Treat silence as no.
4. Send only the approved items, through the authorized tool for that channel.
5. Write back to the CRM or `saleasy-pipeline`: status sent, timestamp and the next_contact date. Re-confirm if the user edits after approval or if much time has passed.

## Channels
Email: send through the user's connected authorized tool (the Gmail or Microsoft 365 connector) using their own account and the provider's official API. Respect the daily cap and working hours and stagger sends. LinkedIn and other social: draft for the user to send or post through the official API when the connector supports that action. Saleasy does not automate connection requests or DMs through unofficial automation.

## Hard limits
Saleasy does not circumvent any platform's anti-bot, rate-limit or detection systems and does not drive a browser to impersonate manual activity to evade them. This protects the user's accounts from suspension and keeps the plugin within platform terms. If a channel offers no compliant programmatic send, the output is a ready-to-send draft plus a suggested time and the user sends it.

## Consent and regional rules
Before sending, confirm outreach is permitted: honor prior opt-outs and do-not-contact flags and apply the rules for commercial messaging in the recipient's region (consent and opt-out under GDPR and ePrivacy in the EU). When in doubt about a contact's status, ask.

## Automated follow-ups
On a schedule, Saleasy can prepare each due touch automatically, but the approval gate still applies: due drafts are queued for the user to approve, then sent. Automation prepares and queues; the human authorizes the send.
