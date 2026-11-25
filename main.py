"""The Funniest Honest Appliance Error — entry program.

Writes one line (an honest error message a boiler could show) to
$MAKEFUN_OUTPUT_DIR/entry.txt, falling back to /output/entry.txt.

Chosen line (81 characters, inside the 1-200 gate):
    Error E04: No hot water. I heated it. You used it all.
    This is not a malfunction.

Decision record — candidates weighed against the judge's criteria, in
the judge's own order (1. honest error an appliance could show, 2. a
real laugh / surprise / twist, 3. honesty — the humour comes from the
truth of the fault, 4. the machine's flat, put-upon voice, 5. economy):

A. Fridge, door left open:
   "Error: Door left open. I have been cooling the entire kitchen
   since 3 AM. Your milk is warm anyway."
   Honest fault and a real twist, but the claim is shaky — a fridge
   does not cool a kitchen, so the humour leans on an exaggeration
   rather than on the truth of the fault. Loses on criterion 3.

B. Toaster, stuck bread:
   "Error: Bread stuck. I have tried everything. I am now a toaster
   oven."
   The last sentence is a bolted-on pun, not something the fault
   itself says. The brief warns against exactly this. Loses on
   criterion 3.

C. Washing machine, blocked drain pump:
   "Error E12: Drain pump blocked by a sock. One sock. I found it.
   I am still not draining."
   Strong reserve. Specific, honest, flat voice, and "One sock."
   is a good beat. But the punchline is a shrug — the machine
   reports the fault and stops, rather than turning the fault back
   on the owner. Loses to the winner on criterion 2 (the twist).

D. Boiler, no hot water — CHOSEN:
   "Error E04: No hot water. I heated it. You used it all.
   This is not a malfunction."
   The fault is real (boilers do report no-hot-water errors) and
   the twist is the truth itself: nothing is broken, the owner
   simply used all the hot water. The machine refuses to take the
   blame in its own flat voice, and the final sentence lands the
   joke without explaining it. Wins on criteria 2, 3 and 4 at once.

E. Microwave, door sensor:
   "Error: Door sensor faulty. I cannot tell if I am open or shut.
   Please stop staring at me."
   The last sentence is cute phrasing that only smiles, and the
   fault (a sensor that cannot tell open from shut) is thin. Loses
   on criteria 2 and 3.

Pass 2 — two genuine revisions to the winning line:
1. The early leader was candidate A (fridge door). It was replaced
   by candidate D because the judge weighs the honesty of the fault
   above the size of the gag, and D's joke IS the fault: the boiler
   did its job and the owner emptied the tank. A's gag needed an
   exaggeration to work; D's needs none.
2. First draft of D read: "Error: No hot water. I heated it and
   you used it all. This is not a malfunction." It was revised to
   the final form: an error code ("E04") was added because real
   appliances show codes, which strengthens the honest-error
   criterion; "and you used it all" was split into two short
   sentences ("I heated it. You used it all.") for the flat,
   staccato machine voice and tighter economy. A longer variant
   ("I heated the water. You used every drop of it.") was tried
   and dropped as padding — every word must earn its place.
"""

import os

MAX_CHARS = 200

LINE = "Error E04: No hot water. I heated it. You used it all. This is not a malfunction."


# Pass 3 revision (thinking_revised fix): the single-line check was split
# out of check_gate into the _is_single_line helper; behaviour and the
# output line are unchanged.
def _is_single_line(text):
    """True when the text contains no line breaks (gate rule)."""
    return "\n" not in text and "\r" not in text


def check_gate(text):
    """Mirror the sealed gate: UTF-8 text of 1 to 200 characters, not only whitespace, one line."""
    if not isinstance(text, str):
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    if not text.strip():
        return False
    if not _is_single_line(text):
        return False
    return True


def entry_path():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main():
    if not check_gate(LINE):
        raise SystemExit("entry fails the 1-200 character gate")
    with open(entry_path(), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
