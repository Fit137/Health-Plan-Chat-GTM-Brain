# Template — personalised cold outreach, ICP-1

Campaign A1. The highest-conversion motion in the library. Method:
`reference/outbound-engine.md`.

**Two forms of D3, and they run differently.** The main sequence below is the pre-run audit:
twenty questions put to the agency's line before the first touch, and if it has not been run,
this is not that sequence. The offered form, where the deliverable is a 2027 Plan Change
Report built from the plans they tell us they sell, is the variant further down and is what runs
cold at scale. Both are defined in `reference/plan-change-report.md`.

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
and the change report offered cold and built on reply. This is what runs at scale, and it
carries no phone call, so nothing is spent on a prospect who does not answer.

**What carries the message.** The September 30 letter deadline and the wave of calls behind
it. Both are fixed CMS facts about the reader's own October, and neither needs a single field
of enrichment to be true.

### Touch 1 — the deliverable

**Subject:** what changed on your plans for 2027

```
Your members get their Annual Notice of Change letters by September 30.
The calls start the week after, and they are all the same call: what does
this mean for me.

Tell me which plans [Agency] sells and I'll read the 2027 Summary of
Benefits against the 2026 version for each one. Every change, premium,
copays, dental, the OTC card, network, with the page it came from. AI does
the reading and I check it against the source.

No charge, and you'll have it the week the documents land. Which plans
should I run?

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

260 characters against the longest agency name in the table. Check it against that name, not
the average one, because this variant is close to the cap.

```
Hi [First name], there's a way to use AI on your inbound before October 15
that answers what a caller's plan covers, not just picks up. I think it
puts [Agency] well ahead of where it would otherwise land. Can I send you
how?
```

### Alternate, contrast first

269 characters. Leads on the distinction rather than arriving at it.

```
Hi [First name], most AI answers the phone. There's a way to use AI that
answers what the caller's plan actually covers, and having it in before
October 15 puts [Agency] well ahead of where it would otherwise land.
Can I send you how?
```

### The eight words carrying the positioning

"Answers what a caller's plan covers, not just picks up" is the whole competitive argument in
plain English, and it is the clause that has to survive any edit.

Without it the message offers AI on the inbound, which is what a $79 receptionist offers.
`reference/feature-matrix.md` is unambiguous that anything a commodity assistant also does is
not a story we can win on, and all six differentiators are Medicare plan IP. The contrast is
not decoration on the value proposition, it **is** the value proposition, compressed.

It also states our side of the distinction in `rules/glossary.md` that must never blur. We
answer the beneficiary. Lead capture and agent-facing tools answer somebody else. A reader who
takes "AI on your inbound" to mean call answering has put us in the wrong category before
replying, and the clause is what prevents that.

What it does not do is name a product, claim a customer, or promise a number, which is what
keeps it sendable.

### The claim line this variant walks

"Outlier results" as a promise is an outcome claim, and `ops/QA-checklist.md` requires every
outcome number to be labelled as modelled and bars anything implying customers. There are
none, so no version of this may say we have produced that result for anyone.

What survives is the possibility and the method. **"I think it could be" is an opinion offered
and "here is how" is a method sent**, and neither asserts a result we have delivered. Watch
three drifts in any rewrite: "we help agencies" implies a book of them, "our clients see"
invents one, and a number attached to the upside needs a unit, a date and the word modelled.

The offer is also what to send. "How" is a written method for handling the inbound surge, not
a call and not a demo. If it does not exist yet, it has to before this goes out, because the
reply to this message asks for it immediately.

### Where the deliverable goes

Not in the request. Whatever they answer, the reply offers the 2027 change report, and only
then does the plan list get asked for. Three steps, each one smaller than the last thing they
agreed to.

### Why it is built this way

**It tells them something they do not know.** No owner knows in September exactly what moved
on every plan in their book for next year, because the documents are only now publishing.
That is what separates this from an audit score or a cheat sheet, both of which told the
owner something they already believed.

**The request asks a question rather than offering anything.** An offer in a connection note
reads as a vendor whatever it contains. A question about the reader's own October reads as a
peer, and it is answerable in a few words with nothing to look up.

**The question does the revealing.** Naming what the calls actually are, one question about
plan coverage, is the whole diagnosis. The owner supplies the rest themselves, because they
already know how that fortnight goes.

**"Staffing, or AI" is the point and it is not a pitch.** It presents two real options and
asks which way they lean. `reference/outbound-engine.md` warns that this audience has been
pitched AI weekly since 2023, and that warning is about being told. Being asked survives it,
because the reader gets to hold the opinion.

**Nothing to look up.** Acceptance and reply are separate decisions on this channel and the
request has to survive both, so the answer has to be available without the reader leaving the
message.

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
