"""Haupt-Einstiegspunkt: App-Shell mit Tool-Registry.

Dieses Modul ist bewusst schlank gehalten. Es liefert nur das
Grundgeruest (Hauptfenster, Tab-Leiste, Tool-Stack) und eine
Registry, in der neue Tools mit einer einzigen Zeile eingehaengt
werden koennen:

    TOOLS: list[ToolDef] = [
        ToolDef("Lexikon", lambda ctx: LexiconWidget(...)),
        ToolDef("CAS Rechner", lambda ctx: CasCalculator()),
        # Neues Tool hier anfuegen.
    ]

Jedes Tool ist ein QWidget und verwaltet seine eigene Oberflaeche
(Toolbar, Navigation, Sidebars) selbst. Ueber ``AppContext`` koennen
Tools miteinander kommunizieren, ohne sich gegenseitig zu kennen:

    ctx.switch_to("CAS Rechner")      - Tab wechseln
    ctx.get_tool("CAS Rechner")       - Referenz auf anderes Tool

Abkuerzungen (Initialnotation):
    CAS - Computer Algebra System.
    GUI - Graphical User Interface.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, TypeAlias

from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QInputDialog,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QTabBar,
    QVBoxLayout,
    QWidget,
)

from cas_rechner import CasCalculator
from lexikon import LexiconWidget, build_stylesheet


# ── Tool-Registry-API ─────────────────────────────────────────────────────────
@dataclass
class AppContext:
    """Service-Objekt, das jedem Tool uebergeben wird.

    Ermoeglicht Tools, den Tab zu wechseln oder eine Referenz auf
    ein anderes Tool anzufordern, ohne direkt die ``MainWindow``-Klasse
    zu kennen.
    """

    switch_to: Callable[[str], None]
    get_tool: Callable[[str], QWidget | None]


ToolFactory: TypeAlias = Callable[[AppContext], QWidget]


@dataclass
class ToolDef:
    """Beschreibt ein in der Tab-Leiste verfuegbares Tool."""

    name: str
    factory: ToolFactory


# ── CAS-Tab-Manager ───────────────────────────────────────────────────────────
class CasTabManager(QWidget):
    """Verwaltet mehrere unabhaengige CAS-Rechner-Instanzen als Tabs.

    Jeder Tab hat seine eigene ``CasCalculator``-Instanz mit eigenem
    SymPy-Namespace, eigenen Variablen und eigenem Graphen. Es gibt
    keinerlei Datenaustausch zwischen den Tabs.

    Bedienung:
        + Neu         Neuen Tab anlegen
        Doppelklick   Tab umbenennen
        ×             Tab schliessen (letzter Tab kann nicht geschlossen werden)
        Ctrl+T        Neuen Tab per Tastatur anlegen
    """

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._calcs: list[CasCalculator] = []
        self._build_ui()
        self._add_tab("CAS 1")

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Tab-Zeile ────────────────────────────────────────────────────
        bar_row = QWidget()
        bar_row.setObjectName("casTabRow")
        bar_row.setFixedHeight(36)
        bar_hl = QHBoxLayout(bar_row)
        bar_hl.setContentsMargins(6, 3, 6, 0)
        bar_hl.setSpacing(4)

        self._tab_bar = QTabBar()
        self._tab_bar.setObjectName("casTabBar")
        self._tab_bar.setTabsClosable(True)
        self._tab_bar.setExpanding(False)
        self._tab_bar.currentChanged.connect(self._on_tab_changed)
        self._tab_bar.tabCloseRequested.connect(self._close_tab)
        self._tab_bar.tabBarDoubleClicked.connect(self._rename_tab)
        bar_hl.addWidget(self._tab_bar)

        add_btn = QPushButton("+")
        add_btn.setObjectName("casAddTabBtn")
        add_btn.setFixedSize(26, 26)
        add_btn.setToolTip("Neuen CAS-Tab erstellen  (Ctrl+T)")
        add_btn.clicked.connect(lambda: self._add_tab())
        bar_hl.addWidget(add_btn)
        bar_hl.addStretch()

        root.addWidget(bar_row)

        # ── Inhalt-Stack ─────────────────────────────────────────────────
        self._stack = QStackedWidget()
        root.addWidget(self._stack, stretch=1)

        # Tastenkuerzel Ctrl+T
        QShortcut(QKeySequence("Ctrl+T"), self).activated.connect(
            lambda: self._add_tab()
        )

    # ── Tab-Verwaltung ────────────────────────────────────────────────────
    def _add_tab(self, name: str | None = None) -> None:
        """Erzeugt eine neue, vollstaendig unabhaengige CAS-Instanz."""
        name = name or f"CAS {len(self._calcs) + 1}"
        calc = CasCalculator()
        self._calcs.append(calc)
        self._stack.addWidget(calc)
        self._tab_bar.addTab(name)
        self._tab_bar.setCurrentIndex(self._tab_bar.count() - 1)

    def _on_tab_changed(self, idx: int) -> None:
        if 0 <= idx < len(self._calcs):
            self._stack.setCurrentIndex(idx)

    def _close_tab(self, idx: int) -> None:
        if self._tab_bar.count() <= 1:
            return  # Letzten Tab nicht schliessen.
        self._tab_bar.removeTab(idx)
        calc = self._calcs.pop(idx)
        self._stack.removeWidget(calc)
        calc.deleteLater()

    def _rename_tab(self, idx: int) -> None:
        current = self._tab_bar.tabText(idx)
        name, ok = QInputDialog.getText(
            self, "Tab umbenennen", "Neuer Name:", text=current
        )
        if ok and name.strip():
            self._tab_bar.setTabText(idx, name.strip())

    # ── Oeffentliche API (kompatibel mit CasCalculator) ───────────────────
    def insert_formula(self, formula: str) -> None:
        """Leitet die Formel an den aktiven Tab weiter."""
        idx = self._tab_bar.currentIndex()
        if 0 <= idx < len(self._calcs):
            self._calcs[idx].insert_formula(formula)


# ── Tool-Registry (hier neue Tools eintragen) ─────────────────────────────────
def _make_lexikon(ctx: AppContext) -> QWidget:
    """Erstellt das Lexikon-Widget mit Formel-Uebergabe an den CAS-Rechner."""
    from PySide6.QtWidgets import QApplication

    def send_formula(formula: str) -> None:
        cas = ctx.get_tool("CAS Rechner")
        if cas is not None and hasattr(cas, "insert_formula"):
            cas.insert_formula(formula)
            ctx.switch_to("CAS Rechner")

    def apply_style(preset: str) -> None:
        QApplication.instance().setStyleSheet(build_stylesheet(preset))

    return LexiconWidget(on_send_formula=send_formula, on_style_changed=apply_style)


TOOLS: list[ToolDef] = [
    ToolDef("Lexikon", _make_lexikon),
    ToolDef("CAS Rechner", lambda _ctx: CasTabManager()),
]


# ── Tab-Leiste ────────────────────────────────────────────────────────────────
class TabBar(QWidget):
    """Horizontale Tab-Leiste.

    Wird mit den Tool-Namen befuellt und delegiert den Wechsel an den
    uebergebenen Callback.
    """

    def __init__(
        self,
        names: list[str],
        on_switch: Callable[[int], None],
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self.setFixedHeight(38)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(8, 0, 8, 0)
        layout.setSpacing(2)
        self._on_switch = on_switch
        self.tabs: list[QPushButton] = []
        for index, name in enumerate(names):
            button = QPushButton(name)
            button.setCheckable(True)
            button.setChecked(index == 0)
            button.clicked.connect(
                lambda _checked, idx=index: self.select(idx)
            )
            layout.addWidget(button)
            self.tabs.append(button)
        layout.addStretch()

    def select(self, index: int) -> None:
        """Markiert den Tab mit gegebenem Index und loest den Wechsel aus."""
        for i, button in enumerate(self.tabs):
            button.setChecked(i == index)
        self._on_switch(index)


# ── Hauptfenster ──────────────────────────────────────────────────────────────
class MainWindow(QMainWindow):
    """App-Shell: Kopfzeile, Tab-Leiste und Tool-Stack.

    Kennt die einzelnen Tools nur ueber die ``TOOLS``-Registry und
    instanziiert sie in der angegebenen Reihenfolge. Alles andere
    (Toolbars, Navigation, Sidebars) verwaltet jedes Tool selbst.
    """

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Elektronik Lexikon")
        self.setMinimumSize(960, 680)
        self._tools_by_name: dict[str, QWidget] = {}
        self._tool_order: list[str] = [t.name for t in TOOLS]
        self._build_ui()

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Kopfzeile mit Titel.
        header = QWidget()
        header.setObjectName("appHeader")
        header.setFixedHeight(52)
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(8, 8, 8, 8)
        header_title = QLabel("Elektronik Lexikon")
        header_title.setObjectName("headerTitle")
        header_layout.addWidget(header_title)
        header_layout.addStretch()
        main_layout.addWidget(header)

        # Tab-Leiste.
        self.tab_bar = TabBar(
            [t.name for t in TOOLS], on_switch=self._on_tab_switch
        )
        main_layout.addWidget(self.tab_bar)

        # Tool-Stack.
        self.stack = QStackedWidget()
        ctx = AppContext(
            switch_to=self.switch_to, get_tool=self._tools_by_name.get
        )
        for tool in TOOLS:
            widget = tool.factory(ctx)
            self._tools_by_name[tool.name] = widget
            self.stack.addWidget(widget)
        main_layout.addWidget(self.stack, stretch=1)

    # ── Tab-Wechsel ───────────────────────────────────────────────────────────
    def closeEvent(self, event) -> None:  # type: ignore[override]
        for widget in self._tools_by_name.values():
            if hasattr(widget, "save_state"):
                widget.save_state()
        super().closeEvent(event)

    def _on_tab_switch(self, index: int) -> None:
        self.stack.setCurrentIndex(index)

    def switch_to(self, name: str) -> None:
        """Wechselt zum Tool mit gegebenem Namen."""
        if name not in self._tool_order:
            return
        index = self._tool_order.index(name)
        self.tab_bar.select(index)


# ── Hauptprogramm ─────────────────────────────────────────────────────────────
def main() -> None:
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setStyleSheet(build_stylesheet("Kraftpapier"))
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
