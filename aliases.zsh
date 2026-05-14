# ── AI Chat History ──────────────────────────────────────────────
# Export, view, and search conversation history from Cline + Gemini.
# Sourced from ~/.zshrc → ~/.cline/aliases.zsh

export CLINE_CHAT_HISTORY="$HOME/.cline/chat-history"
export CLINE_EXPORT_SCRIPT="$HOME/.cline/scripts/export-chat-history.py"
export GEMINI_EXPORT_SCRIPT="$HOME/.cline/scripts/export-gemini-history.py"

# ── Cline Commands ──
alias cline-export='python3 "$CLINE_EXPORT_SCRIPT" --all'
alias cline-export-recent='python3 "$CLINE_EXPORT_SCRIPT" --recent'
alias cline-export-force='python3 "$CLINE_EXPORT_SCRIPT" --force'

alias cline-export='python3 "$CLINE_EXPORT_SCRIPT" --all'
alias cline-export-recent='python3 "$CLINE_EXPORT_SCRIPT" --recent'
alias cline-export-force='python3 "$CLINE_EXPORT_SCRIPT" --force'
alias cline-history='ls -lt "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | head -20 | eza --icons=never 2>/dev/null || ls -lt "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | head -20'
alias cline-latest='open "$(ls -t "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | head -1)"'
alias cline-count='ls "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | wc -l | tr -d " "'

# ── Gemini Commands ──

alias gemini-export='python3 "$GEMINI_EXPORT_SCRIPT" --all'
alias gemini-export-force='python3 "$GEMINI_EXPORT_SCRIPT" --force'
alias gemini-history='ls -lt "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | head -20 | eza --icons=never 2>/dev/null || ls -lt "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | head -20'
alias gemini-latest='open "$(ls -t "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | head -1)"'
alias gemini-count='ls "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | wc -l | tr -d " "'

# ── Cross-Platform Search ──

# Search ALL chat history (Cline + Gemini) for a term
ai-search() {
    if [ $# -eq 0 ]; then
        echo "Usage: ai-search <search-term>"
        return 1
    fi
# /save — Export current session
alias cline-save='bash ~/.cline/scripts/save-current-session.sh'
alias cline-save-md='bash ~/.cline/scripts/save-current-session.sh md'
alias cline-save-html='bash ~/.cline/scripts/save-current-session.sh html'
alias cline-save-json='bash ~/.cline/scripts/save-current-session.sh json'
    local term="$*"
    echo "🔍 Searching all AI chat history for: $term"
    echo ""
    # Cline exports
    local cline_hits=$(grep -l "$term" "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | wc -l | tr -d " ")
    if [ "$cline_hits" -gt 0 ]; then
        echo "📖 Cline ($cline_hits matches):"
        grep -l "$term" "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | while read f; do
            echo "   📄 $(basename "$f")"
        done
    fi
    # Gemini exports
    local gemini_hits=$(grep -l "$term" "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | wc -l | tr -d " ")
    if [ "$gemini_hits" -gt 0 ]; then
        echo ""
        echo "🌐 Gemini ($gemini_hits matches):"
        grep -l "$term" "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | while read f; do
            echo "   📄 $(basename "$f")"
        done
    fi
    if [ "$cline_hits" -eq 0 ] && [ "$gemini_hits" -eq 0 ]; then
        echo "   No matches found."
    fi
}

# Export ALL AI chat history (Cline + Gemini)
ai-export-all() {
    echo "🔄 Exporting Cline sessions..."
    python3 "$CLINE_EXPORT_SCRIPT" --all
    echo ""
    echo "🔄 Exporting Gemini sessions..."
    python3 "$GEMINI_EXPORT_SCRIPT" --all
}

# Unified stats across both platforms
ai-stats() {
    local cline_count=$(ls "$CLINE_CHAT_HISTORY"/*.md 2>/dev/null | wc -l | tr -d " ")
    local gemini_count=$(ls "$CLINE_CHAT_HISTORY/gemini"/*.md 2>/dev/null | wc -l | tr -d " ")
    local gemini_sub_count=$(ls -d "$CLINE_CHAT_HISTORY/gemini"/*/ 2>/dev/null | wc -l | tr -d " ")
    local cline_size=$(du -sh "$CLINE_CHAT_HISTORY" 2>/dev/null | cut -f1)
    echo "📊 AI Chat History (Unified)"
    echo "   ┌─────────────────────┬──────────┬──────────┐"
    echo "   │ Platform            │ Sessions │ Size     │"
    echo "   ├─────────────────────┼──────────┼──────────┤"
    printf "   │ %-19s │ %8s │ %8s │\n" "Cline" "$cline_count" "$cline_size"
    printf "   │ %-19s │ %8s │ %8s │\n" "Gemini" "$gemini_count" "—"
    echo "   └─────────────────────┴──────────┴──────────┘"
    echo ""
    echo "   Commands:"
    echo "   ai-export-all         Export all unexported from both platforms"
    echo "   ai-search <term>     Search both Cline + Gemini history"
    echo "   ai-stats             Show this summary"
    echo "   ──"
    echo "   cline-*              Cline-specific commands"
    echo "   gemini-*             Gemini-specific commands"
}
