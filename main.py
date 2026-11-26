#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Deterministic program: writes exactly one line, the out-of-office
auto-reply, to /output/entry.txt (or to the path given as argv[1]).

Craft notes: the first line worked through legal language — the inbox
filing a restraining order against the sender's email. The new line
works through office process instead: the inbox auto-replied to itself
and is now in a meeting about the human, which turns the auto-reply
into a self-perpetuating bureaucracy that has forgotten its owner
entirely. The punchline is the last instruction — "Do not add to the
thread" — the meeting's minutes, delivered as a warning to the very
person the reply is supposed to serve. 106 characters, under the
160-char gate.
"""

import os
import sys

ENTRY = "I'm away: my inbox auto-replied to itself and now they're in a meeting about me. Do not add to the thread."


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
