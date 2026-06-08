---
title: Embedded Linux
kategorie: SH
tags: [linux, embedded, yocto, buildroot, kernel, device tree, raspberry pi, U-Boot, systemd, busybox, RTOS, TCP/IP]
symbol: —
einheit: —
---

Embedded Linux ist ein vollständiges Linux-System auf eingebetteter Hardware. Es bietet Netzwerk, Dateisystem und Prozesskontrolle, braucht aber mehr Ressourcen als ein RTOS.

:::hbox
:::vbox
**Voraussetzungen**
- [[CPU Aufbau]]
- [[Speicherarten]]
- [[Mikrocontroller]]
:::
:::vbox
**Verwandte Artikel**
- [[Device Tree]]
- [[TCP/IP und MQTT]]
:::
:::vbox
**Führt weiter zu**
- [[Device Tree]]
:::
:::

---

## Wann Embedded Linux?

Embedded Linux lohnt sich wenn:
- Netzwerk-Stack mit TCP/IP gebraucht wird
- Dateisystem mit vielen Dateien nötig ist
- Komplexe Anwendungen (Python, Node.js) laufen sollen
- Hardware leistungsfähig genug ist (mind. 64 MB RAM, 128 MB Flash)

Für einfache Steuerungsaufgaben ist ein MCU mit RTOS besser.

## Bootprozess

1. Bootloader (U-Boot) lädt Kernel vom Flash/SD-Karte
2. Kernel initialisiert Hardware, liest Device Tree
3. Erster Prozess (init / systemd) startet
4. Anwendungen starten

## Device Tree

Der Device Tree beschreibt die Hardware für den Kernel: welche Peripherie wo angebunden ist, welche IRQ-Nummern, Taktquellen. Ersetzt hardcodierte Boardkonfigurationen.

## Distributionen für Embedded

**Buildroot**: Minimal, klein, für Produktionssysteme. Vollständige Kontrolle.

**Yocto/OpenEmbedded**: Flexibel, branchenstandard. Lernkurve hoch.

**Raspberry Pi OS**: Fertig, einfach, für Prototypen. Zu gross für Produktion.

**Alpine Linux**: Sehr klein (wenige MB), musl libc.

## Typische Hardware

- Raspberry Pi: CM4 für Produktion, Pi 4 für Prototypen
- i.MX6/8 (NXP): Industriequalität, breite BSP-Unterstützung
- AM335x (TI): BeagleBone-Familie
- Allwinner, Rockchip: Günstig, Community-Support

## Userspace-Entwicklung

Anwendungen laufen im Userspace. Zugriff auf GPIO, SPI, I2C über Kerneltreiber (/dev/spidev, /dev/i2c-*). Shellskripte, Python, C/C++ möglich.
