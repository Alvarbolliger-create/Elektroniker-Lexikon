---
title: Elektrische Arbeit & Tarif
kategorie: ET
tags: [arbeit, energie, kilowattstunde, tarif, kosten, verbrauch, energiezähler]
groessen: W|Arbeit|J; P|Leistung|W; t|Zeit|s; K|Kosten|Fr
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Elektrische Leistung]]
:::
:::

---

Elektrische Arbeit ist die über die Zeit umgesetzte elektrische Energie. Im Alltag wird sie in Kilowattstunden (kWh) gemessen — das ist die Einheit auf der Stromrechnung.

## Elektrische Arbeit

Leistung mal Zeit ergibt Arbeit (Energie):

:::formel
W = P * t
:::

Das CAS rechnet Einheiten automatisch um: `P * t` mit `_W` und `_h` liefert direkt Joule oder kWh je nach gewünschter Zieleinheit.

## Tarifberechnung

Der Energieversorger rechnet in kWh ab. Der Tarif k (Franken pro kWh) variiert je nach Anbieter und Tageszeit.

:::formel
K = W_kWh * k    # Kosten in Fr = Energie in kWh mal Tarif in Fr/kWh
:::

:::monospace
Beispiele (Tarif 0.25 Fr/kWh):
Backofen 2 kW, 1.5 h:         W = 3 kWh  →  K = 0.75 Fr
LED-Lampe 10 W, 1000 h:       W = 10 kWh →  K = 2.50 Fr
Elektroauto 22 kW, 3 h laden: W = 66 kWh →  K = 16.50 Fr
Jahresverbrauch Haushalt 3500 kWh:          K = 875 Fr
:::

| Gerät | Leistung | Kosten pro Stunde |
|---|---|---|
| LED-Lampe | 10 W | 0,3 Rp. |
| Fernseher | 100 W | 2,5 Rp. |
| Waschmaschine | 2000 W | 50 Rp. |
| Backofen | 2500 W | 63 Rp. |
| Elektroauto (22 kW) | 22 000 W | 5,50 Fr. |

## Energiezähler

Der Energiezähler (Stromzähler) misst die kumulierte kWh. Früher als Ferrarisscheibe (drehende Scheibe durch Induktion), heute digital. Neuere Geräte (Smart Meter) übermitteln den Verbrauch automatisch an den Versorger.

:::tip
Der **Wirkungsgrad** eines Geräts bestimmt direkt den Energieverbrauch: Ein Gerät mit eta = 0,9 braucht für dieselbe Nutzleistung 11 % mehr Energie als ein ideal effizienter Ersatz. Bei Langzeitbetrieb (Heizung, Beleuchtung, Motor) lohnt sich die Investition in effizientere Geräte rasch.
:::
