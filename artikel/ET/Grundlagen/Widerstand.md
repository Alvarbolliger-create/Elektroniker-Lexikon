---
title: Widerstand (Bauformen, Farbcode, E-Reihen)
kategorie: ET
tags: [widerstand, bauteil, farbcode, smd, e-reihen, tht, potentiometer, leistung, derating, bauform, toleranz, worst-case, grenzwertbetrachtung, widerstandsnetzwerk, resistor array, dip, sip]
groessen: R|Widerstand|Ohm; P|Verlustleistung|W; T|Betriebstemperatur|°C
_status: PORT  # ET_alt/Bauelemente/Widerstand.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom, Spannung, Widerstand]]
- [[Elektrische Leistung]]
:::
:::vbox
**Verwandte Artikel**
- [[Leiterwiderstand]]
- [[NTC & PTC]]
:::
:::vbox
**Führt weiter zu**
- [[Reihenschaltung]]
- [[Parallelschaltung]]
- [[Spannungs- & Stromteiler]]
:::
:::

---

Widerstände sind die häufigsten passiven Bauteile in der Elektronik. Sie begrenzen Strom, teilen Spannungen, definieren Verstärkungen und schützen Schaltkreise. Die korrekte Auswahl nach Wert, Bauform und Belastbarkeit ist grundlegend.

## Bauformen

**THT (Through Hole Technology):** Bedrahtete Widerstände, für Lochrasterplatinen und Handbestückung. Leicht identifizierbar und lötbar.

**SMD (Surface Mount Device):** Miniaturisierte Bauteile für maschinelle Bestückung. Bezeichnung nach Gehäusegrösse:

| Gehäuse | Länge × Breite | Typische Leistung |
|---|---|---|
| 0402 | 1,0 × 0,5 mm | 1/16 W |
| 0603 | 1,6 × 0,8 mm | 1/10 W |
| 0805 | 2,0 × 1,25 mm | 1/8 W |
| 1206 | 3,2 × 1,6 mm | 1/4 W |
| 2512 | 6,4 × 3,2 mm | 1 W |

## Aufbau der Widerstandstypen

### Kohleschicht- und Metallschichtwiderstand (THT)

:::schematic
/abbildungen/grundlagen/widerstand_kohleschicht_aufbau.svg
:::

Träger ist ein Keramikzylinder, auf den eine dünne Widerstandsschicht aufgedampft wird — Kohlenstoff (Kohleschicht) oder Metalloxid (Metallschicht). Ein Laser schneidet anschliessend eine **Spiralnut** in die Schicht: Der Strom muss den längeren Wendelweg nehmen, was den Widerstand erhöht. Durch Tiefe und Steigung der Nut wird der Endwert auf ±1 % oder besser eingestellt. Metallkappen an beiden Enden kontaktieren die Schicht; eine Schutzlackierung trägt den Farbcode.

:::schematic
/abbildungen/grundlagen/widerstand_metallschicht_aufbau.svg
:::

Metallschichtwiderstände unterscheiden sich von Kohleschicht durch engere Toleranz (±1 % statt ±5 %), niedrigeres Rauschen und bessere Langzeitstabilität.

### Drahtwiderstand

:::schematic
/abbildungen/grundlagen/widerstand_draht_aufbau.svg
:::

Ein Widerstandsdraht (meistens Nickel-Chrom-Legierung, "Nichrome") wird auf einen Keramikträger gewickelt und mit einer Schutzmasse vergossen. Drahtwiderstände können hohe Leistungen aufnehmen (ab 1 W bis mehrere kW mit Kühlkörper) und haben sehr kleine Toleranzen (±0,01 %).

:::warning
Die Wicklung macht den Drahtwiderstand **induktiv** — bei höheren Frequenzen verhält er sich wie eine Spule. Für HF-Anwendungen gibt es bifilar gewickelte Ausführungen (Stromrichtungen heben Induktivität auf).
:::

### SMD-Widerstand (Dickschicht)

:::schematic
/abbildungen/grundlagen/widerstand_smd_aufbau.svg
:::

Auf einem Aluminiumoxid-Substrat (Al₂O₃) wird eine Widerstandspaste aufgedruckt und eingebrannt. Die Metallisierungs-Kappen an den Stirnseiten dienen als Lötflächen. Die Genauigkeit wird — wie beim THT — durch einen Lasereinschnitt in die Dickschicht eingestellt. Dünnschicht-SMD-Widerstände (±0,1 %) verwenden statt Druckpaste eine aufgedampfte Metallschicht.

### Widerstands-Netzwerk (Resistor-Array)

:::schematic
/abbildungen/grundlagen/widerstand_netzwerk_aufbau.svg
:::

Mehrere Widerstände werden in einem gemeinsamen Gehäuse (meist DIP- oder SIP-Bauform mit 6–10 Anschlussbeinchen) zusammengefasst — intern auf einem einzigen Keramiksubstrat als Dickschicht aufgebracht. Typische Schaltungen: isolierte Einzelwiderstände, gemeinsamer Bezugspunkt (Bus-Anordnung) oder Spannungsteiler-Ketten.

:::tip
Widerstands-Netzwerke sparen Platz und Bestückungsaufwand, wenn viele gleiche Werte gebraucht werden — etwa als Pull-up-/Pull-down-Arrays an parallelen Bus-Leitungen (z. B. Daten- oder Adressbus eines Mikrocontrollers).
:::

## Farbcode (THT)

4-Ring-Farbcode für Standard-Widerstände:

