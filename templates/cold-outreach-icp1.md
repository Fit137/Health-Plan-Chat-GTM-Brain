# Template — personalised cold outreach, ICP-1

Campaign A1. The highest-conversion motion in the library. Method:
`reference/outbound-engine.md`.

**Precondition, non-negotiable.** The Gap Report is run *before* the first touch. If it
has not been run, this is not campaign A1 and this template does not apply.

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

Deliver the full Gap Report. No ask attached. One line: *"The whole thing, no strings.
The section on after-hours is the one I'd read first."*

## Touch 3 — the consequence, 5 days later

The number in 2026 CMS commission dollars, dated and labelled as modelled. One question:
whether they want the same thing run against their own plan documents in a sandbox.

## Touch 4 — the calendar, 7 days later

Weeks remaining until 15 October, and what would have to be true by then. Close the loop
politely if no reply.

---

## Variant — offered rather than pre-run

**When this applies.** Email-only motion, no enrichment on the row beyond the agency name,
and the Gap Report offered cold and run on reply rather than before the first touch. This is
the form `reference/marketing-campaigns.md` allows where pre-running is not economic. It is
the weaker variant and the reason is worth holding: in the pre-run form the ask is permission
to send something that already exists, and here it is permission to do work. Expect a lower
reply rate than the 8% target, which assumes the asset arrives first.

**What carries the email instead of a finding.** The calendar, and only the calendar.
15 October is a fixed CMS date, it is the one deadline this reader organises their year
around, and it needs no enrichment to be true.

### Touch 1 — the calendar

**Subject:** October 15

```
October 15 is [N] weeks out. From then until December 7, every one of your
callers can change their plan.

I'll put twenty real benefit questions to your line before that window opens,
the kind callers actually ask, and send you a written note on which ones came
back answered. No charge and nothing to install.

Want me to run it on [Agency]?

[First name]
```

### Touch 1, alternate opening

Where the calendar has already been used on that row, open on the distinction the whole
positioning rests on. The first line is approved verbatim in `ops/copy-bank.md`.

```
Nobody calls a Medicare agency to ask what Medicare Advantage is. They call to
ask what their own plan covers, and from October 15 to December 7 they can act
on the answer.

I'll put twenty of those questions to your line before the 15th and send you a
written note on which ones came back answered.

Want me to run it on [Agency]?

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

252 characters as written, 288 with the longest agency name merged.

```
From October 15 every caller can switch plans, so your phone matters more
than it does all year. Before then I'll put 20 real benefit questions to
your line and send you a note on which ones came back answered. No charge.
Want me to run it on [Agency]?
```

### Shorter alternate

181 characters. Drops the reason and leads on the offer. Worth running against the first as a
split, because on this channel brevity and a clear reason pull in opposite directions.

```
Before October 15 I'll put 20 real benefit questions to your line and send
you a note on which ones came back answered. No charge, nothing to install.
Want me to run it on [Agency]?
```

### Why it is built this way

**The reason comes before the offer.** October 15 is the date the reader organises their year
around, and one clause on what changes then does the persuading that a paragraph about missed
calls would do worse.

**The ask is a yes or no.** Not a call, not a calendar link, not a reply with information.
Acceptance and reply are two separate decisions on this channel, and a question answerable in
one word is the only ask that survives both.

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
