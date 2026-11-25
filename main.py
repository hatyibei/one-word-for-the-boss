"""Entry for make.fun's "One Word for the Boss" bounty.

Writes exactly one word describing my boss (at most 30 characters, per
this bounty's gate) to /output/entry.txt.
"""

import os

TEXT = "Veto"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
