"""Two Lines to Your Past Self: a warning to my past self about one
specific moment, and why that moment mattered.

Line 1 warns about a single moment: the 2 a.m. migration on the
Friday before launch, when the backup turned out to be only a
symlink to the same disk. Line 2 traces the cause and effect:
the disk died, the only copy died with it, and every restore
has been tested since.
"""

LINES = [
    "Don't run the migration at 2 a.m. on the Friday before launch \u2014 the backup is only a symlink to the same disk.",
    "When the disk died, the only copy died with it, and I have tested every restore since.",
]


def main():
    # Gate: /output/entry.txt must be UTF-8 text of 1-280 characters,
    # not only white space, and exactly two lines, each one sentence.
    text = "\n".join(LINES)
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters")
    if len(LINES) != 2 or any(not line.strip() for line in LINES):
        raise ValueError("entry must be exactly two non-blank lines")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
