---
title: Tristate-Ausgänge
kategorie: SH
kapitel: Logik
tags: [tristate, hochohmiger zustand, dritter zustand, bus, busankopplung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter (UND, ODER, NICHT, NAND, NOR, EXOR)]]
:::
:::vbox
**Verwandte Artikel**
- [[Opencollector & Open-Drain]]
:::
:::vbox
**Führt weiter zu**
- [[Bussysteme (Adress-, Daten-, Steuerbus)]]
:::
:::

---

Ein gewöhnliches Logikgatter kennt nur zwei Ausgangszustände: Low und High. Für **Busankopplungen** reicht das nicht aus — dort müssen sich mehrere Bausteine eine gemeinsame Leitung teilen, ohne sich gegenseitig zu stören. Die Lösung liefert ein dritter Ausgangszustand: **Tristate** (von "drei Zustände").

## Der dritte Zustand: hochohmig (Z)

Neben Low und High kann ein Tristate-Gatter seinen Ausgang zusätzlich **hochohmig** schalten — den sogenannten **Z-Zustand**. In diesem Zustand sperren beide Ausgangstransistoren gleichzeitig, sodass das Gatter elektrisch praktisch "nicht existiert": Es belastet die angeschlossene Leitung nicht und beeinflusst deren Pegel in keiner Weise.

Gesteuert wird dieser Zustand über ein zusätzliches **Enable-Signal (EN)**:

:::merke
Bei einem CMOS-Inverter mit Tristate-Ausgang gilt: Ist EN = High, arbeitet die Schaltung als gewöhnlicher Inverter — der Ausgang folgt normal dem Eingang x. Ist EN = Low, sperren beide Ausgangstransistoren gleichzeitig, der Ausgang y wird **hochohmig** (Z-Zustand). Das Schaltsymbol kennzeichnet einen solchen Ausgang üblicherweise mit einem zusätzlichen Steuereingang "EN" und dem Symbol ∇ am Ausgang.
:::

## Warum Tristate für Busse unverzichtbar ist

Stellen wir uns einen Mikroprozessor vor, an dessen Datenbus ein RAM, ein ROM und ein AD-Wandler angeschlossen sind. Würden alle drei Bausteine gleichzeitig aktiv ihre Daten auf den Bus treiben, käme es zu einem elektrischen Konflikt — die Ausgänge würden sich gegenseitig kurzschliessen.

:::tip
Die Lösung: Von den am Bus angeschlossenen Bausteinen darf zu jedem Zeitpunkt **immer nur einer** aktiv mit dem Mikroprozessor verbunden sein. Während dieser eine Baustein "am Bus hängt" und seine Daten austauscht, werden alle anderen über eine Steuerleitung in den **Tristate-Zustand** versetzt — sie sind für den Bus elektrisch "inexistent" und belasten ihn nicht. Diese Umschaltung übernimmt typischerweise eine Adressdekodierung, die je nach angesprochener Speicheradresse genau ein Enable-Signal aktiviert.
:::

Damit ist der Tristate-Ausgang die Grundvoraussetzung für jedes → [[Bussysteme (Adress-, Daten-, Steuerbus)|Bussystem]], an dem mehrere Sender dieselbe Leitung gemeinsam nutzen — von einfachen Speicherbänken bis zu komplexen Mikroprozessor-Architekturen.

:::info
Eine verwandte, aber andere Lösung für dasselbe Grundproblem bieten → [[Opencollector & Open-Drain|Opencollector-Ausgänge]]: Während Tristate aktiv in den hochohmigen Zustand schaltet, erreichen Opencollector-Schaltungen über einen passiven Pull-Up dieselbe "gemeinsame Leitung"-Fähigkeit auf Wired-AND/Wired-OR-Basis.
:::
