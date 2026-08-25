# Customer journey — seven stages, two funnels

*Load this when writing a stage-specific asset, or when deciding what a prospect at a
known stage needs next. Distils `sources/extracted/customer-journey-funnel.md`.*

KPI targets below are **initial targets to calibrate against first-cohort data**, not
forecasts. There is no baseline yet. Never present them as results.

## ICP-1 — the primary motion

| Stage | Mindset | Asset | KPI | Owner |
|---|---|---|---|---|
| **1 · Problem Awareness** | "We're missing calls we can't afford to miss." | D1 Readiness Scorecard, D2 Missed-Call Calculator, cold outreach with one Gap finding | Driver completion ≥15% of visitors; cold reply ≥8% | Demand gen + founder |
| **2 · Interest / Education** | Wants the size of the problem without starting a project. Sceptical any vendor knows their county's plans | **D3 Benefit Answer Gap Report**, AEP readiness checklist, community post series | Report → sandbox request ≥25%; delivered within 48h | Marketing + founder |
| **3 · Consideration** | Comparing us against careCycle, Coverage Voice, a $79 receptionist, and doing nothing | **D4 72-Hour Plan Brain Sandbox** on their own documents, comparison pages, "what it will and won't say" | Sandbox → pricing conversation ≥40%; **20/20 regression before handover** | Marketing + sales |
| **4 · Decision** | Needs price certainty and liability reassurance. No committee | Pricing one-pager, month-to-month agreement, D5 CMS AI Exposure Review, BAA summary | Sandbox → paid; sandbox to signature ≤10 days | Founder + compliance |
| **5 · Onboarding / First Win** | "Prove it before AEP." | Plan document intake checklist, 20-question regression report, branding and escalation config, agent comms | **Live ≤5 business days**; first after-hours call ≤7 days | Success + eng |
| **6 · Adoption & Expansion** | Wants more of the front line covered | Additional carriers, Spanish, chat embed, monthly answer-quality report | ≥3 plan corpora live; ≥70% resolved without callback | Success + product |
| **7 · Renewal / Advocacy** | Wants proof they can show, and standing among peers | AEP review pack at 2026 CMS rates, before/after Gap score, referral and FMO ask | Retention ≥90% through AEP; ≥1 referral per advocate | Success + partnerships |

## Where ICP-2 diverges

The seven stages hold; four change shape enough to run differently.

- **Stages 1–2.** Trigger is a compliance finding, downline expansion, or rising cost per
  acquisition — not a missed Sunday call. Entry driver is D5 CMS AI Exposure Review or D6
  AEP Peak-Load Stress Test, reached through LinkedIn, not community channels.
- **Stage 3.** Adds a security and compliance review ICP-1 does not have. Requires HIPAA
  posture, honest SOC 2 status, BAA, data residency, integration architecture.
- **Stage 4.** Becomes a committee. Director of Operations is frequently the true buyer;
  the principal signs. Annual contract, phased rollout, expansion pricing.
- **Stages 5–6.** Rollout is per-downline-segment, and **contractor adoption is the
  failure mode.** Agent comms must address "is this replacing me" directly.

## The three exposures

These are the reasons this funnel breaks, in the order they will break it.

**Stage 4 is blocked.** The pricing one-pager and published price do not exist (OF-1). So
every deal currently requires a bespoke price conversation — which is exactly the demo
gate the positioning attacks. This is the single largest unblock in the funnel.

**Stage 5 is at risk.** Live in five business days is the promise a pre-AEP deal depends
on, and deployment speed is our weakest vector at 5.4 against Synthflow 9.4 and Coverage
Voice at 48 hours. This is where the funnel most likely breaks in practice.

**Stage 6 is capped.** Appointment booking (+14.1 demand, both direct competitors ship it)
and SOA capture (a CMS requirement Coverage Voice handles in-call) both sit inside stage 6
and both are roadmap.

## The calendar constrains everything

Recruitment runs **February to mid-September**. AEP is **15 October – 7 December**, and
during it agency owners are unreachable at any price. OEP runs January to March.

This makes the funnel seasonal rather than continuous, and it makes the design-partner
recruitment window — not the roadmap — the binding constraint on Sprint 1.

The one asset that works *during* AEP is the Gap Report: it costs the agency nothing,
takes 90 seconds of their attention, and arrives while the wound is open.

## How the two funnels feed each other

Stage 7 of ICP-1 is where ICP-2 pipeline actually gets created. A producing agency
introducing us to its FMO principal outperforms cold outreach to the same principal by a
wide margin. And an FMO that adopts brings its downline agencies in at once — the
widest acquisition path in the whole model.
