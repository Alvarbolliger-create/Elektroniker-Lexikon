---
title: Leistungsanpassung
kategorie: ET
tags: [leistungsanpassung, innenwiderstand, lastwiderstand, maximale leistung, impedanzanpassung, wirkungsgrad]
groessen: P|Leistung|W; Ri|Innenwiderstand|Ohm; Ra|Lastwiderstand|Ohm; U0|Leerlaufspannung|V; eta|Wirkungsgrad|—
_status: PORT  # ET_alt/Schaltkreise/Leistungsanpassung.md
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Erzeuger-Ersatzschaltung (Thévenin)]]
- [[Spannungs- & Stromteiler]]
:::
:::vbox
**Verwandte Artikel**
- [[Elektrische Leistung]]
:::
:::

---

An welchen Lastwiderstand gibt eine reale Quelle die grösste Leistung ab? Die Antwort — Ra = Ri — ist intuitiv überraschend, aber mathematisch eindeutig. Dieses Prinzip heisst Leistungsanpassung.

## Bedingung für maximale Leistung

:::schematic Reale Spannungsquelle mit Lastwiderstand: Ideale Spannungsquelle U0 in Reihe mit Innenwiderstand Ri (links); Lastwiderstand Ra (rechts) an den Klemmen; Strom I fliesst im Uhrzeigersinn; Spannung U an Ra eingezeichnet; Beschriftung: U0, Ri, Ra, I
/schaltplaene/schaltkreise/leistungsanpassung.svg
:::

Die maximale Leistung an der Last wird erreicht, wenn der Lastwiderstand Ra gleich dem Innenwiderstand Ri der Quelle ist:

:::formel
Ra = Ri    # Anpassungsbedingung
:::

Bei dieser Bedingung gilt für die maximale Leistung:

:::formel
P_max = U0^2 / (4 * Ri)    # Leistung bei Ra = Ri
:::

**Herleitung (Prinzip):** Die Lastleistung P = I² · Ra mit I = U0/(Ri + Ra). Ableitung nach Ra und gleich null setzen ergibt Ra = Ri.

:::monospace
Beispiel: U0 = 12 V, Ri = 50 Ohm
P_max = 12^2 / (4 * 50) = 144 / 200 = 0.72 W
bei Ra = 50 Ohm, I = 12 / (50+50) = 120 mA
:::

## Wirkungsgrad bei Anpassung

Bei Ra = Ri teilen sich Ri und Ra die Spannung genau hälftig. Das bedeutet: Im Innenwiderstand fällt genauso viel Verlustleistung an wie in der Last — der Wirkungsgrad beträgt nur 50 %.

:::formel
eta = Ra / (Ri + Ra)    # Wirkungsgrad allgemein
:::

Bei Ra = Ri: eta = 0,5 (50 %). Für hohe Effizienz muss Ra ≫ Ri sein — dann gehen aber auch Strom und Leistung zurück.

## Strom- / Spannungs- / Leistungsanpassung

Es gibt drei unterschiedliche Optimierungsziele:

| Ziel | Bedingung | Typische Anwendung |
|---|---|---|
| Maximaler Strom | Ra = 0 Ω (Kurzschluss) | Kurzschlussprüfung, Messung Ri |
| Maximale Spannung | Ra → ∞ (Leerlauf) | Spannungsquellen-Buffering |
| Maximale Leistung | Ra = Ri | HF-Technik, Audioübertrager |

## Wann sinnvoll, wann nicht?

**Sinnvoll** bei der Leistungsanpassung:
- HF-Übertragung (Antennen, Koaxialkabel: 50 Ω oder 75 Ω)
- Audioverstärker und Lautsprecher (Impedanzanpassung über Übertrager)
- Sensorauswertung mit maximaler Empfindlichkeit

**Nicht sinnvoll** in der Energietechnik:
- Energieversorgung (50 % Verlust im Innenwiderstand wäre inakzeptabel)
- Netzteile, Batterien, Spannungsregler → Ra ≫ Ri anstreben (eta nahe 100 %)

:::tip
In der HF-Technik werden alle Leitungen und Abschlüsse auf 50 Ω normiert — deshalb haben Koaxialkabel, Messgeräte, Antennenanschlüsse alle 50 Ω Impedanz. Nicht wegen maximaler Leistung allein, sondern um Reflexionen auf der Leitung zu vermeiden.
:::
