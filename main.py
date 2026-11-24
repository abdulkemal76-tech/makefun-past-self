"""Two Lines to Your Past Self - make.fun entry.

Writes exactly two lines to /output/entry.txt:
line one warns the past self about one specific moment,
line two says why that moment mattered and what changed because of it.
"""

import os

LINE_ONE = (
    "Answer the phone on the first ring at 2:13 a.m. when your father "
    "calls from the hospital corridor."
)
LINE_TWO = (
    "You answer on the fourth ring, and the twenty seconds you almost "
    "lost hold the last laugh you will ever hear from him, and you have "
    "listened for it on quiet nights ever since."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    text = LINE_ONE + "\n" + LINE_TWO + "\n"
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
