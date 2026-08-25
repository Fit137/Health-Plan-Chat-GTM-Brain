# Assets & Collaterals Library
**Health Plan Chat · Sprint 1 · August 2026**

Two parallel acquisition functions, one per ICP. Every campaign is expanded across all three
funnel stages. The three highlighted campaigns — **Personalized Cold Outreach**,
**LinkedIn Outreach**, **LinkedIn Ads** — are marked ★.

---

## Read this before building anything

**1. Two of the three highlighted campaigns serve ICP-2, not ICP-1.** From
`icp-dashboard.md`, the ICP-1 decision maker (independent agency owner, 3–10 agents) is
found through direct outbound, Facebook agent groups, Insurance Forums, FMO referral and
peer word of mouth. **LinkedIn appears only at the Manager level for ICP-1, and prominently
for ICP-2.** So Personalized Cold Outreach is the ICP-1 engine; both LinkedIn campaigns are
ICP-2 plays. Pointing LinkedIn Ads at independent agency owners spends against a channel
their buyer is barely in — run it at Directors of Operations and FMO principals instead.

**2. The calendar is the binding constraint.** AEP opens **15 October** — roughly seven
weeks out. From 15 Oct to 7 Dec, ICP-1 is unreachable for anything requiring their time.
Only assets that cost the prospect nothing work during that window, which in practice means
the Gap Report and paid media. Everything requiring their attention should be built now to
land either **before 1 October** or **after 5 January**.

**3. Visual production is a Claude Design dependency.** Per repo convention, all formats
below are specified as content and structure; visual treatment happens separately.

---

## The value driver as top-of-funnel asset

The demand driver from `product-feature-matrix.md` §7 is **D3 · The Benefit Answer Gap
Report** (perceived value 8.6, ease of delivery 6.7). It is the TOFU spine of both
functions. Supporting drivers D1, D2, D5 and D6 act as channel-native entry points that all
route into D3.

| Channel | Value driver format | What the prospect gives | What they get back | Why this format here |
|---|---|---|---|---|
| **Personalized Cold Outreach ★** | Full Gap Report, pre-run before contact | Nothing — we run it unprompted on their public line | PDF scorecard + call recordings of their own line failing benefit questions | The only format where the asset arrives before the ask. Highest conversion, highest cost per prospect |
| **LinkedIn Outreach ★** | Gap Report offer, run on request | A reply and their agency name | Same report, delivered 48h after they accept | Reciprocity works cold on LinkedIn; running it unprompted at ICP-2 scale is not economic |
| **LinkedIn Ads ★** | **D2 Missed-Call Revenue Calculator** as the ad-side driver, Gap Report as the retarget offer | Email + three inputs | Instant dollar figure, then a Gap Report offer | A report takes 48h; paid traffic needs an instant payoff. D2 is the instant one |
| **Agent Community & Forums** | **D1 Medicare AI Readiness Scorecard** | 90 seconds, no email until the score | Score out of 100 + benchmark | Communities reject gated assets. D1 gives value before asking for anything |
| **AEP Prep Webinar** | Aggregate Gap Report findings as content, individual report as the CTA | Attendance | Benchmark data across audited agencies + their own report on request | Anonymised aggregate data is the webinar's substance and the individual report is its conversion event |
| **FMO / Carrier Co-Marketing** | Downline-wide Gap Report | The FMO's introduction to their downline | League-table report across agencies, co-branded | Converts one relationship into distribution; the aggregate is the FMO's own management data |
| **Industry Events** | **D6 AEP Peak-Load Stress Test** | A booked slot | Capacity and knowledge-failure report | Only setting where a white-glove, high-value driver justifies its delivery cost |

---

# Function A · ICP-1 — Independent agency, 3–10 agents

