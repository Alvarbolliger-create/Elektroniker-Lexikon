---
title: AD-Wandler — Auflösung & Fehler
kategorie: SH
kapitel: Wandler
tags: [aufloesung, quantisierungsfehler, lsb, genauigkeit, linearitaetsfehler, fehlerquellen]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[AD-Wandler (Verfahren im Überblick)]]
:::
:::

---

Egal ob Parallel-, Wäge- oder → [[Sigma-Delta-Wandler|Sigma-Delta-Verfahren]]: Kein realer AD-Wandler liefert ein perfektes Abbild seines analogen Eingangssignals. Zwei Eigenschaften bestimmen, wie nahe ein Wandler diesem Ideal kommt — seine **Auflösung** und seine **Fehler**. Beide sind in jedem Datenblatt exakt spezifiziert, und beide zu verstehen ist die Voraussetzung dafür, einen AD-Wandler richtig auszuwählen und seine Messwerte richtig zu interpretieren.

## Die Auflösung: wie fein wird unterteilt?

:::merke
Die **Auflösung** eines AD-Wandlers gibt an, in wie viele "Spannungsstufen" das analoge Eingangssignal zerlegt wird — bestimmt durch die maximale Eingangsspannung U_emax und die Anzahl Bits n: U_LSB = U_emax / 2ⁿ. Ein einfacher Wandler bietet 8 Bit Auflösung (256 Stufen), Industriestandard sind heute häufig 12 Bit (4096 Stufen) — noch feinere Auflösungen sind möglich, aber zunehmend teuer. Jede noch so kleine Spannungsänderung, die kleiner als U_LSB ist, kann der Wandler grundsätzlich **nicht** mehr unterscheiden — dieser unvermeidliche **Quantisierungsfehler** von bis zu ±½ LSB steckt in jedem AD-Wandler, selbst im idealen.
:::

![Quantisierungs-Zeitdiagramm: ein analoges Eingangssignal wird in gleichmässige Stufen (U_LSB) quantisiert; das digitale Ausgangssignal folgt als Treppenfunktion — jede Stufe entspricht einem diskreten Binärcode, der Abstand zwischen zwei benachbarten Stufen ist U_LSB](abbildungen/ad_quantisierung_zeitdiagramm.png)

## Der ideale Wandler — und wovon er abweicht

:::info
Ein idealer AD-Wandler hätte Schalter, die im offenen Zustand unendlich hochohmig und im geschlossenen Zustand widerstandslos (0 Ω) sind, absolut genaue Widerstände, eine driftfreie Referenzspannungsquelle und ideale Operationsverstärker. In der Realität weicht jeder Baustein von diesem Ideal ab — und genau diese Abweichungen lassen sich in drei charakteristische Fehlertypen einteilen, deren Kennlinien sich anhand der Übertragungskennlinie (Code über analoger Eingangsspannung) sauber auseinanderhalten lassen.
:::

## Offsetfehler: die Kennlinie beginnt verschoben

:::tip
Der **Offsetfehler** kennzeichnet eine Verschiebung der gesamten Übertragungskennlinie entlang der Spannungsachse — die Kennlinie beginnt nicht exakt im Punkt (0, 0), sondern erst bei einer von Null verschiedenen Eingangsspannung. Um ihn zu bestimmen, sucht man jenen Punkt, an dem der Wandler vom binären Code 000 auf 001 umschaltet, und rechnet den "schlimmstmöglichen Rundungsfehler" von ½ LSB heraus (Midstep Value): Schaltet der Wandler etwa erst bei 1¾ LSB um, ergibt sich nach Abzug von ½ LSB ein Offsetfehler von 1¼ LSB. Offsetfehler lassen sich in den meisten Schaltungen elektronisch **abgleichen**.
:::

## Verstärkungsfehler: die Kennlinie endet zu früh oder zu spät

:::tip
Der **Verstärkungsfehler** beschreibt das spiegelbildliche Phänomen am oberen Ende der Kennlinie: Der Wandler erreicht den höchsten Binärcode (z. B. 111) bei einer anderen Eingangsspannung, als es die ideale Kennlinie vorsähe. Auch hier wird zur Bestimmung der "schlimmstmögliche Rundungsfehler" von ½ LSB berücksichtigt — diesmal jedoch addiert: Liegt der reale Umschaltpunkt bei 5¾ LSB und der ideale bei 7 LSB, ergibt sich nach Addition von ½ LSB ein Midstep Value von 6¼ LSB und damit ein Verstärkungsfehler von −¾ LSB. Auch der Verstärkungsfehler lässt sich **abgleichen**.
:::

## Linearitätsfehler: der unkorrigierbare Fehler

:::warning
Der **Linearitätsfehler** ist von ganz anderer Natur — und der einzige der drei Fehlertypen, der sich **nicht** abgleichen lässt: Er beschreibt, dass einzelne Stufen der Übertragungskennlinie unterschiedlich breit ausfallen, statt gleichmässig der idealen Geraden zu folgen. Schaltet der Wandler etwa beim Übergang von Code 001 auf 010 schon bei 1¼ LSB um, statt — wie idealerweise — erst bei 1½ LSB, resultiert ein lokaler Fehler von −¼ LSB; beim nächsten Übergang können es −½ LSB sein. Solche Abweichungen treten unregelmässig über die gesamte Kennlinie verteilt auf und lassen sich prinzipbedingt durch keinen globalen Abgleich beseitigen. Die meisten Wandler sind deshalb so ausgelegt, dass ihre Nichtlinearität ±½ LSB nicht überschreitet — sonst würde das niederwertigste Bit praktisch wertlos.
:::

## Alle drei Fehler kombiniert — und das Abtasttheorem als zusätzlicher Stolperstein

:::merke
In der Praxis treten Offset-, Verstärkungs- und Linearitätsfehler stets **in Kombination** auf — die genauen Werte finden sich in den jeweiligen Datenblättern. Ein vierter, oft unterschätzter Faktor kommt hinzu: das → [[Abtasttheorem (Nyquist-Shannon)|Abtasttheorem]]. Wird ein Signal mit höheren Frequenzanteilen "gefüttert", als es die Abtastfrequenz des Wandlers erlaubt, entsteht kein einfacher Messfehler mehr, sondern ein völlig falsches "Phantombild" des Signals — etwa das berüchtigte Aliasing auf dem Bildschirm eines digitalen Oszilloskops, dessen Grenzfrequenz überschritten wurde.
:::

Auflösung, Quantisierungsfehler, Offset-, Verstärkungs- und Linearitätsfehler, dazu die Forderung des Abtasttheorems — wer all diese Faktoren kennt, kann die Kennzahlen jedes beliebigen AD-Wandler-Datenblatts richtig einordnen und das passende Bauteil für die jeweilige Messaufgabe auswählen. Damit schliesst sich der Kreis der Analog-Digital-Wandlung — und es bleibt die spiegelbildliche Frage: Wie verwandelt man eine digitale Zahl wieder zurück in eine analoge Spannung? Die Antwort liefert der → [[DA-Wandler (Digital-Analog-Umsetzer)|DA-Wandler]].
