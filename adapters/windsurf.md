---
trigger: model_decision
description: The Health Plan Chat go-to-market brain. Use for positioning, messaging, claims, competitive work, and any customer-facing copy.
---

The Health Plan Chat go-to-market lives at the root of this repository.

Load `AGENTS.md` first, then `rules/writing-rules.md`, `rules/do-not-say.md`, and
`rules/feature-status.md`. For outbound work, load `reference/outbound-engine.md`.

Pick the audience first, never blend them:

- **ICP-1** — independent Medicare agency, 3–10 licensed agents. One owner decides,
  month-to-month, no procurement.
- **ICP-2** — General Agency or FMO downline. A committee, an annual contract, a security
  review.

Non-negotiables:

- No price, externally, until it is published.
- No unshipped capability in the present tense. Appointment booking and Scope of
  Appointment capture are roadmap.
- No customer, count, logo or testimonial. There are none.
- No SOC 2 claim. Not held.
- Multi-agency deployment is not unique to us.
- Every superlative gets scoped against `rules/do-not-say.md`.

Run `ops/QA-checklist.md` before returning a draft. New market input goes to
`ops/signal-log.md`.
