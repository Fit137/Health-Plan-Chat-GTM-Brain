# Signal log

Raw market input and what was done about it. **Log verbatim, triage separately.** The
value of this file is that it holds what was actually said, not what we concluded.

Newest first.

## How to log

| Field | Rule |
|---|---|
| **Date** | When it was heard, not when it was logged |
| **Source** | Who, their role, their company type, and the context |
| **Verbatim** | Their words. Do not clean them up |
| **Type** | Objection · Competitor move · Pricing · Feature request · Churn reason · Win reason · Compliance |
| **Disposition** | Logged only · Corroborates [ref] · Routed to [ledger] · Escalated |

## Corroboration thresholds

A single signal changes nothing. Thresholds agreed with the founder:

| Signal type | Threshold to act |
|---|---|
| Objection | **3 independent** occurrences → add to `reference/objection-handling.md` |
| Feature request | **3 independent**, or **1 from a lost deal** → raise with product |
| Competitor claim | **1**, if verifiable on their own published material → straight to `rules/do-not-say.md` |
| Pricing pushback | **2** → route to OF-1 |
| Compliance concern | **1** → immediate, no threshold |

Compliance has no threshold because the cost of being wrong is not symmetric.

## Review cadence

Triage weekly during the selling window (February to mid-September). Fortnightly during
AEP, when volume is low and attention is elsewhere. See `ops/review-cadence.md`.

---

## Log

*No signals logged yet. The brain was built 2026-08-25 from Sprint 1 research; market
contact begins with the first design partner outreach.*

*Seed entries below are findings from the build itself, recorded here so the first real
signals have something to corroborate against.*

---

### 2026-08-24 · Coverage Voice ships multi-agency sub-accounts

- **Source.** Coverage Voice TPA/BPO page, own published material.
- **Verbatim.** "Manage sub-accounts across multiple agencies", white-labelled under the
  customer's own brand and domain, live in 48 hours.
- **Type.** Competitor move.
- **Disposition.** **Routed to `rules/do-not-say.md`** and `ops/decisions.md`. Falsifies
  the uniqueness basis for feature 25's +17.4 score. Threshold met at one occurrence
  because it is verifiable on their own material. Score correction still pending in
  `feature-scores.csv`.

### 2026-08-24 · Coverage Voice captures SOA in-call

- **Source.** Coverage Voice Medicare enrollment feature page.
- **Type.** Competitor move / compliance.
- **Disposition.** **Escalated.** SOA is a hard CMS requirement for a TPMO, not a
  convenience feature, and it sits exactly where we hand off. Routed to
  `rules/feature-status.md` as ROADMAP and to product for pre-AEP scoping.

### 2026-08-24 · careCycle entry pricing ~$10,000/month

- **Source.** Third-party pricing analysis. careCycle publishes no pricing.
- **Type.** Pricing.
- **Disposition.** **Routed to `ops/decisions.md`** as the basis of the pricing-wedge
  verdict. Confidence medium-high. **Needs one prospect call to confirm** before it
  appears in any external material.

### 2026-08-24 · Three Medicare-native vendors have zero G2 or Capterra presence

- **Source.** Direct search of both platforms during the competitive analysis.
- **Type.** Competitor move.
- **Disposition.** **Logged, and routed to `reference/competitive-analysis.md`** as a
  standing method note. Two readings, both worth holding: the scoring is not
  like-for-like, and the buyers in this segment are not on review sites — which is itself
  a channel finding that shaped `reference/outbound-engine.md`.

---

## What to watch for first

The signals most likely to change something, ranked by how much:

1. **Any prospect answer to Q-1** (does careCycle do pre-sale benefit Q&A). Touches the
   core positioning claim.
2. **Any pricing pushback at $499**, once published. Two occurrences reopens OF-1.
3. **Any lost deal citing appointment booking or SOA.** One from a lost deal meets the
   threshold and moves the roadmap.
4. **Any onboarding that runs past five business days.** The deployment-speed gate is the
   binding constraint on the whole strategy; the first slip is the signal that it is real.
