---
description: "Export the current session as markdown, HTML, or JSON. Saves to ~/.cline/chat-history/."
---

# /save — Export Current Session

## Usage
```
/save                   ← Export as markdown (default)
/save html              ← Export as HTML (rich rendered)
/save json              ← Export as JSON (raw data)
/save --all             ← Export in all formats
```

## What it captures
- Full conversation (user prompts + AI responses)
- Thinking traces (if available)
- Tool calls with inputs and results
- Session metadata (model, tokens, timing, cost)
- Current workspace state (git log, recent files)
