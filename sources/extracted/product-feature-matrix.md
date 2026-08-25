# Health Plan Chat — Product Feature Matrix & GTM Demand Drivers
**Sprint 1 · August 2026 · canonical text deliverable**

> Visual treatment is deliberately out of scope here — this document and
> `feature-scores.csv` are the handoff for Claude Design. The HTML page in this
> folder (`product-feature-matrix.html`) is a frozen v1 snapshot; where it
> disagrees with this file, **this file wins**. See §8 for what changed.

---

## 1. The three-layer read (primary framing)

The feature sheet is best read as three stacked layers rather than one flat list.
This framing came from the founder's ChatGPT pass and it is correct — so it is now
the spine of this document rather than an appendix to it.

| Layer | What it is | Features | Defensibility |
|---|---|---|---|
| **L1 — Commodity AI** | Voice, transcription, transfers, scheduling, CRM, dashboards, branding, embedding | 14 of 25 | None. Priced at $79–$130/mo by general AI receptionists. |
| **L2 — Insurance workflow** | Lead qualification, after-hours servicing, agency handoff, downline structure | 5 of 25 | Thin alone. Real when fused with L3. |
| **L3 — Medicare plan IP** | Plan-specific benefit Q&A, plan-document comprehension, multi-plan knowledge, structured Medicare content | 6 of 25 | The only genuinely defensible layer. |

### The scoring validates the framing exactly

The layers were assigned from the ChatGPT framing; the scores were assigned
independently from competitor research. They land on top of each other:

| Layer | Q1 Differentiator | Q2 Table Stakes | Q3 Niche/Bet | Q4 Hygiene |
|---|---|---|---|---|
| L1 Commodity AI | **0** | 10 | 0 | 4 |
| L2 Insurance workflow | **0** | 3 | 2 | 0 |
| L3 Medicare plan IP | **6** | 0 | 0 | 0 |

**Every feature in Q1 is an L3 feature. No L1 feature reaches Q1 — not one of the
fourteen.** Two independent methods agreeing this cleanly is the strongest signal
in this analysis.

**The pitch that follows from it:** "we have an AI voice agent" is L1 — a sentence
any of five vendors can say for $79/month. "We have an AI agent that already
understands the Medicare plans you sell" is L3, and it is the only sentence on this
sheet a competitor cannot currently repeat. Everything in §7 is built to make a
prospect discover that distinction themselves.

### One refinement worth spending time on

L3 is the story, but it is not automatically the moat. Plan-document parsing is
already replicable — MedicareCopilot (ConnectureDRX + HealthcareGPS, launched April
2026) runs NLP over Summary of Benefits and Evidence of Coverage documents today.
What is *not* replicable quickly is **L2 fused with L3**: Medicare-specific
qualification logic running on plan-grounded knowledge, deployed across an FMO's
downline. Feature 15 (AI trained on your agency and the plans you sell) scores the
highest competitiveness on the board, +17.1, for exactly that reason — it is
per-customer data work, not a model capability.

Sell L3. Build the L2×L3 fusion, because that is what stays defensible in eighteen
months when document parsing is commodity.

---

## 2. Method

Both axes run −20 to +20.

| Demand band | Score | Competitiveness band | Score |
|---|---|---|---|
| Wanted by all | +14.0 to +19.5 | Unique to us | +11.0 to +20.0 |
| Wanted by most | +4.0 to +13.5 | A few others can do this | +1.0 to +10.0 |
| Wanted by some | −9.0 to −1.0 | Most vendors can do this | −10.0 to −1.0 |
| Wanted by one | −20.0 to −10.0 | Commodity: should be free | −20.0 to −11.0 |

**Quadrant thresholds (explicit):** high demand ≥ **+10.0**, high differentiation ≥ **+5.0**.

- **Q1 Strategic Differentiator** — high demand, high differentiation. Lead the story.
- **Q2 Table Stakes** — high demand, low differentiation. Must work; wins nothing.
- **Q3 Niche / Strategic Bet** — low demand, high differentiation. Segment plays.
- **Q4 Supporting / Hygiene** — low demand, low differentiation. Minimum viable.

### Competitive set

