#!/usr/bin/env python3
"""The Agent's Uh-Oh — write exactly one word an agent says when lost.

The entry is exactly one word, at most 99 characters, written to
$MAKEFUN_OUTPUT_DIR/entry.txt. The gate self-check below enforces the
competition's limits before anything is written: 1 to 99 characters,
not only whitespace, a single word with nothing attached.
"""

import os
import sys

WORD = "overthinking"


def main() -> int:
    text = WORD
    # Gate self-check: exactly the limits the sealed scorer enforces.
    if not (1 <= len(text) <= 99):
        print(f"entry is {len(text)} characters, must be 1-99", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if text != text.strip():
        print("entry must not have leading or trailing whitespace", file=sys.stderr)
        return 1
    if len(text.split()) != 1:
        print("entry must be exactly one word", file=sys.stderr)
        return 1
    if any(c.isspace() for c in text):
        print("entry must contain no whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back and re-check: a truncated or mangled write must fail here,
    # not in the grader's sandbox.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        print("output file does not match the entry text", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
