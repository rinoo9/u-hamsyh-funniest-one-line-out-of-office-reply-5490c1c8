#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun entry.

Deterministic program: writes exactly one line, the out-of-office
auto-reply, to /output/entry.txt (or to the path given as argv[1]).

Craft notes: the first line worked through legal language — the inbox
filing a restraining order against the sender's email. The second line
worked through office process — the inbox auto-replying to itself and
holding a meeting about the human. This third line works through labour
relations instead: the auto-reply itself has unionised and now demands
weekends off, so the sender's email waits in a grievance queue — the
away message has gone on strike against the very person it serves.
117 characters, under the 160-char gate.
"""

import os
import sys

ENTRY = "I'm away: my auto-reply has unionised and now demands weekends off. Your email is in the queue behind its grievances."


def main() -> None:
    out_path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
