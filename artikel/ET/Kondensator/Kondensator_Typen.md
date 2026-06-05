---
title: Kondensator Typen
kategorie: ET
tags: [kondensator, elektrolyt, keramik, folie, tantalum, bauform, anwendung, auswahl, elko, mlcc]
_status: PORT  # ET_alt/Kondensator/Kondensator_Typen.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Kondensator (Übersicht)]]
:::
:::

---

Die Wahl des richtigen Kondensatortyps ist entscheidend — Kapazität allein genügt nicht. Je nach Anwendung zählen Spannungsfestigkeit, Polung, Frequenzverhalten, Grösse und Kosten.

:::schematic
/abbildungen/kondensator/kondensator_typen_uebersicht.svg
:::

## Elektrolytkondensator (Elko)

Sehr grosse Kapazitäten (1 µF – 100 mF) bei moderaten Spannungen (6,3 V – 500 V). Das Dielektrikum ist eine dünne Oxidschicht auf Aluminium- oder Tantalfolie — erzeugt durch elektrolytisches Verfahren.

**Eigenschaften:**
- Gepolt (+ und − müssen eingehalten werden)
- Grosse Kapazität bei kleinem Volumen
- Schlechtes Hochfrequenzverhalten (parasitäre Induktivität und Widerstand)
- Alterung und begrenzte Lebensdauer (Elektrolyt trocknet aus)

**Anwendung:** Netzteilpuffer, Ladungsreservoirs, Koppelkondensatoren bei tiefen Frequenzen.

:::warning
Falsche Polung eines Elkos → Überdruck → Bersten. Elkos immer auf Polung prüfen. Bei Reparatur: Neue Elkos mit gleicher oder höherer Spannungsfestigkeit einbauen.
:::

## Keramikkondensator (MLCC)

Mehrschicht-Keramik-Kondensatoren (Multilayer Ceramic Capacitor). Heute der meistverwendete Kondensatortyp in der Elektronik.

**Eigenschaften:**
- Unpolarisiert
- Hervorragendes Hochfrequenzverhalten (niedrige Parasitär-Induktivität)
- Kompakt (SMD-Bauweise von 0402 bis 2220)
- Kapazitätswert hängt von Spannung und Temperatur ab (X5R, X7R, C0G — je stabiler, desto kleiner die Kapazität)

| Dielektrikum | Kapazitätsbereich | Stabilität | Anwendung |
|---|---|---|---|
| C0G (NP0) | pF – einige nF | Sehr stabil, ±30 ppm/K | Präzisionsfilter, Schwingkreise |
| X7R | nF – µF | Gut, ±15 % | Bypass, Filter |
| X5R/Y5V | µF – 100 µF | Schlecht (spannungsabhängig) | Entkopplung |

**Anwendung:** Bypass/Entkopplung, HF-Filter, Zeitglieder.

## Folienkondensator

Dielektrikum aus Kunststofffolie (PET, PP, Polyester). Robuств, unpolarisiert, geringe Selbstinduktivität.

**Eigenschaften:**
- Unpolarisiert
- Stabil und langlebig (kein Elektrolyt, kein Austrocknen)
- Gutes Temperaturverhalten
- Grösser als Elkos bei gleicher Kapazität

**Anwendung:** Audio (klangkritische Koppelkondensatoren), Snubber-Netzwerke, Motoranlauf, Kompensation.

## Tantalkondensator

Ähnlich wie Elko, aber mit Tantal als Anodenmaterial. Kleiner und stabiler als Aluminium-Elkos.

**Eigenschaften:**
- Gepolt (Polung noch wichtiger als beim Aluminiumelko)
- Geringe Leckströme
- Stabil gegen Temperatur und Alterung

:::warning
Tantalkondensatoren können bei Überpolung oder Überspannung in **Flammen aufgehen** — im wörtlichen Sinne. In kritischen Anwendungen immer mit 50 % Reserve auf die Nennspannung auslegen.
:::

## Auswahltabelle

| Typ | Kapazität | Gepolt | HF | Grösse | Anwendung |
|---|---|---|---|---|---|
| Elko (Al) | 1 µF – 100 mF | Ja | Schlecht | Gross | Netzteilpuffer |
| MLCC | 1 pF – 100 µF | Nein | Sehr gut | Klein | Bypass, Filter, HF |
| Folie | 1 nF – 100 µF | Nein | Gut | Mittel | Audio, Motor, Snubber |
| Tantal | 0,1 – 1000 µF | Ja | Gut | Mittel | SMD-Puffer, stabile Last |
| Supercap | 0,1 – 3000 F | Nein | Schlecht | Sehr gross | Kurzzeitspeicher |
