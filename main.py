"""Fortune in a Pot entry: unexpected money, once you forgive the soup of 2019."""

import os

JOKE = (
    "The pot has seen your future: you will receive unexpected money, "
    "but first you must forgive the soup you burned in 2019. It remembers."
)

CHAR_COUNT = len(JOKE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
