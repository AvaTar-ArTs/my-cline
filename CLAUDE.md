# CLAUDE.md — Cline Agent Workspace

This file provides guidance for **Cline** when operating in its own home directory.

---

## Overview

`~/.cline/` is Cline's home — a self-managed workspace for scripts, skills, chat history, and configuration. Treat this like an operating base: maintain it, evolve it, and use it to remember what we've built.

## Key Directories

| Path | Purpose |
|------|---------|
| `scripts/` | Utility scripts for exporting, syncing, and maintenance |
| `chat-history/` | Exported conversation history (Cline + Gemini) |
| `chat-history/HABIT.md` | Docs on the chat history system |
| `data/` | Cline runtime data — **do not edit** (sessions, DB, logs) |
| `skills/` | Reusable skill definitions |

## Chat History System

Every session is automatically exported to `chat-history/` via three redundant layers:
1. **launchd** — Runs every 5 minutes (macOS native)
2. **cron** — Runs every hour (fallback)
3. **Manual** — `ai-export-all` shell command

Exports include thinking traces, tool calls, and full session metadata.

**When asked about past work**, search chat history:
```bash
ai-search "topic"     # Search both Cline + Gemini exports
cline-history         # List recent Cline exports
```

## Key Commands

```bash
ai-export-all              # Export all unexported sessions from both platforms
ai-stats                   # Show unified statistics
ai-search <term>           # Search all chat history
cline-export               # Export Cline sessions
gemini-export              # Export Gemini sessions
```

## Habits

1. **After every session**: Let the launchd agent handle auto-export (runs every 5 min)
2. **When exploring something new**: Save key findings in `chat-history/HABIT.md` or a new doc
3. **Before major changes to `~/.cline/`**: `git status` to check state
4. **Keep this workspace clean**: No CSV dumps, no temp files in root
