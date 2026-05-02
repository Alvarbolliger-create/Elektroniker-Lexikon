---
title: Fehlerbilder Löten
kategorie: FT
tags: [löten, fehler, kalte lötstelle, lötbrücke, IPC, qualität, tombstoning, nicht-benetzung, 0402, entlötlitze, sichtprüfung]
symbol: —
einheit: —
---

Schlechte Lötstellen sind eine häufige Ursache für Fehler in Elektronik. Viele davon sind mit dem Auge erkennbar, bevor das Gerät eingeschaltet wird.

:::hbox
:::vbox
**Voraussetzungen**
- [[Weichlöten]]
- [[IPC-Kriterien]]
:::
:::vbox
**Verwandte Artikel**
- [[Weichlöten]]
:::
:::vbox
**Führt weiter zu**
- [[PCB Aufbau & Material]]
:::
:::

---

## Kalte Lötstelle

**Aussehen**: Matt, körnig, rau. Manchmal mit sichtbaren Rissen.

**Ursache**: Pad oder Anschlussdraht nicht heiss genug beim Löten. Lot hat sich nicht metallisch verbunden.

**Wirkung**: Schlechte oder keine elektrische Verbindung. Oft intermittierend, schwer zu finden.

**Behebung**: Erneut erhitzen mit sauberer Spitze, bei Bedarf frisches Lot zugeben.

## Lötbrücke

**Aussehen**: Lot verbindet zwei benachbarte Pads oder Pins die nicht verbunden sein sollen.

**Ursache**: Zu viel Lot, zu wenig Abstand, falsch gerichtetes Lot.

**Wirkung**: Kurzschluss. Kann Bauteile oder die ganze Schaltung zerstören.

**Behebung**: Entlötlitze oder Entlötpumpe verwenden. Alternativ mit dem Kolben wegwischen und Reste mit Litze entfernen.

## Nicht-Benetzung

**Aussehen**: Lot sitzt als Kugel auf dem Pad, verbindet sich nicht.

**Ursache**: Oxidiertes Pad oder Bauteil, zu wenig Flussmittel, verschmutzte Lötspitze.

**Behebung**: Fläche reinigen, Flussmittel zugeben, erneut löten.

## Zu viel Lot

**Aussehen**: Grosse Lotmengen, Pad komplett verdeckt, keine Bauteilform erkennbar.

**Wirkung**: Erhöhtes Kurzschlussrisiko, schlechte Wärmeableitung.

## Tombstoning (SMD)

**Aussehen**: Ein SMD-Bauteil steht auf einem Ende auf, das andere Pad ist nicht verbunden.

**Ursache**: Ungleiche Erwärmung der beiden Pads beim Reflowlöten. Ein Pad lötet sich zuerst und zieht das Bauteil hoch.

**Typisch bei**: Kleinen Bauteilen wie 0402 und 0201.

:::tip
Nach dem Löten immer Sichtprüfung unter guter Beleuchtung, besser unter Lupe. Bei SMD-Bauteilen hilft Durchlicht von unten um Brücken zu sehen.
:::
