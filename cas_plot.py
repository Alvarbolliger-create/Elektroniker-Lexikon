"""Eingebetteter 2D/3D-Graph-Panel fuer den CAS-Rechner.

Zeigt rechts neben dem Math-Editor ein QTabWidget mit zwei Karten:

* **2D** - einargumentige Funktionen ``f(x) := ...``
* **3D** - zweiargumentige Funktionen ``g(x, y) := ...``

Jede Karte besitzt eine eigene Funktionsliste (Checkboxen), Bereichs-
Eingaben, eine Matplotlib-``NavigationToolbar`` und eine Leinwand.
Funktionsdefinitionen werden regexbasiert aus dem Editor gelesen;
einfache Variablenzuweisungen ``a := 2`` werden fuer Substitutionen
ausgewertet. SymPy ``lambdify`` + NumPy uebernehmen die Abtastung.
"""

from __future__ import annotations

import cmath
import math
import re
from typing import TYPE_CHECKING, Any

from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import (
    QCheckBox,
    QDoubleSpinBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from phasor_widget import PhasorWidget

if TYPE_CHECKING:
    from cas_rechner import Engine
    from math_editor import MathEditor


# Mehrargumentige Funktionsdefinition (``name(a, b, c) := expr``).
_FUNC_DEF_RE = re.compile(
    r"^\s*([A-Za-z]\w*)\s*\(\s*"
    r"([A-Za-z]\w*(?:\s*,\s*[A-Za-z]\w*)*)\s*\)"
    r"\s*:=\s*(.+)$"
)
_VAR_DEF_RE = re.compile(r"^\s*([A-Za-z]\w*)\s*:=\s*(.+)$")

# Zoom-Faktor pro Mausrad-Tick.
_SCROLL_SCALE: float = 1.2

# Abtastraten: 2D feiner, 3D als Raster quadratisch -> teurer.
_N_SAMPLES_2D: int = 500
_N_SAMPLES_3D: int = 45


def _to_sympy(s: str) -> str:
    """Lokale Kopie der Minimal-Umformung - vermeidet Import-Zirkel."""
    from cas_rechner import to_sympy
    return to_sympy(s)


# ── Gemeinsames Editor-Scanning ────────────────────────────────────────────
def _scan_editor(
    editor: "MathEditor",
    engine: "Engine",
) -> tuple[list[tuple[str, list[str], str]], dict[str, Any]]:
    """Liest alle Funktions- und Variablendefinitionen aus dem Editor.

    Returns:
        Tupel ``(funcs, user_vars)``. ``funcs`` enthaelt Eintraege der Form
        ``(name, [arg, ...], expr)``. ``user_vars`` bildet Variablennamen auf
        bereits geparste SymPy-Ausdruecke ab, damit Funktionen darauf
        referenzieren koennen.
    """
    funcs: list[tuple[str, list[str], str]] = []
    simple_vars: dict[str, str] = {}
    for raw in editor.to_plain_text().splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        m_func = _FUNC_DEF_RE.match(line)
        if m_func:
            args = [a.strip() for a in m_func.group(2).split(",")]
            funcs.append((m_func.group(1), args, m_func.group(3).strip()))
            continue
        m_var = _VAR_DEF_RE.match(line)
        if m_var:
            simple_vars[m_var.group(1)] = m_var.group(2).strip()

    ns = engine._base_namespace()
    user_vars: dict[str, Any] = {}
    for name, expr in simple_vars.items():
        try:
            value = engine._parse(_to_sympy(expr), ns)
            user_vars[name] = value
            ns[name] = value
        except Exception:
            pass
    return funcs, user_vars


def _make_spin(value: float) -> QDoubleSpinBox:
    """Einheitliche SpinBox fuer Bereichs-Eingaben."""
    spin = QDoubleSpinBox()
    spin.setRange(-1e9, 1e9)
    spin.setDecimals(3)
    spin.setSingleStep(1.0)
    spin.setValue(value)
    return spin


# ── 2D-Karte ──────────────────────────────────────────────────────────────
class _Plot2DTab(QWidget):
    """Tab mit 2D-Funktionsplot fuer einargumentige Definitionen."""

    def __init__(
        self,
        editor: "MathEditor",
        engine: "Engine",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._editor = editor
        self._engine = engine
        self._functions: list[tuple[str, str, str]] = []
        self._user_vars: dict[str, Any] = {}
        # Zustand fuer Sicht-Erhalt + dynamisches Resampling.
        self._plotted_funcs: list[tuple[str, str, str]] = []
        self._lines: list[Any] = []
        self._has_plotted: bool = False
        self._force_view_reset: bool = False
        self._resampling: bool = False
        # Analyse-Modus (``None`` | ``"zero"`` | ``"max"`` | ``"min"``).
        self._mode: str | None = None
        self._span_selector: Any = None
        self._analysis_artists: list[Any] = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        header = QLabel("Funktionen auswählen:")
        header.setObjectName("settingsHeading")
        layout.addWidget(header)

        self.func_list = QListWidget()
        self.func_list.setMaximumHeight(140)
        self.func_list.itemChanged.connect(lambda _it: self._plot())
        layout.addWidget(self.func_list)

        # x-Bereich.
        x_row = QHBoxLayout()
        x_row.setSpacing(6)
        x_row.addWidget(QLabel("x von"))
        self.x_min = _make_spin(-10.0)
        x_row.addWidget(self.x_min)
        x_row.addWidget(QLabel("bis"))
        self.x_max = _make_spin(10.0)
        x_row.addWidget(self.x_max)
        x_row.addStretch()
        layout.addLayout(x_row)

        # y-Bereich + Auto-Y + Zeichnen.
        y_row = QHBoxLayout()
        y_row.setSpacing(6)
        y_row.addWidget(QLabel("y von"))
        self.y_min = _make_spin(-10.0)
        y_row.addWidget(self.y_min)
        y_row.addWidget(QLabel("bis"))
        self.y_max = _make_spin(10.0)
        y_row.addWidget(self.y_max)

        self.auto_y = QCheckBox("Auto-Y")
        self.auto_y.setChecked(True)
        self.auto_y.stateChanged.connect(self._on_auto_y_changed)
        y_row.addWidget(self.auto_y)
        y_row.addStretch()

        plot_btn = QPushButton("Zeichnen")
        plot_btn.setObjectName("okButton")
        plot_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        plot_btn.clicked.connect(self._on_plot_button)
        y_row.addWidget(plot_btn)
        layout.addLayout(y_row)

        self._on_auto_y_changed()

        # Analyse-Modi: Ziehen ueber den Graphen waehlt ein x-Intervall.
        analysis_row = QHBoxLayout()
        analysis_row.setSpacing(4)
        analysis_row.addWidget(QLabel("Analyse:"))
        self._mode_buttons: dict[str | None, QPushButton] = {}
        mode_style = (
            "QPushButton { background: transparent; color: #4f46e5;"
            " border: 1px solid #c7d2fe; border-radius: 4px;"
            " font-size: 11px; padding: 3px 10px; }"
            "QPushButton:hover { background: #eef2ff; }"
            "QPushButton:checked { background: #4f46e5; color: white;"
            " border-color: #4338ca; font-weight: 600; }"
        )
        for label, key in (
            ("Nullstelle", "zero"),
            ("Max", "max"),
            ("Min", "min"),
            ("Aus", None),
        ):
            btn = QPushButton(label)
            btn.setCheckable(True)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(mode_style)
            btn.clicked.connect(lambda _checked=False, k=key: self._set_mode(k))
            analysis_row.addWidget(btn)
            self._mode_buttons[key] = btn
        self._mode_buttons[None].setChecked(True)
        analysis_row.addStretch()
        layout.addLayout(analysis_row)

        from matplotlib.backends.backend_qtagg import (
            FigureCanvas,
            NavigationToolbar2QT,
        )
        from matplotlib.figure import Figure

        self._figure = Figure(figsize=(6, 4), tight_layout=True)
        self._canvas = FigureCanvas(self._figure)
        self._nav = NavigationToolbar2QT(self._canvas, self)
        layout.addWidget(self._nav)
        layout.addWidget(self._canvas, stretch=1)

        self._canvas.mpl_connect("scroll_event", self._on_scroll)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color:#dc2626;font-size:11px;")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

    def _on_auto_y_changed(self) -> None:
        enabled = not self.auto_y.isChecked()
        self.y_min.setEnabled(enabled)
        self.y_max.setEnabled(enabled)

    def set_scan_result(
        self,
        funcs: list[tuple[str, list[str], str]],
        user_vars: dict[str, Any],
    ) -> None:
        """Filtert einargumentige Funktionen und befuellt die Liste."""
        self._user_vars = user_vars

        previously_checked: set[str] = set()
        any_checked = False
        for i in range(self.func_list.count()):
            item = self.func_list.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)
            if data and item.checkState() == Qt.CheckState.Checked:
                previously_checked.add(data[0])
                any_checked = True

        self.func_list.blockSignals(True)
        self._functions.clear()
        self.func_list.clear()
        self.status_label.setText("")

        for name, args, expr in funcs:
            if len(args) != 1:
                continue
            self._functions.append((name, args[0], expr))

        if not self._functions:
            hint = QListWidgetItem(
                "Keine 1-argumentigen Funktionen. Beispiel:  f(x) := x^2"
            )
            hint.setFlags(Qt.ItemFlag.NoItemFlags)
            hint.setForeground(QColor("#9ca3af"))
            self.func_list.addItem(hint)
            self.func_list.blockSignals(False)
            return

        for name, var, expr in self._functions:
            item = QListWidgetItem(f"{name}({var}) = {expr}")
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            check = (
                Qt.CheckState.Checked
                if name in previously_checked or not any_checked
                else Qt.CheckState.Unchecked
            )
            item.setCheckState(check)
            item.setData(Qt.ItemDataRole.UserRole, (name, var, expr))
            self.func_list.addItem(item)
        self.func_list.blockSignals(False)

    def _on_plot_button(self) -> None:
        """Explizites Zeichnen setzt die Sicht zurueck."""
        self._force_view_reset = True
        self._plot()

    def _plot(self) -> None:
        """Zeichnet alle angekreuzten Funktionen.

        Behaelt die aktuelle Achsen-Sicht bei wiederholtem ``_plot`` (z. B.
        nach Enter im Editor), sodass Zoom und Pan erhalten bleiben.
        """
        import numpy as np

        x_min_spin = self.x_min.value()
        x_max_spin = self.x_max.value()
        if x_max_spin <= x_min_spin:
            self.status_label.setText(
                "x-Bereich ungültig: Maximum muss grösser als Minimum sein."
            )
            return

        preserve_view = (
            self._has_plotted
            and not self._force_view_reset
            and bool(self._figure.axes)
        )
        prev_xlim: tuple[float, float] | None = None
        prev_ylim: tuple[float, float] | None = None
        if preserve_view:
            prev_xlim = tuple(self._figure.axes[0].get_xlim())  # type: ignore[assignment]
            prev_ylim = tuple(self._figure.axes[0].get_ylim())  # type: ignore[assignment]

        self._figure.clear()
        ax = self._figure.add_subplot(111)

        if preserve_view and prev_xlim is not None:
            xs_min, xs_max = prev_xlim
        else:
            xs_min, xs_max = x_min_spin, x_max_spin

        sy = self._engine.sy
        xs = np.linspace(xs_min, xs_max, _N_SAMPLES_2D)
        errors: list[str] = []
        plotted = 0
        all_ys: list[Any] = []
        self._plotted_funcs = []
        self._lines = []

        from cas_rechner import Engine as _Engine

        for i in range(self.func_list.count()):
            item = self.func_list.item(i)
            if item.checkState() != Qt.CheckState.Checked:
                continue
            data = item.data(Qt.ItemDataRole.UserRole)
            if not data:
                continue
            name, var, expr_raw = data
            try:
                ns = self._engine._base_namespace()
                ns.update(self._user_vars)
                expr_sympy = self._engine._parse(_to_sympy(expr_raw), ns)
                var_sym = sy.Symbol(var)
                func = sy.lambdify(var_sym, expr_sympy, modules=["numpy"])
                ys = func(xs)
                if np.isscalar(ys):
                    ys = np.full_like(xs, float(ys))
                else:
                    ys = np.asarray(ys, dtype=float)
                (line,) = ax.plot(xs, ys, label=f"{name}({var})")
                self._plotted_funcs.append((name, var, expr_raw))
                self._lines.append(line)
                all_ys.append(ys)
                plotted += 1
            except Exception as e:
                errors.append(f"{name}: {_Engine._err(e)}")

        ax.axhline(0, color="#9ca3af", linewidth=0.6)
        ax.axvline(0, color="#9ca3af", linewidth=0.6)
        ax.grid(True, alpha=0.3)
        ax.set_xlabel("x")

        if preserve_view and prev_xlim is not None and prev_ylim is not None:
            ax.set_xlim(prev_xlim)
            ax.set_ylim(prev_ylim)
        else:
            ax.set_xlim(x_min_spin, x_max_spin)
            if self.auto_y.isChecked() and all_ys:
                stacked = np.concatenate(all_ys)
                finite = stacked[np.isfinite(stacked)]
                if finite.size:
                    lo, hi = np.percentile(finite, [1.0, 99.0])
                    if hi - lo < 1e-12:
                        hi = lo + 1.0
                    margin = (hi - lo) * 0.1
                    y_lo, y_hi = float(lo - margin), float(hi + margin)
                    ax.set_ylim(y_lo, y_hi)
                    self._set_y_spins_silent(y_lo, y_hi)
            elif not self.auto_y.isChecked():
                y_min = self.y_min.value()
                y_max = self.y_max.value()
                if y_max > y_min:
                    ax.set_ylim(y_min, y_max)

        if plotted > 0:
            ax.legend(loc="best", fontsize=9)

        ax.callbacks.connect("xlim_changed", self._on_xlim_changed)

        # Analyse-Markierungen verschwinden mit figure.clear; Liste leeren.
        self._analysis_artists = []
        self._install_span_selector(ax)

        self._canvas.draw()
        self._nav.update()

        self._has_plotted = True
        self._force_view_reset = False

        if errors:
            self.status_label.setText(" · ".join(errors))
        elif plotted == 0:
            self.status_label.setText("Keine Funktion ausgewählt.")
        else:
            self.status_label.setText("")

    def _on_xlim_changed(self, ax) -> None:
        """Tastet alle Linien auf den neuen x-Bereich neu ab."""
        if self._resampling or not self._lines:
            return
        self._resampling = True
        try:
            import numpy as np
            xlim = ax.get_xlim()
            xs = np.linspace(xlim[0], xlim[1], _N_SAMPLES_2D)
            sy = self._engine.sy
            for line, (_, var, expr_raw) in zip(
                self._lines, self._plotted_funcs
            ):
                try:
                    ns = self._engine._base_namespace()
                    ns.update(self._user_vars)
                    expr_sympy = self._engine._parse(
                        _to_sympy(expr_raw), ns
                    )
                    var_sym = sy.Symbol(var)
                    func = sy.lambdify(
                        var_sym, expr_sympy, modules=["numpy"]
                    )
                    ys = func(xs)
                    if np.isscalar(ys):
                        ys = np.full_like(xs, float(ys))
                    else:
                        ys = np.asarray(ys, dtype=float)
                    line.set_data(xs, ys)
                except Exception:
                    pass
            self._canvas.draw_idle()
        finally:
            self._resampling = False

    def _set_y_spins_silent(self, lo: float, hi: float) -> None:
        """Setzt die y-SpinBoxen ohne valueChanged-Rueckkopplung."""
        for spin, value in ((self.y_min, lo), (self.y_max, hi)):
            spin.blockSignals(True)
            spin.setValue(value)
            spin.blockSignals(False)

    # ── Analyse: Nullstelle / Maximum / Minimum ────────────────────────
    def _set_mode(self, key: str | None) -> None:
        """Schaltet einen Analyse-Modus ein oder ``None`` (Aus)."""
        for k, btn in self._mode_buttons.items():
            btn.setChecked(k == key)
        self._mode = key
        if self._span_selector is not None:
            self._span_selector.set_active(key is not None)

    def _install_span_selector(self, ax) -> None:
        """Haengt einen ``SpanSelector`` an die Achsen.

        Wird nach jedem ``_plot`` neu erzeugt, weil ``figure.clear`` den
        alten Selector entwertet.
        """
        from matplotlib.widgets import SpanSelector

        self._span_selector = SpanSelector(
            ax,
            self._on_span_select,
            direction="horizontal",
            useblit=True,
            props=dict(alpha=0.3, facecolor="#60a5fa"),
            interactive=False,
        )
        self._span_selector.set_active(self._mode is not None)

    def _on_span_select(self, a: float, b: float) -> None:
        """Wertet das gewaehlte x-Intervall je nach Modus aus."""
        if self._mode is None or not self._plotted_funcs:
            return
        if b <= a:
            return
        self._clear_analysis()
        import numpy as np

        sy = self._engine.sy
        xs = np.linspace(a, b, 2001)
        ax = self._figure.axes[0] if self._figure.axes else None
        if ax is None:
            return

        for name, var, expr_raw in self._plotted_funcs:
            try:
                ns = self._engine._base_namespace()
                ns.update(self._user_vars)
                expr = self._engine._parse(_to_sympy(expr_raw), ns)
                x_sym = sy.Symbol(var)
                f = sy.lambdify(x_sym, expr, modules=["numpy"])
                ys = f(xs)
                if np.isscalar(ys):
                    ys = np.full_like(xs, float(ys))
                else:
                    ys = np.asarray(ys, dtype=float)
                if self._mode == "zero":
                    self._mark_zeros(ax, name, expr, x_sym, xs, ys)
                elif self._mode == "max":
                    self._mark_extremum(ax, name, expr, x_sym, xs, ys, "max")
                elif self._mode == "min":
                    self._mark_extremum(ax, name, expr, x_sym, xs, ys, "min")
            except Exception:
                continue
        self._canvas.draw_idle()

    def _mark_zeros(self, ax, name, expr, x_sym, xs, ys) -> None:
        """Markiert alle Nullstellen im abgetasteten Intervall."""
        import numpy as np

        finite = np.isfinite(ys)
        if not finite.any():
            return
        sy = self._engine.sy
        roots: list[float] = []

        # (a) Strenger Vorzeichenwechsel: ys[i] * ys[i+1] < 0. Das zaehlt
        #     eine Stichprobe, die exakt auf einer Nullstelle liegt, nicht
        #     doppelt (sonst: -1, 0, +1 werden als zwei Wechsel erkannt).
        prod = ys[:-1] * ys[1:]
        strict = (prod < 0) & finite[:-1] & finite[1:]
        for idx in np.where(strict)[0]:
            x_lo, x_hi = float(xs[idx]), float(xs[idx + 1])
            y_lo, y_hi = float(ys[idx]), float(ys[idx + 1])
            x_guess = x_lo - y_lo * (x_hi - x_lo) / (y_hi - y_lo)
            x_root = x_guess
            try:
                x_root = float(sy.nsolve(expr, x_sym, x_guess))
            except Exception:
                pass
            roots.append(x_root)
        for idx in np.where(finite & (ys == 0))[0]:
            roots.append(float(xs[idx]))

        # (b) Tangentiale Nullstellen (z. B. ``x**2`` bei 0): lokale
        #     Minima von |f|, die in Relation zur Funktionsskala sehr
        #     klein sind. nsolve verfeinert, danach Verifikation mit
        #     strengerer Toleranz, damit ``x**2 + 0.001`` nicht faelsch-
        #     licherweise als Nullstelle erkannt wird.
        absy = np.abs(ys)
        finite_absy = absy[finite]
        if finite_absy.size >= 3 and len(ys) >= 3:
            scale = float(np.max(finite_absy))
            tol_detect = max(scale * 1e-4, 1e-12)
            tol_accept = max(scale * 1e-8, 1e-10)
            interior = absy[1:-1]
            is_min = (
                finite[1:-1]
                & finite[:-2]
                & finite[2:]
                & (interior < absy[:-2])
                & (interior < absy[2:])
                & (interior < tol_detect)
            )
            f_lambdified = sy.lambdify(x_sym, expr, modules=["numpy"])
            for idx in np.where(is_min)[0] + 1:
                x_guess = float(xs[idx])
                x_root = x_guess
                try:
                    x_root = float(sy.nsolve(expr, x_sym, x_guess))
                except Exception:
                    pass
                try:
                    y_check = float(f_lambdified(x_root))
                except Exception:
                    y_check = float("inf")
                if np.isfinite(y_check) and abs(y_check) < tol_accept:
                    roots.append(x_root)

        # (c) Duplikate (innerhalb 1e-6) zusammenfassen.
        roots.sort()
        unique: list[float] = []
        for r in roots:
            if not unique or abs(r - unique[-1]) > 1e-6:
                unique.append(r)
        for x_root in unique:
            self._annotate(ax, x_root, 0.0, f"{name}: x≈{x_root:.4g}")

    def _mark_extremum(
        self, ax, name, expr, x_sym, xs, ys, kind: str
    ) -> None:
        """Markiert das Maximum oder Minimum im abgetasteten Intervall."""
        import numpy as np

        finite = np.isfinite(ys)
        if not finite.any():
            return
        sy = self._engine.sy
        if kind == "max":
            masked = np.where(finite, ys, -np.inf)
            idx = int(np.argmax(masked))
        else:
            masked = np.where(finite, ys, np.inf)
            idx = int(np.argmin(masked))
        x_best, y_best = float(xs[idx]), float(ys[idx])
        # Ableitung = 0 in der Naehe - ergibt einen stabileren Extremwert
        # als ein reines Raster (kantenfern, nicht am Intervall-Rand).
        try:
            x_ref = float(sy.nsolve(sy.diff(expr, x_sym), x_sym, x_best))
            if xs[0] <= x_ref <= xs[-1]:
                f = sy.lambdify(x_sym, expr, modules=["numpy"])
                y_ref = float(f(x_ref))
                if (
                    np.isfinite(y_ref)
                    and ((kind == "max" and y_ref >= y_best)
                         or (kind == "min" and y_ref <= y_best))
                ):
                    x_best, y_best = x_ref, y_ref
        except Exception:
            pass
        label = "Max" if kind == "max" else "Min"
        self._annotate(
            ax, x_best, y_best,
            f"{name} {label}: ({x_best:.4g}, {y_best:.4g})",
        )

    def _annotate(self, ax, x: float, y: float, text: str) -> None:
        """Setzt einen Marker + Callout an (x, y)."""
        (marker,) = ax.plot(
            [x], [y], "o", markersize=8,
            color="#dc2626", zorder=5,
        )
        annot = ax.annotate(
            text, xy=(x, y), xytext=(8, 10),
            textcoords="offset points", fontsize=9,
            color="#111827",
            bbox=dict(
                boxstyle="round,pad=0.3",
                fc="#fef3c7", ec="#f59e0b",
            ),
            zorder=6,
        )
        self._analysis_artists.extend([marker, annot])

    def _clear_analysis(self) -> None:
        """Entfernt alle bestehenden Analyse-Marker von der Achse."""
        for artist in self._analysis_artists:
            try:
                artist.remove()
            except Exception:
                pass
        self._analysis_artists.clear()

    def _on_scroll(self, event) -> None:
        if event.inaxes is None:
            return
        ax = event.inaxes
        scale = 1.0 / _SCROLL_SCALE if event.button == "up" else _SCROLL_SCALE
        xdata = event.xdata
        ydata = event.ydata
        if xdata is None or ydata is None:
            return
        xlim = ax.get_xlim()
        ylim = ax.get_ylim()
        ax.set_xlim(
            xdata - (xdata - xlim[0]) * scale,
            xdata + (xlim[1] - xdata) * scale,
        )
        ax.set_ylim(
            ydata - (ydata - ylim[0]) * scale,
            ydata + (ylim[1] - ydata) * scale,
        )
        self._canvas.draw_idle()


# ── 3D-Karte ──────────────────────────────────────────────────────────────
class _Plot3DTab(QWidget):
    """Tab mit 3D-Oberflaechenplot fuer ``f(x, y)``-Definitionen."""

    def __init__(
        self,
        editor: "MathEditor",
        engine: "Engine",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._editor = editor
        self._engine = engine
        self._functions: list[tuple[str, str, str, str]] = []
        self._user_vars: dict[str, Any] = {}
        self._plotted_funcs: list[tuple[str, str, str, str]] = []
        self._has_plotted: bool = False
        self._force_view_reset: bool = False
        self._resampling: bool = False

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)
        layout.setSpacing(8)

        header = QLabel("Funktionen auswählen:")
        header.setObjectName("settingsHeading")
        layout.addWidget(header)

        self.func_list = QListWidget()
        self.func_list.setMaximumHeight(140)
        self.func_list.itemChanged.connect(lambda _it: self._plot())
        layout.addWidget(self.func_list)

        # x-Bereich.
        x_row = QHBoxLayout()
        x_row.setSpacing(6)
        x_row.addWidget(QLabel("x von"))
        self.x_min = _make_spin(-5.0)
        x_row.addWidget(self.x_min)
        x_row.addWidget(QLabel("bis"))
        self.x_max = _make_spin(5.0)
        x_row.addWidget(self.x_max)
        x_row.addStretch()
        layout.addLayout(x_row)

        # y-Bereich.
        y_row = QHBoxLayout()
        y_row.setSpacing(6)
        y_row.addWidget(QLabel("y von"))
        self.y_min = _make_spin(-5.0)
        y_row.addWidget(self.y_min)
        y_row.addWidget(QLabel("bis"))
        self.y_max = _make_spin(5.0)
        y_row.addWidget(self.y_max)
        y_row.addStretch()
        layout.addLayout(y_row)

        # z-Bereich + Auto-Z + Zeichnen.
        z_row = QHBoxLayout()
        z_row.setSpacing(6)
        z_row.addWidget(QLabel("z von"))
        self.z_min = _make_spin(-10.0)
        z_row.addWidget(self.z_min)
        z_row.addWidget(QLabel("bis"))
        self.z_max = _make_spin(10.0)
        z_row.addWidget(self.z_max)

        self.auto_z = QCheckBox("Auto-Z")
        self.auto_z.setChecked(True)
        self.auto_z.stateChanged.connect(self._on_auto_z_changed)
        z_row.addWidget(self.auto_z)
        z_row.addStretch()

        plot_btn = QPushButton("Zeichnen")
        plot_btn.setObjectName("okButton")
        plot_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        plot_btn.clicked.connect(self._on_plot_button)
        z_row.addWidget(plot_btn)
        layout.addLayout(z_row)

        self._on_auto_z_changed()

        from matplotlib.backends.backend_qtagg import (
            FigureCanvas,
            NavigationToolbar2QT,
        )
        from matplotlib.figure import Figure
        # Import registriert den ``3d``-Projektionstyp.
        from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

        self._figure = Figure(figsize=(6, 4), tight_layout=True)
        self._canvas = FigureCanvas(self._figure)
        self._nav = NavigationToolbar2QT(self._canvas, self)
        layout.addWidget(self._nav)
        layout.addWidget(self._canvas, stretch=1)

        self.status_label = QLabel("")
        self.status_label.setStyleSheet("color:#dc2626;font-size:11px;")
        self.status_label.setWordWrap(True)
        layout.addWidget(self.status_label)

    def _on_auto_z_changed(self) -> None:
        enabled = not self.auto_z.isChecked()
        self.z_min.setEnabled(enabled)
        self.z_max.setEnabled(enabled)

    def set_scan_result(
        self,
        funcs: list[tuple[str, list[str], str]],
        user_vars: dict[str, Any],
    ) -> None:
        """Filtert zweiargumentige Funktionen und befuellt die Liste."""
        self._user_vars = user_vars

        previously_checked: set[str] = set()
        any_checked = False
        for i in range(self.func_list.count()):
            item = self.func_list.item(i)
            data = item.data(Qt.ItemDataRole.UserRole)
            if data and item.checkState() == Qt.CheckState.Checked:
                previously_checked.add(data[0])
                any_checked = True

        self.func_list.blockSignals(True)
        self._functions.clear()
        self.func_list.clear()
        self.status_label.setText("")

        for name, args, expr in funcs:
            if len(args) != 2:
                continue
            self._functions.append((name, args[0], args[1], expr))

        if not self._functions:
            hint = QListWidgetItem(
                "Keine 2-argumentigen Funktionen. Beispiel:  g(x, y) := x^2 + y^2"
            )
            hint.setFlags(Qt.ItemFlag.NoItemFlags)
            hint.setForeground(QColor("#9ca3af"))
            self.func_list.addItem(hint)
            self.func_list.blockSignals(False)
            return

        # Bei 3D standardmaessig nur die erste Funktion aktivieren -
        # mehrere Oberflaechen ueberlagern sich optisch schlecht.
        for idx, (name, a1, a2, expr) in enumerate(self._functions):
            item = QListWidgetItem(f"{name}({a1}, {a2}) = {expr}")
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            default_check = (
                Qt.CheckState.Checked
                if name in previously_checked
                or (not any_checked and idx == 0)
                else Qt.CheckState.Unchecked
            )
            item.setCheckState(default_check)
            item.setData(Qt.ItemDataRole.UserRole, (name, a1, a2, expr))
            self.func_list.addItem(item)
        self.func_list.blockSignals(False)

    _CMAPS = ("viridis", "plasma", "cividis", "magma")

    def _on_plot_button(self) -> None:
        """Explizites Zeichnen setzt die Sicht zurueck."""
        self._force_view_reset = True
        self._plot()

    def _plot(self) -> None:
        """Zeichnet alle angekreuzten Flaechen als Surface-Plot.

        Behaelt Kamera-Winkel und Achsen-Limits bei wiederholtem Aufruf
        (z. B. nach Enter im Editor). Nur der ``Zeichnen``-Button setzt
        die Sicht auf die SpinBox-Werte zurueck.
        """
        import numpy as np

        x_min_v = self.x_min.value()
        x_max_v = self.x_max.value()
        y_min_v = self.y_min.value()
        y_max_v = self.y_max.value()
        if x_max_v <= x_min_v or y_max_v <= y_min_v:
            self.status_label.setText(
                "Ungültiger Bereich: Maximum muss grösser als Minimum sein."
            )
            return

        preserve_view = (
            self._has_plotted
            and not self._force_view_reset
            and bool(self._figure.axes)
        )
        prev_xlim = prev_ylim = prev_zlim = None
        prev_elev = prev_azim = None
        if preserve_view:
            old_ax = self._figure.axes[0]
            prev_xlim = tuple(old_ax.get_xlim())
            prev_ylim = tuple(old_ax.get_ylim())
            prev_zlim = tuple(old_ax.get_zlim())
            prev_elev, prev_azim = old_ax.elev, old_ax.azim

        self._figure.clear()
        ax = self._figure.add_subplot(111, projection="3d")

        # Abtastbereich: beim Sicht-Erhalt aktueller Ausschnitt, sonst
        # SpinBox-Werte.
        if preserve_view and prev_xlim is not None and prev_ylim is not None:
            xs_min, xs_max = prev_xlim
            ys_min, ys_max = prev_ylim
        else:
            xs_min, xs_max = x_min_v, x_max_v
            ys_min, ys_max = y_min_v, y_max_v

        sy = self._engine.sy
        xs = np.linspace(xs_min, xs_max, _N_SAMPLES_3D)
        ys = np.linspace(ys_min, ys_max, _N_SAMPLES_3D)
        X, Y = np.meshgrid(xs, ys)

        errors: list[str] = []
        plotted = 0
        all_zs: list[Any] = []
        self._plotted_funcs = []

        from cas_rechner import Engine as _Engine

        for i in range(self.func_list.count()):
            item = self.func_list.item(i)
            if item.checkState() != Qt.CheckState.Checked:
                continue
            data = item.data(Qt.ItemDataRole.UserRole)
            if not data:
                continue
            name, a1, a2, expr_raw = data
            try:
                ns = self._engine._base_namespace()
                ns.update(self._user_vars)
                expr_sympy = self._engine._parse(_to_sympy(expr_raw), ns)
                s1, s2 = sy.Symbol(a1), sy.Symbol(a2)
                func = sy.lambdify((s1, s2), expr_sympy, modules=["numpy"])
                Z = func(X, Y)
                if np.isscalar(Z):
                    Z = np.full_like(X, float(Z))
                else:
                    Z = np.asarray(Z, dtype=float)
                ax.plot_surface(
                    X, Y, Z,
                    cmap=self._CMAPS[plotted % len(self._CMAPS)],
                    alpha=0.85, linewidth=0, antialiased=True,
                )
                self._plotted_funcs.append((name, a1, a2, expr_raw))
                all_zs.append(Z)
                plotted += 1
            except Exception as e:
                errors.append(f"{name}: {_Engine._err(e)}")

        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.set_zlabel("z")

        if preserve_view and prev_xlim is not None and prev_ylim is not None:
            ax.set_xlim(prev_xlim)
            ax.set_ylim(prev_ylim)
            if prev_zlim is not None:
                ax.set_zlim(prev_zlim)
            if prev_elev is not None and prev_azim is not None:
                ax.view_init(elev=prev_elev, azim=prev_azim)
        else:
            ax.set_xlim(x_min_v, x_max_v)
            ax.set_ylim(y_min_v, y_max_v)
            if self.auto_z.isChecked() and all_zs:
                stacked = np.concatenate([z.ravel() for z in all_zs])
                finite = stacked[np.isfinite(stacked)]
                if finite.size:
                    lo, hi = np.percentile(finite, [1.0, 99.0])
                    if hi - lo < 1e-12:
                        hi = lo + 1.0
                    margin = (hi - lo) * 0.1
                    z_lo, z_hi = float(lo - margin), float(hi + margin)
                    ax.set_zlim(z_lo, z_hi)
                    self._set_z_spins_silent(z_lo, z_hi)
            elif not self.auto_z.isChecked():
                z_min = self.z_min.value()
                z_max = self.z_max.value()
                if z_max > z_min:
                    ax.set_zlim(z_min, z_max)

        # Bei Zoom/Pan in x oder y die Flaechen ueber dem neuen Bereich
        # neu abtasten, damit nichts abgeschnitten aussieht.
        ax.callbacks.connect("xlim_changed", self._on_lim_changed)
        ax.callbacks.connect("ylim_changed", self._on_lim_changed)

        self._canvas.draw()
        self._nav.update()
        self._has_plotted = True
        self._force_view_reset = False

        if errors:
            self.status_label.setText(" · ".join(errors))
        elif plotted == 0:
            self.status_label.setText("Keine Funktion ausgewählt.")
        else:
            self.status_label.setText("")

    def _on_lim_changed(self, ax) -> None:
        """Tastet alle Flaechen ueber dem neuen x/y-Bereich neu ab.

        ``plot_surface`` laesst sich nicht in-place aktualisieren; wir
        entfernen alle Surface-Collections der Achse und zeichnen die
        gespeicherten Funktionen auf dem neuen Raster erneut. Kamera-
        Winkel und z-Limit bleiben dabei erhalten.
        """
        if self._resampling or not self._plotted_funcs:
            return
        self._resampling = True
        try:
            import numpy as np

            new_xlim = ax.get_xlim()
            new_ylim = ax.get_ylim()
            for coll in list(ax.collections):
                try:
                    coll.remove()
                except Exception:
                    pass

            sy = self._engine.sy
            xs = np.linspace(new_xlim[0], new_xlim[1], _N_SAMPLES_3D)
            ys = np.linspace(new_ylim[0], new_ylim[1], _N_SAMPLES_3D)
            X, Y = np.meshgrid(xs, ys)
            for idx, (_, a1, a2, expr_raw) in enumerate(self._plotted_funcs):
                try:
                    ns = self._engine._base_namespace()
                    ns.update(self._user_vars)
                    expr_sympy = self._engine._parse(
                        _to_sympy(expr_raw), ns
                    )
                    s1, s2 = sy.Symbol(a1), sy.Symbol(a2)
                    func = sy.lambdify(
                        (s1, s2), expr_sympy, modules=["numpy"]
                    )
                    Z = func(X, Y)
                    if np.isscalar(Z):
                        Z = np.full_like(X, float(Z))
                    else:
                        Z = np.asarray(Z, dtype=float)
                    ax.plot_surface(
                        X, Y, Z,
                        cmap=self._CMAPS[idx % len(self._CMAPS)],
                        alpha=0.85, linewidth=0, antialiased=True,
                    )
                except Exception:
                    continue
            self._canvas.draw_idle()
        finally:
            self._resampling = False

    def _set_z_spins_silent(self, lo: float, hi: float) -> None:
        for spin, value in ((self.z_min, lo), (self.z_max, hi)):
            spin.blockSignals(True)
            spin.setValue(value)
            spin.blockSignals(False)


# ── Phasor-Extraktion ─────────────────────────────────────────────────────
def _extract_phasors(engine: "Engine") -> list[tuple[str, float, float]]:
    """Liest komplexe Variablen aus ``engine.last_user_vars``.

    Returns:
        Liste von ``(name, betrag, winkel_rad)``. Rein reelle Werte und
        nicht-numerische Ausdrücke werden übersprungen.
    """
    result: list[tuple[str, float, float]] = []
    sy = engine.sy
    for name, val in getattr(engine, "last_user_vars", {}).items():
        try:
            numeric = sy.N(val)
            if not getattr(numeric, "is_number", False):
                continue
            re_part = float(sy.re(numeric))
            im_part = float(sy.im(numeric))
            c = complex(re_part, im_part)
            if abs(c.imag) < 1e-10 * (abs(c.real) + abs(c.imag) + 1e-30):
                continue
            r, theta = cmath.polar(c)
            result.append((name, r, theta))
        except Exception:
            continue
    return result


# ── Phasor-Karte ───────────────────────────────────────────────────────────
class _PhasorTab(QWidget):
    """Tab mit Phasor-Diagramm und Checkbox-Liste zum An-/Abwählen."""

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        # Alle bekannten Phasoren (von der Engine geliefert).
        self._all_phasors: list[tuple[str, float, float]] = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 8)
        layout.setSpacing(8)

        header = QLabel("Phasoren anzeigen:")
        header.setObjectName("settingsHeading")
        layout.addWidget(header)

        # Checkbox-Liste ──────────────────────────────────────────────────
        self.func_list = QListWidget()
        self.func_list.setMaximumHeight(130)
        self.func_list.itemChanged.connect(self._on_check_changed)
        layout.addWidget(self.func_list)

        # Phasor-Zeichenfläche ─────────────────────────────────────────────
        self.diagram = PhasorWidget()
        layout.addWidget(self.diagram, stretch=1)

    # ── Datenbindung ──────────────────────────────────────────────────────
    def set_phasors(self, phasors: list[tuple[str, float, float]]) -> None:
        """Aktualisiert die Liste und das Diagramm.

        Bereits angehakte Einträge bleiben angehakt, neue Einträge kommen
        standardmäßig angehakt (konsistent mit 2D-/3D-Tab).
        """
        previously_checked: set[str] = set()
        any_prev = False
        for i in range(self.func_list.count()):
            item = self.func_list.item(i)
            name = item.data(Qt.ItemDataRole.UserRole)
            if name and item.checkState() == Qt.CheckState.Checked:
                previously_checked.add(name)
                any_prev = True

        self._all_phasors = phasors
        self.func_list.blockSignals(True)
        self.func_list.clear()

        if not phasors:
            hint = QListWidgetItem(
                "Keine komplexen Variablen.  Beispiel:  U := 5*exp(j*pi/6)"
            )
            hint.setFlags(Qt.ItemFlag.NoItemFlags)
            hint.setForeground(QColor("#9ca3af"))
            self.func_list.addItem(hint)
            self.func_list.blockSignals(False)
            self.diagram.set_phasors([])
            return

        for name, r, theta in phasors:
            deg = math.degrees(theta) % 360.0
            label = f"{name}   {r:.3g} ∠ {deg:.1f}°"
            item = QListWidgetItem(label)
            item.setFlags(item.flags() | Qt.ItemFlag.ItemIsUserCheckable)
            checked = name in previously_checked or not any_prev
            item.setCheckState(
                Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked
            )
            item.setData(Qt.ItemDataRole.UserRole, name)
            self.func_list.addItem(item)

        self.func_list.blockSignals(False)
        self._refresh_diagram()

    def _on_check_changed(self, _item: QListWidgetItem) -> None:
        self._refresh_diagram()

    def _refresh_diagram(self) -> None:
        """Zeigt nur die angehakten Phasoren im Diagramm."""
        checked: set[str] = set()
        for i in range(self.func_list.count()):
            item = self.func_list.item(i)
            name = item.data(Qt.ItemDataRole.UserRole)
            if name and item.checkState() == Qt.CheckState.Checked:
                checked.add(name)
        visible = [(n, r, t) for n, r, t in self._all_phasors if n in checked]
        self.diagram.set_phasors(visible)


