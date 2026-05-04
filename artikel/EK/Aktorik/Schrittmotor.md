---
title: Schrittmotor
kategorie: EK
tags: [schrittmotor, stepper, vollschritt, halbschritt, mikroschritt, cnc, schrittwinkel, a4988, drv8825, tmc, open-loop]
symbol: M
einheit: °/Schritt
---

Der Schrittmotor dreht sich in definierten Winkelschritten und kann Positionen ohne Positionsrückmeldung halten. Er wird über eine spezielle Steuerelektronik mit einer Folge von Stromimpulsen angesteuert.

:::hbox
:::vbox
**Voraussetzungen**
- [[H-Brücke]]
- [[PWM]]
:::
:::vbox
**Verwandte Artikel**
- [[Motor-Treiber-IC]]
- [[DC Motor]]
- [[Servomotor]]
:::
:::vbox
**Führt weiter zu**
- [[Aktor mit Rückmeldung]]
:::
:::

---

## Aufbau und Wirkprinzip

Mehrere Statorwicklungen (Phasen) werden der Reihe nach bestromt. Das rotierende Magnetfeld zieht den Rotor schrittweise mit. Jeder Schritt entspricht einem festen Winkel.

Typischer Schrittwinkel: **1,8° pro Schritt = 200 Schritte pro Umdrehung**.

Bipolarer Schrittmotor (vier Leitungen): höheres Drehmoment, braucht eine H-Brücke pro Phase. Unipolarer Schrittmotor (sechs bis acht Leitungen): einfachere Ansteuerung, weniger Drehmoment.

---

## Betriebsmodi

| Modus | Auflösung | Eigenschaft |
|---|---|---|
| Vollschritt | 200 Schritte/U | Maximales Drehmoment |
| Halbschritt | 400 Schritte/U | Ruhiger, mittleres Drehmoment |
| Mikroschritt (1/16) | 3200 Schritte/U | Sehr ruhig, geringeres Drehmoment |
| Mikroschritt (1/256) | 51200 Schritte/U | Extrem fein, schwaches Drehmoment |

Beim Mikroschritt werden die Phasenströme sinusförmig moduliert, um Zwischenpositionen zu erreichen.

---

## Ansteuerung

Schrittmotor-Treiber-ICs (z.B. A4988, DRV8825, TMC2209) integrieren zwei H-Brücken, Chopper-Stromregelung und Mikroschrittteilung. Das Steuersignal von der übergeordneten Logik ist einfach:

:::monospace
STEP _____|‾|_|‾|_|‾|_|‾|_     → ein Impuls pro Schritt
DIR  ________/‾‾‾‾‾‾‾‾‾‾‾     → Drehrichtung
:::

Der Treiber regelt den Phasenstrom auf einen einstellbaren Maximalwert (Current Limiting). Der Motor wird mit höherer Spannung als der Nennspannung betrieben — der Treiber begrenzt den Strom über PWM-Chopper.

:::warning
Schrittmotor-Treiber nie unter Last vom Motor trennen. Die Spuleninduktivität erzeugt Spannungsspitzen, die den Treiber sofort zerstören.
:::

---

## Drehmoment und Drehzahl

Das Drehmoment sinkt bei hoher Schrittfrequenz stark. Zu schnelle Folge: der Motor verliert Schritte (Schrittverlust) ohne Fehlermeldung.

:::monospace
Drehmoment
  ↑
  |‾‾\
  |   \
  |    \______
  +----------→ Schrittfrequenz
:::

Beschleunigungs-Rampen (langsam starten, Frequenz hochfahren) sind zwingend, um Schrittverlust zu vermeiden.

---

## Schrittmotortreiber Vergleich

| IC | Strom | Mikroschritt | Besonderheit |
|---|---|---|---|
| A4988 | 2 A | bis 1/16 | Günstig, weit verbreitet |
| DRV8825 | 2,5 A | bis 1/32 | Mehr Strom als A4988 |
| TMC2208 | 2 A | bis 1/256 | Sehr leiser StealthChop-Modus |
| TMC2209 | 2 A | bis 1/256 | StallGuard (erkennt Schrittverlust), UART |

:::tip
TMC-Treiber wählen, wenn leiser Betrieb wichtig ist (3D-Drucker, Laborgeräte). Der StealthChop-Modus eliminiert fast alle hörbaren Motorgeräusche.
:::
