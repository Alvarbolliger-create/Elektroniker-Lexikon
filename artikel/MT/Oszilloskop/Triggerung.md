---
title: Triggerung
kategorie: MT
tags: [triggerung, oszilloskop, flanke, pegel, stabil, flankentrigger, pulstrigger, auto-modus, normal-modus, holdoff, hysterese, single-shot, serielle triggerung, jitter]
symbol: —
einheit: —
---

Die Triggerung hält das Bild auf dem Oszilloskop stabil. Ohne sie läuft das Signal durch. Mit richtiger Triggerung sieht man immer dieselbe Stelle des Signals.

:::hbox
:::vbox
**Voraussetzungen**
- [[Oszilloskop: Aufbau & Bedienung]]
:::
:::vbox
**Führt weiter zu**
- [[Protokoll-Decoder]]
:::
:::

---

## Wie es funktioniert

Das Oszilloskop wartet bis das Signal den eingestellten Triggerpegel und die Triggerflanke (steigend oder fallend) erreicht. In diesem Moment startet die Aufnahme.

Da dasselbe Ereignis immer an derselben Stelle des Signals ist, erscheint das Bild stehend.

## Triggerarten

**Flankentrigger**: Standard. Triggert auf steigende oder fallende Flanke über einem Pegel. Für die meisten Messungen ausreichend.

**Pulstrigger**: Triggert auf Pulse einer bestimmten Breite. Nützlich um zu kurze oder zu lange Pulse zu finden.

**Video-Trigger**: Für PAL/NTSC-Signale.

**Serielle Triggerung**: Triggert auf ein bestimmtes Byte oder Muster in UART, SPI, I2C. Braucht Protokoll-Decoder-Option.

## Auto vs. Normal

**Auto-Modus**: Das Bild läuft auch ohne Trigger. Gut für erste Orientierung.

**Normal-Modus**: Kein Bild ohne Trigger. Das Gerät wartet. Besser für seltene Ereignisse und genaue Messungen.

## Häufige Probleme

Bild läuft: Triggerpegel falsch eingestellt oder falsche Flanke. Lösung: Pegel in die Mitte des Signals setzen.

Bild springt: Signal hat Jitter oder der Triggerpegel liegt in einem rauschenden Bereich. Lösung: Hysterese erhöhen oder Tiefpass-Kopplung verwenden.

:::tip
Trigger-Holdoff verwenden wenn das Signal aus wiederholenden Bursts besteht. Der Holdoff legt eine Mindestzeit zwischen zwei Triggerereignissen fest und verhindert ungewollte Trigger innerhalb des Bursts.
:::
