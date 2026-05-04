"""Artikel-Lexikon als eigenstaendiges Tool-Widget.

Das Modul enthaelt saemtliche Lexikon-Funktionalitaet: Laden der Artikel
aus Markdown-Dateien (rekursiv, mit Unterordner-Unterstuetzung),
Konvertierung in typisierte Block-Objekte, ViewModel fuer den
Anwendungszustand und das eigentliche ``LexiconWidget`` mit drei
Spalten (Artikelliste, Artikel-Anzeige, Tags/Verlinkungen/Formeln).

Architektur (MVVM - Model-View-ViewModel):
    Model     - ``load_all_articles``, ``parse_frontmatter``,
                ``parse_tags``, ``parse_article_blocks``,
                ``format_inline``, ``ensure_article_text``.
    ViewModel - ``LexiconViewModel``: Anwendungszustand, Filterung,
                Block-Aufbereitung. Keine GUI-Abhaengigkeiten.
    View      - ``LexiconWidget``, ``FormulaBlockWidget``,
                ``ArticleContentWidget``, ``HamburgerButton``:
                rein visuelle Darstellung, Delegation an ViewModel.

Lazy Loading:
    Beim Start werden ausschliesslich Frontmatter-Daten (Titel,
    Kategorie, Tags) eingelesen. Der Fliesstext eines Artikels wird
    erst beim ersten Oeffnen nachgeladen und danach gecacht.

Abkuerzungen (Initialnotation):
    CAS  - Computer Algebra System (symbolische Mathematik).
    GUI  - Graphical User Interface.
    HTML - Hypertext Markup Language.
    MVVM - Model-View-ViewModel.
    SVG  - Scalable Vector Graphics.
"""

from __future__ import annotations

import json
import math
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, TypeAlias
from urllib.parse import quote, unquote

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QUrl
from PySide6.QtGui import QColor, QFont, QKeySequence, QPainter, QPaintEvent, QPen, QPixmap, QShortcut
from PySide6.QtSvg import QSvgRenderer
from PySide6.QtSvgWidgets import QSvgWidget
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLayout,
    QLineEdit,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTextBrowser,
    QTreeWidget,
    QTreeWidgetItem,
    QTreeWidgetItemIterator,
    QVBoxLayout,
    QWidget,
)

from math_editor import MathFormulaDisplay

# ── Modul-Konstanten ──────────────────────────────────────────────────────────
ARTICLES_FOLDER: Path = Path(__file__).parent / "artikel"

# Farbpaare (Hintergrund, Vordergrund) fuer die Tag-Badges in der
# Artikel-Detailansicht. Reihenfolge wird per Index modulo Laenge rotiert.
TAG_COLORS: list[tuple[str, str]] = [
    ("#dbeafe", "#1e40af"),
    ("#dcfce7", "#166534"),
    ("#fef3c7", "#92400e"),
    ("#fce7f3", "#9d174d"),
    ("#ede9fe", "#5b21b6"),
]

# Bilddatei-Endungen fuer Raster-Bilder (werden via QPixmap geladen).
_RASTER_SUFFIXES: frozenset[str] = frozenset({
    ".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp",
})


# ── Artikel-Block-Typen ───────────────────────────────────────────────────────
@dataclass
class HeadingBlock:
    """Ueberschrift mit Hierarchie-Ebene 1-3."""

    level: int
    text: str


@dataclass
class ParagraphBlock:
    """Fliesstext-Absatz mit HTML-Inline-Formatierung."""

    html: str


@dataclass
class CodeBlock:
    """Formel-Block (:::formel): geordnete Liste nicht-leerer Formelzeilen."""

    lines: list[str]


@dataclass
class MonospaceBlock:
    """Monospace-Block (:::monospace): vorformatierter Text ohne Formelinterpretation."""

    lines: list[str]


@dataclass
class ListBlock:
    """Aufzaehlung: jeder Eintrag als HTML-formatierter Inline-Text."""

    items: list[str]


@dataclass
class ImageBlock:
    """Eingebettetes Bild mit Alternativtext und relativem Pfad."""

    alt: str
    path: str


@dataclass
class TableBlock:
    """Markdown-Tabelle: Kopfzeile + Datenzeilen mit Inline-HTML."""

    headers: list[str]
    rows: list[list[str]]


@dataclass
class ArticleHeaderBlock:
    """Artikel-Kopfzeile mit Kategorie und optionalen Symbol-/Einheit-Badges."""

    kategorie: str
    symbol: str | None
    einheit: str | None


@dataclass
class SchematicBlock:
    """Schaltplan als SVG- oder PNG-Datei mit optionalem Titel."""

    path: str
    title: str | None = None


@dataclass
class WaveformBlock:
    """Zeitdiagramm mit benannten Signalspuren."""

    # Jede Spur: {"name": str, "values": list[0|1]} für digitale Signale
    # oder {"name": str, "values": list[float], "min": float, "max": float} für analog
    signals: list[dict]
    sample_labels: list[str] | None = None  # Beschriftung der X-Achse


@dataclass
class PlotBlock:
    """Mathematischer Funktionsgraph mit einer oder mehreren Kurven.

    Syntax im Artikel::

        :::plot
        var: t
        range: 0, 5
        Laden:    1 - exp(-t)
        Entladen: exp(-t)
        xlabel: Zeit (τ)
        ylabel: U / U₀
        :::
    """

    var: str
    x_range: tuple[float, float]
    curves: list[dict]          # [{"label": str, "expr": str}, ...]
    xlabel: str = ""
    ylabel: str = ""


@dataclass
class PinoutBlock:
    """IC- oder Stecker-Pinbelegung: Pin-Nummer → Funktionsname."""

    component: str                   # z.B. "NE555", "RJ45"
    pins: list[dict]                 # [{"nr": 1, "name": "GND", "info": "..."}, ...]
    package: str | None = None       # z.B. "DIP-8", "SOT-23"


@dataclass
class TruthTableBlock:
    """Wahrheitstabelle fuer Logikgatter/-schaltungen."""

    inputs: list[str]                # Eingangsvariablen, z.B. ["A", "B"]
    outputs: list[str]               # Ausgangsvariablen, z.B. ["Q", "Q̄"]
    rows: list[list[int]]            # Werte 0/1 pro Zeile (inputs + outputs)


@dataclass
class NoteBlock:
    """Hervorgehobener Hinweis-Block (Warnung, Tipp, Info etc.)."""

    text: str
    kind: str = "info"               # "info" | "tip" | "warning" | "danger" | "norm" | "merke"


@dataclass
class HBoxBlock:
    """Horizontales Layout: Kinder-Bloecke nebeneinander."""

    children: list["ArticleBlock"]


@dataclass
class VBoxBlock:
    """Vertikales Layout: Kinder-Bloecke untereinander."""

    children: list["ArticleBlock"]


ArticleBlock: TypeAlias = (
    HeadingBlock
    | ParagraphBlock
    | CodeBlock
    | MonospaceBlock
    | ListBlock
    | ImageBlock
    | TableBlock
    | ArticleHeaderBlock
    | SchematicBlock
    | WaveformBlock
    | PlotBlock
    | PinoutBlock
    | TruthTableBlock
    | NoteBlock
    | HBoxBlock
    | VBoxBlock
)


# ── Artikel laden ─────────────────────────────────────────────────────────────
def _read_frontmatter_header(path: Path) -> str:
    """Liest nur den YAML-Frontmatter-Block einer Markdown-Datei.

    Stoppt nach dem schliessenden ``---`` oder spaetestens nach 60 Zeilen,
    um bei grossen Dateien unnoetige Datei-IO zu vermeiden.
    """
    lines: list[str] = []
    in_block: bool = False
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            lines.append(line)
            stripped = line.rstrip("\n")
            if stripped == "---":
                if not in_block:
                    in_block = True
                else:
                    break
            elif not in_block and stripped.strip():
                break
            if len(lines) >= 60:
                break
    return "".join(lines)


def _subfolder_category(path: Path, root: Path) -> str:
    """Leitet die Standardkategorie aus dem direkten Unterordner-Namen ab.

    Artikel im Stammverzeichnis erhalten die Kategorie ``Allgemein``.
    """
    rel = path.relative_to(root)
    if len(rel.parts) > 1:
        return rel.parts[0].replace("_", " ").title()
    return "Allgemein"


def ensure_article_text(article: dict[str, Any]) -> None:
    """Laedt den Fliesstext des Artikels bei Bedarf aus der Datei.

    Nach dem ersten Lesen wird der Text gecacht; nachfolgende Zugriffe
    verursachen keine Datei-IO mehr (Lazy Loading).
    """
    if article["text"] is None:
        content: str = article["datei"].read_text(encoding="utf-8")
        _, text = parse_frontmatter(content)
        article["text"] = text


def load_all_articles(
    folder: Path = ARTICLES_FOLDER,
) -> dict[str, dict[str, Any]]:
    """Liest den Frontmatter aller Markdown-Dateien im Artikel-Ordner ein.

    Durchsucht den Ordner rekursiv (Unterordner via ``rglob``). Der
    Fliesstext wird nicht geladen (Lazy Loading via ``ensure_article_text``).

    Args:
        folder: Wurzelordner mit den Markdown-Dateien. Standard ist der
            Lexikon-Ordner; die CAS-Hilfe nutzt einen anderen Ordner.

    Returns:
        Mapping Titel -> Artikel-Datensatz. Der Datensatz enthaelt die
        Schluessel ``titel``, ``kategorie``, ``tags``, ``meta``,
        ``text`` (initial ``None``) und ``datei``.
    """
    articles: dict[str, dict[str, Any]] = {}
    if not folder.exists():
        return articles
    for path in sorted(folder.rglob("*.md")):
        header = _read_frontmatter_header(path)
        meta, _ = parse_frontmatter(header)
        default_cat = _subfolder_category(path, folder)
        title = meta.get("title", path.stem.replace("_", " ").title())
        articles[title] = {
            "titel": title,
            "kategorie": meta.get("kategorie", default_cat),
            "tags": parse_tags(meta.get("tags", "")),
            "meta": meta,
            "text": None,
            "datei": path,
        }
    return articles


def parse_frontmatter(content: str) -> tuple[dict[str, str], str]:
    """Trennt YAML-artigen Frontmatter-Block vom Fliesstext.

    Ein Frontmatter beginnt und endet mit einer ``---``-Zeile. Zwischen
    den beiden Trennern werden ``key: value``-Paare erwartet.
    """
    meta: dict[str, str] = {}
    text = content
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip()
            text = parts[2].strip()
    return meta, text