| # | Competitor | Constraint it imposes |
|---|---|---|
| 1 | **careCycle** | Closest direct threat. Medicare-native voice AI, YC-backed, $2M raised. Owns pre-screening and context-carrying warm transfer. |
| 2 | **Coverage Voice** | Sets commercial expectations: published pricing, <48hr deploy, no lock-in, Salesforce/HubSpot/Zoho standard. |
| 3 | **MedicareCopilot** (ConnectureDRX + HealthcareGPS) | Already does NLP over plan documents — but agent-facing, inside an appointment. No consumer voice surface. That gap is our moat. |
| 4 | **Horizontal voice AI** (Synthflow, Retell, Vapi, Goodcall, Smith.ai) | The price floor: $79–$130/mo, or $0.11–$0.24/min. Synthflow white-labels voice agents out of the box. |
| 5 | **SunFire Matrix / MedicareCENTER** (Integrity) | The free-alternative bar. Plan data from 110 carriers, side-by-side comparison, call recording — free to agents. |

Adjacent, not scored: Rivvi (payer/provider, ~$100K/yr entry), eHealth and Fair Square (national brokers building in-house).

---

## 3. Product feature matrix — qualitative

| # | Feature | Layer | Demand | Competitiveness | vs. sheet |
|---|---|---|---|---|---|
| 1 | 24/7 AI voice answering for inbound calls | L1 | Wanted by All | Commodity: should be free | adjusted |
| 2 | Natural conversational voice interaction | L1 | Wanted by All | Commodity: should be free | adjusted |
| 3 | AI chatbot for website/portal | L1 | Wanted by Some | Commodity: should be free | adjusted |
| 4 | Handles multiple calls simultaneously | L1 | Wanted by Most | Commodity: should be free | adjusted |
| 5 | Warm transfer/escalation to human agent | L1 | Wanted by All | Most vendors can do this | — |
| 6 | After-hours lead capture | L2 | Wanted by All | Commodity: should be free | adjusted |
| 7 | Lead qualification before agent handoff | L2 | Wanted by Most | Most vendors can do this | — |
| 8 | Call transcription & conversation summaries | L1 | Wanted by Most | Most vendors can do this | — |
| 9 | Structured caller information captured for agent | L2 | Wanted by Most | Most vendors can do this | — |
| 10 | Answers Medicare plan-specific questions | **L3** | Wanted by All | Unique to us | — |
| 11 | Understands plan benefits from plan documents | **L3** | Wanted by All | Unique to us | softened |
| 12 | Answers benefits: dental, vision, hearing, transportation, OTC/flex | **L3** | Wanted by All | Unique to us | — |
| 13 | Plan-specific premium/copay/cost-sharing questions | **L3** | Wanted by All | Unique to us | — |
| 14 | Compare benefits across Medicare plans | **L3** | Wanted by Most | A few others can do this | adjusted |
| 15 | AI trained on your agency and the Medicare plans you sell | **L3** | Wanted by Most | Unique to us | — |
| 16 | Agency-branded AI voice agent | L1 | Wanted by Most | Most vendors can do this | adjusted |
| 17 | Agency-branded AI chatbot | L1 | Wanted by Most | Most vendors can do this | adjusted |
| 18 | Embed chatbot into agency's existing website | L1 | Wanted by Most | Commodity: should be free | adjusted |
| 19 | Complete website + chat + voice package for small agencies | L2 | Wanted by Some | A few others can do this | — |
| 20 | CRM integration / lead handoff | L1 | Wanted by Most | Most vendors can do this | — |
| 21 | Call analytics/dashboard | L1 | Wanted by Most | Commodity: should be free | adjusted |
| 22 | Multilingual support | L1 | Wanted by Most | Most vendors can do this | — |
| 23 | Custom agency knowledge base | L1 | Wanted by Most | Most vendors can do this | — |
| 24 | Appointment/callback scheduling *(Coming Soon)* | L1 | Wanted by Most | Most vendors can do this | — |
| 25 | Centralized deployment across agencies/downlines *(Coming Soon)* | L2 | Wanted by Some/FMO | Unique to us | adjusted |

---

## 4. Table A — scores

Sorted by demand. Both values are plot coordinates.

