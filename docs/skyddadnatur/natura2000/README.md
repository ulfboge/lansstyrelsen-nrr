# Bevarandeplaner – Natura 2000 Södermanlands län

Lokalt arkiv av de dokument som är kopplade till Natura 2000-områden i kartverktyget [Skyddad natur](https://skyddadnatur.naturvardsverket.se/).

Hämtat **2026-08-21** via Naturvårdsverkets öppna REST-API (samma källa som kartverktyget):

- Områden: `https://geodata.naturvardsverket.se/n2000/rest/v3/omrade?lan=D`
- Dokumentlista: `…/omrade/{SITECODE}/dokument`
- Fil: `https://geodata.naturvardsverket.se/handlingar/rest/dokument/{id}`

## Innehåll

| | Antal |
|--|------:|
| Natura 2000-områden i D-län | 199 |
| Nedladdade dokument | 197 |
| Dokumenttyp | Bevarandeplan (PDF) |
| Områden utan dokument i Skyddad natur | 2 |
| Total storlek | ca 802 MB |

PDF:erna ligger i `dokument/` (ignoreras av Git p.g.a. storlek). Indexet är versionshanterat:

- `index.csv` — en rad per område/dokument, öppnas i Excel
- `index.json` — samma innehåll plus metadata

## Områden utan dokument

Dessa två SPA-områden (fågeldirektivet) saknar uppladdat dokument i NV:s handlingstjänst:

| SITECODE | Namn | Typ | Areal (ha) |
|----------|------|-----|-----------:|
| SE0220704 | Risskären | SPA | 1 368 |
| SE0220706 | Hävringe skärgård | SPA | 24 285 |

## Uppdatera arkivet

```powershell
python scripts/etl/fetch_skyddadnatur_dokument.py
```

Skriptet hoppar över filer som redan finns. Kör om det när bevarandeplaner revideras.

## Licens och källa

Offentliga handlingar från Länsstyrelsen i Södermanlands län, publicerade av Naturvårdsverket via Skyddad natur. Ange källan vid vidare användning.
