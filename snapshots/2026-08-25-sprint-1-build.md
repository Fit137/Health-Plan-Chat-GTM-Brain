# Snapshot — 2026-08-25 · Sprint 1 build

The state of the go-to-market on the day this brain was built. Baseline for everything
that follows.

## Product

| | |
|---|---|
| Stage | Pre-revenue, pre-design-partner |
| Customers | **Zero** |
| Shipped differentiators | 6, all L3 Medicare plan IP |
| Known table-stakes gaps | Appointment booking, SOA capture |
| Unverified capabilities | 3 (provider lookup, consent capture, accessibility design) |
| Security | HIPAA-aligned handling. **SOC 2 not held, not in audit** |
| Onboarding | 5 business days target, unproven at scale |

## Funnel

Nothing in market. No channel is running. The funnel exists as design, not as data.

| Stage | State |
|---|---|
| 1 Awareness | No channel live |
| 2 Interest | Gap Report machinery not built |
| 3 Consideration | Sandbox is manual, 72h |
| 4 Decision | **Blocked.** No published price |
| 5 Onboarding | Untested |
| 6 Adoption | Two roadmap gaps cap it |
| 7 Renewal | — |

## Competitive

| | |
|---|---|
| Closest on depth | careCycle, ~$10,000/mo, does not serve our segment |
| Closest on product | Coverage Voice — faster, SOC 2, captures SOA, ships sub-accounts |
| Fastest | Synthflow, 9.4 deployment, no Medicare knowledge |
| Our lead | Plan-grounded answer depth 9.3, accessible entry 8.7 |
| Our lag | Deployment speed 5.4, integration breadth 4.6 |

No competitor moved this period. Coverage Voice's SOA capture and multi-agency
sub-accounts were discovered during the build, not newly launched.

## Calendar position

**25 August 2026.** Seven weeks to AEP. Roughly three weeks of usable design-partner
recruitment left before agency owners become unreachable on 15 October.

This is the most consequential number in the snapshot. The recruitment window closes
before the roadmap gaps could plausibly close, which means Sprint 2 either recruits
against the product as it is or waits until January.

## What this snapshot changes

**It sets the baseline.** Every KPI in `reference/customer-journey.md` and
`reference/outbound-engine.md` is an initial target with no data behind it. First-cohort
data replaces them; until then nothing in this brain may be presented as a result.

**It confirms OF-1 as the priority.** Stage 4 is the only *blocked* stage, as opposed to
at-risk or capped, and unblocking it is a decision rather than a build.

**It records what "no customers" means in practice.** No testimonial, no logo, no count,
no case study, no reference call, no "agencies tell us". `status_notes` in the master
context carries this and the QA checklist enforces it. When the first design partner
signs, that is a trigger review — see `ops/review-cadence.md`.

**It does not change any ledger.** Nothing here contradicts a decision or a claim already
recorded. This snapshot is evidence that the strategy as written is internally consistent
on the day it was built, which is the only thing a first snapshot can be.

## Next snapshot

Due end of September, before AEP closes the window. Watch for: whether the price
published, whether a design partner signed, and whether any onboarding ran long.
