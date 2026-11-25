"""Two Days of Quiet Dread — entry program.

Writes one code review comment to /output/entry.txt: a single line that
approves a pull request while carrying quiet existential dread.
Stdlib only; no network, no randomness.
"""

import os

ENTRY = "Approved. The tests pass and the code is clean, which is exactly how the last outage started."


def main() -> None:
    text = ENTRY.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    except OSError:
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    # Read back and confirm the file holds exactly the entry, byte for byte.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == text, "round-trip mismatch"


if __name__ == "__main__":
    main()
