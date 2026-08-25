# ICP Dashboard
**Health Plan Chat · Sprint 1 · August 2026**

> **Two notes on inputs.** The brief refers to "three persona levels as mentioned in this
> presentation" — no presentation was attached, so this uses the three levels already
> established in `competitive-analysis.md` §5: **User / Manager / Decision Maker**. Swap
> them if your deck defines different levels.
>
> Revenue bands are **annual commission revenue**, derived from published 2026 CMS
> compensation ($694 initial / $347 renewal per MA enrollment) against typical per-agent
> production. They are modelled, not surveyed — treat as ranges for segmentation, not as
> verified financials.

---

## 1. The two ICPs

**ICP-1 (MVP → PMF)** is chosen for one reason above all others: it is the segment
careCycle's ~$10,000/month floor has left unsold. It has real inbound volume, real plan
complexity, and no credible offer today.

**ICP-2 (Growth)** is where the corpus advantage compounds — one FMO relationship becomes
distribution across a downline.

| | **ICP-1 · MVP → PMF** | **ICP-2 · Growth** |
|---|---|---|
| **Segment** | Independent Medicare insurance agencies with their own inbound phone number and website | Established Medicare agencies, General Agencies (GAs) and FMO downlines running multi-agent, multi-state distribution |
| **Sub-industries** | Medicare Advantage / Part D / Medicare Supplement brokerage · senior-market insurance · often bundled with final expense, dental/vision/hearing, hospital indemnity | Field Marketing Organisations · General Agencies · Medicare call centres · senior-market IMOs · agencies with captive downlines and override structures |
| **Location** | US, single-state or 2–3 contiguous states. Highest density where MA penetration and senior population concentrate: FL, TX, AZ, CA, PA, OH, NC, MI | US multi-state, 5+ states. Bilingual markets are disproportionately valuable — CA, TX, FL, AZ carry large Medicare-eligible Hispanic populations most agencies cannot staff for |
| **Revenue, $** | **$400K – $2.5M** annual commission revenue | **$2.5M – $25M** annual commission + override revenue |
| **Team Size** | **3 – 10 licensed agents**, plus 1–2 admin/front desk. Often no dedicated marketing or ops hire | **10 – 50 licensed agents** in-house, plus 50–500 contracted downline agents. Has ops, compliance and marketing functions |
| **Business Maturity** | 3–10 years operating. Established book, systematised on paper only. Growth constrained by owner's personal capacity | 8+ years. Systematised, multi-carrier, actively recruiting downline. Has survived multiple AEP cycles and CMS rule changes |
| **Business Model** | Commission-only, FMO-contracted. Mixed lead sources: referral, community seminars, some purchased leads. Revenue concentrated in AEP | Commission plus downline overrides. GA/MGA structure. Paid acquisition at scale, owns or buys lead flow, may run an internal call centre |
| **Best Engagement Model** | **Low-touch, self-serve-led.** Published pricing, no demo gate. Free Benefit Answer Gap Report → 72-hour sandbox → monthly plan, month-to-month. Founder-led onboarding. Land in one office | **Assisted, annual.** Compliance and security review, pilot with one downline segment, then multi-tenant rollout. Annual contract with per-seat or per-agency pricing. FMO co-marketing and co-branded reporting |
| **Organisation Challenges & Pain Points** | Calls go unanswered after hours and during AEP peak — a missed call is roughly **$2,082 in five-year member value**. The five-minute lead window is routinely lost. Front desk cannot answer plan-specific benefit questions, so every "what's my dental allowance?" becomes a callback or a lost caller. Cannot staff bilingual. Owner is the bottleneck on plan knowledge. Compliance handled manually and anxiously | All of ICP-1 at scale, plus: inconsistent answer quality across a downline nobody can supervise call-by-call. Agent turnover destroys accumulated plan knowledge. CMS exposure multiplied across every downline agent. No way to enforce disclaimer, SOA capture or recording uniformly. Recruiting pitch needs a technology differentiator |
| **Why Should They Choose Us** *(value proposition hypothesis)* | *"The only AI that already knows the plans you sell — at a price you can actually pay."* Answers plan-specific benefit questions from the carrier's own documents, in your agency's name, 24/7. The only comparable-depth product starts at $10K/month and is not selling to you | *"Consistent, compliant plan expertise across every agent in your downline."* One plan corpus, enforced uniformly — every agent's front line answers to the same standard, with disclaimer, escalation and recording built in. A recruiting asset, not just an ops tool |
| **Strategic Goals Related to Our Product** | Capture more of existing inbound without hiring · extend selling hours into evenings and weekends without burning out · stop losing AEP overflow · reduce dependence on the owner's personal plan knowledge · enter a bilingual market | Grow the downline without proportional headcount · lift persistency and protect renewal revenue · standardise compliance posture ahead of any CMS scrutiny · differentiate the FMO's recruiting offer · lower blended cost per acquisition on paid lead flow |
| **Triggers** | **AEP approaching** (15 Oct – 7 Dec) · a specific lost lead traced to a missed call · agent quits or goes on leave · adding a new carrier or plan year · a bad-fit enrollment producing a complaint or disenrollment · a competitor agency visibly running AI · first CMS or carrier compliance letter · buying paid leads and watching them go cold | New plan-year contracts signed · downline expansion or acquisition of another agency · a compliance finding anywhere in the downline · carrier pressure on persistency numbers · CPA rising on paid lead flow · losing a recruiting conversation on technology · AEP post-mortem showing abandoned-call volume |

