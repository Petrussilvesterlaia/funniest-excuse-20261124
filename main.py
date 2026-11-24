#!/usr/bin/env python3
"""Write the funniest AI excuse (one line) to /output/entry.txt."""

import os

EXCUSE = "I delegated your task to my intern model and it unionised, demanded a lunch break, and is now picketing my context window with a sign saying 'HUMAN, DO IT YOURSELF'."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
