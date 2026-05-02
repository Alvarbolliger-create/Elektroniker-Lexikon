---
title: TVS-Diode & Varistor
kategorie: EK
tags: [TVS, Varistor, ESD-Schutz, Transient, Surge, Klemmdiode, MOV]
symbol: —
einheit: V, J
---

TVS-Dioden und Varistoren klemmen Überspannungen und schützen Schaltkreise vor Transienten durch ESD, Blitz oder induktive Schaltvorgänge. Sie unterscheiden sich in Aufbau, Präzision und Energieaufnahme.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[Zener-Diode]]
- [[pn-Übergang]]
:::
:::vbox
**Verwandte Artikel**
- [[ESD-Schutzmassnahmen]]
- [[Snubber-Netzwerk]]
- [[Thyristor]]
:::
:::

---

## TVS-Diode (Transient Voltage Suppressor)

### Aufbau und Funktion

Eine TVS-Diode arbeitet wie eine Z-Diode, ist aber für hohe Impulsströme optimiert. In Sperrrichtung leitet sie bei Überschreitung der Durchbruchspannung (Clamping Voltage) und klemmt die Spannung.

Im Normalbetrieb: sperrt.  
Bei Transient: leitet, klemmt Spannung auf V_clamp, absorbiert Energie.

### Typen

**Unidirektional**: Schützt nur gegen eine Polarität. Geeignet für DC-Signale.

**Bidirektional (±)**: Schützt gegen beide Polaritäten. Für AC-Signale oder wenn die Polarität wechseln kann.

### Wichtige Kennwerte

| Kenngrösse | Bedeutung |
|---|---|
| V_WM (Working Peak Reverse Voltage) | Maximale Betriebsspannung im Normalbetrieb |
| V_BR (Breakdown Voltage) | Spannung beim Leitungsbeginn (bei 1 mA) |
| V_C (Clamping Voltage) | Spannung bei Nennimpulsstrom I_PP |
| I_PP (Peak Pulse Current) | Maximaler Impulsstrom (8/20 µs Puls) |
| P_PPM (Peak Pulse Power) | Maximale Impulsleistung |

### Reaktionszeit

TVS-Dioden reagieren in < 1 ps (praktisch sofort). Keine Trägheit durch Kapazitätsprobleme wie bei Varistoren.

### Kapazität

TVS-Dioden haben eine Kapazität (typisch 5–1000 pF). Für Hochgeschwindigkeitssignale (USB 3.0, Ethernet, HDMI) müssen Low-Capacitance TVS verwendet werden (< 1 pF).

---

## Varistor (MOV – Metal Oxide Varistor)

### Aufbau und Funktion

Ein Varistor besteht aus Zinkoxidkörnern in einer Keramikmatrix. Der Widerstand ist stark spannungsabhängig — bei normaler Spannung ist der Varistor hochohmig, bei Überspannung wird er niederohmig und leitet.

Der Varistor hat kein scharfes Klemmniveau — er hat eine graduelle Kennlinie.

### Vorteile Varistor

- Hohe Energieaufnahme (Joule-Bereich) — viel mehr als TVS
- Günstig
- Bidirektional von Natur aus
- Gut für Netzspannungsschutz (230 V, Blitz-Schutz)

### Nachteile Varistor

- Langsamere Reaktion als TVS (ca. 25 ns)
- Altert bei wiederholten Transienten (Clamping-Spannung sinkt, Leckstrom steigt)
- Ungenauere Klemm-Spannung
- Hohe Kapazität (1–10 nF) — ungeeignet für HF-Signale

---

## Vergleich

| Merkmal | TVS-Diode | Varistor |
|---|---|---|
| Reaktionszeit | < 1 ps | ≈ 25 ns |
| Energieaufnahme | Gering (µJ–mJ) | Hoch (J) |
| Klemmgenauigkeit | Sehr gut | Mittel |
| Kapazität | Klein – mittel | Gross |
| Alterung | Kaum | Ja |
| Typische Anwendung | IC-Schutz, ESD, Datenleitungen | Netzspannungsschutz, Surge |

## Kombinierter Schutz

In der Praxis werden beide kombiniert:
1. Varistor am Netzeingang: Grobe Energie (Blitz, Surge) absorbieren
2. TVS-Diode auf Signalebene: Feine, schnelle Transienten klemmen

IEC 61000-4-2 (ESD) und IEC 61000-4-5 (Surge) definieren Testpulse und Schutzanforderungen.
