---
title: Schrittmotor
kategorie: EK
kapitel: Motoren
tags: [schrittmotor, stepper, schrittwinkel, vollschritt, halbschritt, mikroschritt, unipolar, bipolar, schrittverlust, resonanz, rampe, a4988, drv8825, tmc]
groessen: alpha|Schrittwinkel|°; N|Schritte pro Umdrehung|—; f_schritt|Schrittfrequenz|Hz; n|Drehzahl|U/min
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[DC Motor]]
- [[H-Brücke]]
- [[Aktorik Grundlagen]]
:::
:::vbox
**Verwandte Artikel**
- [[Servomotor]]
- [[BLDC]]
:::
:::vbox
**Führt weiter zu**
- [[Servomotor]]
- [[Regelkreis Grundlagen]]
:::
:::

---

Der Schrittmotor dreht sich in definierten Schritten. Jeder Impuls dreht ihn um einen festen Winkel. Er wird **ohne Encoder** für einfache Positionieraufgaben eingesetzt — die Position wird durch Zählen der Schritte verfolgt.

## Funktionsprinzip

Mehrere Statorwicklungen werden der Reihe nach bestromt. Das rotierende Magnetfeld zieht den Rotor (Permanentmagnet oder gezahntes Eisen) in Schritten mit. Typischer Schrittwinkel: **1.8° pro Schritt = 200 Schritte pro Umdrehung**.

:::formel
alpha = 360° / N          # Schrittwinkel
N = 360° / alpha          # Schritte pro Umdrehung
n = f_schritt / N * 60    # Drehzahl [U/min] bei Schrittfrequenz f [Hz]
:::

## Betriebsarten

| Modus | Schritte/Umdr. | Merkmal |
|---|---|---|
| Vollschritt | 200 | 1 oder 2 Phasen aktiv, maximales Drehmoment |
| Halbschritt | 400 | Abwechselnd 1 und 2 Phasen aktiv, sanfterer Lauf |
| Mikroschritt ÷4 | 800 | Ströme teilweise moduliert |
| Mikroschritt ÷16 | 3200 | Sehr ruhiger Lauf, hohe Auflösung |
| Mikroschritt ÷256 | 51200 | Maximale Feinheit (TMC-Treiber) |

### Bestromungssequenz (bipolarer Motor)

**Vollschritt — 2 Phasen aktiv** (maximales Drehmoment):

| Schritt | Phase A | Phase B |
|---|---|---|
| 1 | + | + |
| 2 | − | + |
| 3 | − | − |
| 4 | + | − |

**Halbschritt — abwechselnd 1 und 2 Phasen** (doppelte Auflösung, sanfterer Lauf):

| Schritt | Phase A | Phase B |
|---|---|---|
| 1 | + | 0 |
| 2 | + | + |
| 3 | 0 | + |
| 4 | − | + |
| 5 | − | 0 |
| 6 | − | − |
| 7 | 0 | − |
| 8 | + | − |

Jede Wicklung wird von einer H-Brücke angesteuert: + = Vorwärts, − = Rückwärts, 0 = stromlos.

:::info
Mikroschritt erhöht die Auflösung und reduziert Resonanzen, aber nicht das Haltemoment — das sinkt bei hohem Mikroschrittteiler. Die mechanische Genauigkeit wird durch Getriebespiel und Elastizität begrenzt, nicht durch den Mikroschrittteiler.
:::

## Motortypen

**Bipolarer Schrittmotor (4 Leitungen)**: Zwei Wicklungen, pro Phase eine H-Brücke nötig. Höheres Drehmoment. Standard in 3D-Druckern und CNC-Maschinen.

**Unipolarer Schrittmotor (5/6/8 Leitungen)**: Mittelabgriffe an Wicklungen, einfachere Ansteuerung (Transistoren statt H-Brücke), aber weniger Drehmoment (halbe Wicklung aktiv).

## Drehzahl-Drehmoment-Verlauf

Das Drehmoment sinkt mit steigender Drehzahl. Zu hohe Schrittfrequenz → **Schrittverlust**: Der Motor springt aus dem Schritt und verliert die Position — ohne Rückmeldung unbemerkt.

**Schrittverlust vermeiden durch:**
- Beschleunigungs- und Bremsrampen (nicht sofort auf volle Frequenz schalten)
- Schrittfrequenz unterhalb der Pull-Out-Frequenz halten
- Ausreichenden Sicherheitsabstand zum Nennmoment

**Resonanzfrequenzen**: Bei bestimmten Drehzahlen (typisch 50–150 U/min) vibriert der Motor stark → durch Rampen schnell durchfahren oder Mikroschrittbetrieb nutzen.

## Ansteuerung und Treiberchips

Jede Phase des bipolaren Motors braucht eine H-Brücke. Treiberchips integrieren H-Brücken, Strombegrenzung und Mikroschrittlogik:

| IC | Strom | Mikroschritt | Besonderheit |
|---|---|---|---|
| A4988 | 2 A | bis ÷16 | Günstig, weit verbreitet |
| DRV8825 | 2.5 A | bis ÷32 | Etwas weniger Rauschen als A4988 |
| TMC2208 | 1.4 A RMS | bis ÷256 | StealthChop — sehr leiser Betrieb |
| TMC2209 | 2 A RMS | bis ÷256 | StealthChop + Stallguard (Schrittverlust erkennen) |

:::tip
TMC-Treiber verwenden wenn leiser Betrieb wichtig ist (3D-Drucker, Büroumgebung). StealthChop moduliert den Strom so, dass keine hörbaren Frequenzen entstehen. TMC2209 erkennt zusätzlich Schrittverlust über den Motorstrom — ersetzt für viele Anwendungen den Endschalter.
:::

## Vergleich Schrittmotor / Servo

| Eigenschaft | Schrittmotor | Servo |
|---|---|---|
| Positionsrückmeldung | Keine (Open-Loop) | Encoder (Closed-Loop) |
| Schrittverlust | Möglich und unbemerkt | Erkannt und korrigiert |
| Haltemoment | Hoch (bestromt) | Abhängig von Motor |
| Kosten | Günstig | Höher |
| Einsatz | Einfache Positionierung | Hochgenaue Anwendungen |
| Ansteuerungsaufwand | Mittel | Hoch (Regler nötig) |
