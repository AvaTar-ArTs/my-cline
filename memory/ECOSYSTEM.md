# Cross-Platform Ecosystem Memory

**Purpose**: A single document any agent can read to understand the current
landscape. This is a snapshot, not an authority — the system is fluid and evolving.

**There is no primary.** Each platform leads when it's the right tool.

---

## The Platforms

| Platform | Size | Location | Git |
|----------|------|----------|-----|
| **my-supremepowers** | 1.2GB | `~/my-supremepowers/` | `AvaTar-ArTs/my-powers` |
| **Cline** | self | `~/.cline/` | `AvaTar-ArTs/my-cline` |
| **iterm2** | 4.9GB | `~/iterm2/` | `GPTJunkie/iterm2` |
| **Cursor** | 1.2GB | `~/.cursor/` → `iterm2/cursor-ecosystem/.cursor` | (in iterm2) |
| **Qwen** | 659MB | `~/.qwen/` | (local) |
| **Gemini** | 2.4GB | `~/.gemini/` | (local) |
| **Codex** | 1.0GB | `~/.codex/` | (local) |

## Flow, Not Hierarchy

There is no canonical source. Different platforms carry the latest work
at different times depending on what's being built and which tool fits.
The ecosystem is fluid — ideas, agents, and patterns move between platforms
as the work demands. What was "authoritative" last week may be legacy today.

## Architecture Pattern (Recurring, Not Prescribed)

Every platform tends toward the same pattern, but not because one dictates it —
because it emerges from what works:

```
Governance Doc → Import/Adapt Mechanism → Runtime → Memory/Tracking
```

## Agent Suite (~40 core definitions that replicate across platforms)

### Meta-Cognition
self-evolution, integrated-evolution, ecosystem-learning, ecosystem-synergy, capability-atlas

### Engineering Roles
system-architect, backend-architect, frontend-architect, api-specialist, database-specialist, devops-engineer, python-expert, javascript-expert, performance-engineer, security-engineer, testing-specialist, technical-writer

### Operations
code-reviewer, ecosystem-analyzer, filesystem-inventory, path-list-analyzer, tree-explorer, context-handoff-compiler, content-consolidator, content-organizer

### Business
revenue-optimizer, xeo-strategist, seo-keyword-analyst, project-launch-manager, knowledge-automation-strategist

## Key Architecture Patterns
## git-ai — Universal Authorship Tracking

`git-ai` is a git proxy that automatically attributes every commit to the AI tool
that authored it. It intercepts git operations across all platforms via hooks.

### What It Tracks Per Commit
- Which **AI tool** (claude, gemini, cursor, codex, cline, etc.)
- Which **model** (claude-sonnet-4-5, gemini-2.5-flash, gpt-5.5, etc.)
- Which **human author** approved the changes
- The **prompts** that generated the changes (with URLs to view them)
- Lines **accepted** vs **overridden**

### Commands
```bash
git-ai log --oneline -5          # Recent commits with AI attribution
git-ai blame <file>              # Line-by-line AI authorship
git-ai stats                     # AI authorship statistics
git-ai install-hooks             # Install/update hooks across all platforms
```

### Platforms With Hooks Installed
Claude Code, Codex, Cursor, VS Code, GitHub Copilot, OpenCode, Gemini, Windsurf

### How to Use
Use `git-ai commit` instead of `git commit` (or let the hooks handle it automatically).
The hooks are already installed — commits made through AI tooling should auto-attribute.

### 1. Fractal Self-Governance
Every platform follows: Governance Doc → Import Mechanism → Runtime → Tracking

| Level | Governance | Import | Runtime |
|-------|-----------|--------|---------|
| my-supremepowers | 5-tier system | npm sync + symlinks | Skills, agents, hooks |
| Qwen | Capability Registry | `qwen-sp` bootstrap | Hookify middleware |
## AutoTagger — File Scanner + n8n Workflow Marketplace

| | |
|---|---|
| **Location** | `~/AutoTagger/` |
| **Size** | 730MB |
| **Git** | `AvaTar-ArTs/AutoTagger` |

### Core Tool
`current/autotagger.py` — Python file scanner with semantic awareness, SQLite output, CSV/HTML/MD reporting. CLI entry: `autotag <directory> [prefix]`

