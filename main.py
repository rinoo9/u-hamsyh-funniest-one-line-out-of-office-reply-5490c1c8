#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Deterministic program: writes exactly one line, the out-of-office
auto-reply, to /output/entry.txt (or to the path given as argv[1]).
"""

import os
import sys

ENTRY = "I'm away. My inbox is currently being answered by my cat, who has no thumbs and less patience."


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
