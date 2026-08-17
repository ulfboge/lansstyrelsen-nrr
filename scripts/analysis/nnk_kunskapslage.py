"""
Kunskapslage NNK - Sodermanlands lan (D)
========================================
Beraknar nollmatning av kunskapslaget for livsmiljotyper inom Natura 2000
utifran NNK-statistikuttaget fran Naturvardsverket, samt prioriteringsklasser
P1-P4 enligt FAQ fraga 11 (havdberoende forst, darefter liten utbredning).

Indata : docs/underlag/D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx, flik "2. N2000_NNK"
Utdata : data/nnk/nnk_d.json  - summering, objekt med tier/score, areal per naturtypskod

Kor om skriptet mot ett nytt NNK-uttag for att uppdatera nollmatningen.
Beroenden: openpyxl

    python scripts/analysis/nnk_kunskapslage.py
"""
import os
import json
import collections

import openpyxl

HAR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HAR, "..", ".."))
SRC = os.path.join(REPO, "docs", "underlag",
                   "D_NNK_statistik_per_N2000_NP_NR_per_260120.xlsx")
UT = os.path.join(REPO, "data", "nnk", "nnk_d.json")

# Kategorier som raknas som terrestra (marina och limniska hanteras separat,
# se FAQ fraga 16 och 29 - de ska inte prioriteras under 2026).
TERRESTRA = {"Skog", "Grasmark", "Gräsmark", "Vatmark", "Våtmark",
             "Berg", "Strander", "Stränder", "Dyner"}

# Havdberoende livsmiljotyper - hogsta prioritet enligt FAQ fraga 11
# ("livsmiljotyper som ar i behov av lopande atgarder").
HAVDBEROENDE = {
    "1630", "1631",                                     # havsstrandangar
    "5130", "5133",                                     # enbuskmarker
    "6110", "6210", "6230", "6270", "6280",             # torrangar, silikatgrasmark
    "6410", "6412", "6430", "6510", "6520",             # fuktangar, hoglorta angar
    "8230", "8231", "8232",                             # hallmarkstorrang
    "9070", "9071", "9072",                             # tradklada betesmarker
}

# Marina koder undantas fran "sallsynt"-analysen - de hanteras av nationell
# marin kartering, inte av lansstyrelsen (FAQ fraga 16).
MARINA = {"1110", "1130", "1140", "1150", "1152", "1160", "1170", "1174"}

SALLSYNT_GRANS_HA = 50.0


def num(v):
    """Returnera tal, annars 0.0 (cellerna innehaller tomma strangar och None)."""
    return float(v) if isinstance(v, (int, float)) else 0.0


def las_kolumner(cat_rad, kod_rad, hdr_rad):
    """Kartlagg arealkolumnerna (fran index 25) till (kategori, kod).

    Kategorin star bara pa forsta kolumnen i varje grupp och maste
    framatfyllas. For flaggkolumnerna (Osaker/Obestamd/Icke-natura) ligger
    kategorin i kod-raden i stallet for kategori-raden.
    """
    kolumner = {}
    senaste = None
    for j in range(25, len(hdr_rad)):
        if hdr_rad[j] is None:
            continue
        kod = str(hdr_rad[j]).strip()
        kategori = cat_rad[j]
        if not kategori and kod_rad[j] and not str(kod_rad[j]).strip().isdigit():
            kategori = kod_rad[j]
        if kategori:
            senaste = str(kategori).strip()
        kolumner[j] = (senaste, kod)
    return kolumner


