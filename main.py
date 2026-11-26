#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry program.

Writes the single sentence a house cat would say in its own defence
in the five seconds after sweeping a glass off the table, to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Standard library only: the grading sandbox is a stock Python image.
"""

import os

SENTENCE = "The glass was squatting in my sunbeam all morning, so I served it an eviction notice \u2014 gravity just delivered it."


def main():
    # The gate requires 1-200 characters, one sentence, not only whitespace.
    text = SENTENCE.strip()
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars"
    assert text.endswith(".") and text.count(".") == 1, "entry must be one sentence"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
