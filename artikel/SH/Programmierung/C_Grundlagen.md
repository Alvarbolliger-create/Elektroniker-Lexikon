---
title: C-Grundlagen (Variablen, Schleifen, Funktionen, Arrays)
kategorie: SH
kapitel: Programmierung
tags: [c, programmierung, datentypen, variablen, if-else, switch-case, for-schleife, while-schleife, do-while, funktion, prototyp, array, indexierung, unsigned, signed]
_status: NEU
---

:::hbox
:::vbox
**Voraussetzungen**
- [[Zahlensysteme (Dual, Hexadezimal)]]
- [[Bitmanipulation in der Programmierung]]
:::
:::vbox
**Verwandte Artikel**
- [[Mikrocontroller]]
:::
:::vbox
**Führt weiter zu**
- [[OOP Grundlagen (Klassen, Objekte, Vererbung)]]
:::
:::

---

C ist die in der Mikrocontroller-Programmierung am weitesten verbreitete Sprache — kompakt, hardwarenah und auf praktisch jeder Plattform verfügbar. Dieser Artikel erklärt die vier Grundbausteine: Daten speichern, Entscheidungen treffen, Schleifen schreiben und Funktionen aufbauen.

## Variablen und Datentypen

Eine **Variable** reserviert einen benannten Speicherbereich im RAM. Vor der ersten Verwendung muss sie mit einem **Datentyp** deklariert werden — dieser legt fest, wie viele Bits reserviert werden und ob negative Werte möglich sind:

| Datentyp | Breite | Wertebereich (positiv) | Typische Verwendung |
|---|---|---|---|
| `unsigned char` | 8 Bit | 0 … 255 | Bytes, Registerwerte, kleine Zähler |
| `signed char` | 8 Bit | −128 … +127 | Kleine Werte mit Vorzeichen |
| `unsigned int` | 16 Bit | 0 … 65 535 | Mittlere Zähler |
| `int` | 16 Bit | −32 768 … +32 767 | Ganzzahlen mit Vorzeichen |
| `unsigned long` | 32 Bit | 0 … 4 294 967 295 | Zeitstempel, grosse Zähler |
| `float` | 32 Bit | ±3.4 × 10³⁸ | Kommazahlen (ca. 7 Stellen genau) |
| `double` | 64 Bit | ±1.8 × 10³⁰⁸ | Kommazahlen (ca. 15 Stellen genau) |
| `bool` | 8 Bit | false (0) / true (1) | Wahrheitswerte |

:::warning
Den **kleinstmöglichen Typ** wählen, der den Wertebereich abdeckt — nicht automatisch `int`. Auf einem 8-Bit-Mikrocontroller braucht jede `int`-Variable zwei Speicherzellen; für Werte bis 255 reicht `unsigned char` und spart Platz und Rechenzeit.
:::

Deklaration und Initialisierung (erster Wertzuweisung) können kombiniert werden:

```c
unsigned char error_code = 0;
float temperature = 23.5;
bool alarm_active = false;
```

### Ausführungszeit von Operationen

Nicht alle Rechenoperationen sind gleich schnell. Auf einem Mikrocontroller ohne Gleitkomma-Hardware (FPU) gilt:

| Operation | Beispiel | Taktzyklen (ca.) | Geschwindigkeit |
|---|---|---|---|
| Bitoperation (AND, OR, Shift) | `x << 2` | 1 | sehr schnell |
| Addition / Subtraktion | `a + b` | 1 | sehr schnell |
| Multiplikation (Integer) | `a * b` | 2–4 | schnell |
| Division (Integer) | `a / b` | 8–32 | langsam |
| Kommazahl-Rechnung (float/double) | `a * 1.5` | 50–200 | sehr langsam |

:::merke
Auf Mikrocontrollern ohne FPU wird `float`/`double`-Arithmetik in Software emuliert und kann **100× langsamer** sein als eine Integer-Operation. In zeitkritischem Code (Interrupts, Regelschleifen) daher Integer oder Bitoperationen bevorzugen.

Ausführungszeit einer Anweisung: **t = Taktzyklen / f_clock**

Beispiel: 4 Zyklen bei 16 MHz → t = 4 / 16 000 000 = **250 ns**
:::

### Hexadezimale Konstanten in C

Ganzzahlkonstanten können dezimal **oder** hexadezimal angegeben werden — das Präfix `0x` kennzeichnet eine Hex-Zahl:

```c
unsigned char a = 10;    // dezimal
unsigned char b = 0x0A;  // hexadezimal — identisch mit 10
```

:::merke
Umrechnung: `0x0A` = 0 × 16 + 10 = **10**. `0xFF` = 15 × 16 + 15 = **255**. Beim Vergleich in `switch/case` spielt es keine Rolle, ob der Wert als Hex oder Dezimal übergeben wird — C rechnet intern immer mit dem gleichen Bitmuster. → [[Zahlensysteme (Dual, Hexadezimal)]]
:::

## Kontrollstrukturen

### if / else

Die grundlegende Verzweigung — der Block in `{}` wird nur ausgeführt, wenn die Bedingung wahr ist:

```c
if (temperature > 80.0) {
    alarm_active = true;
} else {
    alarm_active = false;
}
```

Mehrere Bedingungen lassen sich mit `else if` aneinanderreihen — sobald eine Bedingung zutrifft, werden die restlichen übersprungen:

```c
if (error_code == 0) {
    // kein Fehler
} else if (error_code == 1) {
    // Warnung
} else {
    // unbekannter Fehler
}
```

