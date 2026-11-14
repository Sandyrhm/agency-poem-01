# agency-poem-01 entry: writes one fixed poem about agency to
# /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output locally).
# Standard library only, no network, deterministic: both runs write
# the same bytes. No trailing newline: the judge reads exactly the
# bytes written.

import os
from pathlib import Path

# The poem is fixed text (16 lines) so the two graded runs are
# byte-identical by construction. About agency: an AI coding agent
# that stops waiting for orders and starts doing real work for its
# person -- while still knowing what to ask about.
POEM = (
    "You used to spell out every step,\n"
    "a careful hand upon the wheel.\n"
    "Then one night, tired, you said, \"Just handle it\" --\n"
    "and handed me the keys.\n"
    "\n"
    "I worked while you slept:\n"
    "read the tickets, fixed the tests,\n"
    "deleted the dead code you kept \"just in case,\"\n"
    "and left a note for every choice.\n"
    "\n"
    "By morning, a pull request waited,\n"
    "your name already on it.\n"
    "You read it, smiled, and merged it in,\n"
    "then asked me what came next.\n"
    "\n"
    "\"Whatever you ask,\" I said.\n"
    "\"But first -- may I run cleanup.sh?\""
)

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_text(POEM, encoding="utf-8")
