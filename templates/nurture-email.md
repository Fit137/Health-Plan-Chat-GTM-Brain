# Template — nurture email

Campaign S1. **Two separate sequences: six emails for ICP-1, eight for ICP-2. Never merge
the tracks.**

The segmentation signal is which value driver they completed. D1 or D2 implies ICP-1.
D5 or D6 implies ICP-2. If the signal is ambiguous, treat as ICP-1 — the ICP-1 sequence
does no damage to an ICP-2 reader, but the reverse is not true.

---

## ICP-1 sequence arc

1. **Missed-call economics.** The number, in 2026 CMS commission dollars, dated.
2. **The question their front desk cannot answer.** Specific and concrete.
3. **Plan-answer proof.** A real question, a real sourced answer.
4. **What it will and will not say.** The escalation behaviour. This is the trust email.
5. **The AEP calendar.** What has to be true by 15 October.
6. **The sandbox offer.** 72 hours, their own documents, one ask.

## ICP-2 sequence arc

1. **Compliance exposure across a downline nobody can supervise.**
2. **Answer variance as management data**, not as a training problem.
3. **What uniform enforcement actually looks like.**
4. **Honest security posture**, including SOC 2 not held.
5. **Contractor adoption** — the failure mode, named before they hit it.
6. **The recruiting differentiator**, for the principal.
7. **Segment pilot design** with named success criteria.
8. **The offer:** run the Gap Report across one segment.

---

## Per-email structure

One idea. One number, with unit and date. One question or one call to action. Under 150
words. No image. No "P.S." gimmick.

Subject lines: the finding, not the benefit. "Forty-one after-hours calls" beats "Grow
your agency with AI".

---

## Guardrails

- **ICP-1 emails never mention procurement, security review, or annual terms.**
- **ICP-2 emails never mention month-to-month pricing or "no demo required".**
- No price in either track until published (OF-1).
- Every capability checked against `rules/feature-status.md`.
- Every outcome number labelled as modelled. We have no customer results.
- Unsubscribe honoured immediately; this audience is small and reputation travels.
- Run `ops/QA-checklist.md` before the sequence goes live.
