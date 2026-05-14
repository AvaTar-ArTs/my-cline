---
name: systematic-debugging
description: Four-phase root cause analysis before fixing bugs. Investigate → Analyze → Test → Implement.
---

# Systematic Debugging

## Phase 1: Root Cause Investigation
1. Read the error fully — don't skim
2. Reproduce the issue
3. Check what changed recently (git log, memory/CHANGELOG.md)
4. Check relevant config files

## Phase 2: Pattern Analysis
1. Find working examples of similar patterns in this codebase
2. Compare the broken code to working code
3. Identify the delta

## Phase 3: Hypothesis Testing
1. Form a specific hypothesis about root cause
2. Test it with minimal reproduction
3. Confirm or discard, then iterate

## Phase 4: Implementation
1. Fix the root cause, not the symptom
2. Verify the fix resolves the issue
3. Log what was learned in memory/CHANGELOG.md
