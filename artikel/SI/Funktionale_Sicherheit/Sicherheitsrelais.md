---
title: Sicherheitsrelais
kategorie: SI
tags: [sicherheitsrelais, safety relay, zweikanalig, quittierung, PLd, zwangsgeführt, SIL, feedback, PILZ, selbstüberwachung]
symbol: —
einheit: —
---

Ein Sicherheitsrelais wertet Sicherheitssignale (Not-Halt, Schutztür, Lichtschranke) sicher aus. Es kann selbst bei einem internen Fehler die Maschine sicher abschalten.

:::hbox
:::vbox
**Voraussetzungen**
- [[SIL und PL]]
- [[Not-Halt]]
:::
:::vbox
**Verwandte Artikel**
- [[Zweikanalige Abschaltung]]
:::
:::

---

## Warum ein spezielles Relais?

Ein normales Relais kann kleben (Kontakt bleibt haften). Bei einem Sicherheitsrelais verhindern zwangsgeführte Kontakte diesen Fehler. Wenn ein Schliesskontakt klebt, können die Öffnerkontakte nicht mehr öffnen. Das Relais erkennt das und verriegelt.

## Aufbau und Auswertung

Ein Sicherheitsrelais hat typisch:
- Zwei separate Eingangskreise für zweikanalige Sensoren
- Interne Selbstüberwachung (Querschlusserkennung, Kurzschlusstest)
- Zwangsgeführte Ausgangsrelais
- Rückmeldekontakt (Feedback) zur externen Überwachung

Beim Einschalten testet das Relais selbst alle Funktionen durch.

## Zweikanalige Auswertung

Ein Not-Halt-Taster hat zwei Öffner. Kanal 1 und Kanal 2 werden separat zum Sicherheitsrelais geführt. Das Relais vergleicht:
- Schalten beide Kanäle gleichzeitig? (Toleranzfenster: typisch 100-500 ms)
- Wenn nicht: Fehler, Freigabe bleibt gesperrt.

## Quittierung

Nach dem Auslösen muss die Quittierungstaste betätigt werden. Das Relais prüft ob der Eingang wieder ordnungsgemäss geschlossen ist, bevor es die Ausgänge freigibt.

Quittierung kann manuell (Taster) oder automatisch sein. Automatische Quittierung nur erlaubt wenn kein Eingriff von Personen nötig ist.

## Kompakte Sicherheits-SPS

Für komplexere Anwendungen ersetzen Sicherheits-SPS (PILZ PSS, Siemens F-CPU, Schmersal SRB) diskrete Sicherheitsrelais. Sie ermöglichen flexiblere Logik bei gleich hoher Sicherheitsstufe.
