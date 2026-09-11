# The outbound engine

*The channel this GTM actually runs on. Load before writing any cold outreach, and every
outreach template points back here. Synthesized from the assets library, the ICP dashboard
and the journey funnel.*

## Thesis

This market cannot be reached by advertising. Independent Medicare agency owners are not
searching for AI voice agents, they are not on software review sites — the three
Medicare-native vendors have zero G2 presence, which tells you the buyers are not there
either — and they are unreachable for eight weeks of the year.

What reaches them is **evidence about their own business, delivered before any ask.**

That is the whole engine. Everything else is delivery mechanics.

## Why the asset-before-ask structure works here

A cold email that asks for a meeting competes with every other vendor email. A cold email
that contains a recording of the prospect's own phone line failing a benefit question
competes with nothing, because nobody else has done the work.

The Gap Report costs us real money per prospect. That cost is the moat: it is why this
motion cannot be copied at scale by someone running volume outbound, and it is why the
reply rate target is 8% rather than the 1–2% a generic sequence produces.

## How the channels feed each other

```
Communities (D1)  ─┐
LinkedIn ads (D2) ─┼─→  D3 Gap Report  ─→  D4 Sandbox  ─→  Decision
Cold outreach (D3)─┘         ▲
                             │
FMO co-marketing ────────────┘  (downline-wide, co-branded)
```

Every channel routes into D3. D3 routes into D4. D4 is where the deal is won, because it
is the first moment the prospect hears a correct answer to their own hard question.

Communities and the webinar build the aggregate dataset that makes cold outreach credible
("what we found auditing 40 agencies"), so they run early even though they convert slowly.

## The archetypes to rotate

Five, so the sequence does not read as one template:

1. **The recording.** Their own line, failing a real benefit question. No commentary.
2. **The number.** Their missed-call volume in 2026 CMS commission dollars.
3. **The benchmark.** Where they sit against the agencies audited so far.
4. **The calendar.** Weeks until AEP, and what has to be true by then.
5. **The peer.** What another agency in their state did about it — once there is one.

Archetype 5 is unusable until there is a design partner. Do not fabricate it.

## Plan / write / edit

**Plan.** Verify the prospect against the ICP-1 definition before spending a Gap Report on
them — 3–10 agents, own inbound number, sells MA. Title-verify for ICP-2. Running the
report on an out-of-profile agency wastes the one thing that makes this work.

Where the pool comes from, and the search metadata that builds it: `job-signal-search.md`.

**Write.** One finding, one sentence of consequence, one question. Under 120 words. The
finding does the persuading; the copy just has to stay out of its way.

**Edit.** Cut every sentence that describes the product. If the email would still make
sense with our company name removed, it is too generic. If it names a capability, check
`feature-status.md` before it ships.

## Hook patterns that work

- The specific failure: *"I called your line on Sunday and asked about the dental
  allowance on [plan]. Here is what happened."*
- The dated number: *"Forty-one calls after hours last month. At the 2026 CMS initial rate
  that is worth [X] if two of them convert."*
- The calendar: *"Nine weeks to AEP."*
- The question they cannot answer: *"Can anyone in your office answer an OTC card question
  without you?"*

## Hook patterns that do not

- Anything beginning "I hope this finds you well", "Quick question", or "I noticed you're
  in the Medicare space".
- Any claim about our product in the first touch.
- Any mention of AI in the subject line. This audience has been pitched AI weekly since
  2023.

## Calls to action

One per message. In order of how well they work here:

1. "Want the rest of it?" — the report is already run, they just have to say yes.
2. "Want me to run this on your line?" — for LinkedIn, where pre-running is not economic.
3. "Worth 15 minutes before AEP?" — only after they have engaged with a finding.

Never "book a demo". The whole positioning attacks the demo gate; opening with one
contradicts it.

## What good looks like

| Measure | Target | Note |
|---|---|---|
| Cold reply rate | ≥ 8% | Against 1–2% for generic sequences. If it is at 2%, the asset is not being pre-run |
| Report → sandbox request | ≥ 25% | If low, the report is not landing on a real pain |
| Sandbox → pricing conversation | ≥ 40% | If low, the plan grounding is not proving out |
| Report delivery time | ≤ 48h | Slower and the wound has closed |

All four are **initial targets to calibrate against first-cohort data**, not benchmarks.
There is no baseline yet. Never present them as results.

## The seasonal rule

Cold outreach runs February to mid-September. During AEP the only thing that goes out is
the Gap Report itself, because it costs the agency nothing and arrives while the problem
is live. Everything else waits for January.
