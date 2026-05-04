---
title: Signalintegrität
kategorie: EK
tags: [signalintegrität, reflexion, übersprechen, wellenwiderstand, PCB, high-speed, reflexionskoeffizient, augendiagramm, crosstalk, NEXT, FEXT, impedanzkontrolle, LVDS, DDR]
symbol: —
einheit: —
---

Signalintegrität beschreibt wie gut digitale Signale über Leitungen übertragen werden. Bei hohen Frequenzen verhalten sich Leiterbahnen nicht mehr wie Drähte.

:::hbox
:::vbox
**Voraussetzungen**
- [[Impedanz]]
- [[PCB Aufbau]]
- [[Signale]]
:::
:::vbox
**Verwandte Artikel**
- [[Wellenwiderstand]]
- [[Übersprechen]]
:::
:::vbox
**Führt weiter zu**
- [[Wellenwiderstand]]
- [[Übersprechen]]
:::
:::

---

## Wann wird Signalintegrität wichtig?

Faustregel: Wenn die Wellenlänge des Signals kleiner als etwa das Zehnfache der Leitungslänge ist.

Bei einer Leiterbahn von 10 cm und einem Signal mit 300-ps-Anstiegszeit kann Signalintegrität bereits relevant sein. USB, HDMI, DDR-RAM, serielle Hochgeschwindigkeitsprotokolle sind typische Problemfelder.

## Leiterbahn als Übertragungsleitung

Eine Leiterbahn hat nicht nur ohmschen Widerstand, sondern auch Induktivität, Kapazität und Leitwert. Bei hohen Frequenzen dominieren L und C das Verhalten.

Der charakteristische Wellenwiderstand (Z0) hängt von Geometrie und Material ab.

## Reflexion

Wenn eine Signalwelle auf einen Impedanzsprung trifft (falsch abgeschlossene Leitung, Steckverbinder, Querschnittsänderung), wird ein Teil des Signals reflektiert. Der Reflexionskoeffizient Γ bestimmt wie viel:

:::monospace
Γ = (Z_L - Z0) / (Z_L + Z0)    # Z_L = Lastimpedanz, Z0 = Leitungswellenwiderstand
:::
| Abschluss | Z_L | Γ | Wirkung |
|---|---|---|---|
| Offen (kein Abschluss) | ∞ | +1 | Vollständige Reflexion, Spannung verdoppelt sich |
| Kurzschluss | 0 Ω | −1 | Vollständige Reflexion, Spannung invertiert |
| Perfekter Abschluss | Z0 | 0 | Keine Reflexion |

Das reflektierte Signal überlagert sich mit dem nächsten Signal. Ergebnis: Überschwingen, Unterklingen, geschlossenes Augendiagramm.

:::info
Das Augendiagramm ist das Diagnosewerkzeug für Signalintegrität: Überlagert viele Perioden eines digitalen Signals. Ein offenes Auge = gute Übertragung. Reflexionen, Jitter und Übersprechen schliessen das Auge.
:::

Massnahme: Leitungen sauber abschliessen (Serienwiderstand am Ausgang, Paralleler Abschluss am Empfänger).

## Übersprechen (Crosstalk)

Parallele Leitungen koppeln elektromagnetisch. Das Signal einer Leitung induziert eine Störung in der benachbarten.

- **Near-End Crosstalk (NEXT)**: Störung am Senderende
- **Far-End Crosstalk (FEXT)**: Störung am Empfangsende

Massnahmen: Abstand zwischen Leitungen vergrössern, Massefläche zwischen Signalleitungen, differentielle Leitungsführung.

## Differentielle Signalführung

Zwei Leitungen mit entgegengesetzten Signalen. Störungen treffen beide Leitungen gleich, der Empfänger sieht nur die Differenz.

Hohe Störfestigkeit. LVDS, USB, HDMI, Ethernet nutzen dieses Prinzip.

:::tip
In KiCad und Altium gibt es Impedanzkontrollierte Leitungsführung. Den Hersteller nach seinen Lagenaufbau und Kupferstärke fragen, dann den Rechner nutzen um die Leitungsbreite für 50 Ohm oder 100 Ohm Differential zu berechnen.
:::
