---
title: Transformator Aufbau
kategorie: ET
tags: [transformator, aufbau, kern, wicklung, primär, sekundär, streufluss, leerlauf, kurzschluss]
groessen: U1|Primärspannung|V; U2|Sekundärspannung|V; I1|Primärstrom|A; I2|Sekundärstrom|A; N1|Primärwindungen|—; N2|Sekundärwindungen|—
_status: PORT  # ET_alt/Transformator/Transformator_Aufbau.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Spule (Übersicht)]]
- [[Magnetfelder]]
- [[Magnetisierungskurve & Hysterese]]
:::
:::vbox
**Verwandte Artikel**
- [[Transformator Typen]]
:::
:::vbox
**Führt weiter zu**
- [[Übersetzungsverhältnis]]
:::
:::

---

Der Transformator überträgt Wechselenergie zwischen zwei galvanisch getrennten Stromkreisen über ein gemeinsames Magnetfeld. Er ist das wichtigste Bauteil der Energieübertragung — er macht die Hochspannungsübertragung im Netz erst möglich.

## Funktionsprinzip

:::schematic Transformator-Prinzip: Eisenkern (E/I-Form) in der Mitte; Primärwicklung N1 (links am linken Schenkel) mit Wechselspannungsquelle U1 und Strom I1; Sekundärwicklung N2 (rechts am rechten Schenkel) mit Last und Spannung U2, Strom I2; Magnetischer Fluss Phi im Kern als Kreispfeil; Beschriftung: N1, N2, U1, U2, I1, I2, Phi
/schaltplaene/transformator/transformator_aufbau.svg
:::

Zwei Spulen (Primär- und Sekundärwicklung) auf demselben Eisenkern. Der Wechselstrom der Primärseite erzeugt einen wechselnden magnetischen Fluss im Kern, der in der Sekundärwicklung eine Spannung induziert.

Voraussetzung: **Wechselstrom** — bei Gleichstrom ist der Fluss konstant, keine Induktion auf der Sekundärseite.

## Kernformen

| Kernform | Eigenschaften | Anwendung |
|---|---|---|
| M-Kern (Mittelschenkelkern) | Kompakt, gut zugänglich | Netz-Trafos, kleine Netzteile |
| E/I-Kern | Einfach wickelbar | Trafos, Speicherdrosseln |
| Ringkern (Toroid) | Kleiner Streufluss, wenig EMV | Audio, HF, Netzteile |
| Schalenkern | Gut geschlossen, mechanisch stabil | SMD, HF-Übertrager |

## Streufluss

Im idealen Transformator ist der gesamte Fluss mit beiden Wicklungen verkoppelt. In der Realität "streut" ein Teil des Flusses durch die Luft — dieser **Streufluss** koppelt nicht in die Sekundärwicklung und erscheint als **Streuinduktivität**.

Hohe Streuinduktivität → schlechtere Spannungsregulation, mehr Verluste bei Laststössen.

## Leerlauf (I2 = 0)

Im Leerlauf fliesst ein kleiner Magnetisierungsstrom I_0 auf der Primärseite, um den Kern zu magnetisieren. Die Sekundärspannung entspricht der transformierten Leerlaufspannung (Übersetzungsverhältnis).

## Kurzschluss

Bei Kurzschluss auf der Sekundärseite sind nur noch die Wicklungswiderstände und die Streuinduktivitäten strombegrenzend. Der **Kurzschlussstrom** kann ein Vielfaches des Nennstroms betragen — Trafos müssen für definierte Zeit kurzschlussfest sein.

:::warning
Transformatoren dürfen nicht dauerhaft kurzgeschlossen betrieben werden — die Wicklungen überhitzen durch den hohen Kurzschlussstrom. Sicherungen auf der Sekundärseite sind zwingend.
:::

## Transformatorhauptgleichung

Die induzierte Spannung einer Wicklung hängt von Windungszahl, Frequenz, Kernquerschnitt und maximaler Flussdichte ab. Diese Formel gilt für Sinusspannung und den verlustfreien Transformator:

:::formel
U = 4.44 * N * f * A * B_max    # Transformatorhauptgleichung
:::

| Grösse | Einheit | Bedeutung |
|---|---|---|
| U | V | Effektivspannung der Wicklung |
| N | — | Windungszahl |
| f | Hz | Netzfrequenz (50 Hz) |
| A | m² | Effektiver Kernquerschnitt |
| B_max | T | Maximale Flussdichte (muss unter B_sat bleiben) |

Der Faktor 4.44 = 2π/√2 kommt aus dem Formfaktor der Sinuswelle.

**Windungszahl berechnen** — wie viele Windungen braucht eine Wicklung?

:::formel
N = U / (4.44 * f * A * B_max)
:::

**Windungsspannung** — Spannung pro Windung, gilt für alle Wicklungen desselben Kerns:

:::formel
U_W = U / N
:::

:::monospace
Beispiel: 230 V, 50 Hz, Kern A = 25 cm² = 25e-4 m², B_max = 1.2 T
N1 = 230 / (4.44 * 50 * 25e-4 * 1.2) = 230 / 0.666 = 345 Windungen
U_W = 230 / 345 = 0.667 V/Windung

Sekundärwicklung für 12 V:
N2 = 12 / 0.667 = 18 Windungen  (oder: N2 = N1 * U2/U1 = 345 * 12/230 = 18)
:::

:::tip
Die Windungsspannung U_W ist für alle Wicklungen auf demselben Kern gleich. Damit lassen sich alle Sekundärspannungen direkt durch Multiplikation mit N2 bestimmen — ohne die Hauptgleichung für jede Wicklung neu zu lösen.
:::

## Kernmaterialien

| Material | Frequenzbereich | Eigenschaft |
|---|---|---|
| Trafoblech (Si-Stahl) | 50 Hz (Netz) | Niedrige Hystereseverluste |
| Ferrit (Mn-Zn) | 1 kHz – 1 MHz | Geringe Wirbelstromverluste |
| Ferrit (Ni-Zn) | 1 MHz – 100 MHz | HF-Anwendungen |
| Nanocrystalline | 50 Hz – 100 kHz | Sehr niedrige Verluste |

Der Kernquerschnitt und das Material bestimmen, wie viel magnetische Energie ohne Sättigung gespeichert werden kann — die Kernauslegung ist zentrales Designelement.
