#!/usr/bin/env python3
"""Phase 1: Metadaten von Claude-Skill-Repos ernten. Liest keine SKILL.md."""
import json, subprocess, time, sys, pathlib, itertools

OUT = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "skills.jsonl")
TOPICS = ["claude-skill", "claude-skills", "claude-code-skill",
          "claude-code-skills", "anthropic-skills"]
# Bänder unter 1000 Treffern; groessere werden nach Datum gesplittet.
BANDS = [">=100", "20..99", "5..19", "2..4", "1..1"]
DATE_SPLIT = ["<2026-04-01", "2026-04-01..2026-06-15", ">=2026-06-15"]

FIELDS = ("full_name", "description", "stargazers_count", "forks_count",
          "created_at", "pushed_at", "topics", "language", "archived", "fork")

def api(q, page):
    cmd = ["gh", "api", "-H", "Accept: application/vnd.github+json",
           f"search/repositories?q={q}&per_page=100&page={page}"]
    for versuch in range(4):
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            try: return json.loads(r.stdout)
            except Exception: pass
        time.sleep(6 * (versuch + 1))
    return None

def hole(q, sink, gesehen):
    neu = 0
    for page in range(1, 11):
        d = api(q, page)
        time.sleep(2.2)                      # 30 Suchen/min eingehalten
        if not d or "items" not in d: break
        for it in d["items"]:
            fn = it.get("full_name")
            if not fn or fn in gesehen: continue
            gesehen.add(fn)
            sink.write(json.dumps({k: it.get(k) for k in FIELDS}, ensure_ascii=False) + "\n")
            neu += 1
        if len(d["items"]) < 100: break
    return neu

gesehen = set()
with OUT.open("w", encoding="utf-8") as sink:
    for t in TOPICS:
        for band in BANDS:
            d = api(f"topic:{t}+stars:{band}", 1); time.sleep(2.2)
            gesamt = (d or {}).get("total_count", 0)
            if gesamt == 0: continue
            if gesamt <= 1000:
                n = hole(f"topic:{t}+stars:{band}", sink, gesehen)
                print(f"  {t:20} stars {band:8} {gesamt:5} → {n:4} neu", flush=True)
            else:
                for ds in DATE_SPLIT:
                    n = hole(f"topic:{t}+stars:{band}+created:{ds}", sink, gesehen)
                    print(f"  {t:20} stars {band:8} {ds:24} → {n:4} neu", flush=True)
        # Null-Stern-Band nur als Stichprobe (2 Seiten), zum Vergleich
        n = 0
        for page in (1, 2):
            d = api(f"topic:{t}+stars:0..0", page); time.sleep(2.2)
            for it in (d or {}).get("items", []):
                fn = it.get("full_name")
                if not fn or fn in gesehen: continue
                gesehen.add(fn)
                rec = {k: it.get(k) for k in FIELDS}; rec["_stichprobe_0stern"] = True
                sink.write(json.dumps(rec, ensure_ascii=False) + "\n"); n += 1
        print(f"  {t:20} stars 0 (Stichprobe)      → {n:4} neu", flush=True)

print(f"\nFertig: {len(gesehen)} eindeutige Repos in {OUT}")
