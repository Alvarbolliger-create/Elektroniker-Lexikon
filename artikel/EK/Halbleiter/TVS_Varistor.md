---
title: TVS-Diode & Varistor
kategorie: EK
kapitel: Halbleiter
tags: [tvs, transient voltage suppressor, varistor, mov, überspannungsschutz, transient, esd, surge, klemmspannung, bidirektional, schutzbauelement]
groessen: U_Z|Klemmspannung|V; P_pk|Spitzenleistung|W; C|Kapazität|pF; V_clamp|Klemmspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Zener-Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[Zener-Diode]]
:::
:::vbox
**Führt weiter zu**
- [[EMV-Grundlagen]]
:::
:::

---

TVS-Diode und Varistor schützen Schaltungen vor Spannungsspitzen (Transienten) — Blitzeinschläge, Schaltüberspannungen, ESD. Sie reagieren in Nanosekunden und begrenzen die Spannung auf einen sicheren Wert.

## TVS-Diode (Transient Voltage Suppressor)

Eine TVS-Diode ist eine auf hohe Impulsleistung optimierte Zener-Diode. Sie arbeitet im Lawinendurchbruch und kann Stromspitzen von vielen Ampere für kurze Zeit (< 1 ms) verkraften — ohne sich zu zerstören.

### Unidirektional vs. Bidirektional

| Typ | Schutzrichtung | Anwendung |
|---|---|---|
| Unidirektional | Eine Richtung (wie Zener) | Gleichspannungskreise |
| Bidirektional | Beide Richtungen | Wechselspannung, Datenleitungen |

### Kennwerte

:::formel
U_Z = U_clamp - U_F    # Ungefähre Zenerspannung; U_F ≈ 0.7 V
I_PP = P_pk / U_clamp  # Spitzenstrom bei Klemmspannung
:::

| Kenngrösse | Bedeutung | Typisch |
|---|---|---|
| U_WM | Max. Arbeitsspannung (Standby) | 5–400 V |
| U_clamp | Klemmspannung bei I_PP | 1.1–2× U_WM |
| P_pk | Spitzenleistung (1 ms Impuls) | 400 W – 30 kW |
| C | Kapazität | 0.5 – 1000 pF |

:::warning
Die Kapazität einer TVS-Diode begrenzt die Bandbreite. Auf Hochfrequenz-Datenleitungen (USB3, Ethernet) müssen Niedrigkapazitäts-TVS (< 1 pF) verwendet werden — sonst wird das Signal verzerrt.
:::

### Typische Bauteile

| Typ | U_WM | P_pk | C | Einsatz |
|---|---|---|---|---|
| P6KE6.8A | 5.8 V | 600 W | 2 pF | Gleichspannung |
| SMBJ5.0A | 5.0 V | 600 W | 800 pF | Gleichspannung |
| ESD5Z5.0T | 5.0 V | 200 W | 0.5 pF | USB, Daten |
| SA15A | 15 V | 500 W | 800 pF | 12 V System |

## Varistor (VDR / MOV)

Ein Varistor (MOV = Metal Oxide Varistor, VDR = Voltage-Dependent Resistor) ist ein Widerstand, der bei höherer Spannung stark niederohmig wird. Er besteht aus Zinkoxid-Körnern in einer Keramikmatrix — jede Korngrenze verhält sich wie eine kleine Zener-Diode.

### Unterschied TVS vs. Varistor

| Eigenschaft | TVS-Diode | Varistor |
|---|---|---|
| Reaktionszeit | < 1 ns | 1–25 ns |
| Energie | gering (J) | hoch (J bis kJ) |
| Spannung | präzise (±5 %) | grob (±20 %) |
| Kapazität | 0.5–1000 pF | 100–10'000 pF |
| Anwendung | Elektronik, ESD | Netzanschluss, Blitzschutz |
| Bidirektional | Ja (bidirekt. Typ) | Immer bidirektional |

### Anwendung Varistor

Varistoren schützen Netzgeräte vor Blitz- und Schaltüberspannungen. Typisch: ein MOV parallel zum Netzeingang (nach der Sicherung) begrenzt Spitzen auf < 1.5 × U_Netz.

:::formel
U_varistor > U_netz * √2 * 1.2    # Varistor-Nennspannung muss DC-Spitze + Reserve übersteigen
:::

:::info
Varistoren "altern": Jede Überspannung verringert die Klemmspannung und erhöht die Verlustleistung. Nach vielen Transienten kann ein Varistor im Kurzschluss enden — deshalb immer mit Sicherung oder Thermosicherung absichern.
:::

## Schutzkonzept zusammengefasst

:::schematic Zweistufiger Überspannungsschutz: Netzeingang → MOV (grobe Transienten) → Sicherung/Ferrit → TVS (feine Transienten/ESD) → IC
/Diagramm/tvs_schutzkonzept.svg
:::

Typisch werden beide Bauelemente kombiniert:
1. **MOV** direkt am Netzeingang — begrenzt grobe Überspannungen (kV, kA)
2. **TVS** auf der Platine — schützt einzelne ICs vor restlichen Transienten und ESD

Dazwischen liegt eine Impedanz (Sicherung, Ferrit, Widerstand) die verhindert, dass der MOV den IC-Strom direkt kurzschliesst.
