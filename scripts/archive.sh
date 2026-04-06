#!/usr/bin/env bash
#
# Archive The Human Record to multiple preservation targets.
#
# Targets:
#   1. Internet Archive (via ia CLI)
#   2. Software Heritage (auto-archived from GitHub)
#   3. IPFS (optional, if ipfs CLI available)
#
# Prerequisites:
#   - Internet Archive CLI: pip install internetarchive
#   - IPFS CLI (optional): https://docs.ipfs.tech/install/
#
# Usage:
#   ./scripts/archive.sh [version]
#   Example: ./scripts/archive.sh 0.1.0

set -euo pipefail

VERSION="${1:-$(date +%Y%m%d)}"
PROJECT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SNAPSHOT_DIR="$PROJECT_DIR/snapshots"
ARCHIVE_NAME="the-human-record-${VERSION}"

echo "=== The Human Record — Archive Script ==="
echo "Version: $VERSION"
echo ""

# Create snapshot
echo "1. Creating snapshot..."
mkdir -p "$SNAPSHOT_DIR"
SNAPSHOT_FILE="$SNAPSHOT_DIR/${ARCHIVE_NAME}.tar.gz"

tar -czf "$SNAPSHOT_FILE" \
  --exclude='.git' \
  --exclude='node_modules' \
  --exclude='public' \
  --exclude='snapshots/*.tar.gz' \
  -C "$(dirname "$PROJECT_DIR")" \
  "$(basename "$PROJECT_DIR")"

echo "   Created: $SNAPSHOT_FILE"
CHECKSUM=$(shasum -a 256 "$SNAPSHOT_FILE" | cut -d' ' -f1)
echo "   SHA-256: $CHECKSUM"

# Internet Archive
echo ""
echo "2. Internet Archive..."
if command -v ia &>/dev/null; then
  ia upload "$ARCHIVE_NAME" "$SNAPSHOT_FILE" \
    --metadata="title:The Human Record v${VERSION}" \
    --metadata="description:A public library of durable human values, moral tensions, and cross-cultural wisdom." \
    --metadata="creator:The Human Record Contributors" \
    --metadata="licenseurl:https://creativecommons.org/licenses/by-sa/4.0/" \
    --metadata="subject:human values;ethics;wisdom;open data;digital preservation" \
    --metadata="mediatype:data" \
    && echo "   Uploaded to Internet Archive." \
    || echo "   Upload failed. Check ia credentials."
else
  echo "   SKIP: 'ia' CLI not found. Install: pip install internetarchive"
fi

# Software Heritage
echo ""
echo "3. Software Heritage..."
echo "   Software Heritage automatically archives public GitHub repos."
echo "   Ensure the repo is public at: https://github.com/thehumanrecord/thehumanrecord"
echo "   Trigger manual archive: https://archive.softwareheritage.org/save/"

# IPFS
echo ""
echo "4. IPFS..."
if command -v ipfs &>/dev/null; then
  CID=$(ipfs add -r -Q "$PROJECT_DIR/data/")
  echo "   Added to IPFS. CID: $CID"
  echo "   Gateway: https://ipfs.io/ipfs/$CID"
else
  echo "   SKIP: 'ipfs' CLI not found. Install: https://docs.ipfs.tech/install/"
fi

echo ""
echo "=== Archive complete ==="
echo "Snapshot: $SNAPSHOT_FILE"
echo "Checksum: $CHECKSUM"