## A1 ★ Personalized Cold Outreach

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | Benefit Answer Gap Report + cold email sequence | Pre-run mystery shop of the prospect's own line and site, delivered unprompted with a 3-email sequence | PDF report (4–6pp) + plain-text email sequence + 2 call recordings (MP3) | E1: one finding + the recording, no pitch. E2: the full report attached, still no pitch. E3: one-line offer of the sandbox | Zero marketing language in E1–E2. Report must name the exact question, time of day and outcome. **QA: every claim traceable to a recording; no inferred failures.** Legal check on call-recording consent by state | Founder (calls, review) · Ops/VA (list build, shop calls) · Compliance reviewer (consent) | Target list with public phone + site + plans sold · two-party consent state list · scoring rubric | **Build 1 week; 2–3 days per prospect thereafter** | Works during AEP — the only ICP-1 asset that does, because it costs the prospect nothing |
| **Middle of funnel** | 72-Hour Plan Brain Sandbox (D4) | Live agent trained on their own plan documents, branded to their agency | Private phone number + chat link + 1-page "what it will and won't say" | Their plans ingested · sample questions to try · escalation behaviour explained · what is not yet built | Must answer their hardest question correctly or do not ship it. **QA: 20-question regression against their documents before handover; any wrong answer blocks release** | Founder · Eng (ingestion, provisioning) | Their SB and EOC PDFs · agency name and greeting · 3 hardest questions from them | **72 hours from documents received** | The conversion event. Requires their documents, which is itself the qualifying act |
| **Bottom of funnel** | Pricing one-pager + month-to-month agreement | Published price, plain terms, no annual lock | 1-page PDF + short-form agreement | Price by agent count · what is included · what is coming · cancellation terms · data handling and BAA | Price must match the website exactly. **QA: no capability listed that is not shipped — cross-check against `feature-scores.csv`** | Founder · Compliance reviewer | Final pricing decision (OF-1, still open) · BAA template | **3 days once pricing is set** | **Blocked on OF-1** — pricing is not yet published. This asset cannot ship until it is |

## A2 Agent Community & Forums

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | Medicare AI Readiness Scorecard (D1) | 12-question self-assessment, scored instantly, no email gate until the result | Web page + shareable score card | 12 questions on after-hours cover, plan-answer capability, Spanish, compliance · score /100 · 2-line diagnosis · peer benchmark | Questions must be the argument — each one names a gap. **QA: no lead capture before the score displays; communities punish gating** | Founder · GTM lead · Claude Design | Question set · benchmark data from Gap Reports run to date | **1 week** | Facebook agent groups and Insurance Forums are where ICP-1's user and manager levels actually live |
| **Middle of funnel** | "What we found auditing N agencies" post series | Anonymised aggregate findings from Gap Reports, posted as community contribution not promotion | Long-form forum/group posts + short video walkthroughs | % of lines unanswered after hours · most-failed question types · time-to-answer distribution · what good looked like | No agency identifiable. No CTA in the post body. **QA: founder posts under own name; peer word of mouth dies if it reads as vendor marketing** | Founder | ≥15 completed Gap Reports for a defensible sample | **Ongoing, from ~15 reports** | Peer word of mouth dominates this market — this asset buys standing, not clicks |
| **Bottom of funnel** | Peer reference call + design partner story | Named early customer walks a prospect through their own result | 20-min call + 1-page written case study | Their before/after Gap scores · what changed operationally · what it cost · what is still missing | Must include a limitation, stated plainly. **QA: customer approves verbatim; no invented metrics** | Founder · Design partner customer | A design partner with ≥60 days of data and consent | **Post-January (needs usage data)** | The single highest-trust asset in this market and the slowest to earn |

## A3 AEP Prep Webinar

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | "What AEP callers actually ask" webinar | 30-min session built on Gap Report data, not product | Live webinar + recording + slide PDF | The 25 questions callers ask · what most agency lines do with them · the five-minute window · the $694/$347 commission arithmetic | Product appears only in the final 5 minutes. **QA: every statistic sourced on-slide; CMS figures cited to the rate release** | Founder · GTM lead · Claude Design | Aggregate Gap data · 2026 CMS commission figures | **2 weeks to build; must run before 1 Oct** | After 15 Oct nobody attends. Either it runs in the next five weeks or it moves to February |
| **Middle of funnel** | Post-webinar Gap Report offer + AEP readiness checklist | Attendee-only offer of their own audit, plus a practical checklist they can use regardless | Email + PDF checklist | Checklist: after-hours routing, disclaimer script, SOA capture, recording retention, overflow plan | Checklist must be useful without buying anything. **QA: compliance reviewer signs off the CMS items** | Founder · Compliance reviewer | Webinar attendee list | **3 days after webinar** | The checklist is the reciprocity; the report is the conversion |
| **Bottom of funnel** | Pre-AEP onboarding offer | Fixed-scope, fixed-date onboarding to be live before 15 Oct | 1-page offer + implementation schedule | What is delivered by when · what we need from them and when · what happens if we miss the date | Only offer this if onboarding genuinely fits the window. **QA: do not sell a date engineering has not confirmed** | Founder · Eng | Confirmed onboarding capacity | **Offer window closes ~1 Oct** | Deployment speed is our weakest vector (5.4) — over-promising here damages the relationship it wins |

