# Skill: Chat History Export

Export Cline and Gemini conversations to markdown for persistence and review.

## When to Use

- At the end of any substantial session
- When asked "what did we work on before?"
- Before making major changes to the workspace

## How to Use

### Automatic (Preferred)

The system exports automatically via launchd (every 5 min) and cron (every hour).
No action needed — session data is captured within minutes of completion.

### Manual

```bash
ai-export-all     # Export all unexported from both Cline + Gemini
cline-export      # Export only Cline sessions
gemini-export     # Export only Gemini sessions
```

### Search Past Sessions

```bash
ai-search "error handling"     # Search all exported history
cline-history                   # List recent Cline exports
gemini-history                  # List recent Gemini exports
```

### View Most Recent

```bash
cline-latest     # Open most recent Cline export
gemini-latest    # Open most recent Gemini export
```

## What Gets Saved

| Component | Content |
|-----------|---------|
| User messages | Full text of every prompt |
| AI responses | Full text of every answer |
| Thinking traces | Internal reasoning (💭 blocks) |
| Tool calls | Function inputs with JSON |
| Tool results | Outputs (truncated if large) |
| Metadata | Model, cost, tokens, timestamps |

## Storage

- **Location**: `~/.cline/chat-history/`
- **Cline exports**: `~/.cline/chat-history/<date>_<session>_<title>.md`
- **Gemini exports**: `~/.cline/chat-history/gemini/<date>_<session>_<title>.md`
- **Tracking**: `.exported_sessions.json` / `.exported_gemini.json`
- **Auto-export**: launchd (5 min) + cron (1 hour) + manual
