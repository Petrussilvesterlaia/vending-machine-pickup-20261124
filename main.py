#!/usr/bin/env python3
"""Vending machine pickup line entry.

Writes one original pickup line, spoken by a vending machine in the
first person, to /output/entry.txt and validates it against the gate:
UTF-8 text of 1-200 characters, not only whitespace.
"""

import os

LINE = "I've dropped a thousand snacks and never jammed once \u2014 until you walked by, and now my coils turn for free."

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 200


def main() -> None:
    line = LINE.strip()
    if not line:
        raise SystemExit("ERROR: pickup line is empty or only whitespace")
    if len(line) < MIN_LENGTH or len(line) > MAX_LENGTH:
        raise SystemExit(
            f"ERROR: pickup line is {len(line)} characters; "
            f"gate requires {MIN_LENGTH}-{MAX_LENGTH}"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    # Round-trip check: what landed on disk must be exactly the line,
    # valid UTF-8, and still inside the gate.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    decoded = raw.decode("utf-8")
    if decoded != line or not (MIN_LENGTH <= len(decoded) <= MAX_LENGTH):
        raise SystemExit("ERROR: round-trip verification of entry.txt failed")
    print(f"Wrote {len(line)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
