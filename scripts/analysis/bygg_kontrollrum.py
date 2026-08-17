# -*- coding: utf-8 -*-
"""Bygger docs/nnk/kontrollrum_nnk_2026.html och docs/nnk/runbook_nnk_2026.md ur uppgifter.py."""
import json
import datetime
from pathlib import Path

import uppgifter as U

REPO = Path(__file__).resolve().parents[2]
NNK_DOCS = REPO / "docs" / "nnk"

# --- veckor -> datum (ISO-veckor 2026) ---
def mandag(v):
    return datetime.date.fromisocalendar(2026, v, 1)

VECKOR = list(range(34, 53))
ANSVAR = {"H": "Handläggare", "K": "Kollega", "HK": "Båda"}

data = {
    "paket": {k: {"namn": v[0], "veckor": v[1]} for k, v in U.PAKET.items()},
    "veckor": [{"v": v, "datum": mandag(v).isoformat(),
                "manad": mandag(v).strftime("%b")} for v in VECKOR],
    "milstolpar": [{"id": m[0], "v": m[1], "text": m[2], "datum": m[3]}
                   for m in U.MILSTOLPAR],
    "leveranser": [{"id": l[0], "text": l[1], "paket": l[2], "v": l[3],
                    "mottagare": l[4]} for l in U.LEVERANSER],
    "uppgifter": [{"id": u[0], "rubrik": u[1], "paket": u[2], "v1": u[3],
                   "v2": u[4], "ansvar": u[5], "leverans": u[6],
                   "dep": u[7], "steg": u[8]} for u in U.U],
    "checklista": U.CHECKLISTA_INCHECKNING,
    "avgransningar": [{"vad": a[0], "detalj": a[1], "kalla": a[2]}
                      for a in U.AVGRANSNINGAR],
}

# ------------------------------------------------------------------ runbook
def runbook():
    r = []
    a = r.append
    a("# Runbook NNK/NRF 2026 — steg för steg\n")
    a("## Länsstyrelsen i Södermanlands län · Naturskyddsenheten · ref. 2451-2026\n")
    a("**Datum:** 2026-08-17  ")
    a(f"**Omfattning:** {len(U.U)} uppgifter i åtta arbetspaket, "
      f"{sum(len(u[8]) for u in U.U)} konkreta steg  ")
    a("**Hör ihop med:** `docs/nnk/arbetsplan_nnk_2026.md` (varför) · "
      "`docs/nnk/kontrollrum_nnk_2026.html` (överblick och avbockning) · "
      "`docs/nnk/metodik_forvaltarkunskap.md` (förvaltardialogen)\n")
    a("---\n")
    a("## Så används dokumentet\n")
    a("Arbetsplanen säger *varför* och *när*. Det här dokumentet säger *hur*. "
      "Varje uppgift har ett id som matchar kontrollrummet och arbetsplanen, "
      "och stegen är skrivna för att gå att följa rakt av.\n")
    a("Uppgifter markerade **[Handläggare]**, **[Kollega]** eller **[Båda]** "
      "följer rollfördelningen i arbetsplanens avsnitt 6.1.\n")
    a("---\n")

    for p, (namn, veckor) in U.PAKET.items():
        ups = [u for u in U.U if u[2] == p]
        a(f"## {p}. {namn}\n")
        a(f"*{veckor} · {len(ups)} uppgifter*\n")
        for u in ups:
            uid, rub, _, v1, v2, ans, lev, dep, steg = u
            vtxt = f"v{v1}" if v1 == v2 else f"v{v1}–v{v2}"
            a(f"### {uid} · {rub}\n")
            meta = [f"**{vtxt}**", f"**[{ANSVAR[ans]}]**"]
            if dep:
                meta.append("förutsätter " + ", ".join(dep))
            if lev:
                lt = next(x[1] for x in U.LEVERANSER if x[0] == lev)
                meta.append(f"bidrar till *{lt}*")
            a(" · ".join(meta) + "\n")
            for i, s in enumerate(steg, 1):
                a(f"{i}. {s}")
            a("")
        a("---\n")

    a("## Checklista före incheckning i NNK\n")
    a("Gäller varje gång ett område checkas in. Från handledningen avsnitt 2.3 och 3.3.\n")
    for c in U.CHECKLISTA_INCHECKNING:
        a(f"- [ ] {c}")
    a("")
    a("---\n")
    a("## Vad som medvetet inte görs 2026\n")
    a("| Avgränsning | Innebörd | Stöd |")
    a("|---|---|---|")
    for v, d, k in U.AVGRANSNINGAR:
        a(f"| {v} | {d} | {k} |")
    a("")
    a("---\n")
    a("## Milstolpar\n")
    a("| # | Vecka | Datum | Milstolpe |")
    a("|---|---|---|---|")
    for m in U.MILSTOLPAR:
        a(f"| {m[0]} | v{m[1]} | {m[3]} | {m[2]} |")
    a("")
    a("---\n")
    a("## Leveranser\n")
    a("| # | Leverans | Paket | Klart | Mottagare |")
    a("|---|---|---|---|---|")
    for l in U.LEVERANSER:
        a(f"| {l[0]} | {l[1]} | {l[2]} | v{l[3]} | {l[4]} |")
    a("")
    a("---\n")
    a("*Runbook v1.0 · 2026-08-17 · genererad ur "
      "`scripts/analysis/uppgifter.py` med `bygg_kontrollrum.py`*")
    return "\n".join(r)


with open(NNK_DOCS / "runbook_nnk_2026.md", "w", encoding="utf-8") as f:
    f.write(runbook())

payload = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
with open(Path(__file__).with_name("kontrollrum_data.json"), "w", encoding="utf-8") as f:
    f.write(payload)

mall = Path(__file__).with_name("kontrollrum_mall.html").read_text(encoding="utf-8")
html = mall.replace("/*DATA*/{}/*END*/", "/*DATA*/" + payload + "/*END*/")
(NNK_DOCS / "kontrollrum_nnk_2026.html").write_text(html, encoding="utf-8")

print(f"{NNK_DOCS / 'runbook_nnk_2026.md'}: {len(U.U)} uppgifter, "
      f"{sum(len(u[8]) for u in U.U)} steg")
print(f"{NNK_DOCS / 'kontrollrum_nnk_2026.html'} skriven")
print("kontrollrum_data.json skriven")