| # | Feature | Layer | Demand | Competitiveness | Quadrant |
|---|---|---|---:|---:|---|
| 12 | Answers benefits: dental, vision, hearing, transportation, OTC/flex | L3 | +19.4 | +15.9 | Q1 |
| 10 | Answers Medicare plan-specific questions | L3 | +19.2 | +14.6 | Q1 |
| 1 | 24/7 AI voice answering for inbound calls | L1 | +18.6 | −14.2 | Q2 |
| 5 | Warm transfer/escalation to human agent | L1 | +18.2 | −8.4 | Q2 |
| 2 | Natural conversational voice interaction | L1 | +17.8 | −12.7 | Q2 |
| 13 | Plan-specific premium/copay/cost-sharing questions | L3 | +17.6 | +13.4 | Q1 |
| 6 | After-hours lead capture | L2 | +17.4 | −10.6 | Q2 |
| 11 | Understands plan benefits from plan documents | L3 | +16.3 | +11.7 | Q1 |
| 20 | CRM integration / lead handoff | L1 | +15.8 | −8.9 | Q2 |
| 7 | Lead qualification before agent handoff | L2 | +14.9 | −6.2 | Q2 |
| 24 | Appointment/callback scheduling | L1 | +14.1 | −9.2 | Q2 |
| 15 | AI trained on your agency and the Medicare plans you sell | L3 | +13.7 | +17.1 | Q1 |
| 14 | Compare benefits across Medicare plans | L3 | +12.8 | +6.9 | Q1 |
| 8 | Call transcription & conversation summaries | L1 | +12.3 | −9.7 | Q2 |
| 22 | Multilingual support | L1 | +11.9 | −4.7 | Q2 |
| 4 | Handles multiple calls simultaneously | L1 | +11.6 | −13.1 | Q2 |
| 9 | Structured caller information captured for agent | L2 | +11.4 | −5.8 | Q2 |
| 23 | Custom agency knowledge base | L1 | +10.8 | −2.4 | Q2 |
| 16 | Agency-branded AI voice agent | L1 | +10.4 | −3.6 | Q2 |
| 18 | Embed chatbot into agency's existing website | L1 | +9.6 | −10.9 | Q4 |
| 21 | Call analytics/dashboard | L1 | +9.3 | −12.6 | Q4 |
| 17 | Agency-branded AI chatbot | L1 | +8.7 | −7.3 | Q4 |
| 3 | AI chatbot for website/portal | L1 | −3.7 | −15.4 | Q4 |
| 19 | Complete website + chat + voice package for small agencies | L2 | −5.2 | +8.2 | Q3 |
| 25 | Centralized deployment across agencies/downlines | L2 | −8.6 | +17.4 | Q3 |

Demand range −8.6 to +19.4 · competitiveness range −15.4 to +17.4.

---

## 5. Table B — quadrant and rationale

### Q1 — Strategic Differentiator (6) · all L3

| # | Feature | Rationale |
|---|---|---|
| 15 | AI trained on your agency and the plans you sell | **Highest competitiveness on the board (+17.1).** Not because the technology is hard, but because it is per-customer data work — the agency's own book, carriers and plans. Slow to copy and it compounds monthly. Demand sits a band lower because buyers ask for the outcome, not the mechanism. Sell the outcome, price the moat. |
| 12 | Benefits: dental, vision, hearing, transportation, OTC/flex | **The sharpest wedge and highest demand (+19.4).** Supplemental benefits, especially the OTC/flex allowance, are the most-asked question and the primary marketing hook of every MA plan. Impossible to bluff — the answer must come from that plan's documents. This is the demo. |
| 10 | Answers Medicare plan-specific questions | The reason the phone rings at all. careCycle and Coverage Voice capture and qualify but do not answer; MedicareCopilot answers only to the agent. Consumer-facing plan answers are genuinely ours. |
| 13 | Plan-specific premium/copay/cost-sharing | Cost is the second question after benefits. Also our highest-liability answer — a wrong copay is a complaint and potentially a CMS issue. Document-grounded sourcing is what makes it sellable rather than reckless. Scored under 12 for that risk load. |
| 11 | Understands plan benefits from plan documents | **Softened, not downgraded.** MedicareCopilot already runs NLP over Summary of Benefits and Evidence of Coverage docs — a single SB runs 50+ pages. Stays in the unique band only because we point it at a consumer over voice. Treat the capability as rare and the *channel* as the moat. |
| 14 | Compare benefits across Medicare plans | **Downgraded hardest.** SunFire and MedicareCENTER give agents free side-by-side comparison; Medicare Plan Finder gives it to consumers free and adds provider network data for 2026; MedicareCopilot ranks plans on 12 weighted factors. Also edges toward steering, which a TPMO must handle carefully. Keep, guard, do not headline. |

