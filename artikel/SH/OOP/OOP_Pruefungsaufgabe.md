---
title: OOP Prüfungsaufgabe (ZDiode)
kategorie: SH
kapitel: OOP
tags: [oop, pruefung, klassendiagramm, zdiode, konstruktor, methoden, instanzierung, getter, setter, cpp, c++]
---

:::hbox
:::vbox
**Voraussetzungen**
- [[OOP Grundlagen (Klassen, Objekte, Vererbung)]]
- [[Z-Diode]]
:::
:::vbox
**Verwandte Artikel**
- [[OOP Grundlagen (Klassen, Objekte, Vererbung)]]
:::
:::

---

In der Prüfung erhältst du ein **UML-Klassendiagramm** und musst daraus C++-Code ableiten. Die Aufgaben sind immer gleich aufgebaut: Attribut deklarieren, Konstruktor schreiben, Methode implementieren, Objekt erzeugen, Methode aufrufen. Hier wird das vollständig am Beispiel der Z-Diode durchgespielt.

---

## Das Klassendiagramm lesen

```
┌─────────────────────────────────────────────────────────────────┐
│                           ZDiode                                │
├─────────────────────────────────────────────────────────────────┤
│ - voltageUz : double                                            │
│ - powerPzTot : double                                           │
│ - currentIzTot : double                                         │
│ - currentIzMin : double                                         │
│ - currentIzMax : double                                         │
│ - currentIz : double                                            │
├─────────────────────────────────────────────────────────────────┤
│ + ZDiode(spannungUz : double, leistungPzTot : double)           │
│ + setCurrentIz(stromIz : double) : void                         │
│ + getVoltageUz() : double                                       │
│ + getPowerPz() : double                                         │
│ + getCurrentIzTot() : double                                    │
│ + getCurrentIzMin() : double                                    │
│ + getCurrentIzMax() : double                                    │
│ + testWorkingArea() : boolean                                   │
└─────────────────────────────────────────────────────────────────┘
```

| Symbol | Bedeutung | C++ |
|---|---|---|
| `-` | private | `private:` Abschnitt |
| `+` | public | `public:` Abschnitt |
| Typ nach `:` | Datentyp / Rückgabetyp | `double`, `bool`, `void` |
| Kein Rückgabetyp beim Konstruktor | Konstruktor hat **keinen** Rückgabetyp | weder `void` noch anderes |
| `boolean` im Diagramm | UML-Notation | in C++ heisst das `bool` |

---

## Physikalischer Hintergrund: Arbeitsbereich der Z-Diode

:::formel
currentIzTot = powerPzTot / voltageUz   # Maximalstrom aus Verlustleistung
currentIzMin = 0.1 * currentIzTot       # Untergrenze: 10% von IzTot
currentIzMax = 0.9 * currentIzTot       # Obergrenze: 90% von IzTot
currentIz    = 0.5 * currentIzTot       # Default-Arbeitsstrom: 50%
:::

| Grösse | Symbol | Einheit | Bedeutung |
|---|---|---|---|
| Zenerspannung | Uz | V | Spannung, bei der die Z-Diode zündet |
| Verlustleistung | PzTot | W | Maximal erlaubte Wärmeleistung |
| Maximalstrom | IzTot | A | Strom bei voller Verlustleistung |
| Minimalstrom | IzMin | A | Untergrenze des Arbeitsbereichs |
| Maximalstrom Arbeitsbereich | IzMax | A | Obergrenze des Arbeitsbereichs |
| Arbeitsstrom | Iz | A | Aktuell fliessender Strom |

---

## Aufgabe a) — Attribut deklarieren

> Deklarieren Sie nur die Variable `voltageUz` (Attribut) der Klasse `ZDiode`.

Das `-` im Diagramm bedeutet `private`. Der Typ ist `double`.

```cpp
private:
    double voltageUz;
```

:::info
Nur **deklarieren** = Typ und Name, kein Wert. Die Zuweisung erfolgt erst im Konstruktor.
:::

:::warning
Häufiger Fehler: `WoltageUz` oder `VoltageUz` — Attributnamen beginnen in C++ klein (`voltageUz`). Gross-/Kleinschreibung ist bedeutungsrelevant: `voltageUz` und `VoltageUz` wären zwei verschiedene Variablen.
:::

---

## Aufgabe b) — Konstruktor codieren

> Codieren Sie den Konstruktor vollständig. IzTot, IzMin, IzMax werden im Konstruktor berechnet. Default-Wert: `Iz = 0.5 * IzTot`.

**Deklaration** in der Klasse (kein Rückgabetyp — auch nicht `void`!):

```cpp
public:
    ZDiode(double spannungUz, double leistungPzTot);
```

**Implementierung** ausserhalb der Klasse mit `::`:

```cpp
ZDiode::ZDiode(double spannungUz, double leistungPzTot) {
    voltageUz  = spannungUz;
    powerPzTot = leistungPzTot;

    currentIzTot = powerPzTot / voltageUz;
    currentIzMin = 0.1 * currentIzTot;
    currentIzMax = 0.9 * currentIzTot;

    currentIz = 0.5 * currentIzTot;
}
```

:::warning
`void ZDiode::ZDiode(...)` ist **falsch**. Konstruktoren haben keinen Rückgabetyp — gar nichts steht davor.
:::