def parse_tags(raw: str) -> list[str]:
    """Wandelt einen Tag-Eintrag des Frontmatters in eine Liste um.

    Eckige Klammern sind optional, Trennung erfolgt per Komma. Leere
    Eintraege werden verworfen.
    """
    raw = raw.strip().strip("[]")
    return [t.strip() for t in raw.split(",") if t.strip()] if raw else []


# ── Markdown -> Bloecke ───────────────────────────────────────────────────────
def parse_article_blocks(
    text: str,
    all_articles: dict[str, dict[str, Any]],
) -> list[ArticleBlock]:
    """Parst Markdown-Artikeltext in typisierte Block-Objekte.

    Wiki-Links der Form ``[[Ziel]]`` bzw. ``[[Ziel|Anzeige]]`` werden
    vorab in HTML-Anker umgeschrieben. Anschliessend werden Markdown-
    Zeilen in Ueberschriften, Absaetze, Code-Bloecke, Aufzaehlungen und
    Bilder klassifiziert.

    Args:
        text: Roher Markdown-Text ohne YAML-Frontmatter.
        all_articles: Alle bekannten Artikel fuer Wiki-Link-Aufloesung.

    Returns:
        Geordnete Liste typisierter Artikel-Bloecke.
    """

    def replace_link(match: re.Match[str]) -> str:
        target = match.group(1).strip()
        label = match.group(2).strip() if match.group(2) else target
        found = next(
            (t for t in all_articles if t.lower() == target.lower()), None
        )
        if found:
            return (
                f'<a href="artikel://x/{quote(found, safe="")}" '
                f'style="color:#2563eb;text-decoration:none;">{label}</a>'
            )
        return f'<span style="color:#9ca3af;">{label}</span>'

    text = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", replace_link, text)
    lines = text.split("\n")
    blocks: list[ArticleBlock] = []
    in_code: bool = False
    code_buf: list[str] = []
    in_list: bool = False
    list_buf: list[str] = []

    def flush_list() -> None:
        nonlocal in_list, list_buf
        if in_list and list_buf:
            blocks.append(ListBlock(items=list_buf[:]))
            list_buf = []
            in_list = False

    i = 0
    while i < len(lines):
        line = lines[i]

        # :::typ [args] ... ::: Direktive (mit Verschachtelungs-Unterstützung)
        if line.strip().startswith(":::") and line.strip() != ":::":
            flush_list()
            depth = 1
            body: list[str] = []
            j = i + 1
            while j < len(lines) and depth > 0:
                inner = lines[j].strip()
                if inner.startswith(":::") and inner != ":::":
                    depth += 1
                elif inner == ":::":
                    depth -= 1
                if depth > 0:
                    body.append(lines[j])
                j += 1
            blk = _parse_directive(line.strip(), body, all_articles)
            if blk is not None:
                blocks.append(blk)
            i = j
            continue

        if line.strip().startswith("```"):
            flush_list()
            if not in_code:
                in_code = True
                code_buf = []
            else:
                in_code = False
                mono_lines = [ln for ln in code_buf if ln.strip()]
                if mono_lines:
                    blocks.append(MonospaceBlock(lines=mono_lines))
                code_buf = []
            i += 1
            continue

        if in_code:
            code_buf.append(line)
            i += 1
            continue

        # Tabelle: Kopfzeile + Separator + >=0 Datenzeilen.
        if (
            _is_table_row(line)
            and i + 1 < len(lines)
            and _is_table_separator(lines[i + 1])
        ):
            flush_list()
            headers = [format_inline(c) for c in _split_table_row(line)]
            i += 2
            rows: list[list[str]] = []
            while i < len(lines) and _is_table_row(lines[i]):
                rows.append(
                    [format_inline(c) for c in _split_table_row(lines[i])]
                )
                i += 1
            blocks.append(TableBlock(headers=headers, rows=rows))
            continue

        if line.startswith("# "):
            flush_list()
            blocks.append(HeadingBlock(level=1, text=line[2:]))
        elif line.startswith("## "):
            flush_list()
            blocks.append(HeadingBlock(level=2, text=line[3:]))
        elif line.startswith("### "):
            flush_list()
            blocks.append(HeadingBlock(level=3, text=line[4:]))
        elif line.startswith("- "):
            in_list = True
            list_buf.append(format_inline(line[2:]))
        elif line.strip() == "":
            flush_list()
        else:
            img_match = re.fullmatch(
                r"!\[([^\]]*)\]\(([^)]+)\)", line.strip()
            )
            if img_match:
                flush_list()
                blocks.append(
                    ImageBlock(
                        alt=img_match.group(1), path=img_match.group(2)
                    )
                )
            else:
                flush_list()
                blocks.append(ParagraphBlock(html=format_inline(line)))

        i += 1

    flush_list()
    return blocks


def _is_table_row(line: str) -> bool:
    """True wenn die Zeile wie eine Markdown-Tabellenzeile aussieht."""
    s = line.strip()
    return len(s) >= 2 and s.startswith("|") and s.endswith("|")


def _is_table_separator(line: str) -> bool:
    """True wenn die Zeile eine Trennzeile (``|---|---|``) ist."""
    s = line.strip()
    if not (s.startswith("|") and s.endswith("|")):
        return False
    inner = s[1:-1]
    cells = inner.split("|")
    return bool(cells) and all(
        re.fullmatch(r"\s*:?-+:?\s*", c) for c in cells
    )


def _split_table_row(line: str) -> list[str]:
    """Zerlegt eine Tabellenzeile in ihre Zellen (escaped ``\\|`` bleibt)."""
    s = line.strip()
    placeholder = "\x00"
    s = s.replace("\\|", placeholder)
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip().replace(placeholder, "|") for c in s.split("|")]


def format_inline(text: str) -> str:
    """Ersetzt die Markdown-Inline-Marker ``**fett**`` und ``\\`code\\```.

    Reine Textformatierung ohne Block-Verarbeitung.
    """
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(
        r"`(.+?)`",
        r'<code style="background:#f1f5f9;padding:1px 5px;'
        r'border-radius:4px;font-size:13px;">\1</code>',
        text,
    )
    return text


# ── Direktiven-Parser ────────────────────────────────────────────────────────

def _parse_directive(
    header_line: str,
    body_lines: list[str],
    all_articles: dict[str, Any],
) -> ArticleBlock | None:
    """Parst einen :::typ [args] ... ::: Direktiven-Block in ein Block-Objekt."""
    stripped = header_line.strip()[3:].strip()
    parts = stripped.split(None, 1)
    if not parts:
        return None
    kind = parts[0].lower()
    args = parts[1].strip() if len(parts) > 1 else ""
    body_text = "\n".join(body_lines).strip()

    if kind in ("warning", "info", "tip", "danger", "norm", "merke"):
        return NoteBlock(text=body_text, kind=kind)
    if kind == "note":
        note_kind = args if args in ("warning", "info", "tip", "danger", "norm", "merke") else "info"
        return NoteBlock(text=body_text, kind=note_kind)
    if kind == "formel":
        formula_lines = [ln.strip() for ln in body_lines if ln.strip()]
        return CodeBlock(lines=formula_lines) if formula_lines else None
    if kind == "monospace":
        return MonospaceBlock(lines=body_lines)
    if kind == "schematic":
        return SchematicBlock(path=body_text, title=args or None)
    if kind == "waveform":
        return _parse_waveform_body(body_lines)
    if kind == "plot":
        return _parse_plot_body(body_lines)
    if kind == "pinout":
        return _parse_pinout_body(args, body_lines)
    if kind == "truth":
        return _parse_truth_body(args, body_lines)
    if kind == "hbox":
        return HBoxBlock(children=parse_article_blocks(body_text, all_articles))
    if kind == "vbox":
        return VBoxBlock(children=parse_article_blocks(body_text, all_articles))
    return None


def _parse_waveform_body(body_lines: list[str]) -> WaveformBlock:
    """Parst Waveform-Zeilen in ein WaveformBlock-Objekt.

    Syntax pro Zeile::

        labels: T0,T1,T2,T3
        CLK: 0,1,0,1
        ANALOG: ~0.0,1.5,3.3,0.0   # Tilde = analoges Signal
    """
    signals: list[dict] = []
    sample_labels: list[str] | None = None
    for line in body_lines:
        line = line.strip()
        if not line or ":" not in line:
            continue
        name, _, raw = line.partition(":")
        name = name.strip()
        raw_vals = [v.strip() for v in raw.strip().split(",")]
        if name.lower() == "labels":
            sample_labels = raw_vals
            continue
        if raw_vals and raw_vals[0].startswith("~"):
            raw_vals[0] = raw_vals[0][1:]
            try:
                values = [float(v) for v in raw_vals]
                signals.append({
                    "name": name, "values": values,
                    "min": min(values), "max": max(values), "analog": True,
                })
            except ValueError:
                pass
        else:
            try:
                values = [int(v) for v in raw_vals]
                signals.append({"name": name, "values": values, "analog": False})
            except ValueError:
                pass
    return WaveformBlock(signals=signals, sample_labels=sample_labels)


# Erlaubte Funktionen für den Plot-Ausdruck-Evaluator
_PLOT_NS: dict = {
    "exp": math.exp, "log": math.log, "log10": math.log10,
    "sqrt": math.sqrt, "abs": abs,
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "pi": math.pi, "e": math.e,
    "max": max, "min": min,
}


def _parse_plot_body(body_lines: list[str]) -> PlotBlock:
    """Parst einen :::plot-Block in ein PlotBlock-Objekt.

    Syntax::

        var: t
        range: 0, 5
        Laden:    1 - exp(-t)
        Entladen: exp(-t)
        xlabel: Zeit (τ)
        ylabel: U / U₀
    """
    var = "x"
    x_range = (0.0, 1.0)
    curves: list[dict] = []
    xlabel = ""
    ylabel = ""

    for line in body_lines:
        line = line.strip()
        if not line or ":" not in line:
            continue
        key, _, val = line.partition(":")
        key = key.strip()
        val = val.strip()
        key_lower = key.lower()

        if key_lower == "var":
            var = val
        elif key_lower == "range":
            parts = [v.strip() for v in val.split(",")]
            if len(parts) == 2:
                try:
                    x_range = (float(parts[0]), float(parts[1]))
                except ValueError:
                    pass
        elif key_lower == "xlabel":
            xlabel = val
        elif key_lower == "ylabel":
            ylabel = val
        else:
            expr = val.replace("^", "**")
            curves.append({"label": key, "expr": expr})

    return PlotBlock(var=var, x_range=x_range, curves=curves,
                     xlabel=xlabel, ylabel=ylabel)


