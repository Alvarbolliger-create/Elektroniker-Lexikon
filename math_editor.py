"""math_editor.py - 2D Math Editor (multi-line).

Strukturierter Formel-Editor analog Word / Texas Instruments (TI) NSpire.
Unterstuetzt mehrere Zeilen; jede Zeile bildet einen eigenen
mathematischen Ausdruck. Zeilen, die mit '#' beginnen, werden als
Kommentar grau gerendert und nicht ausgewertet.

Bedienung:
  * Tippen            : fuegt Zeichen an der Cursor-Position ein
  * Enter             : alle Zeilen auswerten + neue Zeile darunter
  * Ctrl+Enter        : aktuelle Zeile numerisch (approx) auswerten
  * Ctrl+Z            : Undo (bis 100 Schritte)
  * Ctrl+Y            : Redo
  * Ctrl+C            : aktuelle Zeile + Ergebnis kopieren (oder Auswahl)
  * Ctrl+X            : aktuelle Zeile ausschneiden (oder Auswahl)
  * Backspace         : loescht links vom Cursor; am Zeilenanfang
                        zusammenfuegen mit vorheriger Zeile
  * Delete            : loescht rechts vom Cursor
  * Left/Right        : horizontal navigieren, ueber Zeilengrenzen
                        hinweg und in Container hinein
  * Up/Down           : wechselt zwischen vertikalen Slots oder
                        zwischen Top-Level-Zeilen (mit x-Memory)
  * Tab               : naechster Slot innerhalb eines Containers;
                        in der letzten Matrix-Zelle neue Zeile anhaengen
  * Ctrl+Tab          : Matrix/Gleichungssystem: Zeile anhaengen
  * Ctrl+Shift+Tab    : Matrix: Spalte anhaengen
  * Backspace in leerer letzter Matrix-Zeile/-Spalte: diese entfernen
  * Backspace in leerer System-Zeile: diese entfernen
  * Backspace direkt rechts von Bruch/Wurzel/...: erst markieren,
                        zweites Backspace loescht den Block
  * / oder Ctrl+F     : Bruch aus Tail (bis letztes Trennzeichen)
  * ^                 : Exponent (hochgestellter Slot)
  * Ctrl+_            : Subscript (tiefgestellter Slot, fuer Namen)
  * Ctrl+R            : Quadratwurzel
  * Ctrl+Shift+R      : n-te Wurzel
  * Alt+S             : Summe Sigma
  * Alt+I             : Integral
  * Alt+V             : Vektor (2x1)
  * Alt+G             : Gleichungssystem (2 Zeilen, geschweifte Klammer)

Engine-Anbindung:
  set_engine(engine) setzt die Auswertungs-Engine. Enter schickt alle
  Zeilen via Engine.evaluate_all() und zeigt Ergebnisse rechts nach
  dem Separator.

Start als Standalone (ohne Engine):
  python3 math_editor.py

Abkuerzungen (Initialnotation):
  CAS  : Computer Algebra System
  GUI  : Graphical User Interface
  TI   : Texas Instruments
  SWE  : Softwareentwickler
"""
from __future__ import annotations

import copy
from collections import deque
from dataclasses import dataclass
from typing import Any

from PySide6.QtCore import QPointF, QRectF, QSize, Qt, QTimer
from PySide6.QtGui import (
    QColor, QFont, QFontMetricsF, QKeyEvent, QMouseEvent, QPainter,
    QPainterPath, QPen,
)
from PySide6.QtWidgets import QApplication, QScrollArea, QWidget


# ── Farben & Fonts ────────────────────────────────────────────────────────────
C_TEXT: str = "#111827"
C_CURSOR: str = "#1a56db"
C_SLOT_EMPTY: str = "#9ca3af"   # gestrichelter Rahmen für leeren Slot
C_SLOT_FOCUS: str = "#6366f1"   # gestrichelter Rahmen für Slot mit Cursor
C_FRAC_LINE: str = "#111827"
C_RES_OK: str = "#15803d"   # Ergebnis: grün
C_RES_ERR: str = "#dc2626"   # Ergebnis: rot
C_COMMENT: str = "#9ca3af"   # Kommentarzeilen (grau)
C_SEP: str = "#9ca3af"   # Separator ▶

FONT_FAMILIES: list[str] = ["Cambria Math", "Cambria", "Georgia", "Palatino Linotype", "serif"]
FONT_SIZE_PT: int = 18

FRAC_GAP: float = 3.0   # Abstand zwischen Zähler/Strich/Nenner
FRAC_PAD_X: float = 4.0   # horizontaler Innenabstand im Bruch
FRAC_SCALE: float = 0.85  # Schriftverkleinerung in verschachtelten Brüchen
SLOT_MIN_W: float = 10.0  # Mindestbreite für leeren Slot
SLOT_MIN_H: float = 16.0

# Exponent / Subscript
SUPER_SCALE: float = 0.72
SUB_SCALE: float = 0.72
SUPER_RAISE_FACTOR: float = 0.65   # * x_height des Umgebungs-Fonts = Hebung der Exponent-Baseline
SUB_DROP_FACTOR: float = 0.20   # * x_height = Senkung der Subscript-Baseline

# Wurzel
SQRT_PAD_TOP: float = 3.0        # Abstand zwischen Vinculum-Strich und Radikand
SQRT_PAD_LEFT: float = 1.0        # Abstand Wurzelzeichen → Radikand
SQRT_PAD_RIGHT: float = 2.0        # Überhang des Vinculum rechts
SQRT_RADIX_W_FACTOR: float = 0.55  # Breite des Wurzelhakens ≈ Faktor * Höhe des Radikanden
NTH_INDEX_SCALE: float = 0.55      # Schriftverkleinerung im Index der n-ten Wurzel

# Grosse Operatoren (Σ, ∫)
BIGOP_LIMIT_SCALE: float = 0.65    # Schriftgrösse der Grenzen/Indizes
BIGOP_GAP: float = 2.0     # vertikaler Abstand zwischen Operator und Grenze
BIGOP_BODY_GAP: float = 4.0     # horizontaler Abstand zwischen Operator-Block und Body
SUM_SIZE_FACTOR: float = 1.8     # Σ-Glyph relativ zur Umgebungsschrift
INT_SIZE_FACTOR: float = 2.2     # ∫-Glyph relativ zur Umgebungsschrift (schmaler, deshalb grösser)
INT_LIMIT_X_OFFSET: float = 0.3     # Grenzen um diesen Bruchteil der ∫-Breite nach rechts versetzt
INT_LIMIT_INTO_OP: float = 0.2     # Anteil der Grenzhöhe, der ins ∫-Zeichen hineinragt
INT_D_GAP: float = 3.0     # Abstand body → "d" → var

# Matrix / Vektor
MATRIX_COL_GAP: float = 10.0    # horizontaler Abstand zwischen Spalten
MATRIX_ROW_GAP: float = 4.0     # vertikaler Abstand zwischen Zeilen
MATRIX_PAD_X: float = 6.0     # horizontales Padding zwischen Klammer und Inhalt
MATRIX_PAD_Y: float = 2.0     # vertikales Padding innerhalb der Klammer
MATRIX_BRACKET_W: float = 6.0     # Breite der eckigen Klammer

# Gleichungssystem (geschweifte Klammer links, eine Zeile pro Gleichung)
SYSTEM_BRACE_W: float = 9.0       # Breite der geschweiften Klammer
SYSTEM_ROW_GAP: float = 4.0       # vertikaler Abstand zwischen Zeilen
SYSTEM_PAD_X: float = 6.0         # horizontales Padding Klammer → Inhalt
SYSTEM_PAD_Y: float = 2.0         # vertikales Padding innerhalb der Klammer

SEP_TEXT: str = "  ▶  "          # Separator zwischen Ausdruck und Ergebnis
LINE_GAP: float = 8.0              # vertikaler Abstand zwischen Multi-Line-Zeilen


# ── Node-Hierarchie ───────────────────────────────────────────────────────────
class MathNode:
    """Basisklasse. Jeder Node weiss nach measure() wie gross er ist.

    Koordinaten: x nach rechts, y nach unten. Ein Node hat eine Baseline;
    ascent ist der Abstand von oben bis Baseline, descent von Baseline bis
    unten. height = ascent + descent.
    """

    def __init__(self) -> None:
        self.parent: RowNode | None = None
        self.width: float = 0.0
        self.ascent: float = 0.0
        self.descent: float = 0.0
        # Position der oberen linken Ecke im Parent - wird beim Layout gesetzt.
        self.x: float = 0.0
        self.y: float = 0.0
        # Schriftgroesse in Punkt, die dieser Node verwenden soll.
        self.font_size: float = FONT_SIZE_PT

    @property
    def height(self) -> float:
        return self.ascent + self.descent

    def measure(self, font_size: float) -> None:
        """Berechnet width/ascent/descent. Muss von Unterklasse überschrieben."""
        raise NotImplementedError

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        """Zeichnet diesen Node. (x,y) = obere linke Ecke."""
        raise NotImplementedError


class TextNode(MathNode):
    """Ein einzelnes Zeichen. Ein-Zeichen-pro-Node macht die Cursor-Logik
    trivial - jeder Text-Node ist zwischen zwei Cursor-Positionen."""

    def __init__(self, char: str) -> None:
        super().__init__()
        assert len(char) == 1
        self.char = char
        self.color: str = C_TEXT

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        font = _make_font(font_size)
        fm = QFontMetricsF(font)
        self.width = fm.horizontalAdvance(self.char)
        self.ascent = fm.ascent()
        self.descent = fm.descent()

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        painter.save()
        painter.setFont(_make_font(self.font_size))
        painter.setPen(QColor(self.color))
        # drawText mit (x, baseline_y)
        painter.drawText(QPointF(x, y + self.ascent), self.char)
        painter.restore()


class RowNode(MathNode):
    """Horizontaler Container. Kann beliebig viele Kinder enthalten.

    Cursor-Positionen in einer Row: 0 .. len(children). Index i = links
    vom Kind i (bzw. am Ende, wenn i == len).
    """

    def __init__(self, children: Optional[list[MathNode]] = None) -> None:
        super().__init__()
        self.children: list[MathNode] = []
        # Merkt sich die letzte Cursor-Position in diesem Slot, damit
        # vertikale Navigation (↑/↓, Tab) wieder dort landet, wo der
        # Cursor zuletzt war. None = Slot wurde noch nie betreten.
        self.last_cursor_index: int | None = None
        if children:
            for c in children:
                self.append(c)

    # -- Struktur ---
    def append(self, node: MathNode) -> None:
        node.parent = self
        self.children.append(node)

    def insert(self, index: int, node: MathNode) -> None:
        node.parent = self
        self.children.insert(index, node)

    def pop(self, index: int) -> MathNode:
        node = self.children.pop(index)
        node.parent = None
        return node

    # -- Layout ---
    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        if not self.children:
            # Leerer Slot - Platzhalter-Grösse, damit man reinklicken kann.
            fm = QFontMetricsF(_make_font(font_size))
            self.width = SLOT_MIN_W
            self.ascent = fm.ascent() * 0.75
            self.descent = fm.descent() * 0.75
            return
        for c in self.children:
            c.measure(font_size)
        self.width = sum(c.width for c in self.children)
        self.ascent = max(c.ascent for c in self.children)
        self.descent = max(c.descent for c in self.children)

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        baseline = y + self.ascent
        cx = x
        for c in self.children:
            # Jedes Kind auf gemeinsame Baseline ausrichten.
            top = baseline - c.ascent
            c.x = cx
            c.y = top
            c.paint(painter, cx, top)
            cx += c.width

    # -- Cursor-Geometrie ---
    def cursor_x_at(self, index: int) -> float:
        """Lokale x-Koordinate (relativ zum eigenen x) des Cursors vor Kind i."""
        if index <= 0 or not self.children:
            return 0.0
        if index >= len(self.children):
            return self.width
        return sum(c.width for c in self.children[:index])


class FractionNode(MathNode):
    """Bruch. Zähler oben, Nenner unten, waagrechter Strich dazwischen.

    Baseline liegt auf Höhe des Bruchstrichs (bzw. leicht darüber, typisch
    auf der Math-Axis). Der Bruchstrich-Offset relativ zur Baseline ist
    math_axis; ascent = num.height + gap + math_axis, descent =
    denom.height + gap - math_axis.
    """

    def __init__(self, numerator: RowNode | None = None,
                 denominator: RowNode | None = None) -> None:
        super().__init__()
        self.numerator: RowNode = numerator if numerator is not None else RowNode()
        self.denominator: RowNode = denominator if denominator is not None else RowNode()
        self.numerator.parent = None   # parent wird hier nicht als Row gesetzt
        self.denominator.parent = None
        # Spezielles Parent-Feld, damit Cursor-Logik "rauslaufen" kann:
        self.numerator._container_parent = self    # type: ignore[attr-defined]
        self.denominator._container_parent = self  # type: ignore[attr-defined]
        self._math_axis = 0.0   # y-Offset der Baseline zum Bruchstrich
        self.bar_color: str = C_FRAC_LINE

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        inner = font_size * FRAC_SCALE
        self.numerator.measure(inner)
        self.denominator.measure(inner)

        self.width = max(self.numerator.width, self.denominator.width) + 2 * FRAC_PAD_X

        # Bruchstrich-Position: ungefähr auf x-Höhe der Umgebungs-Schrift.
        fm = QFontMetricsF(_make_font(font_size))
        x_height = fm.xHeight()
        self._math_axis = x_height * 0.5  # Baseline sitzt knapp unterhalb Strich

        self.ascent = self.numerator.height + FRAC_GAP + self._math_axis
        self.descent = self.denominator.height + FRAC_GAP - self._math_axis

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        # Bruchstrich-Y relativ zum Bruch:
        bar_y = y + self.numerator.height + FRAC_GAP

        # Zähler zentriert:
        num_x = x + (self.width - self.numerator.width) / 2
        num_y = y
        self.numerator.x = num_x
        self.numerator.y = num_y
        self.numerator.paint(painter, num_x, num_y)

        # Strich:
        painter.save()
        pen = QPen(QColor(self.bar_color))
        pen.setWidthF(max(1.0, self.font_size / 18.0))
        pen.setCapStyle(Qt.FlatCap)
        painter.setPen(pen)
        painter.drawLine(QPointF(x + 1, bar_y), QPointF(x + self.width - 1, bar_y))
        painter.restore()

        # Nenner zentriert:
        den_x = x + (self.width - self.denominator.width) / 2
        den_y = bar_y + FRAC_GAP
        self.denominator.x = den_x
        self.denominator.y = den_y
        self.denominator.paint(painter, den_x, den_y)

    # -- Container-Interface (wird von der Cursor-Navigation genutzt) --
    def slots(self) -> list[RowNode]:
        return [self.numerator, self.denominator]

    def slot_above(self, row: RowNode) -> RowNode | None:
        return self.numerator if row is self.denominator else None

    def slot_below(self, row: RowNode) -> RowNode | None:
        return self.denominator if row is self.numerator else None

    def first_slot(self) -> RowNode:
        return self.numerator

    def last_slot(self) -> RowNode:
        return self.denominator


class SuperscriptNode(MathNode):
    """Hochgestellter Slot (Exponent). Hat nur einen Slot `inner`. Die
    Basis - also auf was sich der Exponent bezieht - steht links davor
    im umgebenden Row. Das Serialisieren fügt entsprechend `^(…)` ein."""

    def __init__(self, inner: RowNode | None = None) -> None:
        super().__init__()
        self.inner: RowNode = inner if inner is not None else RowNode()
        self.inner.parent = None
        self.inner._container_parent = self   # type: ignore[attr-defined]
        self._raise = 0.0

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        self.inner.measure(font_size * SUPER_SCALE)
        fm = QFontMetricsF(_make_font(font_size))
        self._raise = fm.xHeight() * SUPER_RAISE_FACTOR
        self.width = self.inner.width
        # Die Unterkante des Exponenten liegt _raise über der umgebenden Baseline.
        # Also: ascent des Exponenten ab der umgebenden Baseline = inner.height + _raise.
        # descent = 0 (unter der Baseline nichts).
        self.ascent = self.inner.height + self._raise
        self.descent = 0.0

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        # Ganze Exponent-Box liegt komplett über der umgebenden Baseline.
        self.inner.x = x
        self.inner.y = y
        self.inner.paint(painter, x, y)

    def slots(self) -> list[RowNode]:
        return [self.inner]

    def slot_above(self, row: RowNode) -> RowNode | None:
        return None

    def slot_below(self, row: RowNode) -> RowNode | None:
        return None

    def first_slot(self) -> RowNode:
        return self.inner

    def last_slot(self) -> RowNode:
        return self.inner


class SubscriptNode(MathNode):
    """Tiefgestellter Slot - wird nur für Namen/Indizes verwendet, hat
    keine mathematische Wirkung. Geometrie analog zu SuperscriptNode."""

    def __init__(self, inner: RowNode | None = None) -> None:
        super().__init__()
        self.inner: RowNode = inner if inner is not None else RowNode()
        self.inner.parent = None
        self.inner._container_parent = self   # type: ignore[attr-defined]
        self._drop = 0.0

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        self.inner.measure(font_size * SUB_SCALE)
        fm = QFontMetricsF(_make_font(font_size))
        self._drop = fm.xHeight() * SUB_DROP_FACTOR
        self.width = self.inner.width
        self.ascent = 0.0
        self.descent = self.inner.height + self._drop

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        # y ist die Oberkante der Subscript-Box; die liegt _drop unter der
        # umgebenden Baseline. Das wird vom Row-Layout automatisch richtig
        # positioniert (Row macht baseline-alignment anhand von ascent).
        self.inner.x = x
        self.inner.y = y
        self.inner.paint(painter, x, y)

    def slots(self) -> list[RowNode]:
        return [self.inner]

    def slot_above(self, row: RowNode) -> RowNode | None:
        return None

    def slot_below(self, row: RowNode) -> RowNode | None:
        return None

    def first_slot(self) -> RowNode:
        return self.inner

    def last_slot(self) -> RowNode:
        return self.inner


