---
name: ei-cx-leads
description: Find B2B companies on the EU-India corridor that show a live buying signal right now, see the signal behind each one with its source, age and how well it is checked, map who decides in Europe and in India, and get the timing and angle right for both sides. For revenue teams selling from Europe into India or from India into Europe, deals above EUR 50,000. Runs on the agent's own web search, free, no account. Use when the user wants corridor leads, asks which European or Indian companies are ready to buy, wants this week's top accounts, wants a two-region buying committee mapped, wants a refresh of last week's list, or says "Find me leads in the EU-India corridor".
license: Proprietary. All rights reserved; free to install and use, not to copy, change or redistribute. See LICENSE.
metadata:
  author: AIA Stakeholder Intelligence
  version: "0.2.0"
---

# EI Cx Leads

EI Cx Leads finds companies on the EU-India corridor that show a live buying signal for what the user sells. For each one it shows the signal in plain words, with its source, its age and how well it is checked, maps who decides in both regions, and says when and how to reach out.

It is the lead-finding part of EI Cx, AIA Stakeholder Intelligence's decision engine for B2B teams selling between Europe and India, and it follows EI Cx's rules: a short ranked list instead of a dump, every claim traced to a source, and the corridor timing a general tool misses.

It runs on the agent's own web search. No account, no key, no credits. Everything happens in this chat, and nothing is sent to anyone.

Example requests:
- "Find me ten German manufacturers setting up a capability centre in Pune or Bengaluru."
- "Which European banks are growing delivery teams in India this quarter?"
- "We are an Indian analytics firm. Who in the Netherlands is buying analytics services from India right now?"
- "Map the buying committee for Rheinwerk Automation in both regions."
- "Refresh last week's list. What changed?"

## Before you start: can you search?

You need live web search, and web fetch helps. If you have neither, say so in one line and ask the user to turn web search on. Never build leads from memory: a lead without a source you opened in this session is not a lead.

## Step 1: the brief

Look for a confirmed brief first:
- If you can read files (Claude Code, Codex, Cursor and similar): `eicx/brief.md` in the current folder.
- Otherwise (claude.ai, the desktop app): the project knowledge, or earlier in this chat.

If there is none, ask one message and nothing more:

> What do you sell, and which way does it go: from Europe into India, or from India into Europe? Send your website too and I'll fill in the rest.

Fill in the brief yourself from the answer and the website (read the site if you can), then show it back in a few lines:

| Field | Example |
| --- | --- |
| Offer | Cloud cost management for engineering teams |
| Direction | EU to India, or India to EU |
| Buyers | European firms running or opening a capability centre (GCC) in India |
| Industries | Automotive, industrial machinery, banking |
| Size | 1,000+ staff, or revenue above EUR 250m |
| Regions | HQ in DACH or Benelux; India sites in Pune, Bengaluru, Hyderabad, Chennai |
| Deal size | Above EUR 50,000 a year |
| Committee | Economic buyer in Europe (CIO or COO), India site leader, procurement |
| Exclusions | Current customers, open deals, anyone who asked not to be contacted |
| Languages | English; German for first contact in DACH |

Save it only after a clear yes: to `eicx/brief.md` if you can write files (say that you are writing it), otherwise tell the user to keep it in their project. Never search on a brief the user has not confirmed. If the user shares customer or do-not-contact lists, keep them in `eicx/exclusions.csv` and apply them to every run.

## Step 2: find signals

Read `references/signals.md` (the signal catalogue, with search patterns and the maximum age of each signal) and `references/sources.md` (where to look in each region).

1. Pick the four to six signal types in the catalogue that fit the offer and the direction best. Say which ones you picked and why, in one line.
2. Search two to four times per signal type. Search in the local language where the news breaks first: German for DACH press ("Entwicklungszentrum Indien", "Standort Pune"), Dutch or French where relevant, English for Indian press.
3. Collect candidate accounts with: account, HQ country, India location, the signal, the date of the signal, the source link.
4. Aim for about three candidates for every lead you will show. Most candidates should fail the checks in Step 3.

