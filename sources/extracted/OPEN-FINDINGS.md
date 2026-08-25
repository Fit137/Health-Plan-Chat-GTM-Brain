# Open Findings — standing note

Findings from the Sprint 1 competitive analysis that revise the source sheet
`Health Plan Chat - Product Features - Sheet1.csv`. They are not yet applied to
`feature-scores.csv`. Summarised in `competitive-analysis.md` §15.

Machine-readable copy: `open-findings.csv`
Last reviewed: 2026-08-24 · Source: `competitive-analysis.md` §12

---

## OF-1 · careCycle's price floor is the wedge

**Finding.** careCycle entry pricing is approximately **$10,000/month** for a Medicare
operation of 5–10 licensed agents — roughly $1,000–$2,000 per agent per month — and is
gated behind a demo and custom quote.

**Why it matters.** careCycle is the only competitor with Medicare depth comparable to
ours. At that price the **entire 2–25 agent independent segment is priced out of the only
product that could otherwise serve them.** They are not losing that segment on capability;
they are not competing for it at all.

**What it changes.** The wedge is a **pricing wedge before it is a product wedge.** Our
go-to-market should lead with accessible, predictable pricing for the independent agency
and treat plan depth as the proof that the price is not a downgrade — not the other way
round. It also means the competitive risk is not careCycle winning our deals; it is
careCycle launching a self-serve tier.

**Action implied.** Publish pricing. An unpublished price surrenders the one axis where
the strongest competitor cannot follow without cannibalising a $10k/month book.

**Update, 2026-08-24.** A full pricing model now exists: `gtm/pricing-model.xlsx`
(9 tabs, all inputs on one Control Panel) and `gtm/pricing-model.md` (design handoff).
Plan Fluent, the Hero tier, is proposed at **$499/month** per agency location with 220
conversations included, roughly **20x below careCycle** and above the generic-receptionist
band. A usage vehicle sits on top: declining overage bands above the allowance, capped at
1.5x the platform fee each month so a busy AEP cannot produce a surprise invoice.

Two things surfaced while building it that the founder should weigh:

1. **A generic 80% software gross margin is not reachable here.** Voice AI carries real
   variable COGS. Holding 80% would force the Plan Fluent allowance down to roughly 105
   conversations, which would put a typical agency into overage every month and break the
   predictability the positioning rests on. The model is set to a 70% target and accepts
   ~68% at full allowance. Both are editable inputs.
2. **The value ceiling ($208/mo) currently sits below the cost floor ($467/mo).** That is
   expected at MVP: the value case rests on unconfirmed enrollment assumptions, so price
   leans on cost and market for now. This is the number design partner data should replace
   first, and the one that would justify raising price.

These are proposed numbers pending founder review, not decisions. This finding stays
**Open** until the price is reviewed, confirmed or adjusted, and actually published.

**Confidence.** Medium-high. Sourced from third-party pricing analysis, not from
careCycle's own site (they publish no pricing). Worth confirming via a prospect call.

---

## OF-2 · Feature 25 is not unique to us

**Finding.** Coverage Voice explicitly markets **"manage sub-accounts across multiple
agencies"**, white-labelled under the customer's own brand and domain, live in 48 hours.

**Why it matters.** Sprint 1 scored *Centralized deployment across agencies/downlines* at
**+17.4 competitiveness** — the second-highest score on the board — on the explicit basis
that nobody else offered it. That basis is false.

**What it changes.** The score should come down to roughly **+6 to +8**. It stays in Q3,
but as a **niche play rather than a moat**, and it can no longer be described as unique in
any external material. The FMO and downline story has to rest on **plan grounding across
the downline** — which Coverage Voice does not have — rather than on multi-tenancy, which
it does.

**Action implied.** Correct `feature-scores.csv` row 25 and re-derive its quadrant. Remove
"only we can do this" from any FMO-facing collateral referencing multi-agency deployment.

**Confidence.** High. Stated plainly on Coverage Voice's own TPA/BPO page.

---

## OF-3 · SOA capture is an unroadmapped compliance gap

**Finding.** Coverage Voice captures **Scope of Appointment** details during the AI call,
alongside identity verification and eligibility confirmation, before warm-transferring to
a licensed agent.

**Why it matters.** For a Third-Party Marketing Organisation, SOA is a **hard CMS
compliance requirement, not a convenience feature.** It sits precisely in the flow between
our benefit answer and our warm transfer — the exact moment we currently hand off. A
prospect comparing us side by side will find a compliance step in their product and a gap
in ours.

**What it changes.** SOA capture belongs on the roadmap next to appointment scheduling
(already flagged in Sprint 1 as the urgent gap at +14.1 demand). Both are table-stakes
features: shipping them wins nothing, and lacking them loses deals. Two known
table-stakes gaps in the same handoff sequence compounds the exposure.

**Action implied.** Add SOA capture to the pre-AEP roadmap. Scope it with the compliance
review that demand driver D5 already requires us to build.

**Confidence.** High. Stated on Coverage Voice's Medicare enrollment feature page.

---

## Still open from Sprint 1 — resolvable with a few prospect calls

| # | Question | Why it matters | How to settle it |
|---|---|---|---|
| Q-1 | Does careCycle's *"member-aware call handling with plan/benefit context"* cover pre-sale benefit Q&A, or only post-enrolment member servicing? | Determines whether our plan-knowledge lead is wide or narrow — the core of the entire positioning | Call careCycle as a prospect; ask whether a non-member caller can get a dental allowance answered |
| Q-2 | Do careCycle and Coverage Voice answer in *the agency's* name or their own? | Settles feature 16 (agency-branded voice agent), currently scored −3.6 here and positive by two other passes | Call both as a prospect and listen to the greeting |
| Q-3 | Do we actually do **provider lookup**, **consent capture**, and **accessibility-oriented design for older adults**? | A third-party research pass attributes all three to us; none appear in the source feature sheet, and F15 provider lookup is marked absent for us while two competitors have it | Confirm against the product before any of the three appears in external material |

---

*Close a finding by moving it to a "Resolved" section with the date and what changed — do
not delete it. When a finding is applied to the scores, update `feature-scores.csv`, remove
any inline flag on the affected row, and move the finding to Resolved.*
