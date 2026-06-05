---
title: OPV Integrierer & Differenzierer
kategorie: EK
tags: [OPV, integrierer, differenzierer, rampe, PID, filter, offset-drift, rauschen, dreieckgenerator, D-anteil, I-anteil]
symbol: —
einheit: —
---

Der Integrierer summiert ein Signal über die Zeit auf. Der Differenzierer gibt die Änderungsrate aus. Beide sind direkte Bausteine für PID-Regler und analoge Filter.

:::hbox
:::vbox
**Voraussetzungen**
- [[OPV Invertierend]]
:::
:::vbox
**Verwandte Artikel**
- [[PID-Regler]]
:::
:::vbox
**Führt weiter zu**
- [[PID-Regler]]
:::
:::

---

## Integrierer

Widerstand am Eingang, Kondensator in der Rückkopplung (statt Widerstand).

Bei konstanter Eingangsspannung steigt der Ausgang linear als Rampe. Das entspricht einer mathematischen Integration.

:::formel
U_aus = -1/(R*C) * integral(U_ein)    # Ausgangsspannung als Integral des Eingangs
:::
Anwendung: I-Anteil im PID-Regler, Dreieckgenerator aus einem Rechtecksignal, Tiefpassfilter.

**Problem**: Offset-Spannung am Eingang wird auch integriert. Der Ausgang driftet langsam gegen die Versorgungsschiene. Lösung: Widerstand parallel zum Kondensator (begrenzt die DC-Verstärkung).

## Differenzierer

Kondensator am Eingang, Widerstand in der Rückkopplung.

Reagiert auf Änderungen. Konstantes Signal: Ausgang null. Schnelle Flanke: grosser Ausgangsimpuls.

:::formel
U_aus = -R*C * dU_ein/dt    # Ausgang proportional zur Änderungsrate des Eingangs
:::
Anwendung: D-Anteil im PID-Regler, Flankenerkennung.

**Problem**: Verstärkt Rauschen stark, weil Rauschen hohe Frequenzanteile hat. In der Praxis wird ein kleiner Widerstand in Reihe zum Kondensator geschaltet, um die Hochfrequenzverstärkung zu begrenzen.

:::warning
Differenzierer sind empfindlich gegen Rauschen. Im realen PID-Regler wird der D-Anteil oft gefiltert oder weggelassen wenn das Messsignal verrauscht ist.
:::
