#!/bin/bash
# Save current session snapshot to ~/.cline/chat-history/
# Captures: conversation context, git state, memory state, recent exports
# Output: markdown (default), html, or json
#
# Usage: bash ~/.cline/scripts/save-current-session.sh [format]

set -euo pipefail

CLINE_HOME="$HOME/.cline"
CHAT_DIR="$CLINE_HOME/chat-history"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
FORMAT="${1:-md}"
SESSION_ID="${2:-}"

mkdir -p "$CHAT_DIR"

# --- Gather context ---

# Git log (recent commits)
GIT_LOG=$(cd "$CLINE_HOME" && git log --oneline -10 2>/dev/null || echo "No git history")

# Git status
GIT_STATUS=$(cd "$CLINE_HOME" && git status --short 2>/dev/null || echo "clean")

# Memory files content summary
MEMORY_FILES=$(for f in "$CLINE_HOME"/memory/*.md; do
    [ -f "$f" ] && echo "- $(basename "$f"): $(head -1 "$f")"
done)

# Recent exports list
EXPORT_COUNT=$(find "$CHAT_DIR" -name '*.md' -type f 2>/dev/null | wc -l || echo 0)
GEMINI_COUNT=$(find "$CHAT_DIR/gemini" -name '*.md' -type f 2>/dev/null | wc -l || echo 0)

# Launchd status
LAUNCHD_CLINE=$(launchctl list com.user.cline-chat-export 2>/dev/null | awk '{print $1}' || echo "not found")
LAUNCHD_GEMINI=$(launchctl list com.user.gemini-chat-export 2>/dev/null | awk '{print $1}' || echo "not found")

# git-ai status
GIT_AI=$(git-ai --version 2>/dev/null || echo "not installed")

# --- Build the snapshot ---

SNAPSHOT="---"
SNAPSHOT+="
title: Cline Session Snapshot
timestamp: $(date -u +"%Y-%m-%dT%H:%M:%SZ")
workspace: $CLINE_HOME
"

if [ -n "$SESSION_ID" ]; then
    SNAPSHOT+="session_id: $SESSION_ID"
fi

SNAPSHOT+="---
# Cline Session Snapshot

**Exported**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")
**Workspace**: \`$CLINE_HOME\`

---

## Git State (Recent)

\`\`\`
$GIT_LOG
\`\`\`

**Uncommitted**:
\`\`\`
$GIT_STATUS
\`\`\`

## Memory Files

$MEMORY_FILES

## Export Stats

| Metric | Value |
|--------|-------|
| Cline exports | $EXPORT_COUNT |
| Gemini exports | $GEMINI_COUNT |
| launchd (Cline) | $LAUNCHD_CLINE |
| launchd (Gemini) | $LAUNCHD_GEMINI |
| git-ai | $GIT_AI |

---

*Snapshot captured at $(date -u +"%Y-%m-%d %H:%M:%S UTC")*
"

# --- Write output ---

case "$FORMAT" in
    json)
        # Convert markdown to minimal JSON wrapper
        echo '{"type":"session_snapshot","timestamp":"'"$(date -u +"%Y-%m-%dT%H:%M:%SZ")"'","format":"json"}' > "$CHAT_DIR/snapshot_${TIMESTAMP}.json"
        echo "$SNAPSHOT" >> "$CHAT_DIR/snapshot_${TIMESTAMP}.json"
        echo "💾 Saved: $CHAT_DIR/snapshot_${TIMESTAMP}.json"
        ;;
    html)
        # Wrap in minimal HTML
        {
            echo '<!DOCTYPE html><html><head><meta charset="utf-8"><title>Cline Session Snapshot</title>'
            echo '<style>body{font-family:-apple-system,sans-serif;max-width:800px;margin:auto;padding:20px;}'
            echo 'pre{background:#f5f5f5;padding:10px;border-radius:4px;overflow:auto;}'
            echo 'table{border-collapse:collapse;width:100%}td,th{border:1px solid #ddd;padding:8px;text-align:left}'
            echo 'th{background:#f0f0f0}</style></head><body>'
            echo "$SNAPSHOT" | sed 's/^---.*$//' | sed '/^$/d' | while IFS= read -r line; do
                if [[ "$line" == \#\#\#* ]]; then echo "<h3>${line#\#\#\# }</h3>"
                elif [[ "$line" == \#\#* ]]; then echo "<h2>${line#\#\# }</h2>"
                elif [[ "$line" == \#* ]]; then echo "<h1>${line#\# }</h1>"
                elif [[ "$line" == \|-* ]]; then echo "<li>${line#- }</li>"
                elif [[ "$line" == \`\`\`* ]]; then echo "<pre>"
                elif [[ "$line" == "|"* ]]; then
                    if [[ "$line" == *"---"* ]]; then continue; fi
                    echo "<tr>"
                    echo "$line" | awk -F'|' '{for(i=2;i<NF;i++) print "<td>"$i"</td>"}'
                    echo "</tr>"
                else echo "<p>$line</p>"
                fi
            done
            echo '</body></html>'
        } > "$CHAT_DIR/snapshot_${TIMESTAMP}.html"
        echo "💾 Saved: $CHAT_DIR/snapshot_${TIMESTAMP}.html"
        ;;
    md|*)
        echo "$SNAPSHOT" > "$CHAT_DIR/snapshot_${TIMESTAMP}.md"
        echo "💾 Saved: $CHAT_DIR/snapshot_${TIMESTAMP}.md"
        ;;
esac

# Also run the regular export to catch any completed sessions
python3 "$CLINE_HOME/scripts/export-chat-history.py" --all 2>/dev/null || true
python3 "$CLINE_HOME/scripts/export-gemini-history.py" --all 2>/dev/null || true

echo "✅ Session snapshot saved ($FORMAT)"
