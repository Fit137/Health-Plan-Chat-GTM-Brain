# Customer Journey Funnel
**Health Plan Chat · Sprint 1 · August 2026**

Same seven-stage structure and seven columns as the uploaded RiskSenz sheet, with every cell
rewritten for the Health Plan Chat context. Written for the **primary motion — ICP-1, the
independent Medicare agency of 3–10 licensed agents**; where ICP-2 (GA / FMO downline)
diverges materially, that is set out beneath the table.

Touch-points reference the campaigns in `assets-library.md` and the demand drivers D1–D6 in
`product-feature-matrix.md` §7. KPI targets are **initial targets to calibrate against first
cohort data**, not forecasts — there is no baseline yet.

---

| Funnel Stage | Buyer Mindset & Trigger | Key Questions They Ask | Touch-points & Assets (channel) | Internal Goal / KPI | State After Stage (Desired Outcome) | Function |
|---|---|---|---|---|---|---|
| **1. Problem Awareness** | *"We're missing calls we can't afford to miss."* Triggers: AEP approaching (15 Oct); a lost lead traced to an unanswered call; an agent leaving and taking plan knowledge with them; a new plan year to learn; a complaint or fast disenrollment; a competing agency visibly advertising AI | How many calls are we actually missing?<br>What happens to someone who calls on a Sunday?<br>Can anyone here answer a dental allowance question without me?<br>What is that costing us? | **D1 Readiness Scorecard** — Facebook agent groups, Insurance Forums<br>**D2 Missed-Call Revenue Calculator** — LinkedIn Ads landing page<br>Cold outreach E1: one Gap finding + the recording of their own line<br>AEP Prep Webinar | Scorecard / calculator completions ≥ 15% of visitors<br>Cold E1 reply rate ≥ 8% | Owner accepts they have a measurable, dollarised gap — and that it concentrates on **plan-specific questions asked outside office hours**, not on call volume generally | Demand Gen + founder-led outbound |
| **2. Interest / Education** | Wants the size of the problem without starting a project. Open to a free diagnostic. Genuinely sceptical that any vendor knows the plans in *their* county | Which questions are we actually failing?<br>Is it only after hours, or all day?<br>Can an AI really know *my* plans, or just Medicare in general?<br>What happens when it doesn't know something? | **D3 Benefit Answer Gap Report** — full PDF + their own call recordings<br>AEP readiness checklist (useful without buying)<br>"What we found auditing N agencies" community post series<br>ICP-1 nurture sequence | Gap Report delivered → sandbox request ≥ 25%<br>Report delivered within 48h of shop completion | Believes the gap is real, specific to plan-knowledge rather than staffing, and that only a plan-grounded agent closes it — a receptionist or answering service demonstrably does not | Marketing + founder |
| **3. Consideration** | Comparing us against careCycle, Coverage Voice, a $79 AI receptionist, and doing nothing. Testing whether it is accurate enough not to embarrass them in front of a client | How does this compare to careCycle or Coverage Voice?<br>Will it say the wrong thing?<br>How fast can we be live — before AEP?<br>What does it actually cost? | **D4 72-Hour Plan Brain Sandbox** on their own plan documents<br>Comparison pages (vs careCycle, Coverage Voice, AI receptionist, SunFire)<br>"What it will and won't say" one-pager<br>Peer reference call | Sandbox delivered → pricing conversation ≥ 40%<br>**20/20 regression pass against their documents before handover** | Has heard a correct, sourced answer to their own hardest plan question, in their own agency's voice. Every competitor without plan grounding is now disqualified — the comparison has moved from price to capability | Marketing & Sales (founder-led) |
| **4. Decision** | Needs price certainty and reassurance on liability. **No committee** — the owner decides, and is usually also the top producer | What's the price, and can I stop?<br>Who is liable if it misstates a copay?<br>Is the TPMO disclaimer handled? Are calls recorded and kept?<br>Can we be live before 15 October? | Pricing one-pager + month-to-month agreement<br>**D5 CMS AI Exposure Review**<br>BAA and data-handling summary<br>Pre-AEP onboarding offer with fixed dates | Sandbox → paid conversion<br>Time from sandbox to signature ≤ 10 days | Signs month-to-month with a confirmed onboarding date, understanding plainly what is shipped versus what is roadmap | Sales (founder) + Compliance |
| **5. Onboarding / First Win** | *"Prove it before AEP."* Wants it live fast with minimal disruption to a book that is already running | What do you need from me?<br>Which plans go in first?<br>How do I hear it working?<br>What happens when a caller asks something it doesn't know? | Plan document intake checklist (SB / EOC)<br>20-question regression report against their own documents<br>Greeting, branding and escalation routing config<br>Agent-facing comms: *"what changes for you"* | **Live ≤ 5 business days from documents received**<br>First answered after-hours call ≤ 7 days<br>Regression 20/20 | The agency hears its own line answer a real benefit question, correctly, at nine on a Sunday — and the structured lead lands in their CRM by morning | Customer Success + Eng |
| **6. Adoption & Expansion** | Wants more of the front line covered — more carriers, chat as well as voice, Spanish, and the booked appointment | Can it handle the rest of my carriers and next plan year?<br>Can it book the appointment?<br>Can it do Spanish?<br>Can my other office use it? | Additional carrier and plan-year ingestion<br>Spanish enablement<br>Website chat embed<br>Monthly answer-quality report<br>Second-location expansion | ≥ 3 plan corpora live per agency<br>≥ 70% of benefit questions resolved without a callback<br>After-hours booked appointments trending up | The front line is infrastructure, not an experiment. The agency adds plans and channels without being asked, and would notice immediately if it stopped | Success + Product |
| **7. Renewal / Advocacy** | Confident it paid for itself; wants proof they can show, and standing among peers | How many enrollments came from calls we'd otherwise have missed?<br>What did that earn?<br>Can I show this to my FMO?<br>Will it hold up through next AEP? | AEP review pack: attributed enrollments × 2026 CMS rates ($694 initial / $347 renewal)<br>Before/after Gap score<br>Case study + design partner story<br>Referral and FMO introduction ask | Logo retention ≥ 90% through AEP<br>≥ 1 referral or FMO introduction per advocate<br>Attributed enrollments reported per account | Renews, and introduces us into an agent community or an FMO downline — **which is how ICP-2 pipeline actually gets created** | Success + Partnerships |

