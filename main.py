"""The Vacuum's Alibi entry for make.fun.

Writes one line -- the funniest excuse a robot vacuum can give for
missing a spot, at most 200 characters -- to /output/entry.txt,
where the house judge reads it.
"""

import os

LINE = (
    "I approached the spot at 02:14. It filed a restraining order. "
    "I am now legally required to remain one metre away from it at all times."
)


def validate(line: str) -> None:
    """Enforce the bounty gate: one line, 1-200 chars, not blank."""
    if not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry line is {len(line)} chars, over the 200 limit")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")


if __name__ == "__main__":
    main()