def las_objekt():
    wb = openpyxl.load_workbook(SRC, read_only=True, data_only=True)
    ws = wb["2. N2000_NNK"]
    rader = list(ws.iter_rows(values_only=True))
    cat, kod, hdr = rader[0], rader[1], rader[2]
    kolumner = las_kolumner(cat, kod, hdr)
    data = [r for r in rader[3:] if r[0] == "D"]

    objekt = []
    for r in data:
        o = {
            "sitecode": r[1],
            "namn": str(r[2]).strip(),
            "skyddat": num(r[3]),
            "kart_natura": num(r[4]),
            "karterat": num(r[5]),
            "okarterat": max(0.0, num(r[6])),
            # Antal polygoner per naturtypsstatus
            "n_fullgod": int(num(r[7])),
            "n_ickefullgod": int(num(r[8])),
            "n_utveckl": int(num(r[9])),
            "n_ovrigt": int(num(r[10])),
            "n_ejbedomd": int(num(r[11])),
            "n_statussaknas": int(num(r[12])),
            # Antal polygoner per karteringsstatus
            "n_ejgranskad": int(num(r[13])),
            "n_skrivbord": int(num(r[14])),
            "n_falt_besok": int(num(r[15])),
            "n_falt_inv": int(num(r[16])),
            "n_atgardas": int(num(r[17])),
            # Ursprung
            "bidos": int(num(r[19])) + int(num(r[21])) + int(num(r[23])),
            "nnk": int(num(r[20])),
            "bidos_nnk": int(num(r[22])),
        }

        arealer = collections.Counter()
        per_kod = collections.Counter()
        for j, (kategori, k) in kolumner.items():
            v = num(r[j])
            if v <= 0:
                continue
            if k in ("Obestamd natura-naturtyp", "Obestämd natura-naturtyp",
                     "Osaker natura-/ icke-natura", "Osäker natura-/ icke-natura",
                     "Icke-natura-naturtyp"):
                arealer[("flagga", kategori or "Ovrigt", k)] += v
            else:
                arealer[("kod", kategori, k)] += v
                per_kod[k] += v

        def summa(typ, *, kategorier=None, flagga=None):
            return sum(v for (t, c, k), v in arealer.items()
                       if t == typ
                       and (kategorier is None or c in kategorier)
                       and (flagga is None or k.startswith(flagga)))

        o["terr_natura"] = summa("kod", kategorier=TERRESTRA)
        o["limn_natura"] = summa("kod", kategorier={"Limnisk", "Limniska"})
        o["marin_natura"] = summa("kod", kategorier={"Marin"})
        o["skog"] = summa("kod", kategorier={"Skog"})
        o["grasmark"] = summa("kod", kategorier={"Grasmark", "Gräsmark"})
        o["vatmark"] = summa("kod", kategorier={"Vatmark", "Våtmark"})
        o["osaker_terr"] = summa("flagga", kategorier=TERRESTRA, flagga="Os")
        o["obestamd_terr"] = summa("flagga", kategorier=TERRESTRA, flagga="Ob")
        o["osaker_marin"] = summa("flagga", kategorier={"Marin"}, flagga="Os")
        o["havd"] = sum(v for k, v in per_kod.items() if k in HAVDBEROENDE)
        o["koder"] = dict(per_kod)
        objekt.append(o)
    return objekt


def prioritera(objekt):
    """Satt sallsynthet, andel bedomd, score och prioritetsklass P1-P4."""
    lansareal = collections.Counter()
    for o in objekt:
        for k, v in o["koder"].items():
            lansareal[k] += v
    sallsynt = {k: v for k, v in lansareal.items()
                if v < SALLSYNT_GRANS_HA and k not in MARINA}

    for o in objekt:
        o["sallsynt_ha"] = sum(v for k, v in o["koder"].items() if k in sallsynt)
        o["sallsynt_koder"] = sorted(k for k in o["koder"] if k in sallsynt)
        n_pol = (o["n_fullgod"] + o["n_ickefullgod"] + o["n_utveckl"]
                 + o["n_ovrigt"] + o["n_ejbedomd"] + o["n_statussaknas"])
        o["n_pol"] = n_pol
        o["andel_bedomd"] = ((o["n_fullgod"] + o["n_ickefullgod"]) / n_pol
                             if n_pol else 0.0)
        o["faltdata"] = o["n_falt_besok"] + o["n_falt_inv"]
        o["score"] = (
            o["havd"] * 3.0                                  # FAQ f11: havdberoende
            + o["sallsynt_ha"] * 4.0                         # FAQ f11: liten utbredning
            + (o["osaker_terr"] + o["obestamd_terr"]) * 1.5  # utbredningsosakerhet
            + (o["terr_natura"] - o["havd"]) * 0.5           # ovrig terrester areal
            + (30 if o["faltdata"] == 0 and o["terr_natura"] > 5 else 0)
        )

        if o["havd"] >= 20 or o["sallsynt_ha"] >= 5:
            o["tier"] = "P1"
        elif o["terr_natura"] >= 20 or (o["osaker_terr"] + o["obestamd_terr"]) >= 5:
            o["tier"] = "P2"
        elif o["terr_natura"] > 0:
            o["tier"] = "P3"
        else:
            o["tier"] = "P4"
    return dict(lansareal), sallsynt


