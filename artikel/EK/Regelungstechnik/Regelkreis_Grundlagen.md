---
title: Regelkreis Grundlagen
kategorie: EK
kapitel: Regelungstechnik
tags: [regelkreis, regelung, steuerung, sollwert, istwert, regeldifferenz, stellgrösse, störgrösse, geschlossen, blockschaltbild, P-Regler, rückkopplung, bleibende-abweichung]
groessen: w|Sollwert|V; x|Istwert|V; e|Regeldifferenz|V; y|Stellgrösse|V; z|Störgrösse|V; K_P|Proportionalbeiwert|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Subtrahierender Verstärker]]
- [[OPV Summierender Verstärker]]
:::
:::vbox
**Verwandte Artikel**
- [[Regelstrecke]]
- [[PID-Regler]]
:::
:::vbox
**Führt weiter zu**
- [[Regelstrecke]]
- [[PID-Regler]]
:::
:::

---

Eine **Regelung** unterscheidet sich von der Steuerung dadurch, dass der Istwert gemessen und mit dem Sollwert verglichen wird — Abweichungen werden automatisch korrigiert. Der Regelkreis ist ein **geschlossener Wirkungsablauf**.

## Steuerung vs. Regelung

| Eigenschaft | Steuerung (offen) | Regelung (geschlossen) |
|---|---|---|
| Rückkopplung | keine | ja (Istwert → Vergleich) |
| Störgrossen | kein Ausgleich | werden ausgeregelt |
| Stabilität | immer stabil | kann instabil werden |
| Typisch | Zeitschaltuhr, Motoransteuerung | Thermostat, Drehzahlregler |

## Blockschaltbild

:::schematic Regelkreis Blockschaltbild: Sollwert w (links) → Summierpunkt (+/−) → Regeldifferenz e → Regler → Stellgrösse y → Stellglied → Aktor → Istwert x (rechts). Störgrösse z greift zwischen Stellglied und Aktor ein. Rückkopplung: Istwert x → Sensor/Messkette → zurück zum Minus-Eingang des Summierpunkts. Geschlossener Kreislauf
/Diagramm/regelkreis_blockschaltbild.svg
:::

## Grössen aus dem Spick

| Symbol | Name | Bedeutung |
|---|---|---|
| w | Sollwert | Gewünschter Zielwert (Eingang) |
| x | Istwert | Gemessener Wert der Regelgrösse |
| e | Regeldifferenz | e = w − x (Regelabweichung) |
| y | Stellgrösse | Ausgang Regler → Eingang Strecke |
| z | Störgrösse | Externe Störung auf die Strecke |
| K_P | P-Regelanteil | Proportionaler Verstärkungsfaktor |
| K_I | I-Regelanteil | Integrierender Anteil |
| K_D | D-Regelanteil | Differenzierender Anteil |

## P-Regler (Spick, Strecke = 1 → x = y)

:::formel
e = w * 1 / (1 + K_P)        # verbleibende Regeldifferenz (bleibende Abweichung)
y = w * K_P / (1 + K_P)      # Stellgrösse im eingeschwungenen Zustand
:::

:::info
Der P-Regler hat immer eine **bleibende Regeldifferenz**: Je grösser K_P, desto kleiner die Abweichung — aber desto grösser die Gefahr von Instabilität. Mit K_P → ∞ würde e → 0, aber die Schaltung schwingt auf.
:::

## Reglertypen — Übersicht

| Typ | Bleibende Abweichung | Reaktionszeit | Stabilitätsrisiko |
|---|---|---|---|
| **Zweipunktregler** | ja (±Hysterese) | sofort | keines |
| **Dreipunktregler** | ja (±Hysterese) | sofort | keines |
| **P** | ja | schnell | gering |
| **I** | nein | langsam | mittel |
| **PI** | nein | mittel | mittel |
| **PD** | ja | sehr schnell | gering |
| **PID** | nein | schnell | höher |

## Zweipunktregler

Der Zweipunktregler schaltet den Ausgang zwischen zwei Zuständen (Ein / Aus). Er ist der einfachste Regler und immer stabil — hat aber eine **bleibende Schwingung** um den Sollwert.

**Hysterese** verhindert zu schnelles Umschalten: Der Regler schaltet erst bei Über- oder Unterschreiten zweier verschiedener Schwellen.

:::monospace
Beispiel Thermostat: Sollwert 20 °C
  → Heizung AUS bei 21 °C (obere Schwelle)
  → Heizung EIN bei 18 °C (untere Schwelle)
  Hysterese = 21 − 18 = 3 °C
:::

Elektronische Realisierung: Schmitt-Trigger → [[Schmitt-Trigger Grundlagen]]

## Dreipunktregler

Der Dreipunktregler hat **drei Ausgangszustände** — z. B. Heizen / Aus / Kühlen. Er braucht zwei Schwellwerte und ist geeignet, wenn bidirektionale Stellglieder nötig sind.

:::monospace
Beispiel Heiz/Kühl-Thermostat:
  x < 18 °C → Heizen (Zustand 1)
  18 °C ≤ x ≤ 22 °C → Aus (Zustand 2)
  x > 22 °C → Kühlen (Zustand 3)
:::

:::tip
Faustregeln Reglerauswahl: Einfache, schnelle Strecken → PI. Träge Strecken oder Strecken mit Totzeit → PID. Integrierende Strecken (Füllstand, Position) → P oder PD.
:::
