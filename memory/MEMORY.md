# Session Memory

Persistent knowledge accumulated across sessions. Updated after every substantial interaction.

---

## 2026-05-13 — Full Ecosystem Deep Dive & ~/.cline/ Initialization

### What Was Built
- `~/.cline/` workspace with git, CLINE.md, aliases, scripts, agents, skills, memory
- Chat history export system (Cline + Gemini) with 3-layer redundancy
- Cross-platform ecosystem map (memory/ECOSYSTEM.md)
- Core agents cloned: self-evolution, code-reviewer, ecosystem-analyzer
- Core skills cloned: systematic-debugging, verification-before-completion

### User Preferences
- **No primary platform** — the ecosystem is fluid, not hierarchical
- **CLINE.md** not CLAUDE.md — Cline-native naming
- **BASE.md rejected** — prefers direct naming
- Everything self-contained in `~/.cline/` — aliases, scripts, config
- launchd over cron where possible (macOS native, more reliable)
- `eza` preferred over `ls` for directory listings

### Reusable Knowledge
- `git-ai` tracks AI authorship across 9 platforms — use `git-ai commit` not `git commit`
- `git-ai log --oneline -5` shows recent commits with AI attribution
- `git-ai blame <file>` shows line-by-line AI authorship
- `~/.cursor` → `~/iterm2/cursor-ecosystem/.cursor` (symlink)
- `ai-export-all` exports both Cline + Gemini sessions
- `ai-search <term>` searches all chat history across platforms
- `cline-export`, `gemini-export` for platform-specific exports
- My-supremepowers CHANGELOG.md is at `~/my-supremepowers/CHANGELOG.md`
- Codex has detailed task memories at `~/.codex/memories/MEMORY.md`

### Failures & How to Do Differently
- Git push failures from large files (>50MB): check file sizes before initial commit
- Git push failures from secrets: use `git filter-branch` or allowlist on GitHub
- `.git/index.lock` stale locks: `rm -f repo/.git/index.lock`
- Don't use `git add -A` in repos with large generated files — use targeted `git add`
- Codex's MEMORY.md pattern is better than my CHANGELOG.md — it captures user preferences and failure patterns, not just what was built
