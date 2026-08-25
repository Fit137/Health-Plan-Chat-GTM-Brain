# Asset index

Where everything lives, and what each source artifact settles.

`last_reviewed: 2026-08-25`

## Source manifest

Every artifact this brain was built from, and the decision it settles.

| Artifact | Type | What it settles | Dated | Distilled into |
|---|---|---|---|---|
| Product Feature Matrix | xlsx, 8 sheets | What leads messaging and what is entry cost | 2026-08 | `reference/feature-matrix.md`, `rules/feature-status.md` |
| `feature-scores.csv` | csv, 25 rows | The scores, layers and quadrants | 2026-08 | `reference/feature-matrix.md` |
| Competitive Market Analysis | xlsx / md, 15 sections | Market shape, the wedge, the price finding | 2026-08 | `reference/competitive-analysis.md`, `reference/competitor-battlecards.md` |
| Positioning Dashboard | md | The four vectors and which two we lead | 2026-08 | `reference/positioning.md`, `reference/positioning-verdict.md` |
| ICP Dashboard | xlsx / md | Both ICPs, committee personas, design partner profile | 2026-08 | `reference/icp-personas.md` |
| Value Proposition Framework | docx, 12 tables | Brand promise, 3 pillars, 9 reasons to believe | 2026-08 | `reference/value-proposition-icp1.md`, `ops/copy-bank.md` |
| Customer Journey Funnel | xlsx, 3 sheets | Seven stages, both funnels, the three exposures | 2026-08 | `reference/customer-journey.md` |
| Marketing Assets Library | xlsx / md | Seven campaigns, the driver-by-channel mapping | 2026-08 | `reference/marketing-campaigns.md`, `reference/outbound-engine.md` |
| Pricing model | xlsx, 9 tabs + md | How the price was derived. **Not a decision** | 2026-08 | `reference/pricing-model.md` (internal only) |
| `OPEN-FINDINGS.md` | md | Three live findings that revise the source sheet | 2026-08-24 | `rules/do-not-say.md`, `ops/decisions.md`, `ops/signal-log.md` |

## Conflicts found and how they were resolved

**Feature 25 competitiveness.** The source sheet scores centralised multi-agency
deployment at +17.4 on the explicit basis that nobody else offers it. Coverage Voice's own
published material falsifies that basis. **Resolved in favour of the competitor's
published material.** The verdict is recorded in `ops/decisions.md`; the CSV still carries
the original score with an inline flag, pending the founder applying it. Anyone reading
`feature-scores.csv` directly will see the stale number — read
`reference/feature-matrix.md` instead.

**Three product capabilities.** A third-party research pass attributes provider lookup,
consent capture and accessibility-oriented design to Health Plan Chat. The source feature
sheet does not, and marks provider lookup *absent* for us. **Resolved in favour of the
source sheet**, flagged UNVERIFIED rather than silently dropped, because the research pass
might be right and the product team can settle it in a minute.

**Positioning vectors 1 and 2.** The Sprint 1 brief invited a strategy built on the
vectors competitors lead. The feature analysis contradicts it. **Resolved explicitly with
the founder** rather than silently — full reasoning in `reference/positioning-verdict.md`,
including the counter-argument, kept on purpose.

## Where the originals live

- `sources/raw/` — the six Google-folder deliverables plus the pricing workbook, as
  delivered.
- `sources/extracted/` — the canonical Markdown and CSV each was rendered from. **These
  are the authoritative text**, not transcriptions of the spreadsheets: the spreadsheets
  were generated from them.
- Upstream repository: `Fit137/HealthPlanChatsprint1build`, branch
  `claude/product-feature-matrix-gtm-8tg5m3`, directory `gtm/`.
- Presentation-format renderings: `gtm/presentation/` in that repository.

## Product surfaces

| Surface | Status |
|---|---|
| Website | Not built. Blocked in part on OF-1 |
| Pricing page | **Does not exist.** The single largest funnel unblock |
| Gap Report delivery | Manual, founder-run |
| Sandbox environment | Manual, 72-hour turnaround |
| CRM integration | Per-agency at onboarding |

## Channels

| Channel | Status | Owner |
|---|---|---|
| Personalised cold outreach | Primary, founder-led | Founder |
| Agent communities and forums | Not started. Compounds slowly, so start early | GTM |
| AEP prep webinar | Not started. Needs ≥15 audits first | GTM |
| LinkedIn outreach, ICP-2 | Not started. Needs an ICP-1 reference | Founder |
| LinkedIn ads, ICP-2 | Not started. Needs the D2 calculator built | GTM |
| FMO co-marketing | Not started. Needs a partner agreement | Founder |
| Website and email nurture | Not started. Blocked on the site | GTM |

## Related engagements

Design partner recruitment. Window is **February to mid-September**; from 15 October to
7 December agency owners are unreachable. This window, not the roadmap, is the binding
constraint on Sprint 1.
