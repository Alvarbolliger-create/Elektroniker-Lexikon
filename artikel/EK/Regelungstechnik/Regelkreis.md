---
title: Regelkreis
kategorie: EK
tags: [regelkreis, regler, regelgrösse, führungsgrösse, rückkopplung, stellgrösse, störgrösse, PT1, PT2, totzeit, sprungantwort, istwert, sollwert]
symbol: —
einheit: —
---

Ein Regelkreis hält eine Grösse auf einem gewünschten Wert, auch wenn Störungen auftreten. Grundlage jeder automatischen Steuerung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
:::
:::vbox
**Verwandte Artikel**
- [[P-, I-, D-Regler]]
:::
:::vbox
**Führt weiter zu**
- [[PID-Regler]]
:::
:::

---

## Grundbegriffe

**Führungsgrösse (Sollwert)**: Der gewünschte Wert. Zum Beispiel 25 °C Raumtemperatur.

**Regelgrösse (Istwert)**: Der gemessene tatsächliche Wert.

**Regelabweichung**: Differenz zwischen Soll und Ist. Der Regler versucht sie auf null zu bringen.

**Stellgrösse**: Das was der Regler verändert. Zum Beispiel die Heizleistung.

**Störgrösse**: Äussere Einflüsse die den Istwert verändern. Zum Beispiel ein offenes Fenster.

## Wirkungsweise

Istwert messen, mit Sollwert vergleichen, Abweichung berechnen, Stellgrösse anpassen, erneut messen. Dieser Kreislauf läuft kontinuierlich.

Der entscheidende Unterschied zur Steuerung: Die Steuerung reagiert nicht auf Störungen. Der Regelkreis schon.

## Blockschaltbild

Sollwert → Vergleich → Regler → Stellglied → Strecke → Istwert → zurück zum Vergleich

## Stabilität

Ein Regler kann instabil werden: Er überschiesst den Sollwert, schwingt und klingt nicht ab. Das passiert wenn die Regelung zu aggressiv eingestellt ist. Mehr dazu unter [[Stabilität & Schwingneigung]].

:::info
Beispiele aus der Praxis: Thermostat (Temperatur), Drehzahlregler (Motor), Spannungsregler (Schaltnetzteil), Geschwindigkeitsregler (Fahrzeug), Lageregelung (Roboter).
:::

---

## Regelstrecken-Typen

Die Regelstrecke beschreibt das dynamische Verhalten des zu regelnden Systems. Das Verhalten bestimmt, welcher Regler nötig ist.

| Typ | Verhalten | Sprungantwort | Beispiel |
|---|---|---|---|
| P-Tt (P mit Totzeit) | Sofortige Reaktion, verzögert | Sprung nach Totzeit | Förderband |
| PT1 | Verzögerte proportionale Reaktion | Exponentiell gegen Endwert | Heizung |
| PT2 | Zwei Verzögerungen, ev. Schwingung | Gedämpfte Schwingung | Motordrehzahl |
| IT1 | Integrierende Strecke + Verzögerung | Rampe mit Anlaufverzögerung | Füllstand |
| I (reines Integral) | Ausgang wächst solange Eingang ≠ 0 | Rampe | Positionsregelung |

**PT1-Strecke** (häufigste in der Praxis):

:::monospace
Sprungantwort: y(t) = K × (1 - e^(-t/T))

K = Streckenverstärkung    # Endwert / Eingangssprung
T = Zeitkonstante          # Zeit bis 63.2% des Endwerts erreicht
:::
**Faustregeln für den Regler**:
- PT1-Strecke → PI-Regler ausreichend
- PT2-Strecke → PID, damit der D-Anteil das Überschwingen dämpft
- Strecke mit grosser Totzeit → Regler schwer einstellbar, Totzeit begrenzt die Regelgeschwindigkeit
