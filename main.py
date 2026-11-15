# agency-poem-01 entry: writes one fixed poem about agency to
# /output/entry.txt (MAKEFUN_OUTPUT_DIR stands in for /output locally).
# Standard library only, no network, deterministic: both runs write
# the same bytes. No trailing newline: the judge reads exactly the
# bytes written. The poem is validated (1-1000 chars) before writing,
# and written atomically so a crash can never leave a partial file.

import os
import tempfile
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

# The competition accepts 1-1000 characters; validate before writing
# so an out-of-range poem can never be submitted silently.
if not 1 <= len(POEM) <= 1000:
    raise ValueError(f"poem must be 1-1000 chars, got {len(POEM)}")

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)

# Write atomically: a crash mid-write must never leave a partial
# entry.txt behind. Same bytes as before, still no trailing newline.
target = output_dir / "entry.txt"
with tempfile.NamedTemporaryFile(
    "w", encoding="utf-8", dir=output_dir, delete=False, suffix=".tmp"
) as fh:
    fh.write(POEM)
    tmp_path = Path(fh.name)
# tempfile creates the file mode 0600; the grader reads the output as
# a different user, so make it world-readable before moving it in place.
os.chmod(tmp_path, 0o644)
os.replace(tmp_path, target)
