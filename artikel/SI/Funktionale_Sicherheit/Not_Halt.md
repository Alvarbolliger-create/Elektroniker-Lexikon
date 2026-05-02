---
title: Not-Halt
kategorie: SI
tags: [not-halt, not-aus, sicherheitsfunktion, PLe, SIL 3, ISO 13849, öffner, verrastend, quittierung, IEC 60947, zweikanalig]
symbol: —
einheit: —
---

Der Not-Halt ist die bekannteste Sicherheitsfunktion an Maschinen. Er stoppt gefährliche Bewegungen wenn Menschen in Gefahr sind.

:::hbox
:::vbox
**Voraussetzungen**
- [[SIL und PL]]
- [[Die 5 Sicherheitsregeln]]
:::
:::vbox
**Verwandte Artikel**
- [[Sicherheitsrelais]]
- [[Zweikanalige Abschaltung]]
:::
:::

---

## Not-Halt vs. Not-Aus

Diese Begriffe werden oft verwechselt.

**Not-Halt (IEC 60204-1)**: Stoppt die gefährliche Bewegung. Die Maschine bleibt unter Spannung. Kann nach Quittierung wieder anlaufen.

**Not-Aus (Notstromunterbrecher)**: Trennt die gesamte Spannungsversorgung. Für Gefahren durch Elektrizität selbst.

Beides kann physisch am gleichen Gerät sein, hat aber unterschiedliche Schutzfunktionen.

## Anforderungen an den Not-Halt-Taster

- Pilzform, rot, Hintergrund gelb (IEC 60947-5-5)
- Verrastend (bleibt im ausgelösten Zustand)
- Muss manuell quittiert werden
- Öffnerkontakt (Stromfluss = aktiv; Kabelbruch löst aus)

## Sicherheitskategorie

Not-Halt-Systeme müssen meist PLd oder PLe (ISO 13849) erreichen. Das erfordert in der Regel zweikanalige Auswertung und einen Sicherheitskreis.

Einfache Variante: Not-Halt-Taster mit zwei Öffnern an ein Sicherheitsrelais. Das Relais überwacht beide Kanäle und erkennt wenn sie nicht übereinstimmen.

## Quittierung

Nach dem Auslösen muss die Maschine sicher im Stillstand sein bevor der Not-Halt wieder freigegeben wird. Automatischer Wiederanlauf ist nicht erlaubt.

Die Quittierung kann durch das Entsperren des Tasters (drehen oder ziehen) und anschliessend durch eine separate Starttaste erfolgen.

:::tip
Not-Halt-Geräte regelmässig betätigen und die Funktion prüfen. Ein Not-Halt der nie ausgelöst wird kann im Ernstfall versagen ohne dass es jemand merkt.
:::
