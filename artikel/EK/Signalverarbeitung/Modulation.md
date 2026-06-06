---
title: Modulation
kategorie: EK
kapitel: Signalverarbeitung
tags: [modulation, AM, FM, PM, ASK, FSK, PSK, QAM, PWM, PAM, PCM, PPM, PDM, modulationsgrad, träger, NF, analog, digital, puls-modulation, tastverhältnis]
groessen: m|Modulationsgrad|—; U_mod_hat|Amplitude NF-Schwingung|V; U_T_hat|Amplitude Trägerschwingung|V; D|Tastverhältnis|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Verstärkung & Dämpfung]]
- [[Quarzoszillator]]
:::
:::vbox
**Verwandte Artikel**
- [[Klirrfaktor]]
:::
:::vbox
**Führt weiter zu**
- [[Stromversorgung Grundlagen]]
:::
:::

---

Modulation überlagert ein Nutzsignal (NF, Daten) auf einen Trägersignal (HF-Welle), um es zu übertragen. Am Empfänger wird das Original durch Demodulation zurückgewonnen.

## Modulationsgrad (aus dem Spick)

:::schematic AM-Signal Vollmodulation (m=1): Zeitverlauf oben. Trägersignal (hochfrequent, Amplitude U_T_hat). NF-Hüllkurve (niederfrequent, Amplitude U_mod_hat = U_T_hat bei Vollmodulation). AM-Signal = Träger × (1 + m×sin(ω_NF×t)). Eingezeichnet: Maximalamplitude (U_T + U_mod), Minimalamplitude (U_T − U_mod bei Untermodulation > 0). Untermodulation m<1, Übermodulation m>1 zeigt Abschneiden des Signals
/Diagramm/am_signal.svg
:::

Der Modulationsgrad m beschreibt, wie stark das Trägersignal durch das Nutzsignal beeinflusst wird. Er wird am Oszilloskop aus der Hüllkurve des AM-Signals abgelesen:

:::formel
m         = U_mod_hat / U_T_hat    # Modulationsgrad
U_mod_hat = m * U_T_hat            # Amplitude der NF-Schwingung (Modulation)
U_T_hat   = U_mod_hat / m          # Amplitude der unmodulierten Trägerschwingung
:::

| Modulationsgrad | Bedeutung |
|---|---|
| m < 1 | Untermodulation — Signal kommt durch, schlechtes SNR |
| m = 1 | Vollmodulation — optimal für AM |
| m > 1 | Übermodulation — Verzerrung, Signalverlust |

## Analoge Modulation (aus dem Spick)

| Typ | Kürzel | Was variiert | Bandbreite | Störfestigkeit |
|---|---|---|---|---|
| Amplitudenmodulation | AM | Amplitude des Trägers | schmal | gering |
| Frequenzmodulation | FM | Frequenz des Trägers | breiter | gut |
| Phasenmodulation | PM | Phase des Trägers | breiter | gut |

**AM:** Amplitude des Trägers schwankt proportional zum NF-Signal. Einfache Demodulation (Diode + Kondensator). Störanfällig (Blitze, Funken → Amplitudenrauschen). Typisch: Mittelwelle, Kurzwelle, AM-Radio.

**FM:** Frequenz des Trägers schwankt proportional zum NF-Signal. Limiter im Empfänger unterdrückt Amplitudenstörungen automatisch → bessere Klangqualität. Breitere Bandbreite nötig (UKW: 200 kHz pro Kanal). Typisch: UKW-Radio, VHF-Sprechfunk.

**PM:** Phase des Trägers schwankt. Mathematisch nah an FM. Wird in digitalen Systemen bevorzugt (→ PSK).

## Digitale Modulation (aus dem Spick)

| Typ | Kürzel | Was variiert | Bitraten-Effizienz | Anwendung |
|---|---|---|---|---|
| Amplitude Shift Keying | ASK | Amplitude (ein/aus) | gering | RFID, optisch, OOK |
| Frequency Shift Keying | FSK | Frequenz (f1 / f2) | mittel | Modem, Funk-UART |
| Phase Shift Keying | PSK | Phase (0° / 180°) | gut | WLAN, Bluetooth, GPS |
| Quadrature AM | QAM | Amplitude + Phase | sehr gut | LTE, DVB-C, Kabel |

**ASK (OOK):** Einfachste Variante — Träger ein oder aus. Sehr störanfällig.

**BPSK/QPSK:** Phase wechselt für 0 und 1. Robuster als ASK. Bei QPSK: 4 Phasen → 2 Bit pro Symbol.

**QAM:** Kombination aus Amplituden- und Phasenmodulation. 16-QAM: 16 Zustände = 4 Bit/Symbol. 256-QAM: 8 Bit/Symbol — hohe Datenrate, braucht aber gutes SNR.

## Puls-Modulationsverfahren (aus dem Spick)

| Kürzel | Name | Was variiert | Anwendung |
|---|---|---|---|
| PAM | Pulsamplitudenmodulation | Pulsamplitude | Vorstufe vor ADC |
| PWM / PDM / PBM / PLM | Puls-Weiten-Modulation | Pulsbreite (Duty Cycle) | Motorsteuerung, LED, DC-DC |
| PPM | Puls-Phasen-Modulation | Zeitpunkt des Pulses | RC-Servos |
| PCM | Pulse-Code Modulation | Binärcode pro Zeitslot | Audio-CD, Telefon (ISDN) |
| DPCM | Differential PCM | Differenz zum Vorwert | Sprachkompression |

**PWM** ist in der Leistungselektronik allgegenwärtig. Das Tastverhältnis D = t_on / T steuert die mittlere Ausgangsspannung:

:::formel
U_mittel = D * U_versorgung    # mittlere Ausgangsspannung bei PWM
D = t_on / T                   # Tastverhältnis (Duty Cycle), 0 bis 1
:::

**PCM** digitalisiert ein analoges Signal vollständig: Abtasten (Sampling), Quantisieren (Amplitudenauflösung), Codieren (Binärdarstellung). Basis aller digitalen Audiotechnik.

:::tip
PWM und PDM sind dasselbe Prinzip mit verschiedenen Namen: Pulsbreite = Pulsdauer = Pulslänge. In Datenblättern meist als PWM bezeichnet.
:::