class LogNode(MathNode):
    """Logarithmus mit tiefgestellter Basis: logₙ(argument).

    Visuell: log[Basis](Argument) mit Basis als Subscript rechts von 'log'.
    Serialisiert als log(argument, base) (SymPy-Notation). Leere Basis →
    log(argument) (natürlicher Logarithmus in SymPy).
    Tab-Reihenfolge: Basis → Argument."""

    def __init__(self) -> None:
        super().__init__()
        self.base     = RowNode()
        self.argument = RowNode()
        for s in (self.base, self.argument):
            s.parent = None
            s._container_parent = self   # type: ignore[attr-defined]
        self._log_w       = 0.0
        self._log_ascent  = 0.0
        self._log_descent = 0.0
        self._paren_w     = 0.0
        self._base_drop   = 0.0

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        sub_fs = font_size * SUB_SCALE
        self.base.measure(sub_fs)
        self.argument.measure(font_size)

        fm = QFontMetricsF(_make_font(font_size))
        self._log_w       = fm.horizontalAdvance("log")
        self._log_ascent  = fm.ascent()
        self._log_descent = fm.descent()
        self._paren_w     = fm.horizontalAdvance("(")
        self._base_drop   = fm.xHeight() * SUB_DROP_FACTOR

        self.width = (self._log_w + self.base.width
                      + self._paren_w + self.argument.width + self._paren_w)
        self.ascent  = max(self._log_ascent,  self.argument.ascent)
        base_desc    = self._log_descent + self._base_drop + self.base.height
        self.descent = max(base_desc, self._log_descent, self.argument.descent)

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        baseline = y + self.ascent

        painter.save()
        painter.setFont(_make_font(self.font_size))
        painter.setPen(QColor(C_TEXT))
        painter.drawText(QPointF(x, baseline), "log")
        painter.restore()

        base_x = x + self._log_w
        base_y = baseline + self._base_drop
        self.base.x = base_x
        self.base.y = base_y
        self.base.paint(painter, base_x, base_y)

        paren_x = base_x + self.base.width
        painter.save()
        painter.setFont(_make_font(self.font_size))
        painter.setPen(QColor(C_TEXT))
        painter.drawText(QPointF(paren_x, baseline), "(")
        painter.restore()

        arg_x = paren_x + self._paren_w
        arg_y = baseline - self.argument.ascent
        self.argument.x = arg_x
        self.argument.y = arg_y
        self.argument.paint(painter, arg_x, arg_y)

        close_x = arg_x + self.argument.width
        painter.save()
        painter.setFont(_make_font(self.font_size))
        painter.setPen(QColor(C_TEXT))
        painter.drawText(QPointF(close_x, baseline), ")")
        painter.restore()

    def slots(self) -> list[RowNode]:
        return [self.base, self.argument]

    def slot_above(self, row: RowNode) -> RowNode | None:
        return None

    def slot_below(self, row: RowNode) -> RowNode | None:
        return None

    def first_slot(self) -> RowNode:
        return self.base

    def last_slot(self) -> RowNode:
        return self.argument


class SqrtNode(MathNode):
    """Quadratwurzel - Wurzelzeichen + Vinculum-Strich über dem Radikanden.
    Ein einziger Slot `inner`."""

    def __init__(self, inner: RowNode | None = None) -> None:
        super().__init__()
        self.inner: RowNode = inner if inner is not None else RowNode()
        self.inner.parent = None
        self.inner._container_parent = self   # type: ignore[attr-defined]
        self._radix_w = 0.0
        self.radical_color: str = C_TEXT

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        self.inner.measure(font_size)
        inner_h = max(self.inner.height, SLOT_MIN_H)
        self._radix_w = max(8.0, inner_h * SQRT_RADIX_W_FACTOR)
        self.width = self._radix_w + SQRT_PAD_LEFT + self.inner.width + SQRT_PAD_RIGHT
        self.ascent = self.inner.ascent + SQRT_PAD_TOP
        self.descent = self.inner.descent

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        inner_top = y + SQRT_PAD_TOP
        inner_x = x + self._radix_w + SQRT_PAD_LEFT
        inner_h = max(self.inner.height, SLOT_MIN_H)
        bottom = inner_top + self.inner.height

        # Radix-Pfad zeichnen
        painter.save()
        pen = QPen(QColor(self.radical_color))
        pen.setWidthF(max(1.0, self.font_size / 14.0))
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.MiterJoin)
        painter.setPen(pen)

        rw = self._radix_w
        # Vier Punkte: Haken-Start (kleiner Aufschwung), Tiefpunkt,
        # obere Ecke, Ende des Vinculum-Strichs.
        p1 = QPointF(x,                  inner_top + inner_h * 0.55)
        p2 = QPointF(x + rw * 0.30,      bottom)
        p3 = QPointF(x + rw,             y + 0.5)           # obere Ecke des Zeichens
        p4 = QPointF(x + self.width - 1, y + 0.5)           # Vinculum bis rechts
        painter.drawLine(p1, p2)
        painter.drawLine(p2, p3)
        painter.drawLine(p3, p4)
        painter.restore()

        # Inner zeichnen
        self.inner.x = inner_x
        self.inner.y = inner_top
        self.inner.paint(painter, inner_x, inner_top)

    def slots(self) -> list[RowNode]:
        return [self.inner]

    def slot_above(self, row: RowNode) -> RowNode | None:
        return None

    def slot_below(self, row: RowNode) -> RowNode | None:
        return None

    def first_slot(self) -> RowNode:
        return self.inner

    def last_slot(self) -> RowNode:
        return self.inner


class NthRootNode(MathNode):
    """n-te Wurzel: wie Sqrt, aber mit einem kleinen Index-Slot oben links.
    Slots: [index, inner]. ← von rechts → inner; ↑ im inner → index."""

    def __init__(self, index: RowNode | None = None,
                 inner: RowNode | None = None) -> None:
        super().__init__()
        self.index: RowNode = index if index is not None else RowNode()
        self.inner: RowNode = inner if inner is not None else RowNode()
        self.index.parent = None
        self.inner.parent = None
        self.index._container_parent = self   # type: ignore[attr-defined]
        self.inner._container_parent = self   # type: ignore[attr-defined]
        self._radix_w = 0.0
        self._index_offset_x = 0.0   # x-Offset, an dem der Index beginnt
        self._index_top = 0.0        # y-Offset, an dem der Index beginnt
        self.radical_color: str = C_TEXT

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        self.inner.measure(font_size)
        self.index.measure(font_size * NTH_INDEX_SCALE)
        inner_h = max(self.inner.height, SLOT_MIN_H)
        base_radix_w = max(8.0, inner_h * SQRT_RADIX_W_FACTOR)
        # Der Index soll oberhalb des Haken-Knicks sitzen. Wenn er breiter
        # ist als der Platz, erweitern wir das gesamte Wurzelzeichen.
        self._radix_w = max(base_radix_w, self.index.width + 4.0)
        self.width = self._radix_w + SQRT_PAD_LEFT + self.inner.width + SQRT_PAD_RIGHT
        # Der Index ragt nach oben über das Vinculum hinaus.
        index_overhang = max(0.0, self.index.height - inner_h * 0.35)
        self.ascent = self.inner.ascent + SQRT_PAD_TOP + index_overhang
        self.descent = self.inner.descent

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        # Inner-Bereich liegt unterhalb des Index-Überhangs.
        inner_h = max(self.inner.height, SLOT_MIN_H)
        index_overhang = max(0.0, self.index.height - inner_h * 0.35)
        inner_top = y + index_overhang + SQRT_PAD_TOP
        inner_x = x + self._radix_w + SQRT_PAD_LEFT
        bottom = inner_top + self.inner.height

        # Radix-Pfad (wie Sqrt, nur an verschobener y-Position)
        painter.save()
        pen = QPen(QColor(self.radical_color))
        pen.setWidthF(max(1.0, self.font_size / 14.0))
        pen.setCapStyle(Qt.FlatCap)
        pen.setJoinStyle(Qt.MiterJoin)
        painter.setPen(pen)
        rw = self._radix_w
        vinc_y = inner_top - SQRT_PAD_TOP + 0.5
        p1 = QPointF(x,                  inner_top + inner_h * 0.55)
        p2 = QPointF(x + rw * 0.30,      bottom)
        p3 = QPointF(x + rw,             vinc_y)
        p4 = QPointF(x + self.width - 1, vinc_y)
        painter.drawLine(p1, p2)
        painter.drawLine(p2, p3)
        painter.drawLine(p3, p4)
        painter.restore()

        # Index oben links, so, dass seine Unterkante knapp über dem Haken-Knick sitzt
        idx_x = x + rw * 0.15
        idx_y = y   # Index beginnt ganz oben
        self.index.x = idx_x
        self.index.y = idx_y
        self.index.paint(painter, idx_x, idx_y)

        # Inner
        self.inner.x = inner_x
        self.inner.y = inner_top
        self.inner.paint(painter, inner_x, inner_top)

    def slots(self) -> list[RowNode]:
        return [self.index, self.inner]

    def slot_above(self, row: RowNode) -> RowNode | None:
        return self.index if row is self.inner else None

    def slot_below(self, row: RowNode) -> RowNode | None:
        return self.inner if row is self.index else None

    def first_slot(self) -> RowNode:
        return self.inner

    def last_slot(self) -> RowNode:
        return self.inner


class SumNode(MathNode):
    """Summe: Σ mit Grenzen unten (`var = val`) und oben (`upper`) sowie
    einem Body rechts. Die Slot-Reihenfolge in slots() ist [body, lower_var,
    lower_val, upper] - das ist auch die Tab-Reihenfolge.
    Zwischen lower_var und lower_val wird ein festes „=" gerendert."""

    def __init__(self) -> None:
        super().__init__()
        self.body      = RowNode()
        self.lower_var = RowNode()
        self.lower_val = RowNode()
        self.upper     = RowNode()
        for s in (self.body, self.lower_var, self.lower_val, self.upper):
            s.parent = None
            s._container_parent = self   # type: ignore[attr-defined]
        # Geometrie-Zwischenwerte, gefüllt in measure()
        self._op_w = 0.0
        self._op_h = 0.0
        self._op_baseline = 0.0   # Baseline des Σ-Zeichens (relativ zur Box oben)
        self._eq_w = 0.0          # Breite des „="-Zeichens zwischen lower_var & lower_val
        self._lower_w = 0.0       # gesamte Breite des unteren Blocks
        self._op_block_w = 0.0    # Breite von Σ + oberer/unterer Block (max davon)

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        lim_fs = font_size * BIGOP_LIMIT_SCALE
        self.body.measure(font_size)
        self.upper.measure(lim_fs)
        self.lower_var.measure(lim_fs)
        self.lower_val.measure(lim_fs)

        # „="-Zeichen zwischen lower_var und lower_val in Limit-Schrift
        fm_lim = QFontMetricsF(_make_font(lim_fs))
        self._eq_w = fm_lim.horizontalAdvance("=")
        self._lower_w = (self.lower_var.width + self._eq_w
                        + self.lower_val.width)

        # Sigma-Glyph: Groesse proportional zur umgebenden Schrift
        op_fs = font_size * SUM_SIZE_FACTOR
        fm_op = QFontMetricsF(_make_font(op_fs))
        self._op_w = fm_op.horizontalAdvance("∑")
        self._op_h = fm_op.ascent() + fm_op.descent()
        self._op_baseline = fm_op.ascent()

        # Breite des Operator-Blocks = max(Σ, upper, lower)
        self._op_block_w = max(self._op_w, self.upper.width, self._lower_w)

        # Gesamt
        self.width = self._op_block_w + BIGOP_BODY_GAP + self.body.width

        # Vertikale Geometrie: Wir legen die Baseline des Σ-Zeichens auf die
        # umgebende Baseline. Der Body sitzt auf derselben Baseline. Upper
        # thront über dem Operator, lower unter ihm.
        op_ascent_from_baseline  = self._op_baseline
        op_descent_from_baseline = self._op_h - self._op_baseline
        self.ascent  = max(self.body.ascent,
                           op_ascent_from_baseline
                           + BIGOP_GAP + self.upper.height)
        self.descent = max(self.body.descent,
                           op_descent_from_baseline
                           + BIGOP_GAP + max(self.lower_var.height,
                                             self.lower_val.height))

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        baseline = y + self.ascent

        # Operator-Block horizontal zentriert in seiner Breite
        block_x = x
        block_center = block_x + self._op_block_w / 2

        # Σ
        op_fs = self.font_size * SUM_SIZE_FACTOR
        painter.save()
        painter.setFont(_make_font(op_fs))
        painter.setPen(QColor(C_TEXT))
        sigma_x = block_center - self._op_w / 2
        painter.drawText(QPointF(sigma_x, baseline), "∑")
        painter.restore()

        # upper - zentriert über dem Operator
        up_x = block_center - self.upper.width / 2
        up_y = baseline - self._op_baseline - BIGOP_GAP - self.upper.height
        self.upper.x = up_x
        self.upper.y = up_y
        self.upper.paint(painter, up_x, up_y)

        # lower: „var = val" zentriert unter dem Operator
        low_x = block_center - self._lower_w / 2
        low_y = baseline + (self._op_h - self._op_baseline) + BIGOP_GAP
        self.lower_var.x = low_x
        self.lower_var.y = low_y
        self.lower_var.paint(painter, low_x, low_y)
        # festes „=" zwischen den beiden Slots
        lim_fs = self.font_size * BIGOP_LIMIT_SCALE
        painter.save()
        painter.setFont(_make_font(lim_fs))
        painter.setPen(QColor(C_TEXT))
        fm_lim = QFontMetricsF(_make_font(lim_fs))
        eq_x = low_x + self.lower_var.width
        eq_baseline = low_y + max(self.lower_var.ascent, fm_lim.ascent())
        painter.drawText(QPointF(eq_x, eq_baseline), "=")
        painter.restore()
        val_x = eq_x + self._eq_w
        self.lower_val.x = val_x
        self.lower_val.y = low_y
        self.lower_val.paint(painter, val_x, low_y)

        # Body rechts vom Operator-Block, auf gemeinsamer Baseline
        body_x = x + self._op_block_w + BIGOP_BODY_GAP
        body_y = baseline - self.body.ascent
        self.body.x = body_x
        self.body.y = body_y
        self.body.paint(painter, body_x, body_y)

    # -- Container-Interface --
    def slots(self) -> list[RowNode]:
        return [self.body, self.lower_var, self.lower_val, self.upper]

    def slot_above(self, row: RowNode) -> RowNode | None:
        if row is self.lower_var or row is self.lower_val:
            return self.body
        if row is self.body:
            return self.upper
        return None

    def slot_below(self, row: RowNode) -> RowNode | None:
        if row is self.upper:
            return self.body
        if row is self.body:
            return self.lower_var
        return None

    def first_slot(self) -> RowNode:
        return self.body

    def last_slot(self) -> RowNode:
        return self.body

    def horizontal_next(self, row: RowNode) -> RowNode | None:
        # Unter dem Σ steht "var = val" horizontal - → wechselt zwischen ihnen.
        if row is self.lower_var:
            return self.lower_val
        return None

    def horizontal_prev(self, row: RowNode) -> RowNode | None:
        if row is self.lower_val:
            return self.lower_var
        return None


class IntegralNode(MathNode):
    """Integral: ∫ mit unterer/oberer Grenze, Body und Differential-Slot.
    Rendering: `∫_lower^upper body d var`. Das „d" ist fester Text, `var`
    ist ein eigener Slot. Slot-Reihenfolge: [body, var, lower, upper]."""

    def __init__(self) -> None:
        super().__init__()
        self.body  = RowNode()
        self.var   = RowNode()
        self.lower = RowNode()
        self.upper = RowNode()
        for s in (self.body, self.var, self.lower, self.upper):
            s.parent = None
            s._container_parent = self   # type: ignore[attr-defined]
        self._op_w = 0.0
        self._op_h = 0.0
        self._op_baseline = 0.0
        self._d_w = 0.0       # Breite von „ d "
        self._limit_col_w = 0.0  # Breite der Grenzen-Spalte neben dem ∫

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        lim_fs = font_size * BIGOP_LIMIT_SCALE
        self.body.measure(font_size)
        self.var.measure(font_size)
        self.upper.measure(lim_fs)
        self.lower.measure(lim_fs)

        op_fs = font_size * INT_SIZE_FACTOR
        fm_op = QFontMetricsF(_make_font(op_fs))
        self._op_w = fm_op.horizontalAdvance("∫")
        self._op_h = fm_op.ascent() + fm_op.descent()
        self._op_baseline = fm_op.ascent()

        self._limit_col_w = max(self.upper.width, self.lower.width)

        fm = QFontMetricsF(_make_font(font_size))
        self._d_w = fm.horizontalAdvance(" d")

        self.width = (self._op_w + self._limit_col_w
                      + BIGOP_BODY_GAP + self.body.width
                      + self._d_w + self.var.width + 2.0)

        # vertikal: Grenzen ragen um (1 - INT_LIMIT_INTO_OP) ihrer Höhe aus
        # dem ∫-Zeichen heraus; der Rest sitzt im Zeichen drin.
        op_ascent_from_baseline  = self._op_baseline
        op_descent_from_baseline = self._op_h - self._op_baseline
        self.ascent  = max(self.body.ascent,
                           op_ascent_from_baseline
                           + self.upper.height * (1.0 - INT_LIMIT_INTO_OP))
        self.descent = max(self.body.descent,
                           op_descent_from_baseline
                           + self.lower.height * (1.0 - INT_LIMIT_INTO_OP))

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        baseline = y + self.ascent

        # ∫
        op_fs = self.font_size * INT_SIZE_FACTOR
        painter.save()
        painter.setFont(_make_font(op_fs))
        painter.setPen(QColor(C_TEXT))
        painter.drawText(QPointF(x, baseline), "∫")
        painter.restore()

        # Grenzen: obere sitzt oben rechts am ∫, untere unten rechts.
        # INT_LIMIT_INTO_OP = 0.2 heisst: 20% der Grenzhöhe sitzen im Zeichen,
        # 80% ragen darüber / darunter hinaus.
        limit_x = x + self._op_w * INT_LIMIT_X_OFFSET
        up_y = baseline - self._op_baseline \
               - self.upper.height * (1.0 - INT_LIMIT_INTO_OP)
        low_y = baseline + (self._op_h - self._op_baseline) \
                - self.lower.height * INT_LIMIT_INTO_OP
        self.upper.x = limit_x
        self.upper.y = up_y
        self.upper.paint(painter, limit_x, up_y)
        self.lower.x = limit_x
        self.lower.y = low_y
        self.lower.paint(painter, limit_x, low_y)

        # Body
        body_x = x + self._op_w + self._limit_col_w + BIGOP_BODY_GAP
        body_y = baseline - self.body.ascent
        self.body.x = body_x
        self.body.y = body_y
        self.body.paint(painter, body_x, body_y)

        # „ d"
        painter.save()
        painter.setFont(_make_font(self.font_size))
        painter.setPen(QColor(C_TEXT))
        d_x = body_x + self.body.width
        painter.drawText(QPointF(d_x, baseline), " d")
        painter.restore()

        # Variable
        var_x = d_x + self._d_w
        var_y = baseline - self.var.ascent
        self.var.x = var_x
        self.var.y = var_y
        self.var.paint(painter, var_x, var_y)

    # -- Container-Interface --
    def slots(self) -> list[RowNode]:
        return [self.body, self.var, self.lower, self.upper]

    def slot_above(self, row: RowNode) -> RowNode | None:
        if row is self.lower:
            return self.upper
        if row is self.body or row is self.var:
            return self.upper
        return None

    def slot_below(self, row: RowNode) -> RowNode | None:
        if row is self.upper:
            return self.lower
        if row is self.body or row is self.var:
            return self.lower
        return None

    def first_slot(self) -> RowNode:
        return self.body

    def last_slot(self) -> RowNode:
        return self.var

    def horizontal_next(self, row: RowNode) -> RowNode | None:
        # Neben dem Body steht " d var" - → springt über das " d" in var.
        if row is self.body:
            return self.var
        return None

    def horizontal_prev(self, row: RowNode) -> RowNode | None:
        if row is self.var:
            return self.body
        return None


