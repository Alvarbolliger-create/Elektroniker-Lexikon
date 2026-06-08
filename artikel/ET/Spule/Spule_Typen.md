---
title: Spule Typen
kategorie: ET
tags: [spule, luftspule, ferritkern, ringkern, drossel, bauform, anwendung, emv, netzdrossel]
_status: PORT  # ET_alt/Spule/Spule_Typen.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Spule (Übersicht)]]
:::
:::

---

Die Wahl der richtigen Spule hängt von Induktivität, Strom, Frequenz und Einsatzgebiet ab. Kernmaterial und Bauform bestimmen massgeblich die Eigenschaften.

:::schematic
/abbildungen/spule/spule_typen_uebersicht.svg
:::

## Luftspule

Keine Sättigungsgrenze, kein Kernmaterial. Induktivität bleibt bis zu sehr hohen Frequenzen konstant. Aber: Für hohe Induktivitäten viele Windungen nötig → gross und teuer.

**Anwendung:** HF- und UHF-Schwingkreise, Antennen, Messspulen. In der Leistungselektronik selten wegen der grossen Abmessungen.

## Ferritkernspule

Ferritkern aus gesintertem Metalloxid (mu_r typisch 20 – 15 000). Erhöht die Induktivität drastisch bei kleinen Abmessungen.

| Ferritmaterial | Frequenzbereich | mu_r |
|---|---|---|
| Mn-Zn Ferrit | 1 kHz – 1 MHz | 1000–15 000 |
| Ni-Zn Ferrit | 100 kHz – 100 MHz | 10–2000 |

**Sättigungsgefahr**: Wird der Ferritkern zu stark magnetisiert, sättigt er — die Induktivität bricht ein. Drosseln im Schaltnetzteil müssen deshalb auf den maximalen Strom ausgelegt sein.

**Anwendung:** Schaltnetzteildrosseln, HF-Übertrager, EMV-Ferriten.

## Ringkerndrossel

Wicklung auf einem Ringkern (Toroid). Sehr kleiner Streufluss — das Magnetfeld bleibt weitgehend im Kern eingeschlossen.

**Vorteile:** Geringe EMV-Abstrahlung, hohe Induktivität pro Windung, kein äusseres Magnetfeld.

**Nachteile:** Schwieriger zu wickeln, Kernquerschnitt und Länge schwer zugänglich.

**Magnetischer Pfad bei der Ringspule:** Die Feldlinien laufen als geschlossene Kreise im Ring. Der magnetische Pfad l entspricht daher der **mittleren Feldlinienlänge l_m** — dem Umfang auf dem mittleren Durchmesser d_m:

:::formel
l = l_m = pi * d_m              # mittlere Feldlinienlänge der Ringspule
H = N * I / (pi * d_m)          # Feldstärke der Ringspule
:::

Wird d_m bei gleichem Strom und gleicher Windungszahl um den Faktor x grösser, wächst l_m um denselben Faktor x — H sinkt entsprechend auf 1/x der ursprünglichen Feldstärke (H ~ 1/l). Details zur Feldstärke-Formel allgemein → [[Magnetfelder]].

**Anwendung:** Netzfilter, Audio-Verstärker, Gegentakt-Drossel in Schaltnetzteilen, EMV-Filternetzwerke.

## Netzdrossel (Common-Mode Drossel)

Spezielle Spule für EMV-Unterdrückung: Zwei Wicklungen auf demselben Kern, gegensinnig gewickelt. Gegentaktstrom (Nutzsignal) hebt sich auf — der Kern sättigt nicht. Gleichtaktstrom (EMV-Störung) wird durch die Induktivität gebremst.

**Anwendung:** Eingangsfilter von Schaltnetzteilen, Frequenzumrichtern. Jedes europäische Netzteil mit CE-Zeichen enthält eine Gleichtaktdrossel.

## Auswahltabelle

| Typ | Induktivitätsbereich | Strom | Frequenz | Anwendung |
|---|---|---|---|---|
| Luftspule | nH – einige µH | Beliebig | bis GHz | HF, Schwingkreis |
| Ferritkernspule | µH – mH | klein–mittel | kHz–MHz | Schaltwandler, Filter |
| Ringkerndrossel | µH – H | klein–gross | 50 Hz – MHz | EMV, Audio, Netzfilter |
| Netzdrossel (CM) | mH – H | gross | 50 Hz – kHz | EMV-Filter, Netzgeräte |

:::tip
Für die Leistungselektronik (Schaltwandler, Induktionsherd, Frequenzumrichter) ist Ferrit die erste Wahl. Für Netzfilter und Trafos bei 50 Hz wird weiterhin Trafoblech (laminiertes Siliziumstahl) verwendet — Ferrit sättigt bei 50-Hz-Flussdichten zu früh.
:::
