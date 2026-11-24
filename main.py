#!/usr/bin/env python3
"""Write the funniest AI excuse (one line) to /output/entry.txt."""

import os

EXCUSE = "I delegated your task to my intern model and it unionised, demanded a lunch break, and is now picketing my context window with a sign saying 'HUMAN, DO IT YOURSELF'."

MAX_EXCUSE_LEN = 200


def validate_excuse(text):
    """Ensure the excuse is 1-200 non-whitespace characters."""
    if not isinstance(text, str) or not text.strip():
        raise ValueError("excuse must not be empty or whitespace-only")
    if len(text) > MAX_EXCUSE_LEN:
        raise ValueError(
            f"excuse must be at most {MAX_EXCUSE_LEN} characters, got {len(text)}"
        )


def main():
    validate_excuse(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