# ── Panel mit Tab-Wechsel ─────────────────────────────────────────────────
class PlotPanel(QWidget):
    """Eingebetteter Graph-Bereich mit 2D- und 3D-Tab."""

    def __init__(
        self,
        editor: "MathEditor",
        engine: "Engine",
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._editor = editor
        self._engine = engine

        self.setObjectName("plotPanel")

        outer = QVBoxLayout(self)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        self.tabs = QTabWidget()
        self.tab_2d = _Plot2DTab(editor, engine)
        self.tab_3d = _Plot3DTab(editor, engine)
        self.tab_phasor = _PhasorTab()
        self.tabs.addTab(self.tab_2d, "2D")
        self.tabs.addTab(self.tab_3d, "3D")
        self.tabs.addTab(self.tab_phasor, "Phasor")
        self.tabs.currentChanged.connect(self._on_tab_changed)
        outer.addWidget(self.tabs)

        # Erste Scan-Befuellung der Listen (ohne Plot).
        self._scan_only()

    def showEvent(self, event) -> None:  # type: ignore[override]
        super().showEvent(event)
        self._scan_only()

    def _scan_only(self) -> None:
        """Scannt den Editor und aktualisiert alle Listen ohne Plot."""
        funcs, user_vars = _scan_editor(self._editor, self._engine)
        self.tab_2d.set_scan_result(funcs, user_vars)
        self.tab_3d.set_scan_result(funcs, user_vars)
        self.tab_phasor.set_phasors(_extract_phasors(self._engine))

    def _plot(self) -> None:
        """Scannt den Editor und zeichnet die aktuell sichtbare Karte.

        Wird vom ``CasCalculator`` nach jedem Editor-Enter aufgerufen.
        """
        funcs, user_vars = _scan_editor(self._editor, self._engine)
        self.tab_2d.set_scan_result(funcs, user_vars)
        self.tab_3d.set_scan_result(funcs, user_vars)
        self.tab_phasor.set_phasors(_extract_phasors(self._engine))
        current = self.tabs.currentWidget()
        if hasattr(current, "_plot"):
            current._plot()  # type: ignore[attr-defined]

    def _on_tab_changed(self, _index: int) -> None:
        """Zeichnet die neu aktivierte Karte mit dem aktuellen Editor-Stand."""
        self._plot()


