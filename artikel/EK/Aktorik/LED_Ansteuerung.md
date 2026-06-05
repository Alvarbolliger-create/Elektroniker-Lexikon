---
title: LED-Treiber / Licht-Aktor
kategorie: EK
tags: [led, led-treiber, vorwiderstand, pwm, konstantstrom, high-power-led, dimming, ws2812, pt4115, licht-aktor]
symbol: —
einheit: —
---

Eine LED-Treiberschaltung versorgt LEDs sicher mit definiertem Strom. Spannung direkt an eine LED anlegen ohne Strombegrenzung zerstört sie sofort — auch kurz.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[PWM]]
- [[Transistor als Schalter]]
:::
:::vbox
**Verwandte Artikel**
- [[Buck Converter]]
- [[Optokoppler]]
:::
:::vbox
**Führt weiter zu**
- [[Bussystem-Aktor]]
:::
:::

---

## Vorwiderstand

Die einfachste Strombegrenzung für kleine LEDs. Der Widerstand begrenzt den Strom abhängig von der Versorgungsspannung:

:::formel
R = (U_V - U_F) / I_LED
P_R = (U_V - U_F) * I_LED
:::

:::formel
U_V   = Versorgungsspannung [V]
U_F   = Vorwärtsspannung LED [V]   (1,8–2,2 V rot/gelb, 2,8–3,5 V blau/weiss)
I_LED = gewünschter Strom [A]      (typisch 5–20 mA für Standard-LEDs)
:::

**Rechenbeispiel: Rote LED an 12 V**

:::formel
U_V  = 12 V
U_F  = 2 V
I    = 20 mA

R    = (12 V - 2 V) / 20 mA = 500 Ω  → 470 Ω Normwert
P_R  = (12 V - 2 V) * 20 mA = 200 mW → 0,5-W-Widerstand wählen
:::

:::warning
Bei hohen Versorgungsspannungen (12 V, 24 V) fällt fast die gesamte Verlustleistung am Vorwiderstand ab. Ab mehreren LEDs oder Dauerbetrieb ist eine Konstantstromlösung effizienter.
:::

---

## PWM-Dimming

Pulsweitenmodulation (PWM) stellt die Helligkeit ein, ohne den Spitzenstrom zu ändern. Das menschliche Auge integriert Frequenzen oberhalb von ca. 100 Hz als konstante Helligkeit.

:::formel
Helligkeit [%] = Duty Cycle [%]
:::

Vorteil gegenüber Strom-Dimming: Die Spektralfarbe der LED bleibt konstant, da der Strom im EIN-Zustand immer gleich ist.

---

## Konstantstromquellen

Für präzise Helligkeit und Unabhängigkeit von der Versorgungsspannung: Konstantstromregler.

Einfache Lösungen:
- **CL2N3 / NSI45020**: Zwei-Bein-Konstantstromdiode, kein IC nötig
- **AMC7135**: 350 mA Konstantstrom, SOT-89-Gehäuse
- **Transistorschaltung**: NPN mit Emitterwiderstand als einfacher Konstantstromregler

Für High-Power-LEDs (1–50 W) braucht es einen Buck- oder Boost-LED-Treiber-IC:

| IC | Topologie | Strom | Besonderheit |
|---|---|---|---|
| PT4115 | Buck | bis 1,2 A | Günstig, weit verbreitet |
| LM3409 | Buck | flexibel | Einstellbar, Texas Instruments |
| HV9910 | Buck/Boost | bis 1 A | Universell, hohe Spannung |

---

## Adressierbare LEDs (WS2812, SK6812)

WS2812B und SK6812 sind RGB-LEDs mit integriertem Treiber-IC. Über ein einziges Datenkabel wird Farbe und Helligkeit jeder LED einzeln gesteuert.

Signalprotokoll: 800 kHz Bitstream, 24 Bit pro LED (8 Bit je Farbe). LEDs werden in Reihe geschaltet, jede gibt das Signal weiter.

:::formel
Controller → [LED 1] → [LED 2] → [LED 3] → ...
             R,G,B       R,G,B      R,G,B
:::

Bibliotheken: FastLED, Adafruit NeoPixel (Arduino/ESP32).

:::warning
WS2812-Datenleitungen sind empfindlich auf Leitungsimpedanz und Reflexionen. Bei langen Zuleitungen (> 50 cm) einen 300–500 Ω Widerstand direkt am Datenpunkt einbauen, um Schwingungen zu dämpfen.
:::

---

## High-Power-LEDs

LEDs mit 1–50 W brauchen:
- Konstantstromtreiber (Buck oder Boost)
- Kühlkörper (thermischen Widerstand beachten: T_junction < 125 °C)
- Optik (Linsen oder Reflektoren)

Der thermische Widerstand bestimmt die Betriebstemperatur des Chips:

:::formel
T_J = T_ambient + P * R_theta_JA
:::

:::formel
T_J         = Chip-Temperatur [°C]
T_ambient   = Umgebungstemperatur [°C]
P           = Verlustleistung [W]
R_theta_JA  = thermischer Widerstand Chip-Umgebung [K/W]
:::

---

## Anwendungen als Licht-Aktor

- Architekturbeleuchtung (dimmbar per PWM oder DALI)
- Industriebeleuchtung (Hochregallager, Fertigungshallen)
- Signallichter (Status-LEDs, Ampeln, Warn-Leuchten)
- Displays und Backlighting
- Grow-Lights (Pflanzenwachstum, spektral abstimmbar)
