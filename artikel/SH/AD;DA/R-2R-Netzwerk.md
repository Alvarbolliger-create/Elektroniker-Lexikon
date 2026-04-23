---
title: DA-Wandler: R-2R-Netzwerk
kategorie: Wandler
tags: [Widerstand, Schaltung]
---

# Das Widerstandsnetzwerk

Das R-2R-Netzwerk ist die am häufigsten verwendete Methode zur Digital-Analog-Wandlung.

## Aufbau
Es werden nur zwei Widerstandswerte benötigt: $R$ und $2R$. Dies ist ein großer Vorteil für die Fertigung in integrierten Schaltkreisen, da absolute Widerstandswerte schwer präzise zu fertigen sind, das Verhältnis (1:2) hingegen schon.

## Funktionsweise
Die digitalen Eingänge wirken als Umschalter, die die Zweige des Netzwerks entweder mit $V_{ref}$ oder Masse verbinden. Durch die Struktur wird der Strom an jedem Knotenpunkt halbiert, sodass jedes Bit genau die Gewichtung seiner Wertigkeit ($2^n$) erhält.

---
**Siehe auch:**
- [[AD-und DA-Grundlagen]]
- [[Signale]]