---
title: Mikrocontroller
kategorie: SH
tags: [mikrocontroller, MCU, CPU, peripherie, GPIO, ADC, embedded, ARM, AVR, STM32, ESP32, RP2040, flash, SRAM, timer, UART, SPI, I2C, PWM, DMA, sleep-modus, interrupt]
symbol: µC
einheit: —
---

Ein Mikrocontroller ist ein vollständiger Computer auf einem Chip. CPU, Speicher, Peripherie und I/O in einem Gehäuse. Er ist das Herzstück der meisten eingebetteten Systeme.

:::hbox
:::vbox
**Voraussetzungen**
- [[CPU Aufbau]]
- [[Speicherarten]]
:::
:::vbox
**Verwandte Artikel**
- [[UART]]
- [[SPI]]
- [[I2C]]
:::
:::vbox
**Führt weiter zu**
- [[Embedded Linux]]
:::
:::

---

## Was ist drin?

**CPU-Kern**: Führt Befehle aus. ARM Cortex-M0 bis M7, AVR, PIC, RISC-V.

**Flash**: Programmspeicher. Nicht flüchtig, behält das Programm ohne Strom.

**RAM (SRAM)**: Arbeitsspeicher für Variablen und Stack. Klein, typisch 2 bis 512 kB.

**Peripherie**: Alles was die CPU unterstützt. Timers, UART, SPI, I2C, ADC, DAC, PWM, DMA.

**GPIO**: General Purpose I/O. Digitale Pins die als Ein- oder Ausgang konfiguriert werden.

## Wichtige Familien

| Familie | Hersteller | Spannung | Einstieg |
|---|---|---|---|
| ATmega (AVR) | Microchip | 3.3 / 5 V | Arduino Uno |
| STM32 (ARM Cortex-M) | ST | 3.3 V | Nucleo, Blue Pill |
| RP2040 | Raspberry Pi | 3.3 V | Pi Pico |
| ESP32 | Espressif | 3.3 V | WLAN + Bluetooth |
| PIC | Microchip | 1.8 bis 5.5 V | Industrie |

## Takt und Leistung

Der Takt (MHz) bestimmt wie viele Befehle pro Sekunde ausgeführt werden. Höherer Takt, mehr Leistung, mehr Stromverbrauch.

Bei batteriebetriebenen Geräten: Sleep-Modi nutzen. Im tiefen Schlaf verbrauchen viele MCUs unter 10 µA.

## Entwicklungsumgebung

IDE (z.B. STM32CubeIDE, Arduino IDE, PlatformIO), Compiler (GCC), Debugger (J-Link, ST-Link). Debugger erlaubt Schritt-für-Schritt Ausführung und Inspektion von Variablen direkt auf dem Chip.

:::tip
Für Einsteiger: Arduino-Ökosystem. Einfache API, grosse Community, viele Bibliotheken. Für Profis: STM32 mit HAL oder LL-Treibern. Mehr Kontrolle, mehr Peripherie, bessere Werkzeuge.
:::
