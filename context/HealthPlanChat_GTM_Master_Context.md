---
title: Health Plan Chat Go-To-Market Master Context
project: Health Plan Chat
type: gtm_context_file
purpose: Single source of truth for any AI agent executing Health Plan Chat go-to-market work.
version: 1.0
last_updated: 2026-08-25
status_notes: >
  Pre-revenue, Sprint 1. No customers, no design partners, no testimonials, no case
  studies — do not imply any exist. Pricing is PROPOSED and UNPUBLISHED (OF-1); never
  state a price externally until the founder confirms and publishes it. Appointment
  booking and Scope of Appointment capture are NOT shipped (OF-3). Multi-agency
  deployment is NOT unique to us (OF-2). Three product claims are unverified (Q-3):
  provider lookup, consent capture, accessibility-oriented design. SOC 2 is not held.
  Deployment speed scores 5.4 against Synthflow 9.4 and Coverage Voice 9.1 — this is
  the binding constraint on the whole strategy, not a detail.
canonical_vocabulary: Health Plan Chat, plan corpus, plan-grounded, benefit answer, agency, downline, FMO, AEP, TPMO, SOA, beneficiary, licensed agent
---

# Health Plan Chat — GTM Master Context

## 0. Agent operating instructions

You are reading the single source of truth for Health Plan Chat's go-to-market. Read
this file once, then execute from it. Do not re-derive strategy that is settled here.

**Before you write anything a customer will see**, load all four files in `rules/` and
check your draft against `ops/QA-checklist.md`. That is not optional and it is not a
formality — this business sells into a CMS-regulated market where an overclaim is a
compliance exposure, not a marketing problem.

Four hard guardrails, ranked by how much damage getting them wrong does:

1. **Never claim an unshipped capability.** Check `rules/feature-status.md`. Appointment
   booking and SOA capture are the two that get asked about most and neither ships.
2. **Never state a price externally.** Pricing exists as a model, not as a decision.
3. **Never claim uniqueness without checking `rules/do-not-say.md`.** Three of our nine
   reasons-to-believe rest on claims that have not been verified against the product,
   and one uniqueness claim has already been falsified.
4. **Never blend the two audiences.** ICP-1 is one owner deciding in a single
   conversation. ICP-2 is a committee with a security review. An asset serves one.

When this file and a `rules/` file disagree, this file is authoritative — and both get
updated in the same edit.

## 1. House writing rules

Short version; the full rules are in `rules/writing-rules.md`.

Write to the reader about what they get, never about what the software does. Specifics
beat adjectives: "the dental allowance on their plan", not "comprehensive benefit
information". No exclamation marks. Paragraphs under four lines. The full banned words
list lives in `rules/writing-rules.md`; do not use any of them or their variants.

The audience is a licensed insurance professional who has been sold to badly for years
and who carries personal liability for what their front line says. Write to someone
competent, sceptical and busy.

## 2. Canonical vocabulary

Full table in `rules/glossary.md`. The four that matter most:

- **Health Plan Chat** — three words, all capitalised. Never "HPC" externally.
- **Plan corpus** — the ingested Summary of Benefits and Evidence of Coverage documents
  for one agency's plans. This is the asset that compounds. Not "knowledge base", not
  "training data".
- **Benefit answer** — a response to a plan-specific coverage question. The unit of
  value. Not "conversation", which is the unit of billing.
- **Beneficiary** — the person on Medicare. Never "customer", never "patient". The
  agency is the customer; the beneficiary is who calls.

**The distinction that must never blur:** answering the *beneficiary* is what we do.
Informing the *agent* is what MedicareCopilot and SunFire do. Capturing the *lead* is
what careCycle and Coverage Voice do. Every competitor comparison turns on this.

## 3. Status ledger, short form

Full ledger with flags in `rules/feature-status.md`. Update that file before any copy
follows a status change.

SHIPPED: 24/7 voice answering, plan-grounded benefit Q&A from ingested SB/EOC
documents, premium and copay questions, supplemental benefit questions, cross-plan
comparison within the agency's book, licensed-agent escalation with the conversation
carried across, TPMO disclaimer and automated-system disclosure, call recording with
CMS ten-year retention, agency-branded greeting, Spanish.

IN BUILD: website chat embed, multi-agency deployment.

ROADMAP, and both are table stakes: **appointment booking** (+14.1 demand, both direct
competitors have it) and **Scope of Appointment capture** (a hard CMS requirement for a
TPMO, which Coverage Voice handles in-call). Shipping these wins nothing; lacking them
loses deals.

UNVERIFIED, do not claim in any form until confirmed against the product: provider
lookup, consent capture, accessibility-oriented design for older adults.

## 4. Claim hygiene ledger, short form

Full ledger in `rules/do-not-say.md`. The five that recur:

| Do not say | Say instead |
|---|---|
| "SOC 2 certified" / "HIPAA compliant" | "HIPAA-aligned handling; SOC 2 not held — here is our current posture" |
| "The only AI that can deploy across a downline" | "The only one that carries plan grounding across a downline" |
| "$499/month", or any price, externally | "Pricing is published at [URL]" — and until it is, nothing |
| "Books the appointment" | "Hands the qualified caller to your licensed agent with the whole conversation attached" |
| "Never gets it wrong" | "Every answer resolves against the carrier's own document, and anything plan-specific escalates" |

## 5. What the product actually is

Health Plan Chat is a consumer-facing AI voice and chat agent for independent Medicare
insurance agencies, trained on the specific Medicare plans each agency sells.

A beneficiary calls the agency's own number at nine on a Sunday and asks what their
dental allowance is. The agent answers from that agency's carrier documents, in the
agency's name, applies the TPMO disclaimer, records the call, and either resolves the
question or hands to a licensed agent with the full conversation attached. A structured
lead lands in the agency's CRM.

What it is not: a receptionist that takes a message, a lead-capture bot, an agent-facing
quoting tool, or a consumer plan-shopping site.

## 6. Feature matrix — what leads, what is table stakes

Full detail: `reference/feature-matrix.md`. Source: 25 features scored −20 to +20 on
demand and competitiveness. High demand ≥ +10.0, high differentiation ≥ +5.0.

Features are layered: **L1 Commodity AI** (14 features), **L2 Insurance Workflow** (5),
**L3 Medicare Plan IP** (6).

The finding the entire strategy rests on — the layer and the quadrant are the same fact:

```
               Q1  Q2  Q3  Q4
  L1 Commodity  0  10   0   4
  L2 Workflow   0   3   2   0
  L3 Plan IP    6   0   0   0
```

All six Q1 differentiators are L3 plan IP. Zero of fourteen L1 commodity features reach
Q1. **Anything a $79/month AI receptionist also does is not a story we can win on.**

Lead with the six L3 features. Everything else is entry cost.

## 7. Competitive market analysis

Full detail: `reference/competitive-analysis.md`; battlecards in
`reference/competitor-battlecards.md`.

Six competitors across two frames. The two that matter:

- **careCycle** — the only comparable Medicare depth. Starts around **$10,000/month**
  for 5–10 agents, behind a demo-and-quote gate. They are not losing the independent
  segment on capability; they are not competing for it at all.
- **Coverage Voice** — Medicare-native, HIPAA and SOC 2 certified, live under the
  customer's brand in 48 hours, captures SOA in-call, ships multi-agency sub-accounts.
  Faster and more compliant than us today. Weaker on plan-specific answer depth.

Also: **Synthflow** (horizontal, 9.4 deployment speed, 200+ integrations, no Medicare
knowledge), **MedicareCopilot** (agent-facing platform, absorbs CRM, quoting and
enrolment), **SunFire** (consumer-facing plan shopping), **Smith.ai** (human-plus-AI
answering).

Method note that must travel with any competitive claim: the three Medicare-native
vendors have **zero G2 or Capterra presence**, so their scoring rests on their own
published material, not on review corpora. Say so when the scoring is quoted.

## 8. ICP and buying committee

Full detail: `reference/icp-personas.md`.

**ICP-1 (MVP → PMF)** — independent Medicare agencies, 3–10 licensed agents,
$400K–$2.5M annual commission revenue, single-state or 2–3 contiguous states, densest
in FL, TX, AZ, CA, PA, OH, NC, MI. Chosen for exactly one reason: it is the segment
careCycle's price floor has left unsold. **No committee.** The owner decides and is
usually also the top producer, so they feel the missed-call pain personally.

**ICP-2 (Growth)** — established agencies, General Agencies and FMO downlines. 10–50
in-house agents plus 50–500 contracted downline. $2.5M–$25M. **A committee.** The
Director of Operations is frequently the true buyer; the principal signs. Annual
contract, security review, phased rollout.

Level 1 users have effective veto in both: an agent who did not choose the tool kills it
by quietly not using it.

## 9. Strategic verdicts already decided

Do not relitigate these. Full log with dates and rationale: `ops/decisions.md`.

1. **Lead on plan grounding, not on features.** All six differentiators are L3.
2. **ICP-1 first.** The unsold segment, not the bigger one.
3. **Pricing is the wedge before the product is.** Accessible price leads; plan depth
   proves the price is not a downgrade. Not the other way round.
4. **Publish the price, no demo gate.** The one axis careCycle cannot follow without
   cannibalising a $10k/month book.
5. **Two separate tracks, never merged.** ICP-1 self-serve, ICP-2 assisted annual.
6. **State weaknesses plainly.** Coverage Voice holds SOC 2 and we do not. Understating
   our position loses the deal; overstating it loses the account.
7. **The Benefit Answer Gap Report is the top-of-funnel spine** for both funnels.

## 10. Value proposition — ICP-1

