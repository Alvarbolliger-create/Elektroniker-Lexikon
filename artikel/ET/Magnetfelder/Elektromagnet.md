---
title: Elektromagnet
kategorie: ET
tags: [elektromagnet, spule, magnetfeld, kern, remanenz, amperewindungen, durchflutungsgesetz, luftspalt, relais, freilaufdiode, magnetventil]
symbol: —
einheit: —
---

Ein Elektromagnet erzeugt ein Magnetfeld durch Strom. Er lässt sich ein- und ausschalten. Die Stärke ist über den Strom einstellbar.

:::hbox
:::vbox
**Voraussetzungen**
- [[Lorentzkraft]]
- [[Selbstinduktion]]
:::
:::vbox
**Verwandte Artikel**
- [[Transformator: Aufbau & Funktionsprinzip]]
:::
:::vbox
**Führt weiter zu**
- [[Relais & Schütze]]
:::
:::

---

## Aufbau

Eine Spule auf einem Eisenkern. Der Kern verstärkt das Feld um ein Vielfaches (Permeabilitätszahl µ_r von Eisen: 1000 bis 100000).

Mehr Windungen, mehr Strom, besserer Kern: stärkeres Feld.

## Magnetomotorische Kraft

:::monospace
H * l = N * I       # Durchflutungsgesetz; N = Windungszahl, I = Strom, l = Feldlinienlänge
:::
N × I heisst auch Amperewindungen. Je mehr Amperewindungen, desto stärker das Feld.

## Remanenz

Eisen bleibt nach Abschalten schwach magnetisch. Das nennt sich Remanenz. Bei Relais kann das dazu führen, dass der Anker nicht loslässt. Spezielle Materialien oder Luftspalte reduzieren die Remanenz. Das vollständige Verhalten — inklusive Hysteresekurve und Koerzitivfeldstärke — ist unter [[Sättigung und Hysterese]] beschrieben.

## Luftspalt

Ein Luftspalt im Kern erfüllt zwei Funktionen: Er reduziert die Remanenz und linearisiert die B-H-Kurve. Das bedeutet, die Induktivität bleibt über einen grösseren Strombereich konstant und der Kern sättigt später. Der Luftspalt erhöht zwar den magnetischen Widerstand (und senkt damit L), macht das Bauteil aber robuster gegenüber hohen Gleichströmen. Deshalb haben Schaltnetzteildrosseln meist einen Luftspalt.

## Anwendungen

**Relais**: Elektromagnet zieht Schaltkontakte an. Kleines Steuersignal schaltet grossen Laststrom.

**Magnetventil**: Steuert Flüssigkeits- oder Gasfluss.

**Schütz**: Industrierelais für grosse Ströme.

**Haltemaggnet**: Türen, Sicherheitsverriegelungen.

:::warning
Beim Abschalten entsteht eine Spannungsspitze durch Selbstinduktion. Freilaufdiode parallel zur Spule einbauen, sonst werden Steuertransistoren oder Mikrocontroller-Ausgänge zerstört.
:::