### Q2 — Table Stakes (13) · high demand, no differentiation

| # | Feature | Rationale |
|---|---|---|
| 1 | 24/7 AI voice answering | Universal need — the five-minute lead window is the agency's economics. Every AI receptionist does it for $79/mo. Price of entry, not a capability. |
| 5 | Warm transfer/escalation | Demand near-maximum and partly regulatory: CMS expects plan-specific guidance from a licensed agent, so escalation is a compliance control. careCycle already markets context-carrying transfer. |
| 2 | Natural conversational voice | Non-negotiable for a senior caller; an IVR tree loses the call. Fully commoditised — ElevenLabs-grade voices ship by default in Synthflow, Retell and Vapi. |
| 6 | After-hours lead capture | Strongest evidence on the sheet: Fair Square reports **4× conversion** on after-hours calls handled by AI. Universally wanted, universally available. The L2 workflow around it (routing to the right licensed agent) is worth more than the capture. |
| 20 | CRM integration / lead handoff | Scored above lead qualification: a qualified lead that never lands in the CRM is a lost lead. Coverage Voice ships Salesforce/HubSpot/Zoho standard. Deal-breaker in the negative sense only. |
| 7 | Lead qualification before handoff | Agents drown in unqualified AEP volume, and weak discovery drives bad plan fit → complaints and disenrollment. Both direct competitors lead with pre-screening. **Becomes defensible only when fused with L3 plan logic** — that fusion is the roadmap. |
| 24 | Appointment/callback scheduling | **The urgent gap.** Demand outscores several shipped features — the booked appointment is the conversion event — and both direct competitors already book into the CRM. Wins nothing when shipped; loses deals until it is. Ship before AEP. |
| 8 | Call transcription & summaries | Adjacent to a real obligation: CMS requires sales calls recorded and retained **ten years**. Transcription is solved; the compliance packaging is worth more than the transcript. |
| 22 | Multilingual support | Underrated in aggregate, decisive in CA/TX/FL/AZ where Medicare-eligible Hispanic populations are large and agencies cannot staff bilingual teams. Synthflow offers 30+ languages, so capability is commodity — Spanish *grounded in the plan documents* is not. |
| 4 | Handles multiple calls simultaneously | Matters intensely for six weeks: AEP runs 15 Oct – 7 Dec. Concurrency is inherent to any AI voice stack, so no credit for it. |
| 9 | Structured caller information captured | The difference between a recording and a usable lead. Schema quality varies slightly; no competitor lacks it. |
| 23 | Custom agency knowledge base | "Upload your documents" is a default expectation now. Closest to the threshold of any Q2 feature because our corpus is structurally better — but that credit belongs to feature 15, not here. |
| 16 | Agency-branded AI voice agent | **Downgraded from "a few others."** Synthflow white-labels voice agents as standard at $0.11–0.24/min. Expected, not persuasive. *(Most contested cell — see §8.)* |

### Q3 — Niche / Strategic Bet (2)

| # | Feature | Rationale |
|---|---|---|
| 25 | Centralized deployment across agencies/downlines | **Upgraded from "potential differentiator" to unique.** Very few buyers — hence the lowest demand score — but each is worth many agencies, and nobody is doing multi-tenant, plan-grounded AI across an FMO downline. Goodcall does multi-location for generic receptionists; different problem. This is the land-and-expand engine and the clearest L2×L3 fusion play. **Superseded — see OF-2:** Coverage Voice markets multi-agency sub-accounts white-labelled in 48h, so this is not unique. Competitiveness should fall to ~+6 to +8; the FMO story rests on plan grounding across the downline, not multi-tenancy. |
| 19 | Complete website + chat + voice package | Most agencies already run an FMO-supplied site, so whole-market demand is low — but for the solo or newly-licensed agent it solves everything in one purchase. Few competitors bundle it because it is a services play. Give it its own pricing; never make it the core pitch. |

### Q4 — Supporting / Hygiene (4) · all L1

