"""
Kopplar NNK-polygoner till skyddade omraden (SITECODE / NVRID)
==============================================================
Den publika Natura naturtypskartan saknar omradesidentitet - en polygon gar
inte att knyta till ett Natura 2000-omrade eller naturreservat. Det har
skriptet gor kopplingen med en overlappsbaserad spatial join, sa att NNK gar
att folja upp objektsvis.

Varje NNK-yta tilldelas det skyddade omrade den har storst arealoverlapp med.
Ytor som ligger helt utanfor far SITECODE = None. Andelen av ytan som ligger
inom omradet redovisas som andel_inom, sa att gransfall gar att granska.

Indata  : docs/underlag/naturtypskarta/NNK_YTA.shp  (publik NNK, lanskod D)
          SCI_Rikstackande.zip  (Naturvardsregistret, hamtas automatiskt)
Utdata  : data/nnk/nnk_yta_med_sitecode.gpkg  - NNK-ytor med SITECODE, omradesnamn, bevarandeplan
          data/nnk/nnk_yta_med_sitecode.csv   - samma tabell utan geometri

Beroenden: geopandas, requests
"""
import io
import os
import zipfile
import warnings

import geopandas as gpd
import pandas as pd
import requests

warnings.filterwarnings("ignore")

HAR = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HAR, "..", ".."))
NNK_SHP = os.environ.get(
    "NNK_SHP",
    os.path.join(REPO, "docs", "underlag", "naturtypskarta", "NNK_YTA.shp"))
SCI_URL = ("https://geodata.naturvardsverket.se/nedladdning/"
           "naturvardsregistret/SCI_Rikstackande.zip")
CACHE = os.environ.get(
    "NNK_CACHE",
    os.path.join(REPO, "data", "raw", "n2000"))
UT_GPKG = os.path.join(REPO, "data", "nnk", "nnk_yta_med_sitecode.gpkg")
UT_CSV = os.path.join(REPO, "data", "nnk", "nnk_yta_med_sitecode.csv")
LAN = "Söderman"          # matchar "Södermanlands län" i attributet LAN
MIN_ANDEL = 0.10          # minsta andel av ytan inom omradet for att kopplas


def hamta_sci():
    """Ladda ner och lasa in rikstackande SCI, eller anvanda cachat uttag."""
    os.makedirs(CACHE, exist_ok=True)
    shp = os.path.join(CACHE, "SCI_Rikstackande",
                       "SCI_ej_alvar_rikstackande",
                       "SCI_ej_alvar_rikstackande.shp")
    if not os.path.exists(shp):
        print("Hamtar SCI_Rikstackande fran Naturvardsregistret ...")
        r = requests.get(SCI_URL, timeout=600)
        r.raise_for_status()
        zipfile.ZipFile(io.BytesIO(r.content)).extractall(CACHE)
    return gpd.read_file(shp)


def main():
    print("Laser NNK_YTA ...")
    nnk = gpd.read_file(NNK_SHP)
    nnk = nnk.reset_index(drop=True)
    nnk["radid"] = nnk.index
    nnk["area_ha"] = nnk.geometry.area / 10000
    ogiltiga = int((~nnk.geometry.is_valid).sum())
    if ogiltiga:
        print(f"  {ogiltiga} ogiltiga geometrier - kor buffer(0)")
        nnk["geometry"] = nnk.geometry.buffer(0)
    print(f"  {len(nnk)} ytor, {nnk['area_ha'].sum():.0f} ha, CRS {nnk.crs}")

    sci = hamta_sci()
    d = sci[sci["LAN"].str.contains(LAN, na=False)].copy()
    d = d[["SITE_CODE", "NAMN", "BEVPLAN", "geometry"]].rename(
        columns={"SITE_CODE": "SITECODE", "NAMN": "OMRADE"})
    d["geometry"] = d.geometry.buffer(0)
    print(f"  {len(d)} Natura 2000-omraden (SCI/SAC) i lanet")

    print("Beraknar overlapp ...")
    snitt = gpd.overlay(nnk[["radid", "area_ha", "geometry"]], d,
                        how="intersection", keep_geom_type=True)
    snitt["overlapp_ha"] = snitt.geometry.area / 10000
    snitt["andel_inom"] = snitt["overlapp_ha"] / snitt["area_ha"]

    # Varje yta tilldelas omradet med storst overlapp
    basta = (snitt.sort_values("overlapp_ha", ascending=False)
                  .drop_duplicates("radid")
                  .loc[:, ["radid", "SITECODE", "OMRADE", "BEVPLAN",
                           "overlapp_ha", "andel_inom"]])
    basta = basta[basta["andel_inom"] >= MIN_ANDEL]

    # Ytor som skar flera omraden - vard att granska manuellt
    antal_omr = snitt[snitt["andel_inom"] >= MIN_ANDEL].groupby("radid").size()
    basta = basta.merge(antal_omr.rename("antal_omraden"),
                        left_on="radid", right_index=True, how="left")

    ut = nnk.merge(basta, on="radid", how="left")
    ut["andel_inom"] = ut["andel_inom"].round(3)
    ut["overlapp_ha"] = ut["overlapp_ha"].round(3)
    ut["area_ha"] = ut["area_ha"].round(3)

    inom = ut["SITECODE"].notna()
    print(f"\nKopplade till Natura 2000 : {inom.sum():5} ytor "
          f"({ut.loc[inom, 'area_ha'].sum():.0f} ha)")
    print(f"Utanfor Natura 2000       : {(~inom).sum():5} ytor "
          f"({ut.loc[~inom, 'area_ha'].sum():.0f} ha)  "
          f"- ligger i naturreservat/nationalpark utan N2000-overlapp")
    delade = int((ut["antal_omraden"] > 1).sum())
    print(f"Ytor som skar flera omraden: {delade:5}  "
          f"- tilldelade det med storst overlapp, granska vid behov")
    kant = int(((ut["andel_inom"] < 0.95) & inom).sum())
    print(f"Ytor delvis utanfor gransen: {kant:5}  "
          f"- andel_inom < 0,95 (karteringen gar ibland utanfor beslutsgransen)")

    os.makedirs(os.path.dirname(UT_GPKG), exist_ok=True)
    ut.to_file(UT_GPKG, driver="GPKG")
    ut.drop(columns="geometry").to_csv(UT_CSV,
                                       index=False, sep=";",
                                       encoding="utf-8-sig")
    print(f"\nSkrev {UT_GPKG} och {UT_CSV}")
    return ut


if __name__ == "__main__":
    main()