class MatrixNode(MathNode):
    """Matrix bzw. Vektor (= 1-zeilige Matrix). Die Zellen sind in einem
    2D-Grid `cells[row][col]` organisiert. slots() liefert alle Zellen
    zeilenweise, das ist auch die Tab-Reihenfolge. Erweitert wird die
    Matrix via Tab (neue Spalte, wenn in letzter Zelle) oder Shift+Tab
    (neue Zeile, wenn in letzter Zelle) - das passiert im Editor."""

    def __init__(self, rows: int = 1, cols: int = 2) -> None:
        super().__init__()
        self.cells: list[list[RowNode]] = []
        for _ in range(rows):
            self.cells.append([self._make_cell() for _ in range(cols)])
        # Layout-Zwischenwerte, in measure() gefüllt
        self._col_widths: list[float] = []
        self._row_heights: list[float] = []   # ascent+descent je Zeile
        self._row_ascents: list[float] = []   # je Zeile (für baseline-align)
        self._content_w = 0.0
        self._content_h = 0.0

    def _make_cell(self) -> RowNode:
        cell = RowNode()
        cell.parent = None
        cell._container_parent = self   # type: ignore[attr-defined]
        return cell

    @property
    def n_rows(self) -> int:
        return len(self.cells)

    @property
    def n_cols(self) -> int:
        return len(self.cells[0]) if self.cells else 0

    def add_column(self) -> None:
        for row in self.cells:
            row.append(self._make_cell())

    def add_row(self) -> None:
        cols = self.n_cols
        self.cells.append([self._make_cell() for _ in range(cols)])

    def find_cell(self, row_node: RowNode) -> tuple[int, int] | None:
        for r, row in enumerate(self.cells):
            for c, cell in enumerate(row):
                if cell is row_node:
                    return r, c
        return None

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        for row in self.cells:
            for cell in row:
                cell.measure(font_size)

        # Spaltenbreiten = max. Breite jeder Spalte
        self._col_widths = []
        for c in range(self.n_cols):
            w = max((self.cells[r][c].width for r in range(self.n_rows)),
                    default=SLOT_MIN_W)
            self._col_widths.append(max(w, SLOT_MIN_W))
        # Zeilenhöhen analog
        self._row_heights = []
        self._row_ascents = []
        for r in range(self.n_rows):
            a = max((self.cells[r][c].ascent for c in range(self.n_cols)),
                    default=SLOT_MIN_H / 2)
            d = max((self.cells[r][c].descent for c in range(self.n_cols)),
                    default=SLOT_MIN_H / 2)
            self._row_ascents.append(a)
            self._row_heights.append(a + d)

        self._content_w = (sum(self._col_widths)
                           + MATRIX_COL_GAP * max(0, self.n_cols - 1))
        self._content_h = (sum(self._row_heights)
                           + MATRIX_ROW_GAP * max(0, self.n_rows - 1))

        self.width = (2 * MATRIX_BRACKET_W + 2 * MATRIX_PAD_X
                      + self._content_w)
        total_h = 2 * MATRIX_PAD_Y + self._content_h
        # Baseline vertikal zentriert
        self.ascent = total_h / 2
        self.descent = total_h - self.ascent

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        total_h = self.ascent + self.descent
        content_x = x + MATRIX_BRACKET_W + MATRIX_PAD_X
        content_y = y + MATRIX_PAD_Y

        # Klammern zeichnen (eckige Klammern mit oberen/unteren Hörnchen)
        painter.save()
        pen = QPen(QColor(C_TEXT))
        pen.setWidthF(max(1.0, self.font_size / 14.0))
        pen.setCapStyle(Qt.FlatCap)
        painter.setPen(pen)
        # linke Klammer
        lx = x + MATRIX_BRACKET_W
        painter.drawLine(QPointF(lx, y), QPointF(lx, y + total_h))
        painter.drawLine(QPointF(lx, y), QPointF(lx + MATRIX_BRACKET_W * 0.6, y))
        painter.drawLine(QPointF(lx, y + total_h),
                         QPointF(lx + MATRIX_BRACKET_W * 0.6, y + total_h))
        # rechte Klammer
        rx = x + self.width - MATRIX_BRACKET_W
        painter.drawLine(QPointF(rx, y), QPointF(rx, y + total_h))
        painter.drawLine(QPointF(rx, y), QPointF(rx - MATRIX_BRACKET_W * 0.6, y))
        painter.drawLine(QPointF(rx, y + total_h),
                         QPointF(rx - MATRIX_BRACKET_W * 0.6, y + total_h))
        painter.restore()

        # Zellen
        cy = content_y
        for r in range(self.n_rows):
            cx = content_x
            baseline = cy + self._row_ascents[r]
            for c in range(self.n_cols):
                cell = self.cells[r][c]
                # In der Spalte horizontal zentriert
                col_w = self._col_widths[c]
                cell_x = cx + (col_w - cell.width) / 2
                cell_y = baseline - cell.ascent
                cell.x = cell_x
                cell.y = cell_y
                cell.paint(painter, cell_x, cell_y)
                cx += col_w + MATRIX_COL_GAP
            cy += self._row_heights[r] + MATRIX_ROW_GAP

    # -- Container-Interface --
    def slots(self) -> list[RowNode]:
        out: list[RowNode] = []
        for row in self.cells:
            out.extend(row)
        return out

    def slot_above(self, row: RowNode) -> RowNode | None:
        pos = self.find_cell(row)
        if pos is None or pos[0] == 0:
            return None
        return self.cells[pos[0] - 1][pos[1]]

    def slot_below(self, row: RowNode) -> RowNode | None:
        pos = self.find_cell(row)
        if pos is None or pos[0] >= self.n_rows - 1:
            return None
        return self.cells[pos[0] + 1][pos[1]]

    def first_slot(self) -> RowNode:
        return self.cells[0][0]

    def last_slot(self) -> RowNode:
        return self.cells[-1][-1]

    def horizontal_next(self, row: RowNode) -> RowNode | None:
        pos = self.find_cell(row)
        if pos is None:
            return None
        r, c = pos
        if c + 1 < self.n_cols:
            return self.cells[r][c + 1]
        return None

    def horizontal_prev(self, row: RowNode) -> RowNode | None:
        pos = self.find_cell(row)
        if pos is None:
            return None
        r, c = pos
        if c > 0:
            return self.cells[r][c - 1]
        return None


class SystemNode(MathNode):
    """Gleichungssystem mit öffnender geschweifter Klammer.

    Jede Zeile ist ein eigener Ausdrucks-Slot. Zeilen werden via
    `Ctrl+Tab` oder `Tab` in der letzten Zeile angehängt, leere
    letzte Zeilen per `Backspace` entfernt. Serialisiert als reine
    Liste `[lhs1=rhs1, lhs2=rhs2, ...]` - der Nutzer wickelt selbst
    `solve(...)` drumherum; das `=` in den Zeilen wird anschliessend
    zu `Eq(...)`.
    """

    def __init__(self, rows: int = 2) -> None:
        super().__init__()
        self.rows: list[RowNode] = [self._make_row() for _ in range(rows)]
        self._row_heights: list[float] = []
        self._row_ascents: list[float] = []
        self._content_w: float = 0.0
        self._content_h: float = 0.0

    def _make_row(self) -> RowNode:
        row = RowNode()
        row.parent = None
        row._container_parent = self   # type: ignore[attr-defined]
        return row

    @property
    def n_rows(self) -> int:
        return len(self.rows)

    def add_row(self) -> None:
        self.rows.append(self._make_row())

    def find_row(self, row: RowNode) -> int | None:
        for i, r in enumerate(self.rows):
            if r is row:
                return i
        return None

    def measure(self, font_size: float) -> None:
        self.font_size = font_size
        for row in self.rows:
            row.measure(font_size)

        self._row_ascents = [max(r.ascent, SLOT_MIN_H / 2) for r in self.rows]
        self._row_heights = [
            self._row_ascents[i] + max(r.descent, SLOT_MIN_H / 2)
            for i, r in enumerate(self.rows)
        ]
        self._content_w = max(
            (max(r.width, SLOT_MIN_W) for r in self.rows), default=SLOT_MIN_W
        )
        self._content_h = (
            sum(self._row_heights)
            + SYSTEM_ROW_GAP * max(0, self.n_rows - 1)
        )

        self.width = SYSTEM_BRACE_W + SYSTEM_PAD_X + self._content_w
        total_h = 2 * SYSTEM_PAD_Y + self._content_h
        self.ascent = total_h / 2
        self.descent = total_h - self.ascent

    def paint(self, painter: QPainter, x: float, y: float) -> None:
        total_h = self.ascent + self.descent
        content_x = x + SYSTEM_BRACE_W + SYSTEM_PAD_X
        content_y = y + SYSTEM_PAD_Y

        # Geschweifte Klammer links per QPainterPath (zwei S-Kurven,
        # die in der Mitte am Spitz zusammenlaufen).
        painter.save()
        pen = QPen(QColor(C_TEXT))
        pen.setWidthF(max(1.1, self.font_size / 14.0))
        pen.setCapStyle(Qt.RoundCap)
        pen.setJoinStyle(Qt.RoundJoin)
        painter.setPen(pen)

        stem_x = x + SYSTEM_BRACE_W   # rechte Seite (Stamm der Klammer)
        tip_x = x                     # Spitze (links)
        top = y
        bot = y + total_h
        mid = y + total_h / 2

        path = QPainterPath()
        path.moveTo(stem_x, top)
        path.cubicTo(tip_x, top, stem_x, mid, tip_x, mid)
        path.cubicTo(stem_x, mid, tip_x, bot, stem_x, bot)
        painter.drawPath(path)
        painter.restore()

        # Zeilen links-bündig anordnen.
        cy = content_y
        for i, row in enumerate(self.rows):
            baseline = cy + self._row_ascents[i]
            row_x = content_x
            row_y = baseline - row.ascent
            row.x = row_x
            row.y = row_y
            row.paint(painter, row_x, row_y)
            cy += self._row_heights[i] + SYSTEM_ROW_GAP

    # -- Container-Interface --
    def slots(self) -> list[RowNode]:
        return list(self.rows)

    def slot_above(self, row: RowNode) -> RowNode | None:
        i = self.find_row(row)
        if i is None or i == 0:
            return None
        return self.rows[i - 1]

    def slot_below(self, row: RowNode) -> RowNode | None:
        i = self.find_row(row)
        if i is None or i >= self.n_rows - 1:
            return None
        return self.rows[i + 1]

    def first_slot(self) -> RowNode:
        return self.rows[0]

    def last_slot(self) -> RowNode:
        return self.rows[-1]


# ── Cursor ────────────────────────────────────────────────────────────────────
@dataclass
class Cursor:
    row: RowNode     # in welcher Row stehen wir
    index: int       # zwischen welchen Kindern (0..len(row.children))

    def clamp(self) -> None:
        self.index = max(0, min(self.index, len(self.row.children)))


# ── Utility ───────────────────────────────────────────────────────────────────
_font_cache: dict[int, QFont] = {}

def _make_font(pt: float) -> QFont:
    key = round(pt * 10)
    if key not in _font_cache:
        f = QFont()
        f.setFamilies(FONT_FAMILIES)   # Qt 5.13+ – echte Fallback-Liste statt CSS-String
        f.setPointSizeF(pt)
        _font_cache[key] = f
    return _font_cache[key]


def _container_of(row: RowNode) -> Optional["MathNode"]:
    """Gibt den Container-Node (FractionNode, SuperscriptNode, SqrtNode, …)
    zurück, dem dieser Slot gehört, oder None wenn `row` der Wurzel-Slot ist."""
    return getattr(row, "_container_parent", None)


def _find_enclosing_row(container: "MathNode") -> tuple[RowNode | None, int]:
    """Sucht die Row, in der dieser Container-Node als Kind hängt, +
    seinen Index darin. Funktioniert für jeden MathNode (Fraction,
    Superscript, Sqrt, …), der als Kind einer Row eingehängt ist."""
    row = container.parent
    if row is None:
        return None, -1
    try:
        idx = row.children.index(container)
    except ValueError:
        return None, -1
    return row, idx


def _index_closest_to_x(row: RowNode, target_x: float) -> int:
    """Findet in `row` den Cursor-Index, dessen absolute x-Position am
    nächsten an `target_x` liegt. Wird für vertikale Navigation benutzt,
    wenn der Ziel-Slot noch keine gespeicherte Position hat."""
    if not row.children:
        return 0
    best_idx = 0
    best_dist = abs((row.x + row.cursor_x_at(0)) - target_x)
    for i in range(1, len(row.children) + 1):
        d = abs((row.x + row.cursor_x_at(i)) - target_x)
        if d < best_dist:
            best_dist = d
            best_idx = i
    return best_idx


def _node_contains(node: MathNode, x: float, y: float) -> bool:
    """Liegt der Punkt (x,y) innerhalb des Bounding-Rechtecks des Nodes?"""
    return (node.x <= x <= node.x + node.width
            and node.y <= y <= node.y + node.height)


def _pick_in_row(row: RowNode, x: float, y: float) -> tuple[RowNode, int]:
    """Sucht rekursiv die beste (Slot, Index)-Position für den Klick (x,y).

    Wenn der Klick auf einem Container-Kind liegt, wird in dessen Slot
    abgestiegen. Sonst wird in der gegebenen Row der Index gewählt, dessen
    Cursor-x am nächsten am Klick liegt.
    """
    # Zuerst prüfen ob ein Container-Kind den Punkt enthält → reingehen.
    for child in row.children:
        if not isinstance(child, TextNode) and _node_contains(child, x, y):
            # Welcher Slot dieses Containers? Default: Bounding-Box-Test
            # über alle Slots, dann rekursiv.
            target_slot = _pick_slot_in_container(child, x, y)
            if target_slot is not None:
                return _pick_in_row(target_slot, x, y)
            # Fallback: vor dem Kind im aktuellen Row
            try:
                idx = row.children.index(child)
            except ValueError:
                idx = 0
            return row, idx

    # Kein Container-Treffer → Index in der aktuellen Row anhand x bestimmen.
    return row, _index_closest_to_x(row, x)


def _pick_slot_in_container(container: MathNode, x: float,
                            y: float) -> RowNode | None:
    """Wählt den Slot eines Containers, dessen Bounding-Box den Punkt
    enthält. Wenn keiner direkt trifft, den nächstliegenden (anhand
    Mittelpunkt-Distanz)."""
    if not hasattr(container, "slots") or not callable(getattr(container, "slots")):
        return None
    slots = container.slots()   # type: ignore[attr-defined]
    if not slots:
        return None
    # Direkter Treffer?
    for s in slots:
        if _node_contains(s, x, y):
            return s
    # Sonst: nächster Slot per Mittelpunkts-Distanz
    best = slots[0]
    bx = best.x + best.width / 2
    by = best.y + best.height / 2
    best_d2 = (bx - x) ** 2 + (by - y) ** 2
    for s in slots[1:]:
        sx = s.x + s.width / 2
        sy = s.y + s.height / 2
        d2 = (sx - x) ** 2 + (sy - y) ** 2
        if d2 < best_d2:
            best = s
            best_d2 = d2
    return best


# ── Ergebnis-Parser (2D-Darstellung) ─────────────────────────────────────────
# Token-Typen
_RT_NUM = 'N'    # Zahl
_RT_ID  = 'I'    # Bezeichner
_RT_DS  = 'DS'   # ** oder ^
_RT_US  = 'US'   # _  (Subscript)
_RT_ST  = 'S*'   # *
_RT_SL  = 'S/'   # /
_RT_PL  = 'P+'   # +
_RT_MI  = 'M-'   # -
_RT_LP  = '('
_RT_RP  = ')'
_RT_LB  = '['
_RT_RB  = ']'
_RT_CM  = ','
_RT_CE  = ':='
_RT_SP  = ' '    # Leerzeichen-Block
_RT_CH  = 'C'    # sonstiges Zeichen
_RT_EOF = '$'


