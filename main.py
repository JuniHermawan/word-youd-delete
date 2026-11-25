#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary -- make.fun entry.

Writes exactly one word to $MAKEFUN_OUTPUT_DIR/entry.txt
(the grader mounts that directory as /output).

The word: "colonel" -- spelled nothing like it sounds ("kernel"),
the dictionary's most famous spelling lie. Delete it and English
finally admits the word is pronounced "kernel".
"""

import os

WORD = "colonel"

# Gate: /output/entry.txt must be UTF-8 text of 1 to 77 characters,
# not only white space, and the judge wants exactly one word.
assert WORD and len(WORD) <= 77 and len(WORD.split()) == 1, WORD


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