| # | Feature | Rationale |
|---|---|---|
| 18 | Embed chatbot into existing website | It is a script tag. Necessary for adoption — agencies will not rebuild a site to try us — but plumbing. |
| 21 | Call analytics/dashboard | Every voice platform ships one; most buyers open it twice. Real demand is for the weekly summary that proves ROI. Build the smallest thing that survives a renewal conversation. |
| 17 | Agency-branded AI chatbot | Chat branding is a colour picker. Lower demand than voice branding because the chat surface matters less to this audience. |
| 3 | AI chatbot for website/portal | Lowest on both axes. Beneficiaries phone; the adult child researching is real but secondary. Keep as a delivery surface for the plan brain — never sell it as a feature. |

---

## 6. What the map says

**1. Nineteen of twenty-five features are L1 or L2 in Q2/Q4.** Build them, never lead with them. Every minute of a sales call spent on 24/7 answering, voice quality, dashboards or branding is a minute argued on the axis where we are most replaceable, against someone cheaper.

**2. The moat is an intersection, not a feature.** Plan-document intelligence exists (MedicareCopilot). Consumer-facing 24/7 voice exists (careCycle, Coverage Voice). Nobody has both in one surface. The whole GTM rests on one sentence: *a beneficiary can ask what their dental allowance is at 9pm on a Sunday and get the answer from that agency's own plan documents.*

**3. Appointment scheduling is a live gap, not a roadmap item.** +14.1 demand, higher than several shipped features, and both direct competitors already close the loop. Ship before AEP.

**4. The compliance angle nobody on the list is selling.** CMS requires every marketing, sales and enrollment call recorded and retained ten years; the TPMO disclaimer must be read before plan benefits are discussed; a chatbot must disclose it is automated; plan-specific guidance requires a licensed agent — and CMS has issued **no AI-specific rules**, so the agency carries the liability for whatever its AI says. Our four highest-scoring differentiators are all "AI discusses plan benefits with a beneficiary" — simultaneously the most valuable and highest-liability thing we do. Grounding every answer in the carrier's own documents, with disclaimer and recording automatic, converts our biggest risk into the reason to buy us over a general-purpose bot.

---

## 7. Demand drivers

### Primary: The Benefit Answer Gap Report

Take an agency's published number, their website and the plans they sell. Ask both
channels the 25 benefit questions their beneficiaries actually ask — dental
allowance, OTC card balance, is my podiatrist covered, what is the specialist copay
— during business hours and again at 9pm on a Sunday. Return a scored report:
answered / unanswered / answered incorrectly, with time-to-answer, after-hours
reachability, and the transcripts attached.

| | |
|---|---|
| **What it is** | A free mystery-shop audit of the agency's own front door. 25 real beneficiary benefit questions against their live line and site, in and out of hours. |
| **Immediate value** | Something concrete about their own business in 48 hours, free, no product involved. Most owners have never heard their own after-hours experience. The transcripts need no interpretation. |
| **How it exposes the need** | The gap has a shape no substitute fits: **plan-specific, consumer-asked, answered in the moment.** Hiring does not fix 9pm. An answering service takes a message but cannot state a dental maximum. A $79 AI receptionist books a callback but has never read the plan. SunFire has the data but the beneficiary cannot log in. The problem statement is our product specification. |
| **ICP fit** | Dead-centre: independent agencies with a published number, a real site, 2–25 licensed agents. Self-qualifying — an agency with no inbound volume disqualifies itself for free. Scales upward: run it across an FMO downline and the aggregate report *is* the feature-25 pitch. |
| **Leverage** | Largely automatable with our own voice agent. Grading the answers means ingesting their plans — **the audit completes ~80% of onboarding before a contract exists.** Every plan corpus built is reusable across every agency selling that plan in that county. |
| **The closing number** | 2026 CMS compensation: **$694** per MA enrollment year one, **$347** per renewal year — a member who stays five years is **$2,082**. California: $864 / $432. The report converts unanswered calls into that arithmetic. |

### The portfolio — sliding scale

Both scales 0–10. Ease of delivery is inverted effort: 10 = fully self-serve, 1 = bespoke consulting.

