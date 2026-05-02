---
title: Messkategorien (CAT I – CAT IV)
kategorie: MT
tags: [CAT, messkategorie, überspannung, multimeter, sicherheit, CAT I, CAT II, CAT III, CAT IV, transient, blitzeinschlag, messung]
symbol: —
einheit: —
---

Die Messkategorien CAT I bis CAT IV definieren, für welche Umgebung ein Messgerät ausgelegt ist. Sie beschreiben die zu erwartende Energie bei transienten Überspannungen (Blitzeinschlag, Schaltvorgänge).

:::hbox
:::vbox
**Voraussetzungen**
- [[Strom-, Spannungs-, Widerstandsmessung]]
- [[Gefahren des Stroms]]
:::
:::vbox
**Verwandte Artikel**
- [[Schutzklassen I, II, III]]
- [[Die 5 Sicherheitsregeln]]
:::
:::

---

## Das Problem: Transiente Überspannungen

In einem Stromnetz entstehen kurze Spannungsspitzen durch Blitzeinschläge, Schalthandlungen (Schütze, Transformatoren) oder kapazitive Entladungen. Diese Transienten können ein Messgerät oder den Benutzer gefährden.

Je näher man an der Quelle misst, desto kürzer und energiereicher sind diese Spitzen.

## Die vier Kategorien

| Kategorie | Typische Messung | Beispiele |
|---|---|---|
| **CAT I** | Messung in geschützten Elektronikkreisen | Signalpegel, Sekundärseite kleiner Trafos, Batterieschaltungen |
| **CAT II** | Einphasige Verbraucher an der Steckdose | Stecker, Verlängerungskabel, Haushaltsgeräte, Adapter |
| **CAT III** | Feste Installationen im Gebäude | Verteiler, Sicherungskasten, fest verkabelte Maschinen, Schaltschränke |
| **CAT IV** | Messung am Einspeisepunkt des Gebäudes | Hausanschluss, Zähler, Freileitungen, Überkopfleitung |

## Spannungsangabe

Messgeräte tragen Angaben wie **CAT III 1000 V** oder **CAT II 600 V**. Beide Werte gelten gleichzeitig. Beispiel:

Ein Gerät mit **CAT III 600 V** darf an Festinstallationen bis 600 V eingesetzt werden, aber nicht am Hausanschluss.

Die CAT-Stufe ist wichtiger als die Spannungsangabe. Ein CAT II 1000 V-Gerät ist bei Schaltschrankmessungen trotzdem nicht geeignet — die Transientenenergie ist entscheidend.

## Konsequenzen für die Praxis

**Niemals unterhalb der Kategorie messen.** Ein CAT I-Gerät an der Steckdose kann bei einem Transient explodieren.

**Tastkopf und Kabel müssen dieselbe Kategorie haben wie das Gerät.** Der schwächste Teil bestimmt die Sicherheit.

**Für Schaltschrankarbeit**: mindestens CAT III.  
**Für Hausanschluss**: CAT IV.

:::danger
Ein Gerät mit zu niedriger CAT-Einstufung kann bei einer Überspannung einen Lichtbogen erzeugen. Das ist lebensgefährlich. Immer das passende Gerät verwenden.
:::

## Erkennungsmerkmal

Die CAT-Einstufung steht auf dem Gerät, auf den Tastköpfen und in den technischen Daten. Fehlt die Angabe, ist das Gerät nur für CAT I geeignet.
