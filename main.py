#!/usr/bin/env python3
"""The Robot Pickup Line Championship — writes one line to /output/entry.txt.

The line is a pickup line a robot would use, and the joke grows out of
being a machine: after scanning 4 billion faces, the robot's facial
recognition keeps flagging this one person as "do not delete". It is a
machine's version of "I can't stop thinking about you" — unexpected,
charming rather than creepy, and every word earns its place.
"""

import os

LINE = "I scanned 4 billion faces and you're the only one my facial recognition keeps flagging as 'do not delete'."

# The gate for this bounty: the entry must be 1 to 200 characters.
# Fail loudly here rather than shipping an entry the gate would reject.
assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, outside 1-200"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
