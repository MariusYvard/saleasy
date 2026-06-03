# Connectors

## How tool references work

Saleasy refers to tools by category (email, calendar, CRM, lead data, social, spreadsheet, call notes) rather than by a specific product, so it works for anyone who installs it. The `saleasy-setup` profile records the concrete tool you use in each category and the skills then use whatever you connected.

## Categories for this plugin

| Category | Common options |
| --- | --- |
| Email | Gmail, Outlook / Microsoft 365 |
| Calendar | Google Calendar, Microsoft 365 |
| CRM | HubSpot, Close, Salesforce, Pipedrive or an Excel / Sheets pipeline file |
| Lead data | Apollo, Clay, ZoomInfo, official registries (Companies House, French open data) |
| Social | LinkedIn |
| Spreadsheet | Excel, Google Sheets |
| Call notes | Fireflies, Gong, manual transcript |

If a category has no connected tool, Saleasy falls back to web search, the spreadsheet or asks you to paste the data. Sending happens only through authorized official APIs after your validation.

## CRM as a Google Sheet
A common setup is a CRM kept in a Google Sheet. The Drive connector is read-only, so Saleasy cannot write back through it. Prefer a Google Sheets API connector when one is available: it writes safely keyed on a unique column. Without a write API, Saleasy drives the Sheet by hand and follows the safe write routine in `prospecting/references/sending.md` (back up first, key every row by email, navigate by the Name box, never Ctrl+A in the find box, one cell at a time). Record the Sheet URL and the column mapping in the profile so writes target the right cells.

## France open data
For a French market, Saleasy can use official open data at no cost. The API Recherche d'entreprises and the INSEE Sirene API give firmographics (SIREN, NAF, workforce band, officers) for finding and qualification. The BODACC API gives dated company events used as buying signals for monitoring. API Entreprise is not usable here because it is reserved for public administrations under habilitation.
