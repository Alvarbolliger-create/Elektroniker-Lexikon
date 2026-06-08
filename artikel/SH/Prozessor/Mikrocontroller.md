---
title: Mikrocontroller
kategorie: SH
kapitel: Prozessor
tags: [mikrocontroller, embedded system, peripherie, gpio, on-chip speicher]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Rechnerarchitekturen (CISC, RISC, DSP)]]
:::
:::vbox
**Führt weiter zu**
- [[Interrupt]]
- [[DMA (Direct Memory Access)]]
- [[Boot-Vorgang]]
:::
:::

---

Im → [[Aufbau eines Mikroprozessorsystems|klassischen Mikroprozessorsystem]] sind CPU, Speicher und Peripherie getrennte Chips, die über den Systembus verbunden werden müssen — Decoder, Memorymap, externe Beschaltung. Packt man stattdessen all diese Bausteine in **ein einziges Gehäuse**, entsteht der **Mikrocontroller** (Single Chip Computer): ein vollständiger, eigenständiger Computer auf einem Chip — das Herzstück praktisch jedes eingebetteten Systems, vom Lichtschalter bis zur Industriesteuerung.

## Was steckt im Gehäuse?

:::merke
Ein Mikrocontroller vereint **CPU-Kern** (vom einfachen 8-Bit-Kern bis zu leistungsfähigen ARM-Cortex-M-Architekturen), **Flash** als nichtflüchtigen Programmspeicher, **SRAM** als flüchtigen Arbeitsspeicher für Variablen und Stack sowie umfangreiche **Peripherie** — Timer, UART, SPI, I2C, ADC, DAC, PWM, DMA — direkt auf einem Chip. Über **GPIO**-Pins (General Purpose I/O) lässt sich jeder Anschluss individuell als digitaler Ein- oder Ausgang konfigurieren. Diese enge Integration ist genau das, was den → [[Aufbau eines Mikroprozessorsystems|"einfachen Mikrorechner"]] zum kompakten, eigenständigen Single-Chip-System macht.
:::

## Verbreitete Familien

Welcher Mikrocontroller zum Einsatz kommt, hängt stark von Anwendung, Budget und gewünschter Peripherie ab:

| Familie | Hersteller | Spannung | Typischer Einstieg |
|---|---|---|---|
| ATmega (AVR) | Microchip | 3,3 / 5 V | Arduino Uno |
| STM32 (ARM Cortex-M) | ST Microelectronics | 3,3 V | Nucleo, "Blue Pill" |
| RP2040 | Raspberry Pi | 3,3 V | Raspberry Pi Pico |
| ESP32 | Espressif | 3,3 V | integriertes WLAN + Bluetooth |
| PIC | Microchip | 1,8 – 5,5 V | Industrieanwendungen |

## Takt, Leistung und Stromsparmodi

Der **Systemtakt** (in MHz oder GHz angegeben) bestimmt direkt, wie viele → [[Befehlszyklus & Maschinencode|Befehlszyklen]] pro Sekunde durchlaufen werden — höherer Takt bedeutet mehr Rechenleistung, aber auch höheren Stromverbrauch. Gerade bei batteriebetriebenen Geräten ist das ein entscheidender Faktor:

:::tip
Moderne Mikrocontroller bieten gestaffelte **Sleep-Modi**, in denen Taktquellen, Peripherie und sogar Teile der CPU gezielt abgeschaltet werden. Im tiefsten Schlafzustand verbrauchen viele MCUs unter 10 µA — ein Gerät kann so monate- bis jahrelang mit einer Knopfzelle auskommen, solange es die meiste Zeit "schläft" und nur kurz für seine eigentliche Aufgabe "aufwacht".
:::

## Entwicklungsumgebung

Programmiert wird typischerweise in C oder C++, übersetzt mit einem auf die jeweilige Architektur zugeschnittenen Compiler (z. B. GCC), in einer integrierten Entwicklungsumgebung (IDE — etwa STM32CubeIDE, Arduino IDE oder PlatformIO). Ein **Debugger** (z. B. J-Link, ST-Link) erlaubt es, das Programm Schritt für Schritt direkt auf dem Chip auszuführen und dabei Register- und Variableninhalte zu inspizieren — unverzichtbar, wenn ein Programm nicht so läuft wie erwartet.

:::info
Für den Einstieg eignet sich das **Arduino-Ökosystem**: eine einfache, gut dokumentierte API, eine riesige Community und unzählige fertige Bibliotheken. Für anspruchsvollere Projekte greifen Profis eher zu **STM32** mit HAL- oder LL-Treibern — das bedeutet zwar eine steilere Lernkurve, dafür aber mehr Kontrolle über die Hardware, Zugriff auf deutlich mehr Peripherie und leistungsfähigere Entwicklungswerkzeuge.
:::

Damit ein Mikrocontroller seine Aufgaben erfüllen kann, muss er nicht nur "rechnen", sondern auch auf Ereignisse aus seiner Umgebung **reagieren** können — sei es ein eintreffendes Datenbyte, ein Tastendruck oder ein Sensorsignal. Wie er das tut, ohne die ganze Zeit in einer Warteschleife zu verharren, zeigt der → [[Interrupt|Interrupt]].