| | Driver | Delivery mode | Value | Ease | Best for |
|---|---|---|---:|---:|---|
| D1 | Medicare AI Readiness Scorecard | Self-assessment | 4.2 | 9.4 | Top-of-funnel volume, list building, FMO newsletters |
| D2 | Missed-Call Revenue Calculator | Light tool, self-serve | 5.8 | 9.1 | Paid social/search landing pages, the ROI slide |
| D3 | **Benefit Answer Gap Report** | Light tool + assisted mystery shop | 8.6 | 6.7 | **Primary motion** — outbound to named agencies, FMO co-brand |
| D4 | 72-Hour Plan Brain Sandbox | Value from the software itself | 9.4 | 5.3 | Mid-funnel conversion; ends the evaluation |
| D5 | CMS AI Exposure Review | Service, light white glove | 8.1 | 4.6 | FMOs, compliance officers, agencies already running AI |
| D6 | AEP Peak-Load Stress Test | White glove | 9.1 | 2.4 | Enterprise/FMO only, in the 8 weeks before 15 Oct |

**D1 — Medicare AI Readiness Scorecard.** Twelve self-scored questions in ninety seconds: do you answer after hours, can your front desk state a plan's dental maximum, what happens to a Sunday call, who answers in Spanish. *Immediate value:* a number and a benchmark for an email address. *Exposes the need:* the questions **are** the argument — by the time someone answers "no" to "can a caller learn their OTC allowance without reaching a licensed agent?", the problem is self-diagnosed. *ICP:* broadest reach, weakest qualification. *Leverage:* build once, zero marginal cost, every completion is a segmented lead with a stated gap.

**D2 — Missed-Call Revenue Calculator.** Monthly inbound volume, rough % missed, state → annualised lost commission on published 2026 CMS rates. *Immediate value:* a vague annoyance becomes a dollar figure in fifteen seconds, computed from CMS's own schedule rather than vendor assumptions. *Exposes the need:* splits the loss into calls missed after hours and calls answered but unresolved because nobody could answer the plan question — that second bar is the one no receptionist or answering service reduces. *ICP:* filters by volume. *Leverage:* self-serve, shareable, and it becomes the ROI model sales uses later, pre-agreed by the buyer.

**D3 — Benefit Answer Gap Report.** Detailed above. **Recommended primary.**

**D4 — 72-Hour Plan Brain Sandbox.** They send the SB and EOC documents for the plans they sell; within 72 hours they get a private number and chat link, branded to their agency, trained on those exact plans. *Immediate value:* the strongest moment in the funnel — an owner asks their own hardest plan question and hears a correct, sourced answer in their agency's voice. *Exposes the need:* reframes the category. Having heard plan-grounded answers, a general AI receptionist is permanently disqualified; a price comparison becomes a capability comparison. *ICP:* highest intent only — handing over documents is the qualifying act. *Leverage:* delivery cost is real but falls as ingestion automates, and every corpus is reusable across every agency selling that plan.

**D5 — CMS AI Exposure Review.** Review whatever AI they already run against CMS obligations: is the TPMO disclaimer read before benefits are discussed, does the bot disclose it is automated, are sales calls recorded and retained ten years, is plan-specific guidance escalated to a licensed agent. *Immediate value:* a short findings memo naming specific exposures with specific remedies. *Exposes the need:* sharpest problem-identification play we have and nobody else is running it — CMS has issued no AI-specific rules, so the agency carries the liability. A general bot improvising a copay is the exposure; a document-grounded agent with disclaimer and recording built in is the remedy. *ICP:* larger agencies and FMOs. *Leverage:* checklist-driven, deliverable by a trained non-engineer, and it positions us as the category's standard-setter.

**D6 — AEP Peak-Load Stress Test.** Simulate AEP-peak concurrent volume against their current setup; report hold times, abandonment, concurrency ceiling, and which questions go unanswered under load. *Immediate value:* forecasts a specific, dated, six-week revenue event they already fear. *Exposes the need:* capacity failure and knowledge failure appear as separate lines — more staff fixes the first, only a plan-trained agent fixes the second, and they cannot hire their way out with eight weeks' notice. *ICP:* narrowest, largest contracts. *Leverage:* poor per engagement, excellent per dollar of contract value; the benchmark data sharpens every other driver.

---

## 8. Reconciliation with the other two passes

