---
title: Filtercharakteristik
kategorie: EK
tags: [butterworth, chebyshev, bessel, filtercharakteristik, überschwingen, ripple, steilheit, gruppenlaufzeit, filterordnung, approximation]
symbol: —
einheit: —
---

Filtercharakteristik beschreibt das Verhalten eines Filters im Übergangsbereich. Butterworth, Chebyshev und Bessel sind drei grundlegende Approximationen mit unterschiedlichen Kompromissen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Tiefpass (TP)]]
- [[Aktive Filter]]
:::
:::vbox
**Verwandte Artikel**
- [[Tiefpass (TP)]]
- [[Hochpass (HP)]]
:::
:::

---

## Butterworth

**Maximale Flachheit im Durchlassband.**

- Kein Ripple (Welligkeit) im Durchlassbereich
- Keine Dämpfung unterhalb f_g
- Kein Überschwingen bei f_g
- Sanfte, monoton abfallende Flanke
- **Standard für die meisten Anwendungen**

:::plot
var: f
range: 0.01, 10
xlabel: Frequenz (normiert)
ylabel: Amplitude (normiert)
Butterworth 2. Ord.: 1 / sqrt(1 + f^4)
:::

**Vorteil**: Stabiles, vorhersehbares Verhalten, keine Signalverzerrung im Durchlassband.  
**Nachteil**: Weniger steile Flanke als Chebyshev gleicher Ordnung.

## Chebyshev

**Maximale Steilheit bei erlaubtem Ripple.**

- Steile Flanke — benötigt weniger Ordnungen als Butterworth für gleiche Flankensteilheit
- Ripple (Welligkeit) im Durchlassband — die Amplitude schwankt bis zur Grenzfrequenz
- Kann bei f_g leicht verstärken (bei hohem Q-Faktor)

:::plot
var: f
range: 0.01, 10
xlabel: Frequenz (normiert)
ylabel: Amplitude (normiert)
Chebyshev (ca.):  1 / sqrt(1 + 0.5 * (2*f^2 - 1)^2)
:::

**Vorteil**: Steilste Flanke bei gegebener Ordnung.  
**Nachteil**: Ripple im Durchlassband verzerrt das Signal. Nicht geeignet wenn Signalamplitude präzise sein muss.

## Bessel

**Maximale Linearität der Phase (konstantste Gruppenlaufzeit).**

- Alle Frequenzanteile werden gleich verzögert → **Signalform bleibt erhalten**
- Flachste Flanke der drei Typen
- Kein Ripple, kein Überschwingen

**Vorteil**: Rechtecke und Pulse passieren den Filter ohne Verzerrung der Form.  
**Nachteil**: Flachste Flanke — braucht höhere Ordnung für gleiche Dämpfung.

## Vergleich

| Eigenschaft | Butterworth | Chebyshev | Bessel |
|---|---|---|---|
| Flankensteilheit | mittel | hoch | niedrig |
| Ripple im Durchlassband | keiner | ja | keiner |
| Überschwingen bei f_g | keiner | möglich | keiner |
| Phasenlinearität | mittel | schlecht | sehr gut |
| Typische Anwendung | Allgemein | Steep roll-off | Pulsübertragung |

## Wann welchen wählen?

**Butterworth**: Standardwahl. Signal soll im Durchlassband unverändert bleiben, Flanke ist nicht kritisch.

**Chebyshev**: Die Flanke muss so steil wie möglich sein und ein gewisser Ripple ist akzeptabel. Typisch in HF-Filtern.

**Bessel**: Das Signal enthält Pulse oder Rechtecke, die ihre Form behalten müssen. Typisch in Datenübertragung und Messsystemen.

:::info
Die Filtercharakteristik wird durch die Q-Faktoren der einzelnen Stufen bestimmt. Ein Butterworth-Filter 4. Ordnung besteht aus zwei Sallen-Key-Stufen mit unterschiedlichen Q-Werten (0.54 und 1.31), die zusammen die maximale Flachheit ergeben.
:::
