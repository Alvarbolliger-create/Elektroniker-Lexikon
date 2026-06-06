---
title: Frequenzumrichter
kategorie: EK
kapitel: Motoren
tags: [frequenzumrichter, vfd, asynchronmotor, drehstrom, zwischenkreis, igbt, pwm, u-f-kennlinie, sanftanlauf, oberschwingungen, rückspeisung, emc, emv]
groessen: f_aus|Ausgangsfrequenz|Hz; U_ZK|Zwischenkreisspannung|V; n|Drehzahl|U/min; p|Polpaarzahl|—; s|Schlupf|—
_status: FERTIG
---

:::hbox
:::vbox
**Voraussetzungen**
- [[BLDC]]
- [[IGBT]]
- [[DC-DC Wandler]]
:::
:::vbox
**Verwandte Artikel**
- [[Servomotor]]
- [[BLDC]]
:::
:::vbox
**Führt weiter zu**
- [[Regelkreis Grundlagen]]
:::
:::

---

Ein Frequenzumrichter (FU, auch VFD — Variable Frequency Drive) stellt Frequenz und Spannung einer Drehstromversorgung variabel ein. Damit lässt sich die Drehzahl eines **Asynchronmotors** stufenlos regeln — ohne mechanische Getriebe.

## Aufbau: drei Stufen

:::schematic Frequenzumrichter Aufbau (3 Stufen): Eingang: 3-Phasen-Netz L1/L2/L3 (400 V AC, 50 Hz). Stufe 1: 6-Puls-Diodenbrücke (Gleichrichter) → U_ZK ≈ 565 V DC. Stufe 2: Zwischenkreis (grosser Elko, 400–1000 µF). Stufe 3: 3-Phasen-Wechselrichter mit 6 IGBTs (2 pro Phase, H-Brücke) → variable Ausgangsspannung und -frequenz → Motor (U, V, W)
/Diagramm/frequenzumrichter_aufbau.svg
:::

**1. Gleichrichter**: Erzeugt aus dem dreiphasigen Netz eine Gleichspannung:

:::formel
U_ZK = U_AC_eff * sqrt(2) * sqrt(3) ≈ 565 V    # bei 400 V Drehstrom (3-Phasen-Brücke)
U_ZK = U_AC_eff * sqrt(2)           ≈ 325 V    # bei 230 V Einphasig
:::

**2. Zwischenkreis**: Grosser Elektrolytkondensator glättet die Gleichspannung und puffert Lastspitzen. Typisch 400–1000 µF je 1 kW Motorleistung.

**3. Wechselrichter**: Sechs IGBTs schalten den Zwischenkreis mit hochfrequenter PWM (2–16 kHz) auf drei Ausgangsphasen. Durch Variation der PWM entstehen variable Frequenz und Amplitude.

## U/f-Kennlinie (Konstantflussbetrieb)

Spannung und Frequenz werden **proportional** geändert. So bleibt der magnetische Fluss im Motor konstant → konstantes Drehmoment über den ganzen Drehzahlbereich:

:::formel
U / f = const.      # U/f-Verhältnis konstant halten
:::

:::monospace
Beispiel: Motor 400 V / 50 Hz
Bei f = 25 Hz: U = 200 V    (halbe Frequenz, halbe Spannung)
Bei f = 50 Hz: U = 400 V    (Nennbetrieb)
Bei f > 50 Hz: U = 400 V    (Feldschwächung, Drehmoment sinkt)
:::

## Drehzahlberechnung Asynchronmotor

:::formel
n_sync = f * 60 / p          # Synchrondrehzahl [U/min]
n_mot  = n_sync * (1 - s)    # Motordrehzahl mit Schlupf s (typisch 2–5 %)
:::

| Grösse | Bedeutung |
|---|---|
| p | Polpaarzahl (2-poliger Motor: p=1, 4-poliger: p=2) |
| s | Schlupf (Differenz zwischen Sync.- und Motordrehzahl) |
| f | Ausgangsfrequenz des FU |

## Vorteile des Frequenzumrichters

**Sanftanlauf**: Frequenz startet bei 0 Hz, rampt auf Nennfrequenz → kein Anlaufstromstoss (6–8× Nennstrom bei Direktanlauf). Motor und Mechanik werden geschont.

**Energiesparen bei Pumpen/Lüftern**: Leistung skaliert mit der **dritten Potenz** der Drehzahl:

:::formel
P ~ n^3     # Pumpenkurve: halbe Drehzahl = 1/8 der Leistung!
:::

**Rückspeisung (Rekuperation)**: Beim Bremsen oder bei Überlast (z.B. Kran absenkt Last) kann der Motor als Generator arbeiten. Mit rückspeisefähigem FU (aktives Frontend) fliesst die Energie ins Netz zurück.

## Oberschwingungen und EMV

Der FU erzeugt beim Gleichrichten **Oberschwingungen** (5., 7., 11., 13. Harmonische) im Versorgungsnetz. Diese belasten andere Geräte und Transformatoren.

**Massnahmen**: Netzfilter (Drosselspule am Eingang), 12-Puls-Gleichrichter, aktives Frontend (PFC).

Die hochfrequente PWM am Ausgang erzeugt starke HF-Störungen:

:::warning
Motorleitungen bei Frequenzumrichtern immer geschirmt ausführen. Schirmung beidseitig erden. Leitungen so kurz wie möglich halten (max. 50–100 m je nach FU-Typ). Motorleitungen nicht parallel zu Steuerleitungen verlegen.
:::

## Bremsverfahren

| Methode | Prinzip | Anwendung |
|---|---|---|
| DC-Bremse | DC-Strom in Statorwicklung → magnetisches Bremsmoment | Einfache Haltebremsungen |
| Bremswiderstand | Überschüssige Bremsenergie in Widerstand verheizen | Standard (Bremsmodul extern) |
| Rückspeisung ins Netz | Aktives Frontend wandelt Bremsenergie zurück | Energieeffiziente Anlagen |

## Typische Kenndaten FU

| Grösse | Typischer Wert |
|---|---|
| Eingangsfrequenz | 50/60 Hz |
| Ausgangsfrequenz | 0–400 Hz |
| Zwischenkreisspannung | 565 V DC (bei 400 V AC) |
| PWM-Schaltfrequenz IGBT | 2–16 kHz |
| Wirkungsgrad | 95–98 % |
| Überlastfähigkeit | 150 % für 60 s |

:::tip
Frequenzumrichter sind die Standard-Lösung für Pumpen, Lüfter und Kompressoren: die Energieeinsparung amortisiert die Investition oft in 1–2 Jahren. Bei konstant laufenden Maschinen lohnt sich ein Stern-Dreieck-Anlasser statt FU (günstiger, weniger Aufwand).
:::
