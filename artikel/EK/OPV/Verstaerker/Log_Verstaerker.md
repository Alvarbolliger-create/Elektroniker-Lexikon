---
title: Logarithmischer Verstärker
kategorie: EK
kapitel: OPV
tags: [logarithmisch, log-verstärker, antilog, dynamikbereich, transimpedanz, diodenkennlinie, kompandierung, rms, shockley]
groessen: U_a|Ausgangsspannung|V; I_s|Sättigungsstrom|A; U_T|Temperaturspannung|mV
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierender Verstärker]]
- [[Diode]]
- [[pn-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[OPV Grundlagen]]
:::
:::vbox
**Führt weiter zu**
- [[Klirrfaktor]]
:::
:::

---

Der logarithmische Verstärker nutzt die exponentielle Kennlinie einer Diode in der Rückkopplung, um den natürlichen Logarithmus der Eingangsspannung zu berechnen. Er komprimiert grossen Dynamikbereich auf einen kleinen Aussteuerbereich.

## Funktionsprinzip

:::schematic Logarithmischer OPV-Verstärker: OPV-Dreieck. U_ein → R → invertierender Eingang (−). Nichtinvertierender Eingang (+) auf GND. Diode D in der Rückkopplung (Anode an −, Kathode an Ausgang) statt R_R. Spannung U_D über Diode = Ausgang U_a (negativ). Wegen Shockley-Gleichung: U_a = −U_T·ln(U_ein / (I_S·R))
/Diagramm/opv_log_verstaerker.svg
:::

Im invertierenden Verstärker wird der Rückkopplungswiderstand durch eine **Diode** ersetzt. Wegen der Shockley-Gleichung (U_D = U_T · ln(I_D / I_S), mit U_T = 26 mV) und der virtuellen Masse, durch die der gesamte Eingangsstrom I_ein = U_ein / R durch die Diode fliesst, ergibt sich:

:::formel
U_a = -U_T * ln(U_ein / (I_S * R))    # Ausgangsspannung (logarithmisch)
:::

## Antilogarithmischer Verstärker (Antilog)

Diode und Widerstand vertauschen: Diode am Eingang, Widerstand in der Rückkopplung. Der Ausgang ist die Umkehrfunktion (Exponentialfunktion):

:::formel
U_a = -I_S * R * exp(U_ein / U_T)    # Antilog
:::

## Anwendungen

**Dynamikkompression**: Audiosignale haben einen grossen Dynamikbereich (> 100 dB). Ein Log-Verstärker komprimiert diesen auf handhabbare Pegel (Kompander-Schaltung).

**dB-Messung**: Signalstärke direkt in Dezibel anzeigen — der Ausgang ist proportional zu dB.

**Multiplikation/Division**: log(A) + log(B) = log(A×B). Zwei Log-Verstärker + Summierer = Multiplizierer.

**Fotostrom-Messung**: Fotodioden liefern über viele Dekaden linearen Strom — der Log-Verstärker bildet diesen auf einen kleinen Spannungsbereich ab.

:::warning
Der Log-Verstärker ist **sehr temperaturempfindlich**: U_T = k·T/q ändert sich mit 3.3 mV/10 K. I_S verdoppelt sich alle 10 K. Für genaue Anwendungen müssen Diode und Transistor auf gleicher Temperatur sein (Matched Pair im Gehäuse) und der U_T-Faktor temperaturkompensiert werden.
:::

## Praktische Schaltung

In der Praxis wird statt einer Diode meist ein **BJT (Basis-Kollektor kurzgeschlossen)** verwendet — bessere Kennlinie, geringeres Rauschen, kleinerer Sättigungsstrom. Die Formel bleibt gleich mit I_S = Kollektor-Sättigungsstrom.

Fertige Log-Verstärker-ICs (AD8304, LOG114) integrieren die Temperaturkompensation und liefern kalibrierte Ausgänge direkt in dB.
