---
title: SIL und PL
kategorie: SI
tags: [SIL, PL, funktionale sicherheit, IEC 61508, ISO 13849, risikograph, PFH, MTTFd, PLd, PLe, IEC 62061, kategorie]
symbol: —
einheit: —
---

SIL und PL sind Kennzahlen für die Zuverlässigkeit sicherheitsbezogener Funktionen. Sie geben an wie gut eine Schutzfunktion versagen darf.

:::hbox
:::vbox
**Voraussetzungen**
- [[Fehlerschutz (FI/RCD)]]
:::
:::vbox
**Verwandte Artikel**
- [[Not-Halt]]
- [[Sicherheitsrelais]]
:::
:::vbox
**Führt weiter zu**
- [[Zweikanalige Abschaltung]]
:::
:::

---

## SIL (Safety Integrity Level)

Definiert in IEC 61508 und IEC 62061. Vier Stufen:

| SIL | PFH (1/h) | Anwendungen |
|---|---|---|
| SIL 1 | 10^-5 bis 10^-6 | einfache Maschinen |
| SIL 2 | 10^-6 bis 10^-7 | Industrieanlagen |
| SIL 3 | 10^-7 bis 10^-8 | Prozessindustrie, Aufzüge |
| SIL 4 | 10^-8 bis 10^-9 | Kernkraft, Luftfahrt |

PFH = Probability of Dangerous Failure per Hour.

## PL (Performance Level)

Definiert in ISO 13849, speziell für Maschinen. Fünf Stufen (a bis e).

| PL | MTTFd | DCavg | Kategorie |
|---|---|---|---|
| a | niedrig | keine | B |
| c | mittel | niedrig | 2 |
| d | hoch | niedrig-mittel | 3 |
| e | hoch | hoch | 4 |

MTTFd = mittlere Zeit bis zum gefahrbringenden Ausfall.

## Wie wird ein Level bestimmt?

Über einen Risikographen. Einfliessende Parameter:
- Schwere der möglichen Verletzung (S)
- Häufigkeit der Exposition (F)
- Möglichkeit zur Ausweichung (P)

Das Ergebnis ist der geforderte PLr (required Performance Level). Die Anlage muss diesen erreichen oder übertreffen.

## Kategorie-Konzept (ISO 13849)

Die Kategorie beschreibt die Architektur des Sicherheitssystems:

- **Kat. B**: Einfachkanal, keine Diagnose
- **Kat. 2**: Einfachkanal mit periodischer Prüfung
- **Kat. 3**: Zweikanal, Ausfall eines Kanals wird erkannt
- **Kat. 4**: Zweikanal mit hoher Diagnosedeckung, kein Ausfall führt zum Verlust der Sicherheitsfunktion

## SIL vs. PL

SIL und PL lassen sich annähern konvertieren: PLd entspricht ungefähr SIL 2, PLe entspricht SIL 3. Eine exakte Gleichsetzung ist nicht korrekt, da die Normen unterschiedliche Ansätze haben.

:::warning
Die Berechnung von SIL/PL erfordert Daten aus Datenblättern (B10d-Werte für mechanische Komponenten, PFH für elektronische). Eine Sicherheitsberechnung ohne diese Daten ist nicht normgerecht.
:::