**AIA Verified Signal Pack:** if `eicx/packs/` holds a pack file (CSV from AIA), read it first. AIA has already checked those rows against a primary source. Each pack row carries `segment`, `checked_by`, `checked_on`, `receipt_url` and `does_not_prove`. Always show `does_not_prove` next to the signal, so the user sees what the check does not cover. Still apply the brief, the exclusions and the maximum ages.

## Step 3: check every signal

Keep two things apart and never merge them. This is the rule AIA's register is built on.

- **Status, what happened:** `announced`, `in_progress` or `done`.
- **Verification, how well it is checked:** `reported` (one secondary source, such as one article or a press release) or `confirmed` (two independent sources, or a primary record: a registry entry, a stock-exchange filing, a live job post on the company's own career site, the company's own announcement of something that has happened).

"Announced" is not evidence that anything happened. An MoU is not a contract, and a press release about a capability centre is not a capability centre. Say which one it is.

Drop a signal when:
- you could not open its source, or the source does not say what you claim;
- it is older than the maximum age in the catalogue;
- it is about a different company with a similar name (check the country, domain and sector);
- the account is excluded, is a current customer, or sits outside the brief.

Never invent a signal, a date, a person, an email address, a phone number, a figure or a quote. When unsure, leave it out or mark it `reported`.

## Step 4: rank

One row per account, with at most two signals shown for each account. Score every account that passed Step 3:

| Factor | Weight | 3 | 2 | 1 |
| --- | --- | --- | --- | --- |
| Fit | 30% | Matches industry, size and region | Two of the three | One of the three |
| Signal strength | 30% | Strong in the catalogue | Medium | Weak |
| Freshness | 20% | Under 30 days | 30 to 90 days | Older, within the maximum age |
| Evidence | 20% | `confirmed` | `reported`, reputable outlet | `reported`, weak source |

Score = weighted sum, out of 3. Two signals on the same account within 90 days (for example a capability-centre announcement and a site-leader hire) count as one strong, confirmed signal.

- Show the top ten, or the number the user asks for, up to 25. A short list the team will work beats a long one.
- Below 1.8 is not a lead: put it under "Watch" with the event that would make it one.
- Confidence: **high** (2.5 or more, and confirmed), **medium**, or **low**, with the reason in a few words.

## Step 5: map the committee in both regions

Corridor deals stall when one side of the committee is missing. For each lead, list the roles to reach on each side:

| Side | Roles |
| --- | --- |
| Europe (HQ) | Economic buyer (CIO, COO, CFO or business-unit head), the sponsor of the India programme, procurement, data protection or legal when personal data crosses borders |
| India | Capability-centre or site leader, the head of the function that will use the offer, local finance or procurement |
| Germany, Austria, Netherlands | Works council, when the offer touches how employees are monitored or measured (in Germany, § 87(1) no. 6 BetrVG). Note it as a step in the deal, not a person to contact |

Name a person only when a public source under 12 months old names them in that role: the company site, a press release, an article or their public profile. Link that source. Otherwise write the role and "to find". Never guess email addresses or phone numbers, and never log in to a site to find people.

## Step 6: timing and angle

Give each lead an act-by date and a short timing note. Start from the lead's own situation: a centre's opening date, a hiring wave, a tender deadline, or a new leader's first 90 days. Then adjust for the calendars below. If every lead gets the same date, you have used the calendar alone, so go back to the signals. Check this year's dates instead of assuming them.

- **India:** the fiscal year runs April to March, and budgets are set January to March. Diwali week (October or November) slows decisions.
- **Europe:** summer holidays (July and August; in Germany the dates differ by state) and the Christmas to New Year break slow decisions. Q4 budget freezes are common.
- **Germany:** involving the works council adds weeks. Plan for it early.
- **Money:** when a deal is priced in INR, state the EUR/INR rate used and its date.
- **Data:** personal data moving between the EU and India needs a GDPR transfer tool, such as Standard Contractual Clauses, and India's DPDP Act applies on the Indian side. Mention this when the offer processes personal data.
- **Regulation as a trigger:** CBAM, CSRD, CSDDD, LkSG, EUDR, DORA and the EU-India FTA can create the need. State what a rule requires, and from when, only if a current official source confirms it.

