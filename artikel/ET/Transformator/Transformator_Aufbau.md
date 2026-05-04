---
title: Transformator: Aufbau & Funktionsprinzip
kategorie: ET
tags: [transformator, spule, magnetfeld, wechselstrom, übersetzung, galvanische trennung, primär, sekundär, streufluss, kupferverluste, eisenverluste]
symbol: TR
einheit: —
---

Ein Transformator überträgt Wechselenergie magnetisch von einer Spule zur anderen, ohne galvanische Verbindung. Er kann Spannungen hoch- oder heruntersetzen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Spule (Übersicht)]]
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Übersetzungsverhältnis]]
- [[Wirkungsgrad & Verluste]]
:::
:::vbox
**Führt weiter zu**
- [[Übersetzungsverhältnis]]
- [[Netzteile]]
:::
:::

---

## Aufbau

Zwei Wicklungen (Primär und Sekundär) auf einem gemeinsamen Eisenkern. Der Kern konzentriert das Magnetfeld und verbindet die Wicklungen magnetisch.

Primärwicklung: liegt an der Eingangsspannung. Sekundärwicklung: liefert die Ausgangsspannung.

## Funktionsprinzip

Wechselstrom in der Primärwicklung erzeugt ein wechselndes Magnetfeld im Kern. Dieses Feld induziert in der Sekundärwicklung eine Spannung. Mit Gleichstrom funktioniert das nicht.

## Schaltsymbol

Zwei Spulensymbole nebeneinander, verbunden durch zwei vertikale Linien (Eisenkern). Bei Trenntransformator ohne Kern-Linien oder mit gestrichelter Linie.

## Übersetzung

Das Spannungsverhältnis entspricht dem Windungszahlverhältnis.

:::monospace
U1 / U2 = N1 / N2       # Spannungsübersetzung
I1 / I2 = N2 / N1       # Stromübersetzung (umgekehrt)
:::
Mehr Windungen sekundär: Spannung steigt, Strom sinkt. Weniger Windungen: Spannung sinkt, Strom steigt.

## Galvanische Trennung

Primär- und Sekundärkreis sind elektrisch nicht verbunden. Das ermöglicht sichere Isolierung zwischen Netz und Verbraucher und ist Grundlage vieler Sicherheitskonzepte.

:::info
Ein Transformator funktioniert nur mit Wechselstrom. Mit Gleichstrom baut sich kein wechselndes Feld auf. Die Primärwicklung würde im Dauerbetrieb überhitzen.
:::

## Realer Transformator

Ideale Transformatoren gibt es nicht. In der Praxis entstehen zwei Verlustarten:

- **Kupferverluste**: Ohmsche Verluste in den Wicklungen (I² × R). Steigen quadratisch mit dem Strom.
- **Eisenverluste**: Ummagnetisierungs- und Wirbelstromverluste im Kern. Steigen mit der Frequenz.

Ausserdem gibt es **Streufluss**: Ein Teil des Magnetflusses schliesst sich nicht über den Kern, sondern durch die Luft. Das reduziert die Kopplung zwischen Primär- und Sekundärwicklung.

Detaillierte Verlustrechnung und Wirkungsgradberechnung unter [[Wirkungsgrad & Verluste]].
