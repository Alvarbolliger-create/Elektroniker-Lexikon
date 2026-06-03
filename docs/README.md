# Elektronik-Lexikon Dokumentation

Überblick über die Architektur des Projekts. Einzelne Aspekte sind in
separaten Dateien im Detail beschrieben.

## Inhalt

| Datei | Thema | Quellcode |
| --- | --- | --- |
| [lexikon.md](lexikon.md) | Artikel-Anzeige, Navigation, MVVM, alle Block-Typen | [lexikon.py](../lexikon.py) |
| [artikel_format.md](artikel_format.md) | Artikel-Format, alle Direktiven, Syntax-Referenz | [`artikel/`](../artikel/) |
| [cas.md](cas.md) | CAS-Rechner, SymPy-Engine, Einheiten, Plots | [cas_rechner.py](../cas_rechner.py), [cas_plot.py](../cas_plot.py), [phasor_widget.py](../phasor_widget.py) |
| [math_nodes.md](math_nodes.md) | 2D-Formel-Editor, Node-Baum, Cursor | [math_editor.py](../math_editor.py) |

## Architektur auf einen Blick

Das Projekt besteht aus zwei Tools: dem **Lexikon** (Markdown-basierte
Artikel mit Wiki-Verlinkung und 15 Block-Typen) und dem **CAS-Rechner**
(symbolische Mathematik mit 2D-Formel-Eingabe, Plots und Phasor-Diagramm).
Beide Tools leben als Tabs im selben Hauptfenster, das von `main.py` als
schlanke App-Shell bereitgestellt wird.

```mermaid
flowchart TB
    subgraph main["main.py — App-Shell"]
        App[QApplication]
        Win[MainWindow]
        CTX[AppContext]
        TOOLS["TOOLS-Registry\nToolDef-Liste"]
        TabBar
        App --> Win
        Win --> TabBar
        Win --> CTX
        CTX --> TOOLS
    end

    subgraph lex["Lexikon-Tool (lexikon.py)"]
        LW[LexiconWidget]
        VM1[LexiconViewModel]
        ArticleWidget[ArticleContentWidget]
        FormulaBW[FormulaBlockWidget]
        Loader["load_all_articles()\nparse_article_blocks()"]
        LW --> VM1 --> Loader
        LW --> ArticleWidget --> FormulaBW
    end

    subgraph cas["CAS-Tool"]
        CTM[CasTabManager\nmain.py]
        CasCalc[CasCalculator\ncas_rechner.py]
        CasVM[CasViewModel]
        Engine[Engine]
        HelpView
        Settings
        PlotPanel[PlotPanel\ncas_plot.py]
        PhasorW[PhasorWidget\nphasor_widget.py]
        CTM --> CasCalc
        CasCalc --> CasVM --> Engine
        CasVM --> Settings
        CasCalc --> HelpView
        CasCalc --> PlotPanel --> PhasorW
    end

    subgraph editor["2D-Formel-Editor (math_editor.py)"]
        MathEditor
        Nodes["MathNode-Baum\nFraction, Sqrt, Sum, ..."]
        Display[MathFormulaDisplay]
        MathEditor --> Nodes
        Display --> Nodes
    end

    TOOLS --> LW
    TOOLS --> CTM
    CasCalc --> MathEditor
    FormulaBW -.->|"MathFormulaDisplay"| Display
    FormulaBW -.->|"→ CAS Button via AppContext"| CTM
```

## Projektstruktur

```
Elektroniker-Lexikon/
├── main.py               # App-Shell, TOOLS-Registry, MainWindow, CasTabManager
├── lexikon.py            # Lexikon-Tool (Laden, Parsen, alle Block-Typen, Widgets)
├── cas_rechner.py        # CAS-Rechner (Engine, SymPy, Einheiten, HelpView)
├── math_editor.py        # 2D-Formel-Editor (MathNode-Baum, Cursor, Serialisierung)
├── cas_plot.py           # PlotPanel (2D/3D matplotlib + PhasorWidget-Tab)
├── phasor_widget.py      # PhasorWidget (komplexe Zeiger in Gaußscher Zahlenebene)
├── main.qss              # Zentrales Qt-Stylesheet (objectName-Selektoren)
├── themes.json           # Zwei Farbthemen: "Werkstatt" (grün) + "Oszilloskop" (dunkel)
├── pyproject.toml        # Abhängigkeiten: PySide6, SymPy, matplotlib
│
├── artikel/              # 237+ Markdown-Artikel (*.md) in 7 Kategorien
│   ├── _VORLAGE.md       # Artikel-Template mit allen Block-Typen
│   ├── inhaltsverzeichnis.txt  # Redaktioneller Status der Artikel
│   ├── Diagramm/         # SVG-Beschreibungsdateien (*.txt) für externe Generierung
│   ├── EK/               # Elektronik (13 Unterordner)
│   ├── ET/               # Elektrotechnik (12 Unterordner)
│   ├── SH/               # Schaltungstechnik/Digital (7 Unterordner)
│   ├── FT/               # Fertigungstechnik (3 Unterordner)
│   ├── MT/               # Messtechnik (7 Unterordner)
│   ├── SI/               # Sicherheit (5 Unterordner)
│   └── EN/               # Entwicklung/Engineering (2 Unterordner)
│
├── schaltplaene/         # SVG-Schaltplan-Dateien (direkt in Artikeln eingebettet)
│   └── symbole/          # Einzelne Schaltzeichen als SVG
│
├── cas_hilfe/            # 21 Markdown-Hilfe-Seiten für den CAS-Rechner
└── docs/                 # Diese Dokumentation
```

## Datenfluss: vom Klick auf eine Formel zum Ergebnis

