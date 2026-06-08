---
title: Synchrone Zähler
kategorie: SH
kapitel: Flipflop
tags: [synchroner zaehler, vorwaertszaehler, rueckwaertszaehler, schaltungsanalyse, schaltungsentwurf, gleichzeitige taktung]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops (SR, D, JK, T)]]
:::
:::vbox
**Verwandte Artikel**
- [[Asynchrone Zähler]]
:::
:::vbox
**Führt weiter zu**
- [[Zustandsautomaten (FSM)]]
:::
:::

---

Der grosse Nachteil des → [[Asynchrone Zähler|asynchronen Zählers]] ist die "Welle" der Schaltverzögerungen, die sich von Stufe zu Stufe aufsummiert. Der **synchrone Zähler** löst dieses Problem auf elegante Weise: Hier erhalten **alle** Flipflops gleichzeitig denselben Takt — sie kippen folglich exakt im selben Augenblick. Welche Stufe dabei ihren Zustand ändert und welche nicht, entscheidet eine vorgeschaltete **kombinatorische Logik**, die aus den aktuellen Zuständen aller vorhergehenden Stufen berechnet, was die jeweils nächste Stufe als Eingangswert "sehen" soll.

:::merke
**Vorteil** des synchronen Zählers: Da sich keine Laufzeiten aufsummieren, sind deutlich höhere Taktfrequenzen möglich als beim asynchronen Zähler. **Nachteil**: Der Schaltungsaufwand steigt — anstelle einfacher Kettenschaltungen ist für jede Stufe eine individuell berechnete Verknüpfungslogik an den Steuereingängen nötig.
:::

## Schaltungsentwurf: zwei Grundregeln für den dualen Vorwärtszähler

Beim Aufbau eines synchronen dualen Vorwärtszählers mit JK-Master-Slave-Flipflops lassen sich zwei einfache Konstruktionsregeln anwenden:

:::tip
1. Bei einem synchron arbeitenden, dualen Vorwärtszähler werden die Eingänge **J und K bei jedem Flipflop miteinander verbunden** — jede Stufe arbeitet also im Toggle-Betrieb (T-FF-Verhalten), kippt aber nur dann, wenn ihre Verknüpfungslogik dies zulässt.
2. Das **erste** Flipflop erhält an J und K dauerhaft eine logische 1 (reiner Toggle-Betrieb — es kippt bei jedem Takt). Jedes **folgende** Flipflop erhält an seinen J- und K-Eingängen die **UND-Verknüpfung aller Q-Ausgänge der vorhergehenden Stufen** — eine Stufe kippt also nur dann, wenn *alle* niederwertigeren Stufen gerade gleichzeitig auf 1 stehen (also unmittelbar vor ihrem eigenen Überlauf).
:::

Ein 3-Bit-Zähler nach diesem Schema benötigt deshalb genau ein UND-Gatter (für die Verknüpfung von Q0 und Q1 vor dem dritten Flipflop); ein 4-Bit-Zähler ein zweites usw. — die Verknüpfungslogik wächst mit jeder zusätzlichen Stufe um einen weiteren Eingang.

## Synchroner Rückwärtszähler

Auch hier gilt — analog zum asynchronen Fall — eine einfache Umkehrregel:

:::merke
Beim synchronen Rückwärtszähler gelten dieselben Grundregeln wie beim Vorwärtszähler — jedoch bezogen auf die **negierten** Q̄-Ausgänge: Die Verknüpfungslogik jeder Stufe wertet die UND-Verknüpfung der Q̄-Ausgänge aller vorhergehenden Stufen aus. Wie beim asynchronen Zähler gilt auch hier: Die negierten Ausgänge eines Rückwärtszählers verhalten sich wie die normalen Ausgänge eines Vorwärtszählers — ein Rückwärtszähler lässt sich also stets auch als Vorwärtszähler mit invertiert abgegriffenen Ausgängen auffassen (und umgekehrt).
:::

In der Praxis wird diese Bauweise z. B. in einem synchronen 4-Bit-Rückwärtszähler mit asynchronem Clear umgesetzt: Eine Reset-Taste setzt alle Flipflops sofort (unabhängig vom Takt) zurück, während eine zweite Taste den Zähltakt freigibt — der aktuelle Zählerstand wird dabei meist über einen → [[Demultiplexer & Decoder|BCD-zu-7-Segment-Decoder]] auf einer Anzeige sichtbar gemacht.

## Schaltungsanalyse: das Vorgehen in der Praxis

Wer eine gegebene synchrone Zählerschaltung verstehen will, geht systematisch vor: Zunächst werden für jedes Flipflop die an J und K anliegenden Verknüpfungsterme aus der Schaltung abgelesen; anschliessend wird — Takt für Takt — verfolgt, welchen Zustand jedes Flipflop nach der jeweils nächsten aktiven Flanke einnimmt, und das Ergebnis in ein Zeitdiagramm eingetragen. So lässt sich beispielsweise nachweisen, dass eine bestimmte JK-Beschaltung tatsächlich einen sauberen 3-Bit-Dualzähler ergibt, der die Folge 000, 001, 010, … 111, 000 durchläuft.

:::info
Synchrone Zähler sind auch als fertige integrierte Bausteine erhältlich, bei denen sich das Teiler- bzw. Zählverhältnis sogar **programmieren** lässt — ein bekannter Vertreter ist der IC **74167**, dessen Datenblatt die verschiedenen wählbaren Betriebsarten beschreibt.
:::

Aus genau diesem methodischen Vorgehen — Verknüpfungslogik aufstellen, Zeitverhalten analysieren, Schaltung daraus ableiten — entwickelt sich der allgemeine **synchrone Schaltungsentwurf mit der State-Event-Technik**, mit dem sich nicht nur Zähler, sondern beliebige sequenzielle Schaltungen systematisch entwerfen lassen: der Übergang zum → [[Zustandsautomaten (FSM)|Zustandsautomaten]]. Schaltet man eine synchrone Zählerstufe gezielt als reinen Verhältnisteiler, entsteht zudem der → [[Frequenzteiler|synchrone Frequenzteiler]].
