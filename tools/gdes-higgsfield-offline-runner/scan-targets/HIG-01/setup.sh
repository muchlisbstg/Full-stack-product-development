#!/usr/bin/env bash
# HIG-01 remediation candidate — setup
# Source baseline: higgsfield-ai/skills@27000402070db19d958789d05b3b52b6f4718d7c
# F01 control: never download or execute a mutable remote installer.
# CLI provisioning is deliberately out of scope and must be performed separately.
# Any future installer requires a pinned commit SHA and independent digest verification.
# through an independently verified, user-approved distribution process.
set -euo pipefail

say() { printf '%s\n' "$1"; }
fail() { printf 'ERROR: %s\n' "$1" >&2; exit 1; }

SKILL_DIR="$(cd "$(dirname "$0")" && pwd)"
[ -f "$SKILL_DIR/VERSION" ] || fail "VERSION file missing; run from the pinned skills source root."

HOST=""
TARGET_OVERRIDE=""
while [ "$#" -gt 0 ]; do
  case "$1" in
    --host)
      [ "$#" -ge 2 ] || fail "--host requires claude, cursor, or codex"
      HOST="$2"; shift 2 ;;
    --host=*)
      HOST="${1#--host=}"; shift ;;
    --target-dir)
      [ "$#" -ge 2 ] || fail "--target-dir requires a directory"
      TARGET_OVERRIDE="$2"; shift 2 ;;
    --help|-h)
      say "Usage: ./setup --host <claude|cursor|codex> [--target-dir DIR]"
      say "This script does not install the Higgsfield CLI or authenticate."
      exit 0 ;;
    *)
      fail "Unknown option: $1" ;;
  esac
done

case "$HOST" in
  claude) TARGET_DIR="${HOME}/.claude/skills" ;;
  cursor) TARGET_DIR="${HOME}/.cursor/plugins" ;;
  codex)  TARGET_DIR="${HOME}/.agents/skills" ;;
  *) fail "Explicit --host is required; automatic host detection is disabled." ;;
esac
[ -n "$TARGET_OVERRIDE" ] && TARGET_DIR="$TARGET_OVERRIDE"

# Require an existing parent and reject a symlink target directory.
TARGET_PARENT="$(dirname "$TARGET_DIR")"
[ -d "$TARGET_PARENT" ] || fail "Target parent must already exist: $TARGET_PARENT"
[ ! -L "$TARGET_DIR" ] || fail "Target directory must not be a symlink."
if [ -e "$TARGET_DIR" ] && [ ! -d "$TARGET_DIR" ]; then
  fail "Target exists but is not a directory: $TARGET_DIR"
fi

# CLI must be provisioned separately; this script never downloads or executes installers.
if ! command -v higgsfield >/dev/null 2>&1; then
  fail "Higgsfield CLI is absent. Stop here; use a separately reviewed, pinned, user-approved installer."
fi

SKILLS=(higgsfield-generate higgsfield-soul-id higgsfield-product-photoshoot higgsfield-brandkit higgsfield-marketplace-cards higgsfield-websites higgsfield-faceless-video higgsfield-video-explainer higgsfield-youtube-thumbnail)
mkdir -p "$TARGET_DIR"
for skill in "${SKILLS[@]}"; do
  src="$SKILL_DIR/$skill"
  dst="$TARGET_DIR/$skill"
  [ -d "$src" ] || fail "Source missing: $src"
  if [ -L "$dst" ]; then
    [ "$(readlink "$dst")" = "$src" ] || fail "Conflicting symlink exists: $dst"
  elif [ -e "$dst" ]; then
    fail "Destination exists; refusing to overwrite: $dst"
  else
    ln -s "$src" "$dst"
  fi
  [ -f "$dst/SKILL.md" ] || fail "Skill verification failed: $skill"
done
say "Skills linked. No CLI installation, authentication, network request, or provider action was performed."
