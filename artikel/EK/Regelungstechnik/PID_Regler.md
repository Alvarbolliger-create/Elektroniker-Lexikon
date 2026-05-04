---
title: PID-Regler
kategorie: EK
tags: [PID, regler, regelung, proportional, integral, differential, ziegler-nichols, anti-windup, einstellung, software-implementierung, zweipunktregler, regelsysteme, digitaler regler]
symbol: —
einheit: —
---

Der PID-Regler kombiniert drei Anteile: P reagiert auf die aktuelle Abweichung, I auf die aufgelaufene, D auf die Änderungsrate. Zusammen ergibt das einen robusten und schnellen Regler.

:::hbox
:::vbox
**Voraussetzungen**
- [[Regelkreis]]
:::
:::vbox
**Verwandte Artikel**
- [[Stabilität & Schwingneigung]]
:::
:::vbox
**Führt weiter zu**
- [[Motorregelung]]
:::
:::

---

## Die drei Anteile

**P-Anteil (Proportional)**: Stellgrösse proportional zur Abweichung. Grössere Abweichung, stärkere Reaktion. Einfach, aber es bleibt immer eine bleibende Regelabweichung.

**I-Anteil (Integral)**: Summiert die Abweichung über die Zeit. Beseitigt die bleibende Regelabweichung des P-Reglers. Kann zu Überschwingen führen.

**D-Anteil (Differenzial)**: Reagiert auf die Änderungsrate der Abweichung. Bremst das Überschwingen, macht den Regler schneller. Empfindlich gegen Rauschen.

## Formel

:::monospace
u(t) = Kp * e + Ki * integral(e) + Kd * de/dt      # Stellgrösse aus P, I, D Anteil
:::
Kp, Ki, Kd sind die einstellbaren Verstärkungen.

## Einstellung (Ziegler-Nichols)

Einfache Methode: I und D ausschalten, Kp erhöhen bis der Regelkreis stabil schwingt. Diese Verstärkung (K_u) und die Schwingungsdauer (T_u) ergeben Startwerte.

| Reglertyp | Kp | Ti | Td |
|---|---|---|---|
| P | 0.5 K_u | — | — |
| PI | 0.45 K_u | 0.85 T_u | — |
| PID | 0.6 K_u | 0.5 T_u | 0.125 T_u |

Das sind nur Startwerte. Feinabstimmung in der realen Anlage ist immer nötig.

:::warning
Der D-Anteil verstärkt Rauschen. Bei verrauschten Messsignalen (Sensorrauschen) kann er den Regler destabilisieren. Oft wird nur PI verwendet und auf D verzichtet.
:::

---

## Digitaler PID (Software-Implementierung)

Im Mikrocontroller wird der PID diskret (in Zeitschritten Δt) berechnet:

:::monospace
e[k]       = Soll - Ist                    # Regelabweichung
P_anteil   = Kp × e[k]
I_anteil  += Ki × e[k] × Δt               # aufsummiert
D_anteil   = Kd × (e[k] - e[k-1]) / Δt   # Differenz zum letzten Schritt
u[k]       = P_anteil + I_anteil + D_anteil
:::
**Wichtige Praxis-Details**:
- **Abtastzeit Δt**: Muss schnell genug sein (mindestens 5–10× schneller als Regelstrecke)
- **Anti-Windup**: Der I-Anteil kann unbegrenzt wachsen wenn der Ausgang saturiert ist → Integrator einfrieren oder begrenzen
- **Ausgangsclipping**: `u[k]` auf physikalisch sinnvollen Bereich begrenzen (z.B. 0–100% PWM)

---

## Regler-Verhalten im Überblick

| Regler | Bleibende Abweichung | Überschwingen | Typische Anwendung |
|---|---|---|---|
| P | Ja (bleibend) | Kaum | Einfache Lageregelung |
| I | Nein | Stark | Langsame Strecken |
| PI | Nein | Mittel | Drehzahl, Strom, Temperatur |
| PD | Ja | Gering | Wenn bleibende Abw. akzeptiert |
| PID | Nein | Gering | Allgemein, industriell |

---

---

:::info
Der Zweipunktregler ist kein PID-Regler. Er wird hier als Kontrastbeispiel gezeigt — der einfachste aller Regler, ohne P-, I- oder D-Anteil.
:::

## Zweipunktregler

Der einfachste Regler: Die Stellgrösse kennt nur zwei Zustände — EIN oder AUS.

:::monospace
e > 0:  Stellgrösse = MAX  (z.B. Heizung EIN)
e < 0:  Stellgrösse = 0    (z.B. Heizung AUS)
:::
**Problem**: Dauerndes Schalten um den Sollwert → Hysterese nötig.

**Mit Hysterese (Zweipunktregler mit Schaltdifferenz)**:

:::formel
Istwert < (Sollwert - Δ/2):  Stellgrösse EIN
Istwert > (Sollwert + Δ/2):  Stellgrösse AUS
:::
Die Schaltdifferenz Δ verhindert schnelles Pendeln (Flattern). Typisch: Thermostat, Bimetall-Schalter, einfache Temperaturregelungen.

:::info
Ein Komparator mit Hysterese (Schmitt-Trigger) ist die analoge Umsetzung eines Zweipunktreglers.
:::

**Nachteil**: Das System schwingt immer um den Sollwert herum. Die Amplitude der Schwingung hängt von der Schaltdifferenz und der Verzögerung der Regelstrecke ab.
