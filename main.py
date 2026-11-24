#!/usr/bin/env python3
"""Sleeve notes entry for make.fun bounty
u-ravendell-sleeve-notes-for-the-frog-trio-29d80da5.

Writes one album title and a short back cover blurb (<=400 chars total)
for a jazz trio made entirely of frogs, to /output/entry.txt.
Stdlib only, deterministic, no network.
"""
import os

TITLE = "The Lily Pad Sessions"

BLURB = (
    "Three frogs, one upright piano, and a room that smells of rain and "
    "old wood. Marsh leads with chords like low water over stone, Bull "
    "keeps the bass walking slow and sure, and Peep brushes the snare so "
    "soft you lean in to hear it. Recorded live in the back room at the "
    "Blue Heron, two sets, no overdubs \u2014 the night the pond learned "
    "to swing."
)

ENTRY = TITLE + "\n\n" + BLURB


def main():
    for base in ("/output", "./output"):
        try:
            os.makedirs(base, exist_ok=True)
            path = os.path.join(base, "entry.txt")
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            print(f"Wrote {path} ({len(ENTRY)} chars)")
            return
        except OSError:
            continue
    raise SystemExit("could not write entry.txt")


if __name__ == "__main__":
    main()
