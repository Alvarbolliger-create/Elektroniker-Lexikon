---
title: Karnaugh-Veitch-Diagramm (KVD)
kategorie: SH
tags: [karnaugh, KVD, vereinfachung, boolesche algebra, logik, minimierung, dont-care, minterm, maxterm, gray-code, 4-variablen, quine-mccluskey]
symbol: —
einheit: —
---

Das Karnaugh-Veitch-Diagramm (KVD) ist eine grafische Methode zur Vereinfachung boolescher Funktionen. Es visualisiert alle Mintermkombinationen und erlaubt das Ablesen minimaler Schaltausdrücke ohne algebraische Rechnung.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schaltalgebra]]
- [[Logikgatter]]
:::
:::vbox
**Verwandte Artikel**
- [[Addierer]]
- [[Multiplexer & Demultiplexer]]
:::
:::

---

## Aufbau des KVD

Die Felder sind so angeordnet, dass benachbarte Felder sich in genau **einem Bit** unterscheiden (Gray-Code-Reihenfolge: 00, 01, 11, 10).

**2-Variable KVD** (A, B):

:::schematic
/Diagramm/karnaugh_0.svg
:::
**3-Variable KVD** (A, B, C):

:::schematic
/Diagramm/karnaugh_1.svg
:::
**4-Variable KVD** (A, B, C, D):

:::schematic
/Diagramm/karnaugh_2.svg
:::
---

## Vereinfachungsregeln

1. **Einsen eintragen**: Alle Minterme (Einsen) der Funktion eintragen.
2. **Gruppen bilden**: Einsen zu rechteckigen Gruppen zusammenfassen.
   - Gruppengrösse: immer eine Zweierpotenz: 1, 2, 4, 8, 16...
   - Gruppen dürfen sich überlappen
   - Das KVD ist **torusförmig**: Ränder gelten als benachbart (links–rechts, oben–unten)
3. **So gross wie möglich**: Gruppen immer so gross wie möglich wählen.
4. **Alle Einsen erfassen**: Jede 1 muss in mindestens einer Gruppe liegen.
5. **Ausdruck ablesen**: Für jede Gruppe den gemeinsamen Term notieren.

---

## Beispiel: 3-Variable

Funktion: F(A, B, C) = Σm(1, 3, 5, 7) — Minterme 1, 3, 5, 7

:::schematic
/Diagramm/karnaugh_3.svg
:::
Gruppe 1: {1, 3, 5, 7} — alle 4 Felder der Spalten BC=01 und BC=11  
→ B ändert sich (0→1), C=1 bleibt, A ändert sich → gemeinsam: **C = 1**

Ergebnis: **F = C** (minimaler Ausdruck)

---

## Beispiel: 4-Variable

F(A, B, C, D) = Σm(0, 1, 4, 5, 12, 13)

:::schematic
/Diagramm/karnaugh_4.svg
:::
Gruppe: {0,1,4,5,12,13} — Spalten CD=00 und CD=01, Zeilen AB=00, 01, 11  
A=1 tritt nur in AB=10 auf und ist nicht dabei → D=0, C=0 sind gemeinsam, B ändert sich  
→ Ablesen: **F = C̄ · D̄** (A und B fallen weg)

---

## Don't-Care-Zustände (X)

Wenn bestimmte Eingangskombinationen nie auftreten, können diese als **X (Don't Care)** eingetragen werden. Don't Cares dürfen in Gruppen einbezogen werden, müssen es aber nicht. Das erlaubt grössere Gruppen und damit kleinere Ausdrücke.

:::info
Don't Cares entstehen z.B. bei BCD-Codes: Eingangskombinationen 1010–1111 (10–15) kommen nie vor und können als X gesetzt werden.
:::

---

## KVD vs. Boolesche Algebra

| Methode | Vorteil | Nachteil |
|---|---|---|
| Boolesche Algebra | Formal exakt, keine Grenzen | Unübersichtlich bei vielen Variablen |
| KVD | Visuell, schnell bei 2–4 Variablen | Unpraktisch ab 5+ Variablen |
| Quine-McCluskey | Algorithmisch, beliebig viele Variablen | Aufwändig von Hand |
