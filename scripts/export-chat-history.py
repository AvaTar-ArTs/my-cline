#!/usr/bin/env python3
"""Export Cline sessions to markdown. Saves thinking, tools, metadata."""
from __future__ import annotations
import json, os, sys, argparse
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

SESSIONS_DIR = Path.home() / ".cline" / "data" / "sessions"
OUTPUT_DIR = Path.home() / ".cline" / "chat-history"
TRACKING_FILE = OUTPUT_DIR / ".exported_sessions.json"
MIN_PROMPT = 10

def load_tracking():
    if TRACKING_FILE.exists():
        try: return set(json.loads(TRACKING_FILE.read_text()).get("exported", []))
        except: return set()
    return set()

def save_tracking(exp):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TRACKING_FILE.write_text(json.dumps({"exported": sorted(exp)}, indent=2))

def fmt_ts(ts):
    if ts is None: return "—"
    try:
        dt = datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    except: return str(ts)

def extract_blocks(blocks):
    lines = []
    for b in blocks:
        t = b.get("type", "")
        if t == "text":
            txt = b.get("text", "").strip()
            if txt: lines.append(txt + "\n")
        elif t == "thinking":
            th = b.get("thinking", "").strip()
            if th:
                lines.append("> 💭 **Thinking:**")
                for line in th.split("\n"): lines.append(f"> {line}")
                lines.append("")
        elif t == "tool_use":
            name = b.get("name", "?")
            inp = b.get("input", {})
            lines.append(f"🔧 **Tool: {name}**")
            s = json.dumps(inp, indent=2, default=str)
            if len(s) > 1500: s = s[:1500] + "\n…"
            lines.append(f"```json\n{s}\n```\n")
        elif t == "tool_result":
            res = b.get("content", "")
            tid = b.get("tool_use_id", "")
            rs = str(res)
            lines.append(f"📋 **Result** (`{tid}`):")
            if len(rs) > 1500:
                lines.append(f"_{len(rs)} chars, first 1500:_\n```\n{rs[:1500]}…\n```")
            else:
                lines.append(f"```\n{rs}\n```\n")
    return "\n".join(lines).strip()

def fmt_conversation(messages):
    parts = []
    for m in messages:
        role = m.get("role", "?")
        blocks = m.get("content", [])
        ts = m.get("ts")
        ts_s = f" *({fmt_ts(ts)})*" if ts else ""
        text = extract_blocks(blocks)
        if not text.strip(): continue
        icon = {"user": "👤", "assistant": "🤖", "system": "⚙️"}.get(role, "❓")
        parts.append(f"### {icon} {role.title()}{ts_s}\n\n{text}")
    return "\n\n---\n\n".join(parts)

def get_title(sd, msgs):
    p = sd.get("prompt", "")
    if p and len(p) > MIN_PROMPT:
        c = p.replace("<user_input", "").replace("</user_input>", "").strip()
        if c: return (c[:77] + "...") if len(c) > 80 else c
    for m in msgs:
        if m.get("role") == "user":
            for b in m.get("content", []):
                if b.get("type") == "text":
                    t = b.get("text", "").strip()
                    if t and len(t) > MIN_PROMPT:
                        return (t[:77] + "...") if len(t) > 80 else t
    return f"Session {sd.get('session_id', 'unknown')}"

def fmt_dur(start, end):
    if not start or not end: return "—"
    try:
        s = datetime.fromisoformat(start.replace("Z", "+00:00"))
        e = datetime.fromisoformat(end.replace("Z", "+00:00"))
        sec = int((e - s).total_seconds())
        if sec < 60: return f"{sec}s"
        if sec < 3600: return f"{sec//60}m {sec%60}s"
        return f"{sec//3600}h {(sec%3600)//60}m"
    except: return "—"

def export_session(session_dir, force=False):
    sid = session_dir.name
    mp = session_dir / f"{sid}.json"
    xp = session_dir / f"{sid}.messages.json"
    if not mp.exists() or not xp.exists(): return None
    try:
        sd = json.loads(mp.read_text())
        md = json.loads(xp.read_text())
    except Exception as e:
        print(f"  ⚠️  {sid}: {e}", file=sys.stderr)
        return None
    msgs = md if isinstance(md, list) else md.get("messages", [])
    if not msgs: return None
    if sd.get("status") == "running" and not force: return None
    meta = sd.get("metadata", sd)
    usage = meta.get("usage", meta.get("aggregateUsage", {}))
    it = usage.get("inputTokens", 0) if isinstance(usage, dict) else 0
    ot = usage.get("outputTokens", 0) if isinstance(usage, dict) else 0
    cost = meta.get("totalCost", meta.get("total_cost", 0))
    model = sd.get("model", meta.get("model", "?"))
    prov = sd.get("provider", meta.get("provider", "?"))
    cwd = sd.get("cwd", "—")
    start = sd.get("started_at", "—")
    end = sd.get("ended_at", "—")
    status = sd.get("status", "?")
    title = get_title(sd, msgs)
    dur = fmt_dur(start, end)
    conv = fmt_conversation(msgs)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    export = f'''# Cline Chat Export — {title}

**Exported**: {now}
**Session**: `{sid}` | **Status**: {status} | **Duration**: {dur}
**Model**: {model} | **Provider**: {prov}

## Metadata
| Field | Value |
|-------|-------|
| **Started** | {start} |
| **Ended** | {end or "—"} |
| **Cost** | ${cost:.6f} |
| **Input** | {it:,} |
| **Output** | {ot:,} |
| **Dir** | `{cwd}` |

---

{conv}
'''
    safe = "".join(c if c.isalnum() or c in " -_" else "_" for c in title).strip()[:100]
    ts_pfx = ""
    if start and start != "—":
        try:
            dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
            ts_pfx = dt.strftime("%Y%m%d_%H%M%S_")
        except: pass
    fname = f"{ts_pfx}{sid}_{safe}.md"
    (OUTPUT_DIR / fname).write_text(export)
    return sid

def main():
    p = argparse.ArgumentParser(description="Export Cline sessions to markdown.")
    p.add_argument("--recent", type=int, help="Last N completed sessions")
    p.add_argument("--all", action="store_true", help="All unexported completed")
    p.add_argument("--force", action="store_true", help="Re-export all")
    p.add_argument("--id", type=str, help="Specific session ID")
    args = p.parse_args()
    if not SESSIONS_DIR.exists():
        print(f"❌ Not found: {SESSIONS_DIR}", file=sys.stderr)
        sys.exit(1)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    exported = load_tracking()
    dirs = sorted(
        [d for d in SESSIONS_DIR.iterdir() if d.is_dir() and d.name[0].isdigit()],
        key=lambda d: d.stat().st_mtime, reverse=True,
    )
    if not dirs: print("📭 No sessions."); return
    if args.id:
        t = SESSIONS_DIR / args.id
        dirs = [t] if t.exists() else []
        if not dirs: print(f"❌ Not found: {args.id}"); sys.exit(1)
    elif args.recent: dirs = dirs[:args.recent]
    elif not args.all and not args.force: dirs = dirs[:1]
    ok, skip = 0, 0
    for d in dirs:
        sid = d.name
        if not args.force and sid in exported: skip += 1; continue
        r = export_session(d, force=args.force)
        if r: exported.add(r); ok += 1
        else: skip += 1
    save_tracking(exported)
    print(f"\n📊 {ok} exported, {skip} skipped")
    print(f"📍 {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
