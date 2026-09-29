# Popup-avsnitt: Hävd (jordbruksskiften) — utkast 2026-09-29

Ska in i `nnk-granskning-2026/docs/popup-arcade-uttryck.md` när granskningslagret har havd-fälten.

```arcade
// Hävd enligt Jordbruksverkets jordbruksskiften
var h = $feature.havd_skiften;
if (IsEmpty(h)) { return ""; }
var t = "Hävd enligt skiften (" + $feature.havd_period + "): " + h;
if (h == "Ja" || h == "Delvis") {
  if (!IsEmpty($feature.havd_obrutet_sedan)) {
    t += TextFormatting.NewLine + "Obruten hävd sedan: " + $feature.havd_obrutet_sedan;
  }
}
if (h == "Delvis" && !IsEmpty($feature.havd_ar_utan_bete)) {
  t += TextFormatting.NewLine + "År utan bete: " + $feature.havd_ar_utan_bete;
  if ($feature.havd_ar_utan_bete == "2015") {
    t += TextFormatting.NewLine + "(Bara 2015 saknas – troligen brist i skiftesdata, inte uppehåll i hävden.)";
  }
}
if (h == "Nej") {
  t += TextFormatting.NewLine + "(Ytan träffar skiften men aldrig bete – kan vara en kantträff mot åker.)";
}
if (h == "Oklart") {
  t += TextFormatting.NewLine + "(Ingen skiftesträff. Bete utan stöd syns inte – kontrollera TUVA/ortofoto.)";
}
if ($feature.havd_varning_vall == "Ja") {
  t += TextFormatting.NewLine + "Varning: över halva ytan är vall (åkermark) senaste året.";
}
return t;
```

Filter i Konfigurator: `havd_skiften IN ('Ja','Delvis','Nej','Oklart')` med en rad per värde.
