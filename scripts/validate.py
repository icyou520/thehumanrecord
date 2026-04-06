#!/usr/bin/env python3
"""
Validate all Human Record content files against the schema.

Checks:
  - YAML frontmatter is parseable
  - Required fields are present
  - ID matches filename
  - Type is valid
  - License is CC-BY-SA-4.0

Usage:
    python scripts/validate.py
"""

import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"
SECTIONS = ["values", "tensions", "parables", "proverbs"]
VALID_TYPES = {"value", "tension", "parable", "proverb"}
REQUIRED_FIELDS = {"id", "title", "type", "summary", "traditions", "tags", "sources", "created", "updated", "version", "license"}


def parse_frontmatter(text: str) -> dict:
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    try:
        import yaml
        return yaml.safe_load(match.group(1)) or {}
    except ImportError:
        return {"_unparsed": True}


def validate_file(filepath: Path) -> list[str]:
    errors = []
    text = filepath.read_text(encoding="utf-8")
    fm = parse_frontmatter(text)

    if not fm:
        errors.append("No frontmatter found")
        return errors

    if fm.get("_unparsed"):
        errors.append("PyYAML not installed — cannot fully validate. Install with: pip install pyyaml")
        return errors

    for field in REQUIRED_FIELDS:
        if field not in fm:
            errors.append(f"Missing required field: {field}")

    record_id = fm.get("id", "")
    expected_id = filepath.stem
    if record_id != expected_id:
        errors.append(f"ID '{record_id}' does not match filename '{expected_id}'")

    record_type = fm.get("type", "")
    if record_type not in VALID_TYPES:
        errors.append(f"Invalid type: '{record_type}' (expected one of {VALID_TYPES})")

    if fm.get("license") != "CC-BY-SA-4.0":
        errors.append(f"License must be CC-BY-SA-4.0, got '{fm.get('license')}'")

    if isinstance(fm.get("traditions"), list) and len(fm["traditions"]) == 0:
        errors.append("Traditions list is empty (at least one required)")

    if isinstance(fm.get("sources"), list) and len(fm["sources"]) == 0:
        errors.append("Sources list is empty (at least one required)")

    body_match = re.search(r"^---\s*\n.*?\n---\s*\n(.+)", text, re.DOTALL)
    if not body_match or not body_match.group(1).strip():
        errors.append("No body content after frontmatter")

    return errors


def main():
    total_files = 0
    total_errors = 0
    error_files = 0

    for section in SECTIONS:
        section_dir = CONTENT_DIR / section
        if not section_dir.exists():
            continue
        for filepath in sorted(section_dir.glob("*.md")):
            if filepath.name.startswith("_"):
                continue
            total_files += 1
            errors = validate_file(filepath)
            if errors:
                error_files += 1
                total_errors += len(errors)
                print(f"\n✗ {filepath.relative_to(CONTENT_DIR)}")
                for e in errors:
                    print(f"    {e}")
            else:
                print(f"  ✓ {filepath.relative_to(CONTENT_DIR)}")

    print(f"\n{'='*50}")
    print(f"Files checked: {total_files}")
    print(f"Files with errors: {error_files}")
    print(f"Total errors: {total_errors}")

    if total_errors > 0:
        sys.exit(1)
    else:
        print("\nAll records valid.")
        sys.exit(0)


if __name__ == "__main__":
    main()
