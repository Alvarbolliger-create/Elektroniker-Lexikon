---
title: OPV Spannungsfolger
kategorie: EK
kapitel: OPV
tags: [spannungsfolger, puffer, impedanzwandler, unity gain, 100 prozent gegenkopplung, hochohmig eingang, niederohmig ausgang]
groessen: v_u|Verstärkung|1; R_ein|Eingangswiderstand|GΩ; R_aus|Ausgangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Kollektorschaltung (Emitterfolger)]]
- [[OPV Nichtinvertierender Verstärker]]
:::
:::vbox
**Führt weiter zu**
- [[Instrumentenverstärker (3-OPV)]]
:::
:::

---

Der Spannungsfolger ist die einfachste OPV-Schaltung: der Ausgang ist direkt mit dem invertierenden Eingang verbunden. Die Ausgangsspannung folgt der Eingangsspannung exakt — bei nahezu unendlichem Eingangswiderstand und nahezu null Ausgangswiderstand.

## Schaltung und Formel

:::schematic Spannungsfolger
/schaltplaene/OPV/Verstärker/opv_spannungsfolger.svg
:::

Ausgang direkt auf den invertierenden Eingang (–) zurückgeführt. Signal an den nichtinvertierenden Eingang (+).

:::formel
U_a = U_e    # Verstärkung = 1, gleichphasig
:::

## Warum funktioniert das?

Die goldene Regel: U_+ = U_–. Der OPV regelt seinen Ausgang bis U_– = U_+. Da U_– direkt mit U_a verbunden ist, gilt U_a = U_+  = U_e. Die Verstärkung ist exakt 1.

## Eigenschaften

| Eigenschaft | Wert |
|---|---|
| Spannungsverstärkung | 1 (0 dB) |
| Phasenlage | gleichphasig (0°) |
| Eingangswiderstand | sehr hoch (GΩ, durch OPV begrenzt) |
| Ausgangswiderstand | sehr klein (< 1 Ω bei GK) |

## Anwendungsgebiete

**Impedanzwandler**: Hochohmige Quelle (Sensor, Potentiometer, Mikrofon) treibt niederohmige Last (Kabel, ADC-Eingang), ohne dass die Last die Quelle belastet. Das Messsignal wird nicht verfälscht.

**Pufferstufe**: Zwischen zwei Verstärkerstufen, damit die zweite Stufe den Arbeitspunkt der ersten nicht verschiebt.

**ADC-Puffer**: Vor einem Analog-Digital-Wandler schützt der Spannungsfolger den Sensor vor dem Ladestrom des ADC-Eingangs.

:::info
Der BJT-Emitterfolger erfüllt dieselbe Funktion, ist aber weniger präzise (U_BE-Offset, temperaturabhängig). Der OPV-Spannungsfolger ist der moderne Standard für diese Aufgabe. → [[BJT Kollektorschaltung (Emitterfolger)]]
:::

:::warning
Bei kapazitiver Last (z. B. langer Kabel-Kapazität) kann der Spannungsfolger schwingen. Ein kleiner Widerstand (10–100 Ω) in Reihe zum Ausgang stabilisiert die Schaltung.
:::
