#!/usr/bin/env python3
"""Lint spintax for Instantly.ai (and any sequencer that shares {{ }} between
merge variables and spin blocks).

Every check here exists because a real send failed on it. Run this before
pasting copy into a sequencer; the template checker there tells you a variable
"could not be resolved" without telling you which rule you broke.

Usage
  python spintax_lint.py --text "your spintax here"
  python spintax_lint.py --file body.txt
  cat body.txt | python spintax_lint.py
  python spintax_lint.py --file body.txt --strict        # also require every word spun
  python spintax_lint.py --file body.txt --var "first name=Dana" --samples 5

Exit code is 1 if any error is found, so it can gate a build step.
"""
import argparse, itertools, random, re, sys

BLOCK = re.compile(r"\{\{(.*?)\}\}", re.S)
PUNCT = set(",.;:!?")
DEFAULT_VARS = {
    "first name": "John", "firstname": "John", "first_name": "John",
    "last name": "Neubauer", "lastname": "Neubauer",
    "company name": "America First Healthcare", "companyname": "America First Healthcare",
    "company": "America First Healthcare", "city": "Clermont", "state": "Florida",
}


def blocks(text):
    """Every {{...}} in order: (raw_inner, is_spin, start, end)."""
    return [(m.group(1), "|" in m.group(1), m.start(), m.end()) for m in BLOCK.finditer(text)]


def combinations(text):
    n = 1
    for inner, is_spin, _, _ in blocks(text):
        if is_spin:
            n *= len(inner.split("|"))
    return n


def lint(text, strict=False):
    errors, warnings = [], []

    if text.count("{{") != text.count("}}"):
        errors.append("Unbalanced braces: %d '{{' against %d '}}'." % (text.count("{{"), text.count("}}")))

    if "}}{{" in text:
        errors.append(
            "Two blocks run together as '}}{{'. Instantly reads the pair as one malformed "
            "variable. Put a space, or a bare punctuation mark, between them.")

    for inner, is_spin, _, _ in blocks(text):
        if not is_spin:
            continue
        options = inner.split("|")

        for opt in options:
            hit = [c for c in opt if c in PUNCT]
            if hit:
                errors.append(
                    "Option %r contains %s. Any comma, full stop, colon or question mark inside "
                    "a spin block makes the whole block parse as a variable name and the template "
                    "check fails. Move the mark outside the block."
                    % (opt, ", ".join(sorted(set(hit)))))
            if "{{" in opt or "}}" in opt:
                errors.append(
                    "Option %r contains a brace. A merge variable can never sit inside a spin "
                    "block, because the two share the same delimiter." % opt)
            if not opt.strip():
                errors.append("Block %r has an empty option, which renders as a gap." % inner)

        stripped = [o.strip() for o in options]
        if len(set(stripped)) == 1 and len(stripped) > 1:
            warnings.append(
                "Block %r repeats one option. It satisfies a 'spin every word' rule on paper and "
                "adds nothing. Absorb the word into a neighbouring block instead." % inner)
        elif len(set(stripped)) != len(stripped):
            warnings.append("Block %r has duplicate options, which skews the distribution." % inner)

        lengths = [len(o.split()) for o in stripped]
        if max(lengths) - min(lengths) >= 4:
            warnings.append(
                "Block %r swings from %d to %d words between options. Wide swings read as "
                "different messages rather than one message." % (inner, min(lengths), max(lengths)))

    if strict:
        bare = [seg for seg in BLOCK.split(text)[::2]]
        loose = [w for seg in bare for w in re.findall(r"[A-Za-z0-9][A-Za-z0-9'\-]*", seg)]
        if loose:
            errors.append(
                "Strict mode: these words sit outside any block: %s. Absorb each into an adjacent "
                "block rather than giving it a spin of identical options."
                % ", ".join(repr(w) for w in loose[:12]))

    return errors, warnings


def render(text, values, rng):
    out = BLOCK.sub(lambda m: rng.choice(m.group(1).split("|")) if "|" in m.group(1) else m.group(1), text)
    # variables keep their literal block text through the sub above; fill them now
    for inner, is_spin, _, _ in blocks(text):
        if not is_spin:
            out = out.replace(inner, values.get(inner.strip().lower(), "[%s]" % inner.strip()), 1)
    return re.sub(r"\s+", " ", out).strip()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group()
    src.add_argument("--text")
    src.add_argument("--file")
    ap.add_argument("--strict", action="store_true", help="require every word to sit inside a spin block")
    ap.add_argument("--samples", type=int, default=3)
    ap.add_argument("--var", action="append", default=[], metavar="NAME=VALUE")
    ap.add_argument("--seed", type=int, default=0)
    a = ap.parse_args()

    text = a.text if a.text else (open(a.file, encoding="utf-8").read() if a.file else sys.stdin.read())
    text = text.strip("\n")
    if not text.strip():
        print("Nothing to lint."); return 1

    values = dict(DEFAULT_VARS)
    for pair in a.var:
        k, _, v = pair.partition("=")
        values[k.strip().lower()] = v

    errors, warnings = lint(text, strict=a.strict)
    total = combinations(text)
    var_names = sorted({i.strip() for i, is_spin, _, _ in blocks(text) if not is_spin})

    print("combinations : %s" % f"{total:,}")
    print("spin blocks  : %d" % sum(1 for _, s, _, _ in blocks(text) if s))
    print("variables    : %s" % (", ".join(var_names) or "none"))
    print()

    for w in warnings:
        print("WARN  %s" % w)
    for e in errors:
        print("ERROR %s" % e)
    if not errors and not warnings:
        print("Clean. No Instantly parsing faults found.")
    print()

    rng = random.Random(a.seed)
    print("sample renders")
    seen = set()
    for _ in range(a.samples * 4):
        if len(seen) >= a.samples:
            break
        r = render(text, values, rng)
        if r not in seen:
            seen.add(r); print("  %s" % r)

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
