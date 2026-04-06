#!/usr/bin/env python3
"""
Export The Human Record content to JSONL and CSV formats.

Reads all Markdown files in content/, extracts YAML frontmatter
and body text, and writes structured dataset files.

Usage:
    python scripts/export-dataset.py

Output:
    data/human-record.jsonl
    data/human-record.csv
    data/checksums.sha256
"""

import csv
import hashlib
import json
import os
import re
import sys
from pathlib import Path

CONTENT_DIR = Path(__file__).parent.parent / "content"
DATA_DIR = Path(__file__).parent.parent / "data"
SECTIONS = ["values", "tensions", "parables", "proverbs"]


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Extract YAML frontmatter and body from a Markdown file."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)", text, re.DOTALL)
    if not match:
        return {}, text

    yaml_str, body = match.group(1), match.group(2).strip()

    try:
        import yaml
        frontmatter = yaml.safe_load(yaml_str)
    except ImportError:
        frontmatter = _parse_yaml_simple(yaml_str)

    return frontmatter or {}, body


def _parse_yaml_simple(yaml_str: str) -> dict:
    """Minimal YAML parser for flat frontmatter when PyYAML is unavailable."""
    result = {}
    for line in yaml_str.split("\n"):
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("-"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            if val:
                result[key] = val
    return result


def collect_records() -> list[dict]:
    """Collect all records from content directories."""
    records = []
    for section in SECTIONS:
        section_dir = CONTENT_DIR / section
        if not section_dir.exists():
            continue
        for filepath in sorted(section_dir.glob("*.md")):
            if filepath.name.startswith("_"):
                continue
            text = filepath.read_text(encoding="utf-8")
            frontmatter, body = parse_frontmatter(text)
            if not frontmatter.get("id"):
                continue
            record = {**frontmatter, "body": body, "section": section}
            records.append(record)
    return records


def write_jsonl(records: list[dict], path: Path) -> None:
    """Write records as newline-delimited JSON."""
    with open(path, "w", encoding="utf-8") as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False, default=str) + "\n")
    print(f"  Wrote {len(records)} records to {path}")


def write_csv(records: list[dict], path: Path) -> None:
    """Write a summary CSV with core fields."""
    fields = [
        "id", "title", "type", "section", "summary",
        "created", "updated", "version", "license"
    ]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        for record in records:
            row = {k: record.get(k, "") for k in fields}
            writer.writerow(row)
    print(f"  Wrote {len(records)} records to {path}")


def write_checksums(data_dir: Path) -> None:
    """Generate SHA-256 checksums for all data files."""
    checksum_path = data_dir / "checksums.sha256"
    with open(checksum_path, "w", encoding="utf-8") as f:
        for filepath in sorted(data_dir.glob("*")):
            if filepath.name == "checksums.sha256":
                continue
            sha = hashlib.sha256(filepath.read_bytes()).hexdigest()
            f.write(f"{sha}  {filepath.name}\n")
    print(f"  Wrote {checksum_path}")


def main():
    DATA_DIR.mkdir(exist_ok=True)

    print("Collecting records...")
    records = collect_records()
    if not records:
        print("No records found. Check content/ directory.")
        sys.exit(1)

    print(f"Found {len(records)} records.\n")

    print("Exporting JSONL...")
    write_jsonl(records, DATA_DIR / "human-record.jsonl")

    print("Exporting CSV...")
    write_csv(records, DATA_DIR / "human-record.csv")

    print("Generating checksums...")
    write_checksums(DATA_DIR)

    print(f"\nDone. Dataset files are in {DATA_DIR}/")


if __name__ == "__main__":
    main()
