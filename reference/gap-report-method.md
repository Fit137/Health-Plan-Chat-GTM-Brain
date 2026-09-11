# D3 Benefit Answer Gap Report — what it actually is

*Load before offering, running or writing about the Gap Report. The driver table in
`reference/marketing-campaigns.md` scores D3; this file says what the thing is.*

`last_reviewed: 2026-09-11`

## Why this file exists

Outreach copy in `templates/cold-outreach-icp1.md` offers twenty benefit questions put to an
agency's line. Until now the brain scored D3 and never defined it, so the number in the copy
had nothing behind it. A promise in a first touch is a specification.

## The method

Twenty plan-specific benefit questions, asked of the agency's own published number, across
three time bands: business hours, after six in the evening, and a weekend.

The questions are the ones a beneficiary actually asks, not questions about Medicare. "What
is the dental allowance on this plan", "does the OTC card cover this", "what is the specialist
copay", "is my cardiologist in network on that plan". Each is answerable from a Summary of
Benefits, and each is wrong if answered generically.

## What gets recorded

Three outcomes per call, and they are not the same finding.

| Outcome | What it is | What it costs the agency |
|---|---|---|
| **No answer** | Voicemail, an endless hold, a menu with no exit | The call is lost. Nothing else in the funnel happens |
| **Answered, cannot answer** | A person picks up and takes a message, or promises a callback | The caller waits, and the five-minute window closes |
| **Answered wrong** | A confident answer that the carrier document contradicts | The one that carries liability rather than lost revenue |

The third is the one agencies do not know they have, and it is the reason the report is
checked against the carrier's published document rather than against an opinion.

## The score, and why it is twenty

The report returns a count out of twenty, split by the three outcomes and by time band.

**Twenty is not an arbitrary round number. It is the same test the product is held to.** The
onboarding gate in `context/HealthPlanChat_GTM_Master_Context.md` is 20/20 against the
agency's own documents before handover. So the report measures their line on the test our own
system has to pass before it goes live, which makes the before and after directly comparable
and keeps us honest: we publish their score against a bar we have already agreed to clear.

## What each outcome maps to

| Gap found | What answers it | Status |
|---|---|---|
| No answer | 24/7 voice answering | SHIPPED |
| Answered, cannot answer | Plan-grounded benefit answers from ingested Summary of Benefits and Evidence of Coverage | SHIPPED, and the differentiator we lead on |
| Answered wrong | Every answer resolves against the carrier document, and anything plan-specific escalates | SHIPPED |

Nothing in that table is roadmap, which is what makes the report safe to send. It finds three
problems and all three are answered by capability that exists today. Do not let a finding
drift into appointment booking or Scope of Appointment capture, which are the two the reader
will ask about next and neither ships.

## Why before 15 October

Two reasons and both are the reader's, not ours.

Call volume rises through the Annual Enrollment Period, so whatever the gap is, it is
multiplied across the eight weeks that decide the year. And the owner is unreachable from
15 October to 7 December, so a finding delivered after the 15th cannot be acted on until
January.

## The consent problem in the offered variant

Where the report is offered and run on reply rather than pre-run, the agency knows the call is
coming. An owner who warns the front desk changes what the test measures.

Three honest ways to hold it, in order of preference:

1. **Do not name the window.** Consent to the audit is not consent to a scheduled audit. "In
   the next two weeks" preserves most of the value.
2. **Report it as what it is.** A warned line that still fails is a stronger finding, not a
   weaker one, and a warned line that passes is a real answer the agency has earned.
3. **Pre-run the top tier blind.** For the highest-scoring rows, run before the first touch
   and accept the cost. This is the original A1 form and it exists partly because consent
   contaminates the test.

## Running it cleanly

Ask a benefit question. That is all the call is.

Do not claim to be enrolling, do not request a Scope of Appointment, and do not misrepresent
yourself if asked directly who you are. The question "what is the dental allowance on this
plan" is one anyone may ask, and the finding does not depend on pretending to be anyone.

Bear in mind the agency records its calls, as a Third-Party Marketing Organisation is required
to, so the call exists on their side too. Behave accordingly.

## What the report is for

Not to shame the agency. The report ends one question short on purpose, and the question the
owner asks next is what those calls would have sounded like answered. That is D4, the sandbox
on their own documents, and it is where the deal is won.
