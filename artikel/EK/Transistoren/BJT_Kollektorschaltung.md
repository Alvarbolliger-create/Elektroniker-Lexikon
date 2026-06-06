---
title: BJT Kollektorschaltung (Emitterfolger)
kategorie: EK
kapitel: Transistoren
tags: [kollektorschaltung, emitterfolger, impedanzwandler, puffer, stromverstärker, gleichphasig, niederohmig, hoher eingangswiderstand]
groessen: v_u|Spannungsverstärkung|~1; R_ein|Eingangswiderstand|kΩ; R_aus|Ausgangswiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BJT Grundlagen]]
- [[BJT Arbeitspunkt]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Emitterschaltung]]
- [[OPV Spannungsfolger]]
:::
:::vbox
**Führt weiter zu**
- [[OPV Grundlagen]]
:::
:::

---

Die Kollektorschaltung (auch **Emitterfolger** genannt) verstärkt die Spannung nicht — sie folgt ihr. Dafür hat sie einen sehr hohen Eingangswiderstand und einen sehr kleinen Ausgangswiderstand. Sie wirkt als **Impedanzwandler**.

## Schaltungsprinzip

:::schematic BJT Kollektorschaltung / Emitterfolger (NPN): U_B direkt am Kollektor (kein R_C). R1/R2 Basisteiler. C_ein am Eingang (Basis). Ausgang am Emitter → R_E → GND. u_aus folgt u_ein mit Offset –U_BE. Phasenlage 0°
/Diagramm/bjt_kollektorschaltung.svg
:::

:::schematic Push-Pull-Ausgangsstufe: NPN (oben, Emitter nach Ausgang) und PNP (unten, Emitter nach Ausgang) in Reihe zwischen V+ und V–. Gemeinsamer Ausgang in der Mitte. NPN leitet positive, PNP leitet negative Halbwelle
/Diagramm/bjt_push_pull.svg
:::

Der Kollektor ist direkt an U_B angeschlossen (kein R_C). Das Ausgangssignal wird am Emitter abgegriffen. Das Signal kommt an die Basis. Der Emitterwiderstand R_E ist die Last.

## Spannungsverstärkung

:::formel
v_u = u_aus / u_ein ≈ R_E / (R_E + r_BE/B) ≈ 1    # immer < 1, nahe 1
:::

Die Ausgangsspannung folgt der Eingangsspannung mit einem kleinen Offset (U_BE ≈ 0.7 V). Phasenverschiebung: **0° (gleichphasig)**.

**Warum nahe 1?** Der Emitter "folgt" der Basis — steigt U_B, steigt U_E ebenfalls um fast denselben Betrag (minus die konstante U_BE).

## Eingangs- und Ausgangswiderstand

Das ist die eigentliche Stärke der Kollektorschaltung:

:::formel
R_ein = R_1 || R_2 || (B * (r_BE + R_E))   # sehr hoch, typisch 50–500 kΩ
R_aus = r_BE / B || R_E                      # sehr niedrig, typisch 10–100 Ω
:::

| Kenngrösse | Emitterschaltung | Kollektorschaltung |
|---|---|---|
| Spannungsverstärkung | gross (–100 bis –300) | ≈ 1 |
| Stromverstärkung | gross | gross |
| Eingangswiderstand | mittel (1–10 kΩ) | gross (50–500 kΩ) |
| Ausgangswiderstand | mittel (1–10 kΩ) | klein (10–100 Ω) |
| Phasenlage | 180° | 0° |

## Anwendungsgebiete

**Impedanzwandler**: Hochohmige Quelle (z. B. Sensor, Mikrofon) treibt niederohmige Last (Lautsprecher, Kabel) über einen Emitterfolger — ohne die Quelle zu belasten.

**Leitungstreiber**: Signale über lange Leitungen senden. Der niedrige Ausgangswiderstand verhindert Pegeleinbrüche bei kapazitiver Last.

**Vorverstärker / Pufferstufe**: Zwischen Signalquelle und Verstärkerstufe, damit der Arbeitspunkt der nächsten Stufe die Quelle nicht belastet.

**Komplementärausgang (Push-Pull)**: Zwei Emitterfolger (NPN + PNP) bilden zusammen eine Ausgangsstufe mit minimalem Ausgangswiderstand in beide Stromrichtungen — typisch in Leistungsverstärkern.

:::info
Die analoge Schaltung im OPV-Bereich ist der **Spannungsfolger** — ein OPV mit 100 % Gegenkopplung. Er hat noch bessere Werte (R_ein im GΩ-Bereich, R_aus < 1 Ω) und ist einfacher zu dimensionieren. → [[OPV Spannungsfolger]]
:::