def _parse_pinout_body(args: str, body_lines: list[str]) -> PinoutBlock:
    """Parst Pinbelegungs-Zeilen in ein PinoutBlock-Objekt.

    Syntax Kopfzeile: ``NE555 DIP-8`` oder ``NE555 (DIP-8)``
    Syntax Pin-Zeile: ``1: GND | Masse``
    """
    package: str | None = None
    paren = re.search(r"\(([^)]+)\)", args)
    if paren:
        package = paren.group(1).strip()
        component = args[: paren.start()].strip()
    else:
        p = args.rsplit(None, 1)
        if len(p) == 2 and re.match(r"[A-Za-z]{2,}-\d+", p[1]):
            component, package = p[0], p[1]
        else:
            component = args or "?"

    pins: list[dict] = []
    for line in body_lines:
        line = line.strip()
        m = re.match(r"(\d+)\s*:\s*(.+)", line)
        if not m:
            continue
        nr = int(m.group(1))
        rest = m.group(2).strip()
        if "|" in rest:
            name, _, info = rest.partition("|")
            pins.append({"nr": nr, "name": name.strip(), "info": info.strip()})
        else:
            pins.append({"nr": nr, "name": rest, "info": ""})
    return PinoutBlock(component=component, pins=pins, package=package)


def _parse_truth_body(args: str, body_lines: list[str]) -> TruthTableBlock:
    """Parst eine Wahrheitstabelle aus einer :::truth-Direktive.

    Syntax Kopf: ``A,B | Q,Q̄``   (Eingänge | Ausgänge)
    Syntax Zeile: ``0,1 | 1,0``  oder ``0,1,1,0``
    """
    inputs: list[str] = []
    outputs: list[str] = []
    if "|" in args:
        in_part, _, out_part = args.partition("|")
        inputs = [s.strip() for s in in_part.split(",") if s.strip()]
        outputs = [s.strip() for s in out_part.split(",") if s.strip()]

    rows: list[list[int]] = []
    for line in body_lines:
        line = line.strip()
        if not line:
            continue
        if not inputs and not outputs:
            try:
                if "|" in line:
                    in_p, _, out_p = line.partition("|")
                    vals = [int(v.strip()) for v in in_p.split(",") if v.strip()]
                    vals += [int(v.strip()) for v in out_p.split(",") if v.strip()]
                else:
                    vals = [int(v.strip()) for v in line.split(",") if v.strip()]
                rows.append(vals)
            except ValueError:
                if "|" in line:
                    in_part, _, out_part = line.partition("|")
                    inputs = [s.strip() for s in in_part.split(",") if s.strip()]
                    outputs = [s.strip() for s in out_part.split(",") if s.strip()]
            continue
        try:
            if "|" in line:
                in_p, _, out_p = line.partition("|")
                vals = [int(v.strip()) for v in in_p.split(",") if v.strip()]
                vals += [int(v.strip()) for v in out_p.split(",") if v.strip()]
            else:
                vals = [int(v.strip()) for v in line.split(",") if v.strip()]
            rows.append(vals)
        except ValueError:
            pass

    if not inputs and not outputs and rows:
        total = len(rows[0])
        in_count = max(1, total // 2)
        inputs = [chr(ord("A") + i) for i in range(in_count)]
        outputs = [chr(ord("Q") + i) for i in range(total - in_count)]

    return TruthTableBlock(inputs=inputs, outputs=outputs, rows=rows)


# ── ViewModel ────────────────────────────────────────────────────────────────
class LexiconViewModel:
    """ViewModel des Elektronik-Lexikons.

    Haelt den Anwendungszustand (Artikeldaten, Navigationsverlauf,
    aktuelle Auswahl) und bereitet Daten fuer die View auf.
    Enthaelt keinerlei GUI-Abhaengigkeiten.
    """

    def __init__(
        self,
        folder: Path = ARTICLES_FOLDER,
        title: str = "Elektronik Lexikon",
    ) -> None:
        self.folder: Path = folder
        self.title: str = title
        self.all_articles: dict[str, dict[str, Any]] = load_all_articles(
            folder
        )
        self.history: list[str] = []
        self.current_title: str | None = None
        self.recent_articles: list[str] = []
        self._load_state()

    def filtered_articles(self, query: str) -> dict[str, dict[str, Any]]:
        """Filtert Artikel anhand der Suchanfrage.

        Gesucht wird case-insensitive in Titel, Tags und Kategoriename.

        Args:
            query: Suchbegriff. Leerer String = alle Artikel.

        Returns:
            Mapping Titel -> Artikel-Datensatz (gefiltert).
        """
        q = query.strip().lower()
        if not q:
            return dict(self.all_articles)
        return {
            title: article
            for title, article in self.all_articles.items()
            if q in title.lower()
            or any(q in t.lower() for t in article["tags"])
            or q in article["kategorie"].lower()
        }

    def navigate(self, title: str, push_history: bool = True) -> None:
        """Setzt ``current_title`` und aktualisiert den Navigationsverlauf.

        Args:
            title: Zielartikel.
            push_history: Wenn True und ein aktueller Artikel offen ist,
                wird dieser vor dem Wechsel in den Verlauf geschoben.
        """
        if push_history and self.current_title:
            self.history.append(self.current_title)
        self.current_title = title

    def go_back(self) -> str | None:
        """Kehrt zum vorherigen Artikel zurueck.

        Returns:
            Titel des vorherigen Artikels oder ``None`` wenn kein Verlauf.
        """
        return self.history.pop() if self.history else None

    def can_go_back(self) -> bool:
        """True, wenn der Navigationsverlauf mindestens einen Eintrag hat."""
        return bool(self.history)

    def _state_path(self) -> Path:
        appdata = Path(os.environ.get("APPDATA", Path.home())) / "ElektronikLexikon"
        appdata.mkdir(parents=True, exist_ok=True)
        return appdata / f"{self.folder.name}_state.json"

    def _load_state(self) -> None:
        path = self._state_path()
        if not path.exists():
            return
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            recents = data.get("recent", [])
            self.recent_articles = [r for r in recents if r in self.all_articles][:5]
        except Exception:
            pass

    def save_state(self) -> None:
        try:
            self._state_path().write_text(
                json.dumps({"recent": self.recent_articles}, ensure_ascii=False),
                encoding="utf-8",
            )
        except Exception:
            pass

    def breadcrumb(self, title: str) -> list[str]:
        """Gibt die Pfad-Teile vom Wurzelordner bis zum Artikel zurück."""
        if title not in self.all_articles:
            return [title]
        article = self.all_articles[title]
        try:
            rel = article["datei"].relative_to(self.folder)
        except ValueError:
            return [title]
        folders = [p.replace("_", " ").title() for p in rel.parts[:-1]]
        return folders + [title]

    def add_recent(self, title: str) -> None:
        self.recent_articles = [title] + [r for r in self.recent_articles if r != title]
        self.recent_articles = self.recent_articles[:5]

    def article_blocks(self, title: str) -> list[ArticleBlock]:
        """Liefert die typisierten Artikel-Bloecke inkl. Kopf-Block.

        Laedt den Artikeltext bei Bedarf nach (Lazy Load).

        Args:
            title: Artikeltitel.

        Returns:
            Liste mit ``ArticleHeaderBlock`` als erstem Element, gefolgt
            von den Inhalts-Bloecken des Artikeltexts.
        """
        if title not in self.all_articles:
            return [ParagraphBlock(
                html=(
                    f'<span style="color:#9ca3af;">Artikel '
                    f"<b>{title}</b> nicht gefunden.</span>"
                )
            )]
        article = self.all_articles[title]
        ensure_article_text(article)
        header = ArticleHeaderBlock(
            kategorie=article["kategorie"],
            symbol=article["meta"].get("symbol"),
            einheit=article["meta"].get("einheit"),
        )
        content = parse_article_blocks(article["text"], self.all_articles)
        return [header] + content

    def home_html(self) -> str:
        """Liefert das HTML fuer die Startseite mit Kategorien-Uebersicht."""
        categories: dict[str, list[str]] = {}
        for title, article in self.all_articles.items():
            categories.setdefault(article["kategorie"], []).append(title)
        html = '<div style="max-width:700px;">'
        html += (
            f'<h1 style="font-size:24px;font-weight:700;color:#111827;'
            f'margin-bottom:4px;">{self.title}</h1>'
        )
        html += (
            f'<p style="color:#6b7280;font-size:14px;margin-bottom:24px;">'
            f"{len(self.all_articles)} Begriffe in "
            f"{len(categories)} Kategorien</p>"
        )
        if self.recent_articles:
            html += (
                '<h2 style="font-size:14px;font-weight:600;color:#374151;'
                "text-transform:uppercase;letter-spacing:.05em;"
                "margin:20px 0 8px;border-bottom:1px solid #e5e7eb;"
                'padding-bottom:4px;">Zuletzt geöffnet</h2><div>'
            )
            for t in self.recent_articles:
                html += (
                    f'<a href="artikel://x/{quote(t, safe="")}" '
                    f'style="display:inline-block;background:#eff6ff;'
                    f"color:#1e40af;padding:4px 12px;border-radius:99px;"
                    f"font-size:13px;text-decoration:none;"
                    f'border:1px solid #bfdbfe;margin:2px;">{t}</a>'
                )
            html += "</div>"
        for category_name in sorted(categories):
            html += (
                f'<h2 style="font-size:14px;font-weight:600;color:#374151;'
                f"text-transform:uppercase;letter-spacing:.05em;"
                f"margin:20px 0 8px;border-bottom:1px solid #e5e7eb;"
                f'padding-bottom:4px;">{category_name}</h2><div>'
            )
            for title in sorted(categories[category_name]):
                html += (
                    f'<a href="artikel://x/{quote(title, safe="")}" '
                    f'style="display:inline-block;background:#f3f4f6;'
                    f"color:#1e3a5f;padding:4px 12px;border-radius:99px;"
                    f"font-size:13px;text-decoration:none;"
                    f'border:1px solid #e5e7eb;margin:2px;">{title}</a>'
                )
            html += "</div>"
        html += "</div>"
        return html

    def article_tags(self, title: str) -> list[str]:
        """Gibt die Tag-Liste des Artikels zurueck."""
        if title not in self.all_articles:
            return []
        return self.all_articles[title]["tags"]

    def article_links(self, title: str) -> list[tuple[str, str | None]]:
        """Extrahiert Wiki-Links aus dem Artikeltext.

        Returns:
            Liste von ``(Zieltext, gefundener_Artikeltitel_oder_None)``.
        """
        if title not in self.all_articles:
            return []
        article = self.all_articles[title]
        ensure_article_text(article)
        text = article["text"]
        raw_targets = re.findall(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", text)
        seen: set[str] = set()
        result: list[tuple[str, str | None]] = []
        for target in raw_targets:
            target = target.strip()
            if target in seen or target.lower() == title.lower():
                continue
            seen.add(target)
            found: str | None = next(
                (t for t in self.all_articles if t.lower() == target.lower()),
                None,
            )
            result.append((target, found))
        return result

    def article_formulas(self, title: str) -> list[str]:
        """Extrahiert Formeln ausschliesslich aus CodeBlock-Objekten des Artikels.

        Nur explizit als Formel-Block (:::formel ... :::) ausgezeichnete Zeilen
        werden uebernommen — kein Regex-Scan ueber den Rohtext, damit
        Aufzaehlungen, Pinout-Zeilen oder Kommentare nicht faelschlich
        als Formeln erscheinen.

        Returns:
            Deduplizierte Liste von Formel-Strings (mind. 3 Zeichen).
        """
        if title not in self.all_articles:
            return []
        article = self.all_articles[title]
        ensure_article_text(article)
        blocks = parse_article_blocks(article["text"], self.all_articles)
        seen: set[str] = set()
        result: list[str] = []
        for block in blocks:
            if isinstance(block, CodeBlock):
                for line in block.lines:
                    # Bedingung ("# ...") abstreifen — CAS bekommt nur die Formel
                    formula = line.partition("#")[0].strip()
                    if formula and formula not in seen and len(formula) >= 3:
                        seen.add(formula)
                        result.append(formula)
        return result


# ── GUI-Widgets ───────────────────────────────────────────────────────────────
class HamburgerButton(QPushButton):
    """Quadratischer Toggle-Knopf mit gezeichneten Hamburger-Balken.

    Wird eingesetzt, um die linke und rechte Seitenleiste ein- und
    auszublenden. Die Balken werden im ``paintEvent`` selbst gezeichnet,
    damit die Darstellung skaliert und unabhaengig vom Icon-Set ist.
    """

    def __init__(
        self,
        line_color: str = "white",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._line_color = line_color
        self.setFixedSize(32, 32)
        self.setCursor(Qt.CursorShape.PointingHandCursor)

    def paintEvent(self, event: QPaintEvent) -> None:  # noqa: D401 - Qt-Callback
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(QColor(self._line_color))
        painter.setBrush(QColor(self._line_color))
        width, height = self.width(), self.height()
        x = (width - 16) // 2
        for dy in (-5, 0, 5):
            painter.drawRoundedRect(x, height // 2 + dy - 1, 16, 2, 1, 1)
        painter.end()


class WaveformWidget(QWidget):
    """Zeichnet digitale und analoge Signalspuren im Oszilloskop-Stil.

    Digitale Spuren (values: list[0|1]) werden als Rechteck-Waveform
    dargestellt; analoge Spuren (analog=True) als Liniengraph.
    """

    _BG = QColor("#1a1a2e")
    _TRACK_BG = QColor("#16213e")
    _GRID = QColor("#2d2d4e")
    _LABEL_COLOR = QColor("#94a3b8")
    _DIGITAL_COLOR = QColor("#34d399")
    _ANALOG_COLOR = QColor("#60a5fa")

    _LABEL_W = 72
    _TRACK_H = 46
    _BOTTOM_H = 20
    _TOP_PAD = 6

    def __init__(
        self, block: WaveformBlock, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self._block = block
        n = len(block.signals)
        total_h = self._TOP_PAD + n * self._TRACK_H + self._BOTTOM_H
        self.setFixedHeight(total_h)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed
        )
        self.setMinimumWidth(200)

    def paintEvent(self, event: QPaintEvent) -> None:  # noqa: N802
        signals = self._block.signals
        if not signals:
            return
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        W = self.width()
        plot_w = W - self._LABEL_W - 8
        n_samples = max((len(s["values"]) for s in signals), default=0)
        if n_samples == 0:
            p.end()
            return
        sample_w = plot_w / n_samples

        p.fillRect(0, 0, W, self.height(), self._BG)

        for si, sig in enumerate(signals):
            y0 = self._TOP_PAD + si * self._TRACK_H
            y1 = y0 + self._TRACK_H - 2

            p.fillRect(self._LABEL_W, y0, plot_w, self._TRACK_H - 2, self._TRACK_BG)

            grid_pen = QPen(self._GRID)
            grid_pen.setWidth(1)
            p.setPen(grid_pen)
            for gi in range(n_samples + 1):
                gx = self._LABEL_W + int(gi * sample_w)
                p.drawLine(gx, y0, gx, y1)

            p.setPen(QPen(self._LABEL_COLOR))
            f: QFont = p.font()
            f.setPixelSize(11)
            p.setFont(f)
            p.drawText(
                2, y0, self._LABEL_W - 4, self._TRACK_H - 2,
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight,
                sig["name"],
            )

            values = sig["values"]
            is_analog = sig.get("analog", False)
            sig_pen = QPen(self._ANALOG_COLOR if is_analog else self._DIGITAL_COLOR)
            sig_pen.setWidth(2)
            p.setPen(sig_pen)

            if is_analog:
                min_v: float = sig.get("min", 0.0)
                max_v: float = sig.get("max", 1.0)
                span = (max_v - min_v) or 1.0
                pts: list[tuple[int, int]] = []
                for idx, v in enumerate(values):
                    x = self._LABEL_W + int((idx + 0.5) * sample_w)
                    norm = 1.0 - (v - min_v) / span
                    y = y0 + 3 + int(norm * (self._TRACK_H - 8))
                    pts.append((x, y))
                for idx in range(len(pts) - 1):
                    p.drawLine(pts[idx][0], pts[idx][1], pts[idx + 1][0], pts[idx + 1][1])
            else:
                y_hi = y0 + 5
                y_lo = y1 - 5
                trap_w = max(3, int(sample_w * 0.12))
                x_cur = self._LABEL_W
                for idx, v in enumerate(values):
                    x_next = self._LABEL_W + int((idx + 1) * sample_w)
                    y_cur = y_hi if v else y_lo
                    if idx > 0 and values[idx] != values[idx - 1]:
                        y_prev = y_hi if values[idx - 1] else y_lo
                        p.drawLine(x_cur, y_prev, x_cur + trap_w, y_cur)
                        p.drawLine(x_cur + trap_w, y_cur, x_next, y_cur)
                    else:
                        p.drawLine(x_cur, y_cur, x_next, y_cur)
                    x_cur = x_next

        if self._block.sample_labels:
            p.setPen(QPen(self._LABEL_COLOR))
            f2: QFont = p.font()
            f2.setPixelSize(9)
            p.setFont(f2)
            y_lbl = self._TOP_PAD + len(signals) * self._TRACK_H
            for idx, lbl in enumerate(self._block.sample_labels[:n_samples]):
                x = self._LABEL_W + int(idx * sample_w)
                p.drawText(
                    x, y_lbl, int(sample_w), self._BOTTOM_H - 2,
                    Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop,
                    lbl,
                )
        p.end()


class PlotWidget(QWidget):
    """Zeichnet einen mathematischen Funktionsgraphen mit Achsen und Legende."""

    _COLORS = [
        QColor("#0284c7"), QColor("#dc2626"), QColor("#16a34a"),
        QColor("#d97706"), QColor("#7c3aed"),
    ]
    _BG        = QColor("#ffffff")
    _GRID      = QColor("#e2e8f0")
    _AXIS      = QColor("#475569")
    _LABEL_CLR = QColor("#374151")

    _PAD_L  = 58
    _PAD_R  = 20
    _PAD_T  = 18
    _PAD_B  = 46
    _N      = 300   # Stützpunkte pro Kurve

    def __init__(self, block: PlotBlock, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._block = block
        self._curves_pts: list[list[tuple[float, float]]] = []
        self._sample()
        self.setFixedHeight(240)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

    def _sample(self) -> None:
        b = self._block
        x0, x1 = b.x_range
        span = (x1 - x0) or 1.0
        ns = {**_PLOT_NS, "__builtins__": {}}
        for curve in b.curves:
            pts: list[tuple[float, float]] = []
            for i in range(self._N):
                xv = x0 + (i / (self._N - 1)) * span
                try:
                    ns[b.var] = xv
                    yv = float(eval(curve["expr"], ns))  # noqa: S307
                    pts.append((xv, yv))
                except Exception:
                    pass
            self._curves_pts.append(pts)

    def paintEvent(self, event: QPaintEvent) -> None:  # noqa: N802
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing)
        w = self.width()
        h = self.height()
        plot_w = w - self._PAD_L - self._PAD_R
        plot_h = h - self._PAD_T - self._PAD_B
        x0_px = self._PAD_L
        y0_px = self._PAD_T

        # Hintergrund
        p.fillRect(0, 0, w, h, self._BG)

        # Y-Bereich aus allen Kurven ermitteln
        all_y = [yv for pts in self._curves_pts for _, yv in pts]
        if not all_y:
            p.end()
            return
        y_min, y_max = min(all_y), max(all_y)
        y_span = (y_max - y_min) or 1.0
        y_min -= y_span * 0.08
        y_max += y_span * 0.08
        y_span = y_max - y_min

        x0, x1 = self._block.x_range
        x_span = (x1 - x0) or 1.0

        def to_px(xv: float, yv: float) -> tuple[int, int]:
            px = x0_px + int((xv - x0) / x_span * plot_w)
            py = y0_px + int((1.0 - (yv - y_min) / y_span) * plot_h)
            return px, py

        # Grid
        grid_pen = QPen(self._GRID)
        grid_pen.setWidth(1)
        p.setPen(grid_pen)
        for i in range(6):
            gx = x0_px + int(i / 5 * plot_w)
            p.drawLine(gx, y0_px, gx, y0_px + plot_h)
            gy = y0_px + int(i / 5 * plot_h)
            p.drawLine(x0_px, gy, x0_px + plot_w, gy)

        # Achsen
        axis_pen = QPen(self._AXIS)
        axis_pen.setWidth(2)
        p.setPen(axis_pen)
        p.drawLine(x0_px, y0_px, x0_px, y0_px + plot_h)
        p.drawLine(x0_px, y0_px + plot_h, x0_px + plot_w, y0_px + plot_h)

        # Achsenbeschriftungen
        f = p.font()
        f.setPixelSize(11)
        p.setFont(f)
        p.setPen(QPen(self._LABEL_CLR))

        for i in range(6):
            xv = x0 + i / 5 * x_span
            gx = x0_px + int(i / 5 * plot_w)
            p.drawText(gx - 20, y0_px + plot_h + 4, 40, 16,
                       Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop,
                       f"{xv:.2g}")
            yv = y_min + (1 - i / 5) * y_span
            gy = y0_px + int(i / 5 * plot_h)
            p.drawText(0, gy - 8, self._PAD_L - 6, 16,
                       Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignRight,
                       f"{yv:.2g}")

        if self._block.xlabel:
            fb = p.font()
            fb.setPixelSize(12)
            p.setFont(fb)
            p.drawText(x0_px, y0_px + plot_h + 22, plot_w, 18,
                       Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop,
                       self._block.xlabel)
        if self._block.ylabel:
            p.save()
            p.translate(12, y0_px + plot_h // 2)
            p.rotate(-90)
            fb2 = p.font()
            fb2.setPixelSize(12)
            p.setFont(fb2)
            p.drawText(-60, -8, 120, 16,
                       Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter,
                       self._block.ylabel)
            p.restore()

        # Kurven zeichnen
        for ci, pts in enumerate(self._curves_pts):
            if len(pts) < 2:
                continue
            color = self._COLORS[ci % len(self._COLORS)]
            pen = QPen(color)
            pen.setWidth(2)
            p.setPen(pen)
            prev = to_px(*pts[0])
            for xv, yv in pts[1:]:
                cur = to_px(xv, yv)
                p.drawLine(prev[0], prev[1], cur[0], cur[1])
                prev = cur

        # Legende
        if len(self._block.curves) > 1:
            lx = x0_px + plot_w - 10
            ly = y0_px + 8
            for ci, curve in enumerate(self._block.curves):
                color = self._COLORS[ci % len(self._COLORS)]
                pen = QPen(color)
                pen.setWidth(2)
                p.setPen(pen)
                p.drawLine(lx - 80, ly + 7, lx - 64, ly + 7)
                p.setPen(QPen(self._LABEL_CLR))
                fl = p.font()
                fl.setPixelSize(11)
                p.setFont(fl)
                p.drawText(lx - 60, ly, 60, 16,
                           Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft,
                           curve["label"])
                ly += 18

        p.end()


class FormulaBlockWidget(QFrame):
    """Zeigt eine Formelzeile als 2D-Darstellung mit CAS-Schaltflaeche.

    Layout (QHBoxLayout): ``MathFormulaDisplay`` (Stretch=1) links,
    QPushButton '-> CAS' (Fixbreite) rechts.

    Abkuerzungen (Initialnotation):
        CAS - Computer Algebra System.
    """

    def __init__(
        self,
        formula: str,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)

        # Formel und optionale Bedingung trennen: "U = R*I  # Gleichstrom"
        if "#" in formula:
            formula_part, _, condition = formula.partition("#")
            formula_part = formula_part.strip()
            condition = condition.strip()
        else:
            formula_part = formula.strip()
            condition = ""

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        row = QWidget()
        layout = QHBoxLayout(row)
        layout.setContentsMargins(10, 6, 6, 6)
        layout.setSpacing(8)

        display = MathFormulaDisplay(formula_part)
        layout.addWidget(display, stretch=1)

        copy_btn = QPushButton("⎘")
        copy_btn.setFixedWidth(28)
        copy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        copy_btn.setToolTip("In Zwischenablage kopieren")
        copy_btn.clicked.connect(
            lambda: QApplication.clipboard().setText(formula_part)
        )
        layout.addWidget(copy_btn)
        outer.addWidget(row)

        if condition:
            cond_label = QLabel(f"  ↳ {condition}")
            cond_label.setStyleSheet(
                "color:#6b7280;font-size:11px;padding:0 10px 4px 10px;"
                "font-style:italic;"
            )
            outer.addWidget(cond_label)


class ArticleContentWidget(QScrollArea):
    """Scrollbarer Artikel-Anzeigebereich auf Basis von PySide6-Layouts.

    Rendert typisierte Artikel-Bloecke: Ueberschriften, Absaetze,
    2D-Formel-Bloecke mit CAS-Schaltflaeche, Aufzaehlungen sowie
    Raster- (PNG/JPG) und Vektor-Bilder (SVG). Fuer die Startseite
    steht ``render_html`` mit eingebettetem QTextBrowser bereit.

    Abkuerzungen (Initialnotation):
        CAS - Computer Algebra System.
        SVG - Scalable Vector Graphics.
    """

    def __init__(
        self,
        on_link_clicked: Callable[[QUrl], None],
        on_send_formula: Callable[[str], None],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._on_link_clicked: Callable[[QUrl], None] = on_link_clicked
        self._on_send_formula: Callable[[str], None] = on_send_formula
        self.setWidgetResizable(True)
        self.setFrameShape(QFrame.Shape.NoFrame)
        self._content: QWidget = QWidget()
        self._content.setObjectName("articleContent")
        self._body: QVBoxLayout = QVBoxLayout(self._content)
        self._body.setContentsMargins(40, 32, 40, 32)
        self._body.setSpacing(4)
        self.setWidget(self._content)

    # ── Oeffentliche API ──────────────────────────────────────────────────────

    def render_blocks(
        self,
        blocks: list[ArticleBlock],
        article_folder: Path,
    ) -> None:
        """Loescht bestehenden Inhalt und rendert typisierte Bloecke."""
        self._clear()
        for block in blocks:
            widget = self._block_to_widget(block, article_folder)
            if widget is not None:
                self._body.addWidget(widget)
        self._body.addStretch()

    def render_html(self, html: str) -> None:
        """Rendert reines HTML in einem eingebetteten QTextBrowser.

        Wird fuer die Startseite und Fehlermeldungen verwendet.
        """
        self._clear()
        browser = QTextBrowser()
        browser.setObjectName("articleBrowser")
        browser.setOpenLinks(False)
        browser.anchorClicked.connect(self._on_link_clicked)
        browser.setHtml(html)
        self._body.addWidget(browser)

    # ── Interne Helfer ─────────────────────────────────────────────────────────

    def _clear(self) -> None:
        while self._body.count():
            child = self._body.takeAt(0)
            if child and child.widget():
                child.widget().deleteLater()

    def _block_to_widget(
        self,
        block: ArticleBlock,
        article_folder: Path,
    ) -> QWidget | None:
        if isinstance(block, ArticleHeaderBlock):
            return self._make_header(block)
        if isinstance(block, HeadingBlock):
            return self._make_heading(block)
        if isinstance(block, ParagraphBlock):
            return self._make_paragraph(block)
        if isinstance(block, CodeBlock):
            return self._make_code_section(block)
        if isinstance(block, MonospaceBlock):
            return self._make_monospace_section(block)
        if isinstance(block, ListBlock):
            return self._make_list(block)
        if isinstance(block, TableBlock):
            return self._make_table(block)
        if isinstance(block, ImageBlock):
            return self._make_image(block, article_folder)
        if isinstance(block, SchematicBlock):
            return self._make_schematic(block, article_folder)
        if isinstance(block, WaveformBlock):
            return self._make_waveform(block)
        if isinstance(block, PlotBlock):
            return self._make_plot(block)
        if isinstance(block, PinoutBlock):
            return self._make_pinout(block)
        if isinstance(block, TruthTableBlock):
            return self._make_truth_table(block)
        if isinstance(block, NoteBlock):
            return self._make_note(block)
        if isinstance(block, HBoxBlock):
            return self._make_hbox(block, article_folder)
        if isinstance(block, VBoxBlock):
            return self._make_vbox(block, article_folder)
        return None

    def _make_header(self, block: ArticleHeaderBlock) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 8)
        layout.setSpacing(4)
        cat_label = QLabel(block.kategorie.upper())
        cat_label.setObjectName("categoryLabel")
        layout.addWidget(cat_label)
        if block.symbol or block.einheit:
            badges = QWidget()
            b_layout = QHBoxLayout(badges)
            b_layout.setContentsMargins(0, 0, 0, 0)
            b_layout.setSpacing(6)
            if block.symbol:
                sym = QLabel(block.symbol)
                sym.setObjectName("symbolBadge")
                b_layout.addWidget(sym)
            if block.einheit:
                ein = QLabel(block.einheit)
                ein.setObjectName("einheitBadge")
                b_layout.addWidget(ein)
            b_layout.addStretch()
            layout.addWidget(badges)
        return container

    def _make_heading(self, block: HeadingBlock) -> QLabel:
        label = QLabel(block.text)
        label.setWordWrap(True)
        _styles: dict[int, tuple[str, str, str, str, str]] = {
            1: ("22px", "700", "0 0 4px", "#111827", ""),
            2: (
                "17px", "600", "20px 0 8px", "#111827",
                "border-bottom:1px solid #e5e7eb;padding-bottom:4px;",
            ),
            3: ("15px", "600", "16px 0 6px", "#374151", ""),
        }
        size, weight, margin, color, extra = _styles.get(
            block.level, _styles[3]
        )
        label.setStyleSheet(
            f"font-size:{size};font-weight:{weight};margin:{margin};"
            f"color:{color};{extra}"
        )
        return label

    def _make_paragraph(self, block: ParagraphBlock) -> QLabel:
        label = QLabel()
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setWordWrap(True)
        label.setOpenExternalLinks(False)
        label.setText(
            f'<span style="color:#374151;font-size:15px;line-height:1.7;">'
            f"{block.html}</span>"
        )
        label.linkActivated.connect(
            lambda href: self._on_link_clicked(QUrl(href))
        )
        return label

    def _make_code_section(self, block: CodeBlock) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 4, 0, 4)
        layout.setSpacing(4)
        for formula in block.lines:
            layout.addWidget(FormulaBlockWidget(formula))
        return container

    def _make_monospace_section(self, block: MonospaceBlock) -> QWidget:
        container = QFrame()
        container.setObjectName("monoBlock")
        container.setStyleSheet(
            "QFrame#monoBlock{background:#f8f9fa;border:1px solid #e5e7eb;"
            "border-radius:6px;}"
        )
        layout = QVBoxLayout(container)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(0)
        label = QLabel("\n".join(block.lines))
        label.setTextFormat(Qt.TextFormat.PlainText)
        label.setStyleSheet(
            "font-family:'Courier New',Consolas,monospace;font-size:13px;"
            "color:#1f2937;background:transparent;line-height:1.5;"
        )
        label.setWordWrap(False)
        label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
        )
        layout.addWidget(label)
        return container

    def _make_list(self, block: ListBlock) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(20, 4, 0, 4)
        layout.setSpacing(2)
        for item_html in block.items:
            label = QLabel()
            label.setTextFormat(Qt.TextFormat.RichText)
            label.setWordWrap(True)
            label.setOpenExternalLinks(False)
            label.setText(
                f'<span style="color:#374151;font-size:15px;">'
                f"• {item_html}</span>"
            )
            label.linkActivated.connect(
                lambda href: self._on_link_clicked(QUrl(href))
            )
            layout.addWidget(label)
        return container

    def _make_table(self, block: TableBlock) -> QWidget:
        """Rendert eine Markdown-Tabelle als QGridLayout mit Rahmen.

        Zellinhalte werden als RichText dargestellt; Wiki-Links und
        Inline-Code in Zellen bleiben klickbar bzw. formatiert.
        """
        container = QFrame()
        container.setObjectName("tableBlock")
        container.setFrameShape(QFrame.Shape.NoFrame)
        container.setStyleSheet(
            "QFrame#tableBlock{background:#ffffff;border:1px solid #e5e7eb;"
            "border-radius:6px;}"
            "QLabel[tableCell=\"head\"]{background:#f9fafb;color:#111827;"
            "font-weight:600;font-size:13px;padding:6px 10px;"
            "border-bottom:1px solid #e5e7eb;}"
            "QLabel[tableCell=\"body\"]{color:#374151;font-size:13px;"
            "padding:6px 10px;border-top:1px solid #f1f5f9;}"
        )
        outer = QVBoxLayout(container)
        outer.setContentsMargins(0, 8, 0, 8)
        outer.setSpacing(0)

        grid_host = QWidget()
        grid = QGridLayout(grid_host)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)

        def make_cell(html: str, role: str) -> QLabel:
            label = QLabel()
            label.setTextFormat(Qt.TextFormat.RichText)
            label.setWordWrap(True)
            label.setOpenExternalLinks(False)
            label.setProperty("tableCell", role)
            label.setSizePolicy(
                QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred
            )
            label.setText(html)
            label.linkActivated.connect(
                lambda href: self._on_link_clicked(QUrl(href))
            )
            return label

        for col, head in enumerate(block.headers):
            grid.addWidget(make_cell(head, "head"), 0, col)
        for r, row in enumerate(block.rows, start=1):
            for col in range(len(block.headers)):
                cell = row[col] if col < len(row) else ""
                grid.addWidget(make_cell(cell, "body"), r, col)
        # Spalten gleichmaessig verteilen.
        for col in range(len(block.headers)):
            grid.setColumnStretch(col, 1)

        outer.addWidget(grid_host)
        return container

    def _make_image(self, block: ImageBlock, article_folder: Path) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(4)
        p = block.path.strip()
        img_path = (ARTICLES_FOLDER / p.lstrip("/")) if p.startswith("/") else (article_folder / p)

        if not img_path.exists():
            err = QLabel(f"[Bild nicht gefunden: {block.path}]")
            err.setObjectName("imageError")
            layout.addWidget(err)
            return container

        suffix = img_path.suffix.lower()
        img_widget: QWidget

        if suffix == ".svg":
            svg = QSvgWidget(str(img_path))
            renderer: QSvgRenderer = svg.renderer()
            if renderer.isValid():
                ds = renderer.defaultSize()
                src_w = ds.width() if ds.width() > 0 else 600
                src_h = ds.height() if ds.height() > 0 else 400
                w = min(src_w, 600)
                h = max(int(src_h * w / src_w), 20)
                svg.setFixedSize(w, h)
            img_widget = svg
        elif suffix in _RASTER_SUFFIXES:
            pixmap = QPixmap(str(img_path))
            if pixmap.isNull():
                err = QLabel(f"[Bild nicht lesbar: {block.path}]")
                err.setObjectName("imageError")
                layout.addWidget(err)
                return container
            if pixmap.width() > 600:
                pixmap = pixmap.scaledToWidth(
                    600, Qt.TransformationMode.SmoothTransformation
                )
            pix_label = QLabel()
            pix_label.setPixmap(pixmap)
            img_widget = pix_label
        else:
            err = QLabel(f"[Bildformat nicht unterstuetzt: {block.path}]")
            err.setObjectName("imageError")
            layout.addWidget(err)
            return container

        layout.addWidget(img_widget)
        if block.alt:
            alt_label = QLabel(block.alt)
            alt_label.setObjectName("imageAlt")
            alt_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(alt_label)
        return container

    def _make_schematic(
        self, block: SchematicBlock, article_folder: Path
    ) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(6)

        if block.title:
            title_lbl = QLabel(block.title)
            title_lbl.setStyleSheet(
                "color:#374151;font-size:13px;font-weight:600;"
            )
            layout.addWidget(title_lbl)

        sp = block.path.strip()
        img_path = (ARTICLES_FOLDER / sp.lstrip("/")) if sp.startswith("/") else (article_folder / sp)
        if not img_path.exists():
            err = QLabel(f"[Schaltplan nicht gefunden: {block.path}]")
            err.setObjectName("imageError")
            layout.addWidget(err)
            return container

        suffix = img_path.suffix.lower()
        if suffix == ".svg":
            svg = QSvgWidget(str(img_path))
            renderer: QSvgRenderer = svg.renderer()
            if renderer.isValid():
                ds = renderer.defaultSize()
                src_w = ds.width() if ds.width() > 0 else 700
                src_h = ds.height() if ds.height() > 0 else 500
                w = min(src_w, 700)
                h = max(int(src_h * w / src_w), 20)
                svg.setFixedSize(w, h)
            layout.addWidget(svg)
        elif suffix in _RASTER_SUFFIXES:
            pixmap = QPixmap(str(img_path))
            if pixmap.isNull():
                err = QLabel(f"[Bild nicht lesbar: {block.path}]")
                err.setObjectName("imageError")
                layout.addWidget(err)
            else:
                if pixmap.width() > 700:
                    pixmap = pixmap.scaledToWidth(
                        700, Qt.TransformationMode.SmoothTransformation
                    )
                pix_lbl = QLabel()
                pix_lbl.setPixmap(pixmap)
                layout.addWidget(pix_lbl)
        else:
            err = QLabel(f"[Format nicht unterstützt: {block.path}]")
            err.setObjectName("imageError")
            layout.addWidget(err)
        return container

    def _make_waveform(self, block: WaveformBlock) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(0)
        layout.addWidget(WaveformWidget(block))
        return container

    def _make_plot(self, block: PlotBlock) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 8, 0, 8)
        layout.setSpacing(0)
        layout.addWidget(PlotWidget(block))
        return container

    def _make_pinout(self, block: PinoutBlock) -> QWidget:
        container = QFrame()
        container.setStyleSheet(
            "QFrame{background:#f8fafc;border:1px solid #e2e8f0;"
            "border-radius:8px;}"
        )
        outer = QVBoxLayout(container)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        header_text = block.component
        if block.package:
            header_text += f"  ·  {block.package}"
        header_lbl = QLabel(f"  {header_text}")
        header_lbl.setStyleSheet(
            "background:#1e293b;color:#f1f5f9;font-weight:700;"
            "font-size:13px;padding:7px 12px;"
            "border-radius:7px 7px 0 0;border:none;"
        )
        outer.addWidget(header_lbl)

        grid_host = QWidget()
        grid_host.setStyleSheet("background:transparent;")
        grid = QGridLayout(grid_host)
        grid.setContentsMargins(10, 8, 10, 8)
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(3)

        for row, pin in enumerate(sorted(block.pins, key=lambda p: p["nr"])):
            nr_lbl = QLabel(str(pin["nr"]))
            nr_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            nr_lbl.setFixedSize(26, 26)
            nr_lbl.setStyleSheet(
                "background:#3b82f6;color:#fff;font-weight:700;"
                "font-size:11px;border-radius:13px;border:none;"
            )
            grid.addWidget(nr_lbl, row, 0)

            name_lbl = QLabel(pin["name"])
            name_lbl.setStyleSheet(
                "color:#0f172a;font-weight:600;font-size:13px;border:none;"
            )
            grid.addWidget(name_lbl, row, 1)

            if pin.get("info"):
                info_lbl = QLabel(pin["info"])
                info_lbl.setStyleSheet(
                    "color:#64748b;font-size:12px;border:none;"
                )
                grid.addWidget(info_lbl, row, 2)

        grid.setColumnStretch(2, 1)
        outer.addWidget(grid_host)
        return container

    def _make_truth_table(self, block: TruthTableBlock) -> QWidget:
        container = QFrame()
        container.setObjectName("truthTableBlock")
        container.setStyleSheet(
            "QFrame#truthTableBlock{background:#fff;border:1px solid #e5e7eb;"
            "border-radius:6px;}"
        )
        outer = QVBoxLayout(container)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        grid_host = QWidget()
        grid = QGridLayout(grid_host)
        grid.setContentsMargins(0, 0, 0, 0)
        grid.setHorizontalSpacing(0)
        grid.setVerticalSpacing(0)

        all_headers = block.inputs + block.outputs
        n_in = len(block.inputs)

        for col, name in enumerate(all_headers):
            is_in = col < n_in
            lbl = QLabel(name)
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            lbl.setStyleSheet(
                f"background:{'#e0f2fe' if is_in else '#dcfce7'};"
                f"color:{'#0369a1' if is_in else '#166534'};"
                "font-weight:700;font-size:13px;"
                "padding:6px 14px;border-bottom:2px solid #e5e7eb;"
            )
            grid.addWidget(lbl, 0, col)

        for r, row_vals in enumerate(block.rows):
            for col in range(len(all_headers)):
                v = row_vals[col] if col < len(row_vals) else 0
                is_in = col < n_in
                stripe = "#f9fafb" if r % 2 == 0 else "#fff"
                if v == 1 and not is_in:
                    bg, fg = "#bbf7d0", "#166534"
                else:
                    bg, fg = stripe, ("#374151" if v else "#9ca3af")
                cell = QLabel("1" if v else "0")
                cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
                cell.setStyleSheet(
                    f"background:{bg};color:{fg};"
                    "font-size:13px;font-family:monospace;"
                    "padding:5px 14px;border-top:1px solid #f1f5f9;"
                )
                grid.addWidget(cell, r + 1, col)

        for col in range(len(all_headers)):
            grid.setColumnStretch(col, 1)

        outer.addWidget(grid_host)
        return container

    def _make_note(self, block: NoteBlock) -> QWidget:
        _styles: dict[str, tuple[str, str, str]] = {
            "info":    ("#dbeafe", "#1d4ed8", "ℹ"),
            "tip":     ("#dcfce7", "#16a34a", "✓"),
            "warning": ("#fef3c7", "#b45309", "⚠"),
            "danger":  ("#fee2e2", "#dc2626", "⛔"),
            "norm":    ("#f5f3ff", "#7c3aed", "§"),
            "merke":   ("#fff7ed", "#c2410c", "★"),
        }
        bg, border, icon = _styles.get(block.kind, _styles["info"])

        container = QFrame()
        container.setStyleSheet(
            f"QFrame{{background:{bg};border-left:4px solid {border};"
            "border-top-left-radius:0px;border-top-right-radius:6px;"
            "border-bottom-right-radius:6px;border-bottom-left-radius:0px;"
            "border-top:none;border-right:none;border-bottom:none;}}"
        )
        layout = QHBoxLayout(container)
        layout.setContentsMargins(12, 10, 14, 10)
        layout.setSpacing(10)

        icon_lbl = QLabel(icon)
        icon_lbl.setStyleSheet(
            f"color:{border};font-size:16px;"
            "background:transparent;border:none;"
        )
        icon_lbl.setFixedWidth(22)
        layout.addWidget(icon_lbl)

        text_lbl = QLabel(block.text)
        text_lbl.setWordWrap(True)
        text_lbl.setStyleSheet(
            "color:#1e293b;font-size:14px;"
            "background:transparent;border:none;"
        )
        layout.addWidget(text_lbl, stretch=1)
        return container

    def _make_hbox(self, block: HBoxBlock, article_folder: Path) -> QWidget:
        container = QWidget()
        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 4, 0, 4)
        layout.setSpacing(12)
        for child in block.children:
            w = self._block_to_widget(child, article_folder)
            if w is not None:
                layout.addWidget(w, stretch=1)
        return container

    def _make_vbox(self, block: VBoxBlock, article_folder: Path) -> QWidget:
        container = QWidget()
        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 4, 0, 4)
        layout.setSpacing(4)
        for child in block.children:
            w = self._block_to_widget(child, article_folder)
            if w is not None:
                layout.addWidget(w)
        return container


