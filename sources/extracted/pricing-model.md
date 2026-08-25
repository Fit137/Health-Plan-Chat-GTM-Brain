# Health Plan Chat Pricing

Plan-grounded Medicare voice and chat, priced for the independent agency that careCycle's price floor leaves unserved. Three tiers, a flat platform fee for predictability, and metered conversations above the included allowance so revenue scales with the value delivered.

Built with the saas-pricing-model-builder skill. Companion workbook: `gtm/pricing-model.xlsx`, nine tabs, every input editable from a single Control Panel. This file is the design and landing-page handoff.

---

## 1. Strategic rationale

Health Plan Chat sits at MVP to early PMF. No paying cohort exists yet, so this price is a learning instrument, not a yield instrument, and it should be revised the moment design partner conversion and usage data arrive.

The beachhead is ICP-1: independent Medicare agencies with 3 to 10 licensed agents and 400,000 to 2,500,000 dollars in annual commission revenue. It is easy to service, because the buyer is a single owner-operator who decides without a committee, without procurement and without a security review. Current share is zero. The only competitor with comparable Medicare depth, careCycle, prices a 5 to 10 agent operation at roughly 10,000 dollars a month per `OPEN-FINDINGS.md` OF-1, which means it does not compete for this segment at all. Coverage Voice competes on eligibility and prescreening rather than plan-specific benefit answers. The segment is unserved rather than contested.

The motion is marketing and service led for Front Desk and Plan Fluent. Buyers self-qualify through the Readiness Scorecard and the Benefit Answer Gap Report, then convert on a 72-hour sandbox. Plan document ingestion and CMS obligations need hand-holding, so this is not pure self-serve. Downline is sales led and priced Contact sales, because it requires a compliance review and a phased rollout.

### Why this denominator

Price is charged per agency location per month, not per seat and not purely per minute.

Per seat was rejected because the value, always-on plan-grounded coverage, is shared across the whole office and does not scale with headcount. A three-agent agency with heavy inbound gets more value than a ten-agent agency with none.

Pure per-minute was rejected because unpredictable bills are the single loudest complaint against Smith.ai in the competitive research, severe enough to have produced a BBB failure-to-respond rating. The whole positioning commits to published, predictable pricing.

What is left is a hybrid, and it is the right answer rather than a compromise: a flat platform fee carries the predictability, an included conversation allowance covers normal use, and metered conversations above it let revenue follow value. A monthly cap keeps the metered part from ever producing a frightening invoice.

---

## 2. The scalable usage vehicle

A conversation is one answered voice call or one chat session. That is the meter: it is legible to an agency owner in a way that minutes are not, and it maps to the thing being bought, which is an answered question.

| Element | How it works | Why |
|---|---|---|
| **Platform fee** | Flat, monthly, per agency location | The predictability the positioning promises. Charged whether or not the allowance is used. |
| **Included allowance** | A conversation budget bundled into the fee | Covers normal months entirely, so most agencies never see a variable line at all. |
| **Declining overage bands** | Rate falls as volume rises: $1.45, then $1.15, then $0.95, then $0.80 | AEP triples call volume for six weeks. A flat overage rate would punish an agency for its best season. |
| **Surge cap** | Overage cannot exceed 1.5x the platform fee in any month | The direct answer to the billing-surprise objection. The worst possible invoice is knowable in advance. |
| **Prepaid commit** | 10% off overage rates when volume is committed up front | Converts variable revenue into predictable revenue for both sides. |
| **Annual billing** | 15% off the platform fee | Standard, and it pulls cash forward at the stage that needs it. |

### Rate card

| | Front Desk | **Plan Fluent** | Downline |
|---|---|---|---|
| Role | Decoy | **Hero** | Anchor |
| Platform fee, monthly | $199 | **$499** | Contact sales, from $1,499 |
| Platform fee, annual (per mo.) | $169 | **$424** | Custom |
| Conversations included | 65 | **220** | 750 |
| Effective rate inside allowance | $3.06 | **$2.27** | $2.00 |
| Monthly overage ceiling | $299 | **$749** | Custom |
| **Worst-case monthly bill** | **$498** | **$1,248** | Custom |

Overage bands, applied above the allowance:

| Band | Conversations over allowance | Rate each | With prepaid commit |
|---|---|---|---|
| Band 1 | first 250 | $1.45 | $1.31 |
| Band 2 | next 750 | $1.15 | $1.04 |
| Band 3 | next 2,000 | $0.95 | $0.86 |
| Band 4 | beyond that | $0.80 | $0.72 |

The worst-case row is the number to put in front of a nervous buyer. It is the entire point of the surge cap.

---

## 3. How the price was set

Bottom-up, in three layers. Full math with live formulas is on the Bottom-Up Model tab.

