---
title: OOP Grundlagen (Klassen, Objekte, Vererbung)
kategorie: SH
kapitel: OOP
tags: [oop, objektorientierung, klasse, objekt, instanz, konstruktor, vererbung, kapselung, attribut, methode, cpp, c++]
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Variablen und Datentypen]]
:::
:::vbox
**Verwandte Artikel**
- [[OOP Prüfungsaufgabe (ZDiode)]]
:::
:::vbox
**Führt weiter zu**
- [[OOP Prüfungsaufgabe (ZDiode)]]
:::
:::

---

Objektorientierte Programmierung (OOP) organisiert Code in **Klassen** — wiederverwendbare Baupläne für Objekte. Jedes Objekt hat eigene Daten (Attribute) und Fähigkeiten (Methoden). In der Elektronik wird z. B. eine Z-Diode, ein Motor oder ein Sensor als Objekt modelliert.

## Klasse und Objekt

Eine **Klasse** ist der Bauplan. Ein **Objekt** ist das konkrete Exemplar, das nach diesem Bauplan erzeugt wurde — auch **Instanz** genannt.

:::info
Klasse = Bauplan (einmal geschrieben). Objekt = fertiges Exemplar (beliebig viele möglich).
:::

In C++ trennt man die **Deklaration** (`.h`-Datei, was gibt es) von der **Implementierung** (`.cpp`-Datei, wie funktioniert es):

```cpp
// ZDiode.h — Deklaration (Bauplan)
class ZDiode {
private:
    double voltageUz;
    double currentIz;

public:
    ZDiode(double spannungUz, double leistungPzTot);
    double getVoltageUz();
};
```

```cpp
// ZDiode.cpp — Implementierung
ZDiode::ZDiode(double spannungUz, double leistungPzTot) {
    voltageUz = spannungUz;
}
```

---

## Attribute — Daten des Objekts

Attribute speichern den Zustand eines Objekts. In C++ werden sie im `private:`-Abschnitt deklariert, damit von aussen niemand direkt zugreifen kann (**Kapselung**).

```cpp
class ZDiode {
private:
    double voltageUz;      // Zenerspannung
    double powerPzTot;     // Verlustleistung
    double currentIz;      // aktueller Arbeitsstrom
};
```

| Sichtbarkeit | Bedeutung |
|---|---|
| `private:` | Nur innerhalb der eigenen Klasse zugänglich |
| `public:` | Von überall zugänglich |
| `protected:` | Innerhalb der Klasse und aller Unterklassen zugänglich |

:::warning
In C++ stehen `private:`, `public:`, `protected:` als **Abschnittslabels** mit Doppelpunkt — danach gelten alle folgenden Elemente für diese Sichtbarkeit.
:::

---

## Konstruktor — Initialisierung

Der **Konstruktor** heisst gleich wie die Klasse und hat **keinen Rückgabetyp** — auch nicht `void`. Er wird automatisch aufgerufen wenn ein Objekt mit `new` erzeugt wird.

```cpp
// Deklaration in der Klasse (.h)
class ZDiode {
public:
    ZDiode(double spannungUz, double leistungPzTot);  // kein Rückgabetyp!
};

// Implementierung ausserhalb (.cpp)
ZDiode::ZDiode(double spannungUz, double leistungPzTot) {
    voltageUz  = spannungUz;
    powerPzTot = leistungPzTot;
    currentIzTot = powerPzTot / voltageUz;
    currentIzMin = 0.1 * currentIzTot;
    currentIzMax = 0.9 * currentIzTot;
    currentIz    = 0.5 * currentIzTot;
}
```

:::warning
`void ZDiode::ZDiode(...)` ist **falsch** — Konstruktoren haben keinen Rückgabetyp. Das ist der häufigste Fehler.
:::

---

## Methoden — Fähigkeiten des Objekts

Methoden sind Funktionen, die zu einer Klasse gehören. Die Implementierung erfolgt ausserhalb der Klasse mit dem **Scope-Operator** `::`.

**Getter** lesen einen privaten Wert:

```cpp
// Deklaration
double getVoltageUz();
double getPowerPz();

// Implementierung
double ZDiode::getVoltageUz() {
    return voltageUz;
}
double ZDiode::getPowerPz() {
    return powerPzTot;
}
```

**Setter** setzen einen privaten Wert:

```cpp
void ZDiode::setCurrentIz(double stromIz) {
    currentIz = stromIz;
}
```

**Prüfmethoden** liefern `true` oder `false` — in C++ heisst der Typ `bool` (nicht `boolean`):

```cpp
bool ZDiode::testWorkingArea() {
    return (currentIz >= currentIzMin && currentIz <= currentIzMax);
}
```

:::tip
Rückgabetyp `void` = die Methode gibt nichts zurück. `bool` = true/false. `double` = Fliesskommazahl.
:::

---

## Objekt erzeugen und verwenden

In C++ wird ein Objekt mit `new` auf dem Heap erzeugt. Das Ergebnis ist ein **Zeiger** (`*`). Methoden ruft man über den **Pfeil-Operator** `->` auf:

```cpp
// Objekt erzeugen — zenerDiode ist ein Zeiger auf das Objekt
ZDiode *zenerDiode = new ZDiode(6.2, 0.5);

// Methoden über Pfeiloperator aufrufen
zenerDiode->setCurrentIz(0.030);            // 30 mA setzen
double leistungPz = zenerDiode->getPowerPz();
bool   imBereich  = zenerDiode->testWorkingArea();

// Speicher freigeben (wichtig in C++!)
delete zenerDiode;
```

| Syntax | Bedeutung |
|---|---|
| `ZDiode *name` | Zeigervariable vom Typ ZDiode |
| `new ZDiode(...)` | Objekt im Heap erzeugen, Konstruktor aufrufen |
| `name->methode()` | Methode über Zeiger aufrufen |
| `delete name` | Speicher wieder freigeben |

:::merke
`->` statt `.` — weil `zenerDiode` ein **Zeiger** ist. Bei einem normalen Objekt (kein `new`) würde man `.` schreiben.
:::

---

## Vererbung

Vererbung erlaubt es, eine bestehende Klasse zu erweitern. Die **Unterklasse** erbt alle `public` und `protected` Elemente der **Oberklasse**.

```cpp
// Oberklasse
class Diode {
protected:
    double voltageUf;

public:
    Diode(double uf) {
        voltageUf = uf;
    }
    double getVoltageUf() {
        return voltageUf;
    }
};

// Unterklasse erbt von Diode
class ZDiode : public Diode {
private:
    double voltageUz;

public:
    ZDiode(double uz, double uf) : Diode(uf) {  // Oberklassen-Konstruktor aufrufen
        voltageUz = uz;
    }
    double getVoltageUz() {
        return voltageUz;
    }
};
```

Der Aufruf `Diode(uf)` in der Initialisierungsliste `: Diode(uf)` entspricht `super(uf)` in Java.

:::info
Eine Unterklasse **ist ein** Spezialfall der Oberklasse. ZDiode ist eine Diode — daher ergibt Vererbung hier Sinn.
:::
