---
title: PID-Regler
kategorie: SH
kapitel: Regelungstechnik
tags: [pid-regler, proportionalanteil, integralanteil, differentialanteil, sollwert, istwert, regelkreis, opv]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Regelkreis Grundlagen]]
- [[OPV Grundlagen]]
:::
:::

---

Ein → [[Regelkreis Grundlagen|Regelkreis]] vergleicht fortlaufend einen Sollwert w mit dem tatsächlichen Istwert x und versucht, die Differenz e = w − x — die **Regelabweichung** — möglichst schnell und stabil auf null zu bringen. Doch *wie* genau aus dieser Differenz ein sinnvolles Stellsignal wird, entscheidet der Regler. Der mit Abstand am häufigsten eingesetzte Reglertyp ist der **PID-Regler** — eine geschickte Parallelschaltung von drei grundverschiedenen "Charakteren", die sich gegenseitig ergänzen: dem **P**roportional-, dem **I**ntegral- und dem **D**ifferential-Anteil.

## Der Proportional-Anteil: schnell, aber ungeduldig

:::merke
Der **P-Anteil** multipliziert die Regelabweichung (w − x) mit einem konstanten Faktor K_P — er reagiert also unmittelbar und proportional auf jede Abweichung, ohne "Gedächtnis" und ohne Verzögerung. Betrachtet man ein System nach unendlich langer Zeit (rein statische Betrachtung, Streckenverstärkung = 1) mit reinem P-Regler, ergibt sich für den Endwert der Sprungantwort: x = P·w / (1 + P). Bei einem Sollwert von w = 100 liefert das:

| P-Wert | Endwert x |
|---|---|
| P = 1 | 50,000 |
| P = 10 | 90,909 |
| P = 100 | 99,009 |

Je grösser P gewählt wird, desto näher kommt der Istwert dem Sollwert — ein unendlich grosser P-Anteil wäre also "ideal". In der Praxis zeigt sich aber: **Je grösser P, desto stärker die Schwingneigung des Systems.** Mit dem P-Anteil lässt sich vor allem die "Steilheit" am Anfang der Sprungantwort einstellen — eine **bleibende Regelabweichung** (x = w wird nie ganz erreicht) bleibt mit reinem P-Anteil aber immer bestehen.
:::

## Der Integral-Anteil: das Gedächtnis des Reglers

:::tip
Der **I-Anteil** bildet die "Fläche" unter der Eingangskurve — er **integriert** die Regelabweichung über die Zeit auf. Eine anschauliche Analogie: eine viereckige Badewanne mit konstantem Zu- und Ablauf, oder ein Fussballplatz, über den man mit unterschiedlicher Schrittweite läuft — was zählt, ist die insgesamt zurückgelegte Fläche. Drei Eigenschaften machen den Integrator besonders wertvoll für die Regelungstechnik:

- Er ist ein "Flächenbildner" — er summiert die Vergangenheit auf.
- Er kann am Ausgang ein Signal liefern, **obwohl der Eingang gerade null ist** — er "merkt sich" das letzte Flächenresultat.
- Er verfügt über eine eigene Zeitkonstante T_n und ist damit ein eher träges Element.

Genau diese Fähigkeit, auch bei verschwindender Regelabweichung ein Stellsignal aufrechtzuerhalten, ist der Schlüssel dafür, dass ein PID-Regler die bleibende Regelabweichung des reinen P-Reglers vollständig beseitigen kann: **Bei x = w "lebt" der Regelkreis vom Integrator** — nur dieses Element liefert dann noch ein Signal am Ausgang, obwohl sein Eingang null ist.
:::

## Der Differential-Anteil: die Bremse im richtigen Moment

:::warning
Der **D-Anteil** bildet die "Steigung" des Eingangssignals — mathematisch gesprochen leitet er die Regelabweichung ab. Er ist ein sehr **dynamisches** Element: Ein gutmütiges, sich nur langsam änderndes Eingangssignal wird am Ausgang "scharfkantig". Solange das Eingangssignal konstant ist (keine Steigung), liefert der D-Anteil exakt null — er wirkt also nur dort, wo sich gerade etwas *ändert*.

Da P-, I- und D-Anteil parallel geschaltet sind, erhalten alle drei dasselbe Eingangssignal (w − x). Steigt diese Differenz an (positive Steigung), unterstützen sich P- und I-Anteil gegenseitig. Beim D-Anteil ist die Sache subtiler: Da der Sollwert w konstant bleibt, gilt für die Ableitung (w − x)' = ẇ − ẋ = 0 − ẋ = −ẋ. Dieses Minuszeichen sorgt dafür, dass der D-Anteil in der steilsten Phase der Sprungantwort ein **negatives** Signal liefert — er arbeitet "gegen" den P- und I-Anteil und **bremst** damit das Überschwingen ab.

Genau hier liegt aber auch die Tücke: **Wird der D-Anteil zu gross eingestellt, nimmt die Schwingneigung des Systems sogar wieder zu.** Es gibt also nur ein begrenztes "Fenster", in dem der D-Anteil tatsächlich als Bremse wirkt — wird er übertrieben, kippt sein Effekt ins Gegenteil.
:::

![PID-Regelkreisstruktur: Schritt-Eingangssignal → Vergleichsstelle (w−x) → parallele P-, I- und D-Zweige (mit Zeitkonstanten Ti und TD) → Summationspunkt → Strecke PT2 (mit Verstärkung K und Zeitkonstanten T, d) → Istwert-Rückkopplung; rechts die kompakte Übertragungsfunktion G(s) = K_P·(1 + 1/(s·T_n) + s·T_v)](abbildungen/pid_regelkreisstruktur.png)

