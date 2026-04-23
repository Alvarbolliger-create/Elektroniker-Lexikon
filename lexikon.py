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
import os
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, TypeAlias
from urllib.parse import quote, unquote

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QUrl
from PySide6.QtGui import QColor, QKeySequence, QPainter, QPaintEvent, QPixmap, QShortcut
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
    """Code-Block: geordnete Liste nicht-leerer Formelzeilen."""

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


ArticleBlock: TypeAlias = (
    HeadingBlock
    | ParagraphBlock
    | CodeBlock
    | ListBlock
    | ImageBlock
    | TableBlock
    | ArticleHeaderBlock
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

        if line.strip().startswith("```"):
            flush_list()
            if not in_code:
                in_code = True
                code_buf = []
            else:
                in_code = False
                formula_lines = [ln.strip() for ln in code_buf if ln.strip()]
                if formula_lines:
                    blocks.append(CodeBlock(lines=formula_lines))
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
        """Extrahiert ausfuehrbare Formeln aus Inline-Code und Code-Bloecken.

        Returns:
            Deduplizierte Liste von Formel-Strings (mind. 3 Zeichen,
            enthalten mindestens ein Rechenzeichen).
        """
        if title not in self.all_articles:
            return []
        article = self.all_articles[title]
        ensure_article_text(article)
        text = article["text"]
        formulas: list[str] = re.findall(r"`([^`]*[=+\-*/][^`]*)`", text)
        for block in re.findall(r"```\n?(.*?)\n?```", text, re.DOTALL):
            for line in block.strip().splitlines():
                line = line.strip()
                if line and any(ch in line for ch in "=+-*/"):
                    formulas.append(line)
        seen: set[str] = set()
        result: list[str] = []
        for formula in formulas:
            formula = formula.strip()
            if formula not in seen and len(formula) >= 3:
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
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 6, 6, 6)
        layout.setSpacing(8)

        display = MathFormulaDisplay(formula)
        layout.addWidget(display, stretch=1)

        copy_btn = QPushButton("⎘")
        copy_btn.setFixedWidth(28)
        copy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        copy_btn.setToolTip("In Zwischenablage kopieren")
        copy_btn.clicked.connect(lambda: QApplication.clipboard().setText(formula))
        layout.addWidget(copy_btn)


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
        if isinstance(block, ListBlock):
            return self._make_list(block)
        if isinstance(block, TableBlock):
            return self._make_table(block)
        if isinstance(block, ImageBlock):
            return self._make_image(block, article_folder)
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
        img_path = article_folder / block.path

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
        self.article_tree.itemExpanded.connect(
            lambda item: self._set_folder_arrow(item, expanded=True)
        )
        self.article_tree.itemCollapsed.connect(
            lambda item: self._set_folder_arrow(item, expanded=False)
        )
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
            folder_item = QTreeWidgetItem(["▶ " + folder_display])
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

    def _set_folder_arrow(self, item: QTreeWidgetItem, expanded: bool) -> None:
        if item.childCount() == 0:
            return
        text = item.text(0)
        base = text[2:] if text[:2] in ("▶ ", "▼ ") else text
        item.setText(0, ("▼ " if expanded else "▶ ") + base)

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
            row = QWidget()
            row_layout = QHBoxLayout(row)
            row_layout.setContentsMargins(0, 0, 0, 0)
            row_layout.setSpacing(4)
            cas_btn = QPushButton(formula)
            cas_btn.setObjectName("formulaButton")
            cas_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            cas_btn.setToolTip("In CAS-Rechner uebernehmen")
            cas_btn.clicked.connect(
                lambda _checked, f=formula: self._send_formula_to_calculator(f)
            )
            row_layout.addWidget(cas_btn, stretch=1)
            copy_btn = QPushButton("⎘")
            copy_btn.setFixedWidth(28)
            copy_btn.setCursor(Qt.CursorShape.PointingHandCursor)
            copy_btn.setToolTip("In Zwischenablage kopieren")
            copy_btn.clicked.connect(
                lambda _checked, f=formula: QApplication.clipboard().setText(f)
            )
            row_layout.addWidget(copy_btn)
            self.formulas_layout.addWidget(row)
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
