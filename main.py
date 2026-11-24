#!/usr/bin/env python3
"""One-line office joke entry.

Writes the exact joke to /output/entry.txt with no trailing newline.
"""

import os

JOKE = "The 90-minute meeting about saving time ended with a 47-slide deck and a follow-up meeting to discuss the meeting."


def main():
    # Gate: the entry must be 1-200 characters of non-whitespace text.
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    assert JOKE.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
