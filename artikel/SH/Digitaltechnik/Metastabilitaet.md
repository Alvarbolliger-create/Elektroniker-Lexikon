---
title: Metastabilität, Setup-Time & Hold-Time
kategorie: SH
tags: [metastabilität, setup-time, hold-time, flipflop, synchronisation, clock domain, MTBF, CDC, synchronizer, double-FF, aperture]
symbol: t_su, t_h
einheit: s
---

Ein Flipflop braucht Zeit, um das Eingangssignal sicher einzulesen. Wird diese Zeit verletzt, kann das Flipflop in einen undefinierten Zustand geraten — Metastabilität.

:::hbox
:::vbox
**Voraussetzungen**
- [[Flipflops]]
- [[Synchrone Zähler]]
- [[FPGA]]
:::
:::vbox
**Verwandte Artikel**
- [[FSM (Zustandsautomat)]]
- [[CPU Aufbau]]
:::
:::vbox
**Führt weiter zu**
- [[VHDL und Verilog]]
- [[Embedded Linux]]
:::
:::

---

## Setup-Time (t_su)

Das Eingangssignal (D) muss mindestens t_su vor der Taktflanke stabil sein. Ändert sich D kurz vor der Flanke, kann das Flipflop das Signal nicht sicher einlesen.

:::monospace
t_su = Mindestzeit D stabil vor Taktflanke    # typisch 0.1–2 ns
:::
**Verletzung**: Wenn D sich weniger als t_su vor der Taktflanke ändert, ist unklar ob Q = 0 oder Q = 1 gespeichert wird.

## Hold-Time (t_h)

Das Eingangssignal muss mindestens t_h nach der Taktflanke noch stabil bleiben. Das gibt dem Flipflop Zeit, den Zustand sicher zu übernehmen.

:::monospace
t_h = Mindestzeit D stabil nach Taktflanke    # typisch 0–0.5 ns
:::
## Timing-Diagramm

:::schematic
/Diagramm/metastabilitaet_0.svg
:::
Das Timing-Budget im Design:

:::monospace
T_clk ≥ t_co + t_propag + t_su    # T_clk = Taktperiode, t_co = Clock-to-Output des Vorgängers
:::
## Metastabilität

Wenn Setup- oder Hold-Time verletzt wird, gerät das Flipflop in einen metastabilen Zustand. In diesem Zustand ist die interne Spannung weder klar High noch klar Low — sie liegt dazwischen.

Das Flipflop verlässt den metastabilen Zustand nach einer zufälligen Zeitspanne. Je nach dem landet es bei 0 oder 1 — das Ergebnis ist nicht vorhersagbar.

**Das Problem in der Praxis**: Asynchrone Eingangssignale (von aussen, von anderen Clockdomains) können jederzeit ankommen — auch während des Aperture-Fensters.

## Mean Time Between Failures (MTBF)

Metastabilität lässt sich nicht verhindern, nur die Wahrscheinlichkeit reduzieren:

:::monospace
MTBF = (e^(t_resolve / τ)) / (f_clk × f_data × C1)    # τ und C1: Flipflop-Kennwerte
:::
Je länger die "Auflösezeit" t_resolve, desto unwahrscheinlicher bleibt die Metastabilität über diese Zeit hinaus bestehen.

## Synchronisierungskette (Synchronizer)

**Lösung für asynchrone Eingangssignale**: Zwei hintereinandergeschaltete Flipflops (Double-FF Synchronizer).

:::monospace
Async_Input → FF1 → FF2 → Verwendung im System
              (beide getaktet mit System-Clock)
:::
FF1 kann metastabil werden. FF2 liest den Ausgang von FF1 erst einen vollen Taktzyklus später — das gibt FF1 Zeit, aus dem metastabilen Zustand heraus zu kommen. Mit modernen Flipflops ist die MTBF dann typisch > 1 Million Jahre.

:::warning
Alle asynchronen Signale (externe Eingänge, Signale aus anderen Clock-Domains) müssen synchronisiert werden, bevor sie in synchrone Logik eingespeist werden. Das gilt auch für Reset-Signale!
:::

## Clock Domain Crossing (CDC)

Wenn zwei Teile einer Schaltung mit unterschiedlichen Taktfrequenzen arbeiten, muss jede Signalübergabe zwischen den Domains synchronisiert werden.

Werkzeuge (Synopsys CDC, Questa Verify) können CDC-Verletzungen im Design automatisch prüfen.
