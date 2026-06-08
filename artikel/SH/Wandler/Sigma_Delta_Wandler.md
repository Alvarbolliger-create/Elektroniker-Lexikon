---
title: Sigma-Delta-Wandler
kategorie: SH
kapitel: Wandler
tags: [sigma-delta-wandler, ueberabtastung, rauschformung, 1-bit-wandler, delta-modulation]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[AD-Wandler (Verfahren im Überblick)]]
:::
:::

---

Während die → [[Sukzessive Approximation (Wägeverfahren)|Sukzessive Approximation]] mit einem mehrstufigen, präzisen DA-Wandler als Vergleichsmassstab arbeitet, geht der **Sigma-Delta-Wandler (Σ-Δ-ADC)** den radikal entgegengesetzten Weg: Er reduziert seinen Analogteil auf das absolut Nötigste — einen einzigen 1-Bit-Komparator — und verlagert die eigentliche "Denkarbeit" vollständig in die digitale Signalverarbeitung. Dieses Prinzip hat in den letzten Jahren einen regelrechten Boom erlebt: Auflösungen von 12 bis 24 Bit bei Abtastraten im Bereich mehrerer hundert Kilohertz sind damit zu vertretbaren Kosten möglich.

## Das Grundprinzip: ein Regelkreis mit nur einem Bit

:::merke
Im Kern des Sigma-Delta-Wandlers steckt ein **1-Bit-ADC**, eingebettet in einen Regelkreis: Am Eingang wird die Differenz ("Sigma") zwischen der anliegenden Analogspannung und der Ausgangsspannung eines 1-Bit-DA-Wandlers gebildet. Diese Differenzspannung läuft auf einen **Integrator**, der sie über die Zeit aufsummiert. Ein nachgeschalteter **Komparator** prüft lediglich das Vorzeichen der Integratorspannung — positiv ergibt eine logische Eins, negativ eine logische Null — und speichert das Ergebnis in einem D-Flipflop. Der Ausgang Q dieses Flipflops steuert wiederum den 1-Bit-DAC: Eine Eins erzeugt z. B. +2,5 V, eine Null −2,5 V. Damit schliesst sich der Regelkreis — die Schaltung "pendelt" sich fortlaufend um die tatsächliche Eingangsspannung ein.
:::

## Der Bitstream: ein digitales Abbild der Analogspannung

Das Ergebnis dieses ständigen Hin- und Herpendelns ist ein serieller **Bitstream** aus Einsen und Nullen — und genau in dessen statistischer Zusammensetzung steckt die gesuchte Information:

:::tip
Liegt am Eingang z. B. eine konstante Spannung von 1 V bei einem Wandlerbereich von −2,5 V bis +2,5 V — das sind 3,5 V über dem unteren Ende des 5-V-Messbereichs, also 70 % des vollen Bereichs —, so erzeugt der Modulator über die Zeit gemittelt **mehr Einsen als Nullen**: Der Bitstream `10111011` enthält sechs Einsen und zwei Nullen, also einen Mittelwert von 6/8 = 0,75 — bereits nahe an den erwarteten 0,7. Je länger der betrachtete Bitstream, desto genauer nähert sich dieser Mittelwert dem tatsächlichen Eingangswert an. Eine Eingangsspannung nahe +2,5 V erzeugt entsprechend überwiegend Einsen, eine Spannung nahe −2,5 V überwiegend Nullen, und 0 V läge in der Mitte — gleich viele Einsen wie Nullen.
:::

## Überabtastung: der Schlüssel zur hohen Auflösung

:::warning
Damit dieses statistische Verfahren überhaupt funktioniert, muss der Bitstream sehr viel schneller erzeugt werden, als es das blosse → [[Abtasttheorem (Nyquist-Shannon)|Abtasttheorem]] verlangen würde — man spricht von **Überabtastung (Oversampling)**. Typischerweise liegt die tatsächliche Abtastrate beim Hundert- bis Tausendfachen der eigentlichen Signalbandbreite. Diese massive Überabtastung "verschmiert" das Quantisierungsrauschen über einen viel grösseren Frequenzbereich (Rauschformung) und macht es so möglich, durch nachfolgende digitale Filterung ein extrem präzises Ergebnis zu gewinnen.
:::

## Vom Bitstream zur fertigen Zahl: das digitale Filter

Der rohe 1-Bit-Bitstream selbst ist noch keine brauchbare Messgrösse — erst ein nachgeschaltetes **digitales Filter** verdichtet ihn zu einer aussagekräftigen Zahl:

:::info
Die Aufgabe des digitalen Filters besteht darin, eine digitale Zahl zu ermitteln, die **proportional zum "Einer-Anteil"** im Bitstream ist — je höher dieser Anteil, desto näher liegt die Eingangsspannung am positiven Ende des Messbereichs. Ein einfaches Modell dafür ist ein Zähler, dessen Enable-Eingang nur dann aktiv ist, wenn im Bitstream gerade eine Eins anliegt: Sein Endstand entspricht damit direkt dem Mittelwert. Aus diesem an sich simplen Prinzip entstehen — je nach gewünschter Auflösung und Geschwindigkeit — die unterschiedlichsten, teils sehr aufwendigen digitalen Filterarchitekturen, die den grössten Teil des Schaltungsaufwands eines Sigma-Delta-Wandlers ausmachen.
:::

## Der Zielkonflikt: Auflösung gegen Geschwindigkeit

Wie bei jedem AD-Wandler gilt auch hier: Mehr Genauigkeit kostet Zeit. Der Zusammenhang zwischen Bitstream-Länge, Taktfrequenz, Auflösung und Wandlungsgeschwindigkeit lässt sich konkret beziffern:

| Clock | Bitstrom-Länge | Auflösung | Wandlungszeit | Wandlungen/s |
|---|---|---|---|---|
| 10 MHz | 10'000 | 13,3 Bit | 1 ms | 1 ksps |
| 10 MHz | 1'000'000 | 19,9 Bit | 100 ms | 10 sps |
| 20 MHz | 10'000 | 13,3 Bit | 0,5 ms | 2 ksps |
| 20 MHz | 16'777'214 (24 Bit) | 23,3 Bit | ≈ 839 ms | ≈ 1,2 sps |

Wer also die volle 24-Bit-Auflösung ausschöpfen will, muss sich mit gut einer Messung pro Sekunde begnügen — Sigma-Delta-Wandler sind damit prädestiniert für **langsame, aber hochpräzise** Messaufgaben wie Waagen, Temperatursensorik oder Audiotechnik, nicht aber für schnelle Echtzeitanwendungen.

Damit zeigt sich: Wo das Parallelverfahren auf rohe Geschwindigkeit und das Wägeverfahren auf einen ausgewogenen Mittelweg setzt, gewinnt der Sigma-Delta-Wandler seine Präzision aus einem cleveren Zusammenspiel von extrem einfacher Analogtechnik und aufwendiger digitaler Nachbearbeitung — ein Tausch von Hardwareaufwand gegen Rechenzeit. Wie genau sich die Güte eines AD-Wandlers — gleich nach welchem Verfahren er arbeitet — quantitativ fassen lässt und welche Fehlerquellen seine reale Kennlinie von der idealen abweichen lassen, vertieft der Artikel → [[AD-Wandler — Auflösung & Fehler|AD-Wandler: Auflösung und Fehler]].
