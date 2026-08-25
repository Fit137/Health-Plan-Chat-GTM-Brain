# Review cadence

Who reviews what, how often, and when a file is stale enough to stop trusting.

`last_reviewed: 2026-08-25`

## The cadence

| File | Reviewed | Owner | Stale after |
|---|---|---|---|
| `rules/feature-status.md` | **Every release**, and monthly regardless | Product | **30 days** |
| `rules/do-not-say.md` | Monthly, and on any competitor move | GTM | 60 days |
| `ops/signal-log.md` | **Weekly** in the selling window, fortnightly during AEP | GTM | 14 days |
| `ops/decisions.md` | Monthly | Founder | 90 days |
| `ops/copy-bank.md` | On any ledger change | GTM | 60 days |
| `reference/competitive-analysis.md` | Quarterly, and on any competitor launch | GTM | 90 days |
| `reference/competitor-battlecards.md` | Quarterly | GTM | 90 days |
| `context/…Master_Context.md` | Quarterly, and after any decision | Founder | 90 days |
| `rules/glossary.md` | Quarterly | GTM | 180 days |
| `rules/writing-rules.md` | Quarterly | GTM | 180 days |
| `snapshots/` | Monthly capture | GTM | — |

## Why the status ledger has the shortest fuse

Thirty days, tightest in the brain, for two reasons. It is the file most likely to be
wrong after a release, and being wrong in it produces an overclaim — which in a
CMS-regulated market is a compliance exposure rather than a marketing error.

The maintenance rule: **update the ledger before the copy follows.** Never the reverse.

## Seasonal adjustment

This business has a hard calendar. The cadence bends to it.

**February to mid-September — the selling window.** Full cadence. Weekly signal triage.
This is when market contact happens and when the log actually fills.

**15 October to 7 December — AEP.** Agency owners are unreachable, so new signal volume
collapses. Drop signal triage to fortnightly. **Do not drop the status ledger review** —
this is exactly when a shipped capability gets claimed too early because everyone is busy.

**January.** Reset. Full re-read of the master context and every ledger before the
selling window opens, because plan-year changes have invalidated every benefit example in
the copy bank.

**That January re-read is not optional.** Benefits change annually. Any undated benefit
example in customer-facing copy is wrong by January and reads as incompetence to this
audience.

## Trigger-based reviews, independent of cadence

Run immediately, whatever the calendar says:

- **Any release** → status ledger, then every file whose copy the change touches.
- **Any competitor launch or pricing change** → competitive analysis, battlecards,
  do-not-say.
- **Any lost deal** → signal log, and objection handling if the reason is new.
- **OF-1 closing (price published)** → copy bank, landing page template, nurture
  sequences, objection handling, QA checklist, master context `status_notes`. This one
  touches almost everything.
- **Any of Q-1, Q-2, Q-3 answered** → do-not-say, feature status, master context.
- **First design partner signed** → `status_notes` ("no customers" stops being true),
  copy bank proof points, objection handling ("who else uses this").

## What a review actually is

Not a read-through. Three questions per file:

1. Is anything in here now false?
2. Is anything true but no longer the thing we would lead with?
3. Did anything change since last review that should be in here and is not?

If all three are no, stamp `last_reviewed` and move on. The stamp is the deliverable.

## Staleness is checkable

`scripts/audit_brain.py` in the skill reads `last_reviewed` and flags anything past its
threshold. Run it monthly alongside the ledger reviews.
