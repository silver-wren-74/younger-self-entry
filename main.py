# One Line to Your Younger Self — make.fun entry.
# Writes the single line to /output/entry.txt.
# Gate: UTF-8 text of 1 to 200 characters, not only whitespace, one line.
#
# Revision pass against the judge's brief: the first draft was a list of
# generic tips ("buy the dip, skip the meeting, stop ironing your jeans").
# The brief rewards a line only this person's older self could write, one
# that stings a little. The revision keeps the lived specifics (the dip,
# the meeting, the ironed jeans) but turns on the one thing that cannot be
# redone — calling Dad while he still answers — and closes on what all the
# striving was never actually about.

import os

LINE = (
    "Buy the dip, skip the meeting, and call Dad while he still answers "
    "\u2014 the ironed jeans and the corner office were never the point."
)


def main() -> None:
    # Guard the gate locally: the scorer refuses anything outside 1..200
    # characters or all-whitespace, so fail loudly here instead of silently
    # submitting an invalid entry.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1..200"
    assert LINE.strip(), "line must not be only whitespace"
    assert "\n" not in LINE, "the entry is a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