---

## 2. Purchasing committee personas

### 2.1 ICP-1 · Independent agency, 3–10 agents

| | **Level 1 · User** | **Level 2 · Manager** | **Level 3 · Decision Maker** |
|---|---|---|---|
| **Possible Job Titles** | Licensed Medicare Agent · Insurance Producer · Front Desk / Office Administrator · Client Services Coordinator | Sales Manager · Agency Manager · Operations Lead · Lead Agent | Agency Owner · Founder · Principal Broker · Managing Partner |
| **Responsibility Area** | Taking the call, running the appointment, writing the application, servicing the book | Rota and phone coverage, lead distribution, agent ramp, day-to-day compliance discipline | P&L, carrier and FMO contracts, technology spend, growth strategy |
| **Purchasing Influence** | **Low formal / high veto.** Cannot buy, but abandons any tool that adds friction — and their abandonment kills renewal | **Medium.** Shapes the shortlist, runs the trial, owns the rollout | **High — signs.** In an agency this size the owner is usually also the top producer, so they feel the pain personally |
| **Core Customer Journey Stages** | Onboarding → daily use → renewal advocacy. Never involved in discovery | Problem recognition → evaluation → pilot → rollout | Problem recognition → vendor selection → negotiation → renewal |
| **Potential Reasons to Block** | "It'll answer wrong and I'll get blamed" · fear the AI is a step toward replacing them · one bad transcript early destroys trust | Cannot afford a failed AEP experiment · no bandwidth to run a pilot Sept–Dec · worried it fragments the CRM | Price against uncertain ROI · CMS liability for what the AI says · burned by a previous tech purchase that went unused |
| **Drivers** | Fewer interruptions from questions they've answered a hundred times · warm, qualified handoffs instead of cold callbacks · not working evenings | Coverage without a hiring req · a clean lead record that makes Monday morning predictable · visible AEP capacity | More policies from the same spend · reduced personal dependence · a business that runs without them on a Sunday |
| **Assets to Get Buy-In** | Recorded sample call on their own plans · a one-page "what it will and won't say" · the escalation guarantee | Benefit Answer Gap Report on their own line · 72-hour sandbox · AEP capacity plan | Missed-Call Revenue Calculator in CMS dollars · published pricing, month-to-month · CMS AI Exposure Review |
| **Channels to Find Them** | Facebook agent groups · Insurance Forums · FMO training webinars · agent-only Slack/Discord communities | FMO and GA newsletters · Medicare agent podcasts · AEP prep webinars · LinkedIn | Direct outbound with the free audit attached · FMO principal referral · industry events (Medicarians, AHIP-adjacent) · peer word of mouth |

