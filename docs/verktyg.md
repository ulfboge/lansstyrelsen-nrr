# Analysverktyg – Natura 2000 pipeline

Dokumentation av det befintliga analysverktyget i `C:\Users\galag\GitHub\natura-2000`.
Pipelines körs **från det repot** men skripten refereras och dokumenteras här.

## Repostruktur

| Repo | URL | Roll |
|------|-----|------|
| **lansstyrelsen-nrr** | [github.com/ulfboge/lansstyrelsen-nrr](https://github.com/ulfboge/lansstyrelsen-nrr) | Publik projektyta (denna dokumentation + [GitHub Pages](https://ulfboge.github.io/lansstyrelsen-nrr)) |
| **nnk-granskning-2026** | [github.com/ulfboge/nnk-granskning-2026](https://github.com/ulfboge/nnk-granskning-2026) | Publikt — NNK-granskning 2026 ([kontrollpanel](https://ulfboge.github.io/nnk-granskning-2026)) |
| **natura-2000** | [github.com/ulfboge/natura-2000](https://github.com/ulfboge/natura-2000) | Privat arbetsrepo — pipeline, Origo, ArcGIS Pro, rådata, NV-underlag |

Kör all pipeline-kod och NNK-analys i **natura-2000**. Arbetsdokument och kontrollpanel publiceras i **nnk-granskning-2026**.
Lägg inte preliminär NRF-bedömning, rådata eller NV-underlag i något publikt repo.

**Åtkomst:** du äger `natura-2000` som GitHub-användaren `ulfboge`. Kollegor bjuds in under repots Settings → Collaborators.

---

## Snabbstart

```powershell
cd C:\Users\galag\GitHub\natura-2000
.venv\Scripts\Activate.ps1

# Kör hela pipeline (hoppar över manuella källor)
.\run_all.ps1 -SkipManual

# Eller steg för steg:
python scripts/01_fetch_official_data.py
python scripts/02_prepare_layers.py
python scripts/03_priority_analysis.py
python scripts/04_subset_sodermanland.py
python scripts/05_join_summary_to_layers.py
python scripts/10_export_for_arcgis.py
python scripts/11_county_overview.py
```

---

## Pipeline – steg för steg

| Steg | Skript | Vad det gör |
|------|--------|-------------|
| 1 | `01_fetch_official_data.py` | Laddar ned aktiverade källor från `sources_sodermanland.csv` (NV, etc.) |
| 1b | `01b_fetch_manual_sources.py` | Öppnar webbläsare för manuella källor (VMI, TUVA, VISS) |
| 2 | `02_prepare_layers.py` | Harmoniserar alla lager → `sodermanland_n2000_base.gpkg` (EPSG:3006) |
| 3 | `03_priority_analysis.py` | **Prioritetsanalys** – beräknar area per habitat/objekt, sätter prioritetsklass A/B/C |
| 4 | `04_subset_sodermanland.py` | Extraherar enbart Södermanlands geometrier |
| 5 | `05_join_summary_to_layers.py` | Kopplar prioritets-/statussummering till geometrilager |
| 6 | `06_qgis_package_export.py` | Exporterar QGIS-leveranspaket (GPKG + CSV) |
| 10 | `10_export_for_arcgis.py` | Exporterar ArcGIS Pro-paket (`.gdb`, `.lyrx`, `.aprx`) |
| 11 | `11_county_overview.py` | Länsöversikt: ha per status + per habitatkodserie |

---

## Datakällor (`sources_sodermanland.csv`)

Styrs via `data/sources_sodermanland.csv` – sätt `enabled=1` för att aktivera en källa.

| Källa | Typ | Status | Kommentar |
|-------|-----|--------|-----------|
| `n2000_sites_sci` | Natura 2000 SCI (rikstäckande) | Automatisk | NV nedladdning |
| `n2000_sites_spa` | Natura 2000 SPA (rikstäckande) | Automatisk | NV nedladdning |
| `habitat_map_d` | Naturtypskartan Södermanland (länskod D) | Automatisk | Primär habitatkälla |
| `habitat_map_riks` | Naturtypskartan riks | Valfri (disabled) | Stor fil |
| `vmi` | Våtmarksinventeringen | Manuell | Kräver manuellt val i katalog |
| `tuva` | TUVA – ängs- och betesmarker | Manuell | Jordbruksverket export |
| `viss` | VISS vattenförekomster | Manuell | API-anrop eller export |

---

## Prioritetsanalys – vad som behöver uppdateras

Steg 3 (`03_priority_analysis.py`) beräknar prioritetsklass (A/B/C) och preliminär
bevarandestatus (`gott` / `inte_gott` / `okant`) med en viktad formel:

```
priority_total = 0.30 × naturvärde
              + 0.25 × tryckscore
              + 0.20 × restaureringspotential
              + 0.15 × genomförbarhet
              + 0.10 × synergi
```

### Nuläge: alla defaultvärden = 3 (medelnivå)

Följande variabler är satta till standardvärde `3` och **måste ersättas med verklig information**:

| Variabel | Defaultvärde | Datakälla för verkliga värden |
|----------|-------------|-------------------------------|
| `pressure_score` | 3 | Fältinventering, NV tryckövervakning, HELCOM/EEA |
| `restoration_potential_score` | 3 | Fältinventering, historiska kartor, expertkonsultation |
| `feasibility_score` | 3 | Markägardialoger, ekonomisk analys |
| `synergy_score` | 3 | Korsanalys med gröna infrastrukturen, LONA-projekt |

`nature_value_score` beräknas automatiskt från habitatarea (relativ, 1–5) – den är korrekt.

### Hur man uppdaterar

1. Kör pipeline steg 1–2 för att hämta och förbereda geodata
2. Öppna `data/templates/assessment_template_sodermanland.csv` (se nedan)
3. Fyll i `condition_class`, `proposed_action`, bedömare och motivering per objekt
4. Exportera trycksdata från NV/EEA och uppdatera `pressure_score` per habitattyp
5. Kör om steg 3–11 efter att variablerna uppdaterats i skriptet

---

## Bedömningsmall

`data/templates/assessment_template_sodermanland.csv` innehåller en rad per
habitat × objekt med fält för:

- `condition_class` – preliminär status (`gott` / `inte_gott` / `okant`)
- `field_verification_need` – markera `ja` om fältkontroll krävs
- `assessor` / `assessment_date` – spårbarhet
- `motivation` – fritext
- `proposed_action` – åtgärdsförslag
- `next_review_date` – datum för nästa bedömning

**Fyll i denna mall efter fältinventering** och skicka tillbaka till steg 3
för att beräkna realistisk prioritet.

---

## Leveranser

| Format | Innehåll | Plats |
|--------|----------|-------|
| ArcGIS Pro | `.aprx` (Git), `.lyrx`, GDB/shapefiles (lokal export) | `deliveries/arcgis_LATEST.txt` → `NRF_Sodermanland_N2000.aprx` |
| QGIS | GPKG + CSV | `deliveries/qgis_*` |
| Webbkarta | GeoJSON + Origo-config | `web/public/` |
| Statistik | CSV-tabeller | `data/outputs/` |

---

## Kända begränsningar

| Ämne | Detalj |
|------|--------|
| Preliminär status | `gott/inte_gott/okant` är pipeline-heuristik, **inte** NV officiellt bevarandetillstånd |
| GDAL-GDB | Använd `sodermanland_n2000_pro.gdb` i ArcGIS Pro (inte den gamla GDAL-exporterade) |
| VISS/TUVA | Kräver manuell nedladdning – aktivera `enabled=1` i `sources_sodermanland.csv` |

---

*Se `docs/HANDOFF.md` i `natura-2000`-repot för senaste arbetsnotat.*
