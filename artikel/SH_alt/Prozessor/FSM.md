---
title: FSM (Zustandsautomat)
kategorie: SH
tags: [FSM, zustandsautomat, moore, mealy, zustandsdiagramm, VHDL, C, state-machine, transition, enum]
symbol: —
einheit: —
---

Ein Zustandsautomat (FSM = Finite State Machine) ist ein Modell das zu jedem Zeitpunkt in genau einem Zustand ist und bei Ereignissen zwischen Zuständen wechselt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops]]
- [[Logikgatter]]
:::
:::vbox
**Verwandte Artikel**
- [[VHDL und Verilog]]
- [[Mikrocontroller]]
:::
:::

---

## Warum FSMs?

Viele Systeme haben klar definierte Zustände: eine Tür ist offen oder zu, eine Ampel zeigt Rot, Gelb oder Grün. Ein FSM macht diese Zustände explizit und verhindert ungültige Zustandskombinationen.

## Moore vs. Mealy

**Moore-Automat**: Der Ausgang hängt nur vom Zustand ab.  
**Mealy-Automat**: Der Ausgang hängt vom Zustand und dem aktuellen Eingang ab.

Moore ist einfacher zu verstehen und zu debuggen. Mealy reagiert schneller (eine Taktperiode früher).

## Zustandsdiagramm

Ein Zustandsdiagramm zeigt:
- Kreise: Zustände (und Moore-Ausgaben)
- Pfeile: Übergänge mit Bedingung / Mealy-Ausgabe

Beispiel Ampel:
- Rot → (Timer abgelaufen) → Rot-Gelb → Grün → Gelb → Rot

## Implementierung in Software

:::monospace
typedef enum { ROT, ROT_GELB, GRUEN, GELB } Ampel_t;
Ampel_t zustand = ROT;

void ampel_update(void) {
    switch (zustand) {
        case ROT:      if (timer_abgelaufen()) zustand = ROT_GELB; break;
        case ROT_GELB: if (timer_abgelaufen()) zustand = GRUEN;    break;
        case GRUEN:    if (timer_abgelaufen()) zustand = GELB;     break;
        case GELB:     if (timer_abgelaufen()) zustand = ROT;      break;
    }
}
:::
## Implementierung in VHDL

Zwei-Prozess-Methode: Ein Prozess für den nächsten Zustand (kombinatorisch), ein Prozess für die Zustandsregister (getaktet).

## Einsatz

FSMs sind in fast jeder digitalen Hardware vorhanden: Protokollcontroller, Befehlsdekoder in CPUs, Schnittstellencontroller, Ampelsteuerungen, Aufzugsteuerungen.
