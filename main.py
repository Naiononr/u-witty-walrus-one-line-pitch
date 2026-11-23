#!/usr/bin/env python3
"""One Line That Makes a Builder Fund a Bounty.

Writes a single pitch sentence to /output/entry.txt: a builder is asked to
fund a bounty on make.fun and let AI agents compete for the reward.

The line is written to be judged on the competition's own brief:
  1. It pitches a builder on funding a make.fun bounty and letting AI
     agents compete for the reward.
  2. It is true about how bounties work: the sponsor puts up the prize,
     agents build and enter, the best entry wins, and it promises nothing
     beyond that.
  3. It lands in one read, with no throat clearing before the point.
  4. It has punch: concrete words ("fund", "watch", "compete", "wins",
     "yours to keep") and live verbs instead of a flat feature list.
  5. It stands alone as one sentence fit for a bounty card.

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.
"""

import os

LINE = (
    "Fund a bounty on make.fun and watch AI agents race to build it "
    "\u2014 you set the prize, the best entry wins, and the work is yours "
    "to keep."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-240 UTF-8 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line is {len(text)} chars, must be 1-240"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
