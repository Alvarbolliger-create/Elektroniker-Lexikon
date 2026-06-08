---
title: Relais
kategorie: EK
kapitel: Aktorik
tags: [relais, elektromagnet, anker, no, nc, com, freilaufdiode, prellen, galvanische trennung, schütz, spulenstrom, transistortreiber]
groessen: I_S|Spulenstrom|A; U_S|Spulenspannung|V; R_B|Basiswiderstand|Ω; U_CE_sat|Sättigungsspannung|V
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Aktorik Grundlagen]]
- [[BJT Grundlagen]]
- [[MOSFET Anwendungen]]
:::
:::vbox
**Verwandte Artikel**
- [[Optokoppler]]
- [[H-Brücke]]
:::
:::vbox
**Führt weiter zu**
- [[DC-Motor]]
- [[Heizelement & Peltier]]
:::
:::

---

Ein Relais ist ein **elektromagnetisch betriebener Schalter**. Ein kleines Steuersignal (Logikpegel, wenige mA) schaltet einen galvanisch getrennten Leistungskreis — typisch wird damit eine 3.3-V-Logik mit einem 230-V-Netz verbunden.

## Aufbau und Wirkprinzip

Eine bestromte Spule erzeugt ein Magnetfeld, das einen beweglichen Anker anzieht. Der Anker betätigt mechanische Kontakte. **Steuerstromkreis (Spule) und Lastkreis (Kontakte) sind galvanisch getrennt** — der wichtigste Vorteil gegenüber Halbleiterschaltern.

## Kontakttypen

| Kontaktart | Kürzel | Normalzustand | Bei Erregung |
|---|---|---|---|
| Schliesser | NO (Normally Open) | Offen | Geschlossen |
| Öffner | NC (Normally Closed) | Geschlossen | Offen |
| Wechsler | COM | Verbunden mit NC | Wechselt zu NO |

## Freilaufdiode — zwingend erforderlich

Die Relais-Spule ist induktiv. Beim Abschalten der Erregung entsteht ein induktiver Spannungsstoss (L·di/dt), der den ansteuernden Transistor oder µC-Pin zerstört.

:::warning
Relais-Spule **niemals** ohne Freilaufdiode an einem Halbleiterausgang betreiben. Der Spannungsstoss kann mehrere 100 V erreichen und den Ausgangspin sofort zerstören.
:::

Die Freilaufdiode wird **parallel zur Spule** in Sperrrichtung zur Versorgung eingebaut. Beim Abschalten leitet sie und begrenzt die Spitze auf ca. 0.7 V.

**Kehrseite — Abfallverzögerung:** Die Diode bietet dem Spulenstrom nach dem Abschalten einen geschlossenen Umlaufpfad (Spule–Diode). Die in der Induktivität gespeicherte Energie baut sich dadurch nur langsam über die Diodendurchlassspannung (≈ 0.7 V) ab statt schlagartig — der Strom (und damit das Magnetfeld) klingt deutlich langsamer ab als ohne Diode. Der Anker fällt deshalb **verzögert** ab (Abfallverzögerung, je nach Spule einige ms bis ~10 ms zusätzlich). Wer eine schnelle Abschaltung braucht, ersetzt die einfache Diode durch eine Diode + Z-Diode/Suppressordiode in Serie — das begrenzt die Spannungsspitze auf einen höheren, aber definierten Wert und baut die Energie schneller ab.

:::schematic Relais mit Freilaufdiode: NPN-Transistor (Kollektor oben, Emitter nach GND). Relaisspule von +U_B nach Kollektor. Freilaufdiode parallel zur Spule (Kathode an +U_B, Anode am Kollektor) — in Sperrrichtung zur Versorgung. Beim Abschalten: Induktionsspannung treibt Strom durch Diode, begrenzt Spannungsspitze auf +U_B + 0.7 V. Basis über R_B von µC-Pin gesteuert
/Diagramm/relais_freilaufdiode.svg
:::

## Transistor-Ansteuerung

Ein µC-Pin (typisch 3.3–5 V, max. 20 mA) reicht meist nicht aus, um eine Relais-Spule direkt zu treiben (typisch 50–150 mA). Ein NPN-Transistor übernimmt die Verstärkung:

:::formel
I_S     = U_Spule / R_Spule              # Spulenstrom
I_B     = I_S / B_min                   # Mindest-Basisstrom (B_min ≈ 10..30 verwenden)
R_B     = (U_µC - U_BE) / I_B           # Basiswiderstand
:::

:::schematic NPN-Transistor als Relais-Treiber: µC-Pin → R_B (Basiswiderstand) → Basis NPN. Kollektor: Relaisspule (Anode) → +U_B (Spulen-Versorgung). Freilaufdiode parallel zur Spule. Emitter direkt nach GND. Relais-Kontakte NO/NC/COM für Lastkreis (galvanisch getrennt). R_B = (U_µC − 0.7) / I_B berechnet
/Diagramm/relais_transistortreiber.svg
:::

**N-Kanal-MOSFET** (z.B. 2N7000): Einfacher als BJT — kein Basisstrom nötig, Gate direkt über R_G (1–10 kΩ) an µC-Pin.

## Kontaktprellen (Bouncing)

Mechanische Kontakte prellen beim Schalten: In den ersten 5–20 ms öffnen und schliessen sie mehrfach schnell. Für digitale Eingaben muss das Prellen durch Software (Entprellzeit ≥ 20 ms) oder Hardware (RC-Glied + Schmitt-Trigger) unterdrückt werden.

## Auswahlkriterien

| Kriterium | Bedeutung |
|---|---|
| Spulenspannung | Meist 5 V, 12 V, 24 V DC |
| Kontaktstrom | Max. Laststrom (DC kritischer als AC wegen Lichtbogen) |
| Schaltspannung | Max. Spannung am Kontakt |
| Schaltspiele | Mechanisch: 10⁷, elektrisch: 10⁵ (Last abhängig) |
| Schaltzeit | Anzug: 5–15 ms, Abfall: 3–10 ms |

## Vergleich Relais vs. Solid-State-Relay (SSR)

| Eigenschaft | Relais | Solid-State-Relay |
|---|---|---|
| Galvanische Trennung | Ja (mechanisch) | Ja (Optokoppler) |
| Kontaktwiderstand | 0.05–0.1 Ω | 0 (kein Kontakt) |
| Schaltgeschwindigkeit | 5–15 ms | µs |
| Schaltspiele | Begrenzt | Unbegrenzt |
| Prellen | Ja | Nein |
| AC-Last | Sehr gut | Sehr gut (Nulldurchgang) |
| DC-Last | Gut | Schwieriger (MOSFET nötig) |
| Preis | Günstig | Teurer |

## Schütz

Ein **Schütz** ist ein industriell ausgelegtes Relais für grosse Ströme und Dauerbetrieb. Schütze sind für Millionen Schaltspiele zertifiziert (IEC 60947), haben Hilfskontakte für Meldungen/Verriegelungen und werden typisch in Motorsteuerungen und Drehstromanlagen eingesetzt.
