# Finding and qualifying leads

The source, clean, enrich and score pipeline, plus advanced scoring and list hygiene. Run the stages in order; each hands a clean artifact to the next.

## Define
A usable definition has four parts: industry, company size band, geography, target titles. If any is missing, fill from the profile ICP and confirm before searching at scale. Add intent filters when the user has them (hiring for X, recently funded, uses Y tool).

## Find (compliant discovery)
Priority of sources: connected lead-data provider (Apollo, Clay, ZoomInfo and similar authorized providers), then official registries (for example Companies House), then company sites and public web research, then web search. Capture at minimum: company, full name, title, one public source URL. Use only permitted access: official APIs and authorized providers. Do not scrape a platform in breach of its terms, do not bypass a login or rate limit and do not drive a browser to evade anti-bot or detection systems. If data is only reachable by those means, leave the field "(à trouver)" and move on.

## Data protection
The user is likely under GDPR and ePrivacy. Collect only the fields needed for outreach, record the source and date, keep a basis for contact (for B2B, legitimate interest plus a clear opt-out) and honor any prior opt-out. Never store special-category personal data. When unsure whether a contact may be approached, ask.

## Clean
Deduplicate on email then on name plus company. Normalize company suffixes, domain casing and title variants. Drop rows missing must-have fields and keep a count. Flag, do not silently delete, rows with conflicting data.

## Enrich
Add where findable and mark verified versus inferred: professional email (pattern-guess is inferred, source-confirmed is verified), LinkedIn URL and a dated tension signal. For priority leads add a short person dossier (career history, public presence, decisions they influence, communication style). Never present an inferred email as verified.

## Tension-signal taxonomy
A signal is a recent, public, dated event that gives a real reason to reach out now. Capture type, a one-line label, a source quote and the date. Weight by freshness: full weight under 30 days, half from 30 to 90, older is background not a trigger. Types: restructuring; layoffs or hiring freeze; hiring surge or a role tied to the pain; leadership change in the buyer function; funding, acquisition or merger; product launch or expansion; public pain (reviews, regulation, a churned tool). Also capture champion potential (public advocate, prior user, owns a KPI tied to the pain) and switching-cost or competitive vulnerability. Record the strongest one or two, not a list of weak ones.

## Score with knockout gates
Split criteria into two classes. Required characteristics are binary pass or fail (minimum size, target industry, geography, a must-have technology); a lead that fails any is disqualified outright, with the reason recorded so it is not re-sourced. Survivors get a weighted score on fit, intent and reachability, placed in named tiers with a one-line rationale: hot (strong fit, fresh signal, reachable), warm (good fit, weak or no signal), nurture (partial fit, watch for a trigger). Calibrate by company type (SMB owner-led short cycle; enterprise committee and procurement long cycle).

## List-quality scorecard
Before any outreach, grade the list and gate it (ship, fix, rebuild): catch-all density, duplicate-domain concentration (cap leads per company), bad-title patterns (intern, assistant, student where not relevant), title relevance, verification coverage, name and field quality.

## Sourcing methods
Lookalike by seed domain: start from 3 to 10 known-good customer domains, exclude your own and existing customers, qualify a small sample before scaling. Competitor engagers: people interacting publicly with a competitor are intent, but run a mandatory ICP filter. Sweet spot: prospects with clear pain and willingness to pay convert better than perfect-on-paper but content accounts.

## Deep dive on one account
When the user wants one target studied in depth, score five axes and combine into a 0 to 100 grade with a confidence level: company fit, contact access, opportunity quality, competitive position, outreach readiness. If an axis cannot be assessed, mark it neutral and lower confidence rather than guessing.

## Sanity baseline
A positive reply rate under 1 percent after 200-plus sends means the list or setup is broken; fix that before testing copy.

## Output
Write to `saleasy-pipeline.md` (or `.csv` via a connected spreadsheet) with columns: company, contact, title, email, LinkedIn, signal, tier, reason, source, status, next_contact, owner. New leads get status `new`. Append and deduplicate if the file exists. When a CRM is connected it is the source of truth and the file is a mirror.
