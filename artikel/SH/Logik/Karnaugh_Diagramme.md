---
title: Karnaugh-Veitch-Diagramme (KV-Diagramme)
kategorie: SH
kapitel: Logik
tags: [kv-diagramm, karnaugh-veitch, minimierung, oder-normalform, don't-care, schaltungsvereinfachung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Schaltalgebra (Boolesche Algebra)]]
:::
:::vbox
**Führt weiter zu**
- [[Multiplexer (MUX)]]
:::
:::

---

**Karnaugh-Veitch-Diagramme** (KV-Diagramme) sind eine grafische Methode, um Funktionsgleichungen aus einer Wahrheitstabelle abzulesen und systematisch zu **minimieren** — deutlich übersichtlicher als das algebraische Umformen mit der Schaltalgebra.

## Aufbau eines KV-Diagramms

Ein KV-Diagramm hat genau so viele Felder, wie es mögliche Eingangskombinationen (Vollkonjunktionen) gibt — bei n Variablen also 2ⁿ Felder. Jedes Feld entspricht genau einer Zeile der Wahrheitstabelle.

:::merke
Die Zuordnung der Variablen zu den Achsen eines KV-Diagramms ist beliebig wählbar — eine Variable und ihre Negation müssen aber zwingend an derselben Seite stehen, und benachbarte Spalten/Zeilen dürfen sich immer nur in **einem** Bit unterscheiden (Gray-Code-Reihenfolge: ĀB̄, ĀB, AB, AB̄). Nur so ergeben sich die für die Vereinfachung nötigen Nachbarschaftsbeziehungen.
:::

![Aufbau eines 2-variabligen KV-Diagramms: links die Wahrheitstabelle mit den vier möglichen Kombinationen von A und B; der Pfeil zeigt, wie die vier Vollkonjunktionen (A∧B̄, Ā∧B, A∧B, Ā∧B̄) den Feldern des 2×2-KV-Rasters zugeordnet werden — Variable und ihre Negation stehen stets auf derselben Seite](abbildungen/kv_2var_zuordnung.png)

## Eintragen und Ablesen der ODER-Normalform

Aus der Wahrheitstabelle wird für jede Zeile mit Z = 1 eine **Vollkonjunktion** gebildet (UND-Verknüpfung aller Variablen, jeweils negiert oder nicht negiert, je nach Wert in der Zeile). Die ODER-Verknüpfung aller dieser Vollkonjunktionen ergibt die **ODER-Normalform** (ONF). Im KV-Diagramm trägt man an der jeweiligen Stelle einfach eine 1 ein:

:::tip
Nullen müssen nicht eingetragen werden — das KV-Diagramm zeigt standardmässig nur, *wo* die Funktion den Wert 1 annimmt.
:::

## Vereinfachungsregeln

Die eigentliche Stärke des KV-Diagramms liegt im **Zusammenfassen benachbarter Einsen zu Schleifen**:

| Regel | Aussage |
|---|---|
| Regel 1 | "Benachbarte" Vollkonjunktionen lassen sich zu Schleifen zusammenfassen — eine Schleife umfasst stets 2ⁿ Einsen (1, 2, 4, 8, 16 …) |
| Regel 2 | Erscheint eine Variable in einer Schleife sowohl negiert als auch nicht negiert, entfällt sie aus dem Schleifenterm |
| Regel 3 | Die vereinfachte Gleichung ergibt sich als ODER-Verknüpfung der einzelnen Schleifenterme |
| Regel 4 | Eine Vollkonjunktion darf in mehreren Schleifen gleichzeitig auftreten — je grösser die Schleifen, desto einfacher die Gleichung |
| Regel 5 | KV-Diagramme haben "zylindrische" Nachbarschaft — auch der linke und rechte bzw. obere und untere Rand gelten als benachbart (erweiterte Nachbarschaftsbeziehungen) |

![Die fünf KV-Vereinfachungsregeln mit visuellen Beispielen: Regel 1 — zwei benachbarte Einsen zu einer 2er-Schleife (X=B); Regel 2 — Variable kommt negiert und unnegiert vor, entfällt (X=1); Regel 3 — mehrere Schleifen als ODER-Verknüpfung (X=Ā∧B); Regel 4 — eine Eins darf in mehreren Schleifen verwendet werden (X=C̄); Regel 5 — KV-Diagramm für 3 Variablen zeigt zylindrische Nachbarschaft auch zwischen linkem und rechtem Rand](abbildungen/kv_vereinfachungsregeln.png)

:::merke
Eine Schleife mit 2 Feldern eliminiert eine Variable, eine Schleife mit 4 Feldern eliminiert zwei Variablen, eine Schleife mit 8 Feldern eliminiert drei Variablen — je grösser die Schleife, desto kürzer der resultierende Term.
:::

![KV-Diagramm-Strukturen für 3 und 4 Variablen: oben — 3-Variablen-Raster (8 Felder, zylindrische Form entspricht einem Zylinder) mit zwei Minimierungsbeispielen; unten — 4-Variablen-Raster (16 Felder) mit vollständiger Vollkonjunktions-Beschriftung und Schleifen-Beispiel; allgemein: 2¹ bis 2ⁿ Felder pro Schleife möglich](abbildungen/kv_3var_4var_strukturen.png)

## Don't-Care-Bedingungen

In der Praxis treten manche Eingangskombinationen nie auf (z. B. ungültige Sensorzustände). Für solche Fälle ist der Ausgangswert irrelevant — man trägt ein **x** (Don't Care) ein und darf es bei der Schleifenbildung wahlweise als 0 *oder* als 1 behandeln, je nachdem, was die grössere und damit einfachere Schleife ergibt.

:::tip
Don't-Care-Felder sind ein mächtiges Werkzeug zur Vereinfachung — sie "füllen Lücken" auf, sodass grössere, einfachere Schleifen entstehen. Voraussetzung ist, dass die entsprechende Eingangskombination tatsächlich nie vorkommt.
:::

## Anwendung: Vom Problem zur Schaltung

Der typische Arbeitsablauf bei der Entwicklung einer kombinatorischen Schaltung läuft in festen Schritten ab:

1. **Wahrheitstabelle** aus der Aufgabenstellung erstellen
2. **ODER-Normalform** aus der Wahrheitstabelle ablesen
3. **KV-Diagramm** erstellen und Schleifen bilden
4. **Vereinfachte Funktionsgleichung** aus den Schleifen ableiten
5. **Digitalschaltung** zeichnen — bei Bedarf auf NAND oder NOR umformen (→ [[Schaltalgebra (Boolesche Algebra)]])

:::info
Typische Praxisbeispiele für diesen Ablauf sind Alarmschaltungen ("Alarm, wenn mindestens zwei von drei Sensoren ansprechen"), Codewandler oder Steuerungen für Transportsysteme — überall dort, wo eine feste Logik aus mehreren binären Eingangssignalen ein Ausgangssignal bilden soll. Diese kombinatorische Logik bildet z. B. die Grundlage von [[Multiplexer (MUX)]] und [[Code-Wandler (BCD-zu-7-Segment)]].
:::
