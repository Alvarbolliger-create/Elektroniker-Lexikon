---
title: DMA (Direct Memory Access)
kategorie: SH
tags: [DMA, busmatrix, CPU, UART, SPI, ADC, speicher, circular, double-buffer, cache, cortex-M, DAC]
symbol: —
einheit: —
---

Der DMA-Controller überträgt Daten direkt zwischen Peripherie und Speicher, ohne die CPU zu belasten. Die CPU gibt den Transfer in Auftrag und kann dann andere Aufgaben erledigen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
- [[CPU Aufbau]]
- [[Speicherarten]]
:::
:::vbox
**Verwandte Artikel**
- [[Interrupt & Watchdog]]
- [[SPI]]
- [[UART]]
:::
:::

---

## Problem ohne DMA: CPU-Polling

Ohne DMA muss die CPU jeden Byte einzeln übertragen:

:::monospace
// UART Empfang ohne DMA
while (bytes_to_receive > 0) {
    while (!UART_RxReady());    // warten
    buffer[i++] = UART_Read();  // Byte lesen
    bytes_to_receive--;
}
// CPU ist die ganze Zeit blockiert
:::
Bei 1 Mbit/s UART und 8-Bit-Daten: 125'000 CPU-Interrupts pro Sekunde, jede mit Overhead. Das schluckt erhebliche CPU-Kapazität.

## DMA-Lösung

Der DMA-Controller übernimmt die Übertragung selbst:

:::monospace
// DMA konfigurieren
DMA_Config.Source = &UART->DR;         // Quelle: UART-Register
DMA_Config.Destination = buffer;        // Ziel: RAM
DMA_Config.Length = 1000;              // 1000 Bytes
DMA_Config.Mode = DMA_CIRCULAR;        // optional: kreisförmig
DMA_Start();

// CPU kann sofort anderes tun
do_other_stuff();

// Interrupt wenn fertig
void DMA_IRQHandler(void) {
    // Alle 1000 Bytes empfangen
    process_buffer();
}
:::
## Architektur: Busmatrix

Moderne Mikrocontroller haben eine Busmatrix — ein Kreuzschalter der mehrere Busse parallel nutzen lässt.

:::schematic
/Diagramm/dma_0.svg
:::
CPU und DMA können gleichzeitig auf den Bus zugreifen, wenn sie auf verschiedene Speicherbereiche zugreifen. Bei Konflikt (beide auf denselben Bus) bekommt DMA meist Vorrang (da zeitkritischer).

## DMA-Transfermodi

**Memory-to-Memory**: Kopieren von Daten innerhalb des RAM. Schneller als memcpy() wenn CPU andere Arbeit hat.

**Peripherie-to-Memory**: ADC-Ergebnis → RAM, UART-Empfang → RAM. Häufigster Fall.

**Memory-to-Peripherie**: RAM → SPI-Transmit, RAM → DAC. Für Ausgabe.

**Circular Mode**: DMA überschreibt den Buffer von vorne, wenn er voll ist. Ideal für Audio-Streaming, kontinuierliche ADC-Messung.

**Double-Buffer Mode**: Zwei Buffer wechseln sich ab. Während CPU den einen Buffer verarbeitet, füllt DMA den anderen.

## DMA-Kanäle und Prioritäten

Ein DMA-Controller hat mehrere Kanäle (typisch 4–16). Jeder Kanal hat:
- Quell- und Zieladresse
- Transfergrösse (Bytes, Halbworte, Worte)
- Priorität (Kanäle konkurrieren um den Bus)
- Interrupt bei Halbfertig, Fertig oder Fehler

## Cache-Kohärenz (wichtig bei Cortex-A)

Bei Mikrocontrollern mit Cache (Cortex-A, Cortex-M7) muss sichergestellt werden, dass der DMA nicht auf gecachte Daten schreibt, ohne den Cache zu invalidieren. Fehlender Cache-Flush führt zu Datenkorruption — ein häufiger Fehler.

:::monospace
// Vor DMA-Transfer: Cache invalidieren
SCB_InvalidateDCache_by_Addr(buffer, size);
:::