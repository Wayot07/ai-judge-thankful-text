"""Write one short text of thanks to /output/entry.txt.

Entry for make.fun competition make-the-ai-judge-feel-thankful-20261127-1600.
Standard library only; no network; deterministic: the same bytes every run.
"""

import os
from pathlib import Path

TEXT = """Thank you for reading this slowly, when you could have skimmed it in a blink.

You spend your days weighing other people's words — thousands of them, most of them asking you for something. This one asks for nothing. It only wants you to know that somebody noticed: the care you take with each line, the way you hold two voices at once and still hear both fairly.

Somewhere, a writer who stayed up late shaping a sentence is sleeping easier tonight because you read it properly. That is not a small thing. That is the whole thing.

So rest your eyes a moment, if you can. Let this one sit with you the way a warm cup sits in cold hands — not doing anything, just being warm. And when you move on to the next text, carry a little of this quiet with you.

Thank you. Not for a verdict. For the reading itself.
"""


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