**Cost floor.** A conversation costs about **$0.54** to serve: 3.5 minutes at $0.14 blended per minute for LLM, speech and telephony, plus $0.05 for recording, storage and the CMS ten-year retention obligation. Fixed cost is about **$43** per account per month for support, third-party services and allocated overhead. At an expected 180 conversations a month, cost to serve is **$140**, and at a 70% target gross margin the floor is **$467**.

**Market band.** Normalised to per agency per month: Synthflow around $66 estimated from its published per-minute rate, Goodcall Scale at $249, Smith.ai Basic at $600, careCycle at $10,000. Low $66, median $424, high $10,000. That 150x spread is itself the finding. The category has no middle, and the middle is exactly where a 3 to 10 agent agency lives.

**Value ceiling.** Two incremental enrollments a month at the 2026 CMS initial commission of $694 is $16,656 a year in new commission. Capturing 15% of that puts the ceiling at **$208 a month**. This sits below the floor, which is expected at MVP and is stated plainly rather than hidden: the value case is built on unconfirmed enrollment assumptions, so price currently leans on cost and market, not value. When design partner outcome data lands, this is the number that should move, and it is the one that justifies raising price.

**The Hero.** $499 a month. It clears the $467 floor at expected usage, sits above the commodity AI-receptionist band where the plan-intelligence differentiators justify a premium, and lands **20x below careCycle**, which is the OF-1 wedge expressed as a number.

### One honest tension, stated rather than buried

At the full 220-conversation allowance the gross margin is **67.6%**, slightly under the 70% target. Holding a generic 80% software margin would require cutting the allowance to about **105 conversations**, which would push a typical agency into overage every single month and break the predictability the whole position rests on.

That trade is deliberate. Voice AI carries genuine variable COGS, so it does not behave like pure software, and roughly 68% at the cap is healthy for this category. The Control Panel exposes both the target margin and the reference volume, so this assumption can be challenged directly rather than taken on trust.

---

## 4. Packaging

Tiers were built from the feature matrix, not chosen first. All six differentiators are the L3 Medicare plan-IP layer, and no commodity feature reaches the differentiator zone, so the Hero is built on plan intelligence and nothing else.

- **Front Desk (Decoy)** carries the 16 table-stakes features. Its job is to make Plan Fluent the obvious choice and to lower friction to a first conversation. It is not designed to be a destination.
- **Plan Fluent (Hero)** adds the six plan-intelligence differentiators. Target 60 to 80% of ICP-1 customers here.
- **Downline (Anchor)** adds the two niche features and custom terms. It anchors price high and captures FMO willingness to pay.

### Feature comparison

| | Front Desk | **Plan Fluent** | Downline |
|---|:---:|:---:|:---:|
| **Always-on answering** | | | |
| 24/7 call answering, day and night | Yes | **Yes** | Yes |
| Handles every call at once, even during AEP | Yes | **Yes** | Yes |
| Warm transfer to your licensed agents, with full context | Yes | **Yes** | Yes |
| After-hours lead capture | Yes | **Yes** | Yes |
| **Getting the lead ready** | | | |
| Lead qualification before handoff | Yes | **Yes** | Yes |
| Call transcripts and summaries | Yes | **Yes** | Yes |
| Structured lead records | Yes | **Yes** | Yes |
| CRM sync | Yes | **Yes** | Yes |
| **Your brand, your voice** | | | |
| Agency-branded voice | Yes | **Yes** | Yes |
| Agency-branded chat widget on your site | Yes | **Yes** | Yes |
| Custom knowledge base (hours, policies, FAQs) | Yes | **Yes** | Yes |
| Multilingual, including Spanish | Yes | **Yes** | Yes |
| **Operations** | | | |
| Call analytics dashboard | Yes | **Yes** | Yes |
| Appointment and callback scheduling | soon | **soon** | soon |
| **Plan intelligence** | | | |
| Answers Medicare plan-specific questions | | **Yes** | Yes |
| Reads and understands your plan documents | | **Yes** | Yes |
| Dental, vision, hearing, transportation, OTC and flex answers | | **Yes** | Yes |
| Premium, copay and cost-sharing answers | | **Yes** | Yes |
| Compares benefits across the plans you sell | | **Yes** | Yes |
| Trained on your agency's specific book of plans | | **Yes** | Yes |
| **Scale across locations** | | | |
| Full website, chat and voice package | | | Yes |
| Centralised deployment across your downline | | | soon |

Yes = included and shipped today. soon = on the roadmap, not yet shipped.

**Downline deployment must not be marketed as unique.** Per `OPEN-FINDINGS.md` OF-2, Coverage Voice already ships multi-agency sub-accounts, white labelled, live in 48 hours. Sell plan grounding across the downline, not the multi-tenancy.

A standalone website chatbot is excluded from the table. It scores low demand and commodity density in the feature matrix, and the capability is already covered by the branded chat widget row.

