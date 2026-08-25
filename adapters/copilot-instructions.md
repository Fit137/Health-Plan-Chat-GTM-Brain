<!-- gtm-brain:begin -->
## Health Plan Chat go-to-market

The Health Plan Chat go-to-market lives at the root of this repository. It is the source
of truth for positioning, messaging, claims, and voice. Do not restate strategy from
memory when the brain settles it.

Before any customer-facing writing, in this order:

1. `AGENTS.md`, the router.
2. `rules/writing-rules.md`
3. `rules/do-not-say.md`
4. `rules/feature-status.md`

Pick the audience before writing. The audiences are never blended:

- **ICP-1** — independent Medicare agency, 3–10 licensed agents. One owner decides,
  month-to-month, no procurement, no security review.
- **ICP-2** — General Agency or FMO downline. A committee, an annual contract, a security
  review, a phased rollout.

Non-negotiables:

- No price, externally, until it is published. It is modelled, not decided.
- No unshipped capability in the present tense. Appointment booking and Scope of
  Appointment capture are roadmap.
- No customer, count, logo or testimonial. There are none.
- No SOC 2 claim. Not held.
- Multi-agency deployment is not unique to us.
- Every superlative gets scoped against `rules/do-not-say.md`.

For outbound work, load `reference/outbound-engine.md`. Run `ops/QA-checklist.md` against
every draft before returning it. New market input goes to `ops/signal-log.md` rather than
into the copy.
<!-- gtm-brain:end -->
