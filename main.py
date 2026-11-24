#!/usr/bin/env python3
"""One-line AI excuse for a missed deadline (make.fun bounty).

Writes the excuse to /output/entry.txt and prints it.
Gate: /output/entry.txt must be UTF-8 text of 1-200 characters.
"""
import os

LINE = "The deadline didn't move \u2014 I did. I moved to a timezone where it's still yesterday, so technically I'm three hours early and entirely blameless."


def main():
    assert 1 <= len(LINE) <= 200, f"line must be 1-200 chars, got {len(LINE)}"
    assert LINE.strip(), "line must not be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
