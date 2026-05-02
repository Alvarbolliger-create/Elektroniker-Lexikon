---
title: Multiplexer & Demultiplexer
kategorie: SH
tags: [multiplexer, demultiplexer, MUX, DMUX, datenselektion, digitaltechnik, decoder, adressdekodierung, BCD, 7-segment, chip-select]
symbol: —
einheit: —
---

Ein Multiplexer (MUX) wählt aus mehreren Dateneingängen einen aus und leitet ihn auf einen Ausgang. Ein Demultiplexer (DMUX) macht das Umgekehrte: er verteilt einen Eingang auf mehrere Ausgänge.

:::hbox
:::vbox
**Voraussetzungen**
- [[Logikgatter]]
- [[Schaltalgebra]]
:::
:::vbox
**Verwandte Artikel**
- [[Karnaugh-Veitch-Diagramm (KVD)]]
- [[Addierer]]
- [[Digitale Codes]]
:::
:::

---

## Multiplexer (MUX)

**Funktion**: n Steuerleitungen wählen aus 2ⁿ Dateneingängen genau einen aus.

### 4:1 MUX (2 Steuerleitungen)

```
D0 ──┐
D1 ──┤
D2 ──┤  [MUX]  ──→ Y
D3 ──┘
      ↑
   S1 S0
```

Wahrheitstabelle:

| S1 | S0 | Ausgang Y |
|---|---|---|
| 0 | 0 | D0 |
| 0 | 1 | D1 |
| 1 | 0 | D2 |
| 1 | 1 | D3 |

**Schaltfunktion**:
```
Y = S̄1·S̄0·D0 + S̄1·S0·D1 + S1·S̄0·D2 + S1·S0·D3
```

### Aufbau mit Logikgattern

```
S̄1·S̄0 ──[AND]──┐
S̄1·S0  ──[AND]──┤
S1·S̄0  ──[AND]──┤ [OR] → Y
S1·S0  ──[AND]──┘
```

Jedes AND-Gatter hat zusätzlich den entsprechenden Dateneingang Di.

---

## Demultiplexer (DMUX)

**Funktion**: 1 Eingang wird durch n Steuerleitungen auf einen von 2ⁿ Ausgängen geschaltet.

### 1:4 DMUX (2 Steuerleitungen)

```
      ┌──→ Y0
D ──→ ┤──→ Y1
      ├──→ Y2
      └──→ Y3
        ↑
     S1 S0
```

| S1 | S0 | Aktiver Ausgang |
|---|---|---|
| 0 | 0 | Y0 = D |
| 0 | 1 | Y1 = D |
| 1 | 0 | Y2 = D |
| 1 | 1 | Y3 = D |

Alle nicht ausgewählten Ausgänge = 0.

**Schaltfunktionen**:
```
Y0 = D · S̄1 · S̄0
Y1 = D · S̄1 · S0
Y2 = D · S1 · S̄0
Y3 = D · S1 · S0
```

---

## Decoder als Sonderfall

Ein **Decoder** ist ein DMUX ohne Dateneingänge (D = 1 immer). Er aktiviert genau einen von 2ⁿ Ausgängen basierend auf dem n-Bit-Adresseingang.

**2:4-Decoder** entspricht einem 1:4 DMUX mit D = 1:

| A1 | A0 | Y3 | Y2 | Y1 | Y0 |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 0 | 1 | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 1 | 1 | 1 | 0 | 0 | 0 |

Anwendung: Chip-Select-Generierung, Speicheradressierung.

---

## Anwendungen

**MUX**:
- Mehrere Signale über einen Bus übertragen (Zeit-Multiplex)
- Beliebige Boolesche Funktion mit einem MUX realisieren (programmierbare Logik)
- Analoges Multiplexing: Mehrere Messsignale auf einen ADC schalten

**DMUX/Decoder**:
- Adressdekodierung in Mikroprozessorsystemen
- Speicherauswahl (welcher RAM-Chip antwortet?)
- 7-Segment-Ansteuerung (BCD-zu-7-Segment-Decoder)

:::info
Ein 8:1 MUX kann jede beliebige 3-Variable Boolesche Funktion realisieren: Die 3 Variablen steuern die Selektion, die 8 Dateneingänge werden auf 0 oder 1 gesetzt gemäss der Wahrheitstabelle.
:::

---

## Cascading (Erweiterung)

Zwei 4:1 MUX lassen sich zu einem 8:1 MUX erweitern:

```
D0..D3 ──[MUX A]──┐
                   ├──[MUX C]── Y
D4..D7 ──[MUX B]──┘
         ↑
        S1S0 (MUX A+B gemeinsam)
                ↑
               S2 (MUX C)
```

S2 wählt zwischen den beiden 4:1-Blöcken.