### Adopted from the Perplexity research
- **Explicit numeric quadrant thresholds** rather than implicit zero-crossings. Now stated in §2 (demand ≥ +10.0, differentiation ≥ +5.0) so any reader can re-derive every assignment.
- **"Supporting / Hygiene" as the Q4 name.** Better than "deprioritize" — analytics and chat branding are not things you drop, they are things you build to a minimum. This moved features 17, 18 and 21 out of Q2 into Q4.
- **"Moat emerges only when combined with Medicare-specific logic"** (their note on lead qualification). This is the L2×L3 fusion argument in §1, and it is the single most useful line in that pass.

### Where this analysis differs from Perplexity, and why
- **Commodity competitiveness scores.** Perplexity puts 24/7 answering at −6.9 and after-hours capture at −3.9; this analysis puts them at −14.2 and −10.6. The difference is the benchmark: Perplexity scored against AI vendors generally, this scores against the **$79–$130/month AI-receptionist price floor**. If a $79 tool does it, "should be free" is the honest band.
- **Coverage.** The Perplexity pass scored 10 of the 25 features and omitted feature 12 (dental/vision/hearing/transportation/OTC-flex) — which scores highest on demand here and is the single sharpest wedge on the sheet.

### The one genuinely contested cell — needs a decision
**Feature 16, agency-branded AI voice agent.** The source sheet says "a few others can do this"; Perplexity scores it +7.5; this analysis scores it **−3.6**, on the grounds that Synthflow white-labels voice agents as a standard capability.

Two of three passes score it as a differentiator, so treat this as open rather than settled. **The test that resolves it:** call careCycle and Coverage Voice as a prospect and ask whether the agent answers in *the agency's* name or theirs. If both do, −3.6 stands and branding is a checkbox. If neither does, it belongs near +6 and moves toward Q1. This is a two-hour piece of primary research and it is worth doing before pricing is set.

### Changes from the v1 HTML snapshot
1. Added the three-layer taxonomy as the primary framing (§1) and a `layer` column to `feature-scores.csv`.
2. Replaced implicit zero-line quadrant cuts with explicit thresholds; features 17, 18, 21 moved Q2 → Q4.
3. Renamed Q4 from "Deprioritize" to "Supporting / Hygiene."
4. Added §8. Scores themselves are unchanged.

---

## 9. Sources

careCycle [features](https://carecycle.ai/features/) · [funding](https://www.upstartsmedia.com/p/carecycle-startup-ai-voice-medicare) — Coverage Voice [pricing](https://coveragevoice.com/pricing) · [Medicare agent](https://coveragevoice.com/plan/medicare) — MedicareCopilot [plan intelligence](https://medicarecopilot.ai/ai-plan-intelligence) · [launch](https://finance.yahoo.com/sectors/healthcare/articles/connecturedrx-healthcaregps-launch-medicarecopilot-110000120.html) — SunFire [platform](https://www.psmbrokerage.com/sunfire-medicare-enrollment-platform) · [2026 Plan Finder](https://www.psmbrokerage.com/blog/cms-announces-enhancements-to-the-medicare-plan-finder) — [AI receptionist pricing](https://revsquared.ai/blog/ai-receptionist-pricing-comparison-every-platform) · [2026 comparison](https://www.vellum.ai/blog/best-ai-receptionist-for-small-business) — [Fair Square 4× after-hours](https://www.fiercehealthcare.com/health-tech/fair-square-medicare-rolls-out-ai-voice-agents-help-enroll-seniors-insurance-plans) — [TPMO obligations](https://ritterim.com/blog/insurance-agents-as-tpmos-what-cms-compliance-regulations-mean-for-you/) · [AI compliance 2026](https://tmsbrokerage.com/2026/04/17/how-medicare-agents-can-use-ai-and-automation-without-crossing-cms-compliance-lines/) · [10-year recording rule](https://www.psmbrokerage.com/blog/call-recording-and-retention-requirements-for-telephonic-sales-of-medicare-plans) — [2026 MA commissions](https://blog.actionbenefits.com/cms-releases-medicare-advantage-commissions-for-2026) · [by state](https://essentialcareagents.com/blog/2026-medicare-advantage-part-d-broker-commission-rates/) — [AEP pain points](https://www.seniormarketsales.com/blog/tech-tools-solve-real-agent-pain-points-during-aep) · [five-minute lead window](https://iadbrokerage.com/aep-prep-mistakes/) — [Rivvi](https://rivvi.ai/)