---

## Where ICP-2 (GA / FMO downline) diverges

The seven stages hold, but four of them change shape enough to run differently:

| Stage | What changes for ICP-2 |
|---|---|
| **1–2 Awareness / Interest** | Trigger is a compliance finding, downline expansion, or rising CPA on paid leads — not a missed Sunday call. Entry driver is **D5 CMS AI Exposure Review** or **D6 AEP Peak-Load Stress Test**, reached through LinkedIn Outreach, not community channels |
| **3 Consideration** | Adds a security and compliance review the ICP-1 journey does not have. Requires HIPAA posture, SOC 2 status stated honestly, BAA, data residency and integration architecture. Coverage Voice is HIPAA + SOC 2 certified — understating our position loses, overstating it is worse |
| **4 Decision** | Becomes a **committee**, not a person. The Director of Operations is frequently the true buyer; the owner or FMO principal signs. Annual contract, phased rollout, expansion pricing — not month-to-month |
| **5–6 Onboarding / Expansion** | Rollout is per-downline-segment, and **contractor adoption is the failure mode** — Level 1 downline agents did not choose the tool and will quietly not use it. Agent comms must address "is this replacing me" directly |

---

## Three dependencies this funnel is exposed to

| Stage | Dependency | Status |
|---|---|---|
| **4. Decision** | Pricing one-pager and published price | **Blocked on OF-1.** Pricing is not yet published, so the stage-4 asset does not exist. Currently every deal requires a bespoke price conversation, which is exactly the demo gate the positioning attacks |
| **5. Onboarding** | Live in ≤ 5 business days | **At risk.** Deployment speed is our weakest vector (5.4 vs Synthflow 9.4, Coverage Voice 9.1 at 48 hours). This stage is where the funnel most likely breaks, and it is the stage a pre-AEP promise depends on |
| **6. Adoption** | Appointment booking and SOA capture | **Gaps.** Appointment booking (F08) scores +14.1 demand and both direct competitors have it; SOA capture is OF-3, a CMS requirement Coverage Voice handles in-call. Both sit inside stage 6 and cap expansion |