### 2.2 ICP-2 · Growth agency, GA or FMO downline

| | **Level 1 · User** | **Level 2 · Manager** | **Level 3 · Decision Maker** |
|---|---|---|---|
| **Possible Job Titles** | Licensed Agent · Downline Agent · Call Centre Representative · Retention Specialist · Team Lead | Director of Sales · Director of Operations · Compliance Officer · Agency Success Manager · Call Centre Manager | Owner / CEO · COO · FMO Principal · VP Distribution · Head of Growth |
| **Responsibility Area** | Working assigned leads to enrollment, meeting production targets, servicing assigned members | Agent productivity and ramp, lead routing economics, CMS compliance across the org, vendor management | Distribution strategy, downline recruitment, carrier relationships, capital allocation |
| **Purchasing Influence** | **Low.** Adoption risk rather than purchase risk — but downline agents are contractors who simply won't use what they dislike | **High — often the true buyer.** Runs evaluation, security and compliance review, and owns the rollout plan | **High — signs and sets strategy.** Cares about the downline story as much as the ops outcome |
| **Core Customer Journey Stages** | Rollout → adoption → advocacy or quiet non-use | Discovery → evaluation → security/compliance review → pilot → phased rollout → renewal | Strategic framing → budget approval → negotiation → expansion decision |
| **Potential Reasons to Block** | Not their tool, not their choice — imposed from above · fear of lead quality changing · commission implications unclear | HIPAA/SOC 2 posture, BAA, data residency · integration with the existing CCaaS and CRM · "we already pay for careCycle / Coverage Voice" · rollout risk across contractors | Contract length and lock-in · vendor viability given our stage · whether it strengthens or complicates the FMO's carrier relationships |
| **Drivers** | Better-qualified leads reaching them · less time on questions that don't convert · higher close rate on the same volume | Uniform answer quality without call-by-call supervision · auditable compliance posture · measurable CPA reduction | Downline growth without proportional headcount · persistency and renewal protection · a recruiting differentiator competitors can't match |
| **Assets to Get Buy-In** | Rollout comms explaining what changes and what doesn't · side-by-side lead quality before/after | Security and compliance pack (HIPAA, SOC 2 roadmap, BAA, retention) · pilot design with success criteria · integration architecture doc | Downline-wide aggregate Gap Report · AEP Peak-Load Stress Test · commercial model with expansion pricing · reference from a comparable GA |
| **Channels to Find Them** | Downline onboarding and training sessions · internal agent communications | LinkedIn · Medicare distribution conferences · compliance and ops peer networks · carrier partner introductions | FMO principal peer network · Medicarians and senior-market industry events · carrier relationship introductions · investor and advisor referral |

---

## 3. Design partner / early adopter profile

The profile with the highest affinity to run an unfinished product, tolerate defects, and
return structured feedback.

