# CLINE.md — Cline Agent Workspace

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
| `memory/` | Persistent context across sessions |

## Chat History System

Every session is automatically exported to `chat-history/` via redundant layers:
1. **launchd** — Every 5 min (Cline) / 6 min (Gemini)
2. **cron** — Every hour (fallback)
3. **Cline itself** — via lifecycle hooks below

Exports include thinking traces, tool calls, and full session metadata.
### On /save or /export command
When the user invokes `/save` or `/export`:
1. Run `bash ~/.cline/scripts/save-current-session.sh [format]`
2. The format argument is optional: md (default), html, json
3. This captures current workspace state and triggers any pending completed session exports

## Lifecycle Hooks (Cline's Own Behavior)

These are rules Cline follows automatically — no external scheduler required.

### On Startup (session begins)
Run `ai-export-all` to capture any completed sessions since last run:
- `python3 ~/.cline/scripts/export-chat-history.py --all`
- `python3 ~/.cline/scripts/export-gemini-history.py --all`

### During Session (periodic)
After every **10 tool calls**, if significant work was done, run:
```bash
python3 ~/.cline/scripts/export-chat-history.py --all
```
This ensures partial progress is saved even during long sessions.

### On Completion / Goodbye (session ends)
When the user indicates the session is done, or says goodbye/quit/thanks, run export **before** the final message:
```bash
python3 ~/.cline/scripts/export-chat-history.py --all
python3 ~/.cline/scripts/export-gemini-history.py --all
```
Then record key facts in `memory/INDEX.md`.

### /export Command
When the user types `/export` or asks to save/export, run:
```bash
ai-export-all
```
And confirm: "✅ Sessions exported to `~/.cline/chat-history/`"

## Searching Past Work

```bash
ai-search "topic"     # Search both Cline + Gemini exports
## Agents (Cline-native definitions)

| Agent | File | When to Use |
|-------|------|-------------|
| **self-evolution** | `agents/self-evolution.md` | After sessions — reflect, extract, improve |
| **code-reviewer** | `agents/code-reviewer.md` | Before claiming work is done |
| **ecosystem-analyzer** | `agents/ecosystem-analyzer.md` | When auditing platform state |

## Skills (Cline-native)

| Skill | File | Trigger |
|-------|------|---------|
| **chat-history-export** | `skills/chat-history-export/SKILL.md` | Export / save / backup |
| **systematic-debugging** | `skills/systematic-debugging/SKILL.md` | Fix / debug / error / broken |
| **verification-before-completion** | `skills/verification-before-completion/SKILL.md` | Done / complete / finished |
cli-history           # List recent Cline exports
gemini-history        # List recent Gemini exports
```

## Aliases

Shell aliases and functions are in `~/.cline/aliases.zsh` (sourced from `~/.zshrc`).
## Session Memory

After every session, record key facts in `memory/MEMORY.md` following Codex's pattern:
- **What was built / learned**
- **User preferences** (how Steven wants things done)
- **Reusable knowledge** (patterns, commands, paths)
- **Failures and how to do differently** (what went wrong, how to avoid it)

This turns every session into a compounding knowledge base.

## Key Commands

```bash
ai-export-all              # Export all unexported from both platforms
ai-stats                   # Show unified statistics
ai-search <term>           # Search all chat history
cline-export               # Export Cline sessions
gemini-export              # Export Gemini sessions
```

## Habits

1. **On startup**: Export previous sessions
2. **Every ~10 tool calls**: Export if work happened
3. **On goodbye**: Export + update memory before finishing
4. **/export any time**: User can trigger manual save
5. **Keep this workspace clean**: No CSV dumps, no temp files in root