```mermaid
sequenceDiagram
    participant User
    participant Lex as LexiconWidget (FormulaBlockWidget)
    participant CTX as AppContext
    participant CTM as CasTabManager
    participant Cas as CasCalculator
    participant Ed as MathEditor
    participant Eng as Engine

    User->>Lex: Klick auf "-> CAS"
    Lex->>CTX: on_send_formula(formel)
    CTX->>CTM: insert_formula(formel)
    CTM->>Cas: insert_formula(formel) [aktiver Tab]
    Cas->>Ed: insert_formula(formel)
    CTX->>CTX: switch_to("CAS Rechner")
    User->>Ed: drückt Enter
    Ed->>Eng: evaluate_all(lines)
    Eng-->>Ed: [(text, is_error), ...]
    Ed-->>User: Ergebnis rechts neben "▶"
```

## Datenfluss: Artikel öffnen und rendern

```mermaid
sequenceDiagram
    participant User
    participant LW as LexiconWidget
    participant VM as LexiconViewModel
    participant FS as Dateisystem
    participant ACW as ArticleContentWidget

    User->>LW: Klick auf Artikel-Eintrag
    LW->>VM: navigate(title)
    LW->>VM: article_blocks(title)
    VM->>VM: ensure_article_text()
    alt Text noch nicht geladen
        VM->>FS: read_text(*.md)
        VM->>VM: parse_frontmatter + cachen
    end
    VM->>VM: parse_article_blocks()
    VM-->>LW: [ArticleHeaderBlock, HeadingBlock, ...]
    LW->>ACW: render_blocks(blocks, article_folder)
    loop für jeden Block
        ACW->>ACW: _block_to_widget(block)
    end
    ACW-->>User: Artikel als Qt-Widgets sichtbar
```

## Tool-Registry-Muster

`main.py` kennt die einzelnen Tools nur über die `TOOLS`-Liste:

```python
TOOLS: list[ToolDef] = [
    ToolDef("Lexikon",      _make_lexikon),
    ToolDef("CAS Rechner",  lambda _ctx: CasTabManager()),
    # Neues Tool einfach hier anfügen.
]
```

Tools kommunizieren über `AppContext`, ohne sich direkt zu kennen:

```python
ctx.switch_to("CAS Rechner")   # Tab wechseln
ctx.get_tool("CAS Rechner")    # Referenz auf anderes Tool holen
```

## MVVM-Muster

Beide Tools folgen dem Model-View-ViewModel-Muster:

- **Model**: pure Funktionen (`load_all_articles`, `parse_article_blocks`)
  und Daten-Container (`Settings`).
- **ViewModel**: `LexiconViewModel`, `CasViewModel` — halten Zustand und
  sind frei von PySide6-Abhängigkeiten.
- **View**: `LexiconWidget`, `CasCalculator`, `ArticleContentWidget` —
  reine Darstellung, delegieren an ihre ViewModels.

```mermaid
flowchart LR
    subgraph Lexikon
        LM["Model\nload_all_articles()\nparse_article_blocks()"]
        LVM["ViewModel\nLexiconViewModel\n(kein Qt)"]
        LV["View\nLexiconWidget\nArticleContentWidget"]
        LM --> LVM --> LV
    end
    subgraph CAS
        CM["Model\nSettings\nEngine.evaluate_all()"]
        CVM["ViewModel\nCasViewModel\n(kein Qt)"]
        CV["View\nCasCalculator\nMathEditor"]
        CM --> CVM --> CV
    end
```

## Styling und Themes

Das Styling ist vollständig zentralisiert:

| Datei | Zweck |
| --- | --- |
| [`main.qss`](../main.qss) | Qt-Stylesheet für alle Widgets via `objectName`-Selektoren |
| [`themes.json`](../themes.json) | Zwei Farbpaletten: `"Werkstatt"` (hellgrün) und `"Oszilloskop"` (dunkel) |

Wichtige `objectName`-Selektoren in `main.qss`:

| Selektor | Widget |
| --- | --- |
| `#appHeader` | Obere App-Leiste mit Tab-Auswahl |
| `#casToolbar` | CAS-Rechner-Toolbar |
| `#casTabBar` | Tab-Leiste der CAS-Tabs |
| `#lexiconToolbar` | Lexikon-Toolbar |

## Zusammenspiel auf einer Seite

- **Einstieg**: [`main()`](../main.py) startet `QApplication` und zeigt
  `MainWindow`. Das Fenster instanziiert alle Tools aus der `TOOLS`-Registry.
- **Tab-Wechsel**: [`TabBar`](../main.py) in `main.py` schaltet zwischen
  `LexiconWidget` und `CasTabManager`.
- **Mehrere CAS-Tabs**: [`CasTabManager`](../main.py) hält beliebig viele
  unabhängige `CasCalculator`-Instanzen. Neuer Tab per `+`-Knopf oder
  `Ctrl+T`, Umbenennen per Doppelklick.
- **Formel-Übergabe**: Eine Formel aus dem Lexikon wird via `AppContext`
  an `CasTabManager.insert_formula` → aktivem `CasCalculator` →
  `MathEditor` weitergeleitet.
- **Plots**: [`PlotPanel`](../cas_plot.py) zeigt 2D- und 3D-Graphen für
  im Editor definierte Funktionen (`f(x) :=`, `g(x,y) :=`).
- **Phasor-Diagramm**: [`PhasorWidget`](../phasor_widget.py) stellt
  komplexe Variablen als Zeiger in der Gaußschen Zahlenebene dar.
- **Styling**: Zentral in [`main.qss`](../main.qss) via `objectName`-
  Selektoren (`#appHeader`, `#casToolbar`, `#casTabBar`, ...).