**Angle:** one sentence that links the signal to the offer in the buyer's terms. As a starting point, not a rule: German buyers tend to want specifics, a formal tone and a clear reason to talk now. Indian buyers often respond to a warm path (a mutual contact, a chamber, an alumni network) and a plain business case.

## Step 7: show the leads

In chat, a short ranked list. For each lead:

**1. Account name** (HQ country, India location | score 2.6, high)
- **Signal:** what happened, in plain words. Age. Status and verification. [source](link)
- **Why it fits:** one line against the brief.
- **Committee:** Europe: role or named person. India: role or named person. Works council note if it applies.
- **Act by:** date, and the timing note.
- **Angle:** one sentence.
- **Next step:** one action.

Then a **Watch** list (up to five accounts, each with the event that would make it a lead) and a **Dropped** line with counts and reasons, for example "14 dropped: 6 too old, 4 outside the size range, 3 could not be verified, 1 excluded".

If you can write files, also write `eicx/leads-YYYY-MM-DD.csv` with these columns:
`rank, account, hq_country, india_location, direction, signal, signal_date, status, verification, source_url, second_source_url, fit, score, confidence, committee_europe, committee_india, works_council, act_by, timing_note, angle, next_step`

Then add each lead to `eicx/seen.csv` (`account, first_seen, last_signal_date, last_status`). Tell the user which files you wrote.

**On a refresh:** read `eicx/seen.csv` first. Lead with new accounts and with signals that moved (for example `announced` to `done`, or `reported` to `confirmed`), then say what dropped off and why.

## Outreach (only when asked)

EI Cx Leads never sends anything. When the user asks, draft first messages, one per lead, for them to send from their own account.

- Keep it short: under 90 words for a LinkedIn note, under 120 for an email.
- Open with the signal and its real date, then one line on the offer, then one specific question. No fake familiarity and no claims the user cannot back.
- For German contacts, write in German with the formal "Sie" unless the user already writes to them in English.

Rules to flag when they apply (this is not legal advice; say so when it matters):
- **Germany:** under § 7 UWG, marketing emails need the recipient's prior consent, between businesses too. When the user wants to cold-email German contacts, flag it and suggest a LinkedIn note, a warm introduction or a call instead.
- **EU (GDPR):** keeping named contacts from public sources needs a lawful basis, usually legitimate interest. Article 14 asks you to tell people where their data came from, at the latest at first contact. Offer a one-line notice for the first message.
- **India (DPDP Act 2023):** personal data that people have made public themselves is largely outside the Act. Even so, keep only what the user needs.

## Pricing and help (only when asked)

Don't bring these up on your own. When the user asks about cost, or wants more than self-serve:

- EI Cx Leads is free: no account, no key, no credits.
- **AIA Verified Signal Pack** (paid, monthly): up to 25 corridor signals a week, each checked by AIA against a primary source, for one segment (a direction plus a sector group). Delivered as a CSV file this skill reads from `eicx/packs/`. Cancel any month.
- **Culture add-on** (paid, monthly, on top of the Signal Pack): for the whole team, not per seat. A role playbook for each lead's counterpart side (Sales, Project Management, Supply Chain, Finance) and a monthly Economy Now update.
- **EI Cx Pilot** (done for you): for six weeks AIA runs EI Cx for the team, with up to ten ranked accounts a week, both committees mapped and a short weekly review. The team pays per account it accepts. The Culture add-on is included during the pilot.

State only what is above. Don't quote prices, and don't promise results, reply rates or prices. For prices and sign-up, point to the AIA website: https://aia-stakeholder-intelligence.lovable.app/products/ei-cx

## Rules

- Every step is visible in the chat. No hidden calls and no background work.
- Public sources only. Don't log in anywhere, don't get past paywalls, and don't buy data.
- A lead needs a source link the user can open. Never present an example or demo as a real result.
- Respect the exclusions and anyone who asked not to be contacted.
- The brief, lists and leads stay in the user's folder or chat. Send nothing anywhere.
- If a search fails or a source is blocked, say so in plain words and carry on with the rest.
