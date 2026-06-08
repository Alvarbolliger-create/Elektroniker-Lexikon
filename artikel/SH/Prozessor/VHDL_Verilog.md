---
title: VHDL & Verilog
kategorie: SH
kapitel: Prozessor
tags: [vhdl, verilog, hardwarebeschreibungssprache, hdl, synthese, simulation]
_status: PORT
---

:::hbox
:::vbox
**Voraussetzungen**
- [[FPGA (Field Programmable Gate Array)]]
:::
:::

---

Ein → [[FPGA (Field Programmable Gate Array)|FPGA]] besteht aus Tausenden konfigurierbarer Logikzellen, die sich zu praktisch beliebigen digitalen Schaltungen verdrahten lassen. Doch wie beschreibt man einer solchen Schaltung, was sie tun soll? Hier kommen **Hardwarebeschreibungssprachen (HDL — Hardware Description Languages)** ins Spiel: **VHDL** und **Verilog**.

## Der grundlegende Unterschied: Parallelität statt Reihenfolge

Auf den ersten Blick sehen HDL-Programme aus wie gewöhnlicher Code — doch sie funktionieren nach einem völlig anderen Prinzip:

:::merke
Ein C-Programm beschreibt eine **Abfolge** von Schritten — Zeile für Zeile, eine nach der anderen, von einem einzigen Prozessor abgearbeitet. Ein HDL-Programm dagegen beschreibt eine **Schaltung**: Alle beschriebenen Vorgänge laufen — wie in einer realen Schaltung auch — grundsätzlich **gleichzeitig und dauerhaft** ab. Eine Codezeile entspricht keinem "Befehl", der einmal ausgeführt wird, sondern einem permanent existierenden Stück Hardware — einem Gatter, einem Register, einer Verbindung. Dieses Umdenken von "Reihenfolge" zu "Parallelität und Struktur" ist die grösste Hürde beim Einstieg in VHDL oder Verilog.
:::

## VHDL: entity und architecture

In VHDL wird eine Schaltung in zwei Teile gegliedert: die **Entity** beschreibt die Schnittstelle nach aussen (Ein- und Ausgänge), die **Architecture** beschreibt das innere Verhalten:

:::tip
```vhdl
entity AND_Gate is
    port (
        a, b : in  std_logic;
        y    : out std_logic
    );
end entity AND_Gate;

architecture Verhalten of AND_Gate is
begin
    y <= a and b;
end architecture Verhalten;
```

Die Zeile `y <= a and b;` ist kein "Befehl", der einmal ausgeführt wird — sie beschreibt eine **dauerhafte Verbindung**: Immer wenn sich `a` oder `b` ändert, wird `y` augenblicklich neu berechnet, exakt so, wie es ein echtes UND-Gatter auch tun würde.
:::

## Verilog: module und assign

**Verilog** verfolgt dasselbe Grundprinzip, verwendet dabei aber eine kompaktere, an C angelehnte Syntax:

```verilog
module AND_Gate (
    input  a, b,
    output y
);
    assign y = a & b;
endmodule
```

Auch hier beschreibt `assign y = a & b;` eine fortlaufend aktive Verbindung — keine einmalige Zuweisung, sondern ein dauerhaft existierendes Gatter.

## VHDL und Verilog im Vergleich

| | VHDL | Verilog |
|---|---|---|
| Syntax | streng typisiert, ausführlich (an Ada angelehnt) | kompakt, an C angelehnt |
| Verbreitung | stark in Europa, Luft- und Raumfahrt, Militär | stark in den USA, Halbleiterindustrie |
| Lernkurve | strenger, dadurch fehlerresistenter | schneller Einstieg, dafür fehleranfälliger |
| Typsicherheit | hoch — viele Fehler werden schon beim Kompilieren erkannt | geringer — mehr Freiheit, aber mehr potenzielle Fallstricke |

## Synthetisierbarer Code vs. reine Simulation

Ein wichtiger Unterschied zu gewöhnlichen Programmiersprachen: Nicht jede gültige HDL-Anweisung lässt sich tatsächlich in Hardware umsetzen.

:::warning
**Synthetisierbarer Code** lässt sich vom Synthese-Werkzeug direkt in eine reale Schaltung aus Logikzellen, Registern und Verbindungen übersetzen — er muss sich an feste Regeln halten, die echter Hardware entsprechen. **Simulationscode** dagegen — etwa `wait for 10 ns;` oder Konstrukte zur Erzeugung von Testdaten (Testbenches) — beschreibt zeitliches Verhalten zu Test- und Analysezwecken, lässt sich aber **nicht** in Hardware umsetzen. Verwechselt man beides — schreibt also etwa nicht-synthetisierbaren Code in das eigentliche Schaltungsdesign — meldet das Synthese-Werkzeug einen Fehler, oder schlimmer: es erzeugt eine Schaltung, die sich anders verhält als in der Simulation erwartet.
:::

## Werkzeuge: vom Code zur konfigurierten Hardware

Damit aus VHDL- oder Verilog-Code tatsächlich eine funktionierende → [[FPGA (Field Programmable Gate Array)|FPGA-Konfiguration]] wird, braucht es eine ganze Werkzeugkette:

:::info
**Vivado** (Xilinx/AMD) und **Quartus** (Intel/Altera) sind die herstellereigenen Entwicklungsumgebungen für die jeweiligen FPGA-Familien — sie übernehmen Synthese, Platzierung, Verdrahtung und das Erzeugen der Konfigurationsdatei (Bitstream). Daneben haben sich quelloffene Werkzeuge etabliert: **Yosys** für die Synthese und **GHDL** als VHDL-Simulator — beide erlauben es, HDL-Designs herstellerunabhängig zu entwickeln, zu simulieren und zu testen, bevor sie auf reale Hardware übertragen werden.
:::

Damit schliesst sich der Kreis vom flexiblen, aber stromhungrigen → [[Mikrocontroller|Mikrocontroller]] über das frei konfigurierbare → [[FPGA (Field Programmable Gate Array)|FPGA]] bis zur Sprache, mit der sich digitale Schaltungen direkt als Text formulieren, simulieren und in reale Hardware verwandeln lassen — VHDL und Verilog bilden das Werkzeug, mit dem aus einer Idee eine massgeschneiderte, hochparallele Schaltung wird.
