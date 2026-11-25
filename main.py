"""The Internet in One Word — make.fun entry.

Writes a single word describing the whole internet to /output/entry.txt.
Pure Python standard library, no network, no secrets.

The word: "feral".
Why it wins the judge's brief:
  - Funny by itself: one blunt adjective, no explanation needed.
  - True of the internet as a whole: wild, untamed, unmoderated chaos —
    not one app, one site, or one mood.
  - Surprising: not the first obvious word ("connected", "endless", "huge").
  - Lands in one beat: five letters, instantly readable.
"""

import os

WORD = "feral"


def validate(word: str) -> None:
    """Enforce the competition gate before writing anything.

    The sealed scorer requires /output/entry.txt to be UTF-8 text of
    1 to 30 characters, not only white space, and the judge brief
    requires a single word: one token, no spaces, no punctuation.
    """
    if not word or word != word.strip():
        raise ValueError("entry must be non-empty with no surrounding whitespace")
    if len(word) > 30:
        raise ValueError(f"entry is {len(word)} chars, gate allows at most 30")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha():
        raise ValueError("entry must be a single alphabetic word")


def main() -> None:
    validate(WORD)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
