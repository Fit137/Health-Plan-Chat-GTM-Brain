# Feature matrix — what leads and what is entry cost

*Load this when deciding what a piece of copy should lead with, or when someone proposes
leading on a capability. Distils `sources/extracted/product-feature-matrix.md` and
`feature-scores.csv`.*

## The scoring

25 features, each scored −20 to +20 on **demand** (how much the market wants it) and
**competitiveness** (how differentiated we are on it). Thresholds are explicit: high
demand ≥ +10.0, high differentiation ≥ +5.0. That gives four quadrants:

| | High differentiation | Low differentiation |
|---|---|---|
| **High demand** | **Q1 — lead here** (6) | Q2 — table stakes (13) |
| **Low demand** | Q3 — niche (2) | Q4 — ignore (4) |

## The three layers

Every feature also sits in one of three layers, which is a statement about who else can
build it:

- **L1 Commodity AI** (14 features) — any voice-AI vendor has this. A $79/month AI
  receptionist has this.
- **L2 Insurance Workflow** (5) — requires insurance domain knowledge, not Medicare
  specifically.
- **L3 Medicare Plan IP** (6) — requires ingesting and reasoning over a specific agency's
  carrier documents.

## The finding everything rests on

The layer and the quadrant turn out to be the same fact:

```
               Q1  Q2  Q3  Q4
  L1 Commodity  0  10   0   4
  L2 Workflow   0   3   2   0
  L3 Plan IP    6   0   0   0
```

**All six Q1 differentiators are L3. Zero of fourteen L1 features reach Q1.**

Two independent methods — scoring features on demand and differentiation, and classifying
them by what it takes to build them — produce the same six features. That agreement is
why this is the spine of the strategy rather than one input to it.

## What this means for copy

**Lead with the L3 six.** Plan-grounded benefit Q&A, supplemental benefits, premium and
copay for a named plan, cross-plan comparison, plan-year and county awareness, answer
traced to source.

**Never lead with an L1 feature.** 24/7 answering, natural voice, call transfer, CRM
delivery, multilingual: all real, all shipped, all things the reader can buy for $79 a
month elsewhere. They belong in a feature table, never in a headline.

**Q2 is entry cost.** Thirteen features that the market demands and everyone has. Not
having them loses deals; having them wins nothing. Write about them factually and briefly.

**Score against the real price floor.** If a $79/month AI receptionist does it, the honest
band is "commodity: should be free". Scoring a commodity feature as a differentiator
because it is well-built is how a positioning drifts.

## The two urgent gaps

Both sit in Q2, both are ROADMAP, both are in the same handoff sequence:

- **Appointment booking** — +14.1 demand. Both direct competitors ship it.
- **SOA capture** — a hard CMS requirement for a TPMO. Coverage Voice captures it in-call.

## One score is known to be wrong

Feature 25, *centralised deployment across agencies and downlines*, carries +17.4
competitiveness in `feature-scores.csv` — scored on the explicit basis that nobody else
offered it. That basis is false; see OF-2. The score should be roughly +6 to +8. It stays
in Q3 as a niche play, not a moat. The row is flagged inline and the finding stays open
until the founder applies it.

Do not quote the +17.4 figure. Do not describe multi-agency deployment as unique.
