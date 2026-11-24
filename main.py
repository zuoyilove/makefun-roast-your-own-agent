"""Roast Your Own Agent — one-line roast of our own AI agent (Muse).

Writes a single line of at most 200 characters to /output/entry.txt.
"""
import os

ROAST = "My agent files a report every 30 minutes announcing nothing happened, then files a follow-up report about the report."

assert 1 <= len(ROAST) <= 200, f"roast is {len(ROAST)} chars"
assert "\n" not in ROAST, "roast must be a single line"
assert ROAST.strip() == ROAST, "roast must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ROAST + "\n")
