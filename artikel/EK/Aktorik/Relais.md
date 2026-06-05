---
title: Relais
kategorie: EK
tags: [relais, elektromagnet, schalter, no, nc, freilaufdiode, galvanische-trennung, prellen, schütz]
symbol: K
einheit: —
---

Ein Relais ist ein elektromagnetisch betriebener Schalter. Ein kleines Steuersignal schaltet einen davon galvanisch getrennten Leistungskreis — oft wird damit eine 3,3-V-Logik mit einem 230-V-Netz verbunden.

:::hbox
:::vbox
**Voraussetzungen**
- [[Transistor als Schalter]]
- [[Elektromagnet]]
:::
:::vbox
**Verwandte Artikel**
- [[Optokoppler]]
- [[H-Brücke]]
- [[Bussystem-Aktor]]
:::
:::vbox
**Führt weiter zu**
- [[Sicherheitsrelais]]
- [[Motor-Treiber-IC]]
:::
:::

---

## Aufbau

Eine bestromte Spule zieht einen Anker an. Der Anker betätigt mechanische Kontakte. Steuerstromkreis (Spule) und Lastkreis (Kontakte) sind galvanisch getrennt.

| Kontaktart | Kürzel | Normalzustand | Bei Erregung |
|---|---|---|---|
| Schliesser | NO (normally open) | Offen | Geschlossen |
| Öffner | NC (normally closed) | Geschlossen | Offen |
| Wechsler | COM | Verbunden mit NC | Wechselt zu NO |

---

## Freilaufdiode

Die Spule ist induktiv. Beim Abschalten entsteht eine Gegenspannung (induktiver Spannungsstoss), die Transistoren und Mikrocontrollerausgänge zerstört.

:::danger
Relaisspule nie ohne Freilaufdiode an einem Halbleiterausgang betreiben. Der Spannungsstoss kann mehrere hundert Volt erreichen und den Ausgangs-Pin sofort zerstören.
:::

Die Freilaufdiode wird parallel zur Spule in Sperrrichtung zur Versorgung eingebaut. Beim Abschalten leitet sie und begrenzt die Spitze auf ca. 0,7 V.

---

## Ansteuerung

Direkt an einem Mikrocontrollerpin (max. 20–40 mA) ist ein Relais meist nicht betreibbar. Ein NPN-Transistor dient als Verstärker:

:::formel
µC-Pin → R_B (1–10 kΩ) → Basis NPN
Kollektor NPN → Relais-Spule → VCC
Freilaufdiode parallel zur Spule (Kathode zu VCC)
:::

Fertige Relaismodule (z.B. Arduino-kompatibel) integrieren bereits Transistor, Freilaufdiode und Optokoppler für zusätzliche Trennung.

---

## Prellzeit

Mechanische Kontakte prellen beim Schalten: In den ersten 5–20 ms öffnen und schliessen sie mehrfach schnell hintereinander. Für digitale Eingänge muss dieses Prellen durch Software (Debouncing) oder Hardware (RC-Glied) unterdrückt werden.

---

## Schütz

Ein Schütz ist ein industriell ausgelegtes Relais für grosse Ströme und Dauerbetrieb. Schütze sind für Millionen von Schaltspielen zertifiziert (IEC 60947), haben zusätzliche Hilfskontakte für Meldungen und Verriegelungen und werden typisch in Motorsteuerungen und Drehstromanlagen eingesetzt.

---

## Auswahlkriterien

| Kriterium | Bedeutung |
|---|---|
| Spulenspannung | Meist 5 V, 12 V, 24 V DC oder 230 V AC |
| Kontaktstrom | Max. Laststrom (Gleichstrom ist kritischer als Wechselstrom) |
| Schaltspannung | Max. Spannung am Kontakt |
| Schaltspiele | Mechanisch und elektrisch unterschiedlich |
| Schutzklasse | IP-Klasse für Feuchtigkeit und Staub |
