---
title: Oszilloskop: Aufbau & Bedienung
kategorie: MT
tags: [oszilloskop, messen, signal, zeitbereich, triggerung]
symbol: —
einheit: —
---

Das Oszilloskop zeigt Signale über die Zeit. Es macht sichtbar was das Multimeter nicht zeigt: Flanken, Rauschen, Störungen, Frequenz und Zeitverhalten.

:::hbox
:::vbox
**Voraussetzungen**
- [[Signale]]
- [[Sinuswellen]]
:::
:::vbox
**Verwandte Artikel**
- [[Triggerung]]
- [[Tastkopf 1:1 vs. 10:1]]
:::
:::vbox
**Führt weiter zu**
- [[Protokoll-Decoder]]
:::
:::

---

## Die wichtigsten Bedienelemente

**Volt/Div**: Skalierung der Vertikalachse. Einen grösseren Wert wählen wenn das Signal abgeschnitten wird, kleiner für mehr Detail.

**Time/Div**: Skalierung der Zeitachse. Kleiner für schnelle Signale, grösser für langsame.

**Trigger**: Definiert den Startpunkt der Aufnahme. Ohne Trigger läuft das Bild davon.

## Triggerung

Der Trigger hält das Bild stabil. Er startet die Aufnahme wenn das Signal einen definierten Pegel und eine Flanke (steigend oder fallend) erreicht.

Bei periodischen Signalen immer auf die Signalfrequenz und Pegel einstellen.

## Tastkopf

Verbindet das Gerät mit dem Messobjekt. Der Massehaken (Krokodilklemme) muss immer angeschlossen sein. Ohne Masse keine korrekte Messung.

Mehr dazu unter [[Tastkopf 1:1 vs. 10:1]].

## AC- und DC-Kopplung

Der Eingang des Oszilloskops kann auf **DC-Kopplung** oder **AC-Kopplung** eingestellt werden:

**DC-Kopplung**: Das Signal wird direkt gemessen — inklusive Gleichspannungsanteil. Was auf der Leitung ist, sieht man auf dem Schirm. Richtige Wahl für:
- Gleichspannungsmessungen
- Signale auf einem DC-Offset (z.B. PWM bei 3.3 V)
- Einschaltverhalten, Transienten

**AC-Kopplung**: Ein Kondensator am Eingang blockiert den Gleichspannungsanteil. Nur der Wechselanteil ist sichtbar. Richtige Wahl für:
- Kleine Wechselsignale auf grossem DC-Offset (z.B. Rauschen auf einer 12-V-Versorgung)
- Wenn man nur die Signalform ohne DC-Versatz betrachten will

:::warning
Mit AC-Kopplung kann man den Trigger auf 0 V setzen und das Signal stabil darstellen, auch wenn der DC-Offset unbekannt ist. Aber: Niedrige Frequenzen werden gedämpft (Hochpass-Verhalten des Koppelkondensators). Für Signale unter ~10 Hz lieber DC-Kopplung mit manuellem Offset.
:::

## Bandbreite

Die Bandbreite des Oszilloskops (z.B. 100 MHz) gibt an, bis zu welcher Signalfrequenz die Amplitude noch auf 70.7 % (−3 dB) des Wahrwerts angezeigt wird.

:::monospace
Faustregel: Bandbreite ≥ 5× Signalfrequenz    # für genaue Signalform
:::
Ein 100-MHz-Oszilloskop für ein 20-MHz-Signal ist gut. Für ein 80-MHz-Signal wird die Amplitude bereits leicht verfälscht dargestellt.

## Sicherheit: Kein Messen direkt am 230-V-Netz

Ein netzbetriebenes Oszilloskop hat die **Masseklemme des Tastkopfs intern mit dem Schutzleiter (PE) verbunden**.

Wenn man den Massehaken an einen Punkt klemmt, der nicht GND ist (z.B. die Nettoader einer Schaltung), verbindet man diesen Punkt über das Gerät mit PE — **kurzschlussartig**. Das kann:
- Bauteile der Messstrecke zerstören
- Den Messkreis beschädigen
- Im schlimmsten Fall lebensgefährlich sein

:::warning
Niemals mit dem Standard-Tastkopf eines netzgebundenen Oszilloskops direkt an 230 V AC messen. Für solche Messungen werden **Differenz-Tastköpfe** (hochspannungsgeeignet) oder **isolierte Eingänge** (Handoszilloskop mit Batterie) verwendet.
:::

## Was zeigt das Multimeter nicht?

Kurze Spannungsspitzen (Glitches), Einschwingvorgänge beim Einschalten, Signalform, Phasenversatz zwischen zwei Signalen, digitale Protokolle.

:::tip
Wenn eine Schaltung seltsam funktioniert und das Multimeter nichts zeigt: Oszilloskop anschliessen. Oft sieht man sofort das Problem, z.B. eine Schwingung im Regler oder eine gestörte Versorgungsspannung.
:::

## Kennwerte beim Kauf

| Grösse | Einsteiger | Professionell |
|---|---|---|
| Bandbreite | 50 bis 100 MHz | 200 MHz bis 1 GHz |
| Kanäle | 2 | 2 bis 4 |
| Abtastrate | 1 GSa/s | 5 GSa/s |
| Speichertiefe | 10 kPkt | 100 MPkt |
