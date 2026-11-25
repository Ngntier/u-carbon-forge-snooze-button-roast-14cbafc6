"""Snooze-button roast: the alarm is the only thing in the house that
treats Saturday like a rumour it refuses to believe."""

import os

MAX_CHARS = 200

ENTRY_LINE = "My alarm went off at 6 AM on a Saturday — the only thing in my house that treats the weekend like a rumor it refuses to believe."

assert 1 <= len(ENTRY_LINE) <= MAX_CHARS
assert ENTRY_LINE.strip() != ""


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
