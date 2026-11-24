# EI Cx Leads

Find the companies on the EU-India corridor that show a live buying signal right now. For each one you see what happened, where it was reported, how old it is and how well it is checked. You also see who decides in Europe and in India, and when to reach out. All from chat, on your agent's own web search. Free, no account.

By AIA Stakeholder Intelligence. EI Cx is AIA's decision engine for B2B teams selling between Europe and India.

## Who it is for

B2B revenue teams with deals above €50,000 and buying committees in two regions.

| Direction | Typical seller | Typical buyer |
| --- | --- | --- |
| EU to India | European software and services vendors | European firms setting up or growing capability centres (GCCs) in Pune, Bengaluru, Hyderabad or Chennai |
| India to EU | Indian IT, analytics, engineering and export firms | European banks, OEMs and retailers buying from or partnering with Indian companies |

## What you get

1. **Up to ten ranked accounts a week.** Each comes with the signal behind it, such as a capability centre announced, an Indian entity registered, a new site leader, a tender or CBAM exposure.
2. **Announced is not done.** Every signal shows what happened (announced, in progress, done) and, separately, how well it is checked (reported or confirmed), with a link you can open.
3. **Both sides of the committee.** The roles to reach at the European HQ and in India, named people only when a public source names them, and the works council step for German, Austrian and Dutch accounts.
4. **Timing on both calendars.** An act-by date that allows for India's April to March fiscal year, Diwali, European holidays and works-council lead times.
5. **First messages you send yourself.** Drafts on request, with the German consent rules for email flagged. EI Cx Leads never sends anything.

## Install

**Claude Code:**

```
/plugin marketplace add aswin-bijju/ei-cx-leads
/plugin install ei-cx-leads@aia
```

Or install from a local copy of this repository:

```
claude plugin marketplace add "<path to this folder>"
claude plugin install ei-cx-leads@aia
```

**Claude (claude.ai or desktop):** download [ei-cx-leads.zip](site/ei-cx-leads.zip) and upload it under Skills in Settings. Turn on web search.

**Codex, Cursor and other agents:** copy `skills/ei-cx-leads` into the agent's skills folder.

## Then

Ask "Find me leads in the EU-India corridor". It asks what you sell and which way it goes, fills in a brief from your website, shows it back, and finds your first accounts once you say yes. In Claude Code the brief and each week's list are saved in a `eicx/` folder, so the next run shows what changed.

## What it costs

| | |
| --- | --- |
| EI Cx Leads | Free. No account, no key, no credits |
| AIA Verified Signal Pack | Monthly. Signals AIA has checked against a primary source, delivered as a file the skill reads |
| EI Cx Pilot | Six weeks, done for you. Pay only for the accounts you accept |

Ask AIA for current prices: https://www.linkedin.com/company/aiasintelligence

## Limits

- Public sources only, through your agent's web search. A signal that is not public will not be found.
- No email addresses or phone numbers. Named people only when a public source names them in that role.
- It never sends messages and never logs in anywhere.

## Licence

All rights reserved. You may install and use EI Cx Leads free of charge for your own or your organisation's work. You may not copy, change, redistribute or sell it, or build a competing product from it. See [LICENSE](LICENSE).

## Files

- `LICENSE`: the terms above in full. It is also packed into the zip.
- `skills/ei-cx-leads/SKILL.md`: what your agent reads.
- `skills/ei-cx-leads/references/`: the signal catalogue and the source list.
- `scripts/build_zip.py`: builds `site/ei-cx-leads.zip` for upload to Claude.
- `site/`: the landing page.
