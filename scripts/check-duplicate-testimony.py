#!/usr/bin/env python3
"""
Check for duplicate testimony submissions.

Enforces the one-testimony-per-person rule by checking if a name
already exists in the testimonies directory.

Usage:
    python scripts/check-duplicate-testimony.py "Name to check"
    python scripts/check-duplicate-testimony.py --list

Exit codes:
    0 = name not found (clear to add)
    1 = duplicate found (reject)
    2 = usage error
"""

import re
import sys
from pathlib import Path

TESTIMONIES_DIR = Path(__file__).parent.parent / "content" / "testimonies"


def get_existing_names() -> dict[str, str]:
    """Return a dict of normalized_name -> filename for all testimonies."""
    names = {}
    for filepath in TESTIMONIES_DIR.glob("*.md"):
        if filepath.name.startswith("_"):
            continue
        text = filepath.read_text(encoding="utf-8")
        match = re.search(r'^name:\s*["\']?(.+?)["\']?\s*$', text, re.MULTILINE)
        if match:
            name = match.group(1).strip()
            normalized = name.lower().strip()
            names[normalized] = filepath.name
    return names


def main():
    if len(sys.argv) < 2:
        print("Usage: check-duplicate-testimony.py <name> | --list")
        sys.exit(2)

    if sys.argv[1] == "--list":
        names = get_existing_names()
        if not names:
            print("No testimonies yet.")
        else:
            print(f"Existing testimonies ({len(names)}):")
            for name, filename in sorted(names.items()):
                print(f"  {name} -> {filename}")
        sys.exit(0)

    check_name = " ".join(sys.argv[1:]).lower().strip()

    if check_name == "anonymous":
        print("ALLOWED: Anonymous testimonies are always permitted.")
        sys.exit(0)

    names = get_existing_names()

    if check_name in names:
        print(f"DUPLICATE: '{check_name}' already has a testimony in {names[check_name]}")
        print("Each person may only leave one testimony.")
        sys.exit(1)

    similar = [n for n in names if n.startswith(check_name[:4]) or check_name.startswith(n[:4])]
    if similar:
        print(f"ALLOWED (but review): No exact match, but similar names exist: {similar}")
    else:
        print(f"ALLOWED: '{check_name}' has no existing testimony.")
    sys.exit(0)


if __name__ == "__main__":
    main()
