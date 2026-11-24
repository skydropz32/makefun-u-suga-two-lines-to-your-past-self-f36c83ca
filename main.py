"""Two Lines to Your Past Self: a warning to my past self about one
specific moment, and why that moment mattered.

Line 1 warns about a single moment: the 2 a.m. migration on the
Friday before launch, when the backup turned out to be only a
symlink to the same disk. Line 2 traces the cause and effect:
the disk died, the only copy died with it, and every restore
has been tested since.
"""

import re

LINES = [
    "Don't run the migration at 2 a.m. on the Friday before launch \u2014 the backup is only a symlink to the same disk.",
    "When the disk died, the only copy died with it, and I have tested every restore since.",
]


def _validate_lines(lines):
    """Check the entry shape before writing: exactly two non-blank
    lines, each a single sentence, 1-280 characters in total."""
    if len(lines) != 2 or any(not line.strip() for line in lines):
        raise ValueError("entry must be exactly two non-blank lines")
    for line in lines:
        if "\n" in line or "\r" in line:
            raise ValueError("entry line must not contain a newline")
        if line != line.strip():
            raise ValueError("entry line must not have leading/trailing space")
        # One sentence: ends with a sentence mark, and no sentence
        # boundary mid-line (a mark followed by space + capital, so
        # abbreviations like "a.m." do not count as a new sentence).
        if line[-1] not in ".!?":
            raise ValueError("each entry line must end with a sentence mark")
        if re.search(r"[.!?]\s+[A-Z]", line):
            raise ValueError("each entry line must be exactly one sentence")
    text = "\n".join(lines)
    if not (1 <= len(text) <= 280):
        raise ValueError("entry must be 1-280 characters")
    return text


def main():
    text = _validate_lines(LINES)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
