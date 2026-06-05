# Offene Querverweise (Platzhalter)

Diese Datei listet alle Verweise von ET-Artikeln auf andere Themenbereiche,
die noch nicht gesetzt werden können weil die Zielstruktur noch offen ist.

---

## ET → EK (Elektronik)

| Von (ET)                          | Nach (EK)                            | Grund                                      |
|---|---|---|
| Grundlagen/Leiterwiderstand       | EK/Halbleiter/Halbleitermaterial      | Leitfähigkeit Halbleiter vs. Metall        |
| Grundlagen/Elektrisches_Feld      | EK/Halbleiter/MOSFET (noch nicht da) | Gatefeld steuert Kanal                     |
| Grundlagen/Strom_Spannung_Widerstand | EK/Halbleiter/Diode                | Ohmsches Gesetz gilt nicht für Dioden      |
| Magnetfelder/Lorentzkraft         | EK/Motoren/DC_Motor                   | Kraftwirkung auf Leiter = Motorprinzip     |
| Magnetfelder/Elektromagnet        | EK/Motoren/DC_Motor                   | Elektromagnet im Motor                     |
| Magnetfelder/Elektromagnet        | EK/Halbleiter/TVS_Varistor            | Freilaufdiode bei Spulenschaltungen        |
| Magnetisierungskurve              | EK/Stromversorgung/Flyback_Forward    | Kernsättigung bei Schaltnetzteilen         |
| Spule/Spule_Typen                 | EK/Stromversorgung/Flyback_Forward    | Speicherdrossel, Transformator in SNT      |
| Kondensator/Kondensator_Typen     | EK/Stromversorgung/Flyback_Forward    | Glättungskondensator                       |
| Wechselstrom/Resonanz             | EK/Filter/Filtercharakteristik        | Resonanzfilter = LC-Filter                 |
| Wechselstrom/LC_Filter            | EK/Filter/Filter_Grundlagen           | LC-Filter vs. RC-Filter Vergleich          |
| Drehstrom/Drehstrom_Grundlagen    | EK/Motoren/BLDC                       | BLDC = dreiphasiger Drehstrom              |
| Drehstrom/Drehstrom_Grundlagen    | EK/Motoren/Schrittmotor               | Mehrphasen-Ansteuerung                     |
| Drehstrom/Drehstrom_Grundlagen    | EK/Motoren/Frequenzumrichter (fehlt)  | VFD erzeugt Drehstrom via PWM aus DC       |
| Schaltkreise/Leistungsanpassung   | EK/OPV/Rueckkopplungsarten            | Impedanzanpassung mit OPV                  |

---

## ET → SH (Software & Hardware)

| Von (ET)                          | Nach (SH)                            | Grund                                      |
|---|---|---|
| Wechselstrom/Sinuswellen          | SH/Grundlagen/Signale                 | PWM als Sinusannäherung                    |
| Kondensator/Konstantstrom_Laden   | SH (ADC-Artikel fehlt noch)           | Sägezahn-ADC basiert auf Konstantstrom     |
| Wechselstrom/RLC_Reihenschaltung  | SH (Filter-Artikel fehlt)             | Digitale Filter als Pendant zu analogen    |

---

## ET → MT (Messtechnik)

| Von (ET)                          | Nach (MT)                            | Grund                                      |
|---|---|---|
| Grundlagen/Strom_Spannung_Widerstand | MT/Multimeter/Multimeter            | Messen mit Multimeter                      |
| Grundlagen/Leiterwiderstand       | MT/Vierleitermessung/Vierleitermessung | Genaue R-Messung                         |
| Schaltkreise/Wheatstone_Bruecke   | MT/Multimeter/Innenwiderstand_Messfehler | Brücke als Messprinzip                 |
| Wechselstrom/Sinuswellen          | MT/Oszilloskop/Tastkopf               | Sinus messen mit Oszilloskop               |

---

## Fehlende Artikel (müssen noch erstellt werden)

| Artikel                           | Ordner                | Bemerkung                                  |
|---|---|---|
| ~~Widerstand (Bauformen, Farbcode)~~ | ~~ET/Grundlagen/~~ | ✓ Stub erstellt — PORT aus ET_alt/Bauelemente/Widerstand.md |
| ~~NTC & PTC~~                     | ~~ET/Grundlagen/~~    | ✓ Stub erstellt — PORT aus ET_alt/Bauelemente/NTC_PTC.md    |
| EK/Motoren/Frequenzumrichter      | EK/Motoren/           | VFD fehlt komplett                         |

---

## Motoren-Erweiterung (geplant)

**Strukturänderung:** Ordner `ET/Drehstrom/` → `ET/Motoren/` umbenennen.
Drehstrom-Artikel bleiben, neue Motorartikel kommen dazu.

### Neue Artikel (Prio-Reihenfolge)

| Artikel | Inhalt | Abhängigkeiten |
|---|---|---|
| Asynchronmotor | Funktionsprinzip, Schlupf, Anlauf, Kennlinie, Schutzklassen | Drehstrom Grundlagen |
| BLDC / PMSM | Aufbau Innen-/Aussenläufer, Kommutierung, 3-Phasen-Ansteuerung | Drehstrom Grundlagen |
| Frequenzumrichter (VFD) | Gleichrichten → Zwischenkreis → PWM-Inverter, U/f-Kennlinie, Schutzfunktionen | Drehstrom Grundlagen |
| Schrittmotor | Vollschritt / Halbschritt / Microstepping, offene Regelung, Drehmomentverlust | — |
| DC-Motor | Bürsten, Kommutator, Kennlinie, H-Brücke | Lorentzkraft |
| Encoder / Drehgeber | Inkremental vs. absolut, A/B-Signal, Auflösung | Sensor vs. sensorlos |

### Innenläufer vs. Aussenläufer

| Typ | Rotor | Vorteile | Anwendung |
|---|---|---|---|
| Innenläufer | Magnet innen, Wicklung aussen | Kompakt, schnell | Industrieantriebe, E-Autos |
| Aussenläufer | Magnet aussen dreht sich, Wicklung steht | Grosses Trägheitsmoment, ruhiger Lauf | Drohnen, Lüfter, Direktantrieb |
