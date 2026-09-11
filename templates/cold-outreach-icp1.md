# Template — personalised cold outreach, ICP-1

Campaign A1. The highest-conversion motion in the library. Method:
`reference/outbound-engine.md`.

**Two forms of D3, and they run differently.** The main sequence below is the pre-run audit:
twenty questions put to the agency's line before the first touch, and if it has not been run,
this is not that sequence. The offered form, where the deliverable is a Plan Answer Sheet
built from the plans they tell us they sell, is the variant further down and is what runs
cold at scale. Both are defined in `reference/plan-answer-sheet.md`.

**Qualify first.** 3–10 licensed agents, own inbound number, sells Medicare Advantage,
and reachable — February to mid-September only.

---

## Touch 1 — the finding

**Subject:** [the specific thing that happened, no product words, no "AI"]

```
[One sentence: what you did and what happened. Name the plan and the question.]

[One sentence: what that means in their terms. A number if you have one,
with its unit and its date.]

[One question. Not a meeting request.]

[First name]
```

Under 120 words. No attachment. No calendar link. No description of the product.

**Worked shape:**
> I called your main line on Sunday evening and asked what the dental allowance is on the
> [Plan Name]. The call went to voicemail.
>
> I ran the same question at four other agencies in [County]. Three of the five could not
> answer it outside office hours.
>
> Want to see what your line does with the other nineteen questions I tried?

## Touch 2 — the rest of it, 4 days later

Deliver the full audit. No ask attached. One line: *"The whole thing, no strings. The
section on after-hours is the one I'd read first."*

## Touch 3 — the consequence, 5 days later

The number in 2026 CMS commission dollars, dated and labelled as modelled. One question:
whether they want the same thing run against their own plan documents in a sandbox.

## Touch 4 — the calendar, 7 days later

Weeks remaining until 15 October, and what would have to be true by then. Close the loop
politely if no reply.

---

## Variant — offered rather than pre-run

**When this applies.** Email or LinkedIn, no enrichment on the row beyond the agency name,
and the Plan Answer Sheet offered cold and built on reply. This is what runs at scale, and it
carries no phone call, so nothing is spent on a prospect who does not answer.

**What carries the message.** The question list and the calendar. Twenty named questions let
the owner diagnose their own front desk in seconds, and 15 October is the fixed CMS date they
organise the year around. Neither needs enrichment to be true.

### Touch 1 — the deliverable

**Subject:** the 20 questions, answered

```
Between October 15 and December 7 your callers will ask the same twenty
questions about their plans. The dental allowance, the OTC card, the
specialist copay, what the out-of-pocket maximum actually covers.

Tell me which plans [Agency] sells and I'll send back a one-page answer
sheet for each. Twenty questions, the answer to each, and the page of the
carrier document it came from. Yours to print and keep by the phone.

No charge. Which plans should I run it on?

[First name]
```

### Merge fields and the one computed value

Two merge fields, both already on the contact record: `[Agency]` and `[First name]`.

`[N]` is computed, not typed. Weeks between send date and 15 October, rounded to the
nearest whole week. Hardcoding it puts a wrong number in the first line of every email sent
after the first day, and a wrong date to this reader is the error only an outsider makes.
Below two weeks, switch to days.

### What changes downstream

Touch 2 in the main sequence delivers the report. In this variant the report is delivered
on the reply, so touch 2 becomes a second calendar touch that only fires where there was no
reply. Touches 3 and 4 are unchanged.

The reply is also where appointment setting belongs. `reference/outbound-engine.md` ranks
"worth 15 minutes before AEP" third and permits it only once the prospect has engaged with a
finding, and a reply asking for the audit is that engagement. It stays out of touch 1.

### The claim to watch in this variant

"I'll run" and "I'll put" are commitments, in the future tense, about work not yet done.
That is accurate and it must stay that way. Any drift into "I run these for agencies" or
"agencies I've audited" is a customer reference, and there are none.

---

## Variant — LinkedIn connection request, ICP-1 owner

**Track note.** `reference/marketing-campaigns.md` routes ICP-1 owners found on LinkedIn into
A1 rather than into B1, because B1 carries ICP-2 content. This is A1 content on the LinkedIn
channel, which is allowed, and the rule that has to hold is the content one: no procurement,
no security review, no downline language, ever, in this variant.

**The hard limit is 300 characters, not words.** That is the LinkedIn connection note cap and
it counts the merged agency name. Check the longest name in the table against it, not the
average one: at 252 characters the message below still fits the longest name in a 997-row
list with room to spare, and a message near 290 will truncate on the rows that matter.

### The request

233 characters as written, 233 with or without a merge field. No agency name is needed,
because the offer is specific without it.

```
Between October 15 and December 7 your callers will ask the same 20
questions about their plans. Tell me which plans you sell and I'll send
back a one-page answer sheet for each, taken from the carrier documents.
No charge. Want one?
```

### Shorter alternate

216 characters. Leads on the deliverable rather than the calendar.

```
Tell me which Medicare plans you sell and I'll send back a one-page answer
sheet for each: the 20 questions your callers ask most, answered from the
carrier documents, with sources. Free, before October 15. Want one?
```

### Why it is built this way

**The question list does the diagnosis.** An owner reads "the dental allowance, the OTC card,
the specialist copay" and knows within seconds which of them their front desk cannot answer
today. They diagnose themselves, privately, which lands harder than a stranger's verdict and
costs them nothing in pride.

**The ask is the conversion.** We need their plan list to build the sheet, so the reply the
deliverable requires is the reply we want. There is no second conversion step and no meeting
request anywhere in the first touch.

**There is no company name and no capability.** Strip the sender and the note still makes
sense, which is the test in `ops/QA-checklist.md`. A connection note that describes a product
reads as a vendor and is declined before it is read.

**"No pitch" does not appear.** Saying it is what pitching sounds like to this reader. Not
pitching is the version that works.

### On acceptance

A connection note carrying the whole offer means the reply can come before the connection is
accepted, and nothing is lost when it does not. Where the request is accepted with no reply,
the first message after acceptance is touch 1 of the email sequence, unchanged. Do not open
that message by thanking them for connecting.

---

## Guardrails

- **Every capability mention** is checked against `rules/feature-status.md` before send.
  Do not say it books appointments. Do not say it captures SOA.
- **No price**, in any touch, until the price is published (OF-1).
- **No customer references, counts or testimonials.** There are none.
- **No claim of uniqueness** without `rules/do-not-say.md` open.
- **Banned words** per `rules/writing-rules.md`. No exclamation marks. No em-dash tic.
- **Numbers carry unit and date.** "$694, the 2026 CMS initial rate."
- Run `ops/QA-checklist.md` before the first send of any new sequence.
