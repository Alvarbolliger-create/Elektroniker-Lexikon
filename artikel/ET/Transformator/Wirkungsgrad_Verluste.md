---
title: Wirkungsgrad & Verluste (Transformator)
kategorie: ET
tags: [wirkungsgrad, verluste, kupferverluste, eisenverluste, hystereseverluste, wirbelstrom, transformator]
groessen: eta|Wirkungsgrad|—; P_v|Verlustleistung|W; P_Cu|Kupferverluste|W; P_Fe|Eisenverluste|W; I|Strom|A; R|Wicklungswiderstand|Ohm
_status: PORT  # ET_alt/Transformator/Wirkungsgrad_Verluste.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Übersetzungsverhältnis]]
- [[Magnetisierungskurve & Hysterese]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektrische Leistung]]
:::
:::

---

Kein realer Transformator ist verlustfrei. Die Verluste teilen sich in zwei Gruppen: **Kupferverluste** (abhängig vom Strom) und **Eisenverluste** (abhängig von Frequenz und Flussdichte). Gute Netz-Trafos erreichen Wirkungsgrade von über 98 %.

## Wirkungsgrad

:::formel
eta = P2 / P1    # P2 = Sekundärleistung, P1 = Primärleistung
:::

:::formel
P1 = P2 + P_v    # Primärleistung = Nutzleistung + Verluste
:::

## Kupferverluste (Last-Verluste)

Die Wicklungswiderstände R1 und R2 erzeugen ohmsche Verluste, die quadratisch mit dem Strom steigen:

:::formel
P_Cu = I1^2 * R1 + I2^2 * R2
:::

**Abhängig von:** Laststrom → bei Leerlauf null, bei Nennlast maximal.

Massnahmen: Grösserer Kupferquerschnitt, hochleitfähiges Material, kurze Wicklungen.

## Eisenverluste (Leerlauf-Verluste)

Eisenverluste entstehen im Kern und sind unabhängig vom Laststrom — sie entstehen auch im Leerlauf:

**Hystereseverluste** (→ [[Magnetisierungskurve & Hysterese]]): Jede Feldumkehr kostet Energie proportional zur Fläche der Hysteresekurve.

**Wirbelstromverluste**: Der wechselnde Fluss induziert Kreisströme (Wirbelströme) im leitfähigen Kernmaterial. Diese erzeugen Wärme.

:::formel
P_Fe = P_hyst + P_wirbel
:::

**Massnahmen:**
- **Hystereseverluste**: Kernmaterial mit schmaler Hystereseschleife (Weicheisen, Ferrit)
- **Wirbelstromverluste**: Kern aus dünnen, isolierten Blechen (Trafoblech) oder aus nicht leitendem Ferrit

## Gesamtverluste und Leistungsbilanz

| Verlusttyp | Abhängigkeit | Verhalten |
|---|---|---|
| Kupferverluste P_Cu | I² | Bei Leerlauf ≈ 0, steigt mit Last |
| Hystereseverluste | f · B_max^n | Konstant bei konstanter Spannung |
| Wirbelstromverluste | f² · B_max² | Konstant bei konstanter Spannung |

:::monospace
Beispiel: Trafo 1 kVA, P_Cu_Nenn = 20 W, P_Fe = 10 W
Bei Nennlast: P_v = 20 + 10 = 30 W
eta = 1000 / (1000 + 30) = 97.1 %
:::

## Optimaler Betriebspunkt

Der Wirkungsgrad ist maximal, wenn P_Cu = P_Fe. Netz-Trafos werden typisch auf ca. 75 % Nennlast für maximalen Wirkungsgrad ausgelegt — weil sie selten mit 100 % belastet werden.

:::tip
Trafos im Leerlauf verbrauchen immer noch Strom (Magnetisierungsstrom + Eisenverluste). Grosse Anlagen sollten bei Nichtbetrieb abgeschaltet werden — bei hundert Trafos in einem Industriebetrieb summieren sich die Leerlaufverluste deutlich.
:::