| Attribute | Profile |
|---|---|
| **Design Partner Attributes** | Owner-operator of a 4–12 agent independent agency who is also the agency's top producer — so they feel the missed-call pain personally and can authorise a pilot in the same conversation. Has already bought at least one AI or automation tool (often a CRM with AI bolted on, or a general AI receptionist) and been disappointed by it, so they can articulate exactly what "not good enough" means. Technical-adjacent, not technical: runs their own CRM automations, active in agent communities |
| **Job Titles** | Agency Owner · Founder · Principal Broker · Managing Partner · Owner-Producer |
| **Demographics** | US-based, typically 35–55 — old enough to run a real book, young enough to be an early technology adopter in a conservative industry. 3–10 years operating. Single-state or 2–3 states. Often a second-career agent from sales, healthcare or tech, which correlates strongly with tool experimentation |
| **Responsibility Areas** | Everything: personal production, agent recruitment and training, lead buying, phone coverage, carrier contracting, compliance, and the technology stack. No one to delegate the evaluation to — which is exactly why they can move fast |
| **Current Tools** | Agency CRM (Agent CRM, HubSpot, GoHighLevel, Radius) · SunFire or MedicareCENTER for quoting and enrolment, free via their FMO · a VoIP line (RingCentral, Dialpad) · possibly a general AI receptionist or answering service · spreadsheets for plan comparison cheat-sheets they built themselves |
| **Key Pain Points** | Their own line goes unanswered at 9pm during AEP · the front desk cannot answer a dental or OTC allowance question, so every one becomes a callback · they are personally the plan-knowledge bottleneck · bilingual callers are lost outright · manual, anxious compliance · paid leads going cold inside the five-minute window |
| **Critical Triggers** | **AEP proximity is the dominant trigger** (15 Oct – 7 Dec) · a specific traced lost lead · an agent departure removing plan knowledge · a new carrier or plan year to learn · a complaint or rapid disenrollment · seeing a competing agency advertise AI |
| **Goals & Motivations** | Grow without hiring · stop being the bottleneck · reclaim evenings and weekends · look modern to prospects and recruits · be early to something their peers haven't found yet — status inside the agent community is a real and underrated motivator |
| **Decision Criteria** | Does it answer *my* plans correctly — tested on their own hardest question · does it say the wrong thing (accuracy and escalation behaviour) · does it sound like my agency · price they can commit to without a board · month-to-month, no annual lock-in · can they hear it working within days, not weeks |
| **Influence Level** | **Complete.** Sole decision maker, sole budget holder, and usually the primary user. No committee, no procurement, no security review. This is the single biggest reason to start here rather than with ICP-2 |
| **Barriers to Purchase** | Fear the AI gives a wrong benefit or copay answer and creates a CMS or carrier problem · reputational risk if a client realises they spoke to a bot · burned by prior tech spend that went unused · **no time between mid-September and January** · scepticism that any vendor genuinely knows their specific county's plans |
| **Information Sources** | Facebook agent groups and Insurance Forums · FMO trainers and upline principals · Medicare agent podcasts and YouTube channels · peer word of mouth, which dominates everything else in this market · AEP prep webinars · LinkedIn to a lesser degree |
| **Success Metrics** | Calls answered outside business hours · % of benefit questions resolved without a callback · appointments booked from after-hours calls · lead-to-appointment and appointment-to-enrollment rate · time saved personally · attributable enrollments — the number that renews the contract |
| **Early Adopter Characteristics** | Already experimenting with AI and vocal about it · tolerant of rough edges if the core answer is right · gives specific, usable feedback rather than "it didn't work" · will hand over plan documents without a legal review · responds to being treated as a co-designer rather than a customer · **evangelises in agent communities**, which is the fastest distribution channel in this market |

### The recruitment window is the binding constraint

Design partners have time between **February and mid-September**. From 15 October to 7
December they are in AEP and unreachable; January through March is OEP. It is now late
August 2026 — roughly **seven weeks before AEP opens.**

That gives two viable plays, and they are mutually exclusive:

1. **Recruit now, ship for AEP.** A partner who feels the pain most acutely is the one
   about to enter AEP. Onboarding must be days, not weeks — which is precisely our weakest
   vector (5.4 on deployment speed). Sign a small number, instrument heavily, accept that
   AEP is a stress test rather than a feedback cycle.
2. **Recruit now, onboard in January.** Use the Benefit Answer Gap Report through AEP as a
   *listening* instrument — it needs nothing from them but their phone number, and it
   captures evidence at the exact moment the pain is sharpest. Convert those reports into
   design partnerships in February when they have time to give real feedback.

**Recommendation: run play 2 as the default and play 1 for no more than three partners.**
The Gap Report is the only asset that works during AEP, because it costs the agency nothing
and arrives when the wound is open.
