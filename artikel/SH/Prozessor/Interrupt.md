---
title: Interrupt & Watchdog
kategorie: SH
tags: [interrupt, ISR, polling, watchdog, NVIC, vektortabelle, kontextwechsel, volatile, priorität, ARM, cortex-M, window-watchdog]
symbol: —
einheit: —
---

Ein Interrupt unterbricht das laufende Programm sofort wenn ein Ereignis eintritt. Der Prozessor führt eine kurze Serviceroutine aus und kehrt dann zurück.

:::hbox
:::vbox
**Voraussetzungen**
- [[Mikrocontroller]]
- [[CPU Aufbau]]
:::
:::vbox
**Verwandte Artikel**
- [[Pull-up / Pull-down & Entprellen]]
- [[Bitmanipulation]]
:::
:::vbox
**Führt weiter zu**
- [[DMA (Direct Memory Access)]]
- [[Boot-Vorgang Mikrocontroller]]
:::
:::

---

## Polling vs. Interrupt

**Polling**: Die CPU fragt in einer Schleife ständig ab, ob ein Ereignis eingetroffen ist. Einfach, aber verschwenderisch — die CPU tut nichts Nützliches ausser fragen.

```c
while (1) {
    if (UART_DataAvailable()) {
        byte = UART_Read();
    }
    // CPU ist die ganze Zeit beschäftigt
}
```

**Interrupt**: Das Ereignis meldet sich selbst. Die CPU kann in der Zwischenzeit anderes tun oder schlafen.

```c
// ISR wird automatisch aufgerufen wenn Byte ankommt
void UART_IRQHandler(void) {
    byte = UART_Read();
}

while (1) {
    LowPower_Sleep();   // CPU schläft, verbraucht wenig Strom
}
```

## Ablauf eines Hardware-Interrupts (ARM Cortex-M)

1. Peripherie (Timer, UART, GPIO…) setzt einen Interrupt-Flag
2. Der NVIC (Nested Vectored Interrupt Controller) prüft ob der Interrupt freigegeben und nicht maskiert ist
3. CPU schliesst den aktuellen Befehl ab
4. CPU rettet den Kontext automatisch auf den Stack: PC, PSR, R0–R3, R12, LR
5. CPU liest aus der Vektortabelle die Adresse der ISR
6. CPU springt in die ISR
7. ISR läuft, löscht den Interrupt-Flag am Ende
8. CPU stellt den Kontext vom Stack wieder her (automatisch)
9. Programm läuft weiter ab der unterbrochenen Stelle

## Vektortabelle

Eine Tabelle im Flash-Speicher, die für jeden möglichen Interrupt die Adresse der zugehörigen ISR enthält. Beim ARM Cortex-M beginnt sie bei Adresse 0x00000000.

Eintrag 0: Startwert des Stack-Pointers  
Eintrag 1: Adresse des Reset-Handlers  
Ab Eintrag 2: Exception-Vektoren (NMI, HardFault, …)  
Ab Eintrag 16: Peripherie-Interrupt-Vektoren (herstellerabhängig)

## Prioritäten und NVIC

Der NVIC verwaltet Interrupt-Prioritäten. Ein Interrupt mit höherer Priorität kann eine laufende ISR unterbrechen (Nested Interrupt). ARM Cortex-M unterstützt 8 bis 256 Prioritätsstufen je nach Chip.

```c
NVIC_SetPriority(USART1_IRQn, 2);  // Priorität setzen
NVIC_EnableIRQ(USART1_IRQn);       // Interrupt freischalten
```

## Wichtige Regeln für ISRs

- So kurz wie möglich halten. Kein `delay()`, keine langen Berechnungen.
- Gemeinsame Variablen mit `volatile` deklarieren, damit der Compiler sie nicht wegoptimiert.
- Keine blockierenden Funktionen aufrufen (printf, malloc, ...).

```c
volatile uint8_t new_data = 0;     // volatile: wichtig!

void UART_IRQHandler(void) {
    buffer[idx++] = UART->DR;
    new_data = 1;                   // Flag setzen, Hauptschleife wertet aus
}
```

## Watchdog Timer

Ein Watchdog ist ein unabhängig laufender Timer. Wenn das Programm ihn nicht regelmässig zurücksetzt ("füttert"), löst er einen System-Reset aus.

Zweck: Hänger, Endlosschleifen und Deadlocks in eingebetteten Systemen automatisch beheben.

```c
// Watchdog muss regelmässig getriggert werden
IWDG_ReloadCounter();   // "Füttern" — verhindert Reset
```

### Normaler Watchdog

Wird der Timer nicht innerhalb der Timeout-Zeit gefüttert → Reset. Timeout typisch einstellbar von einigen Millisekunden bis mehrere Sekunden.

### Window-Watchdog

Muss innerhalb eines Zeitfensters gefüttert werden — nicht zu früh, nicht zu spät. Zu frühes Füttern gilt als Fehler und löst ebenfalls einen Reset aus.

Das verhindert, dass ein hängendes Programm zufällig immer genau im falschen Moment füttert. Sicherheitstechnisch strenger als der normale Watchdog.

:::warning
Den Watchdog in der Entwicklung erst zuletzt aktivieren. Während Debug-Sessions kann er unerwartete Resets auslösen.
:::
