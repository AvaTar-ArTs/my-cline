# Chat History Habit

Goal: Every Cline session auto-saved to ~/.cline/chat-history/ with thinking traces, tool calls, and metadata.

## Automation
- launchd: 5 min (Cline) + 6 min (Gemini) — Active
- cron: Hourly + :30 fallback — Active
- Manual: python3 ~/.cline/scripts/export-chat-history.py --all

## Commands
- cline-export — Export all unexported
- cline-history — List recent exports
- cline-latest — Open most recent
- cline-stats — Summary

## Captured Per Session
User prompts, AI responses, thinking traces, tool calls with JSON, tool results, metadata (model, tokens, cost, timing)

