---
title: Computerarchitektur Busse
kategorie: Rechnersysteme
tags: [Bus, Hardware, CPU]
---

# Das Nervensystem des Computers

In einem Computer kommunizieren die Komponenten (CPU, Speicher, Peripherie) über ein Bussystem.

## Die drei Hauptbusse
1. **Datenbus:** Überträgt die eigentlichen Informationen. Seine Breite (z. B. 32 Bit oder 64 Bit) bestimmt die Leistungsfähigkeit.
2. **Adressbus:** Überträgt die Adresse des Speicherorts oder Bausteins, mit dem die CPU kommunizieren will.
3. **Steuerbus:** Überträgt Signale wie "Read", "Write" oder Taktvorgaben.

## Wichtige Mechanismen
- **Chip Select (CS):** Ein Signal, das einen bestimmten Baustein (z. B. einen RAM-Riegel) aktiviert.
- **Tri-State:** Ein Zustand von Ausgängen, bei dem sie weder High noch Low, sondern "hochohmig" (getrennt) sind. Dies verhindert Kurzschlüsse, wenn viele Bausteine am selben Bus hängen.

---
**Siehe auch:**
- [[CPU Aufbau]]
- [[Speicherarten]]