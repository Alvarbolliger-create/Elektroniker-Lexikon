---
title: Bitmanipulation in der Programmierung
kategorie: SH
kapitel: Grundlagen
tags: [bitoperationen, bitweise verknuepfung, shift, maskierung, datentypen, overflow, signed, unsigned]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)]]
:::
:::vbox
**Verwandte Artikel**
- [[Mikrocontroller]]
:::
:::

---

In der Mikrocontroller-Programmierung (z. B. in C) wird ständig direkt auf einzelne Bits zugegriffen — um Register zu konfigurieren, Pins zu setzen oder Statusflags abzufragen. Dafür stellt die Sprache **bitweise Operatoren** bereit, die Byte für Byte oder sogar Bit für Bit arbeiten.

## Ganzzahlige Datentypen

Bevor man mit Zahlen rechnet, muss man festlegen, wie viele Bits dafür reserviert sind und ob negative Werte vorkommen können:

| Datentyp | Breite | Wertebereich |
|---|---|---|
| `unsigned char` | 8 Bit | 0 … 255 |
| `signed char` | 8 Bit | −128 … +127 |
| `unsigned int` | 16 Bit | 0 … 65 535 |
| `int` | 16 Bit | −32 768 … +32 767 |
| `unsigned long` | 32 Bit | 0 … 4 294 967 295 |
| `long` | 32 Bit | −2 147 483 648 … +2 147 483 647 |
| `float` | — | Fliesskommazahlen, ca. 7 Stellen genau |

:::warning
Wählt man den Datentyp zu klein, tritt bei der Rechnung ein **Overflow** auf — das Ergebnis "passt nicht hinein" und wird stillschweigend falsch. Beispiel: `unsigned char C = 129 + 128;` ergibt nicht 257, sondern 1 (das MSB geht verloren). Abhilfe: einen breiteren Datentyp wählen, z. B. `int` statt `unsigned char`. → [[Binäre Arithmetik (Addition, Subtraktion, Zweierkomplement)]]
:::

## Bitweise Operatoren in C

| Operator | Bedeutung | Wirkung |
|---|---|---|
| `&` | bitweises UND | setzt Bits gezielt auf 0 (maskieren / löschen) |
| `\|` | bitweises ODER | setzt Bits gezielt auf 1 |
| `^` | bitweises EXOR | invertiert gezielt einzelne Bits |
| `~` | bitweise Negation | invertiert alle Bits |
| `>>` | Shift rechts | verschiebt das Bitmuster nach rechts |
| `<<` | Shift links | verschiebt das Bitmuster nach links |
| `&&`, `\|\|`, `!` | logische UND/ODER/Negation | werten den ganzen Operanden als wahr (≠ 0) oder falsch (= 0) |

:::merke
Verwechslungsgefahr: `&` und `|` arbeiten **bitweise** (Bit für Bit, Ergebnis ist eine Zahl), während `&&` und `||` **logisch** arbeiten (das Ergebnis ist immer 0 oder 1 — "ist der ganze Wert ungleich null?"). `0x12 && 0x30` ergibt `1`, `0x12 & 0x30` dagegen `0x10`.
:::

## Gezielt Bits setzen, löschen und abfragen

Die drei klassischen Aufgaben der Bitmanipulation lassen sich mit je einem passenden Operator und einer **Bitmaske** lösen:

:::tip
**Bit setzen** → ODER mit einer 1 an der gewünschten Position: `A = A | 0x80;` setzt Bit 7.

**Bit löschen** → UND mit einer 0 an der gewünschten Position (alle anderen Bits bleiben über 1 erhalten): `A = A & 0xFB;` bzw. lesbarer `A = A & ~0x04;` löscht Bit 2.

**Bit umkehren (toggeln)** → EXOR mit einer 1 an der gewünschten Position: `A = A ^ 0x01;` kehrt Bit 0 um.
:::

Eine kombinierte Aufgabe — *"Bit 7 setzen, Bit 2 löschen, Rest unverändert lassen"* — löst man in einer Zeile:

```c
A = (A | 0x80) & (~0x04);
```

## Schieben (Shift)

Die Shift-Operatoren verschieben das gesamte Bitmuster um eine festgelegte Anzahl Stellen. Frei werdende Stellen werden mit 0 aufgefüllt (bei `unsigned`-Typen).

```c
A = 0x30;        // 0011'0000
B = A >> 3;      // 0000'0110  (Shift right 3 → entspricht Division durch 8)
C = A << 2;      // 1100'0000  (Shift left 2 → entspricht Multiplikation mit 4)
```

:::merke
Ein Schritt nach links entspricht einer Multiplikation mit 2, ein Schritt nach rechts einer (ganzzahligen) Division durch 2 — vorausgesetzt, es geht dabei kein Bit über den Rand verloren.
:::

## Praxisbeispiel: Register konfigurieren

Mikrocontroller-Register fassen oft mehrere unabhängige Einstellungen in einem einzigen Byte zusammen. Eine typische Initialisierung kombiniert mehrere der gezeigten Techniken:

```c
unsigned char A;          // 8-Bit Register
A = (A | 0x80) & (~0x04); // Bit 7 setzen, Bit 2 löschen, restliche Bits unverändert
```

Solche Konstrukte sind die Grundlage für die direkte Hardwareansteuerung — etwa beim Setzen einzelner GPIO-Pins, beim Auslesen von Statusflags oder beim Konfigurieren von Schnittstellen wie [[SPI]] oder [[I2C]] auf einem [[Mikrocontroller]].