def _lex_result(s: str) -> list:
    """Tokenisiert einen Ergebnis-String für den 2D-Parser."""
    toks: list = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if s[i:i+2] == '**':
            toks.append((_RT_DS, '**')); i += 2
        elif c == '^':
            toks.append((_RT_DS, '^')); i += 1
        elif s[i:i+2] == ':=':
            toks.append((_RT_CE, ':=')); i += 2
        elif c == '*':
            toks.append((_RT_ST, '*')); i += 1
        elif c == '/':
            toks.append((_RT_SL, '/')); i += 1
        elif c == '+':
            toks.append((_RT_PL, '+')); i += 1
        elif c == '-':
            toks.append((_RT_MI, '-')); i += 1
        elif c == '(':
            toks.append((_RT_LP, '(')); i += 1
        elif c == ')':
            toks.append((_RT_RP, ')')); i += 1
        elif c == '[':
            toks.append((_RT_LB, '[')); i += 1
        elif c == ']':
            toks.append((_RT_RB, ']')); i += 1
        elif c == ',':
            toks.append((_RT_CM, ',')); i += 1
        elif c == ' ':
            j = i
            while j < n and s[j] == ' ':
                j += 1
            toks.append((_RT_SP, s[i:j])); i = j
        elif c.isdigit() or (c == '.' and i + 1 < n and s[i + 1].isdigit()):
            j = i
            while j < n and (s[j].isdigit() or s[j] == '.'):
                j += 1
            toks.append((_RT_NUM, s[i:j])); i = j
        elif c == '_':
            toks.append((_RT_US, '_')); i += 1
        elif c.isalpha():
            j = i
            while j < n and s[j].isalnum():
                j += 1
            toks.append((_RT_ID, s[i:j])); i = j
        else:
            toks.append((_RT_CH, c)); i += 1
    toks.append((_RT_EOF, ''))
    return toks


class _ResultParser:
    """Recursive-Descent-Parser für SymPy-Ergebnis-Strings.

    Wandelt ``x**2 + 1/2`` oder ``sqrt(2)`` in einen 2D-MathNode-Baum um.
    """

    def __init__(self, tokens: list) -> None:
        self._t = tokens
        self._p = 0

    def _type(self) -> str:
        return self._t[self._p][0]

    def _val(self) -> str:
        return self._t[self._p][1]

    def _eat(self) -> tuple:
        tok = self._t[self._p]
        self._p += 1
        return tok

    def _eat_sp(self) -> list:
        nodes: list = []
        while self._type() == _RT_SP:
            for ch in self._val():
                nodes.append(TextNode(ch))
            self._eat()
        return nodes

    def _peek_past_sp(self) -> str:
        i = self._p
        while i < len(self._t) and self._t[i][0] == _RT_SP:
            i += 1
        return self._t[i][0] if i < len(self._t) else _RT_EOF

    def _parse_args_list(self, max_args: int = 16) -> list[list]:
        """Liest kommagetrennte Ausdrücke bis ')' oder EOF; Klammer schon offen."""
        args: list[list] = []
        first = True
        while self._type() not in (_RT_RP, _RT_EOF) and len(args) < max_args:
            if not first:
                if self._type() == _RT_CM:
                    self._eat()
                self._eat_sp()
            first = False
            args.append(self._parse_expr())
            self._eat_sp()
        if self._type() == _RT_RP:
            self._eat()
        return args

    def parse(self) -> RowNode:
        row = RowNode()
        # Zuweisung prüfen: IDENT SP? ':='
        saved = self._p
        if self._type() == _RT_ID:
            name = self._val()
            self._eat()
            sp1 = self._eat_sp()
            if self._type() == _RT_CE:
                self._eat()
                for ch in name:
                    row.append(TextNode(ch))
                for n in sp1:
                    row.append(n)
                row.append(TextNode(':'))
                row.append(TextNode('='))
                for n in self._eat_sp():
                    row.append(n)
                for n in self._parse_expr():
                    row.append(n)
                self._append_tail(row)
                return row
            else:
                self._p = saved

        for n in self._parse_expr():
            row.append(n)

        # Vergleichs-/Gleichheitsoperatoren: = ≈ ≤ ≥ ≠ < >
        # Mehrfach-Ketten erlaubt (a = b = c, a ≤ b < c …)
        _CMP_CHARS = {'=', '≈', '≤', '≥', '≠', '<', '>'}
        while True:
            sp = self._eat_sp()
            if self._type() == _RT_CH and self._val() in _CMP_CHARS:
                op_val = self._eat()[1]
                for n in sp:
                    row.append(n)
                row.append(TextNode(op_val))
                for n in self._eat_sp():
                    row.append(n)
                for n in self._parse_expr():
                    row.append(n)
            else:
                for n in sp:
                    row.append(n)
                break

        self._append_tail(row)
        return row

    def _append_tail(self, row: RowNode) -> None:
        while self._type() != _RT_EOF:
            v = self._eat()[1]
            for ch in v:
                if ch.isprintable():
                    row.append(TextNode(ch))

    def _parse_expr(self) -> list:
        """Summe: product (('+' | '-') product)*"""
        nodes = self._parse_product()
        while True:
            if self._type() == _RT_SP:
                if self._peek_past_sp() not in (_RT_PL, _RT_MI):
                    break
                sp = self._eat_sp()
                op = self._eat()
                sp2 = self._eat_sp()
                nodes.extend(sp)
                nodes.append(TextNode(op[1]))
                nodes.extend(sp2)
                nodes.extend(self._parse_product())
            elif self._type() in (_RT_PL, _RT_MI):
                op = self._eat()
                nodes.append(TextNode(op[1]))
                nodes.extend(self._eat_sp())
                nodes.extend(self._parse_product())
            else:
                break
        return nodes

    def _parse_product(self) -> list:
        """Produkt: power ('*' power | '/' power)*  – / erzeugt FractionNode."""
        left = self._parse_power()
        while True:
            # Leerzeichen vor * oder / überspringen (z.B. "R2 / R1")
            if self._type() == _RT_SP:
                if self._peek_past_sp() not in (_RT_ST, _RT_SL):
                    break
                self._eat_sp()
            if self._type() not in (_RT_ST, _RT_SL):
                break
            op = self._eat()[0]
            self._eat_sp()
            if op == _RT_ST:
                right = self._parse_power()
                left.append(TextNode('·'))
                left.extend(right)
            else:
                den = self._parse_power()
                while self._type() == _RT_ST:
                    self._eat()
                    self._eat_sp()
                    den.extend(self._parse_power())
                num_row = RowNode()
                for n in left:
                    num_row.append(n)
                den_row = RowNode()
                for n in den:
                    den_row.append(n)
                return [FractionNode(num_row, den_row)]
        return left

    def _parse_script_content(self) -> list:
        """Liest Sup/Subscript-Inhalt ohne Leerzeichen/Operatoren.

        Tokens werden direkt als Text übernommen (kein Funktionsaufruf),
        damit U_C(t) nicht das (t) ins Subscript zieht.
        Mehrere aufeinanderfolgende ID/NUM-Tokens werden zusammengefasst
        (z.B. '3dB' aus f_3dB).
        """
        nodes: list = []
        while self._type() in (_RT_ID, _RT_NUM):
            v = self._val()
            self._eat()
            nodes.extend(TextNode(c) for c in v)
        if not nodes:
            nodes = self._parse_unary()
        return nodes

    def _parse_power(self) -> list:
        """Potenz/Index: beliebige Kombination von ^ und _ in jeder Reihenfolge.

        Erlaubt: x^2, x_n, x^2_n, x_n^2, B_max^n usw.
        Nach Sub/Superscripts wird ein optionales (arg) konsumiert, damit
        Notationen wie U_C(t) oder H_3dB(f) korrekt rendern: das (t) bleibt
        normaler Text statt in _append_tail zu verschwinden.
        """
        base = self._parse_unary()
        while self._type() in (_RT_DS, _RT_US):
            if self._type() == _RT_DS:
                self._eat()
                self._eat_sp()
                exp_row = RowNode()
                for n in self._parse_script_content():
                    exp_row.append(n)
                base = base + [SuperscriptNode(exp_row)]
            else:
                self._eat()
                self._eat_sp()
                sub_row = RowNode()
                for n in self._parse_script_content():
                    sub_row.append(n)
                base = base + [SubscriptNode(sub_row)]
        # U_C(t), H_3dB(f) usw.: (arg) nach Sub/Superscript als Text anhängen
        if self._type() == _RT_LP:
            self._eat()
            base.append(TextNode('('))
            first = True
            while self._type() not in (_RT_RP, _RT_EOF):
                if not first:
                    if self._type() == _RT_CM:
                        self._eat()
                    base.append(TextNode(','))
                    base.extend(self._eat_sp())
                first = False
                base.extend(self._parse_expr())
            if self._type() == _RT_RP:
                self._eat()
            base.append(TextNode(')'))
        return base

    def _parse_unary(self) -> list:
        if self._type() == _RT_MI:
            self._eat()
            return [TextNode('-')] + self._parse_atom()
        return self._parse_atom()

    def _parse_atom(self) -> list:
        t = self._type()
        v = self._val()

        if t == _RT_NUM:
            self._eat()
            return [TextNode(c) for c in v]

        if t == _RT_ID:
            self._eat()
            if self._type() == _RT_LP:
                self._eat()
                if v == 'sqrt':
                    inner = self._parse_expr()
                    if self._type() == _RT_RP:
                        self._eat()
                    inner_row = RowNode()
                    for n in inner:
                        inner_row.append(n)
                    return [SqrtNode(inner_row)]
                if v in ('log', 'ln', 'lg'):
                    # log(arg)  oder  log(arg, base)
                    args = self._parse_args_list(2)
                    node = LogNode()
                    for n in (args[0] if args else []): node.argument.append(n)
                    if v == 'ln':
                        node.base.append(TextNode('e'))
                    elif v == 'lg':
                        node.base.append(TextNode('1'))
                        node.base.append(TextNode('0'))
                    elif len(args) > 1:
                        for n in args[1]: node.base.append(n)
                    return [node]
                if v == 'nthroot':
                    # nthroot(n, x)  →  NthRootNode mit index=n, inner=x
                    args = self._parse_args_list(2)
                    node = NthRootNode()
                    for n in args[0]: node.index.append(n)
                    for n in (args[1] if len(args) > 1 else []): node.inner.append(n)
                    return [node]
                if v == 'int':
                    # int(body, var, lower, upper)  →  IntegralNode
                    args = self._parse_args_list(4)
                    node = IntegralNode()
                    for n in (args[0] if len(args) > 0 else []): node.body.append(n)
                    for n in (args[1] if len(args) > 1 else []): node.var.append(n)
                    for n in (args[2] if len(args) > 2 else []): node.lower.append(n)
                    for n in (args[3] if len(args) > 3 else []): node.upper.append(n)
                    return [node]
                if v == 'sum':
                    # sum(body, var, lower, upper)  →  SumNode
                    args = self._parse_args_list(4)
                    node = SumNode()
                    for n in (args[0] if len(args) > 0 else []): node.body.append(n)
                    for n in (args[1] if len(args) > 1 else []): node.lower_var.append(n)
                    for n in (args[2] if len(args) > 2 else []): node.lower_val.append(n)
                    for n in (args[3] if len(args) > 3 else []): node.upper.append(n)
                    return [node]
                if v == 'vec':
                    # vec(a, b)  oder  vec(a, b, c)  →  Spaltenvektor
                    args = self._parse_args_list()
                    rows = max(len(args), 1)
                    node = MatrixNode(rows=rows, cols=1)
                    for i, arg in enumerate(args):
                        for n in arg: node.cells[i][0].append(n)
                    return [node]
                # Andere Funktionen: als Text + Klammern
                result: list = [TextNode(c) for c in v]
                result.append(TextNode('('))
                first = True
                while self._type() not in (_RT_RP, _RT_EOF):
                    if not first:
                        if self._type() == _RT_CM:
                            self._eat()
                        result.append(TextNode(','))
                        result.extend(self._eat_sp())
                    first = False
                    result.extend(self._parse_expr())
                if self._type() == _RT_RP:
                    self._eat()
                result.append(TextNode(')'))
                return result
            return [TextNode(c) for c in v]

        if t == _RT_LP:
            self._eat()
            nodes = self._parse_expr()
            if self._type() == _RT_RP:
                self._eat()
            return [TextNode('(')] + nodes + [TextNode(')')]

        if t == _RT_LB:
            self._eat()
            nodes = [TextNode('[')]
            first = True
            while self._type() not in (_RT_RB, _RT_EOF):
                if not first:
                    if self._type() == _RT_CM:
                        self._eat()
                    nodes.append(TextNode(','))
                    nodes.extend(self._eat_sp())
                first = False
                nodes.extend(self._parse_expr())
            if self._type() == _RT_RB:
                self._eat()
            nodes.append(TextNode(']'))
            return nodes

        if t == _RT_SP:
            return self._eat_sp()

        if t == _RT_CH:
            self._eat()
            return [TextNode(v)] if v.isprintable() else []

        if t != _RT_EOF:
            self._eat()
            return [TextNode(c) for c in v if c.isprintable()]
        return []


def _parse_result_to_row(text: str) -> RowNode:
    """Parst einen Ergebnis-String in einen 2D-MathNode-Baum."""
    try:
        tokens = _lex_result(text)
        parser = _ResultParser(tokens)
        return parser.parse()
    except Exception:
        row = RowNode()
        for ch in text:
            if ch.isprintable():
                row.append(TextNode(ch))
        return row


def _colorize_result_row(row: RowNode, color: str) -> None:
    """Setzt die Darstellungsfarbe aller Nodes im Ergebnis-Baum rekursiv."""
    for child in row.children:
        _colorize_result_node(child, color)


def _colorize_result_node(node: MathNode, color: str) -> None:
    if isinstance(node, TextNode):
        node.color = color
    elif isinstance(node, FractionNode):
        node.bar_color = color
        _colorize_result_row(node.numerator, color)
        _colorize_result_row(node.denominator, color)
    elif isinstance(node, SqrtNode):
        node.radical_color = color
        _colorize_result_row(node.inner, color)
    elif isinstance(node, NthRootNode):
        node.radical_color = color
        _colorize_result_row(node.inner, color)
        _colorize_result_row(node.index, color)
    elif isinstance(node, SuperscriptNode):
        _colorize_result_row(node.inner, color)
    elif isinstance(node, SubscriptNode):
        _colorize_result_row(node.inner, color)
    elif isinstance(node, RowNode):
        _colorize_result_row(node, color)


# ── SymPy → MathNode-Konverter ────────────────────────────────────────────────
# Wandelt einen SymPy-Ausdrucks-Baum direkt in MathNodes um, ohne den Umweg
# über einen String.  Wird von _build_result_row genutzt wenn die Engine einen
# rohen SymPy-Wert mitliefert.  Bei Ausdrücken mit Einheiten oder bei Fehlern
# fällt der Aufrufer auf den bestehenden Text-Parser zurück.

def _sy_row(nodes: list) -> RowNode:
    r = RowNode()
    for n in nodes:
        r.append(n)
    return r

def _sy_txt(s: str) -> list:
    return [TextNode(c) for c in s]

_SY_P_ADD = 1   # Additionsebene
_SY_P_MUL = 2   # Multiplikationsebene
_SY_P_POW = 3   # Potenzebene

def _sy_needs_paren(expr: Any, p: int) -> bool:
    """True wenn expr in Kontext p Klammern braucht."""
    if getattr(expr, 'is_Add', False): return p >= _SY_P_MUL
    if getattr(expr, 'is_Mul', False): return p >= _SY_P_MUL
    if getattr(expr, 'is_Pow', False): return p >= _SY_P_POW
    return False

_SY_CONST: dict[str, str] = {
    'Pi': 'π', 'Exp1': 'e', 'GoldenRatio': 'φ',
    'EulerGamma': 'γ', 'ImaginaryUnit': 'i',
    'Infinity': '∞', 'NegativeInfinity': '-∞',
    'ComplexInfinity': 'zoo', 'NaN': 'NaN',
    'Zero': '0', 'One': '1', 'NegativeOne': '-1', 'Half': '½',
}

_SY_FNAME: dict[str, str] = {
    'sin': 'sin', 'cos': 'cos', 'tan': 'tan',
    'cot': 'cot', 'sec': 'sec', 'csc': 'csc',
    'asin': 'arcsin', 'acos': 'arccos', 'atan': 'arctan',
    'acot': 'arccot', 'atan2': 'arctan2',
    'sinh': 'sinh', 'cosh': 'cosh', 'tanh': 'tanh',
    'asinh': 'arsinh', 'acosh': 'arcosh', 'atanh': 'artanh',
    're': 'Re', 'im': 'Im', 'conjugate': 'conj',
    'sign': 'sgn', 'ceiling': 'ceil', 'floor': 'floor',
    'binomial': 'C',
}


