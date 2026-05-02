---
title: Fehlersuche auf der Leiterplatte
kategorie: MT
tags: [fehlersuche, debugging, PCB, kurzschluss, spannungsmessung, strommessung, wärmebildkamera, halbierungsmethode]
symbol: —
einheit: —
---

Systematisches Vorgehen spart Zeit. Wer planlos misst, sucht lange. Wer strukturiert vorgeht, findet den Fehler in wenigen Schritten.

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom-, Spannungs-, Widerstandsmessung]]
- [[Oszilloskop: Aufbau & Bedienung]]
:::
:::vbox
**Verwandte Artikel**
- [[Tastkopf 1:1 vs. 10:1]]
- [[Triggerung]]
- [[Fehlerbilder Löten]]
:::
:::

---

## Grundsatz: Vom Einfachen zum Komplexen

Bevor gemessen wird: Sichtprüfung. Viele Fehler sind sichtbar — kalte Lötstellen, Kurzschluss zwischen Pads, vergessener Jumper, verpolt eingelöteter Kondensator.

## Schritt 1: Versorgungsspannungen prüfen

Das Gerät lässt sich nicht einschalten? Zuerst die Versorgung messen, bevor man die Logik verdächtigt.

**Messreihenfolge**:
1. Eingangsspannung (nach Sicherung, Stecker, Schalter)
2. Ausgang des Spannungsreglers oder Schaltnetzteils
3. Spannung direkt an den VCC-Pins der ICs
4. GND-Verbindungen prüfen (Durchgang mit Multimeter)

Wenn die Versorgung stimmt aber nichts passiert: weiter mit Schritt 2.

## Schritt 2: Kurzschluss lokalisieren

Verdacht auf Kurzschluss an VCC oder GND?

1. Widerstand zwischen VCC und GND messen (Schaltung spannungsfrei!)
2. Ist er nahe 0 Ω: Kurzschluss vorhanden
3. Gerät an eine strombegrenzte Versorgung anschliessen (Current-Limit auf 100 mA setzen)
4. Mit der Wärmebildkamera oder durch Berühren das heisse Bauteil finden
5. Alternativ: Spannung langsam erhöhen und mit Multimeter im Strommodus die heisseste Stelle ertasten

## Schritt 3: Taktsignale und Reset

Läuft der Mikrocontroller überhaupt? Am Oszilloskop prüfen:

- Taktoszillator schwingt? (XTAL-Pins oder CLK-Ausgang)
- Reset-Pin korrekt (nicht dauerhaft low)?
- Bootvorgang startet? (erste Pegel an GPIO nach Power-On beobachten)

## Schritt 4: Kommunikation prüfen

Kein Lebenszeichen vom Mikrocontroller?

- UART-Debug-Port anschliessen, Bootmeldungen lesen
- JTAG/SWD-Debugger verbinden, prüfen ob der Chip erkannt wird
- SPI/I2C-Bus mit Protokolldecoder am Oszilloskop beobachten

## Schritt 5: Signalverfolgung

Einen bekannten Eingangspegel einspeisen und schauen, wo er aufhört. Pegel an jedem Knoten messen.

**Halbierungsmethode**: Bei einem langen Signalpfad in der Mitte messen. Fehler in erster oder zweiter Hälfte? Wieder halbieren bis der Fehler lokalisiert ist.

## Typische Fehlerquellen

| Symptom | Häufige Ursache |
|---|---|
| Gar keine Reaktion | Sicherung, Verpolung, fehlende Versorgung |
| Gerät startet, hängt sich auf | Watchdog, falsche Taktfrequenz, fehlerhafter Flash |
| Sporadische Abstürze | Versorgung bricht ein, Interrupt-Problem, Stack-Überlauf |
| Kommunikation fehlerhaft | Baudrate, Pull-ups, Pegelkonverter, Kabelkapazität |
| Bauteil heiss | Kurzschluss, Falschpolung, falscher Bauteilwert |
| Rauschen / Brummen | Masseschleife, fehlende Entkopplung, Layoutproblem |

## Hilfsmittel

**Wärmebildkamera**: Findet überhitzte Bauteile sofort.  
**Logikanalysator**: Digitale Protokolle aufzeichnen und dekodieren.  
**Strombegrenzte Versorgung**: Schützt die Schaltung bei Kurzschluss.  
**Funktionsgenerator**: Testeingangssignale erzeugen.

:::tip
Immer einen funktionierenden Referenzaufbau zum Vergleich bereithalten, wenn möglich. Direkte Messwertvergleiche sparen viel Zeit.
:::
