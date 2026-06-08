---
title: Komparator
kategorie: EK
kapitel: OPV
tags: [komparator, vergleicher, open-collector, pullup, referenzspannung, offsetspannung, overdrive, lm393, lm339, tlv3201, open-loop]
groessen: U_ref|Referenzspannung|V; U_in|Eingangsspannung|V; t_p|Propagation Delay|ns
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Schmitt-Trigger Grundlagen]]
- [[Fensterkomparator]]
:::
:::vbox
**Führt weiter zu**
- [[Schmitt-Trigger Grundlagen]]
- [[Fensterkomparator]]
:::
:::

---

Ein Komparator vergleicht zwei Spannungen und gibt binär aus welche grösser ist. Er ist ein OPV **ohne Gegenkopplung** — die hohe Leerlaufverstärkung treibt den Ausgang sofort an eine der Versorgungsschienen.

## Funktion

:::schematic Komparator Grundschaltung: OPV-Dreieck ohne Gegenkopplung. Referenzspannung U_ref am invertierenden Eingang (−) (eingestellt über Spannungsteiler). Eingangssignal U_in am nichtinvertierenden Eingang (+). Ausgang U_a schaltet direkt an HIGH oder LOW. Kein Rückkopplungspfad
/Diagramm/komparator_grundschaltung.svg
:::

:::formel
U_a = U_a_max    wenn U_1 > U_2   # Ausgang HIGH
U_a = U_a_min    wenn U_1 < U_2   # Ausgang LOW
:::

Schon wenige Mikrovolt Unterschied genügen, um den Ausgang voll auszusteuern (A_ol = 100 000×).

## Open-Collector-Ausgang

:::schematic Komparator Open-Collector-Ausgang: Komparator-IC. Interner NPN-Transistor: Kollektor als Ausgang-Pin, Emitter auf GND. Externer R_pullup von V_cc zum Kollektor-Pin. Last oder Folgeschaltung am selben Knoten. Transistor leitet → Ausgang LOW. Transistor sperrt → Ausgang HIGH (durch R_pullup). Mehrere Open-Collector-Ausgänge am selben Pullup = Wired-AND
/Diagramm/komparator_open_collector.svg
:::

Die meisten Komparator-ICs haben einen **Open-Collector-Ausgang**: Intern sitzt nur ein Transistor der nach GND zieht. Ein externer **Pullup-Widerstand** nach V_cc ist zwingend nötig.

**Vorteil**: Die Ausgangsspannung (HIGH-Pegel) ist frei wählbar — der Pullup bestimmt sie. Mehrere Komparatoren können am selben Pullup zusammengeschaltet werden (Wired-AND).

:::formel
R_pullup = (V_cc - U_ol) / I_ol_max    # Pullup; U_ol = Low-Ausgang, I_ol = max. Senkstrom
:::

## OPV vs. Komparator-IC

| Eigenschaft | OPV (z.B. LM358) | Komparator (z.B. LM393) |
|---|---|---|
| Ausgang | Push-Pull | Open-Collector |
| Propagation Delay | langsam (µs) | schnell (ns–µs) |
| Für GK geeignet | Ja (stabil) | Nein (schwingt) |
| Ausgangspegel | ≈ Schienen | wählbar (Pullup) |

:::warning
Einen OPV als Komparator zu verwenden ist möglich, aber nicht ideal: langsame Flanken, kein definiertes Verhalten nahe der Schaltschwelle, Ausgang erreicht Schienen nicht. Für schnelle oder präzise Vergleiche immer Komparator-IC verwenden.
:::

## Wichtige Kennwerte

**Offsetspannung**: Die Eingänge sind nicht perfekt symmetrisch — es besteht eine Differenz im mV bis µV Bereich, die zu einem Schaltfehler führt. Häufig hat ein Komparator Anschlüsse zum Abgleich.

**Overdrive**: Je grösser die Spannungsdifferenz, desto schneller schaltet der Komparator. Mit minimalem Overdrive (< 1 mV) kann die Schaltzeit um Grössenordnungen langsamer werden.

**Betriebsspannung**: Komparatoren können immer mit +/– Speisung betrieben werden, auch wenn «dual supply» nicht im Datenblatt steht.

## Grundschaltung mit Referenz

U_ref mit Spannungsteiler oder Zener-Diode an einen Eingang. Das zu vergleichende Signal an den anderen. Sobald U_in die Referenz überschreitet, schaltet der Ausgang.

:::monospace
Beispiel: Lichtschalter
LDR-Spannungsteiler → (+), Referenz-Spannungsteiler → (–)
Bei Dunkel: U_LDR sinkt unter U_ref → Ausgang LOW → LED/Relais einschalten
:::

## Typische Komparator-ICs

| Typ | Kanäle | Ausgang | t_p | V_supply |
|---|---|---|---|---|
| LM393 | 2 | Open-Collector | 1.3 µs | 2–36 V |
| LM339 | 4 | Open-Collector | 1.3 µs | 2–36 V |
| TLV3201 | 1 | Push-Pull | 260 ns | 2.7–5.5 V |
| MAX9021 | 1 | Push-Pull | 270 ns | 2.4–5.5 V, RRIO |