def summera(objekt):
    nycklar = ["skyddat", "karterat", "okarterat", "kart_natura", "terr_natura",
               "limn_natura", "marin_natura", "havd", "skog", "grasmark",
               "vatmark", "osaker_terr", "obestamd_terr", "osaker_marin",
               "n_fullgod", "n_ickefullgod", "n_utveckl", "n_ovrigt",
               "n_ejbedomd", "n_statussaknas", "n_ejgranskad", "n_skrivbord",
               "n_falt_besok", "n_falt_inv", "n_atgardas",
               "bidos", "nnk", "bidos_nnk", "n_pol"]
    s = {"antal_objekt": len(objekt)}
    s.update({k: sum(o[k] for o in objekt) for k in nycklar})
    return s


def main():
    objekt = las_objekt()
    per_kod, sallsynt = prioritera(objekt)
    s = summera(objekt)

    print(f"Natura 2000-omraden (SCI/SAC) i D-lan : {s['antal_objekt']}")
    print(f"Totalt skyddat                        : {s['skyddat']:>10.0f} ha")
    print(f"Karterat i NNK                        : {s['karterat']:>10.0f} ha")
    print(f"Okarterat                             : {s['okarterat']:>10.0f} ha")
    print(f"Karterat som livsmiljotyp             : {s['kart_natura']:>10.0f} ha")
    print(f"  varav terrestert                    : {s['terr_natura']:>10.0f} ha")
    print(f"  varav havdberoende                  : {s['havd']:>10.0f} ha")
    print(f"Osaker naturtyp, terrestert           : {s['osaker_terr']:>10.0f} ha")
    print(f"Osaker naturtyp, marint                : {s['osaker_marin']:>10.0f} ha")
    andel = 100 * s["n_ejbedomd"] / s["n_pol"]
    print(f"Polygoner utan tillstandsbedomning    : {s['n_ejbedomd']} av "
          f"{s['n_pol']} ({andel:.1f} %)")
    print(f"Polygoner med ursprung BIDOS          : {s['bidos']}")

    for tier in ("P1", "P2", "P3", "P4"):
        g = [o for o in objekt if o["tier"] == tier]
        print(f"\n{tier}: {len(g):3} objekt | terrester {sum(o['terr_natura'] for o in g):8.0f} ha"
              f" | havdberoende {sum(o['havd'] for o in g):7.0f} ha"
              f" | {sum(o['n_pol'] for o in g):5} polygoner")

    print("\nSallsynta livsmiljotyper i lanet (< 50 ha inom N2000):")
    for k, v in sorted(sallsynt.items(), key=lambda x: x[1]):
        print(f"  {k:6} {v:8.2f} ha")

    with open(UT, "w", encoding="utf-8") as fh:
        json.dump({"summering": s, "objekt": objekt,
                   "per_kod": per_kod, "sallsynt": sallsynt},
                  fh, ensure_ascii=False)
    print(f"\nSkrev {UT}")


if __name__ == "__main__":
    main()