### n8n Workflow Library (13 packages)
Self-contained workflow packages under `n8n_workflows/workflows/`:
- **Free**: trend-analyzer-free
- **Pro (12)**: trend-analyzer-pro, ai-note-taker-pro, content-repurposing-pro, ai-voice-generator-pro, local-llm-assistant-pro, private-gpt-rag-pro, ai-video-generator-pro, faceless-youtube-automation-pro, tiktok-ai-generator-pro, aeo-optimizer-pro, agentic-workflow-builder-pro, multimodal-pipeline-pro

Each package has `workflow.json` (n8n import), `.env.example`, and `README.md`.

### V6 SaaS Bundle
`V6.md`, `V6_SAAS_OVERVIEW.md`, `saas/` strategy + roadmap, `saas_landing_v1.html`
| Codex | Agent Normalization Registry | Qwen→Codex staging | Command wrappers |
| Cline | CLINE.md | Manual scripts | launchd + lifecycle hooks |

### 2. Agent Normalization Pipeline (Codex)
Codex has a 4-tier system for importing agents from Qwen:
- **Tier 1**: Engineering roles → normalize to Codex-ready blueprints
- **Tier 2**: Workflow agents → convert to checklists/skills
- **Tier 3**: Broad agents → distill into bounded instructions
- **Tier 4**: Domain-specific → reference only

### 3. Chat History System (Cline)
3-layer redundancy for session persistence:
- **launchd** (5 min Cline, 6 min Gemini) ✅ Active — both `LastExitStatus=0`
- **cron** (hourly Cline + hourly@:30 Gemini) ✅ Active
- **Manual**: `ai-export-all` / `cline-export` / `gemini-export`
- Exports include: thinking traces, tool calls, metadata, timestamps

**Known fix applied**: Script was crashing on string-type content blocks (not dicts) in some sessions. Fixed 2026-05-14 with `isinstance(b, dict)` guard.

### 4. The Cline Lifecycle
- **On startup**: Export previous sessions, read memory
- **Every ~10 tool calls**: Export if work was done
- **On goodbye**: Export current session, update memory
- **/export**: Immediate manual save

## Active Revenue Infrastructure

| Product | Status | Target |
|---------|--------|--------|
| AVATARARTS WORKFORCE ($99/mo) | Launch-ready | $15K/mo |
| XEO INTELLIGENCE ENGINE ($2.5K setup + $300/mo) | Service-ready | $7.5K/mo |
| LOFI EMPIRE (ad rev + sponsorships) | Content-ready | $10K/mo |
| **Combined** | | **$25K-$35K/mo** |
| Marketplace Python scripts (4,338+) | Dispersed across platforms | $950K+ potential |

## Key Agent Suite (~40 core agents)

### Meta-Cognition
self-evolution, integrated-evolution, ecosystem-learning, ecosystem-synergy, capability-atlas

### Engineering Roles
system-architect, backend-architect, frontend-architect, api-specialist, database-specialist, devops-engineer, python-expert, javascript-expert, performance-engineer, security-engineer, testing-specialist, technical-writer

### Operations
code-reviewer, ecosystem-analyzer, filesystem-inventory, path-list-analyzer, tree-explorer, context-handoff-compiler, content-consolidator, content-organizer

### Business
revenue-optimizer, xeo-strategist, seo-keyword-analyst, project-launch-manager, knowledge-automation-strategist

## Memory Locations by Platform

| Platform | Memory/Context Location |
|----------|------------------------|
| **Cline** | `~/.cline/memory/INDEX.md`, `~/.cline/memory/ECOSYSTEM.md` |
| **Cline** | `~/.cline/chat-history/` (auto-exported sessions) |
| **my-supremepowers** | `docs/`, `CHANGELOG.md`, `How-To.md` |
| **Qwen** | `~/.qwen/docs/learned-context.md` |
| **Cursor** | `~/.cursor/CHAT_MEMORY.md` |
| **Qwen** | `~/.qwen/docs/CHANGELOG.md` |

## Quick Reference Commands

```bash
# Export all unexported sessions (Cline + Gemini)
ai-export-all

# Search all chat history
ai-search "<topic>"

# Show unified stats
ai-stats

# List recent exports
cline-history
gemini-history
```

---

*Last updated: 2026-05-13*
*Next review: When any platform configuration changes*