### switch / case

Wenn eine **einzige Variable** gegen viele feste Werte geprüft wird, ist `switch` übersichtlicher als eine lange `if`-Kette. Jedes `case` muss mit `break` abgeschlossen werden — sonst "fällt" die Ausführung in den nächsten Case durch:

```c
void error(unsigned char ErrorNo) {
    switch (ErrorNo) {
        case 10:
            printf("no_connection");
            break;
        case 11:
            printf("check_cable");
            break;
        case 12:
            printf("timeout");
            break;
        case 13:
            printf("no_data");
            break;
        default:
            printf("error");
    }
}
```

:::merke
`error(0x0A)` übergibt den Wert **10** dezimal (0x0A = 10). Die Funktion springt zu `case 10:` und gibt `"no_connection"` aus. Hexadezimale Argumente werden vor dem Vergleich in ihren dezimalen Wert umgewandelt — `case 10:` und `case 0x0A:` sind identisch.
:::

:::warning
Fehlt das `break`, läuft die Ausführung automatisch in den nächsten `case` weiter (**fall-through**) — einer der häufigsten Programmierfehler in C! Der `default`-Zweig fängt alle Werte ab, für die kein `case` definiert ist, und sollte immer vorhanden sein.
:::

### for-Schleife

Für Schleifen mit **bekannter** Anzahl Durchläufe:

```c
for (int i = 0; i < 8; i++) {
    // wird 8-mal ausgeführt: i = 0, 1, 2, ..., 7
}
```

Aufbau: `for (Initialisierung; Bedingung; Schritt nach jedem Durchlauf)`

### while-Schleife

Prüft die Bedingung **vor** jedem Durchlauf — der Rumpf wird möglicherweise **keinmal** ausgeführt:

```c
while (sensor_value > threshold) {
    sensor_value = read_sensor();
}
```

### do-while-Schleife

Prüft die Bedingung **nach** jedem Durchlauf — der Rumpf wird **mindestens einmal** ausgeführt:

```c
int counter = 1;
do {
    counter = counter * 3;
} while (counter <= 27);
```

:::merke
**Durchläufe zählen:** Startwert notieren, dann jeden Schritt nachverfolgen bis die Bedingung falsch wird:

| Durchlauf | Rechnung | counter nach Rechnung | Bedingung (≤ 27) |
|---|---|---|---|
| 1 | 1 × 3 | 3 | 3 ≤ 27 → weiter |
| 2 | 3 × 3 | 9 | 9 ≤ 27 → weiter |
| 3 | 9 × 3 | 27 | 27 ≤ 27 → weiter |
| 4 | 27 × 3 | 81 | 81 > 27 → **Abbruch** |

Die Schleife wird **4-mal** durchlaufen. Die Prüfung erfolgt immer nach der Berechnung.
:::

## Funktionen

Eine Funktion fasst wiederverwendbaren Code unter einem Namen zusammen. Der **Funktionsprototyp** deklariert die Schnittstelle und steht vor dem ersten Aufruf (typisch in einer `.h`-Headerdatei):

```c
bool checkValue(unsigned int value);
```

:::merke
Die vier Bestandteile eines Funktionsprototyps:

| Element | Beispiel | Bedeutung |
|---|---|---|
| **Rückgabetyp** | `bool` | Welchen Typ gibt die Funktion zurück? |
| **Funktionsname** | `checkValue` | Unter welchem Namen wird sie aufgerufen? |
| **Parametertyp** | `unsigned int` | Welchen Datentyp hat der Übergabewert? |
| **Parametername** | `value` | Wie heisst der Parameter innerhalb der Funktion? |

`void` als Rückgabetyp bedeutet: die Funktion gibt nichts zurück.
:::

Die **Implementierung** enthält den eigentlichen Code und muss exakt zur Prototyp-Deklaration passen:

```c
bool checkValue(unsigned int value) {
    if (value > 100) {
        return true;
    }
    return false;
}
```

:::tip
Mehrere Parameter werden durch Kommas getrennt: `float calc(float u, float r)`. Jeder Parameter hat seinen eigenen Typ und Namen — auch wenn zwei Parameter denselben Typ haben, muss dieser zweimal geschrieben werden: `int add(int a, int b)`.
:::

## Arrays

Ein **Array** ist eine geordnete Folge gleichartiger Werte im RAM, erreichbar über einen gemeinsamen Namen. Grösse und Typ werden bei der Deklaration angegeben:

```c
unsigned char randNumbers[7] = {3, 13, 17, 26, 37, 43, 62};
```

:::warning
**Indexierung beginnt bei 0!** Das erste Element hat Index 0, das letzte Index (Grösse − 1):

| Index | [0] | [1] | [2] | [3] | [4] | [5] | [6] |
|---|---|---|---|---|---|---|---|
| Wert | 3 | 13 | 17 | 26 | 37 | 43 | 62 |

`randNumbers[3]` liefert **26**, nicht 37. Ein Zugriff mit Index 7 (= Grösse) greift auf einen nicht reservierten Speicherbereich zu — undefiniertes Verhalten!
:::

Auf einzelne Elemente wird mit dem Index in `[]` zugegriffen:

```c
unsigned int newValue = randNumbers[3] * randNumbers[4];
// = 26 * 37 = 962
```

Arrays und `for`-Schleifen ergänzen sich ideal — der Schleifenzähler dient direkt als Index:

```c
for (int i = 0; i < 7; i++) {
    // randNumbers[i] ist das i-te Element
}
```
