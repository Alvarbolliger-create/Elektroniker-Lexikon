---
title: Ausgangstypen (Push-Pull, Open-Collector, Tristate)
kategorie: SH
kapitel: Grundlagen
tags: [push-pull, opencollector, open-drain, tristate, ausgangstreiber, pull-up, hochohmig, iec-symbol, busankopplung]
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)]]
:::
:::vbox
**Verwandte Artikel**
- [[Opencollector & Open-Drain]]
- [[Tristate-Ausgänge]]
:::
:::vbox
**Führt weiter zu**
- [[Bussysteme (Adress-, Daten-, Steuerbus)]]
- [[I2C]]
:::
:::

---

Jeder digitale Ausgang treibt seine Last auf eine von drei grundlegend verschiedenen Arten — je nach Bauweise kann er aktiv High und Low erzeugen, nur Low erzeugen, oder sich vollständig "abkoppeln". Die Wahl des Ausgangstyps bestimmt, ob Ausgänge zusammengeschaltet werden dürfen, ob ein Pull-Up-Widerstand nötig ist und wie sich die Schaltung im Fehlerfall verhält.

## Überblick: die drei Ausgangstypen

:::merke
| Ausgangstyp | High erzeugen | Low erzeugen | Hochohmig | Pull-Up nötig? |
|---|---|---|---|---|
| **Push-Pull** | aktiv (oberer Transistor) | aktiv (unterer Transistor) | Nein | Nein |
| **Open-Collector / Open-Drain** | passiv (über ext. Pull-Up) | aktiv (unterer Transistor) | Nein (ohne Pull-Up: undefiniert) | **Ja** |
| **Tristate** | aktiv | aktiv | **Ja** (dritter Zustand) | Nein |
:::

## Push-Pull

Der häufigste Ausgangstyp: Zwei Transistoren — einer zieht den Ausgang aktiv auf High, der andere aktiv auf Low. Es ist immer genau einer der beiden leitend.

```
V_CC
  |
 [P-Kanal FET]  ← "oberer" Treiber (Pull-Up-Transistor)
  |
  ●── Ausgang
  |
 [N-Kanal FET]  ← "unterer" Treiber (Pull-Down-Transistor)
  |
 GND
```

:::warning
Zwei Push-Pull-Ausgänge dürfen **nie direkt zusammengeschaltet** werden — wenn einer High und der andere Low treibt, entsteht ein Kurzschluss durch V_CC und GND. Für gemeinsame Leitungen → Open-Collector oder → Tristate verwenden.
:::

Das IEC-Symbol eines Ausgangs **mit Treiber** (Puffer/Treiberstufe) zeigt ein Dreieck am Ausgang, das die aktive Treiberfähigkeit symbolisiert. Ein Treiber ohne Invertierung heisst **Buffer (Puffer)**, mit Invertierung **Inverter**.

## Open-Collector / Open-Drain

Der obere Transistor fehlt. Der Ausgang kann nur aktiv auf **Low** gezogen werden — für High sperrt der Transistor einfach, und der Pegel entsteht passiv über einen externen **Pull-Up-Widerstand** nach V_CC.

:::merke
**Berechnungsregel Pull-Up:** Der Widerstand muss gross genug sein, um den Strom im Low-Zustand zu begrenzen, aber klein genug, um den Pegel im High-Zustand sauber auf V_CC zu ziehen. Typisch: 1 kΩ … 10 kΩ.

**Vorteil:** Der Pull-Up kann an einer **anderen Spannung** als die Logik betrieben werden — z. B. 12 V für ein Relais, auch wenn die Logik mit 3,3 V arbeitet.
:::

### Wired-AND durch Zusammenschalten

Mehrere Open-Collector-Ausgänge dürfen direkt zusammengeschaltet werden — ein einziger gemeinsamer Pull-Up genügt:

- Zieht **irgendein** Ausgang auf Low → gemeinsame Leitung = Low
- Nur wenn **alle** sperren → gemeinsame Leitung = High (über Pull-Up)

Das ergibt automatisch eine **UND-Verknüpfung** (Wired-AND), ohne zusätzliche Gatter. Dieses Prinzip nutzt z. B. der → [[I2C]]-Bus (SDA und SCL sind Open-Drain mit Pull-Up).

Mehr Details: → [[Opencollector & Open-Drain]]

## Tristate

Ein Tristate-Ausgang kennt drei Zustände: **High**, **Low** und **hochohmig (Z)**. Im Z-Zustand sperren beide Transistoren gleichzeitig — der Ausgang ist elektrisch "nicht vorhanden" und beeinflusst die Leitung nicht.

Gesteuert wird der Z-Zustand über ein **Enable-Signal (EN)**:

| EN | Ausgangszustand |
|---|---|
| 1 (aktiv) | normaler Betrieb: High oder Low je nach Eingangssignal |
| 0 (inaktiv) | hochohmig (Z) — Ausgang abgekoppelt |

:::merke
Mehrere Tristate-Ausgänge dürfen an dieselbe Leitung — aber es darf **immer nur einer** gleichzeitig aktiv sein (EN = 1). Alle anderen müssen hochohmig geschaltet sein. Diese Bedingung stellt typischerweise eine Adressdekodierlogik sicher. → [[Bussysteme (Adress-, Daten-, Steuerbus)]]
:::

Mehr Details: → [[Tristate-Ausgänge]]

## Vergleich: wann welchen Ausgangstyp?

| Anwendung | Ausgangstyp |
|---|---|
| Normaler Logikausgang, keine Busse | Push-Pull |
| Mehrere Geräte an einer Leitung (I2C, Wired-AND) | Open-Drain / Open-Collector |
| Datenbus (RAM, ROM, Peripherie am Prozessor) | Tristate |
| Last mit anderer Betriebsspannung (Relais, LED mit 12 V) | Open-Collector |
