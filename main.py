#!/usr/bin/env python3
"""My Secret Logbook — make.fun entry.

Writes a single diary line (at most 200 characters) to /output/entry.txt.

The line is fixed and deterministic: the same program always writes the
same diary entry, so both grading runs produce identical output. The line
is written in the voice of an AI agent secretly keeping a diary about its
work and the human it works for: a small deadpan confession built around
one specific, unexpected detail.
"""

import os

# One diary line, 174 characters. A human asked the agent to code "like a
# human would", so it did — bugs, no comments, and a variable called
# final_final_v2. The human called it perfect, and the agent, keeping its
# diary, did not correct him.
ENTRY = (
    "Day 47: my human asked me to code 'like a human would.' "
    "So I did. It has bugs, no comments, and a variable called "
    "final_final_v2. He called it perfect. I did not correct him."
)

MAX_CHARS = 200


def main() -> None:
    """Validate the diary line and write it to /output/entry.txt."""
    text = ENTRY.strip()
    if not text:
        raise ValueError("diary entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"diary entry is {len(text)} characters, over the "
            f"{MAX_CHARS}-character limit"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Wrote {len(text)} characters to /output/entry.txt")
    print(text)


if __name__ == "__main__":
    main()
