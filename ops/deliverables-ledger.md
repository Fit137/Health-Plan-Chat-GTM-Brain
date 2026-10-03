# Deliverables ledger

Everything produced for Health Plan Chat, from the Sprint 1 GTM strategy through the
Sprint 2 outbound build, with its status and where it lives.

`last_reviewed: 2026-10-03`

## How to read the status column

| Status | Means |
|---|---|
| **Shipped** | Exists, delivered, and the client can open it today |
| **In repo** | Committed to a repository the client owns |
| **Handed over** | Delivered as a file or link, not committed anywhere |
| **Spec only** | Written down in full, **not built**. Nothing to open |
| **Blocked** | Cannot be finished until a named decision is made |

> A spec is not a deliverable the client can use. Section 5 lists every item that is
> specified but not built, because that is the gap worth seeing.

---

## 1 · Sprint 1 — GTM strategy

The analytical layer. Built from the founder's source sheet and market research.

### 1.1 The six Google-folder deliverables

Presentation-format, matched to the reference template. Arial throughout, navy/gold/zebra
palette except the funnel, which uses the reference funnel palette.

| # | Deliverable | Format | Status |
|---|---|---|---|
| 1 | Product Feature Matrix | xlsx, 8 sheets | Shipped |
| 2 | Competitive Market Analysis | xlsx, 15 sections | Shipped |
| 3 | ICP Dashboard | xlsx | Shipped |
| 4 | Value Proposition Framework | docx, 12 tables | Shipped |
| 5 | Customer Journey Funnel | xlsx, 3 sheets | Shipped |
| 6 | Marketing Assets Library | xlsx | Shipped |

### 1.2 The canonical text behind them

These are the authoritative versions. The spreadsheets were generated from these, not the
other way round.

| Deliverable | What it settles | Status |
|---|---|---|
| `gtm/product-feature-matrix.md` | 25 features scored, layered L1/L2/L3, quadranted | In repo |
| `gtm/feature-scores.csv` | The scores as data | In repo |
| `gtm/competitive-analysis.md` | Six competitors, the wedge, the price finding | In repo |
| `gtm/positioning-dashboard.md` | The four vectors and which two we lead | In repo |
| `gtm/icp-dashboard.md` | Both ICPs, committee personas, design partner profile | In repo |
| `gtm/value-proposition.md` | Brand promise, three pillars, nine reasons to believe | In repo |
| `gtm/customer-journey-funnel.md` | Seven stages, both funnels, three exposures | In repo |
| `gtm/assets-library.md` | Seven campaigns across three funnel stages, both ICPs | In repo |
| `gtm/OPEN-FINDINGS.md` + `.csv` | Three live findings that revise the source sheet | In repo |

### 1.3 Pricing

| Deliverable | Status |
|---|---|
| `gtm/pricing-model.xlsx` — 9 tabs, all inputs on a Control Panel | Shipped |
| `gtm/pricing-model.md` — derivation, cost floor, the customer-facing table | Shipped, **internal only** |
| The published price | **Blocked.** OF-1. Modelled, not decided |

### 1.4 The walkthrough

| File | What it is | Status |
|---|---|---|
| `gtm/walkthrough/01-CONTENT.md` | 901 lines. The founder review, built to settle the price and three findings | Shipped |
| `gtm/walkthrough/02-DESIGN-CONCEPTS.md` | 372 lines. Design direction, no system imposed | Shipped |
| `gtm/walkthrough/03-CLAUDE-DESIGN-HANDOFF.md` | 245 lines. The paste block for the design pass | Shipped |

### 1.5 Supporting

| Deliverable | Status |
|---|---|
| Feature matrix as a published page | Shipped — `claude.ai/artifact/W3UkYa1XbQE2SuFkWSYTPe` |
| `gtm/product-feature-matrix.html` | Frozen v1, superseded by the `.md`. Do not update |
| Sprint 1 baseline snapshot | In repo — `snapshots/2026-08-25-sprint-1-build.md` |

---

## 2 · The GTM Brain — the control layer

A portable context system any coding agent can read, so every asset produced afterwards
obeys the same ICP, claim rules and voice. 48 commits.

### 2.1 Core

| Deliverable | What it does |
|---|---|
| `CLAUDE.md` | The router. If anything disagrees, this wins |
| `README.md` | 304 lines. Use cases, benefits, where the brain runs |
| `llms.txt` | Machine-readable index |
| `context/HealthPlanChat_GTM_Master_Context.md` | 307 lines. The distilled source of truth |

### 2.2 The rules layer