# ── Lexikon-Tool-Widget ───────────────────────────────────────────────────────
class LexiconWidget(QWidget):
    """Komplettes Lexikon-Tool als einzelnes QWidget.

    Dreispaltige Ansicht: linke Artikelliste, zentraler Anzeigebereich,
    rechte Spalte mit Tags/Verlinkungen/Formeln. Eigene Toolbar mit
    Zurueck-Knopf - das Widget ist vollstaendig eigenstaendig und
    kennt die App-Shell nicht.

    Fuer den CAS-Wechsel wird eine Callback-Funktion uebergeben, die
    eine Formel an den CAS-Rechner delegiert und dort hin umschaltet.
    """

    def __init__(
        self,
        on_send_formula: Callable[[str], None] | None = None,
        folder: Path = ARTICLES_FOLDER,
        title: str = "Elektronik Lexikon",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.view_model: LexiconViewModel = LexiconViewModel(
            folder=folder, title=title
        )
        self._on_send_formula_external = on_send_formula
        self._build_ui()
        self._refresh_list()
        self._show_home()

    def reload(self) -> None:
        """Laedt Artikel neu und zeigt die Startseite an.

        Wird z. B. nach externen Dateiaenderungen oder beim erneuten
        Oeffnen eines Hilfe-Panels gebraucht.
        """
        self.view_model = LexiconViewModel(
            folder=self.view_model.folder, title=self.view_model.title
        )
        self._refresh_list()
        self._show_home()

    # ── Aufbau ────────────────────────────────────────────────────────────────
    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Mini-Toolbar mit Zurueck-Knopf (rechtsbuendig).
        toolbar = QWidget()
        toolbar.setObjectName("lexiconToolbar")
        toolbar.setFixedHeight(36)
        tb_layout = QHBoxLayout(toolbar)
        tb_layout.setContentsMargins(8, 4, 8, 4)
        tb_layout.setSpacing(8)
        self.breadcrumb_label = QLabel()
        self.breadcrumb_label.setObjectName("breadcrumbLabel")
        tb_layout.addWidget(self.breadcrumb_label)
        tb_layout.addStretch()
        self.back_button = QPushButton("<- Zurueck")
        self.back_button.setObjectName("backButton")
        self.back_button.setEnabled(False)
        self.back_button.clicked.connect(self._go_back)
        tb_layout.addWidget(self.back_button)
        root.addWidget(toolbar)

        # Dreispaltige Hauptflaeche.
        body = QWidget()
        body_layout = QHBoxLayout(body)
        body_layout.setContentsMargins(0, 0, 0, 0)
        body_layout.setSpacing(0)

        # Linke Seitenleiste mit Suchfeld und Artikelliste.
        self._left_open = True
        self.left_sidebar = QWidget()
        self.left_sidebar.setObjectName("leftSidebar")
        self.left_sidebar.setMinimumWidth(0)
        self.left_sidebar.setMaximumWidth(220)
        left_layout = QVBoxLayout(self.left_sidebar)
        left_layout.setContentsMargins(10, 12, 10, 6)
        left_layout.setSpacing(8)

        self.left_content = QWidget()
        left_content_layout = QVBoxLayout(self.left_content)
        left_content_layout.setContentsMargins(0, 0, 0, 0)
        left_content_layout.setSpacing(8)
        self.search = QLineEdit()
        self.search.setObjectName("searchField")
        self.search.setPlaceholderText("Begriff suchen...")
        self.search.textChanged.connect(self._refresh_list)
        left_content_layout.addWidget(self.search)
        self.article_tree = QTreeWidget()
        self.article_tree.setObjectName("articleTree")
        self.article_tree.setHeaderHidden(True)
        self.article_tree.setIndentation(14)
        self.article_tree.setAnimated(True)
        self.article_tree.setExpandsOnDoubleClick(False)
        self.article_tree.setHorizontalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAlwaysOff
        )
        self.article_tree.setVerticalScrollBarPolicy(
            Qt.ScrollBarPolicy.ScrollBarAsNeeded
        )
        self.article_tree.itemClicked.connect(self._on_tree_item_clicked)
        left_content_layout.addWidget(self.article_tree)
        self.count_label = QLabel()
        self.count_label.setObjectName("countLabel")
        left_content_layout.addWidget(self.count_label)
        left_layout.addWidget(self.left_content, stretch=1)

        self.hamburger_left_inner = HamburgerButton(line_color="#374151")
        self.hamburger_left_inner.setObjectName("sidebarCloseBtn")
        self.hamburger_left_inner.setToolTip("Artikelliste ausblenden")
        self.hamburger_left_inner.clicked.connect(lambda: self._toggle_left())
        left_bottom = QHBoxLayout()
        left_bottom.setContentsMargins(0, 0, 0, 0)
        left_bottom.addWidget(self.hamburger_left_inner)
        left_bottom.addStretch()
        left_layout.addLayout(left_bottom)
        body_layout.addWidget(self.left_sidebar)

        self.left_anim = QPropertyAnimation(self.left_sidebar, b"maximumWidth")
        self.left_anim.setDuration(260)
        self.left_anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.left_anim.finished.connect(self._on_left_anim_done)

        # Artikel-Anzeige (zentrale Spalte).
        self.display = ArticleContentWidget(
            on_link_clicked=self._on_link_clicked,
            on_send_formula=self._send_formula_to_calculator,
        )
        body_layout.addWidget(self.display, stretch=1)

        # Rechte Seitenleiste: Tags, Verlinkungen, Formeln.
        self._right_open = True
        self.right_sidebar = QWidget()
        self.right_sidebar.setObjectName("rightSidebar")
        self.right_sidebar.setMinimumWidth(0)
        self.right_sidebar.setMaximumWidth(175)
        right_layout = QVBoxLayout(self.right_sidebar)
        right_layout.setContentsMargins(12, 16, 12, 6)
        right_layout.setSpacing(4)

        def make_section_label(text: str) -> QLabel:
            label = QLabel(text)
            label.setObjectName("sectionLabel")
            return label

        def make_divider() -> QFrame:
            frame = QFrame()
            frame.setObjectName("divider")
            frame.setFrameShape(QFrame.Shape.HLine)
            return frame

        self.right_content = QWidget()
        right_content_layout = QVBoxLayout(self.right_content)
        right_content_layout.setContentsMargins(0, 0, 0, 0)
        right_content_layout.setSpacing(4)

        right_content_layout.addWidget(make_section_label("TAGS"))
        self.tags_container = QWidget()
        self.tags_layout = QVBoxLayout(self.tags_container)
        self.tags_layout.setContentsMargins(0, 2, 0, 0)
        self.tags_layout.setSpacing(4)
        right_content_layout.addWidget(self.tags_container)

        right_content_layout.addWidget(make_divider())
        right_content_layout.addWidget(make_section_label("VERLINKUNGEN"))
        self.links_container = QWidget()
        self.links_layout = QVBoxLayout(self.links_container)
        self.links_layout.setContentsMargins(0, 2, 0, 0)
        self.links_layout.setSpacing(2)
        right_content_layout.addWidget(self.links_container)

        right_content_layout.addWidget(make_divider())
        right_content_layout.addWidget(make_section_label("FORMELN -> CAS"))
        self.formulas_container = QWidget()
        self.formulas_layout = QVBoxLayout(self.formulas_container)
        self.formulas_layout.setContentsMargins(0, 2, 0, 0)
        self.formulas_layout.setSpacing(4)
        right_content_layout.addWidget(self.formulas_container)
        right_content_layout.addStretch()
        right_layout.addWidget(self.right_content, stretch=1)

        self.hamburger_right_inner = HamburgerButton(line_color="#374151")
        self.hamburger_right_inner.setObjectName("sidebarCloseBtn")
        self.hamburger_right_inner.setToolTip("Tags & Verlinkungen ausblenden")
        self.hamburger_right_inner.clicked.connect(
            lambda: self._toggle_right()
        )
        right_bottom = QHBoxLayout()
        right_bottom.setContentsMargins(0, 0, 0, 0)
        right_bottom.addStretch()
        right_bottom.addWidget(self.hamburger_right_inner)
        right_layout.addLayout(right_bottom)
        body_layout.addWidget(self.right_sidebar)

        self.right_anim = QPropertyAnimation(
            self.right_sidebar, b"maximumWidth"
        )
        self.right_anim.setDuration(260)
        self.right_anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.right_anim.finished.connect(self._on_right_anim_done)

        root.addWidget(body, stretch=1)

        # Floating-Toggle-Buttons: sichtbar wenn Sidebar geschlossen ist.
        self.left_float_btn = HamburgerButton(parent=self)
        self.left_float_btn.setObjectName("leftFloatBtn")
        self.left_float_btn.setFixedSize(36, 36)
        self.left_float_btn.setToolTip("Artikelliste einblenden")
        self.left_float_btn.clicked.connect(lambda: self._toggle_left())
        self.left_float_btn.hide()

        self.right_float_btn = HamburgerButton(parent=self)
        self.right_float_btn.setObjectName("rightFloatBtn")
        self.right_float_btn.setFixedSize(36, 36)
        self.right_float_btn.setToolTip("Tags & Verlinkungen einblenden")
        self.right_float_btn.clicked.connect(lambda: self._toggle_right())
        self.right_float_btn.hide()

        QShortcut(QKeySequence("Alt+Left"), self).activated.connect(self._go_back)
        QShortcut(QKeySequence("Ctrl+F"), self).activated.connect(
            lambda: (self.search.setFocus(), self.search.selectAll())
        )
        QShortcut(QKeySequence("Return"), self.article_tree).activated.connect(
            self._activate_current_tree_item
        )

    # ── Sidebar-Toggle ────────────────────────────────────────────────────────
    def _toggle_left(self) -> None:
        self.left_anim.stop()
        start = self.left_sidebar.width()
        if self._left_open:
            self._left_open = False
            self.left_float_btn.show()
            self.left_float_btn.raise_()
            self._reposition_float_buttons()
            self.left_anim.setStartValue(start)
            self.left_anim.setEndValue(0)
        else:
            self._left_open = True
            self.left_float_btn.hide()
            self.left_content.show()
            self.hamburger_left_inner.show()
            self.left_anim.setStartValue(start)
            self.left_anim.setEndValue(220)
        self.left_anim.start()

    def _toggle_right(self) -> None:
        self.right_anim.stop()
        start = self.right_sidebar.width()
        if self._right_open:
            self._right_open = False
            self.right_float_btn.show()
            self.right_float_btn.raise_()
            self._reposition_float_buttons()
            self.right_anim.setStartValue(start)
            self.right_anim.setEndValue(0)
        else:
            self._right_open = True
            self.right_float_btn.hide()
            self.right_content.show()
            self.hamburger_right_inner.show()
            self.right_anim.setStartValue(start)
            self.right_anim.setEndValue(175)
        self.right_anim.start()

    def _on_left_anim_done(self) -> None:
        if not self._left_open:
            self.left_content.hide()
            self.hamburger_left_inner.hide()

    def _on_right_anim_done(self) -> None:
        if not self._right_open:
            self.right_content.hide()
            self.hamburger_right_inner.hide()

    def _reposition_float_buttons(self) -> None:
        h = self.height()
        w = self.width()
        margin = 12
        btn = 36
        self.left_float_btn.move(margin, h - btn - margin)
        self.right_float_btn.move(w - btn - margin, h - btn - margin)

    def resizeEvent(self, event) -> None:  # type: ignore[override]
        super().resizeEvent(event)
        self._reposition_float_buttons()

    # ── Artikel-Anzeige & Navigation ──────────────────────────────────────────
    def _refresh_list(self) -> None:
        """Baut den Artikel-Baum aus der Ordnerhierarchie neu auf.

        Ordner unter dem Artikel-Wurzelordner werden zu verschachtelten
        Knoten; Markdown-Dateien sind die Blaetter. Ohne Suchbegriff
        werden Top-Level-Ordner aufgeklappt, tiefere Ebenen bleiben
        zugeklappt. Mit aktiver Suche werden alle Knoten aufgeklappt,
        damit die Treffer sichtbar sind.
        """
        query = self.search.text().strip()
        articles = self.view_model.filtered_articles(query)
        tree = self._build_folder_tree(articles)

        self.article_tree.clear()
        expand_all = bool(query)
        self._populate_tree(None, tree, expand_all=expand_all)
        if not expand_all:
            for i in range(self.article_tree.topLevelItemCount()):
                top = self.article_tree.topLevelItem(i)
                if top is not None and top.childCount() > 0:
                    top.setExpanded(True)

        self.count_label.setText(f"{len(articles)} Begriffe")

    def _build_folder_tree(
        self, articles: dict[str, dict[str, Any]]
    ) -> dict[str, Any]:
        """Erstellt eine geschachtelte Dict-Struktur aus den Artikelpfaden.

        Rueckgabe:
            ``{"dirs": {name: sub_node}, "files": [(title, article), ...]}``
        """
        root: dict[str, Any] = {"dirs": {}, "files": []}
        folder = self.view_model.folder
        for title, article in articles.items():
            try:
                rel = article["datei"].relative_to(folder)
            except ValueError:
                rel = Path(article["datei"].name)
            node = root
            for part in rel.parts[:-1]:
                node["dirs"].setdefault(
                    part, {"dirs": {}, "files": []}
                )
                node = node["dirs"][part]
            node["files"].append((title, article))
        return root

    def _populate_tree(
        self,
        parent: QTreeWidgetItem | None,
        node: dict[str, Any],
        expand_all: bool,
    ) -> None:
        """Haengt Ordner- und Artikel-Knoten rekursiv in den Baum ein."""
        for dirname in sorted(node["dirs"]):
            folder_display = dirname.replace("_", " ").title()
            folder_item = QTreeWidgetItem([folder_display])
            folder_item.setToolTip(0, dirname)
            subnode = node["dirs"][dirname]
            matching = next(
                (t for t, _ in subnode["files"]
                 if t.lower() in (dirname.lower(), folder_display.lower())),
                None,
            )
            if matching is not None:
                folder_item.setData(0, Qt.ItemDataRole.UserRole, matching)
            if parent is None:
                self.article_tree.addTopLevelItem(folder_item)
            else:
                parent.addChild(folder_item)
            self._populate_tree(folder_item, subnode, expand_all)
            if expand_all:
                folder_item.setExpanded(True)
        for title, _article in sorted(node["files"]):
            leaf = QTreeWidgetItem([title])
            leaf.setData(0, Qt.ItemDataRole.UserRole, title)
            if parent is None:
                self.article_tree.addTopLevelItem(leaf)
            else:
                parent.addChild(leaf)

    def _on_tree_item_clicked(
        self, item: QTreeWidgetItem, _column: int
    ) -> None:
        title = item.data(0, Qt.ItemDataRole.UserRole)
        if title:
            self._show_article(title)
            if item.childCount() > 0:
                item.setExpanded(True)
            return
        item.setExpanded(not item.isExpanded())

    def _activate_current_tree_item(self) -> None:
        item = self.article_tree.currentItem()
        if item is not None:
            self._on_tree_item_clicked(item, 0)

    def _on_link_clicked(self, url: QUrl) -> None:
        if url.scheme() == "artikel":
            self._show_article(
                unquote(url.path().lstrip("/")), push_history=True
            )

    def _show_article(self, title: str, push_history: bool = True) -> None:
        if title not in self.view_model.all_articles:
            self.display.render_html(
                f'<p style="color:#9ca3af;padding:40px;">Artikel '
                f"<b>{title}</b> nicht gefunden.</p>"
            )
            return
        self.view_model.navigate(title, push_history)
        self.view_model.add_recent(title)
        self.back_button.setEnabled(self.view_model.can_go_back())
        parts = self.view_model.breadcrumb(title)
        self.breadcrumb_label.setText("  ›  ".join(parts))

        article_folder: Path = (
            self.view_model.all_articles[title]["datei"].parent
        )
        self.display.render_blocks(
            self.view_model.article_blocks(title),
            article_folder,
        )

        # Tags
        self._clear_layout(self.tags_layout)
        tags = self.view_model.article_tags(title)
        for i, tag in enumerate(tags):
            bg, fg = TAG_COLORS[i % len(TAG_COLORS)]
            button = QPushButton(tag)
            button.setStyleSheet(
                f"QPushButton{{background:{bg};color:{fg};border:none;"
                f"border-radius:99px;font-size:11px;font-weight:500;"
                f"padding:3px 10px;text-align:left;}}"
                f"QPushButton:hover{{border:1px solid {fg};}}"
            )
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.setToolTip(f'Nach Tag "{tag}" filtern')
            button.clicked.connect(lambda _checked, t=tag: self.search.setText(t))
            self.tags_layout.addWidget(button)
        if not tags:
            no_tags = QLabel("Keine Tags")
            no_tags.setObjectName("emptyLabel")
            self.tags_layout.addWidget(no_tags)

        # Verlinkungen
        self._clear_layout(self.links_layout)
        links = self.view_model.article_links(title)
        for target, found in links:
            button = QPushButton(target)
            if found:
                button.setObjectName("foundLink")
                button.setCursor(Qt.CursorShape.PointingHandCursor)
                button.clicked.connect(
                    lambda _checked, t=found: self._show_article(
                        t, push_history=True
                    )
                )
            else:
                button.setObjectName("brokenLink")
                button.setEnabled(False)
            self.links_layout.addWidget(button)
        if not links:
            no_links = QLabel("Keine Verlinkungen")
            no_links.setObjectName("emptyLabel")
            self.links_layout.addWidget(no_links)

        # Formeln -> CAS (rechte Seitenleiste)
        self._clear_layout(self.formulas_layout)
        formulas = self.view_model.article_formulas(title)
        for formula in formulas:
            cas_btn = QPushButton(formula)
            cas_btn.setObjectName("formulaButton")
            cas_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            cas_btn.setToolTip("In CAS-Rechner übernehmen")
            cas_btn.clicked.connect(
                lambda _checked, f=formula: self._send_formula_to_calculator(f)
            )
            self.formulas_layout.addWidget(cas_btn)
        if not formulas:
            no_formulas = QLabel("Keine Formeln")
            no_formulas.setObjectName("emptyLabel")
            self.formulas_layout.addWidget(no_formulas)

        # Aktuellen Artikel im Baum markieren und Elternknoten aufklappen.
        iterator = QTreeWidgetItemIterator(self.article_tree)
        while iterator.value():
            item = iterator.value()
            if item.data(0, Qt.ItemDataRole.UserRole) == title:
                self.article_tree.setCurrentItem(item)
                ancestor = item.parent()
                while ancestor is not None:
                    ancestor.setExpanded(True)
                    ancestor = ancestor.parent()
                break
            iterator += 1

    def save_state(self) -> None:
        self.view_model.save_state()

    def _send_formula_to_calculator(self, formula: str) -> None:
        if self._on_send_formula_external is not None:
            self._on_send_formula_external(formula)

    def _clear_layout(self, layout: QLayout) -> None:
        """Entfernt alle Widgets eines Layouts und plant sie zum Loeschen ein."""
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def _show_home(self) -> None:
        """Zeigt die Startseite mit Kategorien-Uebersicht."""
        self.view_model.current_title = None
        self.breadcrumb_label.setText("")
        self.display.render_html(self.view_model.home_html())
        for layout in (
            self.tags_layout, self.links_layout, self.formulas_layout
        ):
            self._clear_layout(layout)

    def _go_back(self) -> None:
        title = self.view_model.go_back()
        if title is not None:
            self._show_article(title, push_history=False)
        else:
            self._show_home()
        self.back_button.setEnabled(self.view_model.can_go_back())
