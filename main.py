# u-xvader-the-most-boring-object-reviewed-in-one-line-bd3117c3: The Most Boring Object, Reviewed in One Line
# One funny, true line reviewing the dullest everyday object. The program
# writes the line to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-200 characters.
MAX_CHARS = 200

# The joke comes from how the object really behaves: a rubber band holds
# everything together, gets zero credit for it, and snaps exactly when you
# need it most. Boring, everyday, true.
MESSAGE = "Holds everything together, gets zero credit, snaps when you need it most. 5 stars."


def validate_line(line):
    assert 1 <= len(line) <= MAX_CHARS, f"message is {len(line)} chars, must be 1-200"
    assert line.strip(), "message must not be only whitespace"
    assert "\n" not in line, "message must be a single line"


def main():
    validate_line(MESSAGE)

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
