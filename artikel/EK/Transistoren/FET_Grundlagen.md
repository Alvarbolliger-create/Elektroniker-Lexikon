---
title: FET Grundlagen
kategorie: EK
kapitel: Transistoren
tags: [fet, feldeffekttransistor, mosfet, jfet, gate, source, drain, n-kanal, p-kanal, anreicherungstyp, verarmungstyp, selbstleitend, selbstsperrend, steilheit, esd-empfindlich]
groessen: U_GS|Gate-Source-Spannung|V; I_D|Drainstrom|A; U_DS|Drain-Source-Spannung|V; U_th|Schwellspannung|V; g_m|Steilheit|A/V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Halbleiter Grundlagen]]
- [[BJT Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[BJT Grundlagen]]
- [[IGBT]]
:::
:::vbox
**Führt weiter zu**
- [[FET Sourceschaltung]]
- [[MOSFET Anwendungen]]
:::
:::

---

Der Feldeffekttransistor (FET) wird durch eine Spannung gesteuert, nicht durch einen Strom. Das Gate zieht praktisch keinen Strom — der Eingangswiderstand ist im GΩ-Bereich. Er ist das wichtigste Bauelement in digitalen ICs und modernen Schaltreglern.

## Grundprinzip: Feldsteuerung

Das elektrische Feld am Gate steuert einen leitfähigen Kanal zwischen Drain (D) und Source (S). Je nach Gate-Source-Spannung U_GS verändert sich die Leitfähigkeit des Kanals — und damit der Drainstrom I_D.

| Anschluss | Kürzel | Funktion |
|---|---|---|
| Gate | G | Steuereingang (spannungsgesteuert) |
| Drain | D | Hauptstrom fliesst rein |
| Source | S | Hauptstrom fliesst raus |
| Bulk/Body | B | Substrat (oft intern mit S verbunden) |

## Schaltsymbole

:::hbox
:::vbox
**JFET N-Kanal**
:::schematic
/schaltplaene/symbole/J_N.svg
:::
:::
:::vbox
**JFET P-Kanal**
:::schematic
/schaltplaene/symbole/J_P.svg
:::
:::
:::vbox
**N-MOSFET (Enhancement)**
:::schematic
/schaltplaene/symbole/M_N.svg
:::
:::
:::vbox
**P-MOSFET (Enhancement)**
:::schematic
/schaltplaene/symbole/M_P.svg
:::
:::
:::vbox
**N-MOSFET (Depletion)**
:::schematic
/schaltplaene/symbole/M_N_dep.svg
:::
:::
:::vbox
**P-MOSFET (Depletion)**
:::schematic
/schaltplaene/symbole/M_P_dep.svg
:::
:::
:::

## Typenübersicht

| FET-Typ | Kanal | Leitend ohne Gate-Spannung? | Steuerung | Anwendung |
|---|---|---|---|---|
| JFET N-Kanal | N | Ja (selbstleitend) | Negativspannung sperrt | HF, Verstärker |
| JFET P-Kanal | P | Ja (selbstleitend) | Positivspannung sperrt | Verstärker |
| Depletion MOSFET N | N | Ja (selbstleitend) | Negativspannung sperrt | HF, Ics |
| Depletion MOSFET P | P | Ja (selbstleitend) | Positivspannung sperrt | ICs |
| Enhancement MOSFET N | N | **Nein (selbstsperrend)** | Positivspannung öffnet | Schalter, Verstärker |
| Enhancement MOSFET P | P | **Nein (selbstsperrend)** | Negativspannung öffnet | High-Side Schalter |

**Standard in der Praxis**: N-Kanal Enhancement MOSFET — selbstsperrend (sicher im Ruhezustand), günstiger R_DS(on) als P-Kanal.

## N-Kanal Enhancement MOSFET (Aufbau)

:::schematic MOSFET Querschnitt (N-Kanal Enhancement): p-Substrat (Bulk) unten. Zwei n⁺-Inseln (Source links, Drain rechts). Dünne SiO₂-Schicht (Gate-Oxid) über dem Kanal. Polysilizium-Gate oben. Bei U_GS > U_th bildet sich Inversionskanal (n-leitend) unter dem Oxid zwischen Source und Drain
/Diagramm/mosfet_querschnitt.svg
:::

- **Substrat (Bulk/Body)**: p-dotiertes Silizium
- **Source und Drain**: n⁺-dotierte Inseln im p-Substrat
- **Gate**: Polysilizium, getrennt vom Substrat durch dünne SiO₂-Schicht (Gate-Oxid, 5–100 nm)

Im Gegensatz zum BJT (Stromfluss durch das Volumen) fliesst der Strom beim MOSFET nur an der **Oberfläche** des Substrats.

**Kanalbildung:**

Ohne Gate-Spannung bilden sich an den n⁺-Inseln **Verarmungszonen** (pn-Übergänge Drain-Bulk und Source-Bulk sind gesperrt). Es gibt keinen leitenden Pfad zwischen Drain und Source.

Mit U_GS > U_th zieht das elektrische Feld des Gates Elektronen an die Substratoberfläche. Ab der **Schwellenspannung U_th** (auch V_T oder U_p) liegt starke Inversion vor: Eine n-leitende **Inversionsschicht** bildet sich unter dem Gate-Oxid. Drain und Source sind leitend verbunden — der Transistor leitet.

Die Kanalgeometrie (Breite W, Länge L) bestimmt R_DS(on): breiterer oder kürzerer Kanal = kleinerer Widerstand.

:::warning
Das Gate ist durch die Oxidschicht extrem ESD-empfindlich. Statische Entladung (einige hundert Volt) kann das Oxid irreversibel durchschlagen. Immer mit ESD-Schutz (Erdung, Armband) arbeiten und Gate-Source mit 100 kΩ absichern.
:::

## Kennlinien

:::schematic FET Transferkennlinie (I_D über U_GS): Kurve beginnt bei U_GS = U_th (Schwellenspannung), steigt dann quadratisch an. Steilheit g_m = Steigung der Tangente am Arbeitspunkt. Enhancement-Typ: Kurve beginnt bei U_th > 0 (N-Kanal)
/Diagramm/fet_transferkennlinie.svg
:::

:::schematic FET Ausgangskennlinienfeld (I_D über U_DS): mehrere Kurven für verschiedene U_GS. Ohmscher Bereich links (linearer Anstieg), Sättigungsbereich rechts (konstanter I_D). Grenze Sättigung markiert bei U_DS = U_GS – U_th
/Diagramm/fet_ausgangskennlinien.svg
:::

## Steilheit g_m

Die Steilheit (Transconductance) gibt an, wie stark das Gate den Drainstrom beeinflusst:

:::formel
g_m = ΔI_D / ΔU_GS    # Steilheit in A/V (oder Siemens S)
:::

Je höher g_m, desto mehr Strom kann das Gate mit einer kleinen Spannungsänderung steuern. Im Gegensatz zum BJT (wo g_m = I_C / U_T) hängt g_m beim MOSFET vom Arbeitspunkt und der Geometrie ab.

## FET vs. BJT im Vergleich

| Eigenschaft | BJT | FET (MOSFET) |
|---|---|---|
| Steuerung | Stromgesteuert (I_B) | Spannungsgesteuert (U_GS) |
| Eingangswiderstand | mittel (kΩ) | sehr hoch (GΩ) |
| Steuerstrom | nötig (I_B = I_C/B) | nur Ladestrom beim Schalten |
| Durchlassverluste | U_CE(sat) ≈ 0.3 V | R_DS(on) × I_D (mΩ möglich) |
| Rauschen | höher | tiefer (JFET) |
| Schaltgeschwindigkeit | schnell | sehr schnell |
| Temperaturverhalten | I_C steigt (instabiler) | R_DS(on) steigt (stabiler) |
| Integrierbarkeit | schlecht | sehr gut (CMOS) |

## JFET-Konstantstromquelle

Ein JFET mit Gate direkt an Source (U_GS = 0) liefert einen stabilen Strom I_D = I_DSS. Mit einem Source-Widerstand R_S wird der Strom eingestellt:

:::formel
I_D = U_GS / R_S    # Drainstrom der Konstantstromquelle
:::

Einfache, günstige Konstantstromquelle ohne Regelung — bei niedrigen Genauigkeitsanforderungen ausreichend.
