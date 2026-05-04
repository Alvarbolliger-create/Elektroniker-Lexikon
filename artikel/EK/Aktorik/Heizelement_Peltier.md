---
title: Heizelement / Peltier-Element
kategorie: EK
tags: [heizelement, peltier, thermostat, kühlung, wärme, thermoelektrisch, pid, pwm, ptc, tec]
symbol: P
einheit: W
---

Ein Heizelement gibt elektrische Energie als Wärme ab. Ein Peltier-Element pumpt Wärme von einer Seite zur anderen — je nach Stromrichtung heizt oder kühlt es. Beide werden in temperaturgesteuerten Systemen eingesetzt.

:::hbox
:::vbox
**Voraussetzungen**
- [[Transistor als Schalter]]
- [[PWM]]
:::
:::vbox
**Verwandte Artikel**
- [[Aktorik]]
- [[Sensorik]]
:::
:::vbox
**Führt weiter zu**
- [[PID Regler]]
- [[Bussystem-Aktor]]
:::
:::

---

## Heizelement

Ein Heizelement ist ein ohmscher Widerstand, der Strom vollständig in Wärme umwandelt. Der Wirkungsgrad ist per Definition 100 % (elektrisch auf thermisch).

:::formel
P = U * I = U^2 / R = I^2 * R
:::

Heizelemente werden per PWM oder bei Netzspannung per Phasenanschnittsteuerung geregelt.

| Typ | Merkmal | Einsatz |
|---|---|---|
| PTC-Keramik (Kaltleiter) | Widerstand steigt mit Temperatur → selbstlimitierend | Innenraumheizung, Luft-Vorwärmer |
| Nichrom-Heizdraht | Hohe Temperaturen möglich (> 1000 °C) | Industrieöfen, 3D-Drucker-Hotend |
| Silikon-Heizmatte | Flexibel, flächig | Rohre, Behälter, Freiflächenbeheizung |
| Quarzstrahler | Infrarotstrahlung direkt | Industrietrockner, Heizstrahler |

:::warning
Bei Heizelementen immer eine thermische Sicherung oder Thermoschutzschalter einplanen. Ein Regelungsfehler (z.B. festsitzender Transistor) führt sonst zu Dauerheizbetrieb und Brand.
:::

---

## Peltier-Element

Ein Peltier-Element (thermoelektrisches Modul, TEC — Thermoelectric Cooler) basiert auf dem Peltier-Effekt: Fliesst Strom durch die Verbindung zweier unterschiedlicher Halbleitermaterialien (N- und P-Typ), entsteht auf einer Seite Kälte und auf der anderen Wärme.

Durch Umpolung wechseln Kalt- und Warmseite. Damit ist ein einziges Element zum präzisen Heizen und Kühlen geeignet.

:::formel
Q_K = alpha * T_K * I - 0.5 * I^2 * R_TEC - K * delta_T
:::

:::monospace
Q_K     = Kühlleistung [W]
alpha   = Seebeck-Koeffizient [V/K]
T_K     = Temperatur Kaltseite [K]
delta_T = Temperaturdifferenz zw. Warm- und Kaltseite [K]
:::

---

## Wirkungsgrad des Peltier-Elements

Der Wirkungsgrad (COP — Coefficient of Performance) ist gering:

| Methode | COP typisch |
|---|---|
| Kompressionskältemaschine | 2–4 |
| Peltier-Element | 0,2–0,5 |

Für 1 W Kühlleistung werden typisch 3–8 W elektrische Leistung benötigt. Die überschüssige Wärme muss auf der Warmseite abgeführt werden (Kühlkörper, Lüfter, Wasserkühlung).

---

## Temperaturregelung

Beide Komponenten werden typisch über einen [[PID Regler]] geregelt:

- Sensor: NTC-Thermistor, PT100 oder PT1000 für genaue Messung
- Stellglied: PWM auf Heizelement oder Peltier
- Regelgrösse: Temperatur [°C oder K]

:::tip
Für einfache Anwendungen (Ein/Aus-Thermostat) reicht ein Zweipunkt-Regler. Für genaue Temperaturstabilisierung (z.B. Laserdiode auf ±0,01 °C) wird ein PID-Regler benötigt.
:::

---

## Anwendungen

| Komponente | Einsatz |
|---|---|
| Heizelement (PTC) | Raumheizung, Industrieöfen, 3D-Drucker-Hotend |
| Peltier | Laserdiodenkühlung, Weinkühlschrank, CPU-Kühler |
| Peltier (Heizmodus) | Temperaturstabilisierte Messkammern |
| Kombination | Laborinstrumente, Thermostate mit engem Regelband |
