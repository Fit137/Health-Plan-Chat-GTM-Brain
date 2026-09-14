---
name: instantly-spintax
description: Convert a plain cold email or LinkedIn message into sequencer-safe spintax, with subject line variants, a de-spun plain set, and a static fallback. Use this whenever someone is preparing outbound copy for Instantly.ai, Smartlead, Lemlist, Woodpecker or any tool that uses {{ }} for merge variables, mentions spintax or spin syntax, asks to "spin" or "randomise" a message, wants subject line variants for cold email A/B testing, needs a fallback message, or hits a template warning that a variable "could not be resolved". Reach for it proactively when a first cold email is about to go out at volume, because identical copy across thousands of sends is a deliverability problem before it is a copy problem.
---

# Spintax for Instantly and friends

A sequencer rewrites one message into thousands of near-identical sends. Mailbox providers
notice identical bodies. Spintax varies the wording so the sends differ, without the writer
maintaining a thousand drafts.

The trap is that **Instantly uses `{{ }}` for merge variables and for spin blocks**. One
delimiter, two meanings, and the parser decides which by looking for a pipe. Almost every
failure below comes from a block that the parser gave up on and treated as a variable name,
producing the unhelpful warning *"{{...}} could not be resolved for this lead."*

## What to produce

Unless the request is narrower, return all five:

1. **The spun body**, with its combination count.
2. **Three or four spun subject lines**, each carrying a merge variable.
3. **The same subject lines de-spun** — first option of each block, variables kept — because
   people paste these into A/B slots one at a time.
4. **A static fallback**: no variables at all, for when a merge field fails to resolve.
   Instantly requires one as soon as the copy uses anything beyond simple variables.
5. **The linter output**, so the user can see it passes before pasting.

## The five rules that break sends

Each of these came from a real template failure, not from documentation.

**Punctuation never goes inside a block.** Not leading, not trailing. A comma, full stop,
colon or question mark inside any option makes the parser read the whole block as a variable
name. `{{the call volume.|the volume.}}` fails. Write `{{the call volume|the volume}}.` and
let the mark sit bare outside.

**Blocks never touch.** `}}{{` reads as one malformed variable. Separate with a space, or
with the bare punctuation mark that belongs there anyway.

**Variables never sit inside a block.** `{{Hi {{first name}}|Hello {{first name}}}}` cannot
parse. Keep the variable outside and spin around it.

**Meaning never moves.** Spin the connective phrasing only. Proper nouns, numbers, dates,
the core claim, the product category and the ask all stay fixed, so that every render says
the same thing. A date may vary in *format* — `October 15 | Oct 15 | October 15th` — because
that changes no meaning. If two options would make a prospect reply differently, they are not
alternatives, they are two different messages.

**Every option is a real alternative.** A block of identical options, `{{for|for|for}}`,
satisfies a rule and achieves nothing. Where a connective word needs to be inside a block,
absorb it into a neighbouring one instead: not `{{a record AEP}} {{for|for}}` but
`{{a record AEP for|a record-setting AEP for|your biggest AEP for}}`.

## How to build it

Work through the plain message once, in order.

**Mark the fixed spans first.** Names, dates, numbers, the product noun, the ask. These
never enter a spin block except where a pure format variant exists.

**Group the rest into phrase blocks, not word blocks.** Spinning single words produces
combinations that read like a thesaurus accident. Spinning three-to-six word phrases keeps
every render grammatical, because each option is independently well-formed. `{{could kick
off|could be the start of|could mark the start of}}` is safe in a way that
`{{kick|start|begin}}` is not.

**Absorb connectives and punctuation outward.** Trailing prepositions go inside the block
before them. Punctuation goes outside every block. Where a mark follows a variable, it simply
sits bare — a variable cannot carry it.

**Aim for three options per block.** Three across six blocks is 729 combinations, which is
past the point where repetition is visible at any realistic send volume. Going to five options
per block buys a bigger number and a worse worst-case render.

**Then lint it.** See below. Do not hand over copy you have not run through the script.

### Spin-heavy requests

When the user asks for every word inside a block, the goal is no bare *words*, not no bare
*characters*. Punctuation stays outside, because putting it in is the first rule's failure.
Achieve it by absorbing connectives into adjacent blocks, and run the linter with `--strict`,
which reports any word left loose.

## Subject lines

Write three or four with different angles rather than one idea reworded — a date line, a
company-first line, a topic line, an outcome line. The point of the set is to learn which
angle works, which needs the angles to actually differ.

Each should carry a merge variable, and company name usually beats first name in a subject:
it reads as research rather than as mail-merge.

Keep subject spin light. Two or three options per line is plenty, and a subject that changes
too much across sends stops being a test of one thing.

**Check the subject against the campaign's own rules before writing it.** Many outbound
playbooks bar particular words from subject lines; in this repo, `reference/outbound-engine.md`
bars "AI" there. Read the project's channel rules if the repo has them.

## The fallback

Same message, every variable removed, no spin. Replace a company variable with a neutral
stand-in such as "your agency" or "your team", and drop the name greeting rather than
replacing it — a bare "Hi there," reads worse than opening on the first real sentence.

## Lint before you ship

```bash
python scripts/spintax_lint.py --file body.txt
python scripts/spintax_lint.py --text "..." --strict --samples 5
python scripts/spintax_lint.py --file body.txt --var "company name=Acme Benefits"
```

It reports the combination count, flags every failure mode above, and prints sample renders
with variables filled in. Exit code 1 on any error, so it can gate a build step.

The samples matter as much as the errors: read three or four and check they are sentences a
person would send. The linter cannot tell you a combination reads badly, only that it parses.

## Worked example

Plain input:

> John, October 15 could kick off a record AEP for America First Healthcare. AI can help you
> handle the increased call volume. May I show you how?

Spun body, 729 combinations:

```
{{first name}}, {{October 15|Oct 15|October 15th}} {{could kick off|could be the start of|could mark the start of}} {{a record AEP for|a record-setting AEP for|your biggest AEP for}} {{company name}}. {{AI can help you handle|AI can help you take on|AI can help you cover}} {{the increased call volume|the jump in call volume|the extra call volume}}. {{May I show you how|Can I show you how|Want me to show you how}}?
```

Note what did not move: the date's meaning, "AEP", "AI", and the ask. Note where the
punctuation sits: outside every block. Note that "for" rides inside the block before it
rather than standing alone.

Subject lines, spun:

```
{{October 15 at|October 15 for|Oct 15 at}} {{company name}}
{{company name}} {{before October 15|ahead of October 15|before Oct 15}}
{{AEP call volume at|AEP prep at|the AEP rush at}} {{company name}}
{{a record AEP for|a record-setting AEP for|your biggest AEP for}} {{company name}}
```

De-spun, for pasting one at a time:

```
October 15 at {{company name}}
{{company name}} before October 15
AEP call volume at {{company name}}
a record AEP for {{company name}}
```

Fallback, no variables:

```
October 15 could kick off a record AEP for your agency. AI can help you handle the increased call volume. May I show you how?
```
