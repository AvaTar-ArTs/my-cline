# Cross-Platform Ecosystem Memory

**Purpose**: A single document any agent (Cline, Claude, Qwen, Gemini, Codex, Cursor)
can read to understand the full architecture of Steven's AI ecosystem.

**Canonical source of truth**: `~/my-supremepowers/`
**Agent workspace**: `~/.cline/`

---

## Six Platforms, One System

| Platform | Role | Size | Key Location | Git Remote |
|----------|------|------|-------------|------------|
| **my-supremepowers** | Canonical control plane | 1.2GB | `~/my-supremepowers/` | `AvaTar-ArTs/my-powers` |
| **Cline** | Self-managing agent | self | `~/.cline/` | `AvaTar-ArTs/my-cline` |
| **iterm2** | Mother repo / telemetry | 4.9GB | `~/iterm2/` | `GPTJunkie/iterm2` |
| **Cursor** | Desktop GUI (symlinked) | 1.2GB | `~/.cursor/` → `iterm2/cursor-ecosystem/.cursor` | (in iterm2) |
| **Qwen** | Integration workshop | 659MB | `~/.qwen/` | (local) |
| **Gemini** | Extension host | 2.4GB | `~/.gemini/` | (local) |
| **Codex** | Normalized runtime | 1.0GB | `~/.codex/` | (local) |

## Canonical Hierarchy

```
my-supremepowers (author here first)
    ↓
Qwen (integration/staging)
Gemini (extension host)
Codex (normalized runtime)
Cursor (GUI surface)
Cline (autonomous agent)
```

## Key Architecture Patterns

### 1. Fractal Self-Governance
Every platform follows: Governance Doc → Import Mechanism → Runtime → Tracking

| Level | Governance | Import | Runtime |
|-------|-----------|--------|---------|
| my-supremepowers | 5-tier system | npm sync + symlinks | Skills, agents, hooks |
| Qwen | Capability Registry | `qwen-sp` bootstrap | Hookify middleware |
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
- **launchd**: Every 5 min (Cline) / 6 min (Gemini) — macOS native
- **cron**: Every hour — fallback
- **Manual**: `ai-export-all` command
- Exports include: thinking traces, tool calls, metadata, timestamps

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
