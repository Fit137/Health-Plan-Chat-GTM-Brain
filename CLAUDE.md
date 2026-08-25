# Health Plan Chat — Go-to-Market Brain

The single source of truth for Health Plan Chat's go-to-market. Strategy, messaging,
claims and voice. Content and context, not application code.

**If the routers ever disagree, this file wins.**

## Read in this order

1. `context/HealthPlanChat_GTM_Master_Context.md` — the distilled source of truth. Read
   the frontmatter `status_notes` first; it tells you what you may not assume.
2. `rules/glossary.md` — canonical vocabulary.
3. `rules/feature-status.md` — what may be promised.
4. `rules/do-not-say.md` — claim hygiene. Every prohibition carries a replacement.
5. `rules/writing-rules.md` — how every word is written.
6. `ops/QA-checklist.md` — the pre-ship gate.

Then pull in what the task needs: `reference/` for depth, `templates/` and `examples/`
for production, `ops/` for state.

## Two audiences. Pick one before writing.

- **ICP-1** — independent Medicare agency, 3–10 licensed agents. One owner decides,
  month-to-month, no procurement, no security review.
- **ICP-2** — General Agency or FMO downline. A committee, an annual contract, a security
  review, a phased rollout.

An asset serves one. Never both. The signal for which track a prospect is on is which
value driver they completed: D1 or D2 implies ICP-1, D5 or D6 implies ICP-2.

## Non-negotiables

- **No price, externally, ever, until it is published.** It is modelled, not decided.
- **No unshipped capability in the present tense.** Appointment booking and Scope of
  Appointment capture are roadmap and are the two most often asked about.
- **No customer, count, logo or testimonial.** There are none. Vague plurals — "agencies
  tell us", "what we're seeing" — are fabrication.
- **No SOC 2 claim.** Not held. Coverage Voice is certified; say so when it comes up.
- **Multi-agency deployment is not unique to us.** Sell plan grounding across the
  downline, not the multi-tenancy.
- **Every superlative gets scoped** against `rules/do-not-say.md` before it stands.

## Before you ship

Run `ops/QA-checklist.md` in full. If an item cannot be ticked, it fails. The three that
get through most often: a price slipping in as "affordable", a roadmap capability in the
present tense, and a vague plural implying customers.

## To update this brain

New market input — a call note, an objection, a competitor move, a churn reason — goes to
`ops/signal-log.md` first, then gets triaged against the corroboration thresholds there.
**Ledgers before copy, always.** Decisions are dated in `ops/decisions.md` and are not
relitigated.
