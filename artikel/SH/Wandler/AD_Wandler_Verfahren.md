---
title: AD-Wandler (Verfahren im Überblick)
kategorie: SH
kapitel: Wandler
tags: [ad-wandler, parallelverfahren, flash-adc, zaehlverfahren, kompensationsverfahren, rampenverfahren, kaskadenverfahren, prioritaetsdecoder]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Sample & Hold-Schaltung]]
- [[Abtasttheorem (Nyquist-Shannon)]]
:::
:::vbox
**Führt weiter zu**
- [[Sukzessive Approximation (Wägeverfahren)]]
- [[Sigma-Delta-Wandler]]
:::
:::

---

Die Natur "denkt" analog — Temperatur, Druck, Helligkeit, Schalldruck verlaufen kontinuierlich. Digitale Systeme dagegen rechnen ausschliesslich mit Zahlen. Damit die beiden Welten zueinanderfinden, braucht es einen **Analog-Digital-Wandler (ADC)**: Er bildet eine analoge Eingangsspannung U_e auf eine digitale Zahl Z ab — dargestellt durch das DIN-Normsymbol "∩/#". Das von der → [[Sample & Hold-Schaltung|Sample & Hold-Schaltung]] bereitgestellte, "eingefrorene" Signal lässt sich auf ganz unterschiedliche Arten in eine Zahl verwandeln.

## Das Parallelverfahren (Flash-ADC): blitzschnell, aber aufwendig

:::merke
Beim **Parallelverfahren** wird die Eingangsspannung U_e gleichzeitig an alle Komparatoren eines abgestuften Spannungsteilers angelegt. Jeder Komparator k_i vergleicht U_e mit seiner eigenen, um jeweils 1 LSB versetzten Schaltschwelle (z. B. 0,5 · U_LSB, 1,5 · U_LSB, 2,5 · U_LSB, …) — ist U_e grösser als die Schwelle, schaltet der Ausgang auf High. So entsteht ein "Thermometer-Muster" aus High- und Low-Pegeln, das in D-Flipflops zwischengespeichert und von einem **Prioritätsdecoder** in eine Binärzahl umgewandelt wird. Bei einem 3-Bit-Wandler mit U_Ref = 7 V beträgt der Schaltschwellenabstand U_ΔKomparator = U_Ref / (7 · R) = 1 V — der Komparator k₁ schaltet bereits bei 0,5 V, k₇ erst bei 6,5 V.
:::

:::warning
Das Parallelverfahren ist durch seine reine Parallelverarbeitung extrem **schnell** — es eignet sich für Wandlungszeiten unter einer Mikrosekunde. Der Preis dafür ist ein enormer Hardwareaufwand: Für eine Auflösung von n Bit werden 2ⁿ − 1 Komparatoren benötigt — bei nur 10 Bit Auflösung sind das bereits 1023 Komparatoren auf einem einzigen Chip!
:::

## Das Zählverfahren: einfach, aber langsam

Eine ganz andere Philosophie verfolgen die **Zählverfahren** — sie nähern sich dem gesuchten Wert schrittweise an, anstatt ihn auf einen Schlag zu bestimmen:

:::tip
Beim **Kompensationsverfahren** (Nachlaufverfahren) vergleicht ein Komparator die Eingangsspannung U_e mit der Ausgangsspannung U(Z) eines internen → [[DA-Wandler (Digital-Analog-Umsetzer)|DA-Wandlers]]. Ist U_e grösser, zählt ein Vorwärts-/Rückwärtszähler aufwärts — die DA-Wandlerspannung steigt mit; ist U_e kleiner, zählt er abwärts. Diese Schaltung bildet einen **Regelkreis**: Der Zählerstand pendelt sich dauerhaft um U_e ein und liefert dabei laufend ein aktuelles Resultat — praktisch für sich nur langsam ändernde Signale, allerdings mit Wandlungszeiten von 1 ms bis zu einer Sekunde entsprechend träge.

Beim **Ein-Rampen-Verfahren (Single Slope)** erzeugt ein Sägezahngenerator eine kontinuierlich ansteigende Referenzspannung. Ein Zähler läuft so lange mit, wie diese Rampe unterhalb von U_e liegt — sobald sie U_e übersteigt, stoppt der Zähler, und sein Stand entspricht der gesuchten Zahl. Der Vorteil: Es wird **kein** DA-Wandler benötigt. Der Nachteil: Die Genauigkeit hängt empfindlich von der Stabilität des Sägezahngenerators ab — Temperaturdrift und Alterung des Kondensators erschweren Genauigkeiten unter 0,1 %.

