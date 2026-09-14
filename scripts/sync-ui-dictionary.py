"""Copy shared UI/CSS references into independently installable skill folders."""

import argparse
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    outdated = []
    for skill in ("intent-clarifier", "simple-explanation"):
        for filename in ("ui-dictionary.md", "LICENSE-ui-menu.txt",
                         "css-dictionary.md", "LICENSE-css-menu.txt"):
            source = root / "shared" / filename
            target = root / "agent-skills" / skill / "references" / filename
            content = source.read_bytes()
            if args.check:
                if not target.exists() or target.read_bytes() != content:
                    outdated.append(str(target.relative_to(root)))
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(content)
    if outdated:
        parser.exit(1, "Out of sync: " + ", ".join(outdated) + "\n")
    print("UI/CSS references are in sync.")


if __name__ == "__main__":
    main()
