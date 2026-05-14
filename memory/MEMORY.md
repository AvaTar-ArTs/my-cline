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


## 2026-05-14 — Ecosystem Completion & /save Command

### What Was Built
- **Book of Memory** at `~/Guides/book_of_memory/INDEX.md` — comprehensive single-volume analysis of all 10 platforms, governance architecture, agent ecosystem, business infrastructure, memory stack, toolchain, principles, and implementation roadmap
- **`/save` command** — exports current session as markdown, HTML, or JSON with workspace state snapshot
- **Snapshot script** at `~/.cline/scripts/save-current-session.sh`
- **Commands/save.md** — slash command definition
- **CLINE.md lifecycle hooks** updated with `/save` and `/export` handling

### What Was Discovered
- **Context-Expert-Agent worktree**: 1,064 Python scripts, 297K lines, 321MB
- **enriched-pythons.csv**: 12,995-file AI-classified inventory bridging scripts to agent framework
- **all_scan_worktrees.csv**: 6,184-row raw scan feeding classification pipeline
- **skills.sh**: Open agent skills registry — Cline is a listed agent, 14 superpowers skills in top 151
- **Stance**: Skills.sh is reference, not dependencies — Cline skills are original creations

### User Preferences
- Book of Memory = definitive single-volume document (not a skeleton)
- Don't remove existing docs — append and insert
- Skills.sh is reference, not something to import from
- Focus ~/.cline/ on original creations
- github repo AvaTar-ArTs/my-powers had old push failure

### Reusable Knowledge
- `npx skills` is the CLI for skills.sh ecosystem
- Content automation pipeline at `~/pythons/content_automation_system.py` targeting $10K/mo
- Security audit at `~/pythons/SECURITY_AUDIT_EVAL_EXEC_2026-04-12.md` — 4 eval/exec vulnerabilities fixed
- Marketplace deployment at `~/pythons/deploy_to_marketplaces.py` — CodeCanyon, Gumroad, Payhip, Sellfy

### Next Session Pickup
- Phase 1 partly done (brainstorm ✅, /save ✅)
- Phase 2 (agent expansion) and Phase 3 (skills expansion) are next
- Consider pushing my-powers repo with `git push --force`