---

# Function B · ICP-2 — GA / FMO downline

## B1 ★ LinkedIn Outreach

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | Connection + 3-touch sequence offering a downline Gap Report | Targeted at Directors of Ops, Compliance Officers and FMO principals — not agency owners | LinkedIn connection note + 3 DMs + 1 InMail variant | T1: one insight from aggregate audit data. T2: offer to run it across a downline segment. T3: single-question close | Under 300 characters per touch. No attachments in T1. **QA: title-verify every prospect against ICP-2 definition; ICP-1 owners get routed to A1 instead** | Founder · GTM lead · Ops/VA (list build) | Sales Navigator list by title and company size · aggregate Gap data | **1 week to build; ongoing** | This is where LinkedIn actually works. Level 2 (Director of Ops) is frequently the true buyer |
| **Middle of funnel** | Downline pilot proposal + security pack | Pilot design across one downline segment, with the compliance and security answers pre-empted | Proposal PDF (6–8pp) + security/compliance pack | Pilot scope, segment, success criteria, timeline · HIPAA posture · SOC 2 status and roadmap · BAA · data residency · retention · integration architecture | State SOC 2 status honestly, including if it is roadmap not certified. **QA: compliance reviewer signs; competitors hold SOC 2 and buyers will ask** | Founder · Compliance reviewer · Eng | Current security posture · integration inventory · pilot success metrics | **2 weeks** | Coverage Voice is HIPAA + SOC 2 certified. Understating our position loses; overstating it is worse |
| **Bottom of funnel** | Multi-tenant rollout plan + commercial model | Phased downline rollout with expansion pricing | Plan PDF + pricing model + MSA | Phase 1 segment · phase 2 expansion triggers · per-agency vs per-seat pricing · support model · co-branding terms | **QA: do not claim multi-agency deployment is unique — see OF-2. Coverage Voice ships sub-accounts white-labelled in 48h** | Founder · GTM lead | Expansion pricing decision · multi-tenant capability status (roadmap) | **2 weeks; gated on capability** | Feature 25 is roadmap, not shipped. Sell the plan-grounding across the downline, not the multi-tenancy |

## B2 ★ LinkedIn Ads

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | Missed-Call Revenue Calculator (D2) + ad set | Instant-payoff driver behind paid traffic, because a Gap Report takes 48 hours | Landing page tool + 6 ad variants (single image, document ad, text) | Inputs: monthly inbound volume, % missed, state → annualised lost commission on 2026 CMS rates, split by after-hours vs unanswered-question | Result must compute before email capture. **QA: arithmetic verifiable against the published CMS rate release; a wrong number here destroys credibility with an ops buyer** | GTM lead · Founder · Claude Design | 2026 CMS rate table by state · ad account · targeting by title and company size | **2 weeks build; 1 week to first data** | Target Director of Ops / Compliance / FMO principal titles. **Do not target independent agency owners here** |
| **Middle of funnel** | Retargeting: aggregate audit report as a document ad | Gated benchmark report to calculator visitors who did not convert | LinkedIn document ad + landing page | Benchmark findings across audited agencies · what separates the top quartile · methodology | Genuine data only. **QA: minimum sample of 15 agencies before publishing any benchmark** | Founder · GTM lead · Claude Design | ≥15 Gap Reports · retargeting audience | **1 week after sample reached** | Document ads outperform link ads for this buyer; the asset doubles as the B1 outreach hook |
| **Bottom of funnel** | Demo request + CMS AI Exposure Review (D5) offer | For ops and compliance buyers, the compliance review converts better than a product demo | Conversion ad + booking page + review scoping doc | What the review covers: disclaimer timing, automated-system disclosure, recording retention, escalation to licensed agent | **QA: this is a genuine audit, not a disguised demo — deliver findings even where they favour a competitor** | Founder · Compliance reviewer | Review checklist · calendar capacity | **1 week** | D5 is the sharpest problem-identification play we have and nobody in the category runs it |

