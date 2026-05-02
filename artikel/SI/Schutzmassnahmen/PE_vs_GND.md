---
title: Schutzerde (PE) vs. Signalmasse (GND)
kategorie: SI
tags: [PE, GND, schutzerde, masse, erdung, sicherheit, EMV, potenzialausgleich, brummschleife, masseschleife, Y-kondensator]
symbol: —
einheit: —
---

PE und GND sind beide Bezugspotenziale, aber mit unterschiedlicher Aufgabe. Die Verwechslung führt zu Sicherheitsrisiken oder EMV-Problemen.

:::hbox
:::vbox
**Voraussetzungen**
- [[Schutzklassen I, II, III]]
- [[Gefahren des Stroms]]
:::
:::vbox
**Verwandte Artikel**
- [[Fehlerschutz (FI/RCD)]]
- [[EMV Pre-Compliance]]
:::
:::vbox
**Führt weiter zu**
- [[Sternpunkterdung]]
- [[Isolationsmessung]]
:::
:::

---

## Schutzerde PE (Protective Earth)

PE ist die grün-gelbe Leitung im Netzanschluss. Sie verbindet alle leitfähigen Gehäuse und Metallteile mit der Erde. Zweck: Sicherheit.

Bei einem Isolationsfehler (z.B. Phasenleiter berührt Gehäuse) fliesst der Fehlerstrom über PE ab — nicht über den Menschen. Der Leitungsschutzschalter oder FI-Schalter löst aus.

PE ist über den Hausanschluss direkt mit dem Erdreich verbunden (Fundamenterder, Erder). Widerstand so klein wie möglich, typisch unter 1 Ω zum nächsten Erder.

## Signalmasse GND (Ground)

GND ist der Bezugspunkt aller Signale in einer Schaltung. Spannungen werden relativ zu GND gemessen. GND ist kein Sicherheitsleiter.

In batteriebetriebenen Geräten ist GND galvanisch von PE getrennt. In Netzgeräten mit Schutzklasse II ebenfalls.

GND liegt je nach Schaltung auf einem anderen Potenzial als PE. Bei einem ungefährlichen Netzgerät (Primär/Sekundär getrennt) liegt die Sekundär-GND oft irgendwo zwischen den Netzleitern.

## Warum man sie nicht einfach verbinden darf

**Sicherheitsproblem**: Wenn GND und PE falsch verbunden werden, kann bei einem Fehler Strom über die Signalmasse fliessen — durch Kabel, Steckverbinder, Messgeräte. Das kann Personen und Geräte gefährden.

**EMV-Problem**: PE führt Ableitströme von Y-Kondensatoren. Diese hochfrequenten Ströme auf der Signalmasse verursachen Störungen in empfindlichen Schaltungen.

**Brummschleifen**: Bei galvanisch verbundenen Geräten (z.B. zwei Netzgeräte, beide mit PE verbunden, beide mit GND verbunden) entsteht eine Masseschleife. Kleinstpotenzialunterschiede zwischen den Erdungspunkten treiben Störströme durch die Signalleitungen. Ergebnis: 50-Hz-Brummen.

## Wann PE und GND verbunden werden

In manchen Schaltungen ist eine einzige Verbindungsstelle von GND zu PE sinnvoll und normgemäss:
- Primärseitige GND in Schaltnetzteilen wird einpunktig mit PE verbunden (Ableitstrom-Pfad für Y-Kondensatoren)
- Schaltschränke: Signalmasse über einen definierten Punkt mit Potenzialausgleich verbunden

Wichtig: Nur an einem einzigen Punkt verbinden. Mehrfachverbindungen erzeugen Schleifen.

## Symbole

| Symbol | Bedeutung |
|---|---|
| ⏚ (drei waagrechte Linien) | Erde / Erdanschluss (PE) |
| ⏚ (Dreieck mit Strich) | Chassis-Masse / Schutzerde |
| GND / ⊥ (umgekehrtes T) | Signalmasse / digitale Masse |

:::warning
An einer Schaltung niemals PE direkt als Signalrückleiter verwenden. PE ist ein Schutzleiter, kein Signalleiter.
:::