| Farbe | Ziffer | Multiplikator | Toleranz |
|---|---|---|---|
| Schwarz | 0 | × 1 | — |
| Braun | 1 | × 10 | ±1 % |
| Rot | 2 | × 100 | ±2 % |
| Orange | 3 | × 1 k | — |
| Gelb | 4 | × 10 k | — |
| Grün | 5 | × 100 k | ±0,5 % |
| Blau | 6 | × 1 M | ±0,25 % |
| Violett | 7 | × 10 M | ±0,1 % |
| Grau | 8 | — | ±0,05 % |
| Weiss | 9 | — | — |
| Gold | — | × 0,1 | ±5 % |
| Silber | — | × 0,01 | ±10 % |

**Beispiel:** Braun-Schwarz-Orange-Gold = 1-0-× 1k ±5 % = 10 kΩ ±5 %

## SMD-Kennzeichnung

3-stellig: Erste zwei Ziffern = Wert, dritte Ziffer = Multiplikator (Anzahl Nullen).

:::monospace
472 → 47 × 10^2 = 4700 Ω = 4,7 kΩ
103 → 10 × 10^3 = 10 000 Ω = 10 kΩ
R10 → 0,10 Ω  (R = Dezimalpunkt)
:::

4-stellig (höhere Präzision): Erste drei Ziffern = Wert, vierte = Multiplikator.

## E-Reihen

Widerstände werden nicht in beliebigen Werten produziert, sondern in normierten **E-Reihen**. Die Reihe gibt an, wie viele Werte pro Dekade existieren:

| Reihe | Werte/Dekade | Toleranz | Verwendung |
|---|---|---|---|
| E6 | 6 | ±20 % | Veraltet |
| E12 | 12 | ±10 % | Allgemein |
| E24 | 24 | ±5 % | Standard |
| E48 | 48 | ±2 % | Präzision |
| E96 | 96 | ±1 % | Präzision |

**E12-Reihe (12 Werte):** 1,0 — 1,2 — 1,5 — 1,8 — 2,2 — 2,7 — 3,3 — 3,9 — 4,7 — 5,6 — 6,8 — 8,2 (dann × 10 weiter)

:::tip
**Toleranzen in Berechnungen:** Soll der Wertebereich einer Grösse berechnet werden, die aus mehreren toleranzbehafteten Bauteilen multiplikativ zusammengesetzt ist (z. B. tau = R · C), müssen die Extremwerte **kombiniert, nicht gemischt** werden:

- Minimalwert: kleinste Faktoren miteinander multiplizieren (R_min · C_min)
- Maximalwert: grösste Faktoren miteinander multiplizieren (R_max · C_max)

Ein Mischen wie R_min · C_max würde keinen real existierenden Bauteilkombination entsprechen und das Ergebnis verfälschen.
:::

## Verlustleistung & Derating

Jeder Widerstand hat eine maximale Verlustleistung P_max (auf dem Datenblatt). Bei höheren Temperaturen muss die Belastung reduziert werden (Derating):

:::merke
Als Faustregel: Im Dauerbetrieb nur **50 % der Nennleistung** nutzen, um Reserven für Temperatur, Alterung und Streuung zu haben.
:::

| Typ | Nennleistung | Maximale Betriebstemperatur |
|---|---|---|
| SMD 0603 | 0,1 W | 70 °C (darüber Derating) |
| THT 1/4 W | 0,25 W | 70 °C |
| THT 1 W | 1 W | 70 °C |
| Hochlastwiderstand | 10–100 W | Mit Kühlkörper |

## Spannungsfestigkeit

Jeder Widerstand hat neben der **Leistungsgrenze** auch eine **maximale Betriebsspannung** (Spannungsfestigkeit). Diese ist unabhängig von der Verlustleistung — die Spannung kann auch bei kleinen Strömen zu hoch werden.

Der Grund: Bei zu hoher Spannung kann der Lichtbogen über die Widerstandsschicht schlagen (besonders bei kleinen SMD-Gehäusen mit kurzem Kriechweg). Zudem kann die elektrische Feldstärke in der dünnen Schicht zur Degradierung führen.

| Gehäuse | Max. Betriebsspannung (typisch) |
|---|---|
| SMD 0402 | 25 V |
| SMD 0603 | 50 V |
| SMD 0805 | 150 V |
| SMD 1206 | 200 V |
| THT 1/4 W | 250 V |
| THT 1 W | 500 V |

:::merke
Nicht nur die Verlustleistung P = U²/R prüfen — auch sicherstellen, dass die Spannung **über** dem Widerstand die Spannungsfestigkeit nicht überschreitet. Bei Hochspannungsschaltungen (z. B. 230 V AC nach Gleichrichten: ca. 325 V Spitze) müssen Widerstände in Reihe geschaltet oder speziell ausgewählte Hochvolt-Typen verwendet werden.
:::

## Vergleichstabelle Widerstandstypen

| Typ | Toleranz | Rauschen | Max. Spannung | Anwendung |
|---|---|---|---|---|
| Kohleschicht | ±5–10 % | Hoch | 250 V | Preiswert, allgemein |
| Metallschicht | ±1 % | Niedrig | 250 V | Präzision, Audio |
| Drahtwiderstand | ±0,01 % | Sehr niedrig | 500 V+ | Präzisionsmessung, Leistung |
| Widerstands-Netzwerk | ±2–5 % | Mittel | 50–100 V | Pull-up/-down-Arrays, Bus-Leitungen |
| SMD Dickschicht | ±1–5 % | Mittel | 50–200 V | Massenproduktion |
| SMD Dünnschicht | ±0,1 % | Niedrig | 50–200 V | Präzision SMD |
