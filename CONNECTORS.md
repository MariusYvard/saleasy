# Connectors

## How tool references work

Saleasy refers to tools by category (email, calendar, CRM, lead data, social, spreadsheet, call notes) rather than by a specific product, so it works for anyone who installs it. The `saleasy-setup` profile records the concrete tool you use in each category and the skills then use whatever you connected.

## Categories for this plugin

| Category | Common options |
| --- | --- |
| Email | Gmail, Outlook / Microsoft 365 |
| Calendar | Google Calendar, Microsoft 365 |
| CRM | HubSpot, Close, Salesforce, Pipedrive or an Excel / Sheets pipeline file |
| Lead data | Apollo, Clay, ZoomInfo, official registries |
| Social | LinkedIn |
| Spreadsheet | Excel, Google Sheets |
| Call notes | Fireflies, Gong, manual transcript |

If a category has no connected tool, Saleasy falls back to web search, the spreadsheet or asks you to paste the data. Sending happens only through authorized official APIs after your validation.
