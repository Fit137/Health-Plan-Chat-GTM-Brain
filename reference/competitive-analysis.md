# Competitive analysis — market shape and the wedge

*Load this for any competitive claim, comparison page, or battlecard work. Distils
`sources/extracted/competitive-analysis.md`. Per-rival talk tracks are in
`competitor-battlecards.md`.*

## The shape of the market

Six competitors, in two groups that do not overlap much.

**Medicare-native.** careCycle, Coverage Voice, MedicareCopilot, SunFire. These know
Medicare. None of them answers the beneficiary's plan question except careCycle, and
careCycle prices itself out of our segment.

**Horizontal voice AI.** Synthflow, Smith.ai. These are excellent at voice and have no
Medicare knowledge at all.

The gap between the groups is the market. An agency choosing today picks between a product
that understands Medicare but costs $10,000 a month, and one it can afford that has never
read a Summary of Benefits.

## The price finding — this is the wedge

careCycle entry pricing is approximately **$10,000 a month** for an operation of 5–10
licensed agents, roughly $1,000–$2,000 per agent per month, behind a demo and custom
quote.

careCycle is the only competitor with Medicare depth comparable to ours. At that price the
entire 2–25 agent independent segment is priced out of the only product that could serve
it. **They are not losing that segment on capability. They are not competing for it.**

Two consequences:

1. **The wedge is a pricing wedge before it is a product wedge.** Go to market leading
   with accessible, predictable pricing, and treat plan depth as the proof that the price
   is not a downgrade — not the other way round.
2. **The competitive risk is not careCycle winning our deals.** It is careCycle launching
   a self-serve tier. Publishing our price is what makes that expensive for them: they
   cannot follow without cannibalising a $10k/month book.

Confidence: medium-high. Sourced from third-party pricing analysis, not from careCycle,
who publish no pricing. Worth confirming on a prospect call before it appears in external
material.

## The scoring vectors

Four vectors, detailed in `positioning.md`. We lead plan-grounded answer depth (9.3) and
accessible entry (8.7). We are last on deployment speed (5.4) and integration breadth
(4.6).

## Method note — travels with any score we quote

The three Medicare-native vendors have **zero G2 and zero Capterra presence**. Their
scoring rests on their own published material, not on independent review corpora, while
Synthflow's rests on a large review corpus. The comparison is therefore not like-for-like,
and saying so is what makes the rest of the analysis credible.

Direct web access to competitor sites was blocked during this research; findings come from
search results and published pages retrieved indirectly. Re-verify before external use.

## What each competitor is actually good at

Leading with the rival's genuine strength is what makes a battlecard credible internally
and survivable in front of a prospect. Full cards in `competitor-battlecards.md`.

| Competitor | Genuinely good at | Where the gap is |
|---|---|---|
| **careCycle** | Medicare depth, member-aware call handling, enterprise-grade delivery | Price floor excludes our whole segment |
| **Coverage Voice** | 48-hour launch, HIPAA + SOC 2, in-call SOA capture, white-label sub-accounts | Plan-specific answer depth |
| **MedicareCopilot** | Absorbs CRM, quoting, carrier-direct enrolment, commissions, compliance | Agent-facing. Does not answer the beneficiary |
| **Synthflow** | Fastest setup in the category, 200+ integrations, 30+ languages, real review corpus | No Medicare plan knowledge whatsoever |
| **SunFire** | Consumer plan shopping and comparison at scale | Not an answering product |
| **Smith.ai** | Human-plus-AI reliability, established trust | Generic. Cannot answer a plan question |

## Where we are weakest

Stated plainly because the ICP-2 security review will surface all of it anyway:

- **Deployment speed 5.4** against Synthflow 9.4 and Coverage Voice's 48-hour promise.
- **SOC 2 not held.** Coverage Voice is certified. This comes up in every ICP-2 evaluation.
- **SOA capture absent.** Coverage Voice does it in-call, at the exact moment we hand off.
- **Appointment booking absent.** Both direct competitors have it, +14.1 demand.
- **No customers, no case studies, no reference calls yet.**

Understating our position loses the deal. Overstating it loses the account.

## Three open questions that would move the analysis

| # | Question | Why it matters | How to settle |
|---|---|---|---|
| Q-1 | Does careCycle's plan-context handling cover pre-sale benefit Q&A, or only post-enrolment member servicing? | Determines whether our plan-knowledge lead is wide or narrow — the core of the positioning | Call careCycle as a prospect, ask whether a non-member caller can get a dental allowance answered |
| Q-2 | Do careCycle and Coverage Voice answer in the agency's name or their own? | Settles whether agency-branded voice is a differentiator | Call both as a prospect, listen to the greeting |
| Q-3 | Do we actually do provider lookup, consent capture, accessibility-oriented design? | Third-party research attributes all three to us; the source sheet does not | Confirm against the product before any appears externally |

All three are cheap to answer and all three are unresolved. See `ops/decisions.md`,
"Open, owned elsewhere".