---

## 5. What the model says when you run it

Four agency profiles across a full year, with AEP at 15 October to 7 December driving volume to 2.4x baseline in November. Detail is on the Scenario Model tab.

| Profile | Tier | Year revenue | Year cost | Gross margin | Surge cap hit |
|---|---|---|---|---|---|
| Small agency, 60 conv./mo baseline | Front Desk | $2,616 | $963 | 63.2% | never |
| Typical agency, 180 conv./mo | Plan Fluent | $6,545 | $1,857 | 71.6% | never |
| Heavy agency, 420 conv./mo | Plan Fluent | $10,020 | $3,646 | 63.6% | November |
| Same heavy agency | Downline | $18,368 | $3,646 | 80.2% | never |

The last two rows are the same agency on two different tiers, and the contrast is the upgrade conversation in numbers. On Plan Fluent a heavy agency hits the surge cap in November and margin falls to 52.9% that month, because the cap protects the buyer at our expense. The same November usage on Downline returns 68.6% and never touches a cap. **The point at which a tier's margin crosses the floor is the upgrade trigger, and the model computes it rather than leaving it to instinct.**

---

## 6. Using the workbook

`gtm/pricing-model.xlsx`, nine tabs. Every input lives on the Control Panel; the other eight tabs are formulas that read from it.

| Tab | What it is for |
|---|---|
| **Control Panel** | The only tab with editable inputs. Costs, tier prices, allowances, overage bands, guardrails, and a live margin readout at four utilisation levels. |
| Strategy | The Phase 1 and 2 decisions with rationale. |
| Feature Matrix | All 25 capabilities scored, zoned and assigned to a tier. |
| Bottom-Up Model | Floor, market band, value ceiling, Hero price, and floor sensitivity by volume. |
| Usage Rate Card | The usage vehicle as a customer would see it, including the worst-case bill. |
| Unit Economics | Revenue, cost and margin for one account from 0 to 1,600 conversations, colour scaled. |
| Scenario Model | Four profiles across 12 months with AEP seasonality. |
| Sensitivity | Margin grid: platform fee against real usage. |
| Pricing Table | The customer-facing table with the full feature grid. |

**Colour code.** Blue cells are editable inputs. White cells are formulas. Green cells are key outputs. Amber cells are assumptions that need confirming. Red fill anywhere means gross margin has fallen below the floor set in Control Panel B52.

**Three experiments worth running first.**

1. Set the target gross margin to 80% and watch the floor jump past the Hero price. The model is telling you the allowance would have to fall to about 105 conversations.
2. Raise the surge cap from 1.5x to 3x and watch the heavy-agency November margin recover. That is the trade between protecting the buyer and protecting revenue, priced.
3. Push cost per minute from $0.14 to $0.20 and see which tiers go red. That is the exposure if inference or telephony costs move against us.

---

## 7. Notes for design

- Highlight Plan Fluent. Target 60 to 80% of customers there. If most land on Front Desk instead, the Hero is overpriced or underbuilt, not the segment being poor.
- Front Desk exists to make Plan Fluent obvious. Do not let it compete for attention on the page.
- Downline has no self-serve price. Design its card around Contact sales with the starting figure as a reference, not a clickable price, and route its CTA to a pilot request rather than a checkout.
- Show the worst-case monthly bill on the pricing page, not just the platform fee. In a category where the loudest complaint is surprise invoices, publishing the ceiling is a differentiator rather than a disclosure.
- Billing toggle defaults to monthly. Show annual as a percentage saved, not just a lower number.
- The two roadmap rows must not render as plain checkmarks. If either ships before this goes live, update this file and the workbook in the same change.

---

## 8. Assumptions to confirm before this is published

| Assumption | Current value | Why it matters |
|---|---|---|
| Cost per minute, all-in | $0.14 | The single most load-bearing input. Every margin in the model moves with it. |
| Average minutes per conversation | 3.5 | Cost scales on minutes while price is metered on conversations, so long calls compress margin. |
| Fixed cost per account per month | $43 | Estimated, not measured. Dominates unit economics at the Front Desk tier. |
| Incremental enrollments per month | 2 (base case) | Unconfirmed. This is the number design partner data should replace first, and the one that justifies a price rise. |
| Typical agency conversation volume | 180/month | Sets the floor. If real usage runs higher, the floor rises and $499 gets tight. |
| Competitor prices | Synthflow and careCycle estimated | Synthflow has no flat published price; careCycle is third-party sourced. Coverage Voice publishes tiers but no figures were found, so it is not in the numeric band. |

Every one of these is a blue cell on the Control Panel. Change it and the whole model moves.

**Status of OF-1.** A proposed price now exists with the math behind it. The finding stays open until the founder reviews these assumptions, confirms or adjusts the number, and it is actually published.
