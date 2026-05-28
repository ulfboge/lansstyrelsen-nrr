# Datamodell – NRR Södermanland 2026–2027

> Dokumenterar Feature Service-schemat för fältdatainsamling via ArcGIS Survey123/Field Maps,
> synkroniserat mot `data/templates/assessment_template_sodermanland.csv` och ESRI File GDB.

---

## 1. Arkitektur

```
FÄLT                           ENTERPRISE PORTAL                ANALYS / LEVERANS
────────────────────           ─────────────────────────        ──────────────────────────
Survey123 (formulär)    ──┐
                           ├──▶  Feature Service             ──▶  ArcGIS Pro (analys)
Field Maps (karta/GPS)  ──┘      habitatbedomning_falt            ArcGIS Online (webkarta)
                                 + Attachments (foton)            ArcGIS Dashboard
                                 (ESRI Enterprise GDB)            Export → CSV / GDB / WFS
```

All fältdata synkar automatiskt. ArcGIS Pro ansluter direkt mot Feature Servicen –
ingen manuell import krävs.

---

## 2. Feature Service-schema

**Tabellnamn:** `habitatbedomning_falt`  
**Projektion:** SWEREF 99 TM (EPSG:3006)  
**Geometrityp:** Polygon (primär) och Punkt  
**Attachments:** Aktiverade (foton och dokument)

| Fält | Typ | Längd | Domän | Motsvarighet i CSV-mall |
|------|-----|-------|-------|------------------------|
| `site_code` | Text | 20 | – | `site_code` |
| `habitat_code` | Text | 10 | `d_habitat` | `habitat_code` |
| `assessment_unit_id` | Text | 30 | – | `assessment_unit_id` |
| `estimated_area_ha` | Double | – | – | `estimated_area_ha` |
| `condition_class` | Text | 20 | `d_condition` | `condition_class` |
| `geometry_confidence` | Text | 10 | `d_confidence` | `geometry_confidence` |
| `habitat_confidence` | Text | 10 | `d_confidence` | `habitat_confidence` |
| `condition_confidence` | Text | 10 | `d_confidence` | `condition_confidence` |
| `data_currency` | Text | 50 | – | `data_currency` |
| `field_verification_need` | Text | 5 | `d_yesno` | `field_verification_need` |
| `data_sources` | Text | 500 | – | `data_sources` |
| `last_field_visit` | Date | – | – | `last_field_visit` |
| `assessor` | Text | 100 | – | `assessor` |
| `motivation` | Text | 2000 | – | `motivation` |
| `main_uncertainty` | Text | 1000 | – | `main_uncertainty` |
| `proposed_action` | Text | 1000 | – | `proposed_action` |
| `next_review_date` | Date | – | – | `next_review_date` |
| `Shape` | Polygon | – | – | *(geometry)* |

> `assessment_unit_id` format: `{site_code}_{löpnummer}`, t.ex. `SE0230201_003`.
> Samma Natura 2000-område kan ha flera bedömningsenheter (habitatfläckar).

---

## 3. Domänvärden

### d_condition – Tillståndsklass
| Värde | Beskrivning |
|-------|-------------|
| `gott` | Gott tillstånd |
| `icke_gott` | Icke gott tillstånd |
| `okant` | Okänt tillstånd |

### d_confidence – Osäkerhetsnivå
| Värde | Beskrivning |
|-------|-------------|
| `hog` | Hög säkerhet |
| `medel` | Medel säkerhet |
| `lag` | Låg säkerhet |

### d_yesno
| Värde | Beskrivning |
|-------|-------------|
| `ja` | Ja |
| `nej` | Nej |

### d_habitat – Vanliga EU Annex I-habitattyper i Södermanland (urval)
| Kod | Habitattyp |
|-----|-----------|
| `6210` | Kalkgräsmarker |
| `6270` | Fennoskandiska låglandsängar |
| `7140` | Rikkärr |
| `7230` | Alkaliska kärr |
| `9010` | Västlig taiga |
| `9050` | Örtrika barrskogar |
| `9060` | Barrskogar på isälvsavlagringar |
| `9080` | Lövsumpskogar |
| `91D0` | Skogbevuxen myr |
| `91E0` | Alluviala lövskogar |

*(Komplettera med alla Annex I-typer som förekommer i länet efter genomgång av befintliga karteringar)*

---

## 4. Survey123-formulär – fältmappning

Survey123 Connect kopplas mot Feature Servicen ovan via XLSForm.
Fältarbetaren fyller i formuläret i appen; GPS-koordinater och foton bifogas automatiskt.

| Formulärfält (Survey123) | Typ | Mappar mot Feature Service-fält |
|--------------------------|-----|----------------------------------|
| Natura 2000-ID | `select_one` (lista) | `site_code` |
| Habitattyp | `select_one` (d_habitat) | `habitat_code` |
| Bedömningsenhet (auto) | `calculate` | `assessment_unit_id` |
| Uppskattad areal (ha) | `decimal` | `estimated_area_ha` |
| Tillståndsklass | `select_one` (d_condition) | `condition_class` |
| Säkerhet – geometri | `select_one` (d_confidence) | `geometry_confidence` |
| Säkerhet – habitat | `select_one` (d_confidence) | `habitat_confidence` |
| Säkerhet – tillstånd | `select_one` (d_confidence) | `condition_confidence` |
| Datakällor | `text` | `data_sources` |
| Fältbesök behövs? | `select_one` (d_yesno) | `field_verification_need` |
| Motivering | `text` (lång) | `motivation` |
| Huvudsaklig osäkerhet | `text` (lång) | `main_uncertainty` |
| Föreslagen åtgärd | `text` (lång) | `proposed_action` |
| Nästa granskning | `date` | `next_review_date` |
| Foto | `image` | Attachment |
| GPS-polygon | `geoshape` | `Shape` |

Inventerar namn (`assessor`) och datum (`last_field_visit`) sätts automatiskt
från Survey123-inloggning och enhetens klocka.

---

## 5. Relation till övriga filer i projektet

| Fil | Relation |
|-----|----------|
| `data/templates/assessment_template_sodermanland.csv` | Samma fältstruktur – används för skrivbordsbedömningar och import |
| `data/sources_sodermanland.csv` | Datakälleregister – fylls i `data_sources`-fältet vid bedömning |
| `scripts/etl/fetch_natura2000.py` | Hämtar Natura 2000-polygoner som referenslager i Field Maps |
| `docs/planner_struktur.md` | Planeringsstruktur för Planner vid tjänststart |

---

## 6. Uppstart – checklista (dag 1–2)

- [ ] Be GIS-enheten skapa Feature Service `habitatbedomning_falt` i Enterprise Portal
- [ ] Importera domäner och attributschema (se ovan)
- [ ] Aktivera Attachments på lagret
- [ ] Installera Survey123 Connect på laptop → bygg XLSForm
- [ ] Skapa webbkarta i Portal: N2000-polygoner som ref. + `habitatbedomning_falt` redigerbart
- [ ] Testa offline-insamling innan första fältdag
- [ ] I ArcGIS Pro: **Add Data → Feature Service URL** → live-anslutning klar

---

*Senast uppdaterad: 2026-05-28*
