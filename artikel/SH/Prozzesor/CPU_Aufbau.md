---
title: CPU Aufbau
kategorie: Rechnersysteme
tags: [ALU, Prozessor, Register]
---

# Das Gehirn: Die Central Processing Unit

Die CPU führt Befehle aus und steuert den Datenfluss.

## Kernkomponenten
- **ALU (Arithmetic Logic Unit):** Das Rechenwerk für mathematische und logische Operationen.
- **Steuerwerk (Control Unit):** Interpretiert Befehle und gibt Taktsignale an andere Teile weiter.
- **Program Counter (PC):** Ein Register, das die Adresse des nächsten auszuführenden Befehls speichert.
- **Instruction Register (IR):** Speichert den aktuell in Ausführung befindlichen Befehl.
- **PSW (Program Status Word):** Enthält Status-Flags (z. B. Zero-Flag, Carry-Flag).

## Der Befehlszyklus
Jeder Befehl durchläuft drei Phasen:
1. **Fetch:** Befehl aus dem Speicher laden.
2. **Decode:** Befehl interpretieren.
3. **Execute:** Befehl ausführen.

---
**Siehe auch:**
- [[Computerarchitektur - Busse]]
- [[Binäre Arithmetik]]