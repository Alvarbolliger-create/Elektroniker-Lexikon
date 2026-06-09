---
title: Logikanalysator
kategorie: MT
tags: [logikanalysator, digital, protokoll, timing, UART, SPI, I2C]
symbol: —
einheit: —
---

Ein Logikanalysator zeichnet viele digitale Kanäle gleichzeitig auf. Er zeigt Timing-Verhältnisse und kann Protokolle automatisch dekodieren.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale (Analog, Digital, Binär)]]
- [[Flipflops (SR, D, JK, T)]]
:::
:::vbox
**Verwandte Artikel**
- [[Protokoll-Decoder]]
:::
:::vbox
**Führt weiter zu**
- [[UART]]
- [[SPI]]
- [[I2C]]
:::
:::

---

## Wozu braucht man ihn?

Das Oszilloskop zeigt Signalformen. Der Logikanalysator zeigt Timingbeziehungen vieler Signale gleichzeitig und dekodiert Protokolle direkt.

Ideal für: SPI-Kommunikation debuggen, I2C-Fehler finden, UART-Inhalt lesen, mehrere GPIO-Pins gleichzeitig überwachen.

## Funktionsprinzip

Alle Kanäle werden mit einer hohen Abtastrate abgetastet (typisch 24 MHz bis 500 MHz). Jeder Kanal ist ein Bit: HIGH oder LOW. Das Ergebnis ist eine Zeitlinie aller Kanäle.

## Protokoll-Dekodierung

Gute Logikanalysatoren (und Software wie PulseView oder Saleae Logic) erkennen automatisch UART, SPI, I2C, CAN, 1-Wire und viele weitere Protokolle. Die Daten werden als lesbare Bytes oder Werte angezeigt.

## Typen

**PC-basiert (USB)**: Günstiger Einstieg. Saleae Logic, sigrok-kompatible Geräte (z.B. Cypress FX2-basiert). Software auf dem PC verarbeitet und zeigt an.

**Standalone**: Grosses Display, kein PC nötig. Für Labor und Produktion.

## Einstiegsgeräte

| Gerät | Kanäle | Abtastrate | Protokolle |
|---|---|---|---|
| Logic 8 (Saleae) | 8 | 100 MHz digital | alle gängigen |
| FX2-basierter LA | 8 | 24 MHz | via sigrok |
| DreamSourceLab DSLogic | 16 | 400 MHz | viele |

:::tip
PulseView (Open Source) mit einem günstigen FX2-basierten Logikanalysator ist ein sehr guter Einstieg. Kostet unter 20 CHF und dekodiert die meisten gängigen Protokolle.
:::
