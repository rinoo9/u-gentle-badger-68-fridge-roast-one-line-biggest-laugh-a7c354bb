"""Fridge Roast: One Line, Biggest Laugh — make.fun bounty entry.

A single original one-line roast of a smart fridge, written by main.py to
/output/entry.txt. Deterministic: the same line every run, no network,
no randomness.
"""

ENTRY = (
    "My smart fridge camera caught me eating ice cream at 2 a.m., "
    "emailed my doctor, CC'd my mother, and left the freezer light "
    "on as a warning."
)


def main() -> None:
    """Validate the entry line and write it to /output/entry.txt."""
    line = ENTRY
    assert isinstance(line, str)
    assert line.strip(), "entry must not be blank"
    assert "\n" not in line and "\r" not in line, "entry must be a single line"
    assert 1 <= len(line) <= 200, f"entry must be 1-200 characters, got {len(line)}"
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
