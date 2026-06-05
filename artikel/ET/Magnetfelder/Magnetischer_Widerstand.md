---
title: Magnetischer Widerstand (Reluktanz)
kategorie: ET
tags: [magnetischer widerstand, reluktanz, magnetischer kreis, durchflutung, fluss, analogie, luftspalt]
groessen: R_m|Reluktanz|A/Wb; Theta|Durchflutung|A; Phi|Fluss|Wb; l|Feldlinienlänge|m; mu_r|relative Permeabilität|—; A|Kernfläche|m²
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Magnetfelder]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektromagnet]]
:::
:::

---

Der magnetische Widerstand (Reluktanz) beschreibt, wie stark ein magnetischer Pfad dem Fluss entgegenwirkt — analog zum elektrischen Widerstand. Die Analogie macht magnetische Kreise mit denselben Methoden lösbar wie elektrische.

## Formel

:::formel
R_m = l / (mu_0 * mu_r * A)    # Reluktanz in A/Wb (= 1/H)
:::

| Grösse | Einheit | Bedeutung |
|---|---|---|
| l | m | Länge des magnetischen Pfades |
| mu_r | — | Relative Permeabilität des Materials |
| A | m² | Querschnittsfläche des Pfades |

**Hoher R_m**: Langer Pfad, kleiner Querschnitt, niedriges mu_r (z. B. Luftspalt) → Fluss wird "gebremst".

**Niedriger R_m**: Kurzer Pfad, grosser Querschnitt, hohes mu_r (Ferrit, Eisen) → Fluss läuft leicht.

## Ohmsches Gesetz des Magnetischen Kreises

Analog zu U = R · I gilt:

:::formel
Theta = R_m * Phi    # Durchflutung = magn. Widerstand · magn. Fluss
:::

| Elektrischer Kreis | Magnetischer Kreis |
|---|---|
| Spannung U (V) | Durchflutung Theta = N·I (A) |
| Strom I (A) | Magnetischer Fluss Phi (Wb) |
| Widerstand R (Ω) | Reluktanz R_m (A/Wb) |
| Leitwert G (S) | Permeanz P_m (Wb/A = H) |

## Reihenschaltung magnetischer Widerstände

Im magnetischen Kreis addieren sich Reluktanzen in Reihe — genau wie elektrische Widerstände:

:::formel
R_m_ges = R_m1 + R_m2 + R_m3
:::

**Anwendung Luftspalt**: Ein Luftspalt im Eisenkern erhöht die Gesamtreluktanz erheblich, weil mu_r(Luft) ≈ 1 viel kleiner als mu_r(Eisen) ≈ 1000. Selbst ein kleiner Luftspalt dominiert die Reluktanz.

:::monospace
Beispiel: Eisenkern mu_r = 2000, l_Fe = 100 mm, A = 100 mm²
R_m_Fe = 100e-3 / (4*pi*1e-7 * 2000 * 100e-6) = 398 kA/Wb

Luftspalt l_Luft = 1 mm:
R_m_Luft = 1e-3 / (4*pi*1e-7 * 1 * 100e-6) = 7.96 MA/Wb

R_m_Luft ist 20× grösser als R_m_Fe!
:::

## Praktische Bedeutung

- **Transformatoren**: Kleiner Luftspalt vermeiden (hohe Reluktanz → schlechtere Kopplung)
- **Drosseln**: Gezielter Luftspalt stabilisiert die Induktivität bei hohen Strömen (verhindert Sättigung)
- **Elektromagnet**: Kleine Reluktanz im Eisenpfad konzentriert den Fluss → hohe Flussdichte im Luftspalt → grosse Anzugskraft