def _sy_nodes(expr: Any, sy: Any, p: int = 0) -> list:
    """Konvertiert einen SymPy-Ausdruck rekursiv in eine MathNode-Liste."""
    cls = type(expr).__name__

    # ── Spezielle Konstanten ─────────────────────────────────────────
    if cls in _SY_CONST:
        return _sy_txt(_SY_CONST[cls])

    # ── Zahlen ───────────────────────────────────────────────────────
    if isinstance(expr, sy.Integer):
        v = int(expr)
        nodes = _sy_txt(str(abs(v)))
        if v < 0:
            nodes = _sy_txt('-') + nodes
            if p >= _SY_P_MUL:
                return _sy_txt('(') + nodes + _sy_txt(')')
        return nodes

    if isinstance(expr, sy.Rational):
        pv, qv = int(expr.p), int(expr.q)
        if qv == 1:
            return _sy_nodes(sy.Integer(pv), sy, p)
        num_r = _sy_row(_sy_txt(str(abs(pv))))
        den_r = _sy_row(_sy_txt(str(qv)))
        frac  = FractionNode(num_r, den_r)
        return (_sy_txt('-') + [frac]) if pv < 0 else [frac]

    if isinstance(expr, sy.Float):
        return _sy_txt(str(float(expr)))

    # ── Symbol ───────────────────────────────────────────────────────
    if isinstance(expr, sy.Symbol):
        return _sy_txt(str(expr))

    # ── Gleichung ────────────────────────────────────────────────────
    if cls == 'Equality':
        return (_sy_nodes(expr.lhs, sy) + _sy_txt(' = ')
                + _sy_nodes(expr.rhs, sy))

    # ── Abs ──────────────────────────────────────────────────────────
    if cls == 'Abs':
        return _sy_txt('|') + _sy_nodes(expr.args[0], sy) + _sy_txt('|')

    # ── exp(x) → eˣ ─────────────────────────────────────────────────
    if cls == 'exp':
        return [TextNode('e'),
                SuperscriptNode(_sy_row(_sy_nodes(expr.args[0], sy)))]

    # ── sqrt ─────────────────────────────────────────────────────────
    if cls == 'sqrt':
        return [SqrtNode(_sy_row(_sy_nodes(expr.args[0], sy)))]

    # ── Pow ──────────────────────────────────────────────────────────
    if getattr(expr, 'is_Pow', False):
        base, exp = expr.args
        if exp == sy.Rational(1, 2):
            return [SqrtNode(_sy_row(_sy_nodes(base, sy)))]
        if isinstance(exp, sy.Rational) and exp.p == 1 and exp.q > 1:
            return [NthRootNode(_sy_row(_sy_nodes(base, sy)),
                                _sy_row(_sy_txt(str(exp.q))))]
        if exp == sy.Integer(-1):
            dn = _sy_nodes(base, sy, _SY_P_MUL)
            if _sy_needs_paren(base, _SY_P_MUL):
                dn = _sy_txt('(') + dn + _sy_txt(')')
            return [FractionNode(_sy_row(_sy_txt('1')), _sy_row(dn))]
        if getattr(exp, 'is_negative', False):
            pos = -exp
            bn = _sy_nodes(base, sy, _SY_P_POW)
            if _sy_needs_paren(base, _SY_P_POW):
                bn = _sy_txt('(') + bn + _sy_txt(')')
            en = _sy_nodes(pos, sy)
            return [FractionNode(_sy_row(_sy_txt('1')),
                                 _sy_row(bn + [SuperscriptNode(_sy_row(en))]))]
        bn = _sy_nodes(base, sy, _SY_P_POW)
        if _sy_needs_paren(base, _SY_P_POW):
            bn = _sy_txt('(') + bn + _sy_txt(')')
        en = _sy_nodes(exp, sy)
        result = bn + [SuperscriptNode(_sy_row(en))]
        return (_sy_txt('(') + result + _sy_txt(')')) if p >= _SY_P_POW else result

    # ── Mul ──────────────────────────────────────────────────────────
    if getattr(expr, 'is_Mul', False):
        return _sy_mul(expr, sy, p)

    # ── Add ──────────────────────────────────────────────────────────
    if getattr(expr, 'is_Add', False):
        nodes = _sy_add(expr, sy)
        if p >= _SY_P_MUL and len(expr.args) > 1:
            return _sy_txt('(') + nodes + _sy_txt(')')
        return nodes

    # ── Listen / Tupel (z. B. von solve()) ───────────────────────────
    if isinstance(expr, (list, tuple)):
        ob, cb = ('[', ']') if isinstance(expr, list) else ('(', ')')
        nodes = _sy_txt(ob)
        for i, item in enumerate(expr):
            if i > 0:
                nodes += _sy_txt(', ')
            nodes += _sy_nodes(item, sy)
        return nodes + _sy_txt(cb)

    if isinstance(expr, dict):
        nodes = _sy_txt('{')
        for i, (k, v) in enumerate(expr.items()):
            if i > 0:
                nodes += _sy_txt(', ')
            nodes += _sy_nodes(k, sy) + _sy_txt(': ') + _sy_nodes(v, sy)
        return nodes + _sy_txt('}')

    # ── log mit Basis ─────────────────────────────────────────────────
    if cls == 'log' and len(expr.args) == 2:
        an = _sy_nodes(expr.args[0], sy)
        bn = _sy_nodes(expr.args[1], sy)
        return (_sy_txt('log') + [SubscriptNode(_sy_row(bn))]
                + _sy_txt('(') + an + _sy_txt(')'))

    # ── Fakultät ─────────────────────────────────────────────────────
    if cls == 'factorial':
        arg = expr.args[0]
        an = _sy_nodes(arg, sy, _SY_P_POW)
        if _sy_needs_paren(arg, _SY_P_POW):
            an = _sy_txt('(') + an + _sy_txt(')')
        return an + _sy_txt('!')

    # ── Bekannte Funktionen ───────────────────────────────────────────
    fname = _SY_FNAME.get(cls, cls)
    if expr.args:
        nodes = _sy_txt(fname) + _sy_txt('(')
        for i, arg in enumerate(expr.args):
            if i > 0:
                nodes += _sy_txt(', ')
            nodes += _sy_nodes(arg, sy)
        return nodes + _sy_txt(')')

    return _sy_txt(str(expr))


def _sy_sign(expr: Any, sy: Any) -> tuple:
    """Gibt (is_negative, betrag_expr) zurück."""
    if getattr(expr, 'is_Mul', False):
        args = list(expr.args)
        if sy.Integer(-1) in args:
            rest = [a for a in args if a != sy.Integer(-1)]
            return True, (rest[0] if len(rest) == 1 else sy.Mul(*rest))
        for a in args:
            if isinstance(a, sy.Number) and a < 0:
                rest = [x for x in args if x is not a]
                pos  = sy.Mul(*([(-a)] + rest)) if rest else -a
                return True, pos
    if isinstance(expr, sy.Number) and expr < 0:
        return True, -expr
    return False, expr


def _sy_add(expr: Any, sy: Any) -> list:
    nodes: list = []
    for i, term in enumerate(expr.args):
        neg, pos = _sy_sign(term, sy)
        if i == 0:
            if neg:
                nodes += _sy_txt('-')
            nodes += _sy_nodes(pos if neg else term, sy, _SY_P_ADD)
        else:
            nodes += _sy_txt(' - ' if neg else ' + ')
            nodes += _sy_nodes(pos, sy, _SY_P_ADD)
    return nodes


def _sy_product(factors: list, sy: Any) -> list:
    nodes: list = []
    for i, f in enumerate(factors):
        if i > 0:
            prev = factors[i - 1]
            # Kein · zwischen Zahl und Symbol (2x statt 2·x)
            if not (isinstance(prev, sy.Number) and isinstance(f, sy.Symbol)):
                nodes += _sy_txt('·')
        fn = _sy_nodes(f, sy, _SY_P_MUL)
        if _sy_needs_paren(f, _SY_P_MUL):
            fn = _sy_txt('(') + fn + _sy_txt(')')
        nodes += fn
    return nodes or _sy_txt('1')


def _sy_mul(expr: Any, sy: Any, p: int) -> list:
    num_f: list = []
    den_f: list = []
    sign_neg = False

    for factor in expr.args:
        if factor == sy.Integer(-1):
            sign_neg = not sign_neg
        elif (getattr(factor, 'is_Pow', False)
              and getattr(factor.args[1], 'is_negative', False)):
            b, e = factor.args
            pos_e = -e
            den_f.append(b if pos_e == sy.Integer(1) else sy.Pow(b, pos_e))
        elif isinstance(factor, sy.Rational) and int(factor.p) < 0:
            sign_neg = not sign_neg
            num_f.append(sy.Rational(-int(factor.p), int(factor.q)))
        else:
            num_f.append(factor)

    if den_f:
        num_n = (_sy_nodes(num_f[0], sy, _SY_P_MUL) if len(num_f) == 1
                 else _sy_product(num_f, sy)) if num_f else _sy_txt('1')
        den_n = (_sy_nodes(den_f[0], sy, _SY_P_MUL) if len(den_f) == 1
                 else _sy_product(den_f, sy))
        frac   = FractionNode(_sy_row(num_n), _sy_row(den_n))
        result = (_sy_txt('-') + [frac]) if sign_neg else [frac]
        return (_sy_txt('(') + result + _sy_txt(')')) if p >= _SY_P_MUL else result

    prod   = _sy_product(num_f, sy)
    result = (_sy_txt('-') + prod) if sign_neg else prod
    if p >= _SY_P_MUL and (sign_neg or len(num_f) > 1):
        return _sy_txt('(') + result + _sy_txt(')')
    return result


def _sy_has_units(expr: Any) -> bool:
    """True wenn der Ausdruck SymPy-Einheiten enthält."""
    try:
        from sympy.physics.units import Quantity
        return bool(getattr(expr, 'atoms', lambda *_: set())(Quantity))
    except Exception:
        return False


def _sympy_to_result_row(text: str, raw_expr: Any, sy: Any) -> RowNode:
    """Baut einen Ergebnis-RowNode aus rohem SymPy-Ausdruck + Text-Prefix.

    Prefix ('var := ') wird aus dem Text-String extrahiert und als plain
    TextNodes vorangestellt, damit Variablennamen korrekt dargestellt werden.
    Den eigentlichen Wert wandelt der SymPy-Renderer in 2D-MathNodes um.
    Falls der Text ein '≈'-Näherungswert enthält, wird der Dezimalanteil
    als Klartext angefügt.
    """
    row = RowNode()
    prefix = ''
    main   = text
    if ' := ' in text:
        idx    = text.index(' := ')
        prefix = text[:idx + 4]   # 'var := '
        main   = text[idx + 4:]
    for ch in prefix:
        row.append(TextNode(ch))

    for node in _sympy_expr_to_row(raw_expr, sy).children:
        row.append(node)

    # Näherungswert ('≈ 1.414') aus Text anhängen falls vorhanden
    if '  ≈  ' in main:
        approx_suffix = main[main.index('  ≈  '):]
        for ch in approx_suffix:
            row.append(TextNode(ch))
    return row


def _sympy_expr_to_row(expr: Any, sy: Any) -> RowNode:
    """Einstiegspunkt: SymPy-Ausdruck → RowNode."""
    return _sy_row(_sy_nodes(expr, sy))


