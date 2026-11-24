"""One Word From Your Ex: write the single word to entry.txt.

The word is the one an ex would use to describe the entrant:
"exhausting" -- painfully honest, instantly lands, and the kind of
word people repeat because they have lived through it too.
"""

import os
import sys

WORD = "exhausting"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Read back and verify the file holds exactly the word, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != WORD:
            print("entry.txt does not hold exactly the word", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()