**Probe mit Uz = 6.2 V, PzTot = 0.5 W:**

| Grösse | Rechnung | Ergebnis |
|---|---|---|
| IzTot | 0.5 W / 6.2 V | ≈ 80.6 mA |
| IzMin | 0.1 × 80.6 mA | ≈ 8.06 mA |
| IzMax | 0.9 × 80.6 mA | ≈ 72.6 mA |
| Iz (Default) | 0.5 × 80.6 mA | ≈ 40.3 mA |

---

## Aufgabe c) — Methode `testWorkingArea()` codieren

> Diese Methode prüft ob `currentIz` im Arbeitsbereich liegt. Rückgabe: `true` = innerhalb, `false` = ausserhalb.

In C++ heisst der Rückgabetyp `bool` (nicht `boolean` wie im UML-Diagramm steht).

```cpp
// Deklaration
bool testWorkingArea();

// Implementierung
bool ZDiode::testWorkingArea() {
    return (currentIz >= currentIzMin && currentIz <= currentIzMax);
}
```

Oder ausführlicher mit `if`:

```cpp
bool ZDiode::testWorkingArea() {
    if (currentIz >= currentIzMin && currentIz <= currentIzMax) {
        return true;
    } else {
        return false;
    }
}
```

:::merke
`&&` = UND — **beide** Bedingungen müssen gleichzeitig wahr sein. `||` wäre ODER (hier falsch).
:::

---

## Aufgabe d) — Objekt instanzieren

> Schreiben Sie den Code, der das Objekt `zenerDiode` für Uz = 6.2 V und PzTot = 0.5 W erzeugt.

```cpp
ZDiode *zenerDiode = new ZDiode(6.2, 0.5);
```

| Teil | Bedeutung |
|---|---|
| `ZDiode *` | Zeigervariable vom Typ ZDiode (`*` = Zeiger) |
| `zenerDiode` | Name des Zeigers (frei wählbar, lowerCamelCase) |
| `new` | Erzeugt das Objekt im Heap-Speicher |
| `ZDiode(6.2, 0.5)` | Ruft Konstruktor auf: Uz = 6.2 V, PzTot = 0.5 W |

---

## Aufgabe e) — Methode aufrufen und Wert speichern

> Speichern Sie die Leistung als `leistungPz` (Fliesskommavariable). Z-Diodenstrom Iz soll 30 mA betragen.

Da der Strom zuerst gesetzt werden muss, sind es zwei Schritte. Methoden werden über den **Pfeil-Operator** `->` aufgerufen, weil `zenerDiode` ein Zeiger ist:

```cpp
// Schritt 1: Strom setzen — 30 mA = 0.030 A
zenerDiode->setCurrentIz(0.030);

// Schritt 2: Leistung auslesen und speichern
double leistungPz = zenerDiode->getPowerPz();
```

:::warning
Einheiten: 30 mA = **0.030** A. Nicht 0.30 (= 300 mA) und nicht 30 (= 30 A).
:::

:::tip
`->` statt `.` — weil `zenerDiode` ein **Zeiger** ist (`ZDiode *`). Bei einem Objekt ohne `new` würde man `.` schreiben.
:::

**Arbeitsbereich prüfen:**
30 mA liegt zwischen IzMin (≈ 8 mA) und IzMax (≈ 73 mA) → `testWorkingArea()` gibt `true` zurück.

```cpp
bool imBereich = zenerDiode->testWorkingArea();   // true
```

---

## Vollständiger Code

```cpp
// ===== ZDiode.h — Deklaration =====
class ZDiode {
private:
    double voltageUz;
    double powerPzTot;
    double currentIzTot;
    double currentIzMin;
    double currentIzMax;
    double currentIz;

public:
    ZDiode(double spannungUz, double leistungPzTot);
    void   setCurrentIz(double stromIz);
    double getVoltageUz();
    double getPowerPz();
    double getCurrentIzTot();
    double getCurrentIzMin();
    double getCurrentIzMax();
    bool   testWorkingArea();
};

// ===== ZDiode.cpp — Implementierung =====
ZDiode::ZDiode(double spannungUz, double leistungPzTot) {
    voltageUz    = spannungUz;
    powerPzTot   = leistungPzTot;
    currentIzTot = powerPzTot / voltageUz;
    currentIzMin = 0.1 * currentIzTot;
    currentIzMax = 0.9 * currentIzTot;
    currentIz    = 0.5 * currentIzTot;
}

void ZDiode::setCurrentIz(double stromIz) {
    currentIz = stromIz;
}

double ZDiode::getVoltageUz()    { return voltageUz; }
double ZDiode::getPowerPz()      { return powerPzTot; }
double ZDiode::getCurrentIzTot() { return currentIzTot; }
double ZDiode::getCurrentIzMin() { return currentIzMin; }
double ZDiode::getCurrentIzMax() { return currentIzMax; }

bool ZDiode::testWorkingArea() {
    return (currentIz >= currentIzMin && currentIz <= currentIzMax);
}

// ===== main.cpp — Verwendung =====
ZDiode *zenerDiode = new ZDiode(6.2, 0.5);
zenerDiode->setCurrentIz(0.030);
double leistungPz = zenerDiode->getPowerPz();
bool   imBereich  = zenerDiode->testWorkingArea();
delete zenerDiode;
```
