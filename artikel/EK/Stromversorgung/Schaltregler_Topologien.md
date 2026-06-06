---
title: Schaltregler Topologien
kategorie: EK
kapitel: Stromversorgung
tags: [schaltregler, Sperrwandler, Flusswandler, Flyback, Forward, Gegentakt, Halbbrücke, Vollbrücke, galvanische-Trennung, Transformator, Resonanzwandler, PFC, SNT]
groessen: U_E|Eingangsspannung|V; U_A|Ausgangsspannung|V; D|Tastverhältnis|—; P|Leistung|W
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[DC-DC-Wandler]]
- [[MOSFET Anwendungen]]
- [[Thyristor]]
:::
:::vbox
**Verwandte Artikel**
- [[DC-DC-Wandler]]
- [[Thermomanagement]]
:::
:::vbox
**Führt weiter zu**
- [[Thermomanagement]]
:::
:::

---

Schaltnetzteil-Topologien unterscheiden sich in Leistungsbereich, galvanischer Trennung und Schaltungsaufwand. Der Spick unterscheidet Wandler ohne und mit galvanischer Trennung.

## Topologien ohne galvanische Trennung — Übersicht

Bereits in [[DC-DC-Wandler]] behandelt. Alle Formeln basieren auf dem Tastverhältnis D:

| Wandler | Formel U_A | Spannungsbereich |
|---|---|---|
| Buck (Abwärts) | D · U_E | 0 ≤ U_A ≤ U_E |
| Boost (Aufwärts) | U_E / (1−D) | U_A ≥ U_E |
| Buck-Boost (Invers) | −D/(1−D) · U_E | U_A ≤ 0 |
| SEPIC / Zeta | D/(1−D) · U_E | U_E > 0, U_A positiv |
| Cuk / Doppelinverter | −D/(1−D) · U_E | U_E > 0, U_A negativ |
| Synchronwandler | D · U_E | Bidirektional |

## Topologien mit galvanischer Trennung

Ein Transformator trennt Ein- und Ausgangsseite elektrisch. Pflicht für Netzteile nach Sicherheitsvorschriften.

### Sperrwandler — Fly-Back Converter

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | < 250 W |
| Energieübertragende Elemente | Gekoppelte Speicherdrossel mit Luftspalt |
| Besonderheit | Aufbau wie Transformator, aber mit Luftspalt zur Energiespeicherung (kein gleichzeitiger Energie-Fluss) |

Einfachste Topologie mit galvanischer Trennung. Weit verbreitet in Ladegeräten und kleinen Netzteilen (Handy-Ladegerät, USB-Netzteil).

### Eintaktflusswandler — Forward Converter

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | < 500 W |
| Energieübertragende Elemente | Transformator + zusätzliche Speicherdrossel |
| Besonderheit | Energie fliesst direkt (gleichzeitig) durch Transformator |

### Gegentaktflusswandler — Push-Pull Converter

Zwei Varianten mit unterschiedlichem Leistungsbereich:

| Variante | Leistungsbereich | Schalter |
|---|---|---|
| Halbbrückenflusswandler | 100 W bis 2 kW | S1, S2 (Halbbrücke) |
| Vollbrückenflusswandler | > 300 W bis kW-Bereich | S1–S4 (H-Brücke) |

Transformator überträgt die Energie. Typisch für PC-Netzteile, Industrienetzteile, Motorendstufen.

### Resonanzwandler

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | Einige 10 W bis kW-Bereich |
| Besonderheit | Resonanzkreis (C_R, L_R) ermöglicht ZVS/ZCS (Zero Voltage/Current Switching) → sehr hoher Wirkungsgrad, geringe EMV |

Mit galvanischer Trennung durch zusätzlichen Transformator T_r erweiterbar.

### Brückenloser PFC-Wandler

| Eigenschaft | Wert |
|---|---|
| Leistungsbereich | 10 W bis unterer kW-Bereich |
| Besonderheit | Resonanzkreis aus zwei Kondensatoren und zwei magnetisch gekoppelten Drosseln und Übertrager |

PFC = Power Factor Correction — verbessert den Leistungsfaktor der Netzaufnahme.

## Zerhacker

Der **Zerhacker** ist eine elektromechanische Vorrichtung, die eine Gleichspannung in eine rechteckförmige Wechselspannung umwandelt — damit kann ein Transformator die Spannung transformieren. Historisch vor Halbleiter-Schaltreglern verwendet.

## Topologien-Vergleich

| Topologie | Leistung | Trennung | Aufwand | Typischer Einsatz |
|---|---|---|---|---|
| Buck | bis kW | nein | gering | Punkt-zu-Punkt-Versorgung (MCU, µC) |
| Boost | bis kW | nein | gering | LED-Treiber, PFC-Vorstufe |
| Flyback | < 250 W | ja | mittel | Handy-Ladegerät, USB-Netzteil |
| Forward | < 500 W | ja | mittel | Industrienetzteil |
| Halbbrücke | 100 W – 2 kW | ja | hoch | PC-Netzteil, Servoantrieb |
| Vollbrücke | > 300 W | ja | hoch | Grosse Netzteile, Frequenzumrichter |
| Resonanz | 10 W – kW | ja | sehr hoch | Hochleistungs-Netzteile, ZVS-Schaltungen |

:::tip
Für EFZ-Niveau: Buck und Boost berechnen, Flyback und Forward konzeptuell verstehen. Die galvanisch getrennten Topologien sind hauptsächlich für die Auswahl und das Verständnis von Fertigmodulen relevant.
:::
