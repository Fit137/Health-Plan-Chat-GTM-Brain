# QA checklist — the pre-ship gate

Run before anything goes to a customer, a prospect, or the public. Every item is
mechanical: if you cannot tick it, it fails.

This is the tickable mirror of the four files in `rules/`. If a rule cannot be checked
here, it is not a rule yet.

---

## Claims — the ones that carry real exposure

- [ ] **No price appears anywhere.** No figure, no tier name, no "starting at". Until
      OF-1 closes, this is absolute.
- [ ] **Every capability mentioned carries the right tense for its flag** in
      `rules/feature-status.md`. Nothing IN BUILD, ROADMAP or UNVERIFIED is written in the
      present tense.
- [ ] **Appointment booking is not claimed or implied.** ROADMAP.
- [ ] **SOA capture is not claimed or implied.** ROADMAP.
- [ ] **Provider lookup, consent capture and accessibility design do not appear.**
      UNVERIFIED.
- [ ] **No SOC 2 claim.** Not held. If security is discussed, the honest posture appears.
- [ ] **HIPAA appears only as "HIPAA-aligned handling"**, never as compliance or
      certification, and only alongside specifics.
- [ ] **No customer count, logo, testimonial, case study, or vague plural** implying
      customers. There are none.
- [ ] **Multi-agency deployment is not described as unique.** OF-2.
- [ ] **Every superlative** — only, first, best, never, always, no other — has been
      checked against `rules/do-not-say.md` and appears in its scoped form.
- [ ] **Every outcome number is labelled as modelled**, with its unit and its date.
- [ ] **Any competitor claim is accurate**, states their genuine strength, and does not
      repeat a fact in the "commonly misremembered" list.

## Audience and stage

- [ ] The asset serves **exactly one ICP**. No blending.
- [ ] If ICP-1: **no mention** of procurement, security review, or annual terms.
- [ ] If ICP-2: **no mention** of month-to-month pricing or "no demo required".
- [ ] The funnel stage is clear and the call to action matches it.
- [ ] The call to action is **not "book a demo"**.
- [ ] There is exactly **one** call to action.

## Channel

- [ ] The channel is in the approved mix (`rules/writing-rules.md` §5).
- [ ] If community or forum: the value is ungated and the vendor affiliation is disclosed.
- [ ] If paid social: targeting is by job title and company size, **never** beneficiaries.
- [ ] If a benchmark is quoted: sample is **≥ 15 agencies** and no individual agency is
      named without consent.
- [ ] No carrier or plan named in a way that implies endorsement.

## Naming and vocabulary

- [ ] "Health Plan Chat" — three words, capitalised, no abbreviation.
- [ ] "Beneficiary" for the person on Medicare, never patient or customer.
- [ ] "Plan corpus", not knowledge base or training data.
- [ ] No banned near-synonym from `rules/glossary.md`: chatbot, bot, receptionist,
      patient, Medicare-approved, enrol the caller.
- [ ] Acronyms spelled out on first use: AEP, FMO, GA, SOA, TPMO.

## Writing mechanics

- [ ] No banned word: seamless, revolutionary, cutting-edge, game-changer, unlock,
      leverage, elevate, supercharge, robust, holistic, best-in-class, world-class,
      effortless, delve, tapestry, testament.
- [ ] **No exclamation marks.**
- [ ] At most one em-dash, and it does real work.
- [ ] No rhetorical-question headline.
- [ ] Paragraphs under four lines.
- [ ] Specifics, not adjectives. Every "comprehensive" or "powerful" replaced with the
      actual thing.
- [ ] Every number carries its unit and its date.
- [ ] Any benefit example carries its plan year.

## Spoken and video only

- [ ] TPMO disclaimer, automated-system disclosure and recording notice are stated in
      full, not implied, and were not cut for pacing.
- [ ] Nothing IN BUILD, ROADMAP or UNVERIFIED is shown on screen or narrated as live.
- [ ] No demo shows an appointment being booked.

## Voice

- [ ] Compare against the matching file in `examples/`. Does it sound like the same
      company?
- [ ] Would a licensed agent who has been sold to badly for a decade find this
      condescending, over-enthusiastic, or vague? If any of the three, rewrite.
- [ ] Remove the company name. Is the asset still obviously worth reading? If not, it is
      about us rather than about them.

---

## The three that fail most often

Watch these specifically, because they are the ones that get through:

1. **A price slipping in** as "affordable", "a fraction of", or "starting at". All three
   are price claims.
2. **A roadmap capability in the present tense**, usually appointment booking, usually in
   a sentence about the handoff.
3. **A vague plural implying customers** — "agencies tell us", "what we're seeing", "in
   our experience". There are no customers. These are fabrication.
