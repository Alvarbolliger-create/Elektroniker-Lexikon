---
title: Pull-up / Pull-down & Entprellen
kategorie: SH
tags: [pull-up, pull-down, entprellen, debouncing, taster, eingang, floating, schmitt-trigger, ISR, timer, widerstand]
symbol: —
einheit: —
---

Digitale Eingänge brauchen einen definierten Pegel. Ohne Beschaltung schwimmt ein offener Eingang zwischen High und Low — das Ergebnis ist unvorhersehbar.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter]]
- [[Signale]]
:::
:::vbox
**Verwandte Artikel**
- [[Flipflops]]
- [[Mikrocontroller]]
:::
:::vbox
**Führt weiter zu**
- [[Interrupt & Watchdog]]
- [[Bitmanipulation]]
:::
:::

---

## Floating-Eingang

Ein nicht angeschlossener oder hochohmiger Eingang hat keinen definierten Pegel. Er reagiert auf Einstrahlung, Leitungskapazitäten und Leckströme. Das Ergebnis ist zufällig High oder Low.

Das ist ein häufiger Anfängerfehler: Taster ohne Widerstand anschliessen.

## Pull-up-Widerstand

```
VCC --- R --- Eingang --- Taster --- GND
```

Im Ruhezustand liegt der Eingang auf High (wird durch R auf VCC gezogen). Wenn der Taster gedrückt wird, zieht er den Eingang auf GND (Low).

Logik: nicht gedrückt = 1, gedrückt = 0 (invertierte Logik).

Typischer Wert: 4.7 kΩ bis 10 kΩ. Zu klein: viel Strom. Zu gross: langsames Aufladen parasitärer Kapazitäten.

## Pull-down-Widerstand

```
VCC --- Taster --- Eingang --- R --- GND
```

Im Ruhezustand liegt der Eingang auf Low. Wenn der Taster gedrückt wird, zieht er den Eingang auf High.

Logik: nicht gedrückt = 0, gedrückt = 1 (normale Logik).

## Interne Pull-ups (Mikrocontroller)

Die meisten Mikrocontroller haben interne Pull-up-Widerstände. Per Software aktivierbar:

```c
// AVR (Arduino)
pinMode(pin, INPUT_PULLUP);

// STM32 HAL
GPIO_InitStruct.Pull = GPIO_PULLUP;
```

Typischer interner Wert: 20 kΩ bis 50 kΩ. Für lange Leitungen oder schnelle Signale besser extern und kleiner dimensionieren.

## Prellen (Contact Bounce)

Mechanische Schalter und Taster prellen: die Kontakte öffnen und schliessen mehrmals in schneller Folge, bevor sie stabil liegen. Dauer: wenige Millisekunden.

Ohne Entprellung wertet die Logik mehrere Flanken aus, obwohl der Benutzer nur einmal gedrückt hat.

## Entprellen Hardware

**RC-Glied + Schmitt-Trigger**:

```
Taster --- R (10 kΩ) --- C (100 nF) --- Schmitt-Trigger-Eingang
```

Das RC-Glied glättet die Prellimpulse. Der Schmitt-Trigger erzeugt saubere Flanken mit Hysterese.

Zeitkonstante: `τ = R × C = 10 kΩ × 100 nF = 1 ms`

## Entprellen Software

Einfachste Methode: Nach dem Erkennen einer Flanke kurz warten, dann nochmals einlesen.

```c
if (taste_gedrückt()) {
    delay_ms(20);               // Prellzeit abwarten
    if (taste_gedrückt()) {     // jetzt stabil lesen
        // Aktion ausführen
    }
}
```

Bessere Methode: Zustandszähler in der Timer-ISR, alle 1 ms den Eingang einlesen. Erst nach N gleichen Werten den Zustand wechseln.

```c
// In Timer-ISR (alle 1 ms)
if (GPIO_Read(TASTE)) {
    if (debounce_cnt < 20) debounce_cnt++;
} else {
    if (debounce_cnt > 0) debounce_cnt--;
}
taste_stabil = (debounce_cnt >= 20);
```

:::tip
Für einfache Projekte reicht SOFTWARE-Entprellung mit delay. Für zeitkritische Anwendungen oder viele Tasten besser Hardware-Entprellung oder Zähler in der Timer-ISR.
:::
