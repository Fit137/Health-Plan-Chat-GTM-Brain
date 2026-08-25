# Health Plan Chat — Go-to-Market Brain

The single source of truth for Health Plan Chat's go-to-market. Strategy, messaging,
claims and voice. Content and context, not application code.

Read by Codex, Cursor, Zed, opencode, Jules and anything else that reads `AGENTS.md`.
**`CLAUDE.md` is authoritative if the two ever disagree** — they are kept identical on
purpose, so if you find a difference, treat `CLAUDE.md` as correct and flag it.

## Read in this order

1. `context/HealthPlanChat_GTM_Master_Context.md` — the distilled source of truth. Read
   the frontmatter `status_notes` first; it tells you what you may not assume.
2. `rules/glossary.md` — canonical vocabulary.
3. `rules/feature-status.md` — what may be promised.
4. `rules/do-not-say.md` — claim hygiene. Every prohibition carries a replacement.
5. `rules/writing-rules.md` — how every word is written.
6. `ops/QA-checklist.md` — the pre-ship gate.

Then pull in what the task needs: `reference/` for depth, `templates/` and `examples/`
for production, `ops/` for state. Full index: `llms.txt`.

## Two audiences. Pick one before writing.

- **ICP-1** — independent Medicare agency, 3–10 licensed agents. One owner decides,
  month-to-month, no procurement, no security review.
- **ICP-2** — General Agency or FMO downline. A committee, an annual contract, a security
  review, a phased rollout.

An asset serves one. Never both.

## Non-negotiables

- **No price, externally, ever, until it is published.** It is modelled, not decided.
- **No unshipped capability in the present tense.** Appointment booking and Scope of
  Appointment capture are roadmap.
- **No customer, count, logo or testimonial.** There are none.
- **No SOC 2 claim.** Not held.
- **Multi-agency deployment is not unique to us.**
- **Every superlative gets scoped** against `rules/do-not-say.md`.

## Before you ship

Run `ops/QA-checklist.md` in full. If an item cannot be ticked, it fails.

## To update this brain

New market input goes to `ops/signal-log.md` first, then gets triaged against the
corroboration thresholds there. **Ledgers before copy, always.** Decisions are dated in
`ops/decisions.md` and are not relitigated.
