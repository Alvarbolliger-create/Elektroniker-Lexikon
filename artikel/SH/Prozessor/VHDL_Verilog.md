---
title: VHDL und Verilog
kategorie: SH
tags: [VHDL, Verilog, HDL, FPGA, synthese, simulation, RTL, entity, architecture, module, assign, process]
symbol: —
einheit: —
---

VHDL und Verilog sind Hardwarebeschreibungssprachen. Sie beschreiben wie Logik aufgebaut ist, nicht wie sie abgearbeitet wird.

:::hbox
:::vbox
**Voraussetzungen**
- [[FPGA]]
- [[Logikgatter]]
- [[Flipflops]]
:::
:::vbox
**Verwandte Artikel**
- [[FSM (Zustandsautomat)]]
:::
:::

---

## Was ist anders als C?

In C werden Befehle nacheinander ausgeführt. In VHDL/Verilog beschreibt man gleichzeitig ablaufende Hardware. Alle Signalzuweisungen in einem Prozess passieren parallel zum gleichen Zeitpunkt.

Das Denken muss umgestellt werden: nicht "was passiert als nächstes", sondern "was ist mit diesem Signal verbunden".

## Grundelemente in VHDL

```vhdl
-- Einfaches UND-Gatter
entity and_gate is
  port (a, b : in std_logic;
        y    : out std_logic);
end entity;

architecture rtl of and_gate is
begin
  y <= a and b;
end architecture;
```

## Grundelemente in Verilog

```verilog
// Gleiches UND-Gatter in Verilog
module and_gate (
  input  a, b,
  output y
);
  assign y = a & b;
endmodule
```

## VHDL vs. Verilog

| Eigenschaft | VHDL | Verilog |
|---|---|---|
| Ursprung | Ada (streng typisiert) | C-ähnlich |
| Verbreitung | Europa, Industrie | USA, Asien |
| Lernkurve | steiler | flacher |
| Synthese | beide gleichwertig | beide gleichwertig |

Beide Sprachen werden von allen modernen Synthesewerkzeugen unterstützt.

## Synthesierbar vs. Simulation only

Nicht jeder gültige VHDL/Verilog-Code kann in Hardware umgesetzt werden. Konstrukte wie `wait for 10 ns` sind nur für Simulationen sinnvoll.

Synthesierbare Teile: Kombinatorische Logik (assign/concurrent signal), Zustandsautomaten, Prozesse mit Takt-Flanken-Erkennung.

## Werkzeuge

- **Xilinx Vivado**: Für Xilinx FPGAs (kostenlos für viele Devices)
- **Intel Quartus**: Für Intel/Altera FPGAs
- **Yosys + nextpnr**: Open-Source, für iCE40 und andere
- **GHDL + GTKWave**: Open-Source VHDL-Simulation
