---
title: CPU Aufbau
kategorie: SH
tags: [CPU, ALU, register, pipeline, cache, architektur, RISC, CISC, fetch-decode-execute, von-neumann, harvard, PC, opcode]
symbol: —
einheit: —
---

Die CPU (Central Processing Unit) führt Befehle aus. Sie besteht aus wenigen grundlegenden Baugruppen die zusammenarbeiten.

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
- [[Binäre Arithmetik]]
- [[Flipflops]]
:::
:::vbox
**Verwandte Artikel**
- [[Speicherarten]]
- [[FPGA]]
:::
:::vbox
**Führt weiter zu**
- [[Embedded Linux]]
:::
:::

---

## Grundbausteine

**ALU (Arithmetic Logic Unit)**: Rechnet und vergleicht. Addition, Subtraktion, UND, ODER, Shift, Vergleich.

**Register**: Sehr schnelle Speicherzellen direkt in der CPU. 8 bis 32 Register bei modernen Architekturen. Daten müssen in Register geladen werden bevor die ALU sie verarbeiten kann.

**Programmzähler (PC)**: Zeigt auf den nächsten auszuführenden Befehl im Speicher.

**Befehlsdekoder**: Übersetzt den Befehlscode (Opcode) in Steuersignale für alle anderen Einheiten.

**Bus-Interface**: Verbindet die CPU mit Speicher und Peripherie.

## Fetch-Decode-Execute

Jeder Befehl durchläuft drei Schritte:
1. **Fetch**: Befehl aus dem Speicher laden (Adresse aus PC)
2. **Decode**: Befehl interpretieren, Operanden holen
3. **Execute**: ALU rechnet, Ergebnis speichern

Dieser Zyklus wiederholt sich mit jeder Taktperiode.

## Pipeline

Eine Pipeline überlappet die drei Phasen. Während Befehl 1 ausgeführt wird, wird Befehl 2 dekodiert und Befehl 3 geholt. Theoretisch ein Befehl pro Takt statt drei.

Problem: Sprungbefehle (if/else, Schleifen) unterbrechen die Pipeline (Branch Penalty).

## Cache

RAM ist langsamer als die CPU. Cache-Speicher (SRAM direkt auf dem Chip) puffert häufig genutzte Daten. L1-Cache: sehr schnell, sehr klein. L2-Cache: etwas langsamer, grösser.

## RISC vs. CISC

**RISC** (ARM, RISC-V): Wenige, einfache Befehle. Jeder Befehl gleich schnell. Einfachere Pipeline.  
**CISC** (x86): Viele, komplexe Befehle. Ein Befehl kann viele Operationen ausführen. Hardware übersetzt intern in RISC-ähnliche Micro-Ops.

## Harvard- vs. Von-Neumann-Architektur

Der entscheidende Unterschied liegt in der **Bus- und Speicherstruktur**:

**Von-Neumann-Architektur**:
- Ein gemeinsamer Adressraum und Datenbus für Programm und Daten
- CPU kann nur abwechselnd auf Befehle oder Daten zugreifen (Von-Neumann-Flaschenhals)
- Einfacher, flexibler (Programm kann sich selbst modifizieren)
- Typisch: x86-PCs, klassische Mikroprozessoren

```
RAM/Flash ──[gemeinsamer Bus]── CPU
```

**Harvard-Architektur**:
- Getrennte Adressräume und Busse für Programm und Daten
- CPU kann gleichzeitig einen Befehl holen UND auf Daten zugreifen → höherer Durchsatz
- Typisch: Mikrocontroller (AVR, PIC, ARM Cortex-M im Betrieb), DSPs

```
Flash (Programm) ──[Programmbus]──┐
                                   ├── CPU
SRAM  (Daten)    ──[Datenbus]   ──┘
```

**In der Praxis**: Viele moderne ARM-CPUs haben intern Harvard-Architektur (getrennte Caches für Code und Daten), aber einen gemeinsamen Adressraum nach aussen (Modified Harvard). Das gibt ihnen die Einfachheit von Von-Neumann und die Geschwindigkeit von Harvard.