## Wer dominiert wann? Eine Sprungantwort in drei Phasen

Betrachtet man die Sprungantwort eines PID-geregelten Systems genauer, fällt auf, dass die drei Anteile zu unterschiedlichen Zeitpunkten ganz unterschiedlich stark zur Wirkung kommen:

| Phase der Sprungantwort | P-Anteil | I-Anteil | D-Anteil |
|---|---|---|---|
| Anfang (Punkt A, flacher Teil) | sehr gross (+) | klein (+) | klein (−) |
| steilste Stelle (Punkt B) | klein (+) | mittel (+) | gross (−) |
| Beharrungszustand x = w (Punkt C) | null | mittel (+) | null |

![PID-Sprungantwort mit Phasenanalyse: Die farbige Kurve zeigt den Istwert-Verlauf nach einem Sollwert-Sprung — Punkt A im flachen Anfangsteil, Punkt B an der steilsten Stelle, Punkt C im eingeschwungenen Zustand; daneben die beschrifteten Einflussfelder jedes Anteils (P, I, D) in den drei Phasen A, B und C](abbildungen/pid_sprungantwort_phasen.png)

:::merke
Daraus lassen sich drei zentrale Beobachtungen ableiten:

- **Am Anfang der Sprungantwort dominiert der P-Anteil** — mit ihm lässt sich die "Steilheit" des Anlaufs einstellen.
- **In der steilsten Phase dominiert der D-Anteil** — mit ihm lässt sich der "Ausschaltpunkt" festlegen. Gilt dort näherungsweise P + I = D ("Seilziehen"), neutralisieren sich die drei Anteile gegenseitig — der ideale Moment, um die Sprungantwort sanft abzubremsen.
- **Im eingeschwungenen Zustand (x = w) lebt der Regelkreis allein vom Integrator** — P- und D-Anteil liefern dort beide null, nur der I-Anteil hält das Stellsignal aufrecht und sorgt dafür, dass die Regelabweichung tatsächlich auf null sinkt.
:::

## Die Formel hinter dem PID-Regler

Mathematisch lässt sich das Zusammenspiel der drei Anteile in einer einzigen Übertragungsfunktion zusammenfassen:

:::formel
G(s) = K_P · (1 + 1/(s · T_n) + s · T_v)
:::

Dabei ist K_P die Verstärkung des P-Anteils, T_n die Nachstellzeit (Integrierzeitkonstante) und T_v die Vorhaltezeit (Differenzierzeitkonstante) des Reglers.

## Praktische Realisierung mit Operationsverstärkern

:::info
Sowohl die Sollwertvorgabe (über einen Spannungsteiler mit Potentiometer) als auch die Vergleichsstelle (w − x) lassen sich elegant mit → [[OPV Grundlagen|Operationsverstärker]]-Grundschaltungen realisieren — etwa als Subtrahierer mit fünf gleich grossen Widerständen R1 = R2 = R3 = R4 = R5. Auch der gesamte PID-Regler selbst lässt sich mit einer Schaltung aus mehreren Operationsverstärkern aufbauen, bei der sich die drei Regelparameter **unabhängig voneinander** einstellen lassen:

- K_P = R_P / R_I
- T_n = R_I · C_I
- T_v = R_D · C_D

Ein zusätzlicher Widerstand R3 begrenzt dabei die Verstärkung des D-Teils bei hohen Frequenzen — ohne diese "Kontur" würde der differenzierende Anteil hochfrequentes Rauschen unkontrolliert verstärken. Aus demselben Grundaufbau lassen sich übrigens auch die einfacheren Reglertypen **PI** (D-Teil mit R_D = 0 Ω deaktiviert) und **PD** (I-Teil über einen Schalter S kurzgeschlossen) ableiten. Eine kompaktere, aber weniger flexible Variante realisiert den kompletten PID-Regler mit nur einem einzigen Operationsverstärker — dort lassen sich die drei Parameter dann allerdings nicht mehr unabhängig voneinander einstellen.
:::

## Den Regler von Hand einstellen: ein bewährtes Vorgehen

Wie findet man in der Praxis die passenden Werte für K_P, T_n und T_v? Ein erprobtes, schrittweises Vorgehen hat sich dabei durchgesetzt:

1. Falls möglich, ein Simulationsmodell der Strecke erfassen.
2. Den **P-Anteil so weit erhöhen, bis der Istwert zu schwingen beginnt** — damit findet man die Grenze der Verstärkung.
3. Den **D-Anteil erhöhen, um diese Schwingung zu dämpfen** — die Sprungantwort wird ruhiger und nähert sich dem Sollwert an.
4. Den **I-Anteil zuschalten** — zunächst mit einer grossen Zeitkonstante beginnen und diese dann schrittweise verkleinern. Erst dadurch wird x = w tatsächlich erreicht und die bleibende Regelabweichung verschwindet.
5. **Test in der Praxis** — denn das reale System verhält sich selten exakt wie das Simulationsmodell.

So entsteht aus drei denkbar einfachen Grundverhalten — proportional, integrierend, differenzierend — ein Regler, der sich nahezu jeder Regelstrecke anpassen lässt: schnell genug, um zügig auf Änderungen zu reagieren, stabil genug, um nicht aufzuschwingen, und präzise genug, um am Ende exakt den gewünschten Sollwert zu erreichen. Damit schliesst sich der Kreis der Regelungstechnik — vom einfachen → [[Regelkreis Grundlagen|Regelkreis]] über die Mess- und Wandlertechnik bis hin zur feinfühligen, dreigeteilten Reglerstruktur, die heute in unzähligen technischen Systemen rund um die Uhr im Hintergrund arbeitet.
