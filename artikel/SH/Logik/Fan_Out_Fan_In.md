---
title: Fan-Out & Fan-In
kategorie: SH
kapitel: Logik
tags: [fan-out, fan-in, treiberfaehigkeit, lasteingaenge, durchlaufzeit, zusammenschalten]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikfamilien (TTL, CMOS, BiCMOS, ECL)]]
:::
:::

---

Ein Logikgatter treibt seinen Ausgang nicht "ins Leere", sondern in der Regel mehrere nachfolgende Eingänge gleichzeitig. Wie viele solche Lasten ein Ausgang verkraftet — und wie viele Lasteingänge ein Eingang selbst darstellt — beschreiben die Kenngrössen **Fan-Out** und **Fan-In**.

## Definition

Der **Fan-Out** gibt an, wie viele Eingänge derselben Logikfamilie ein Ausgang gleichzeitig treiben kann, ohne dass die garantierten Pegel- und Stromwerte verletzt werden. Der **Fan-In** beschreibt umgekehrt, wie stark ein Eingang den treibenden Ausgang als "Last" belastet.

:::merke
Der Fan-Out ist durch die maximalen Ausgangsströme I_OH (High-Zustand, fliesst aus dem Gatter heraus) und I_OL (Low-Zustand, fliesst ins Gatter hinein) begrenzt — bezogen auf die Eingangsströme I_IH und I_IL der angeschlossenen Lasten. Wird diese Grenze überschritten, brechen die Ausgangspegel ein und der Störabstand schrumpft (→ [[Schaltpegel & Störabstand]]).
:::

## Treiberfähigkeit verschiedener Logikfamilien

Die Treiberfähigkeit (Drive) hängt stark von der gewählten Logikfamilie ab — Bipolar- und BiCMOS-Familien liefern in der Regel deutlich mehr Strom als reine CMOS-Familien:

| Familie | Technologie | Treiberstrom (I_OL / I_OH) |
|---|---|---|
| LVT | BiCMOS | 64 / −32 mA |
| ALVC | CMOS | 24 / −24 mA |
| AC / ACT | CMOS | 24 / −24 mA |
| AHC | CMOS | 8 / −8 mA |
| LV | CMOS | 8 / −8 mA |
| 74F | Bipolar | 64 / −15 mA |
| BCT | BiCMOS | 64 / −15 mA |
| HC / HCT | CMOS | 6 / −6 mA |
| TTL | Bipolar | 16 / −0.4 mA |

:::tip
Das negative Vorzeichen bei I_OH zeigt an, dass dieser Strom aus dem IC heraus**fliesst** (das Gatter "liefert" Strom an die Last); I_OL hingegen fliesst in das Gatter **hinein**. Besonders bei Backplane-, Bus- und Treiberschaltungen — etwa beim 8-fach-Bustreiber xxx245 — spielt eine hohe Treiberfähigkeit eine grosse Rolle: Bei kapazitiven Lasten sind schnelle Schaltzeiten nur möglich, wenn der Baustein über genügend Drive verfügt, um die Lastkapazität schnell umzuladen.
:::

## Praktische Konsequenzen

Reicht der Fan-Out eines Gatters nicht aus, um alle nachgeschalteten Eingänge sicher zu versorgen, gibt es zwei gängige Lösungen: Entweder schaltet man **Treiberbausteine** (Bus-Treiber, Buffer) zwischen Quelle und Lasten, oder man verteilt die Last auf mehrere parallele Gatterausgänge. Auch die Leitungslänge spielt eine Rolle — lange Leitungen wirken wie zusätzliche kapazitive Lasten und verschlechtern die Flankensteilheit, was wiederum den Einsatz von Gattern mit Schmitt-Trigger-Eingang nötig machen kann.

Fan-Out und Fan-In sind damit, neben Schaltpegel und Störabstand, eines der wichtigsten Kriterien, wenn Logikbausteine **verschiedener** Familien — etwa TTL und CMOS — miteinander kombiniert werden sollen (→ [[Logikfamilien (TTL, CMOS, BiCMOS, ECL)]]).
