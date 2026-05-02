---
title: LED-Ansteuerung
kategorie: EK
tags: [LED, vorwiderstand, PWM, konstantstrom, WS2812, helligkeit, high-power-LED, SK6812, U_F, dimming, PT4115]
symbol: —
einheit: —
---

LEDs brauchen eine definierte Strombegrenzung. Spannung direkt anlegen ohne Strombegrenzung zerstört sie sofort.

:::hbox
:::vbox
**Voraussetzungen**
- [[Diode]]
- [[PWM]]
- [[BJT Transistor]]
:::
:::vbox
**Verwandte Artikel**
- [[Optokoppler]]
- [[Buck Converter]]
:::
:::

---

## Vorwiderstand

Die einfachste Strombegrenzung. Der Widerstand begrenzt den Strom abhängig von der Versorgungsspannung:

```
R = (U_versorgung - U_F) / I_LED
P_R = (U_versorgung - U_F) * I_LED     # Verlustleistung am Widerstand
```

Typische Werte:
- U_F: 1.8–2.2 V (rot/gelb), 2.8–3.5 V (blau/weiss/grün)
- I_LED: 5–20 mA für Standardanzeige-LEDs

**Rechenbeispiel: LED an 24 V** (häufige Industriespannung)

```
U_versorgung = 24 V
U_F          = 2 V   (rote LED)
I_LED        = 20 mA

R = (24 V - 2 V) / 20 mA = 22 V / 0.02 A = 1100 Ω → 1 kΩ (nächster Normwert)
P_R = 22 V * 20 mA = 440 mW
```

Einen 0.5-W-Widerstand würde man bei 440 mW bereits überlasten. Mindestens **1 W** wählen, besser 2 W für Reserve.

:::warning
Bei hohen Versorgungsspannungen (12 V, 24 V) fällt fast die gesamte Spannung am Vorwiderstand ab — er wird warm und die Schaltung ist ineffizient. Ab ~5 Stück LEDs parallel oder bei Dauerbetrieb ist eine Konstantstromquelle oder ein PWM-gesteuerter Schaltregler effizienter.
:::

Nachteil: Helligkeit ändert sich mit Versorgungsspannung.

## PWM-Dimming

Durch Pulsweitenmodulation lässt sich die Helligkeit einstellen ohne den Strom zu ändern. Das menschliche Auge integriert bei Frequenzen über ca. 100 Hz.

```
Helligkeit (%) = Tastverhältnis (%)
```

Vorteil: Farbton bleibt konstant, da der Strom gleich bleibt.

## Konstantstromquellen

Für präzise Helligkeit und unabhängig von Versorgungsspannung: Konstantstromregler (z.B. CL2N3, AMC7135) oder einfacher Transistor-Schaltung mit Emitterwiderstand.

Notwendig für High-Power-LEDs (1 W, 3 W, 10 W) und LED-Stripes.

## WS2812 und adressierbare LEDs

WS2812B und SK6812 sind RGB-LEDs mit integriertem Treiber-IC. Über ein einziges Datenkabel (800 kHz Signalprotokoll) werden Farbe und Helligkeit jeder einzelnen LED gesteuert.

Bis zu hunderte LEDs in Reihe, jede einzeln adressierbar. Bibliotheken: FastLED, Adafruit NeoPixel für Arduino/ESP.

## Hochleistungs-LEDs

High-Power-LEDs (1-50 W) brauchen:
- Konstantstromtreiber (Boost/Buck)
- Kühlkörper (thermischer Widerstand beachten)
- Optik (Linsen, Reflektoren)

LED-Treiberchips: PT4115, LM3409, HV9910.

:::warning
LEDs niemals ohne Strombegrenzung direkt an eine Spannungsquelle anschliessen. Selbst eine kurze Spitze überschreitet den maximalen Strom und beschädigt die LED dauerhaft.
:::
