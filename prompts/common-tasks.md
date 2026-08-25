# Common tasks — filled prompts

Copy, adjust the bracketed parts, run. Each names the files to load and ends with the QA
instruction.

---

## Write a cold outreach sequence for an ICP-1 agency

> Load `CLAUDE.md`, all four files in `rules/`, `reference/outbound-engine.md`,
> `reference/value-proposition-icp1.md`, `templates/cold-outreach-icp1.md` and
> `examples/cold-outreach-icp1-approved.md`.
>
> Write a four-touch sequence for [agency name], [N] licensed agents in [county, state],
> selling [plans]. The Gap Report has already been run and found: [findings].
>
> Match the voice of the approved example. No price, no capability claim in touch one, no
> customer references. Then run the draft against `ops/QA-checklist.md` and show me the
> result line by line.

## Write a LinkedIn sequence for an ICP-2 prospect

> Load `CLAUDE.md`, all four files in `rules/`, `reference/value-proposition-icp2.md`,
> `reference/outbound-engine.md`, `templates/linkedin-outreach-icp2.md` and
> `examples/linkedin-icp2-approved.md`.
>
> Target is [name], [title] at [company], roughly [N] contracted downline agents.
> Aggregate audit findings available: [findings].
>
> Sell enforceability, not plan knowledge. State security posture honestly. Never mention
> month-to-month. Then run `ops/QA-checklist.md`.

## Handle an objection I just got on a call

> Load `reference/objection-handling.md`, `rules/do-not-say.md` and
> `rules/feature-status.md`.
>
> The prospect said: "[verbatim]."
>
> Give me the honest answer. If the honest answer is "not yet", say not yet and tell me
> what to move to instead. If this objection is not already in the file, draft the entry
> and I will add it.

## Check a draft before it ships

> Load all four files in `rules/` and `ops/QA-checklist.md`.
>
> Here is the draft: [paste].
>
> Run every item on the checklist and report pass or fail with the specific line for each
> failure. Do not rewrite it — I want the failures first.

## Log a signal from a call

> Load `ops/signal-log.md`, `ops/decisions.md` and the ledger this points at.
>
> Signal: [verbatim quote or note]. Source: [who, when, what context].
>
> Log it, triage it, and tell me whether it changes positioning, ICP, messaging or the
> claim ledger — or whether it corroborates something already logged. If it crosses the
> corroboration threshold, draft the ledger change.

## Build a comparison page against a competitor

> Load `reference/competitor-battlecards.md`, `reference/competitive-analysis.md`,
> `rules/do-not-say.md` and `templates/landing-page.md`.
>
> Competitor: [name].
>
> Lead with their genuine strength, accurately. State our gaps where they are real. Then
> run `ops/QA-checklist.md` and flag anything that reads as spin.

## Update the status ledger after a release

> Load `rules/feature-status.md`.
>
> Shipped this week: [capabilities]. Moved to in-build: [capabilities].
>
> Update the ledger first. Then tell me every file in the brain whose copy is now stale
> because of the change, and update `snapshots/` with what changed.

## Produce the weekly review

> Load `ops/review-cadence.md`, `ops/signal-log.md` and `ops/decisions.md`.
>
> Run the review due this week. Report any ledger past its staleness threshold, any open
> question with no owner, and any signal logged but never triaged.

---

## Never write without loading the brain

If a prompt above is run without the control layer loaded, the output will be plausible
and wrong: it will quote a price that is not published, claim a capability that is not
shipped, or repeat a uniqueness claim that has been falsified. That is not a hypothetical
— all three are live traps in this brain, recorded in `status_notes`.
