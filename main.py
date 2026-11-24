#!/usr/bin/env python3
"""One Word From Your Ex — entry.

Writes exactly one word to /output/entry.txt: the word an ex would
use to describe the entrant. One word, nothing else.

Chosen word: "exhausting" — the word an ex would actually say, funny
because it is blunt, painful because it is a verdict on the whole
relationship, and instantly relatable.
"""

import os

WORD = "exhausting"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
