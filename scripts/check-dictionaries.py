"""Check that the shared dictionaries stay bilingual and structurally intact.

Run with no arguments; exits non-zero and prints every problem it finds.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SHARED = ROOT / "shared"

# (file, entry heading pattern, paired line prefixes)
ENTRY_PAIRS = [
    ("ui-dictionary.md", r"^### ", [("- 일상 표현: ", "- Everyday phrasing: "),
                                    ("- 쉬운 설명: ", "- Plain explanation: ")]),
    ("css-dictionary.md", r"^#### ", [("- 일상 표현: ", "- Everyday phrasing: ")]),
]


def check_entry_pairs(problems):
    """Every entry carrying a Korean line must carry its English counterpart."""
    for filename, heading, pairs in ENTRY_PAIRS:
        path = SHARED / filename
        entry = None
        found = {}

        def flush():
            if entry is None:
                return
            for ko, en in pairs:
                if found.get(ko) and not found.get(en):
                    problems.append(f"{filename}: '{entry}' has '{ko.strip()}' but no '{en.strip()}'")

        for line in path.read_text().split("\n"):
            if re.match(heading, line):
                flush()
                entry, found = line.lstrip("# ").strip(), {}
            for ko, en in pairs:
                for prefix in (ko, en):
                    if line.startswith(prefix):
                        found[prefix] = True
        flush()


def check_table_columns(problems):
    """Every row of a markdown table must have the same number of columns.

    A mis-inserted cell silently shifts a row's meaning, so this is worth guarding.
    """
    for path in sorted(SHARED.glob("*-dictionary.md")):
        block, start = [], 0
        for lineno, line in enumerate(path.read_text().split("\n"), 1):
            if line.startswith("| "):
                if not block:
                    start = lineno
                block.append((lineno, line.count("|")))
                continue
            if block:
                widths = {w for _, w in block}
                if len(widths) > 1:
                    problems.append(
                        f"{path.name}: table at line {start} has mixed column counts {sorted(widths)}"
                    )
                block = []


def main():
    problems = []
    check_entry_pairs(problems)
    check_table_columns(problems)
    if problems:
        print("\n".join(problems))
        sys.exit(1)
    print("Dictionaries are bilingual and structurally consistent.")


if __name__ == "__main__":
    main()
