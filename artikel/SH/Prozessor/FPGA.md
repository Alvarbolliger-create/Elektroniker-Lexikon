---
title: FPGA
kategorie: SH
tags: [FPGA, konfigurierbar, LUT, HDL, VHDL, Verilog, parallele logik, PAL, GAL, CPLD, bitstream, DSP, PLL]
symbol: —
einheit: —
---

Ein FPGA (Field Programmable Gate Array) ist ein konfigurierbarer Chip. Die Logik wird nach der Fertigung durch den Entwickler festgelegt und kann jederzeit geändert werden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter]]
- [[Flipflops]]
:::
:::vbox
**Verwandte Artikel**
- [[VHDL und Verilog]]
- [[CPU Aufbau]]
:::
:::vbox
**Führt weiter zu**
- [[VHDL und Verilog]]
:::
:::

---

## Entwicklung: PAL → GAL → CPLD → FPGA

Programmierbare Logikbausteine haben sich von einfachen zu komplexen Architekturen entwickelt:

| Typ | Struktur | Komplexität | Merkmal |
|---|---|---|---|
| PAL (Programmable Array Logic) | AND-Array fest, OR programmierbar | Einfach (< 100 Gatter) | Einmal programmierbar (OTP) |
| GAL (Generic Array Logic) | AND-Array und OR programmierbar | Einfach | Mehrfach löschbar (EEPROM) |
| CPLD (Complex PLD) | Mehrere PAL/GAL-Blöcke mit Verbindungsmatrix | Mittel (100–10'000 Gatter) | Sofortige Konfiguration |
| FPGA | LUT-basierte Blöcke, flexible Verbindung | Gross (10'000–Millionen LUTs) | Höchste Flexibilität |

**PAL/GAL** eignen sich für einfache Glue-Logic (Adressdekodierung, einfache FSM). FPGAs für komplexe Systeme.

---

## Aufbau

Ein FPGA enthält tausende bis millionen von:

**LUT (Look-Up Table)**: Kleine Wahrheitstabelle die beliebige Logikfunktionen berechnet. Typisch 4-6 Eingänge, 1 Ausgang.

**Flipflops**: Für getaktete Logik und Zustandsmaschinen.

**Verbindungsmatrix**: Programmierbare Verbindungen zwischen LUTs. Das ist der konfigurierbare Teil.

Zusätzlich: DSP-Blöcke (Multiplizierer), Block-RAM, PLLs, High-Speed-Transceiver, I/O-Zellen.

## Konfiguration

Die Konfiguration wird im Bitstream gespeichert. Beim Einschalten wird der Bitstream aus einem externen Flash oder vom Prozessor geladen. Das dauert Millisekunden bis Sekunden.

Einige FPGAs haben internen Flash (z.B. Lattice iCE40).

## Vorteile gegenüber MCU

- **Parallelität**: Alle Logikblöcke arbeiten gleichzeitig. Keine sequentielle Abarbeitung.
- **Determinismus**: Exakte Timing-Kontrolle ohne Interrupt-Latenz
- **Hohe Datenrate**: Mehrere GBit/s parallele Verarbeitung

Anwendungen: Digitale Signalverarbeitung, Protokollkonverter, Echtzeit-Bildverarbeitung, Prototyping von ASICs.

## Nachteile

- Hoher Lernaufwand (HDL, Synthesewerkzeuge)
- Teurer als MCUs gleicher Leistung
- Entwicklungszeit länger

## Einstieg

**Lattice iCE40**: Kleines, günstiges FPGA. Open-Source-Toolchain (Yosys, nextpnr). Ideal zum Lernen.  
**Xilinx Artix-7**: Leistungsfähig, weit verbreitet in der Industrie.  
**Intel (Altera) Cyclone**: Verbreitet in Industrieprojekten.
