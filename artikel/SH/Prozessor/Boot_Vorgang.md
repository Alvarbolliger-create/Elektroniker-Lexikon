---
title: Boot-Vorgang Mikrocontroller
kategorie: SH
tags: [boot, reset, power-on-reset, POR, brown-out, BOD, startup, vektortabelle, ARM, cortex-M, watchdog, U-Boot, BSS, stack-pointer]
symbol: —
einheit: —
---

Nach dem Einschalten durchläuft ein Mikrocontroller eine definierte Startsequenz, bevor der Anwendercode läuft. Wer diese Sequenz versteht, kann Startprobleme gezielt debuggen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
- [[CPU Aufbau]]
- [[Interrupt & Watchdog]]
:::
:::vbox
**Verwandte Artikel**
- [[Embedded Linux]]
- [[Device Tree]]
:::
:::

---

## Auslöser eines Resets

Ein Mikrocontroller kann durch verschiedene Ereignisse zurückgesetzt werden:

| Reset-Ursache | Abkürzung | Beschreibung |
|---|---|---|
| Power-on-Reset | POR | Versorgungsspannung steigt von 0 |
| Brown-out Detection | BOD / BOR | Spannung fällt unter Mindestpegel |
| Externer Reset-Pin | NRST / RST | Reset-Pin von aussen auf Low |
| Watchdog-Reset | IWDG / WWDG | Watchdog nicht rechtzeitig gefüttert |
| Software-Reset | SW-Reset | Per Programm ausgelöst |
| LockUp | — | CPU in ungültigem Zustand (Cortex-M) |

## Power-on-Reset (POR)

Der eingebaute POR-Schaltkreis hält den Chip im Reset, bis die Versorgungsspannung stabil über dem Betriebspegel liegt. So startet der Chip nicht in einem undefinierten Zustand.

Typische POR-Schwelle: 1.5–2.5 V für einen 3.3-V-Chip.

## Brown-out Detection (BOD)

Wenn die Spannung während des Betriebs kurz einbricht (z.B. durch einen hohen Strompeak beim Motoranlaufen), erkennt der BOD-Detektor dies und hält den Chip im Reset, bis die Spannung wieder stabil ist.

Ohne BOD kann der Chip bei zu niedriger Spannung mit falschen Werten rechnen — das ist gefährlicher als ein kontrollierter Reset.

## Clock-Startup

Nach dem Reset wartet der Chip, bis der Taktoszillator stabil schwingt:

1. Reset freigegeben
2. Chip läuft intern mit langsamem RC-Oszillator (typisch 8–16 MHz, ungenau)
3. PLL oder externer Quarz wird gestartet
4. Chip wartet bis PLL eingerastet (Clock-Ready-Flag)
5. CPU-Takt auf hohe Frequenz umschalten
6. Anwendercode starten

Die Startup-Zeit des Quarzes kann 1–10 ms dauern. Das ist konfigurierbar.

## Reset-Handler: Die ersten Befehle

Beim ARM Cortex-M lädt die CPU zuerst zwei Werte aus der Vektortabelle (im Flash, ab Adresse 0x00000000):

- Adresse 0x00: Startwert des Stack-Pointers (MSP)
- Adresse 0x04: Adresse des Reset-Handlers

Der Reset-Handler (meist vom Startup-Code der Toolchain bereitgestellt) macht folgendes:

:::monospace
// Vereinfacht: was startup.s macht
1. Stack-Pointer setzen (aus Vektortabelle)
2. BSS-Segment auf 0 initialisieren (globale uninit. Variablen)
3. Data-Segment aus Flash in RAM kopieren (globale init. Variablen)
4. Optional: SystemInit() aufrufen (Clock-Konfiguration)
5. main() aufrufen
:::
## Reset-Ursache lesen

Microcontroller speichern die Reset-Ursache in einem Register. Das erlaubt dem Programm, unterschiedlich zu reagieren:

:::monospace
if (RCC->CSR & RCC_CSR_WDGRSTF) {
    // Watchdog-Reset: Log-Eintrag, sicherer Zustand herstellen
} else if (RCC->CSR & RCC_CSR_PORRSTF) {
    // Power-on: normale Initialisierung
}
RCC->CSR |= RCC_CSR_RMVF;   // Flags löschen
:::
## Startup bei Embedded Linux

Bei einem Linux-System (z.B. Raspberry Pi, STM32MP1) ist die Sequenz länger:

1. ROM-Bootloader (in CPU eingebettet) startet
2. Lädt U-Boot aus Flash/SD-Karte
3. U-Boot initialisiert DRAM, lädt Kernel-Image
4. Kernel startet, initialisiert Treiber (Device Tree)
5. init-Prozess (systemd / BusyBox init) startet
6. Userspace-Dienste und Anwendungen starten
