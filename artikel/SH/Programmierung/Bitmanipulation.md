---
title: Bitmanipulation in C
kategorie: SH
tags: [bitmanipulation, bitmasken, register, C, shift, AND, OR, XOR, volatile, ISR, makro, embedded, GPIO]
symbol: —
einheit: —
---

In der Embedded-Programmierung werden Hardware-Register direkt per Bitmanipulation gesteuert. Einzelne Bits setzen, löschen und abfragen ohne andere Bits zu verändern.

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme]]
- [[Binäre Arithmetik]]
:::
:::vbox
**Verwandte Artikel**
- [[Mikrocontroller]]
- [[Interrupt & Watchdog]]
:::
:::vbox
**Führt weiter zu**
- [[SPI]]
- [[Schieberegister]]
:::
:::

---

## Bitoperatoren in C

| Operator | Name | Beispiel | Ergebnis |
|---|---|---|---|
| `&` | AND (bitweise) | `0b1100 & 0b1010` | `0b1000` |
| `\|` | OR (bitweise) | `0b1100 \| 0b1010` | `0b1110` |
| `^` | XOR (bitweise) | `0b1100 ^ 0b1010` | `0b0110` |
| `~` | NOT (Komplement) | `~0b00001111` | `0b11110000` |
| `<<` | Linksshift | `1 << 3` | `0b00001000` |
| `>>` | Rechtsshift | `0b1000 >> 2` | `0b0010` |

## Bit setzen (auf 1)

```c
register |= (1 << n);   // Bit n setzen, alle anderen unverändert
```

Beispiel: Bit 3 in einem 8-Bit-Register setzen:
```c
PORTB |= (1 << 3);      // Bit 3 = 1, Bits 0-2, 4-7 unverändert
```

## Bit löschen (auf 0)

```c
register &= ~(1 << n);  // Bit n löschen, alle anderen unverändert
```

Beispiel: Bit 5 löschen:
```c
PORTB &= ~(1 << 5);     // Bit 5 = 0, Rest unverändert
```

## Bit abfragen

```c
if (register & (1 << n)) { /* Bit n ist gesetzt */ }
```

Beispiel: Prüfen ob Bit 2 gesetzt ist:
```c
if (PINB & (1 << 2)) {
    // Taste gedrückt
}
```

## Bit toggeln (umschalten)

```c
register ^= (1 << n);   // Bit n umschalten
```

XOR mit 1 dreht ein Bit um. XOR mit 0 lässt es unverändert.

## Mehrere Bits gleichzeitig

```c
// Bits 0, 2 und 4 setzen
register |= (1 << 0) | (1 << 2) | (1 << 4);

// Bits 1 und 3 löschen
register &= ~((1 << 1) | (1 << 3));
```

## Bitfeld lesen und schreiben

Einen Wert in mehreren Bits speichern (z.B. 4-Bit-Wert ab Bit 4):

```c
uint8_t wert = 0b1010;         // 4-Bit-Wert

// Schreiben: Bits 4-7 auf 'wert' setzen
reg = (reg & 0x0F) | (wert << 4);

// Lesen: Bits 4-7 extrahieren
wert = (reg >> 4) & 0x0F;
```

## Lokale vs. globale Variablen

**Lokale Variable**: Existiert nur innerhalb der Funktion. Liegt auf dem Stack. Wird beim Verlassen der Funktion automatisch freigegeben.

```c
void funktion(void) {
    int x = 5;   // lokal: nur hier sichtbar
}
// x existiert hier nicht mehr
```

**Globale Variable**: Existiert die gesamte Programmlaufzeit. Liegt im RAM (BSS/Data-Segment). Für alle Funktionen sichtbar.

```c
int zaehler = 0;   // global: überall sichtbar

void isr(void) {
    zaehler++;     // ISR kann auf globale Variable zugreifen
}
```

:::warning
Globale Variablen, die in ISRs verändert werden, immer als `volatile` deklarieren:
`volatile int zaehler = 0;`
Sonst optimiert der Compiler den Zugriff weg und das Programm verhält sich falsch.
:::

**Statische lokale Variable**: Liegt im RAM wie eine globale, ist aber nur innerhalb der Funktion sichtbar. Behält ihren Wert zwischen den Aufrufen.

```c
void funktion(void) {
    static int aufrufe = 0;   // bleibt erhalten
    aufrufe++;
}
```

## Typische Register-Makros

In Mikrocontroller-Projekten werden häufig Makros verwendet:

```c
#define SET_BIT(reg, bit)    ((reg) |= (1U << (bit)))
#define CLR_BIT(reg, bit)    ((reg) &= ~(1U << (bit)))
#define TGL_BIT(reg, bit)    ((reg) ^= (1U << (bit)))
#define GET_BIT(reg, bit)    (((reg) >> (bit)) & 1U)
```
