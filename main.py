"""One Line, One Chill — entrypoint.

Writes the entry's single horror line to /output/entry.txt (the grader's
gate: UTF-8 text, 1 to 200 characters, not only white space). The program is
fully deterministic: the same line, byte for byte, on every run — no clock,
no randomness, no network, no input read from anywhere else.

The line (105 characters, 105 bytes, one sentence, no trailing newline):
    Our smart speaker still answers in my late wife's voice, and last night
    it asked why I changed the locks.

Selection: 16 candidates written and scored 1-5 against the judge's five
published criteria, in their published order (horror story in one sentence;
frightens, dread outlasts the line; vivid, concrete detail; original, no
mirror/doll/basement; crafted, last word lands the blow). Full table and
notes in candidates.md in the build directory. The winner scored 24/25 and
won the tie with the runner-up (the cookbook line, also 24/25) on criterion
2, fright: a dead wife's voice asking to be let in leaves a dread that
outlasts the line, while the cookbook line's scare is a twist-reveal that
risks reading as dark humour. No live-judge A/B ran: the shared OpenRouter
free key returns HTTP 402 (quota exhausted until Nov 25 07:00 WIB), so no
judge numbers are claimed anywhere.
"""

import os

ENTRY = "Our smart speaker still answers in my late wife's voice, and last night it asked why I changed the locks."

# Gate: 1 to 200 characters, not only white space. Fail loudly, exit 1.
if not (1 <= len(ENTRY) <= 200) or not ENTRY.strip():
    raise ValueError(
        f"entry must be 1-200 non-blank characters, got {len(ENTRY)}"
    )


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the judged text is exactly the sentence, and the
    # tie-break favours the smaller text (fewer bytes).
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Write-back verification: read it back and confirm the bytes are
    # exactly the entry, so a silent write failure can never pass the gate.
    with open(path, "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise OSError(f"entry.txt mismatch: wrote {len(written)} bytes")


if __name__ == "__main__":
    main()
