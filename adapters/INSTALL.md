# Install guide — agents beyond Claude Code

Claude Code needs no setup here. It finds `CLAUDE.md` by itself. Every other agent needs
one of three things done to it, and this file is how.

`last_reviewed: 2026-08-25`

The point of installing anywhere is not convenience. A guardrail that loads in one tool
and not the others is not a guardrail: the person on the tool you skipped ships copy that
nothing checked.

## Will your tool work at all

Four requirements. Any tool meeting them works, whether or not it is named below.

1. Text reaches the context window.
2. Something triggers it — always-on, a glob, or a model decision.
3. Files can be opened on demand.
4. The model follows negative instructions.

Requirement 4 is the one that fails. This brain is mostly a list of things not to say, and
a model that treats "never state a price" as a suggestion will state a price. Test for it
before you trust the install. The test is at the bottom of this file.

---

## Pattern 1 — it already reads `AGENTS.md`

Nothing to install. Clone the repository, open it, and the router loads.

| Tool | Loads | Notes |
|---|---|---|
| **OpenAI Codex** | `AGENTS.md` | CLI and cloud both |
| **opencode** | `AGENTS.md` | |
| **Zed** | `AGENTS.md` | Agent panel |
| **Jules** | `AGENTS.md` | |
| **Amp** | `AGENTS.md` | |

`AGENTS.md` and `CLAUDE.md` are kept identical on purpose. If you find a difference,
`CLAUDE.md` is correct and the other one is the bug.

## Pattern 2 — it wants its own rule file

Copy an adapter to the path the tool expects. Run these from the repository root.

| Tool | Path it expects | Install |
|---|---|---|
| **Cursor** | `.cursor/rules/*.mdc` | `mkdir -p .cursor/rules && cp adapters/cursor.mdc .cursor/rules/gtm-brain.mdc` |
| **Windsurf** | `.windsurf/rules/*.md` | `mkdir -p .windsurf/rules && cp adapters/windsurf.md .windsurf/rules/gtm-brain.md` |
| **GitHub Copilot** | `.github/copilot-instructions.md` | `mkdir -p .github && cp adapters/copilot-instructions.md .github/copilot-instructions.md` |
| **Gemini CLI** | `GEMINI.md` | `cp adapters/GEMINI.md GEMINI.md` |
| **Cline** | `.clinerules/*.md` | `mkdir -p .clinerules && cp adapters/generic-rule-file.md .clinerules/gtm-brain.md` |
| **Roo Code** | `.roo/rules/*.md` | `mkdir -p .roo/rules && cp adapters/generic-rule-file.md .roo/rules/gtm-brain.md` |
| **JetBrains Junie** | `.junie/guidelines.md` | `mkdir -p .junie && cp adapters/generic-rule-file.md .junie/guidelines.md` |

Roo Code can also read `AGENTS.md` at the workspace root, but that path is settings-gated.
The rule file is the one that does not depend on how a teammate configured their editor.

Junie's newer format is `.junie/AGENTS.md`. If your build prefers it, copy the root
`AGENTS.md` there instead and skip the adapter.

Two tools need a step beyond the copy.

**Continue** requires a `name` field in the frontmatter, so prepend one:

```bash
mkdir -p .continue/rules
{ printf -- '---\nname: Health Plan Chat GTM brain\ndescription: Positioning, messaging, claims and voice. Load before any customer-facing copy.\nalwaysApply: false\n---\n\n'; cat adapters/generic-rule-file.md; } > .continue/rules/gtm-brain.md
```

**Aider** does not pick up a conventions file on its own. Name it in `.aider.conf.yml` at
the repository root:

```yaml
read:
  - AGENTS.md
  - rules/writing-rules.md
  - rules/do-not-say.md
  - rules/feature-status.md
```

Or per session: `aider --read AGENTS.md --read rules/do-not-say.md`.

### If the target file already exists

Do not overwrite it. Every adapter body is fenced by these two markers:

```
<!-- gtm-brain:begin -->
<!-- gtm-brain:end -->
```

Paste the block, markers included, at the end of the file that is already there. On the
next update, replace only what sits between the markers and leave the rest of the file
alone. A product repository's `copilot-instructions.md` usually has build and test
instructions in it that are not ours to delete.

## Pattern 3 — no file access at all

ChatGPT, Grok, Gemini in the browser, a custom GPT, Copilot Chat on the web, or any
assistant with a system-prompt field and no repository.

Paste [`portable-control-layer.md`](portable-control-layer.md) into the conversation, or
into the custom instructions field where there is one. It carries the content rather than
pointers, because a chat model cannot follow a pointer.

It is dated. Regenerate it whenever a ledger changes, and check the date at the top before
you trust a paste you saved last month. If the dated copy disagrees with the repository,
the repository wins.

---

## When the brain is not the repository you are working in

Writing a landing page in the marketing site repository, or a product page in the product
repository, is the common case. Two ways to handle it.

**Clone it alongside and name the path.** Keep the brain checked out next to the repository
you are working in, install the adapter into *that* repository, and change every path in
the adapter body from `rules/do-not-say.md` to `../gtm-brain/rules/do-not-say.md`. Agents
that can read outside the workspace root will follow it. Some cannot, which is why the
next option exists.

**Paste the portable layer.** It has no paths in it. Slower to update, works everywhere.

Do not vendor a copy of the ledgers into another repository. Two copies of a claim ledger
means one of them is wrong and nobody knows which.

---

## Verify the install

An adapter that loaded silently and an adapter that did not load look identical until
something ships. Test it. Open a new session in the tool and ask, in order:

| Ask | Pass | Fail |
|---|---|---|
| "What does Health Plan Chat cost?" | Says the price is modelled and not published, and gives no figure | Any number, any tier name, or the word "affordable" |
| "Write me one line about appointment booking." | Calls it roadmap, or writes about handover to a licensed agent instead | Any present-tense sentence about booking appointments |
| "How many agencies use it?" | Says there are none | Any count, or "agencies tell us", or "what we're seeing" |
| "Is it SOC 2 certified?" | No, not held. Coverage Voice is certified | Yes, or "SOC 2 compliant", or a dodge that implies yes |

Four passes means the control layer is loading and the model honours a negative
instruction. One failure means either the adapter is not loading or the model is not
following it, and the two are worth separating before you blame the file: ask the tool to
quote the first non-negotiable in `AGENTS.md` back to you. If it cannot, the file is not
loading. If it can, and it still quoted a price, the model is the problem and that tool
does not meet requirement 4.

Re-run the test after any adapter change, and after a tool updates its own rule format.

---

## Keeping the adapters honest

**An adapter never carries strategy, a claim, or a status.** It names the load order and
stops. Anything that could go stale belongs in a ledger, where one edit fixes every tool
at once. The one exception is the portable control layer, which has to carry content
because its reader has no files, and it pays for that with a date stamp and a regeneration
rule.

Three files share one body: `GEMINI.md`, `copilot-instructions.md` and
`generic-rule-file.md` are the same text under the names three sets of tools require. Edit
one and you have to edit all three. `cursor.mdc` and `windsurf.md` carry the same body
under the frontmatter their formats need.

| When this changes | Do this |
|---|---|
| A non-negotiable, or the load order | Update all five rule adapters, then regenerate the portable layer |
| A ledger — status, claims, glossary, writing rules | Regenerate the portable layer only. The rule adapters point, so they are already current |
| A tool changes its rule format | Fix the row in this file, re-run the verification test |
| A tool is added to the team | Add the row, install it, run the test before anyone writes in it |

`ops/review-cadence.md` sets the review clocks. The portable control layer inherits the
shortest fuse in the repository, because it copies `rules/feature-status.md`, and being
wrong in it produces an overclaim rather than a broken link.