## B3 FMO / Carrier Partner Co-Marketing

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | Downline-wide Gap Report + partner pitch | Audit across an FMO's downline, delivered as their management data and co-branded | Partner pitch deck (10–12 slides) + aggregate league-table report | What we audit · what the FMO learns about their own downline · co-branding terms · what agents get free | The FMO must get standalone value even if nobody buys. **QA: no individual agency named without consent** | Founder · GTM lead · Claude Design | One FMO partner agreement · downline roster | **3 weeks incl. partner negotiation** | Highest-leverage motion in the library: one relationship becomes distribution across dozens of agencies |
| **Middle of funnel** | Co-branded agent webinar + recruiting asset | Session delivered to the FMO's downline, positioned as an FMO member benefit | Webinar + slide deck + 1-page agent handout | Same content as A3 but co-branded · FMO-specific benchmark data · member offer | FMO reviews all content before delivery. **QA: no carrier or plan named in a way that implies endorsement — CMS marketing rules apply** | Founder · FMO partner · Compliance reviewer | FMO approval · downline benchmark data | **2 weeks after partnership** | Also serves the FMO's recruiting pitch, which is what makes them promote it |
| **Bottom of funnel** | Downline deployment agreement + enablement kit | Terms and rollout materials for deploying across contracted agencies | MSA + enablement kit (onboarding guide, agent comms, FAQ) | Per-agency pricing and override treatment · onboarding sequence · agent-facing comms · support escalation | Agent comms must address the "is this replacing me" objection directly. **QA: contractor adoption is the failure mode — Level 1 users have effective veto** | Founder · FMO partner · Eng | Signed partnership · multi-tenant capability · pricing model | **4 weeks; gated on capability** | Gated on the same roadmap item as B1 bottom of funnel |

---

# Shared · Always-on

## S1 Website & Email Nurture

| Funnel Stage | Asset/Collateral | Description | Format | Content Outline | Content Specifications & QA | Contributors | Inputs Required | Est. Timeframe | Notes |
|---|---|---|---|---|---|---|---|---|---|
| **Top of funnel** | Homepage + Gap Report and Scorecard landing pages | Destination for every campaign; carries the positioning and both self-serve drivers | Website pages + forms | Positioning statement · the plan-fluency proof · D1 and D3 entry points · pricing page | Copy comes from `value-proposition.md`. **QA: verify the four flagged claims in that document before publishing — three are not yet true** | Founder · GTM lead · Claude Design | Value proposition copy · pricing decision · brand assets | **2–3 weeks** | Pricing page is blocked on OF-1, and OF-1 is the largest single positioning lever we hold |
| **Middle of funnel** | Segmented nurture sequences (ICP-1 and ICP-2) | Two separate tracks — the buyers, channels and objections differ entirely | Email sequences (6 for ICP-1, 8 for ICP-2) | ICP-1: missed-call economics → plan-answer proof → sandbox offer. ICP-2: compliance exposure → downline consistency → pilot offer | Never merge the tracks. **QA: ICP-1 sequence must not reference procurement or security review; ICP-2 must not reference month-to-month pricing** | GTM lead · Founder | Segmented list · driver completion data | **2 weeks** | Segmentation signal comes from which driver they completed — D1/D2 implies ICP-1, D5/D6 implies ICP-2 |
| **Bottom of funnel** | Objection-handling library + comparison pages | Answers to the objections the competitive analysis predicts, and honest comparison content | Internal battlecard + public comparison pages | vs careCycle (price) · vs Coverage Voice (plan answers vs eligibility) · vs a general AI receptionist (plan knowledge) · vs SunFire (consumer-facing vs agent-facing) · "will it say the wrong thing" | Comparisons must be defensible and dated. **QA: no claim of uniqueness on multi-agency deployment (OF-2); state competitor strengths accurately or the page reads as spin** | Founder · GTM lead | `competitive-analysis.md` · verified capability list | **2 weeks** | "It'll answer wrong and I'll get blamed" is the top ICP-1 blocker — it needs its own asset, not a bullet |

---

## Build order given the AEP calendar

| Sequence | Window | Build | Rationale |
|---|---|---|---|
| **1** | Now → 2 weeks | A1 Gap Report + cold sequence · S1 landing pages | The only ICP-1 motion that works during AEP, and the destination everything needs |
| **2** | Now → 4 weeks | B1 LinkedIn Outreach · B2 calculator + ads | ICP-2 stays reachable through AEP; their buying cycle is long enough to start now |
| **3** | Before 1 Oct | A3 webinar · A2 scorecard | Hard deadline — after 15 Oct the ICP-1 audience is gone until January |
| **4** | Through AEP | Run A1 and B2 only; accumulate Gap Reports | Builds the sample the benchmark assets need |
| **5** | January | A2 post series · A3 relaunch · A1 peer references | Requires accumulated data and an audience with time |
| **Gated** | On OF-1 | Pricing page · A1 bottom-of-funnel one-pager | Cannot ship until pricing is published |
| **Gated** | On roadmap | B1/B3 bottom-of-funnel | Multi-tenant deployment is not shipped |
