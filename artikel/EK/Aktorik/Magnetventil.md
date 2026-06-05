---
title: Magnetventil
kategorie: EK
tags: [magnetventil, solenoid, pneumatik, hydraulik, spule, ventil, fluid, no, nc, proportional]
symbol: —
einheit: —
---

Ein Magnetventil (Solenoid-Ventil) öffnet oder schliesst eine Fluidleitung durch einen Elektromagneten. Es wird in pneumatischen, hydraulischen und flüssigkeitsführenden Systemen eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Relais]]
- [[Transistor als Schalter]]
:::
:::vbox
**Verwandte Artikel**
- [[Linearmotor]]
- [[Aktorik]]
:::
:::vbox
**Führt weiter zu**
- [[Bussystem-Aktor]]
:::
:::

---

## Aufbau und Wirkprinzip

Eine bestromte Spule erzeugt ein Magnetfeld, das einen Metallkolben (Anker) anzieht. Der Anker öffnet oder schliesst mechanisch den Ventilsitz, durch den das Fluid strömt.

| Typ | Normalstellung | Bei Bestromung |
|---|---|---|
| NC (normally closed) | Ventil geschlossen | Ventil öffnet |
| NO (normally open) | Ventil offen | Ventil schliesst |
| Bistabil | Hält letzte Position | Braucht Umschalt-Impuls |

---

## Elektrische Ansteuerung

DC-Magnetventile (12 V, 24 V) werden direkt über einen Transistor oder ein Relais geschaltet. Da die Spule induktiv ist, gilt auch hier:

:::warning
Freilaufdiode parallel zur Spule einbauen. Beim Abschalten zerstört der induktive Spannungsstoss die Schalthalbleiter.
:::

AC-Magnetventile (230 V) brauchen keine Freilaufdiode, aber die Ansteuerung muss für die Hochspannung ausgelegt sein. Typisch: Optokoppler oder Solid-State-Relais als Zwischenstufe.

---

## Proportionalventile

Einfache Magnetventile sind EIN/AUS. Proportionalventile öffnen stufenlos proportional zum Spulenstrom. Das ermöglicht eine analoge Durchflussregelung:

:::formel
Q = k * I
:::

:::formel
Q = Durchfluss
k = Ventilkonstante
I = Spulenstrom
:::

Angesteuert über PWM mit Tiefpassfilter oder über einen geregelten Konstantstromtreiber.

---

## Wichtige Kenngrössen

| Parameter | Bedeutung |
|---|---|
| Nennspannung | Betriebsspannung der Spule |
| Nennstrom | Spulenstrom bei Nennspannung |
| Schaltdruck | Maximaler Fluiddruck |
| Schaltzeit | Öffnungs-/Schliesszeit (typisch 10–200 ms) |
| Kv-Wert | Durchflusskoeffizient |
| Schutzart | IP-Klasse (wichtig bei Wasser, Öl, Staub) |

---

## Anwendungen

- Pneumatische Zylinder ein-/ausfahren (Industrieroboter, Pressen)
- Gartenbewässerung (Wasserventile)
- Gasleitungen in Heizungen
- Laborautomation (Dosierventile, Chromatografie)
- Fahrzeugtechnik (ABS, Getriebesteuerung)
