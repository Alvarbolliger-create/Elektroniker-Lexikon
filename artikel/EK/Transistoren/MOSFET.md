---
title: FET / MOSFET
kategorie: EK
tags: [MOSFET, FET, transistor, schalter, gate, kanal, enhancement, depletion, JFET, n-kanal, p-kanal, gate-kapazität, RDS_on, schwellspannung, UGS_th, field effect transistor, spannungsgesteuert]
symbol: Q
einheit: —
---

Der MOSFET wird spannungsgesteuert, nicht stromgesteuert wie der BJT. Er ist das wichtigste Schaltelement in modernen Schaltungen, von Mikroprozessoren bis Schaltnetzteilen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Bipolartransistor (BJT)]]
:::
:::vbox
**Verwandte Artikel**
- [[IGBT]]
- [[Als Schalter]]
:::
:::vbox
**Führt weiter zu**
- [[Als Schalter]]
- [[Buck (Step-down)]]
:::
:::

---

## Aufbau und Typen

Drei Anschlüsse: Gate (G), Drain (D), Source (S).

**N-Kanal**: Leitend wenn Gate-Source-Spannung positiv genug ist. Häufigster Typ, meist der bessere Schalter.

**P-Kanal**: Leitend wenn Gate-Source-Spannung negativ genug ist. Einfacher für High-Side-Schalten.

## Schaltsymbol

Drei Anschlüsse mit einer gestrichelten Linie für den Kanal und einem Pfeil der die Kanalrichtung zeigt.

:::hbox
:::schematic N-Kanal Enhancement MOSFET
/schaltplaene/symbole/M_N.svg
:::
:::schematic P-Kanal Enhancement MOSFET
/schaltplaene/symbole/M_P.svg
:::
:::

## Interner Aufbau: N-Kanal Enhancement-MOSFET

Der N-Kanal Anreicherungs-MOSFET (häufigste Bauform) auf Halbleiterebene:

- **Substrat**: p-dotiertes Silizium (p-Substrat)
- **Source und Drain**: zwei n⁺-dotierte Inseln (stark n-dotiert), in das p-Substrat eingebettet
- **Gate**: Metallschicht (oder polykristallines Silizium) über einer dünnen Siliziumdioxid-Isolierschicht (SiO₂, typisch 5–100 nm)
- **Kanal**: der Bereich unter dem Gate zwischen Source und Drain

**Ohne Gate-Spannung**: Zwischen Source und Drain liegen zwei gegeneinander geschaltete PN-Übergänge (n⁺-p und p-n⁺). Der Transistor sperrt.

**Mit Gate-Spannung über Schwellwert U_GS_th**: Das elektrische Feld des Gates zieht Elektronen aus dem p-Substrat an die Oberfläche. Es entsteht eine dünne Inversionsschicht (n-Kanal) — eine leitfähige Verbindung von Source zu Drain. Strom kann fliessen.

```
R_DS_on    # Widerstand im leitenden Zustand (aus Datenblatt)
U_GS_th    # Schwellspannung, ab der der MOSFET leitet (typisch 1-4 V)
```

## Wie er schaltet

Das Gate ist vom Kanal durch die Oxidschicht galvanisch getrennt. Es fliesst **kein** DC-Steuerstrom. Die Steuerspannung U_GS erzeugt das elektrische Feld das den Inversionskanal bildet.

## Warum besser als BJT als Schalter?

Der MOSFET hat keinen Steuerstrom. Der Gate-Treiber muss nur die Gate-Kapazität umladen. Bei hohen Schaltfrequenzen ist das effizienter.

Im Vergleich: BJT braucht dauerhaft Basisstrom. MOSFET braucht Ladung nur beim Umschalten.

:::warning
Das Gate ist durch die Oxidschicht sehr empfindlich gegen statische Entladung (ESD). Nie mit blossen Händen an das Gate fassen ohne ESD-Schutz. Immer Gate-Source mit einem Widerstand (10 bis 100 kΩ) gegen undefinierten Zustand absichern.
:::

## Kenndaten typischer MOSFETs

| Typ | U_DS max | I_D max | R_DS_on | Anwendung |
|---|---|---|---|---|
| 2N7000 | 60 V | 0.2 A | 5 Ω | Logik, Kleinsignale |
| IRLZ44N | 55 V | 47 A | 22 mΩ | Leistungsschalten |
| IRF540 | 100 V | 28 A | 77 mΩ | Schaltnetzteile |

---

## Selbstleitend vs. Selbstsperrend

| Eigenschaft | Enhancement (Anreicherung) | Depletion (Verarmung) |
|---|---|---|
| Ohne Gate-Spannung | **sperrt** | **leitet** |
| Steuerung | Gate-Spannung öffnet Kanal | Gate-Spannung verengt Kanal |
| Häufigkeit | Sehr häufig (Schalter, Verstärker) | Selten (Konstantstromquelle) |
| Abschalten | U_GS = 0 reicht | Negative U_GS nötig |

Enhancement-MOSFETs (selbstsperrend) sind Standard in der Praxis, da sie sicher im stromlosen Zustand sperren.

---

:::info
Der JFET ist ein eigenständiger Transistortyp — kein MOSFET-Untertyp. Er ist ebenfalls spannungsgesteuert, hat aber einen grundlegend anderen Halbleiteraufbau und ist immer selbstleitend.
:::

## JFET (Junction FET)

Der JFET ist ein älterer, selbstleitender FET-Typ. Aufbau: n-dotierter Kanal mit zwei p-dotierten Gate-Bereichen (oder umgekehrt für p-JFET).

**Eigenschaften**:
- Immer selbstleitend: ohne Gate-Spannung fliesst Strom
- Abschalten durch negative U_GS (N-JFET): U_GS_off typisch –1 bis –8 V
- Gate bildet eine PN-Diode zum Kanal → sehr hohe Eingangsimpedanz, aber Gate darf nicht vorwärts leitend sein (U_GS < 0.5 V)
- Kein Oxidgitter → robuster gegen ESD als MOSFET

**Typische Anwendung**: Rauscharme HF-Verstärker, Konstantstromquellen.

```
I_D = I_DSS × (1 - U_GS / U_GS_off)²    # Shockley-Gleichung (Sättigungsbereich)
```

- I_DSS: Drainstrom bei U_GS = 0 (aus Datenblatt)
- U_GS_off: Gate-Spannung bei der der Kanal sperrt (negativ bei N-JFET)

:::info
Unterschied JFET / MOSFET auf einen Blick: JFET hat kein Oxid unter dem Gate, der Kanal ist physisch immer vorhanden (selbstleitend). MOSFET hat Oxid, der Kanal wird elektrisch erzeugt (Anreicherung) oder verringert (Verarmung).
:::