Full detail with nine reason-to-believe copy drills: `reference/value-proposition-icp1.md`.

**Brand promise.** Every caller gets a straight answer about their Medicare plan — the
dental allowance, the copay, the OTC card — at the moment they ask, in your agency's
name, whether or not anyone is in the office.

**Three pillars:** Plan Fluency · Answers You Can Stand Behind · Coverage Without the
Headcount.

## 11. Value proposition — ICP-2

Full detail: `reference/value-proposition-icp2.md`.

*"Consistent, compliant plan expertise across every agent in your downline."* One plan
corpus, enforced uniformly, with disclaimer, escalation and recording built in. A
recruiting asset, not just an ops tool. Sell to the Director of Operations first; give
the principal the recruiting-differentiator angle.

## 12. Positioning statement

Full detail: `reference/positioning.md`; the strategic fork in
`reference/positioning-verdict.md`.

Health Plan Chat owns the one question the category does not answer: *what does my plan
actually cover?* Every competitor either captures the caller or informs the agent; none
answers the beneficiary.

Four vectors, and we lead two:

| Vector | Leader | Us |
|---|---|---|
| Speed to working deployment | Synthflow 9.4 | **5.4 — our binding constraint** |
| Integration breadth | Synthflow 9.6 | 4.6 |
| **Plan-grounded answer depth** | **Health Plan Chat 9.3** | we lead |
| **Accessible entry for a small agency** | **Health Plan Chat 8.7** | we lead |

Acquisition on our two vectors happens by **demonstration, not persuasion**. An agency
hears its own line fail a dental-allowance question at 9pm, then hears our agent answer
it from their carrier's own documents.

**The condition governing all of it:** at 5.4 on deployment speed we are not yet
credible in a category judged on time-to-first-agent. The corpus advantage only starts
compounding once onboarding survives the first evaluation.

## 13. Customer journey funnels

Full detail: `reference/customer-journey.md`.

Seven stages, both ICPs: Problem Awareness → Interest/Education → Consideration →
Decision → Onboarding/First Win → Adoption & Expansion → Renewal/Advocacy.

Three exposures:

- **Stage 4 is blocked on OF-1.** No published price means every deal needs a bespoke
  price conversation — exactly the demo gate the positioning attacks.
- **Stage 5 is at risk.** Live in 5 business days is what a pre-AEP promise depends on,
  and deployment speed is our weakest vector.
- **Stage 6 is capped.** Appointment booking and SOA capture both sit inside it.

**The calendar is the constraint.** Recruitment runs February to mid-September. From
15 October to 7 December agency owners are unreachable. This funnel is seasonal.

## 14. Campaign and asset plan

Full detail: `reference/marketing-campaigns.md`; channel method in
`reference/outbound-engine.md`.

Seven campaigns. ICP-1: personalised cold outreach (starred), agent community and
forums, AEP prep webinar. ICP-2: LinkedIn outreach (starred), LinkedIn ads (starred),
FMO and carrier co-marketing. Shared: website and email nurture.

The top-of-funnel value driver is **D3 · The Benefit Answer Gap Report**, and it changes
shape by channel: pre-run and unprompted in cold outreach, offered on request on
LinkedIn, replaced by the **D2 Missed-Call Revenue Calculator** behind paid traffic
because a report takes 48 hours and paid traffic needs an instant payoff.

Channels this GTM does not run: consumer-facing advertising, cold calling agencies, paid
search on beneficiary terms.

## 15. Execution cheatsheet

The twenty facts looked up most.

| | |
|---|---|
| What we sell | AI voice and chat front line for Medicare agencies, trained on their plans |
| Who buys, ICP-1 | Agency owner, 3–10 agents, decides alone |
| Who buys, ICP-2 | Director of Operations evaluates, principal signs |
| The one-liner | The only AI that already knows the plans you sell |
| We lead on | Plan-grounded answer depth (9.3), accessible entry (8.7) |
| We lag on | Deployment speed (5.4), integration breadth (4.6) |
| Main rival | careCycle, ~$10,000/month, does not serve this segment |
| Fastest rival | Coverage Voice, 48 hours, SOC 2, captures SOA |
| Differentiators | 6, all L3 Medicare plan IP |
| Table-stakes gaps | Appointment booking, SOA capture |
| TOFU driver | D3 Benefit Answer Gap Report |
| Paid-traffic driver | D2 Missed-Call Revenue Calculator |
| Proof of value | 72-hour Plan Brain Sandbox on their own documents |
| AEP | 15 Oct – 7 Dec. Owners unreachable |
| Selling window | February – mid-September |
| 2026 CMS rates | $694 initial / $347 renewal (national); $864 / $432 California |
| Missed call worth | ~$2,082 in five-year member value |
| Onboarding promise | Live in 5 business days from documents received |
| Regression gate | 20/20 against the agency's own documents before handover |
| Price | PROPOSED, UNPUBLISHED. Never state externally |
