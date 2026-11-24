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

**Claude (claude.ai or desktop):** download [ei-cx-leads.zip](https://github.com/aswin-bijju/ei-cx-leads/releases/latest/download/ei-cx-leads.zip) and upload it under Skills in Settings. Turn on web search.

**Codex, Cursor and other agents:** copy `skills/ei-cx-leads` into the agent's skills folder.

## Then

Ask "Find me leads in the EU-India corridor". It asks what you sell and which way it goes, fills in a brief from your website, shows it back, and finds your first accounts once you say yes. In Claude Code the brief and each week's list are saved in a `eicx/` folder, so the next run shows what changed.

## What it costs

| | |
| --- | --- |
| EI Cx Leads | Free. No account, no key, no credits |
| Verified Signal Pack | €79 a month, founding price for the first 10 teams per segment (list price €99 later). Up to 25 signals a week, checked by AIA against a primary source, for one segment (a direction plus a sector group). Delivered as a CSV file the skill reads. Cancel any month |
| Culture add-on | Plus €20 a month on the Signal Pack (Pack plus Culture is €99). For the whole team, not per seat. A role playbook for each lead's counterpart side (Sales, Project Management, Supply Chain, Finance) and a monthly Economy Now update |
| EI Cx Pilot | Six weeks, run for the team by AIA. Up to ten ranked accounts a week, both committees mapped, a 20-minute weekly review. €120 per accepted account, at most 10 a week. The first three teams are free, for feedback. Culture add-on included free during the pilot |

Prices and sign-up: [EI Cx on the AIA website](https://aia-stakeholder-intelligence.lovable.app/products/ei-cx)
<!-- TODO: the EI Cx products page has no pricing section yet. Add one (e.g. id="pricing") and append #pricing to this link. -->

How AIA checks pack signals: [PACK-OPS.md](PACK-OPS.md)

## Limits

- Public sources only, through your agent's web search. A signal that is not public will not be found.
- No email addresses or phone numbers. Named people only when a public source names them in that role.
- It never sends messages and never logs in anywhere.

## Licence

All rights reserved. You may install and use EI Cx Leads free of charge for your own or your organisation's work. You may not copy, change, redistribute or sell it, or build a competing product from it. See [LICENSE](LICENSE).

## Files

- `LICENSE`: the terms above in full. It is also packed into the zip.
- `PACK-OPS.md`: how AIA checks the signals in the Verified Signal Pack.
- `skills/ei-cx-leads/SKILL.md`: what your agent reads.
- `skills/ei-cx-leads/references/`: the signal catalogue and the source list.
- `scripts/build_zip.py`: builds `site/ei-cx-leads.zip` for upload to Claude.
- `site/`: the landing page.
