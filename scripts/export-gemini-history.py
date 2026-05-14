#!/usr/bin/env python3
"""Export Gemini CLI sessions to markdown history.

Reads from:  ~/.gemini/tmp/users/chats/
Writes to:   ~/.cline/chat-history/gemini/
Includes thoughts (thinking traces), tool calls, metadata.
"""
from __future__ import annotations
import json, os, sys, argparse, re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

GEMINI_DIR = Path.home() / ".gemini" / "tmp" / "users" / "chats"
OUTPUT_DIR = Path.home() / ".cline" / "chat-history" / "gemini"
TRACKING_FILE = Path.home() / ".cline" / "chat-history" / ".exported_gemini.json"

def load_tracking():
    if TRACKING_FILE.exists():
        try: return set(json.loads(TRACKING_FILE.read_text()).get("exported", []))
        except: return set()
    return set()

def save_tracking(exp):
    TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKING_FILE.write_text(json.dumps({"exported": sorted(exp)}, indent=2))

def parse_gemini_jsonl(path: Path) -> List[Dict]:
    """Parse a Gemini JSONL file into structured conversation entries."""
    entries = []
    session_info = {}
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line: continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            continue
        # First line is session metadata
        if "sessionId" in obj and "startTime" in obj and "kind" in obj and "id" not in obj:
            session_info = obj
            continue
        # $set lines are metadata updates
        if "$set" in obj:
            continue
        # Normal message entries
        if "type" in obj:
            entries.append(obj)
    return entries, session_info

def format_thoughts(thoughts: List[Dict]) -> str:
    if not thoughts: return ""
    lines = ["> 💭 **Thinking:**"]
    for t in thoughts:
        subj = t.get("subject", "")
        desc = t.get("description", "")
        ts = t.get("timestamp", "")
        if subj: lines.append(f"> **{subj}**")
        if desc: lines.append(f"> {desc}")
        if ts: lines.append(f"> *({ts})*")
        lines.append(">")
    return "\n".join(lines).strip()

def format_content(content) -> str:
    """Format the content field - can be string or list of objects."""
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        parts = []
        for item in content:
            if isinstance(item, dict):
                if "text" in item:
                    parts.append(item["text"])
                elif "code" in item:
                    parts.append(f"```\n{item['code']}\n```")
                elif "result" in item:
                    parts.append(f"```\n{item['result']}\n```")
                else:
                    parts.append(json.dumps(item, indent=2))
            else:
                parts.append(str(item))
        return "\n\n".join(p.strip() for p in parts if p.strip())
    return str(content)

def export_session(path: Path) -> Optional[str]:
    """Export one Gemini session file."""
    session_id = path.stem
    # Use the full path as a unique key
    entries, info = parse_gemini_jsonl(path)
    if not entries: return None

    kind = info.get("kind", "session")
    start = info.get("startTime", "")
    last = info.get("lastUpdated", "")
    title = entries[0].get("content", "") if entries else "Gemini Session"
    if isinstance(title, list):
        for item in title:
            if isinstance(item, dict) and "text" in item:
                title = item["text"]
                break
    if isinstance(title, str):
        title = title.strip()[:80]

    # Format conversation
    conv_parts = []
    for entry in entries:
        etype = entry.get("type", "?")
        ts = entry.get("timestamp", "")
        content = format_content(entry.get("content", ""))
        thoughts = entry.get("thoughts", [])
        display = entry.get("displayContent", [])
        emoji = "👤" if etype == "user" else "🤖" if etype == "gemini" else "🔧"
        label = "User" if etype == "user" else "Gemini" if etype == "gemini" else etype.capitalize()

        lines = [f"### {emoji} {label} *({ts})*"]
        if display:
            dtext = format_content(display)
            if dtext: lines.append(dtext + "\n")
        if content and etype != "user":
            lines.append(content)
        elif content and etype == "user":
            # Clean up hook_context and loaded_context noise
            clean = re.sub(r'<hook_context>.*?</hook_context>', '', content, flags=re.DOTALL)
            clean = re.sub(r'<loaded_context>.*?</loaded_context>', '', clean, flags=re.DOTALL)
            clean = re.sub(r'<extension_context>.*?</extension_context>', '', clean, flags=re.DOTALL)
            clean = re.sub(r'---.*?---', '', clean)
            clean = clean.strip()
            if clean: lines.append(clean)
        thought_text = format_thoughts(thoughts)
        if thought_text: lines.append(thought_text)
        conv_parts.append("\n\n".join(lines))

    conversation = "\n\n---\n\n".join(conv_parts)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    export = f"""# Gemini Chat Export — {title}

**Exported**: {now}
**Session**: `{session_id}` | **Kind**: {kind}
**Started**: {start}
**Last Updated**: {last}

---

{conversation}
"""

    safe = re.sub(r'[^a-zA-Z0-9 _-]', '_', title)[:80].strip()
    ts_pfx = ""
    if start:
        try:
            dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
            ts_pfx = dt.strftime("%Y%m%d_%H%M%S_")
        except: pass
    fname = f"{ts_pfx}{session_id}_{safe}.md"
    (OUTPUT_DIR / fname).write_text(export)
    return str(path.absolute())

def main():
    p = argparse.ArgumentParser(description="Export Gemini sessions to markdown.")
    p.add_argument("--all", action="store_true", help="All unexported sessions")
    p.add_argument("--force", action="store_true", help="Re-export all")
    args = p.parse_args()

    if not GEMINI_DIR.exists():
        print(f"❌ Not found: {GEMINI_DIR}")
        sys.exit(1)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    exported = load_tracking()
    # Find all JSONL files
    files = sorted(GEMINI_DIR.rglob("*.jsonl"), key=lambda f: f.stat().st_mtime, reverse=True)
    if not files:
        print("📭 No Gemini sessions found.")
        return

    ok, skip = 0, 0
    for f in files:
        key = str(f.absolute())
        if not args.force and key in exported:
            skip += 1
            continue
        r = export_session(f)
        if r:
            exported.add(r)
            ok += 1
            print(f"  ✅ {f.name}")
        else:
            skip += 1

    save_tracking(exported)
    print(f"\n📊 Gemini: {ok} exported, {skip} skipped")
    print(f"📍 {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
