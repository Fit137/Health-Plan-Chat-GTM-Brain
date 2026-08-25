# Health Plan Chat — Go-to-Market Brain

A plain-text repository holding Health Plan Chat's entire go-to-market in a form an AI
agent can load and execute against without re-deriving anything, and a human can use as a
command centre for decisions.

It is content and context, not application code.

## What Health Plan Chat is

A consumer-facing AI voice and chat agent for independent Medicare insurance agencies,
trained on the specific Medicare plans each agency sells.

A beneficiary calls the agency's own number at nine on a Sunday and asks what their dental
allowance is. The agent answers from that agency's carrier documents, in the agency's
name, applies the required disclaimers, records the call, and either resolves the question
or hands to a licensed agent with the full conversation attached.

## Why the go-to-market is shaped this way

Two findings, and everything follows from them.

**One.** Twenty-five features were scored on demand and differentiation, then independently
classified by what it takes to build them — commodity AI, insurance workflow, or Medicare
plan IP. The two methods produce the same six features. All six top-quadrant
differentiators are Medicare plan IP; none of the fourteen commodity features reaches the
top quadrant. So anything a $79/month AI receptionist also does is not a story worth
telling.

**Two.** The only competitor with comparable Medicare depth starts around $10,000 a month,
behind a demo gate. The entire 2–25 agent independent segment is not being sold to by the
one product that could serve it. That makes the wedge a pricing wedge before it is a
product wedge.

## How it is organised

| Folder | What it holds | When it loads |
|---|---|---|
| `CLAUDE.md`, `AGENTS.md`, `llms.txt` | Routers. Load order and non-negotiables | Every session |
| `context/` | The master context, everything distilled into one read | Strategy questions |
| `rules/` | Glossary, status ledger, claim ledger, writing rules | **Every writing task** |
| `reference/` | One file per source artifact, plus battlecards, objections and the channel engine | On demand |
| `templates/`, `examples/`, `prompts/` | How work gets produced fast and on-voice | Production |
| `ops/`, `snapshots/` | Decisions, signals, approved copy, the QA gate, review cadence | State and review |
| `adapters/` | One pointer per tool, so guardrails reach everyone | Tool setup |
| `sources/` | The originals and their extracts | When a claim is questioned |

## What it is for

- Producing on-voice assets without briefing anyone.
- Stopping agents and hurried humans from overclaiming — which in a CMS-regulated market
  is a compliance exposure, not a marketing error.
- Keeping strategy out of one person's head.
- Compounding: every call note, objection and competitor move goes into the ledgers, so
  the brain sharpens with use instead of going stale.

## Where the return comes from

Three places. Assets stop being briefed from scratch, so production cost falls. Claims
stop needing legal review one at a time, because the claim ledger has already done the
scoping. And settled decisions stop being relitigated — `ops/decisions.md` records not
just what was decided but what each decision did *not* change, which is the part that
usually causes the re-argument.

## Read this before using it

The `status_notes` field at the top of
`context/HealthPlanChat_GTM_Master_Context.md` is the most important line in the
repository. It says what you may not assume. Right now it says: pre-revenue, no customers,
price not published, two table-stakes capabilities not shipped, three capabilities
unverified, SOC 2 not held.

An asset that ignores any of those is not a draft with a mistake in it. It is a claim the
company cannot stand behind.

## Maintenance rule

**Ledgers before copy, always.** When a capability ships, a price publishes, or a
competitor moves, update the ledger first and let the copy follow. Never the other way
round.

Review cadence and staleness thresholds: `ops/review-cadence.md`. The status ledger has
the shortest fuse at 30 days, because it is the file most likely to be wrong after a
release and the one where being wrong costs most.

## Built with

The [GTM Brain skill](https://github.com/alielshenawy1/Ali-GTM-Brain-Skill), from the
Sprint 1 research in `Fit137/HealthPlanChatsprint1build`. Source manifest and conflict
resolutions: `ops/asset-index.md`.
