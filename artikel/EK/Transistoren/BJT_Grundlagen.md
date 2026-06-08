---
title: BJT Grundlagen
kategorie: EK
kapitel: Transistoren
tags: [bjt, bipolartransistor, npn, pnp, basis, emitter, kollektor, stromverstärkung, kennlinie, grundschaltungen, emitterschaltung, kollektorschaltung, basisschaltung, arbeitsgerade, sättigung]
groessen: B|Stromverstärkung (DC)|—; I_C|Kollektorstrom|A; I_B|Basisstrom|A; I_E|Emitterstrom|A; U_CE|Kollektor-Emitter-Spannung|V; U_BE|Basis-Emitter-Spannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[pn-Übergang]]
- [[Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[FET Grundlagen]]
- [[BJT Arbeitspunkt]]
:::
:::vbox
**Führt weiter zu**
- [[BJT Emitterschaltung]]
- [[BJT Arbeitspunkt]]
- [[BJT Kollektorschaltung (Emitterfolger)]]
:::
:::

---

Ein Bipolartransistor (BJT) steuert einen grossen Strom mit einem kleinen. Ein schwacher Basisstrom kontrolliert einen bis zu mehrere hundert Mal stärkeren Kollektorstrom — das ist die Stromverstärkung.

## Aufbau und Typen

:::hbox
:::schematic NPN-Schichtenaufbau: n-Emitter | p-Basis (dünn) | n-Kollektor. Anschlüsse B, C, E eingezeichnet. Basis-Emitter-Übergang in Durchlass, Basis-Kollektor-Übergang in Sperr
/Diagramm/bjt_npn_schichten.svg
:::
:::schematic PNP-Schichtenaufbau: p-Emitter | n-Basis (dünn) | p-Kollektor. Umgekehrte Schichtreihenfolge zum NPN
/Diagramm/bjt_pnp_schichten.svg
:::
:::

Drei Halbleiterschichten, drei Anschlüsse:

| Anschluss | Kürzel | Funktion |
|---|---|---|
| Basis | B | Steuereingang (kleiner Strom) |
| Kollektor | C | Hauptstrom fliesst rein (NPN) |
| Emitter | E | Hauptstrom fliesst raus |

**NPN** (häufigster Typ): Kollektorstrom fliesst wenn ein kleiner Strom in die Basis fliesst. Emitter und Kollektor sind n-dotiert, Basis ist p-dotiert.

**PNP**: Umgekehrte Polarität — Strom fliesst aus der Basis heraus. Emitter und Kollektor sind p-dotiert.

## Schaltsymbole

:::hbox
:::schematic NPN-Transistor
/schaltplaene/symbole/Q_NPN.svg
:::
:::schematic PNP-Transistor
/schaltplaene/symbole/Q_PNP.svg
:::
:::

**NPN**: Pfeil am Emitter zeigt nach aussen (weg vom Transistor). **PNP**: Pfeil zeigt nach innen.

## Funktionsweise: Ladungsträgerfalle

Im NPN-Transistor sind zwei pn-Übergänge hintereinander geschaltet:
- **Basis-Emitter**: in Durchlassrichtung gepolt (U_BE ≈ 0.7 V) → Elektronen wandern vom Emitter in die Basis
- **Basis-Kollektor**: in Sperrrichtung gepolt → starkes elektrisches Feld

Die Basiszone ist absichtlich extrem dünn gehalten. Die eingedrungenen Elektronen treffen sofort auf das starke Feld der Basis-Kollektor-Sperrschicht — diese wirkt als **Ladungsträgerfalle**: Das Feld beschleunigt die Elektronen in Richtung Kollektor.

**Ergebnis:** Über 99% der vom Emitter kommenden Elektronen erreichen den Kollektor. Nur ~1% fliesst über den Basisanschluss ab. Dieses Verhältnis bestimmt die Stromverstärkung B ≈ 100 (oder mehr).

Kleine Basisstromänderungen führen zu grossen Kollektorstromänderungen.

## Stromverstärkung B (h_FE)

Das zentrale Kenndatum des BJT:

:::formel
B = I_C / I_B    # Stromverstärkung (DC); typisch 50–500
I_E = I_C + I_B  # Emitterstrom = Summe
:::

Ein kleiner Basisstrom I_B steuert den grossen Kollektorstrom I_C. Der Emitterstrom I_E ist die Summe beider.

| Transistor | B_min | B_typ | I_C(max) | Anwendung |
|---|---|---|---|---|
| BC547 | 110 | 300 | 100 mA | Kleinsignal, Schalten |
| BC337 | 100 | 250 | 800 mA | Mittlere Ströme |
| BD139 | 40 | 100 | 1.5 A | Treiberstufen |
| TIP31 | 25 | 50 | 3 A | Leistung |

## Betriebsbereiche

:::schematic BJT Ausgangskennlinienfeld: mehrere Kurven I_C über U_CE für verschiedene I_B-Werte (I_B = 0, 20, 40, 60, 80 µA). Sättigungsbereich links, aktiver Bereich Mitte, Sperrbereich bei I_B = 0. Arbeitsgerade eingezeichnet: geht von Punkt (U_CE = U_B, I_C = 0) bis (U_CE = 0, I_C = U_B/R_C). Q-Punkt markiert
/Diagramm/bjt_ausgangskennlinien.svg
:::

| Bereich | U_BE | U_CE | Zustand |
|---|---|---|---|
| Gesperrt | < 0.6 V | ≈ U_B | Kein Strom — "Schalter offen" |
| Aktiv / linear | ≈ 0.7 V | > 0.3 V | I_C = B · I_B — Verstärker |
| Gesättigt | ≈ 0.7 V | < 0.3 V | Maximaler Strom — "Schalter zu" |

Im **Schalterbetrieb** wird zwischen gesperrt und gesättigt gewechselt. Im **Verstärkerbetrieb** bleibt der Transistor im linearen Bereich (aktiver Betrieb).

## Die drei Grundschaltungen

Die Wahl des gemeinsamen Anschlusses (GND-Bezug) bestimmt das Verhalten der Verstärkerstufe:

| Eigenschaft | Emitterschaltung | Kollektorschaltung | Basisschaltung |
|---|---|---|---|
| Gemeinsamer Anschluss | Emitter | Kollektor | Basis |
| Stromverstärkung | gross (B ≈ 300) | gross (B ≈ 300) | < 1 |
| Spannungsverstärkung | gross (≈ 300) | < 1 | gross (≈ 100) |
| Leistungsverstärkung | sehr gross (≈ 30 000) | gross (≈ 300) | gross (≈ 200) |
| Eingangswiderstand | mittel (≈ 5 kΩ) | gross (≈ 50 kΩ) | klein (≈ 50 Ω) |
| Ausgangswiderstand | mittel | klein (≈ 100 Ω) | gross (≈ 50 kΩ) |
| Phasenlage | gegenphasig (180°) | gleichphasig | gleichphasig |
| Hauptanwendung | Spannungs-/Stromverstärker | Impedanzwandler | HF-Verstärker |

*Werte gelten für NPN-Kleinsignaltransistoren bei niedrigen Frequenzen.*

## Transistor als Schalter

### NPN — Low-Side-Schalter (Last zwischen V+ und Kollektor)

:::schematic NPN Low-Side Schalter: V+ → R_Last → Kollektor. Emitter → GND. Basis → R_B → Steuerausgang (µC). Freilaufdiode parallel zur Last
/Diagramm/bjt_npn_schalter.svg
:::

Berechnungsreihenfolge:

:::formel
I_Last = (V_plus - U_CEsat) / R_Last    # Laststrom; U_CEsat ≈ 0.2 V im Sättigungsbereich
I_B_min = I_Last / B_min               # Mindest-Basisstrom für Sättigung
I_B = 5 * I_B_min                     # Übersteuerungsfaktor 3–10 (typisch 5)
R_B = (U_Steuer - U_BE) / I_B         # Basiswiderstand; U_BE = 0.7 V
:::

:::monospace
Beispiel: V+ = 15 V, U_Steuer = 5 V, U_CEsat = 0.2 V, R_Last = 150 Ω, B = 90
  I_Last  = (15 - 0.2) / 150      = 98.7 mA
  I_B_min = 98.7 mA / 90          = 1.09 mA
  I_B     = 5 × 1.09 mA           = 5.45 mA
  R_B     = (5 - 0.7) / 5.45 mA  = 789 Ω → Normwert 680 Ω
:::

### PNP — High-Side-Schalter (Emitter an V+, Last gegen GND)

:::schematic PNP High-Side Schalter: V+ → Emitter. Kollektor → R_Last → GND. Basis → R_B → Steuerausgang (µC, gegen GND). Freilaufdiode parallel zur Last
/Diagramm/bjt_pnp_schalter.svg
:::

Beim PNP liegt der Emitter auf der Versorgungsspannung. Der Basisstrom fliesst aus der Basis heraus — die Steuerspannung muss unter V+ liegen, um zu schalten.

:::formel
I_Last  = (V_plus - U_CEsat) / R_Last
I_B_min = I_Last / B_min
I_B     = 5 * I_B_min
R_B     = (V_plus - U_EB - U_CEsat_Steuer) / I_B    # U_EB = 0.7 V (Emitter-Basis)
:::

:::monospace
Beispiel: V+ = 12 V, R_Lampe = 15 Ω, U_CEsat = 0.2 V, B = 200, Übersteuerung 5×
  I_Last  = (12 - 0.2) / 15 = 0.79 A
  I_B_min = 0.79 / 200      = 3.93 mA
  I_B     = 5 × 3.93 mA    = 19.65 mA
  R_B     = (12 - 0.7 - 0.2) / 19.65 mA = 564 Ω → Normwert 560 Ω
:::

:::warning
Immer den Basiswiderstand einbauen — niemals direkt vom Logikausgang auf die Basis. U_BE ≈ 0.7 V ist fest, R_B begrenzt den Basisstrom auf den berechneten Wert.
:::

Induktive Lasten (Relais, Motor) erfordern zwingend eine **Freilaufdiode** parallel zur Last → [[Relais]]
