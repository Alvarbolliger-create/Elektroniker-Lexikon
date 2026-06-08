---
title: Akku Grundlagen
kategorie: EK
kapitel: Akku
tags: [akku, batterie, zellchemie, lithium-ionen, lfp, nimh, kapazität, c-rate, innenwiderstand, serienschaltung, parallelschaltung, pack, nennspannung, ladeschlussspannung]
groessen: U_Nenn|Nennspannung|V; C_Ah|Kapazität|Ah; E|Energie|Wh; I_C|C-Rate-Strom|A; R_i|Innenwiderstand|Ω
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Spannungsquellen]]
:::
:::vbox
**Verwandte Artikel**
- [[BMS — Batteriemanagementsystem]]
- [[Spannungsstabilisierung]]
:::
:::vbox
**Führt weiter zu**
- [[BMS — Batteriemanagementsystem]]
- [[Zell-Balancing]]
:::
:::

---

Ein Akkumulator (Akku, Sekundärbatterie) ist ein **wiederaufladbarer** elektrochemischer Energiespeicher. Er wandelt chemische Energie in elektrische Energie um und kann durch Zufuhr von Strom wieder geladen werden. Im Gegensatz dazu: eine Primärbatterie ist nicht wiederaufladbar.

## Elektrische Kenngrössen

**Nennspannung** — typische Spannung während der Entladung. Hängt ausschliesslich von der Zellchemie ab.

**Kapazität C** — speicherbare Ladungsmenge in Amperestunden (Ah):

:::formel
E = U_Nenn * C_Ah    # Energie [Wh] = Spannung [V] × Kapazität [Ah]
:::

**C-Rate** — beschreibt den Lade-/Entladestrom relativ zur Kapazität:

:::formel
I = C_Rate * C_Ah    # Strom bei gegebener C-Rate
:::

:::monospace
Beispiel: 3000 mAh Zelle
Bei 1C: I = 1 × 3 A = 3 A   (in 1h entladen)
Bei 2C: I = 2 × 3 A = 6 A   (in 30 min entladen)
Bei 0.5C: I = 0.5 × 3 A = 1.5 A   (in 2h entladen)
:::

**Innenwiderstand R_i** — parasitärer Widerstand der Zelle. Bei hohem Strom entsteht Spannungsabfall und Wärme:

:::formel
U_klemme = U_Nenn - I * R_i    # Klemmenspannung unter Last
P_verlust = I^2 * R_i          # Verlustleistung als Wärme
:::

## Zellchemie-Vergleich

| Chemie | Nennspannung | Ladeschluss | Entladeschluss | Besonderheiten |
|---|---|---|---|---|
| Li-Ion (NMC/NCA) | 3.6–3.7 V | 4.2 V | 3.0 V | Hohe Energiedichte, empfindlich auf Überladung |
| LiFePO4 (LFP) | 3.2 V | 3.65 V | 2.5 V | Sehr sicher, >3000 Zyklen, etwas schwerer |
| LTO (Lithium-Titanat) | 2.3 V | 2.8 V | 1.5 V | Sehr schnell ladbar (10C), kälteresistent, geringe Energiedichte |
| NiMH | 1.2 V | 1.45 V | 1.0 V | Robust, AA/AAA-Format, kein Memory-Effekt |
| Blei-Gel (VRLA) | 2.0 V | 2.4 V | 1.75 V | Schwer, günstig, wartungsfrei, Starterbatterien |

:::warning
Li-Ion (NMC/NCA) ist empfindlich auf Überladung (> 4.2 V) und Tiefentladung (< 3.0 V). Ohne BMS kann die Zelle unwiederbringlich beschädigt werden oder in Brand geraten (Thermal Runaway). LFP ist deutlich sicherer — kein Thermal Runaway bekannt.
:::

## Zellenverbund: Pack-Design

Einzelzellen werden zu einem **Batteriepack** verschaltet, um die gewünschte Spannung und Kapazität zu erreichen:

**Reihenschaltung (S — Series)**: Spannungen addieren sich, Kapazität bleibt gleich:

:::formel
U_pack = n_S * U_Nenn    # Gesamtspannung
C_pack = C_Zelle         # Kapazität bleibt
:::

**Parallelschaltung (P — Parallel)**: Kapazität und Maximalstrom addieren sich, Spannung bleibt:

:::formel
C_pack = n_P * C_Zelle   # Gesamtkapazität
I_max  = n_P * I_Zelle   # Maximalstrom
:::

**Pack-Notation S×P**: z. B. 10S4P = 10 Zellen in Serie, 4 davon parallel.

:::monospace
E-Bike Akku: 10S4P aus 18650-Zellen (3.6 V / 3 Ah)
U_pack = 10 × 3.6 V  = 36 V
C_pack = 4  × 3 Ah   = 12 Ah
E_pack = 36 V × 12 Ah = 432 Wh
:::

## Zelldrift — warum ein BMS nötig ist

Zellen altern nie exakt gleich (Fertigungstoleranzen, unterschiedliche Temperaturen im Pack). Mit der Zeit driften ihre Spannungen auseinander:

- **Beim Entladen**: Schwächste Zelle erreicht zuerst die Untergrenze → BMS schaltet ab, obwohl andere Zellen noch Energie haben.
- **Beim Laden**: Stärkste Zelle erreicht zuerst die Obergrenze → Ladevorgang stoppt, obwohl andere Zellen noch nicht voll sind.

Ohne Balancing sinkt die nutzbare Kapazität mit jedem Zyklus. Ein **BMS mit Zell-Balancing** löst dieses Problem.

## Lade-Verfahren Li-Ion: CC/CV

Standard-Ladeverfahren für Li-Ion und LFP:

| Phase | Englisch | Beschreibung |
|---|---|---|
| 1. Konstantstrom | CC (Constant Current) | Ladestrom konstant (typisch 0.5–1C) bis Ladeschlussspannung |
| 2. Konstantspannung | CV (Constant Voltage) | Spannung konstant auf Ladeschluss, Strom sinkt bis < 0.05C |

:::tip
Akkus nicht dauerhaft auf 100 % geladen lassen (beschleunigt Alterung). Für lange Lagerung: Li-Ion bei 40–60 % SOC (ca. 3.7–3.8 V je Zelle) lagern, kühl und trocken.
:::
