---
title: Relais & Schütze
kategorie: EK
tags: [relais, schütz, elektromagnet, freilaufdiode, schalten, prellzeit, NO, NC, galvanische trennung, IEC 60947, hilfskontakt]
symbol: K
einheit: —
---

Relais und Schütze schalten elektrische Lasten durch einen Elektromagnet. Steuerstromkreis und Lastkreis sind galvanisch getrennt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Elektromagnet]]
- [[Als Schalter]]
:::
:::vbox
**Verwandte Artikel**
- [[Sicherheitsrelais]]
:::
:::vbox
**Führt weiter zu**
- [[Not-Halt-Konzepte]]
- [[Maschinensicherheit]]
:::
:::

---

## Relais

Elektromagnet zieht einen Anker an. Dieser betätigt mechanische Kontakte. Der Steuerkreis (Spule) ist vom Lastkreis (Kontakte) getrennt.

Kontaktarten: Schliesser (NO, normally open), Öffner (NC, normally closed), Wechsler (COM).

**Einsatz**: Kleinsteuersignal (3.3 V oder 5 V Logik) schaltet grossen Lastkreis (230 V AC oder 24 V DC mit mehreren Ampere).

## Schütz

Industrielles Relais für grosse Ströme und Dauerbetrieb. Zusätzliche Hilfskontakte für Meldungen und Verriegelungen. Zertifiziert für Schaltspiele im Millionenbereich.

Typisch für Motorsteuerungen, Heizungen und Drehstromanwendungen.

## Freilaufdiode

Die Relaisspule ist eine Induktivität. Beim Abschalten entsteht eine Spannungsspitze. Diese zerstört den Transistor oder Mikrocontrollerausgang der das Relais steuert.

Freilaufdiode parallel zur Spule, in Sperrrichtung zur Versorgung. Beim Abschalten leitet sie und begrenzt die Spitze auf 0.7 V.

:::warning
Kein Relais ohne Freilaufdiode an einem Halbleiterausgang betreiben. Die Spannungsspitze kann mehrere hundert Volt erreichen und IC-Ausgänge sofort zerstören.
:::

## Prellzeit

Mechanische Kontakte prellen beim Schalten kurz. In 5 bis 20 ms öffnen und schliessen sie mehrfach schnell hintereinander. Für digitale Systeme muss dieses Prellen softwareseitig oder durch externe Entprellung unterdrückt werden.

## Kenndaten Auswahlhilfe

| Kriterium | Relais | Schütz |
|---|---|---|
| Strom | bis ca. 16 A | ab 6 A bis kA |
| Schaltspiele | 100 000 | über 1 000 000 |
| Zertifizierung | gering | IEC 60947 |
| Hilfskontakte | selten | Standard |