| File | Enforces |
|---|---|
| `rules/glossary.md` | Canonical vocabulary |
| `rules/feature-status.md` | What may be promised. Shipped vs roadmap |
| `rules/do-not-say.md` | Claim hygiene. Every prohibition carries a replacement |
| `rules/writing-rules.md` | How every word is written |

### 2.3 The reference layer

Fifteen files distilling the Sprint 1 analysis into working documents: positioning,
positioning verdict, ICP personas, competitive analysis, competitor battlecards, feature
matrix, value propositions for both ICPs, customer journey, marketing campaigns, outbound
engine, pricing model, job-signal search, plan change report.

### 2.4 Templates and examples

| Deliverable | Status |
|---|---|
| `templates/cold-outreach-icp1.md` | In repo, 353 lines |
| `templates/linkedin-outreach-icp2.md` | In repo |
| `templates/landing-page.md` | In repo — **a template, not a page.** See 5.1 |
| `templates/nurture-email.md` | In repo |
| `templates/community-post.md` | In repo |
| `examples/cold-outreach-icp1-approved.md` | In repo |
| `examples/linkedin-icp2-approved.md` | In repo |

### 2.5 Operating ledgers

`ops/QA-checklist.md` · `ops/decisions.md` · `ops/signal-log.md` · `ops/asset-index.md` ·
`ops/copy-bank.md` · `ops/review-cadence.md` · this file.

### 2.6 Multi-agent portability

| Deliverable | For |
|---|---|
| `adapters/INSTALL.md` | 176 lines. How to install the brain anywhere |
| `adapters/portable-control-layer.md` | The portable spec |
| `adapters/cursor.mdc` · `GEMINI.md` · `copilot-instructions.md` · `windsurf.md` · `generic-rule-file.md` | Per-agent rule files |
| `AGENTS.md` | The agent-facing entry point |
| `prompts/common-tasks.md` | Ready prompts for recurring jobs |

---

## 3 · Sprint 2 — the outbound build

Everything from the sourcing spec through a live, measured campaign.

### 3.1 The two Claude skills

Handed over as `.skill` files. Deliberately kept out of the repo.

| Skill | Contents | Status |
|---|---|---|
| **`clay-icp-sourcing`** | `SKILL.md` · `references/exclusion-classes.md` · `references/prompt-patterns.md` · `scripts/audit_companies.py` · `scripts/audit_people.py` | Handed over |
| **`instantly-spintax`** | `SKILL.md` · `scripts/spintax_lint.py` | Handed over |

Both synced to SOP v3.0 on 2026-09-28.

### 3.2 The playbook

| Deliverable | Status |
|---|---|
| `ops/outbound-sop.md` — 1,563 lines, 15 steps, 3 tool manuals, 13 appendices | In repo |
| `reference/job-signal-search.md` — 1,173 lines, the sourcing spec and prompt patterns | In repo |
| `reference/plan-change-report.md` — what D3 is and how it is built | In repo |
| The recorded SOP video walkthrough | Shipped by the founder. SOP v3.0 matches it step for step |

### 3.3 The prompts

| Prompt | Where |
|---|---|
| Company-name cleaning | SOP Appendix C |
| LinkedIn prioritisation tiering | SOP Appendix D |
| ICP fit gate | `reference/job-signal-search.md` |
| Website carrier/plan extraction | `reference/job-signal-search.md` |

### 3.4 Campaign assets

| Deliverable | Status |
|---|---|
| Cold email body, spun to 729 combinations, linted clean | In repo, `templates/cold-outreach-icp1.md` |
| Four subject line variants | In repo |
| Static fallback message | In repo |
| LinkedIn connection request, founder voice, under 300 characters | In repo |
| Two-step post-acceptance LinkedIn sequence | In repo |

### 3.5 Lists and data

| Deliverable | Rows | Status |
|---|---|---|
| `icp-triage.csv` — 82 companies triaged, 72 delete / 4 verify / 6 keep | 82 | Handed over |
| `split-A-request-with-note.csv` | 739 | Handed over |
| `split-B-plain-request.csv` | 740 | Handed over |

### 3.6 Reporting

| Deliverable | Status |
|---|---|
| Campaign Numbers — published page | Shipped, `claude.ai/artifact/9iDjfrpT5t8P41bzSmndVw` |
| AEP Outbound Stack — 16:9 stack map for the Loom background | Shipped, `claude.ai/artifact/J9QkyWkjEkmgQJuQAi2hid` |
| `campaign-debrief.mmd` — Mermaid debrief | Handed over |
| `stack-map.mmd` — Mermaid stack map, vertical | Handed over |

### 3.7 Lead work

