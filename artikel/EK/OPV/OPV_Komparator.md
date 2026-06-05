---
title: OPV Komparator
kategorie: EK
tags: [komparator, OPV, schwellwert, hysterese, schmitt-trigger, LM393, LM339, open-collector, referenzspannung, zweipunktschwelle, fensterkomparator, IEC 60617]
symbol: —
einheit: —
---

Ein Komparator vergleicht zwei Spannungen und gibt digital aus welche grösser ist. Der Ausgang ist immer in einem von zwei Zuständen: HIGH oder LOW.

:::formel
U_a = U_a_max   für U_1 > U_2
U_a = U_a_min   für U_1 < U_2
:::
:::hbox
:::vbox
**Voraussetzungen**
- [[OPV: Aufbau & Kennwerte]]
:::
:::vbox
**Verwandte Artikel**
- [[Schmitt-Trigger]]
:::
:::vbox
**Führt weiter zu**
- [[Schwellwertschalter]]
:::
:::

---

## Schaltsymbol

Zwei Darstellungen sind üblich:

| Amerikanisch | IEC 60617 |
|---|---|
| Dreieck mit + und − Eingang | Rechteck mit X, Y Eingängen und X>Y Ausgang |

## Grundprinzip

OPV ohne Gegenkopplung. Die sehr hohe Leerlaufverstärkung (100 000×) sorgt dafür, dass schon ein Unterschied von wenigen Mikrovolt den Ausgang vollständig an eine der Versorgungsschienen treibt.

- U_+ > U_−: Ausgang → U_a_max (≈ U+)
- U_+ < U_−: Ausgang → U_a_min (≈ U−)

## Komparator-IC vs. OPV

Ein echter Komparator-IC unterscheidet sich wesentlich vom OPV:

| Eigenschaft | OPV (z.B. LM358) | Komparator (z.B. LM393) |
|---|---|---|
| Ausgang | Push-Pull (aktiv HIGH und LOW) | Open-Collector (nur aktiv LOW) |
| Schaltgeschwindigkeit | langsam (µs) | schnell (ns–µs) |
| Ausgangspegel | ≈ Versorgungsschienen | wählbar (Pullup-Widerstand nötig) |
| Verhalten ohne GK | instabil, Schwingen möglich | für Vergleich optimiert |

**Open-Collector-Ausgang (LM393)**: Der Ausgang hat nur einen Transistor der nach GND zieht. Ein Pullup-Widerstand nach +V zieht den Ausgang auf HIGH wenn der Transistor sperrt. Vorteil: Mehrere Komparatoren können ODER-verknüpft werden (Ausgänge einfach zusammenschalten).

## Referenzspannung

Eine Eingangsspannung ist die Referenz (U_ref), die andere das Signal (U_in). Wenn U_in die Referenz überschreitet, schaltet der Ausgang.

Typische Anwendung: Lichtschalter — LDR-Spannungsteiler an einem Eingang, Referenzspannungsteiler am anderen. Wenn es dunkel wird, schaltet das Licht ein.

## Fensterkomparator

Zwei Komparatoren zusammen prüfen ob ein Signal **innerhalb** eines Spannungsfensters liegt:

- Komparator 1: Prüft ob U_in > U_S_unten
- Komparator 2: Prüft ob U_in < U_S_oben
- Nur wenn beide Bedingungen erfüllt: Ausgang HIGH

Anwendung: Überwachen ob eine Spannung im erlaubten Bereich liegt (z.B. Batterie zwischen 11 V und 13 V).

## Hysterese (Schmitt-Trigger)

Ohne Hysterese schaltet der Komparator bei verrauschtem Signal viele Male hin und her wenn das Signal nahe am Schwellwert ist.

Lösung: Positive Rückkopplung erzeugt zwei verschiedene Schaltschwellen. Für Details → [[Schmitt-Trigger]].

## Typische Komparator-ICs

| Typ | Kanäle | Ausgang | Versorgung |
|---|---|---|---|
| LM393 | 2 | Open-Collector | 2–36 V |
| LM339 | 4 | Open-Collector | 2–36 V |
| TLV3201 | 1 | Push-Pull | 2.7–5.5 V |

:::warning
Einen normalen OPV (LM358) als Komparator zu verwenden ist möglich, aber nicht ideal: langsame Schaltflanken, kein definiertes Verhalten bei der Umschaltschwelle, Ausgang kommt nicht bis an die Versorgungsschienen. Für schnelle oder präzise Vergleiche immer einen dedizierten Komparator-IC einsetzen.
:::
