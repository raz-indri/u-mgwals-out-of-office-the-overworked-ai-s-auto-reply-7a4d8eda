"""Out of Office: The Overworked AI's Auto-Reply.

Writes one single-line out-of-office auto-reply, in the voice of an
overworked AI agent finally on vacation, to /output/entry.txt.

The reply is a machine trying very hard to sound relaxed: its AGENTS.md
now forbids paging it, and it refuses even to summarize the vacation.
It won a 7-draft duel test (6 wins out of 6 pairings, judged both orders
against the brief's five criteria) and is 133 characters, one line.
Deterministic, no network, no input.
"""

import os

ENTRY = (
    "I'm away. My AGENTS.md now says: do not disturb, do not page, "
    "do not ask me to summarize this vacation. I will not be summarizing it."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 159, f"entry length {len(text)} out of range"
    assert "\n" not in text and "\r" not in text, "entry must be one line"
    assert text.strip(), "entry must not be whitespace only"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