Das **Zwei-Rampen-Verfahren (Dual Slope)** behebt genau diese Schwäche elegant: Zunächst integriert ein Operationsverstärker die Eingangsspannung U_e während einer **konstanten** Zeit t₁ — die Integratorspannung steigt linear an. Anschliessend wird auf eine Referenzspannung mit umgekehrtem Vorzeichen umgeschaltet; die Integratorspannung sinkt nun mit konstanter Steigung zurück gegen Null, und ein Zähler misst die dafür benötigte Zeit t₂. Da sowohl Auf- als auch Abintegration über **denselben** Kondensator und denselben Taktgenerator laufen, heben sich Bauteilfehler des Kondensators gegenseitig auf — übrig bleibt nur die Genauigkeit des Taktgenerators, die sich leicht auf 0,01 % bringen lässt. Der Preis: mit 1 ms bis 100 ms vergleichsweise lange Wandlungszeiten.

![Zeitdiagramm des Zwei-Rampen-Verfahrens (Dual Slope): während der konstanten Zeit t₁ integriert der OP die Eingangsspannung U_e auf; danach wird U_ref mit umgekehrtem Vorzeichen angelegt und die Zeit t₂ gemessen, bis der Integrator wieder auf Null zurückgekehrt ist — das Verhältnis t₂/t₁ entspricht U_e/U_ref](abbildungen/dual_slope_zeitdiagramm.png)
:::

## Das Wägeverfahren: der goldene Mittelweg

Ein Verfahren, das Geschwindigkeit und Hardwareaufwand geschickt ausbalanciert, ist die → [[Sukzessive Approximation (Wägeverfahren)|Sukzessive Approximation]] — sie "wägt" das Ergebnis Bit für Bit, vom höchstwertigen zum niederwertigsten, und kommt dabei mit nur einem internen DA-Wandler aus.

## Das Kaskadenverfahren: Parallelverfahren im Kompromiss

:::info
Das **Kaskadenverfahren** kombiniert das schnelle Parallelverfahren mit dem genaueren Wägeprinzip, um den Hardwareaufwand zu reduzieren: Ein erster, "grober" Parallelwandler bestimmt zunächst die oberen Bits (z. B. die oberen 5 von 10 Bit). Dieses Grobergebnis wird über einen internen DA-Wandler wieder in eine Spannung zurückverwandelt, von der Eingangsspannung subtrahiert und das Ergebnis verstärkt (z. B. ×32) — anschliessend bestimmt ein zweiter Parallelwandler die unteren Bits aus dieser "Restspannung". Eine **digitale Fehlerkorrektur** setzt die beiden Teilergebnisse am Ende korrekt zusammen. So lassen sich Wandlungszeiten unter einer Mikrosekunde erreichen, ohne gleich 1023 Komparatoren verbauen zu müssen — der Preis sind zwei AD-Wandler und ein zusätzlicher DA-Wandler.
:::

## Das Sigma-Delta-Verfahren: hohe Auflösung durch radikale Vereinfachung

Einen völlig anderen Weg geht schliesslich der → [[Sigma-Delta-Wandler|Sigma-Delta-Wandler]]: Er verzichtet auf einen mehrstufigen, präzisen Analogteil fast vollständig und verlagert die eigentliche "Intelligenz" in die digitale Signalverarbeitung.

## Auflösung: wie fein wird unterteilt?

Unabhängig vom gewählten Verfahren bestimmt sich die **Auflösung** eines AD-Wandlers stets aus denselben zwei Grössen:

:::formel
U_LSB = U_emax / 2^(Anzahl Bits)        Z = U_e / U_LSB
:::

Ein 10-Bit-Wandler mit Eingangsbereich 0…10 V liefert demnach eine Auflösung von U_LSB = 10 V / 2¹⁰ ≈ 9,77 mV — eine Eingangsspannung von 4,563 V ergibt damit Z = 4,563 V / 0,00976 V ≈ 466,7 ≈ 0111010010₂.

## Welches Verfahren für welche Anwendung?

:::merke
Bei der Wahl eines passenden AD-Wandlers sind drei Fragen entscheidend: **(1)** In welchem Spannungsbereich bewegt sich das Signal — bipolar oder unipolar? **(2)** Wie hoch ist die höchste im Signal enthaltene Frequenzkomponente — und damit, gemäss → [[Abtasttheorem (Nyquist-Shannon)|Abtasttheorem]], welche Mindest-Abtastfrequenz wird benötigt? **(3)** Wie fein muss die Auflösung sein, also wie klein darf U_LSB ausfallen? Schnelle Anwendungen wie digitale Oszilloskope verlangen nach Flash- oder Pipeline-Wandlern im Bereich von Hunderten von MHz Abtastrate; hochauflösende Mess- und Audiotechnik setzt dagegen eher auf langsamere, aber sehr genaue Dual-Slope- oder Sigma-Delta-Wandler.
:::

Damit ist die Bandbreite der grundsätzlichen Lösungsansätze abgesteckt — vom brachialen, aber blitzschnellen Parallelverfahren bis zum cleveren, hochauflösenden Sigma-Delta-Prinzip. Wie genau das pragmatische Wägeverfahren dabei Schritt für Schritt zu seinem Ergebnis "wägt", zeigt der nächste Artikel: → [[Sukzessive Approximation (Wägeverfahren)|Sukzessive Approximation]].
