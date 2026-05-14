# 📜 Chat History Habit

**Goal**: Every Cline session is automatically saved to `~/.cline/chat-history/`
with full thinking traces, tool calls, and metadata.

---

## How It Works

### 1. Automatic Export (Three Layers)

The system uses three redundant layers for maximum reliability:

**Layer 1 — launchd (Primary, runs every 5 min)**
macOS launchd agents fire every 5 minutes for Cline and every 6 minutes for Gemini.
They run at login, survive reboots, and are more reliable than cron:

```bash
# Cline: ~/Library/LaunchAgents/com.user.cline-chat-export.plist
/usr/bin/python3 ~/.cline/scripts/export-chat-history.py --all   # every 300s

# Gemini: ~/Library/LaunchAgents/com.user.gemini-chat-export.plist
/usr/bin/python3 ~/.cline/scripts/export-gemini-history.py --all # every 360s
```

**Layer 2 — Cron (Fallback, every hour)**
Traditional cron runs hourly as a safety net:

```
0 * * * * /usr/bin/python3 ~/.cline/scripts/export-chat-history.py --all
30 * * * * /usr/bin/python3 ~/.cline/scripts/export-gemini-history.py --all
```

**Layer 3 — Manual (On demand)**
Run anytime with a single command:

```bash
ai-export-all   # Exports both Cline + Gemini immediately
```

### 2. Manual Export

Run anytime to export immediately:

```bash
# Export all unexported completed sessions
python3 ~/.cline/scripts/export-chat-history.py --all

# Export last 5 sessions
python3 ~/.cline/scripts/export-chat-history.py --recent=5

# Re-export everything (even already exported)
python3 ~/.cline/scripts/export-chat-history.py --force

# Export a specific session by ID
python3 ~/.cline/scripts/export-chat-history.py --id=1778710977787_2cww9
```

### 3. View Your History

```bash
# List all exported sessions
ls -lt ~/.cline/chat-history/*.md

# Quickly open the most recent export
open "$(ls -t ~/.cline/chat-history/*.md | head -1)"

# Search all chat history
grep -l "some-topic" ~/.cline/chat-history/*.md
```

---

## What's Captured

Each export is a comprehensive markdown file containing:

| Feature | Included |
|---------|----------|
| ✅ **User prompts** | Full text of every user message |
| ✅ **Assistant responses** | Full text of every AI response |
| ✅ **Thinking traces** | `> 💭 **Thinking:**` block with reasoning |
| ✅ **Tool calls** | `🔧 **Tool: name**` with JSON input |
| ✅ **Tool results** | `📋 **Result**` with output |
| ✅ **Session metadata** | Model, provider, tokens, cost, timing |
| ✅ **Timestamps** | Per-message timestamps |
| ✅ **Duration** | Total session duration |
| ✅ **Working directory** | CWD at session start |

---

## Storage

- **Location**: `~/.cline/chat-history/`
- **Format**: `YYYYMMDD_HHMMSS_<session-id>_<title>.md`
- **Tracking**: `.exported_sessions.json` (prevents duplicate exports)
- **Retention**: All sessions kept indefinitely; clean up manually if desired

---

## Session Source

Cline stores raw session data in `~/.cline/data/sessions/<session-id>/`:
- `<session-id>.json` — Session metadata (model, tokens, cost, timing)
- `<session-id>.messages.json` — Full conversation with thinking traces

The export script reads these, formats them into beautiful markdown, and
saves them to `~/.cline/chat-history/`.

---

## The Rule

> **After every substantial session (or at end of day), run:**
> ```bash
> python3 ~/.cline/scripts/export-chat-history.py --all
> ```
>
> This ensures your conversation history, including all AI reasoning,
> tool usage, and decisions, is permanently saved for future reference.

The cron job handles this automatically — but running manually after
key sessions gives you immediate access to the export.