| Deliverable | Status |
|---|---|
| Battle card — Lawrence Lee, Solomon Agency (docx) | Handed over |
| Lead profile — Lawrence Lee, Solomon Agency (docx) | Handed over |
| Lookalike campaign metadata from that reply | Handed over |

### 3.8 Measured results

| Measure | Value |
|---|---|
| Contacted, email | 982 |
| Replies | 29 |
| Response rate | 2.95 per cent of list |
| **Replies carrying a phone number** | **96.6 per cent — 28 of 29** |
| LinkedIn A/B split | 739 / 740 |
| Companies removed at triage | 72 of 82 |
| ICP TAM, modelled | 12,100 to 24,200 companies |

---

## 4 · Where everything lives

| Location | Holds | Access |
|---|---|---|
| `Fit137/Health-Plan-Chat-GTM-Brain` | The brain, the SOP, all rules and templates | Public |
| `Fit137/HealthPlanChatsprint1build` | Sprint 1 analysis, the six deliverables, the walkthrough | Private |
| `saasrelaunch/Health-Chat-Plan-GTM-Brain` | Delivery copy of the brain | Public. **Not inventoried here** |
| `Fit137/Health-Plan-Chat-consulting-call` | Pre-sprint discovery | Private. **Not inventoried here** |
| Published pages | Three artifacts, listed above | Link-shared |
| Direct file handovers | Skills, CSVs, docx, mermaid | **Not recorded anywhere.** See 5.5 |

---

## 5 · Specified but not built

Everything below is written down in full and has no built artifact. Each is a real gap,
not an oversight in the specification.

### 5.1 Landing page

| | |
|---|---|
| Spec | `templates/landing-page.md` — nine sections, price block correctly absent |
| Copy source | `reference/value-proposition-icp1.md` |
| Status | **Spec only.** `ops/asset-index.md` records the website as "Not built" |
| Blocked by | **GAP-1.** Section 3 of the page is the demonstration — a real question and a real answer with its source cited. No verbatim transcript of a plan-grounded answer exists. Without it an agent either guts the page or fabricates a product claim |
| Also blocked by | OF-1 for the pricing block |

### 5.2 D2 Missed-Call Revenue Calculator

| | |
|---|---|
| Spec | `sources/extracted/assets-library.md` line 92, and `sources/extracted/product-feature-matrix.md` |
| What it does | Monthly inbound volume, rough % missed, state → annualised lost commission on published 2026 CMS rates, split into after-hours and answered-but-unresolved |
| Build estimate in the spec | 2 weeks build, 1 week to first data |
| Needs | The 2026 CMS rate table by state, an ad account, title and company-size targeting |
| QA bar in the spec | Arithmetic verifiable against the published CMS rate release |
| Status | **Spec only.** `ops/asset-index.md`: LinkedIn ads "Not started. Needs the D2 calculator built" |

### 5.3 Pitch deck

| | |
|---|---|
| What is specified | A **partner pitch deck, 10–12 slides**, for the ICP-2 FMO co-marketing motion. `sources/extracted/assets-library.md` line 100 |
| Build estimate in the spec | 3 weeks including partner negotiation |
| Needs | One FMO partner agreement and a downline roster |
| Status | **Spec only** |
| **A "custom pitch deck generator"** | **No specification exists anywhere in either repo.** If this was scoped, it was scoped outside the repos and nothing records it. It needs defining before it can be built |

### 5.4 The remaining drivers

| Driver | Status |
|---|---|
| D1 Medicare AI Readiness Scorecard | Spec only |
| **D3 2027 Plan Change Report** | Method defined in `reference/plan-change-report.md`. **Delivery is manual, founder-run.** No machinery built |
| D4 72-Hour Plan Brain Sandbox | Manual, 72-hour turnaround |
| D5 CMS AI Exposure Review | Spec only |
| D6 AEP Peak-Load Stress Test | Spec only |

### 5.5 Not recorded anywhere

Everything in 3.1, 3.5, 3.7 and part of 3.6 was handed over as a file or a link and lives
in no repository. If a laptop is lost or a chat is cleared, it is gone.

- [ ] Collect the skills, CSVs, docx files and mermaid sources into a `deliverables/`
      directory in one of the repos.

---

## 6 · What unblocks what

Two open items gate most of section 5.

| Item | Question | Unblocks |
|---|---|---|
| **OF-1** | Is $499 the price, and when does it publish? | Funnel stage 4, the pricing page, the landing page price block, the copy bank, the nurture sequence |
| **GAP-1** | What does a plan-grounded answer look like, verbatim? | The landing page demonstration, the sandbox handover, the "what it will and won't say" one-pager, and the sales conversation. **One captured transcript closes all four** |

Both are owned outside this brain. Neither is a build.