# ── Widget ────────────────────────────────────────────────────────────────────
class MathEditor(QWidget):
    """Das eigentliche Editor-Widget. Hält einen Root-RowNode und einen
    Cursor. Bei jeder Änderung wird neu vermessen und neu gezeichnet."""

    PADDING = 16.0   # Innenabstand zum Widget-Rand

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setMinimumHeight(120)

        # Multi-Line: jede Zeile ist eine eigene Top-Level-RowNode.
        # Die Zeilen werden vertikal gestapelt gezeichnet.
        self.lines: list[RowNode] = [RowNode()]
        # Ergebnisse pro Zeile: (text, is_error). ("", False) = kein Ergebnis.
        self.results: list[tuple[str, bool]] = [("", False)]
        # Navigierbare RowNodes für Ergebnisse (parallel zu results).
        # None = kein Ergebnis in dieser Zeile.
        self.result_rows: list[RowNode | None] = [None]
        self.cursor: Cursor = Cursor(self.lines[0], 0)

        # Cursor-Blinken
        self._cursor_visible: bool = True
        self._blink: QTimer = QTimer(self)
        self._blink.setInterval(530)
        self._blink.timeout.connect(self._toggle_cursor)
        self._blink.start()

        # Strukturierter Backspace: Container-Nodes werden erst markiert,
        # beim zweiten Backspace gelöscht. Jede andere Taste hebt es auf.
        self._marked_node: MathNode | None = None
        self._mark_border: QColor = QColor("#3b82f6")
        self._mark_fill: QColor = QColor(59, 130, 246, 45)

        # Textauswahl: Anker-Position (Row, Index) oder None wenn keine Auswahl.
        self._sel_anchor: tuple[RowNode, int] | None = None

        # Undo/Redo-Historie (deep-copy-Snapshots, max. 100 Eintraege).
        # deque(maxlen=100): das aelteste Element faellt automatisch raus — O(1).
        self._undo_stack: deque[dict] = deque(maxlen=100)
        self._redo_stack: deque[dict] = deque(maxlen=100)

        # Engine-Anbindung
        self._engine: Any = None
        self._dirty: bool = True     # True = irgendeine Zeile wurde geaendert
        self._content_w: int = 0
        self._content_h: int = 0

        self._relayout()

    # ── Public API ────────────────────────────────────────────────────────
    def set_engine(self, engine: Any) -> None:
        """Setzt die Engine-Referenz."""
        self._engine = engine

    def to_plain_text(self) -> str:
        """Alle Zeilen mit Newline getrennt serialisiert. Primär für Debug."""
        return "\n".join(_serialize_row(line) for line in self.lines)

    def clear(self) -> None:
        """Setzt den Editor vollstaendig auf einen leeren Zustand zurueck."""
        self.lines = [RowNode()]
        self.results = [("", False)]
        self.result_rows = [None]
        self.cursor = Cursor(self.lines[0], 0)
        self._marked_node = None
        self._sel_anchor = None
        self._dirty = True
        self._relayout()

    def insert_formula(self, formula: str) -> None:
        """Haengt eine neue Zeile an und traegt die Formel dort ein."""
        # Nur eine neue Zeile anhaengen, wenn die letzte nicht leer ist.
        last = self.lines[-1]
        if len(last.children) > 0:
            self.lines.append(RowNode())
            self.results.append(("", False))
            self.result_rows.append(None)
        new_line = self.lines[-1]
        self.cursor.row = new_line
        self.cursor.index = 0
        for ch in formula.strip():
            if ch.isprintable():
                node = TextNode(ch)
                new_line.insert(self.cursor.index, node)
                self.cursor.index += 1
        self._mark_dirty()
        self._relayout()
        self.setFocus()

    # ── Interne Helfer für Multi-Line ─────────────────────────────────────
    def _is_top_level_row(self, row: RowNode) -> bool:
        """True wenn row eine der Top-Level-Zeilen ist."""
        return row in self.lines

    def _top_line_index(self) -> int:
        """Index der Top-Level-Zeile, in der der Cursor aktuell steht
        (auch wenn er in einem verschachtelten Container sitzt)."""
        row = self.cursor.row
        # Solange row nicht in self.lines ist, eine Ebene hoch.
        while row is not None and row not in self.lines:
            container = _container_of(row)
            if container is None:
                return -1
            outer, _ = _find_enclosing_row(container)
            if outer is None:
                return -1
            row = outer
        if row is None:
            return -1
        try:
            return self.lines.index(row)
        except ValueError:
            return -1

    def _line_is_comment(self, line: RowNode) -> bool:
        """True wenn die Zeile mit # beginnt."""
        if not line.children:
            return False
        first = line.children[0]
        return isinstance(first, TextNode) and first.char == "#"

    # ── Ergebnis-Zeilen-Hilfsmethoden ────────────────────────────────────
    def _is_in_result_row(self) -> bool:
        """True, wenn der Cursor sich in einer (schreibgeschützten) Ergebnis-Row befindet."""
        return any(r is self.cursor.row for r in self.result_rows if r is not None)

    def _result_row_line_index(self) -> int | None:
        """Gibt den Zeilen-Index zurück, dessen Ergebnis-Row der Cursor enthält, oder None."""
        for i, r in enumerate(self.result_rows):
            if r is not None and r is self.cursor.row:
                return i
        return None

    # ── Textauswahl ───────────────────────────────────────────────────────
    def _has_selection(self) -> bool:
        """True wenn es eine aktive Auswahl im aktuellen Row gibt."""
        return (
            self._sel_anchor is not None
            and self._sel_anchor[0] is self.cursor.row
            and self._sel_anchor[1] != self.cursor.index
        )

    def _sel_range(self) -> tuple[RowNode, int, int] | None:
        """Gibt (row, start, end) der aktuellen Auswahl zurück oder None."""
        if not self._has_selection():
            return None
        _, anchor_idx = self._sel_anchor  # type: ignore[misc]
        start = min(anchor_idx, self.cursor.index)
        end = max(anchor_idx, self.cursor.index)
        return (self.cursor.row, start, end)

    def _clear_selection(self) -> None:
        self._sel_anchor = None

    # ── Undo / Redo ───────────────────────────────────────────────────────
    def _snapshot(self) -> dict:
        """Erstellt einen tiefen Klon des aktuellen Editor-Zustands."""
        row_idx = self._top_line_index()
        return {
            "lines":        copy.deepcopy(self.lines),
            "results":      list(self.results),
            "result_rows":  list(self.result_rows),
            "row_idx":      max(row_idx, 0),
            "col_idx":      self.cursor.index,
        }

    def _push_undo(self) -> None:
        """Speichert den aktuellen Zustand auf dem Undo-Stack."""
        self._undo_stack.append(self._snapshot())
        self._redo_stack.clear()

    def _restore_snapshot(self, snap: dict) -> None:
        self.lines        = snap["lines"]
        self.results      = snap["results"]
        self.result_rows  = snap["result_rows"]
        row_idx = snap["row_idx"]
        if 0 <= row_idx < len(self.lines):
            self.cursor.row   = self.lines[row_idx]
            self.cursor.index = min(snap["col_idx"], len(self.cursor.row.children))
        else:
            self.cursor.row   = self.lines[-1]
            self.cursor.index = len(self.cursor.row.children)
        self._marked_node = None
        self._sel_anchor  = None
        self._relayout()

    def _undo(self) -> None:
        if not self._undo_stack:
            return
        self._redo_stack.append(self._snapshot())
        self._restore_snapshot(self._undo_stack.pop())

    def _redo(self) -> None:
        if not self._redo_stack:
            return
        self._undo_stack.append(self._snapshot())
        self._restore_snapshot(self._redo_stack.pop())

    # ── Zwischenablage ────────────────────────────────────────────────────
    def _copy(self) -> None:
        """Kopiert die Auswahl (oder die gesamte Zeile + Ergebnis) in die Zwischenablage."""
        sel = self._sel_range()
        if sel:
            row, start, end = sel
            tmp = RowNode()
            tmp.children = list(row.children[start:end])
            text = _serialize_row(tmp)
        elif self._is_in_result_row():
            # Cursor im Ergebnis-Bereich → nur den Ergebnis-Text kopieren.
            i = self._result_row_line_index()
            if i is None:
                return
            text = self.results[i][0] if i < len(self.results) else ""
        else:
            i = self._top_line_index()
            if i < 0:
                return
            text = _serialize_row(self.lines[i])
            result = self.results[i][0] if i < len(self.results) else ""
            if result:
                text = text + "  =  " + result
        QApplication.clipboard().setText(text)

    def _cut(self) -> None:
        """Ausschneiden: Inhalt kopieren und löschen."""
        self._copy()
        if self._is_in_result_row():
            return
        if self._has_selection():
            self._delete_selection()
        else:
            i = self._top_line_index()
            if 0 <= i < len(self.lines):
                row = self.lines[i]
                while row.children:
                    row.pop(0)
                self.cursor.row   = row
                self.cursor.index = 0
                self._mark_dirty()
                self._relayout()

    def _paste(self) -> None:
        """Fügt Text aus der Zwischenablage ein (zeichenweise als TextNodes)."""
        if self._is_in_result_row():
            return
        text = QApplication.clipboard().text()
        if not text:
            return
        lines = text.split("\n")
        for idx, part in enumerate(lines):
            for ch in part:
                if ch.isprintable():
                    self._insert_text(ch)
            if idx < len(lines) - 1:
                i = self._top_line_index()
                if 0 <= i and i + 1 < len(self.lines):
                    self.cursor.row   = self.lines[i + 1]
                    self.cursor.index = 0
                else:
                    self._new_line_below_current()

    def _delete_selection(self) -> bool:
        """Löscht ausgewählte Zeichen. Gibt True zurück wenn Auswahl existierte."""
        sel = self._sel_range()
        if sel is None:
            return False
        if self._is_in_result_row():
            self._sel_anchor = None
            return True
        row, start, end = sel
        for _ in range(end - start):
            row.pop(start)
        self.cursor.index = start
        self._sel_anchor = None
        self._mark_dirty()
        self._invalidate_slot_memory()
        return True

    def _sel_extend_left(self) -> None:
        """Auswahl um eine Position nach links erweitern (Shift+Left)."""
        if self._sel_anchor is None or self._sel_anchor[0] is not self.cursor.row:
            self._sel_anchor = (self.cursor.row, self.cursor.index)
        if self.cursor.index > 0:
            self.cursor.index -= 1
        self._invalidate_slot_memory()
        self._relayout()

    def _sel_extend_right(self) -> None:
        """Auswahl um eine Position nach rechts erweitern (Shift+Right)."""
        if self._sel_anchor is None or self._sel_anchor[0] is not self.cursor.row:
            self._sel_anchor = (self.cursor.row, self.cursor.index)
        if self.cursor.index < len(self.cursor.row.children):
            self.cursor.index += 1
        self._invalidate_slot_memory()
        self._relayout()

    @staticmethod
    def _build_result_row(
        text: str,
        is_error: bool = False,
        raw_expr: Any = None,
        sy: Any = None,
    ) -> RowNode:
        """Baut den Ergebnis-RowNode.

        Wenn ein roher SymPy-Wert verfügbar ist (und keine Einheiten enthält),
        wird der SymPy-Renderer verwendet; sonst fällt die Methode auf den
        Text-Parser zurück.
        """
        color = C_RES_ERR if is_error else C_RES_OK
        if not is_error and raw_expr is not None and sy is not None:
            try:
                if not _sy_has_units(raw_expr):
                    row = _sympy_to_result_row(text, raw_expr, sy)
                    _colorize_result_row(row, color)
                    return row
            except Exception:
                pass  # Fallback auf Text-Parser
        row = _parse_result_to_row(text)
        _colorize_result_row(row, color)
        return row

    # ── Ergebnis löschen ─────────────────────────────────────────────────
    def _clear_result(self, line_idx: int) -> None:
        """Löscht das Ergebnis der angegebenen Zeile und setzt den Cursor
        ans Ende der Ausdrucks-Zeile."""
        if line_idx < 0 or line_idx >= len(self.results):
            return
        self.results[line_idx] = ("", False)
        if line_idx < len(self.result_rows):
            self.result_rows[line_idx] = None
        self.cursor.row = self.lines[line_idx]
        self.cursor.index = len(self.lines[line_idx].children)
        self._invalidate_slot_memory()
        self._relayout()

    # ── Engine-Auswertung ─────────────────────────────────────────────────
    def _mark_dirty(self) -> None:
        """Markiert die aktuelle Zeile als geändert → ihr Ergebnis verschwindet."""
        i = self._top_line_index()
        if i >= 0 and i < len(self.results):
            if self.results[i] != ("", False) or (
                i < len(self.result_rows) and self.result_rows[i] is not None
            ):
                self.results[i] = ("", False)
                if i < len(self.result_rows):
                    self.result_rows[i] = None
                self._dirty = True

    def _evaluate(self, approx_current: bool = False) -> None:
        """Serialisiert alle Zeilen, gruppiert mehrzeilige Ausdrücke (offene
        Klammern) und schickt sie gemeinsam an die Engine.

        Wird `approx_current=True` gesetzt (per Ctrl+Enter), wird die
        Gruppe der aktuellen Zeile numerisch ausgewertet (force_approx).
        """
        if self._engine is None:
            return
        texts = [_serialize_row(line) for line in self.lines]
        n = len(texts)

        groups, line_to_group = _group_by_brackets(texts)
        engine_texts = [gt for gt, _ in groups]

        force: set | None = None
        if approx_current:
            cur_i = self._top_line_index()
            if cur_i >= 0 and cur_i in line_to_group:
                force = {line_to_group[cur_i]}

        raw_exprs: dict[int, Any] = {}   # line_idx → roher SymPy-Wert
        try:
            group_results = self._engine.evaluate_all(
                engine_texts, force_approx=force
            )
            while len(group_results) < len(groups):
                group_results.append(("", False, None))

            # Ergebnis auf die LETZTE Zeile der jeweiligen Gruppe setzen;
            # alle anderen Gruppenzeilen bleiben leer.
            self.results = [("", False)] * n
            for gi, (_, idxs) in enumerate(groups):
                if idxs and gi < len(group_results):
                    gr = group_results[gi]
                    text, is_err = gr[0], gr[1]
                    raw = gr[2] if len(gr) > 2 else None
                    self.results[idxs[-1]] = (text, is_err)
                    if raw is not None:
                        raw_exprs[idxs[-1]] = raw
        except Exception as e:
            self.results = [(str(e), True) for _ in self.lines]

        # Navigierbare Ergebnis-Rows aufbauen.
        sy = getattr(self._engine, "sy", None)
        self.result_rows = [None] * n
        for i, (res_text, is_err) in enumerate(self.results):
            if res_text:
                raw = raw_exprs.get(i)
                self.result_rows[i] = self._build_result_row(res_text, is_err, raw, sy)

        self._dirty = False
        self._relayout()

    # -- Paint ---------------------------------------------------------------
    def paintEvent(self, _event) -> None:
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, True)
        p.setRenderHint(QPainter.TextAntialiasing, True)

        # Alle Zeilen + ihre Ergebnisse zeichnen.
        for i, line in enumerate(self.lines):
            # x/y wurden im _relayout gesetzt.
            is_comment = self._line_is_comment(line)
            if is_comment:
                self._paint_line_comment(p, line)
            else:
                line.paint(p, line.x, line.y)
            # Slot-Outlines dieser Zeile
            self._paint_slot_outlines(p, line)
            # Ergebnis nach ▶ (als 2D-Node-Baum)
            rrow = self.result_rows[i] if i < len(self.result_rows) else None
            if rrow is not None and not is_comment:
                # Separator ▶
                baseline = rrow.y + rrow.ascent
                sep_x = line.x + line.width + 4
                p.save()
                p.setFont(_make_font(FONT_SIZE_PT))
                p.setPen(QColor(C_SEP))
                p.drawText(QPointF(sep_x, baseline), SEP_TEXT)
                p.restore()
                # Ergebnis-Node malen (Farbe ist bereits in den Nodes gesetzt)
                rrow.paint(p, rrow.x, rrow.y)

        # Markierten Node (strukturierter Backspace) umranden
        if self._marked_node is not None:
            n = self._marked_node
            p.save()
            p.setBrush(self._mark_fill)
            pen = QPen(self._mark_border)
            pen.setWidthF(1.5)
            p.setPen(pen)
            p.drawRect(QRectF(n.x - 1, n.y - 1, n.width + 2, n.height + 2))
            p.restore()

        # Textauswahl
        sel = self._sel_range()
        if sel is not None:
            self._paint_selection(p, *sel)

        # Cursor
        if self._cursor_visible and self.hasFocus():
            self._paint_cursor(p)

        p.end()

    def _paint_line_comment(self, p: QPainter, line: RowNode) -> None:
        """Kommentar-Zeile (beginnt mit #): komplett grau zeichnen."""
        # Einfach: alle Kinder als grauen Text zeichnen, wir umgehen die
        # normale Paint-Kaskade der Nodes, weil wir nur Text erwarten.
        p.save()
        font = _make_font(FONT_SIZE_PT)
        p.setFont(font)
        p.setPen(QColor(C_COMMENT))
        fm = QFontMetricsF(font)
        baseline = line.y + fm.ascent()
        # Sequenziell: TextNode-Zeichen raus, alles andere via normalem paint
        # in grau ist nicht trivial - für jetzt: Text-Kinder grau zeichnen,
        # Nicht-Text-Kinder fallen zurück auf ihr normales paint.
        cx = line.x
        for c in line.children:
            if isinstance(c, TextNode):
                p.drawText(QPointF(cx, baseline), c.char)
                cx += fm.horizontalAdvance(c.char)
            else:
                # struktureller Node in Kommentar - einfach normal zeichnen
                top = baseline - c.ascent
                c.x = cx
                c.y = top
                c.paint(p, cx, top)
                cx += c.width
        p.restore()

    def _paint_slot_outlines(self, p: QPainter, row: RowNode) -> None:
        # Slot einer RowNode, die zu einem Container gehört: wenn leer oder
        # Cursor drin, gestrichelten Rahmen zeichnen.
        container = _container_of(row)
        if container is not None:
            has_cursor = (self.cursor.row is row)
            empty = len(row.children) == 0
            if empty or has_cursor:
                color = QColor(C_SLOT_FOCUS if has_cursor else C_SLOT_EMPTY)
                pen = QPen(color)
                pen.setStyle(Qt.DashLine)
                pen.setWidthF(1.0)
                p.save()
                p.setPen(pen)
                w = max(row.width, SLOT_MIN_W)
                h = max(row.height, SLOT_MIN_H)
                p.drawRect(QRectF(row.x - 1, row.y - 1, w + 2, h + 2))
                p.restore()

        for c in row.children:
            if hasattr(c, "slots") and callable(getattr(c, "slots")):
                for s in c.slots():   # type: ignore[attr-defined]
                    self._paint_slot_outlines(p, s)

    def _paint_cursor(self, p: QPainter) -> None:
        row = self.cursor.row
        bx = row.x + row.cursor_x_at(self.cursor.index)
        by = row.y
        bh = max(row.height, SLOT_MIN_H)
        # Schreibgeschützte Ergebnis-Zeile: grauer Cursor
        color = QColor(C_SLOT_EMPTY) if self._is_in_result_row() else QColor(C_CURSOR)
        pen = QPen(color)
        pen.setWidthF(1.5)
        p.save()
        p.setPen(pen)
        p.drawLine(QPointF(bx, by), QPointF(bx, by + bh))
        p.restore()

    def _paint_selection(self, p: QPainter, row: RowNode, start: int, end: int) -> None:
        x0 = row.x + row.cursor_x_at(start)
        x1 = row.x + row.cursor_x_at(end)
        y = row.y
        h = max(row.height, SLOT_MIN_H)
        p.save()
        p.setPen(Qt.NoPen)
        p.setBrush(QColor(59, 130, 246, 70))
        p.drawRect(QRectF(x0, y, x1 - x0, h))
        p.restore()

    def _toggle_cursor(self) -> None:
        self._cursor_visible = not self._cursor_visible
        self.update()

    def _wake_cursor(self) -> None:
        self._cursor_visible = True
        self._blink.start()

    # ── Layout ────────────────────────────────────────────────────────────
    def _relayout(self) -> None:
        fm = QFontMetricsF(_make_font(FONT_SIZE_PT))
        sep_w = fm.horizontalAdvance(SEP_TEXT)

        # Alle Zeilen und Ergebnis-Rows vermessen.
        for line in self.lines:
            line.measure(FONT_SIZE_PT)
        while len(self.result_rows) < len(self.lines):
            self.result_rows.append(None)
        for rrow in self.result_rows:
            if rrow is not None:
                rrow.measure(FONT_SIZE_PT)

        # Vertikal stapeln; Breite = maximales (expr + ggf. Ergebnis)
        y = self.PADDING
        max_w = 0.0
        for i, line in enumerate(self.lines):
            line.x = self.PADDING
            line.y = y

            rrow = self.result_rows[i] if i < len(self.result_rows) else None
            if rrow is not None:
                # Baseline-Ausrichtung: Ergebnis auf gleiche Baseline wie Ausdruck.
                baseline = line.y + line.ascent
                rrow.x = line.x + line.width + 4 + sep_w
                rrow.y = baseline - rrow.ascent
                # Effektive Höhe: Ausdruck + Ergebnis, ab line.y gerechnet
                rrow_bottom = line.ascent + rrow.descent  # Abstand rrow-Unterkante von line.y
                line_h = max(line.height, rrow_bottom, fm.height())
                extra_w = 4 + sep_w + rrow.width + 8
            else:
                line_h = max(line.height, fm.height())
                extra_w = 0.0

            y += line_h + LINE_GAP
            w = line.width + extra_w
            if w > max_w:
                max_w = w
        total_h = y - LINE_GAP   # letztes Gap abziehen

        # Groesse fuer Layout/ScrollArea: nicht setMinimumHeight (das kann nur
        # wachsen), sondern eine richtige sizeHint plus eine resize() falls
        # wir nicht in einer ScrollArea haengen.
        self._content_w = int(max_w + 2 * self.PADDING + 4)
        self._content_h = int(total_h + self.PADDING + 4)
        # Mindestgroessen schrumpfen mit, falls der Inhalt kleiner geworden ist.
        self.setMinimumSize(0, 0)
        self.resize(max(self._content_w, self.width()),
                    max(self._content_h, self.height()))
        self.updateGeometry()
        self._wake_cursor()
        self._ensure_cursor_visible()
        self.update()

    def sizeHint(self) -> QSize:
        # Wird von QScrollArea benutzt, um die noetige Widget-Groesse zu wissen.
        return QSize(self._content_w, self._content_h)

    def minimumSizeHint(self) -> QSize:
        return QSize(self._content_w, self._content_h)

    def _ensure_cursor_visible(self) -> None:
        """Wenn der Editor in einer QScrollArea hängt, scrollt diese so,
        dass die aktuelle Cursor-Position sichtbar ist."""
        # Eltern-Hierarchie nach QScrollArea durchsuchen.
        parent = self.parent()
        while parent is not None:
            if isinstance(parent, QScrollArea):
                row = self.cursor.row
                cx = int(row.x + row.cursor_x_at(self.cursor.index))
                cy = int(row.y)
                ch = int(max(row.height, SLOT_MIN_H))
                # Mit etwas Margin scrollen - sonst klebt der Cursor am Rand.
                margin = 20
                parent.ensureVisible(cx, cy + ch // 2, margin, ch // 2 + margin)
                return
            parent = parent.parent()

    # ── Events ────────────────────────────────────────────────────────────
    def focusInEvent(self, e) -> None:
        super().focusInEvent(e)
        self._wake_cursor()

    def focusOutEvent(self, e) -> None:
        super().focusOutEvent(e)
        self.update()

    def mousePressEvent(self, e: QMouseEvent) -> None:
        if e.button() != Qt.LeftButton:
            super().mousePressEvent(e)
            return
        x = e.position().x()
        y = e.position().y()
        target = self._pick_at(x, y)
        if target is not None:
            row, idx = target
            self.cursor.row = row
            self.cursor.index = idx
            self._marked_node = None
            self._wake_cursor()
            self.update()
        self.setFocus()

    def _pick_at(self, x: float, y: float) -> tuple[RowNode, int] | None:
        """Wandelt Widget-Koordinaten (x,y) in eine (Row, Index)-Position um.
        Wählt zunächst die Top-Level-Zeile, dann rekursiv den Slot/Index."""
        if not self.lines:
            return None
        # Welche Top-Level-Zeile? Wenn der Klick zwischen Zeilen liegt,
        # nimm die nächstgelegene.
        line = self.lines[0]
        best_d = abs(self._line_center_y(line) - y)
        for ln in self.lines[1:]:
            d = abs(self._line_center_y(ln) - y)
            if d < best_d:
                best_d = d
                line = ln
        # Falls die Y-Koordinate direkt in einer Zeile liegt, bevorzuge die.
        for ln in self.lines:
            if ln.y <= y <= ln.y + max(ln.height, SLOT_MIN_H):
                line = ln
                break

        # Prüfen ob der Klick in eine Ergebnis-Row fällt (rechts vom Ausdruck).
        for i, rrow in enumerate(self.result_rows):
            if rrow is None or i >= len(self.lines):
                continue
            rrow_top = rrow.y
            rrow_bottom = rrow.y + max(rrow.height, SLOT_MIN_H)
            if rrow_top <= y <= rrow_bottom:
                if x >= rrow.x - 2:
                    return _pick_in_row(rrow, x, y)

        return _pick_in_row(line, x, y)

    @staticmethod
    def _line_center_y(line: RowNode) -> float:
        h = max(line.height, SLOT_MIN_H)
        return line.y + h / 2

    def keyPressEvent(self, e: QKeyEvent) -> None:
        key = e.key()
        mods = e.modifiers()
        text = e.text()
        ctrl = bool(mods & Qt.ControlModifier)

        # Strukturierter Backspace: Markierung wird nur durch wiederholtes
        # Backspace bestätigt. Jede andere Taste hebt sie auf.
        if key != Qt.Key_Backspace:
            self._marked_node = None

        # Undo / Redo / Copy / Cut
        if ctrl and key == Qt.Key_Z:
            self._undo()
            return
        if ctrl and key == Qt.Key_Y:
            self._redo()
            return
        if ctrl and key == Qt.Key_C:
            self._copy()
            return
        if ctrl and key == Qt.Key_X:
            self._push_undo()
            self._cut()
            return
        if ctrl and key == Qt.Key_V:
            self._push_undo()
            self._paste()
            return

        # Snapshot vor modifizierenden Operationen speichern.
        _NAV_KEYS = {
            Qt.Key_Left, Qt.Key_Right, Qt.Key_Up, Qt.Key_Down,
            Qt.Key_Home, Qt.Key_End,
        }
        if key not in _NAV_KEYS:
            self._push_undo()

        # Ctrl+Tab → neue Zeile in Matrix bzw. Gleichungssystem.
        # Ctrl+Shift+Tab bzw. Ctrl+Backtab → neue Spalte (nur Matrix).
        if (key == Qt.Key_Tab) and (mods & Qt.ControlModifier) \
                and not (mods & Qt.ShiftModifier):
            self._container_add_row()
            return
        if (key == Qt.Key_Backtab and (mods & Qt.ControlModifier)) \
                or (key == Qt.Key_Tab and (mods & Qt.ControlModifier)
                    and (mods & Qt.ShiftModifier)):
            self._matrix_add_column()
            return

        # Enter → auswerten aller Zeilen + Cursor auf nächste Zeile.
        # Ctrl+Enter → aktuelle Zeile numerisch auswerten (aprox), bleibt dort.
        if key in (Qt.Key_Return, Qt.Key_Enter):
            self._clear_selection()
            if mods & Qt.ControlModifier:
                self._evaluate(approx_current=True)
            else:
                self._evaluate()
                i = self._top_line_index()
                if 0 <= i and i + 1 < len(self.lines):
                    # Nächste Zeile existiert → dorthin bewegen, keine neue einfügen.
                    self.cursor.row   = self.lines[i + 1]
                    self.cursor.index = 0
                    self._relayout()
                else:
                    self._new_line_below_current()
            return

        # Ctrl+F → Bruch
        if key == Qt.Key_F and mods & Qt.ControlModifier:
            self._insert_fraction_from_tail()
            return

        # Ctrl+R → Quadratwurzel,  Ctrl+Shift+R → n-te Wurzel
        if key == Qt.Key_R and mods & Qt.ControlModifier:
            if mods & Qt.ShiftModifier:
                self._insert_nth_root()
            else:
                self._insert_sqrt()
            return

        # Alt+S → Summe,  Alt+I → Integral,  Alt+V → Vektor,  Alt+L → Logarithmus
        if mods & Qt.AltModifier and not (mods & Qt.ControlModifier):
            if key == Qt.Key_S:
                self._insert_sum()
                return
            if key == Qt.Key_I:
                self._insert_integral()
                return
            if key == Qt.Key_V:
                self._insert_matrix()
                return
            if key == Qt.Key_L:
                self._insert_log()
                return
            if key == Qt.Key_G:
                self._insert_system()
                return


        # Ctrl+_ (= Ctrl+Shift+Minus auf CH-Layout) → Subscript.
        # Prüfung über Text oder Key: robust gegen Layout-Unterschiede.
        if (mods & Qt.ControlModifier) and (
            text == "_"
            or (key == Qt.Key_Underscore)
            or (key == Qt.Key_Minus and mods & Qt.ShiftModifier)
        ):
            self._insert_subscript()
            return

        # ^ (Caret) allein → Exponent. Auf CH-Layout ist ^ ein Dead-Key;
        # Qt liefert dann Key_Dead_Circumflex mit leerem text(). Wir
        # akzeptieren beide Varianten und Key_AsciiCircum für US-Layout.
        # (getattr wegen Robustheit gegenüber alten PySide6-Versionen.)
        _KEY_DEAD_CIRC = getattr(Qt, "Key_Dead_Circumflex", -1)
        if key == Qt.Key_AsciiCircum or key == _KEY_DEAD_CIRC or text == "^":
            self._insert_superscript()
            return

        if key == Qt.Key_Backspace:
            self._backspace()
            return
        if key == Qt.Key_Delete:
            self._delete()
            return

        if key == Qt.Key_Left:
            if mods & Qt.ShiftModifier:
                self._sel_extend_left()
            else:
                self._clear_selection()
                self._move_left()
            return
        if key == Qt.Key_Right:
            if mods & Qt.ShiftModifier:
                self._sel_extend_right()
            else:
                self._clear_selection()
                self._move_right()
            return
        if key == Qt.Key_Up:
            self._clear_selection()
            self._move_vertical(up=True)
            return
        if key == Qt.Key_Down:
            self._clear_selection()
            self._move_vertical(up=False)
            return
        if key == Qt.Key_Tab:
            self._clear_selection()
            self._move_to_next_slot()
            return

        if key == Qt.Key_Home:
            self._clear_selection()
            self.cursor.index = 0
            self._invalidate_slot_memory()
            self._relayout()
            return
        if key == Qt.Key_End:
            self._clear_selection()
            self.cursor.index = len(self.cursor.row.children)
            self._invalidate_slot_memory()
            self._relayout()
            return

        # Normales Zeichen einfügen
        if text and text.isprintable():
            self._insert_text(text)
            return

        super().keyPressEvent(e)

    # ── Bearbeitungs-Operationen ─────────────────────────────────────────
    def _insert_text(self, s: str) -> None:
        if self._is_in_result_row():
            return
        self._delete_selection()  # löscht Auswahl falls vorhanden (kein Relayout)
        self._mark_dirty()
        for ch in s:
            node = TextNode(ch)
            self.cursor.row.insert(self.cursor.index, node)
            self.cursor.index += 1
        self._invalidate_slot_memory()
        self._relayout()

    def _backspace(self) -> None:
        if self._is_in_result_row():
            line_idx = self._result_row_line_index()
            if line_idx is not None:
                self._clear_result(line_idx)
            return
        if self._has_selection():
            self._delete_selection()
            self._relayout()
            return
        row = self.cursor.row
        if self.cursor.index > 0:
            prev = row.children[self.cursor.index - 1]
            # Text-Zeichen: normal sofort löschen.
            if isinstance(prev, TextNode):
                row.pop(self.cursor.index - 1)
                self.cursor.index -= 1
                self._mark_dirty()
                self._invalidate_slot_memory()
                self._relayout()
                return
            # Strukturierter Node (Bruch, Wurzel, Summe, …): erst markieren,
            # beim zweiten Backspace wirklich löschen.
            if self._marked_node is prev:
                row.pop(self.cursor.index - 1)
                self.cursor.index -= 1
                self._marked_node = None
                self._mark_dirty()
                self._invalidate_slot_memory()
                self._relayout()
            else:
                self._marked_node = prev
                # Cursor-Blinken zurücksetzen, damit man die Markierung
                # ohne flackernden Cursor sieht.
                self._wake_cursor()
                self.update()
            return

        # Cursor ganz links. Wenn wir in einem Container-Slot sind:
        container = _container_of(row)
        if container is None:
            # Top-Level-Zeile. Wenn es eine vorherige gibt: zusammenführen.
            if self._is_top_level_row(row):
                self._merge_with_previous_line()
            return

        # Sonderfall Matrix: leere Zeile/Spalte in der Matrix entfernen,
        # wenn der Cursor in ihr steht.
        if isinstance(container, MatrixNode):
            if self._try_delete_matrix_line(container, row):
                return

        # Sonderfall Gleichungssystem: leere Zeile im System entfernen.
        if isinstance(container, SystemNode):
            if self._try_delete_system_row(container, row):
                return

        # Default: aus dem Slot raushüpfen.
        outer, idx = _find_enclosing_row(container)
        if outer is not None:
            self.cursor.row = outer
            self.cursor.index = idx
            self._relayout()

    def _try_delete_matrix_line(self, mat: "MatrixNode",
                                row: RowNode) -> bool:
        """Wird bei Backspace in leerer Matrix-Zelle aufgerufen.
        Löscht die Zeile (wenn sie komplett leer ist und n_rows > 1) oder
        die Spalte (analog). Gibt True zurück, wenn gelöscht wurde - dann
        ist der _backspace-Aufruf fertig."""
        pos = mat.find_cell(row)
        if pos is None:
            return False
        r, c = pos

        # Prüfen ob die aktuelle Zelle leer ist
        if len(row.children) != 0:
            return False

        # Zeile komplett leer? Und mehr als eine Zeile vorhanden?
        row_empty = all(len(cell.children) == 0 for cell in mat.cells[r])
        if row_empty and mat.n_rows > 1:
            del mat.cells[r]
            # Cursor in gleiche Spalte der neuen "letzten oder vorigen Zeile"
            new_r = min(r, mat.n_rows - 1)
            new_cell = mat.cells[new_r][min(c, mat.n_cols - 1)]
            self.cursor.row = new_cell
            self.cursor.index = len(new_cell.children)
            self._mark_dirty()
            self._invalidate_slot_memory()
            self._relayout()
            return True

        # Spalte komplett leer? Und mehr als eine Spalte?
        col_empty = all(len(mat.cells[rr][c].children) == 0
                        for rr in range(mat.n_rows))
        if col_empty and mat.n_cols > 1:
            for rr in range(mat.n_rows):
                del mat.cells[rr][c]
            new_c = min(c, mat.n_cols - 1)
            new_cell = mat.cells[min(r, mat.n_rows - 1)][new_c]
            self.cursor.row = new_cell
            self.cursor.index = len(new_cell.children)
            self._mark_dirty()
            self._invalidate_slot_memory()
            self._relayout()
            return True

        return False

    def _container_add_row(self) -> None:
        """Ctrl+Tab: hängt je nach umgebendem Container eine Zeile an.

        Sucht den nächstgelegenen Matrix- oder System-Container vom
        Cursor aus nach aussen; ignoriert Ctrl+Tab, wenn keiner gefunden
        wird.
        """
        row: RowNode | None = self.cursor.row
        while row is not None:
            container = _container_of(row)
            if isinstance(container, MatrixNode):
                self._matrix_add_row()
                return
            if isinstance(container, SystemNode):
                self._system_add_row(container)
                return
            if container is None:
                return
            outer, _ = _find_enclosing_row(container)
            row = outer

    def _matrix_add_row(self) -> None:
        """Ctrl+Tab: Zeile an die aktuelle Matrix anhängen, Cursor in
        die erste Zelle der neuen Zeile."""
        container = _container_of(self.cursor.row)
        if not isinstance(container, MatrixNode):
            return
        container.add_row()
        self.cursor.row.last_cursor_index = self.cursor.index
        self.cursor.row = container.cells[-1][0]
        self.cursor.index = 0
        self._mark_dirty()
        self._invalidate_slot_memory()
        self._relayout()

    def _system_add_row(self, container: "SystemNode") -> None:
        """Hängt eine neue Zeile an das Gleichungssystem an und setzt
        den Cursor an deren Anfang."""
        container.add_row()
        self.cursor.row.last_cursor_index = self.cursor.index
        self.cursor.row = container.rows[-1]
        self.cursor.index = 0
        self._mark_dirty()
        self._invalidate_slot_memory()
        self._relayout()

    def _try_delete_system_row(self, sys_node: "SystemNode",
                               row: RowNode) -> bool:
        """Backspace in leerer System-Zeile: Zeile entfernen, wenn mehr
        als eine Zeile existiert. Gibt True zurück, wenn gelöscht."""
        if row.children:
            return False
        if sys_node.n_rows <= 1:
            return False
        i = sys_node.find_row(row)
        if i is None:
            return False
        del sys_node.rows[i]
        new_i = min(i, sys_node.n_rows - 1)
        new_row = sys_node.rows[new_i]
        self.cursor.row = new_row
        self.cursor.index = len(new_row.children)
        self._mark_dirty()
        self._invalidate_slot_memory()
        self._relayout()
        return True

    def _matrix_add_column(self) -> None:
        """Ctrl+Shift+Tab: Spalte an die aktuelle Matrix anhängen, Cursor
        in die (neue) letzte Zelle der Zeile, in der wir waren."""
        container = _container_of(self.cursor.row)
        if not isinstance(container, MatrixNode):
            return
        # Merken, in welcher Zeile wir sind
        pos = container.find_cell(self.cursor.row)
        r = pos[0] if pos is not None else 0
        container.add_column()
        self.cursor.row.last_cursor_index = self.cursor.index
        self.cursor.row = container.cells[r][-1]
        self.cursor.index = 0
        self._mark_dirty()
        self._invalidate_slot_memory()
        self._relayout()

    def _delete(self) -> None:
        if self._is_in_result_row():
            line_idx = self._result_row_line_index()
            if line_idx is not None:
                self._clear_result(line_idx)
            return
        if self._has_selection():
            self._delete_selection()
            self._relayout()
            return
        row = self.cursor.row
        if self.cursor.index < len(row.children):
            row.pop(self.cursor.index)
            self._mark_dirty()
            self._invalidate_slot_memory()
            self._relayout()
            return
        # Cursor am Ende einer Top-Level-Zeile: Ergebnis mit Del löschen.
        if self._is_top_level_row(row):
            i = self._top_line_index()
            if i >= 0 and i < len(self.result_rows) and self.result_rows[i] is not None:
                self._clear_result(i)

    def _move_left(self) -> None:
        row = self.cursor.row

        # Cursor in Ergebnis-Zeile: einfaches Navigieren oder raus zur Ausdrucks-Zeile.
        line_idx = self._result_row_line_index()
        if line_idx is not None:
            if self.cursor.index > 0:
                self.cursor.index -= 1
            else:
                # Zeilenanfang der Ergebnis-Zeile → zurück ans Ende des Ausdrucks.
                expr_row = self.lines[line_idx]
                self.cursor.row = expr_row
                self.cursor.index = len(expr_row.children)
            self._invalidate_slot_memory()
            self._relayout()
            return

        if self.cursor.index > 0:
            prev = row.children[self.cursor.index - 1]
            if hasattr(prev, "last_slot") and callable(getattr(prev, "last_slot")):
                target = prev.last_slot()   # type: ignore[attr-defined]
                self.cursor.row = target
                self.cursor.index = len(target.children)
            else:
                self.cursor.index -= 1
        else:
            # Am Anfang der Row. Erst prüfen, ob der umgebende Container
            # einen horizontalen Vorgänger-Slot hat - dann dort ans Ende.
            container = _container_of(row)
            if container is not None and hasattr(container, "horizontal_prev"):
                tgt = container.horizontal_prev(row)   # type: ignore[attr-defined]
                if tgt is not None:
                    self.cursor.row = tgt
                    self.cursor.index = len(tgt.children)
                    self._invalidate_slot_memory()
                    self._relayout()
                    return
            if container is not None:
                outer, idx = _find_enclosing_row(container)
                if outer is not None:
                    self.cursor.row = outer
                    self.cursor.index = idx
            elif self._is_top_level_row(row):
                # Top-Level-Zeile, Cursor ganz links.
                # Prüfen ob vorige Zeile eine Ergebnis-Zeile hat → dort rein.
                i = self.lines.index(row)
                if i > 0:
                    prev_rrow = (self.result_rows[i - 1]
                                 if i - 1 < len(self.result_rows) else None)
                    if prev_rrow is not None and prev_rrow.children:
                        self.cursor.row = prev_rrow
                        self.cursor.index = len(prev_rrow.children)
                    else:
                        self.cursor.row = self.lines[i - 1]
                        self.cursor.index = len(self.lines[i - 1].children)
        self._invalidate_slot_memory()
        self._relayout()

    def _move_right(self) -> None:
        row = self.cursor.row

        # Cursor in Ergebnis-Zeile: einfaches Navigieren oder in nächste Zeile.
        line_idx = self._result_row_line_index()
        if line_idx is not None:
            if self.cursor.index < len(row.children):
                self.cursor.index += 1
            else:
                # Ende der Ergebnis-Zeile → Anfang der nächsten Ausdrucks-Zeile.
                if line_idx < len(self.lines) - 1:
                    self.cursor.row = self.lines[line_idx + 1]
                    self.cursor.index = 0
            self._invalidate_slot_memory()
            self._relayout()
            return

        if self.cursor.index < len(row.children):
            nxt = row.children[self.cursor.index]
            if hasattr(nxt, "first_slot") and callable(getattr(nxt, "first_slot")):
                target = nxt.first_slot()   # type: ignore[attr-defined]
                self.cursor.row = target
                self.cursor.index = 0
            else:
                self.cursor.index += 1
        else:
            # Am Ende der Row.
            container = _container_of(row)
            if container is not None and hasattr(container, "horizontal_next"):
                tgt = container.horizontal_next(row)   # type: ignore[attr-defined]
                if tgt is not None:
                    self.cursor.row = tgt
                    self.cursor.index = 0
                    self._invalidate_slot_memory()
                    self._relayout()
                    return
            if container is not None:
                outer, idx = _find_enclosing_row(container)
                if outer is not None:
                    self.cursor.row = outer
                    self.cursor.index = idx + 1
            elif self._is_top_level_row(row):
                # Top-Level-Zeile, Cursor ganz rechts.
                # Prüfen ob diese Zeile eine Ergebnis-Zeile hat → dort rein.
                i = self.lines.index(row)
                rrow = (self.result_rows[i]
                        if i < len(self.result_rows) else None)
                if rrow is not None and rrow.children:
                    self.cursor.row = rrow
                    self.cursor.index = 0
                elif i < len(self.lines) - 1:
                    self.cursor.row = self.lines[i + 1]
                    self.cursor.index = 0
        self._invalidate_slot_memory()
        self._relayout()

    def _invalidate_slot_memory(self) -> None:
        """Verwirft die gemerkten Einsprungs-Positionen in den Slots des
        umgebenden Containers. Wird nach horizontalen Bewegungen oder
        Editieraktionen aufgerufen, damit das nächste ↑/↓ wieder
        x-basiert sucht statt zu einer veralteten Position zu springen."""
        container = _container_of(self.cursor.row)
        if container is not None and hasattr(container, "slots"):
            for s in container.slots():   # type: ignore[attr-defined]
                s.last_cursor_index = None

    # Alter Name als Alias - damit ich nichts übersehe falls irgendwo noch
    # der alte Name referenziert wird.
    # (keiner mehr - entfernt nach Refactor)

    def _enter_slot(self, target: RowNode) -> None:
        """Wechselt den Cursor in einen anderen Slot und wählt dort den Index:
          1. zuerst die im Ziel gespeicherte letzte Position, sonst
          2. den Index, dessen x-Position am nächsten an der aktuellen ist.
        Die Position im gerade verlassenen Slot wird vorher gespeichert."""
        # aktuelle Position im verlassenen Slot merken
        self.cursor.row.last_cursor_index = self.cursor.index
        # aktuelle x-Pixel-Position berechnen (für Fallback)
        cur_x = self.cursor.row.x + self.cursor.row.cursor_x_at(self.cursor.index)

        self.cursor.row = target
        if target.last_cursor_index is not None:
            self.cursor.index = min(target.last_cursor_index,
                                    len(target.children))
        else:
            self.cursor.index = _index_closest_to_x(target, cur_x)

    def _move_vertical(self, up: bool) -> None:
        """↑/↓ wechselt zwischen vertikal angeordneten Slots desselben
        Containers (z. B. Zähler ↔ Nenner, oder Index ↔ Wurzelinhalt).
        Auf Top-Level (also in einer Zeile direkt) wechselt ↑/↓ zwischen
        den Top-Level-Zeilen. x-Memory: Cursor-x wird auf die Ziel-Zeile
        abgebildet (nächster Index, der pixelmässig am nächsten liegt)."""
        # Sonderfall: Cursor in Ergebnis-Zeile → direkt in Ausdruck-Zeile springen.
        line_idx = self._result_row_line_index()
        if line_idx is not None:
            target_i = line_idx - 1 if up else line_idx + 1
            if 0 <= target_i < len(self.lines):
                cur_x = self.cursor.row.x + self.cursor.row.cursor_x_at(self.cursor.index)
                tgt = self.lines[target_i]
                self.cursor.row = tgt
                self.cursor.index = _index_closest_to_x(tgt, cur_x)
                self._relayout()
            return

        row = self.cursor.row
        container = _container_of(row)
        while container is not None:
            if up and hasattr(container, "slot_above"):
                tgt = container.slot_above(row)   # type: ignore[attr-defined]
                if tgt is not None:
                    self._enter_slot(tgt)
                    self._relayout()
                    return
            if (not up) and hasattr(container, "slot_below"):
                tgt = container.slot_below(row)   # type: ignore[attr-defined]
                if tgt is not None:
                    self._enter_slot(tgt)
                    self._relayout()
                    return
            # eine Ebene raus
            outer, _ = _find_enclosing_row(container)
            if outer is None:
                return
            row = outer
            container = _container_of(row)
        # Container-Kette abgelaufen: wir sind auf Top-Level → zwischen Zeilen.
        if self._is_top_level_row(row):
            i = self.lines.index(row)
            target_i = i - 1 if up else i + 1
            if 0 <= target_i < len(self.lines):
                # aktuelle x-Pixel-Position als Ziel für die neue Zeile
                cur_x = row.x + row.cursor_x_at(self.cursor.index)
                target_line = self.lines[target_i]
                self.cursor.row = target_line
                self.cursor.index = _index_closest_to_x(target_line, cur_x)
                self._relayout()

    def _move_to_next_slot(self) -> None:
        """Tab: nächster Slot im umgebenden Container. Ist man im letzten
        Slot einer Matrix, wird stattdessen eine neue Zeile angehängt und
        der Cursor wandert dorthin (so wächst ein Vektor zu einer längeren
        Liste). In allen anderen Containern läuft der Cursor rechts raus."""
        row = self.cursor.row
        container = _container_of(row)
        if container is None or not hasattr(container, "slots"):
            return
        slots = container.slots()   # type: ignore[attr-defined]
        try:
            i = slots.index(row)
        except ValueError:
            return
        if i + 1 < len(slots):
            self._enter_slot(slots[i + 1])
        elif isinstance(container, MatrixNode):
            # Letzte Zelle der Matrix: Zeile anhängen und in deren erste Zelle.
            container.add_row()
            self.cursor.row.last_cursor_index = self.cursor.index
            self.cursor.row = container.cells[-1][0]
            self.cursor.index = 0
        elif isinstance(container, SystemNode):
            # Letzte Zeile des Gleichungssystems: neue Zeile anhängen.
            container.add_row()
            self.cursor.row.last_cursor_index = self.cursor.index
            self.cursor.row = container.rows[-1]
            self.cursor.index = 0
        else:
            outer, idx = _find_enclosing_row(container)
            if outer is not None:
                self.cursor.row.last_cursor_index = self.cursor.index
                self.cursor.row = outer
                self.cursor.index = idx + 1
        self._relayout()

    def _insert_fraction_from_tail(self) -> None:
        """Aktuellen Zeilen-Tail (bis zum letzten Trennzeichen) zum Zähler
        machen; leeren Nenner einfügen; Cursor in Nenner setzen.
        Ist der Tail leer, wird ein leerer Bruch eingefügt."""
        if self._is_in_result_row():
            return
        row = self.cursor.row
        # Tail bestimmen: gehe links vom Cursor so weit wie möglich, bis
        # entweder ein Nicht-TextNode kommt oder ein Operator/Leerzeichen.
        end = self.cursor.index
        start = end
        SEPARATORS = set(" +\u2212-*/=<>,;:()[]{}")  # inkl. Unicode-Minus
        while start > 0:
            c = row.children[start - 1]
            if not isinstance(c, TextNode):
                break
            if c.char in SEPARATORS:
                break
            start -= 1

        # Tail-Knoten einsammeln. pop(start) verschiebt jeweils das nächste
        # Element an Position `start` nach, deshalb poppen wir (end-start)-mal
        # an derselben Stelle und erhalten die Knoten in der richtigen Reihenfolge.
        tail_nodes = [row.pop(start) for _ in range(end - start)]

        numerator = RowNode(tail_nodes)
        denominator = RowNode()
        frac = FractionNode(numerator=numerator, denominator=denominator)

        # Bruch an die Stelle einsetzen, wo der Tail war
        row.insert(start, frac)
        self.cursor.row = frac.denominator
        self.cursor.index = 0
        self._mark_dirty()
        self._relayout()

    def _insert_container_at_cursor(self, container: MathNode,
                                    focus_slot: RowNode) -> None:
        """Gemeinsamer Helfer: Container am Cursor einfügen, Cursor in den
        gewünschten Slot setzen, neu layouten."""
        if self._is_in_result_row():
            return
        row = self.cursor.row
        row.insert(self.cursor.index, container)
        self.cursor.row = focus_slot
        self.cursor.index = 0
        self._mark_dirty()
        self._relayout()

    # ── Multi-Line-Operationen ───────────────────────────────────────────
    def _new_line_below_current(self) -> None:
        """Fügt eine neue leere Zeile nach der aktuellen Top-Level-Zeile ein
        und setzt den Cursor dort an den Anfang."""
        i = self._top_line_index()
        if i < 0:
            i = len(self.lines) - 1
        new_line = RowNode()
        self.lines.insert(i + 1, new_line)
        self.results.insert(i + 1, ("", False))
        self.result_rows.insert(i + 1, None)
        self.cursor.row = new_line
        self.cursor.index = 0
        self._marked_node = None
        self._relayout()

    def _merge_with_previous_line(self) -> bool:
        """Bei Backspace am Anfang einer Zeile: Inhalt der aktuellen Zeile
        ans Ende der vorherigen anhängen und die aktuelle Zeile entfernen.
        Gibt True zurück, wenn die Aktion ausgeführt wurde."""
        if self.cursor.index != 0:
            return False
        if not self._is_top_level_row(self.cursor.row):
            return False
        i = self.lines.index(self.cursor.row)
        if i == 0:
            return False
        prev_line = self.lines[i - 1]
        curr_line = self.lines[i]
        # Position für Cursor merken: Ende der alten vorherigen Zeile
        merge_index = len(prev_line.children)
        # Kinder anhängen (in Reihenfolge; parent muss neu gesetzt werden)
        while curr_line.children:
            c = curr_line.pop(0)
            prev_line.append(c)
        # Zeile + Ergebnis entfernen
        del self.lines[i]
        del self.results[i]
        if i < len(self.result_rows):
            del self.result_rows[i]
        self.cursor.row = prev_line
        self.cursor.index = merge_index
        self._mark_dirty()
        # Ergebnis der vorherigen Zeile ist jetzt veraltet
        if i - 1 < len(self.results):
            self.results[i - 1] = ("", False)
        if i - 1 < len(self.result_rows):
            self.result_rows[i - 1] = None
        self._relayout()
        return True

    def _insert_superscript(self) -> None:
        """Exponent einfügen. Der leere Slot öffnet sich direkt rechts vom
        Cursor - die Basis ist alles, was links davor im Row steht."""
        node = SuperscriptNode()
        self._insert_container_at_cursor(node, node.inner)

    def _insert_subscript(self) -> None:
        """Subscript einfügen (nur für Namen/Indizes, keine math. Wirkung)."""
        node = SubscriptNode()
        self._insert_container_at_cursor(node, node.inner)

    def _insert_sqrt(self) -> None:
        """Quadratwurzel einfügen. Cursor landet im Radikand."""
        node = SqrtNode()
        self._insert_container_at_cursor(node, node.inner)

    def _insert_nth_root(self) -> None:
        """n-te Wurzel einfügen. Cursor landet im Index-Slot (oben links),
        damit man gleich die Wurzelordnung eintippen kann."""
        node = NthRootNode()
        self._insert_container_at_cursor(node, node.index)

    def _insert_sum(self) -> None:
        """Summe Σ einfügen. Cursor landet im unteren Variablen-Slot, damit
        man typisch „i" gefolgt von der Grenze tippen kann."""
        node = SumNode()
        self._insert_container_at_cursor(node, node.lower_var)

    def _insert_integral(self) -> None:
        """Integral ∫ einfügen. Cursor startet in der unteren Grenze."""
        node = IntegralNode()
        self._insert_container_at_cursor(node, node.lower)

    def _insert_log(self) -> None:
        """Logarithmus logₙ einfügen. Cursor startet in der Basis."""
        node = LogNode()
        self._insert_container_at_cursor(node, node.base)

    def _insert_matrix(self) -> None:
        """Vektor einfügen - als 2×1-Matrix gerendert (= Spaltenvektor
        `[a; b]`). Cursor landet in der ersten Zelle. Eine weitere Zeile
        kommt durch Tab in der letzten Zelle dazu; mehr Spalten via
        `Ctrl+Tab` (macht aus dem Vektor eine Matrix)."""
        node = MatrixNode(rows=2, cols=1)
        self._insert_container_at_cursor(node, node.cells[0][0])

    def _insert_system(self) -> None:
        """Gleichungssystem mit geschweifter Klammer einfügen. Startet
        mit zwei leeren Zeilen; weitere Zeilen kommen via `Ctrl+Tab`
        (oder Tab in der letzten Zeile) dazu."""
        node = SystemNode(rows=2)
        self._insert_container_at_cursor(node, node.rows[0])



class MathFormulaDisplay(QWidget):
    """Schreibgeschuetzter Formel-Anzeiger auf Basis des MathNode-Systems.

    Stellt eine einzelne Formelzeile im Cambria-Math-Font dar, ohne
    Cursor, Fokus oder interaktive Eingabe. Einsatzbereich: eingebettete
    Formel-Darstellung in Lexikon-Artikeln neben der CAS-Schaltflaeche.

    Abkuerzungen (Initialnotation):
        CAS      - Computer Algebra System.
        MathNode - Basisklasse des strukturierten Formel-Baums.
    """

    _PADDING_X: float = 10.0
    _PADDING_Y: float = 6.0

    def __init__(self, formula: str, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self._row: RowNode = _parse_result_to_row(formula.strip())
        self._row.measure(FONT_SIZE_PT)
        self.setFixedHeight(max(int(self._row.height + 2 * self._PADDING_Y + 2), 32))

    def paintEvent(self, _event) -> None:  # noqa: D401 - Qt-Callback
        p = QPainter(self)
        p.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        p.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)
        self._row.paint(p, self._PADDING_X, self._PADDING_Y)
        p.end()

    def sizeHint(self) -> QSize:
        w = max(int(self._row.width + 2 * self._PADDING_X + 4), 40)
        h = max(int(self._row.height + 2 * self._PADDING_Y + 2), 32)
        return QSize(w, h)

    def minimumSizeHint(self) -> QSize:
        return self.sizeHint()


# ── Mehrzeilige Ausdrucks-Gruppierung ────────────────────────────────────────
def _group_by_brackets(
    texts: list[str],
) -> tuple[list[tuple[str, list[int]]], dict[int, int]]:
    """Gruppiert aufeinanderfolgende Zeilen mit offenen Klammern.

    Zeilen, deren Klammern am Zeilenende noch nicht geschlossen sind,
    werden mit der folgenden Zeile zusammengeführt. Das erlaubt mehrzeilige
    Ausdrücke wie ``solve({`` / ``x+y=5,`` / ``x-y=1`` / ``}, {x,y})``.

    Returns:
        groups: Liste von (merged_text, [source_line_indices]).
        line_to_group: Zuordnung Zeilen-Index → Gruppen-Index.
    """
    groups: list[tuple[str, list[int]]] = []
    line_to_group: dict[int, int] = {}

    pending_text = ""
    pending_indices: list[int] = []
    depth = 0

    def flush() -> None:
        nonlocal pending_text, pending_indices, depth
        if pending_indices:
            gi = len(groups)
            for idx in pending_indices:
                line_to_group[idx] = gi
            groups.append((pending_text, list(pending_indices)))
            pending_text = ""
            pending_indices = []
            depth = 0

    for i, raw in enumerate(texts):
        stripped = raw.strip()
        is_comment = stripped.startswith("#")
        is_empty = not stripped

        if is_empty or is_comment:
            flush()
            gi = len(groups)
            line_to_group[i] = gi
            groups.append((raw, [i]))
            continue

        if not pending_indices:
            pending_text = raw
            pending_indices = [i]
            depth = 0
        else:
            pending_text += " " + raw
            pending_indices.append(i)

        for c in stripped:
            if c in "([{":
                depth += 1
            elif c in ")]}":
                depth -= 1

        if depth <= 0:
            flush()

    flush()
    return groups, line_to_group


# ── Serialisierung (simpel, für späteren Engine-Anschluss) ───────────────────
def _serialize_row(row: RowNode) -> str:
    parts: list[str] = []
    for c in row.children:
        if isinstance(c, TextNode):
            parts.append(c.char)
        elif isinstance(c, FractionNode):
            parts.append("(" + _serialize_row(c.numerator) + ")/("
                         + _serialize_row(c.denominator) + ")")
        elif isinstance(c, SuperscriptNode):
            parts.append("^(" + _serialize_row(c.inner) + ")")
        elif isinstance(c, SubscriptNode):
            # Tiefgestellter Text ist hier nur kosmetisch (Namens-Index),
            # also serialisieren wir ihn als `_<inner>` ohne Klammern,
            # damit SymPy das als Teil des Symbolnamens lesen kann.
            parts.append("_" + _serialize_row(c.inner))
        elif isinstance(c, LogNode):
            arg  = _serialize_row(c.argument)
            base = _serialize_row(c.base)
            if base:
                parts.append("log(" + arg + ", " + base + ")")
            else:
                parts.append("log(" + arg + ")")
        elif isinstance(c, SqrtNode):
            parts.append("sqrt(" + _serialize_row(c.inner) + ")")
        elif isinstance(c, NthRootNode):
            # n-te Wurzel → (inner)**(1/index)
            inner = _serialize_row(c.inner)
            idx = _serialize_row(c.index) or "2"
            parts.append("(" + inner + ")**(1/(" + idx + "))")
        elif isinstance(c, SumNode):
            # Sum(body, (var, lower, upper))  - SymPy-Notation
            body  = _serialize_row(c.body)
            var   = _serialize_row(c.lower_var)
            lo    = _serialize_row(c.lower_val)
            up    = _serialize_row(c.upper)
            parts.append("Sum(" + body + ", (" + var + ", " + lo + ", " + up + "))")
        elif isinstance(c, IntegralNode):
            # Integral(body, (var, lower, upper))
            body = _serialize_row(c.body)
            var  = _serialize_row(c.var)
            lo   = _serialize_row(c.lower)
            up   = _serialize_row(c.upper)
            parts.append("Integral(" + body + ", (" + var + ", " + lo + ", " + up + "))")
        elif isinstance(c, MatrixNode):
            # Als geschachtelte Liste serialisieren - Spaltenvektor mit
            # einer Spalte wird zu [[a],[b]], Matrix zu [[a,b],[c,d]].
            rows_s = []
            for mrow in c.cells:
                cells_s = [_serialize_row(cell) for cell in mrow]
                rows_s.append("[" + ", ".join(cells_s) + "]")
            parts.append("Matrix([" + ", ".join(rows_s) + "])")
        elif isinstance(c, SystemNode):
            # Gleichungssystem → Liste der Zeilen [zeile1, zeile2, ...].
            # Der Nutzer wickelt selbst `solve(...)` drumherum. Das `=` in
            # den Zeilen wird durch rewrite_equals_as_eq später zu `Eq(...)`;
            # leere Zeilen werden verworfen.
            eqs = [_serialize_row(r) for r in c.rows]
            eqs = [e for e in eqs if e.strip()]
            parts.append("[" + ", ".join(eqs) + "]")
    return "".join(parts)


# -- Standalone-Test ---------------------------------------------------------
def main() -> None:
    """Startet den Editor als eigenstaendige Anwendung ohne Engine."""
    import sys
    from PySide6.QtWidgets import (
        QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QHBoxLayout,
    )

    app = QApplication(sys.argv)

    win = QMainWindow()
    win.setWindowTitle("2D Math Editor - Proof of Concept")

    central = QWidget()
    layout = QVBoxLayout(central)

    hint = QLabel(
        "Tippe eine Formel. /=Bruch, ^=Exponent, Ctrl+_=Subscript, "
        "Ctrl+R=Wurzel, Ctrl+Shift+R=n-te Wurzel,\n"
        "Alt+S=Summe, Alt+I=Integral, Alt+V=Vektor, Alt+G=Gleichungssystem.\n"
        "Hoch/Runter wechselt zwischen Slots, Links/Rechts navigiert und "
        "taucht ein, Tab springt zum naechsten Slot "
        "(in letzter Matrix-Zelle: neue Zeile)."
    )
    hint.setStyleSheet("color: #6b7280; padding: 4px;")
    layout.addWidget(hint)

    editor = MathEditor()
    layout.addWidget(editor)

    readout = QLabel("-")
    readout.setStyleSheet("color: #111827; font-family: Consolas, monospace;")
    layout.addWidget(readout)

    def refresh() -> None:
        readout.setText("Serialisiert: " + editor.to_plain_text())

    # Nach jedem Paint die Serialisierung anzeigen
    _orig_paint = editor.paintEvent

    def _hook(e):
        _orig_paint(e)
        refresh()

    editor.paintEvent = _hook  # type: ignore[assignment]

    btns = QHBoxLayout()
    b_clear = QPushButton("Leeren")
    b_clear.clicked.connect(editor.clear)
    btns.addWidget(b_clear)
    btns.addStretch(1)
    layout.addLayout(btns)

    win.setCentralWidget(central)
    win.resize(700, 400)
    win.show()
    editor.setFocus()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
