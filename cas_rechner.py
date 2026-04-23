"""CAS-Rechner: Komplett-Widget im Stil des Texas-Instruments NSpire.

Das Modul besteht aus vier Hauptteilen:

    * ``Engine``        - SymPy-basierte Auswertung mit Zuweisungen
                          (``:=``), Einheiten und Zahlenformat-Optionen
                          (Standard, SIC, ENG).
    * ``MathEditor``    - strukturierter zweidimensionaler Formel-Editor
                          (siehe Modul ``math_editor``) mit Bruechen,
                          Wurzeln, Exponent, Subscript, Summe, Integral
                          sowie Vektor/Matrix. Multi-Line: jede Zeile ist
                          ein eigener Ausdruck.
    * ``CasViewModel``  - Anwendungszustand (Einstellungen, Engine,
                          Hilfe-Modus). Keine GUI-Abhaengigkeiten.
    * ``CasCalculator`` - View: Zusammenbau mit Toolbar (Hilfe,
                          Einstellungen, Leeren) und Hilfe-Ansicht.

Editor-Bedienung siehe ``math_editor.py``.

Syntax, die die Engine versteht:

    * ``:=``       globale Zuweisung (gilt im ganzen Dokument).
    * ``=``        Gleichung (Eq) - wird mit den globalen Werten
                   verglichen.
    * ``x^2``      Potenz (intern als ``x**2``).
    * ``sqrt(x)``  Wurzel.
    * ``π``, ``∞``, ``ℯ`` Konstanten (Euler-Zahl auch als ``e``).
    * ``phi`` Goldener Schnitt, ``e`` Euler-Zahl.
    * Physik: ``c``, ``G``, ``g_n``, ``mu0``, ``eps0``, ``kB``, ``NA``,
      ``qe``, ``hP``, ``hbar``, ``Rgas``, ``sigmaSB``, ``me``, ``mp``.
    * ``|x|``      Betrag.
    * ``2x``       implizite Multiplikation.
    * ``# ...``    Kommentarzeile (wird nicht ausgewertet).

Hilfe-Lexikon: Markdown-Dateien (mit YAML-Frontmatter) im Ordner
``cas_hilfe/`` neben dieser Datei werden automatisch gelistet.

Abkuerzungen (Initialnotation):
    CAS  - Computer Algebra System (symbolische Mathematik).
    SIC  - scientific notation (wissenschaftliche Notation).
    ENG  - engineering notation (Ingenieur-Notation).
    RAD  - Radiant (Bogenmass).
    DEG  - Degree (Grad).
    SI   - Systeme International d'Unites.
    TI   - Texas Instruments.
    YAML - YAML Ain't Markup Language.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Callable

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QButtonGroup,
    QDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSpinBox,
    QSplitter,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from lexikon import LexiconWidget
from math_editor import MathEditor

# ── Modul-Konstanten ──────────────────────────────────────────────────────────
HELP_FOLDER: Path = Path(__file__).parent / "cas_hilfe"

# Lazy-Cache fuer den Einheiten-Namespace: wird erst beim ersten Aufruf
# gebaut, weil das Importieren von ``sympy.physics.units`` messbar Zeit
# kostet.
_UNITS_CACHE: dict[str, Any] | None = None

# Hochgestellte Ziffern fuer die SIC-/ENG-Notation.
_SUPERSCRIPT_DIGITS: dict[int, int] = str.maketrans("0123456789-+", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻⁺")

# Zuordnung Zehner-Exponent -> SI-Praefix (fuer ENG-Darstellung).
_PREFIX_FOR_EXP3: dict[int, str] = {
    24: "Y", 21: "Z", 18: "E", 15: "P", 12: "T", 9: "G", 6: "M", 3: "k",
    0: "", -3: "m", -6: "µ", -9: "n", -12: "p", -15: "f", -18: "a",
    -21: "z", -24: "y",
}

# Einheiten, die per Praefix (k, M, m, ...) skaliert werden duerfen.
_UNITS_WITH_PREFIX: set[str] = {
    "m", "s", "A", "K", "mol", "N", "J", "W", "Pa", "Hz",
    "V", "Ω", "F", "C", "T", "H", "Wb", "S", "g", "L", "eV",
}


# ── Vorverarbeitung NSpire-Schreibweise nach SymPy ────────────────────────────
def to_sympy(s: str) -> str:
    """Uebersetzt die NSpire-Schreibweise in SymPy-Schreibweise.

    ``:=`` wird absichtlich nicht angefasst - das Marker-Zeichen wird
    weiter oben in der Auswertung als globale Zuweisung separat
    verarbeitet.
    """
    s = s.strip()
    s = s.replace("^", "**")
    s = re.sub(r"√\s*\(([^)]+)\)", r"sqrt(\1)", s)
    s = re.sub(r"√([A-Za-z0-9_.]+)", r"sqrt(\1)", s)
    s = re.sub(r"\|([^|]+)\|", r"Abs(\1)", s)
    s = s.replace("π", "pi").replace("∞", "oo").replace("ℯ", "e")
    # Einheiten-Praefix: Ziffer direkt vor _ → implizite Multiplikation.
    # Muss vor der allgemeinen Ziffern-Alpha-Regel kommen.
    s = re.sub(r"(\d)(_)", r"\1*_", s)
    s = re.sub(r"(\d)\s*([A-Za-z(])", r"\1*\2", s)
    return s


def rewrite_equals_as_eq(s: str) -> str:
    """Ersetzt ``=`` durch ``Eq(lhs, rhs)`` klammer- und kommabewusst.

    SymPys eingebautes ``convert_equals_signs`` arbeitet tokenbasiert und
    stolpert ueber ``solve(x^2 = 4, x)``: Dort wird das Komma mit in die
    Eq-Argumente gezogen (``Eq(x^2, 4, x)``). Diese Implementierung
    versteht Klammern und Kommas und begrenzt die Ausdruecke links und
    rechts vom ``=`` korrekt.

    Nicht angefasst werden: ``==``, ``!=``, ``<=``, ``>=``, ``:=``.
    """
    positions: list[int] = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == "=":
            prev = s[i - 1] if i > 0 else ""
            nxt = s[i + 1] if i + 1 < n else ""
            if prev in "=<>!:" or nxt == "=":
                i += 1
                continue
            positions.append(i)
        i += 1

    if not positions:
        return s

    # Rueckwaerts arbeiten, damit die Positionen links vom Ersetzungspunkt
    # stabil bleiben.
    for pos in reversed(positions):
        # Linke Grenze: bis Komma, oeffnende Klammer auf Tiefe 0 oder
        # Stringanfang.
        left = pos - 1
        depth = 0
        while left >= 0:
            c = s[left]
            if c in ")]}":
                depth += 1
            elif c in "([{":
                if depth == 0:
                    break
                depth -= 1
            elif c == "," and depth == 0:
                break
            left -= 1
        left_start = left + 1

        # Rechte Grenze analog.
        right = pos + 1
        depth = 0
        while right < len(s):
            c = s[right]
            if c in "([{":
                depth += 1
            elif c in ")]}":
                if depth == 0:
                    break
                depth -= 1
            elif c == "," and depth == 0:
                break
            right += 1

        lhs = s[left_start:pos].strip()
        rhs = s[pos + 1:right].strip()
        if not lhs or not rhs:
            continue  # z. B. "a = " - keine Umformung.
        s = s[:left_start] + f"Eq({lhs}, {rhs})" + s[right:]

    return s


def find_cycle(assigns: dict[str, str]) -> list[str] | None:
    """Sucht einen Zyklus in den globalen Zuweisungen.

    Gibt einen Pfad der Zyklus-Knoten zurueck oder ``None``, wenn kein
    Zyklus existiert.
    """
    graph: dict[str, set[str]] = {
        v: {
            u for u in assigns
            if u != v and re.search(rf"\b{re.escape(u)}\b", e)
        }
        for v, e in assigns.items()
    }

    def dfs(
        node: str, path: list[str], visited: set[str]
    ) -> list[str] | None:
        for neighbour in graph.get(node, ()):
            if neighbour in path:
                return path[path.index(neighbour):] + [neighbour]
            if neighbour in visited:
                continue
            result = dfs(neighbour, path + [neighbour], visited | {neighbour})
            if result:
                return result
        return None

    for v in graph:
        result = dfs(v, [v], {v})
        if result:
            return result
    return None


# ── Einstellungen ─────────────────────────────────────────────────────────────
class Settings:
    """Laufzeit-Einstellungen des Rechners.

    Attributes:
        angle_mode: ``"RAD"`` (Standard) oder ``"DEG"``.
        number_format: ``"auto"`` (exakt bzw. Bruch), ``"SIC"`` oder
            ``"ENG"``.
        decimal_places: Anzahl Nachkommastellen (Standard 6).
    """

    def __init__(self) -> None:
        self.angle_mode: str = "RAD"
        self.number_format: str = "auto"
        self.decimal_places: int = 6


# ── Einheiten-Namespace ───────────────────────────────────────────────────────
def _build_units_namespace() -> dict[str, Any]:
    """Liefert ein Dict, das ``_name`` auf SymPy-Einheits-Ausdruecke abbildet.

    Enthaelt auch alle gaengigen Praefix-Kombinationen (``_km``, ``_µm``,
    ``_nF``, ``_MHz``, ...).
    """
    global _UNITS_CACHE
    if _UNITS_CACHE is not None:
        return _UNITS_CACHE

    import sympy.physics.units as u
    from sympy import Rational

    # SI-Grundeinheiten und gaengige abgeleitete Einheiten.
    base_units: dict[str, Any] = {
        "m":   u.meter,
        "kg":  u.kilogram,
        "s":   u.second,
        "A":   u.ampere,
        "K":   u.kelvin,
        "mol": u.mole,
        "cd":  u.candela,
        "N":   u.newton,
        "J":   u.joule,
        "W":   u.watt,
        "Pa":  u.pascal,
        "Hz":  u.hertz,
        "V":   u.volt,
        "Ohm": u.ohm,
        "ohm": u.ohm,
        "F":   u.farad,
        "C":   u.coulomb,
        "T":   u.tesla,
        "H":   u.henry,
        "Wb":  u.weber,
        "S":   u.siemens,
        "g":   u.gram,
        "L":   u.liter,
        "min": u.minute,
        "h":   u.hour,
    }
    # Optionale Einheiten, die in manchen SymPy-Versionen fehlen.
    for name, attr in [("d", "day"), ("eV", "electronvolt")]:
        if hasattr(u, attr):
            base_units[name] = getattr(u, attr)

    r = Rational
    prefixes: list[tuple[str, Any]] = [
        ("Y", 10**24), ("Z", 10**21), ("E", 10**18), ("P", 10**15),
        ("T", 10**12), ("G", 10**9), ("M", 10**6), ("k", 10**3),
        ("h", 100), ("da", 10),
        ("d", r(1, 10)), ("c", r(1, 100)), ("m", r(1, 1000)),
        ("u", r(1, 10**6)),  ("µ", r(1, 10**6)),
        ("n", r(1, 10**9)),  ("p", r(1, 10**12)),
        ("f", r(1, 10**15)), ("a", r(1, 10**18)),
        ("z", r(1, 10**21)), ("y", r(1, 10**24)),
    ]

    # Welche Einheiten duerfen praefixiert werden? ``kg`` schliessen wir
    # aus (bereits praefigiert), ebenso die Zeiteinheiten min/h/d.
    prefixable = [
        "m", "s", "A", "K", "mol", "N", "J", "W", "Pa", "Hz",
        "V", "Ohm", "ohm", "F", "C", "T", "H", "Wb", "S",
        "g", "L", "eV",
    ]

    ns: dict[str, Any] = {}
    # Basiseinheiten zuerst, damit sie bei Namenskollisionen gewinnen.
    for name, value in base_units.items():
        ns["_" + name] = value

    for unit_name in prefixable:
        if unit_name not in base_units:
            continue
        unit_value = base_units[unit_name]
        for prefix_name, prefix_factor in prefixes:
            key = "_" + prefix_name + unit_name
            if key in ns:
                continue  # Basiseinheit hat Vorrang.
            ns[key] = prefix_factor * unit_value

    _UNITS_CACHE = ns
    return ns


# ── SIC- / ENG-Formatierung ───────────────────────────────────────────────────
def _superscript(n: int) -> str:
    """Liefert die Zahl ``n`` in hochgestellten Ziffern."""
    return str(n).translate(_SUPERSCRIPT_DIGITS)


def _scientific_parts(x: float) -> tuple[float, int]:
    """Zerlegt ``x`` in Mantisse und Zehnerexponent.

    Returns:
        ``(mantissa, exp10)`` mit ``1 <= |mantissa| < 10``.
    """
    import math
    if x == 0:
        return (0.0, 0)
    sign = -1 if x < 0 else 1
    ax = abs(x)
    exp10 = int(math.floor(math.log10(ax)))
    mant = sign * ax / 10**exp10
    return (mant, exp10)


def _engineering_parts(x: float) -> tuple[float, int]:
    """Zerlegt ``x`` fuer Ingenieur-Notation.

    Returns:
        ``(mantissa, exp3)`` mit ``1 <= |mantissa| < 1000`` und ``exp3``
        als Vielfaches von 3.
    """
    import math
    if x == 0:
        return (0.0, 0)
    sign = -1 if x < 0 else 1
    ax = abs(x)
    exp10 = int(math.floor(math.log10(ax)))
    exp3 = (exp10 // 3) * 3
    mant = sign * ax / 10**exp3
    return (mant, exp3)


def _format_mantissa(mant: float, places: int) -> str:
    """Praesentiert eine Mantisse: Nachkommastellen setzen, Nullen kappen."""
    s = f"{mant:.{places}f}"
    if "." in s:
        s = s.rstrip("0").rstrip(".")
    return s if s else "0"


def format_number_scientific(x: float, places: int = 6) -> str:
    """Formatiert ``x`` in wissenschaftlicher Notation (SIC)."""
    mant, exp10 = _scientific_parts(x)
    mant_s = _format_mantissa(mant, places)
    if exp10 == 0:
        return mant_s
    return f"{mant_s}·10{_superscript(exp10)}"


def format_number_engineering(x: float, places: int = 6) -> tuple[str, int]:
    """Formatiert ``x`` in Ingenieur-Notation (ENG).

    Returns:
        Tupel ``(mantisse_str, exp3)``. ``exp3`` wird zusaetzlich
        zurueckgegeben, damit der Aufrufer bei Einheiten direkt den
        passenden SI-Praefix waehlen kann.
    """
    mant, exp3 = _engineering_parts(x)
    mant_s = _format_mantissa(mant, places)
    return mant_s, exp3


def _unit_allows_prefix(unit_text: str) -> bool:
    """Prueft, ob ``unit_text`` durch einen SI-Praefix erweitert werden darf.

    True, wenn der Text genau ein Einheiten-Kuerzel (ggf. mit fuehrendem ``_``)
    ohne Multiplikation oder Potenz ist.
    """
    t = unit_text.strip().lstrip("_")
    if not t:
        return False
    if any(c in t for c in "·*/^ "):
        return False
    return t in _UNITS_WITH_PREFIX


# ── Zusatzfunktionen (TI-NSpire-Stil) ─────────────────────────────────────────
def _build_extra_functions(sy: Any) -> dict[str, Any]:
    """Liefert ein Namespace-Dict mit TI-artigen Zusatz-Funktionen.

    Wird in ``Engine._base_namespace`` mit dem SymPy-Namespace gemerged.

    Konvention: Wrapper akzeptieren sowohl SymPy-Matrix als auch
    Python-Listen (werden intern in ``Matrix`` konvertiert), damit
    Listen-Eingaben wie ``[1, 2, 3]`` direkt als Vektor gelten.
    """
    matrix_cls = sy.Matrix

    def _to_matrix(v: Any) -> Any:
        """Konvertiert Liste/Tuple in ``Matrix``; ``Matrix`` bleibt ``Matrix``."""
        if isinstance(v, sy.MatrixBase):
            return v
        if isinstance(v, (list, tuple)):
            if v and isinstance(v[0], (list, tuple)):
                return matrix_cls(v)
            return matrix_cls(v)
        return matrix_cls([v])

    def _to_flat_list(v: Any) -> list[Any]:
        """Wandelt Matrix oder geschachtelte Liste in eine flache Liste."""
        if isinstance(v, sy.MatrixBase):
            return list(v)
        if isinstance(v, (list, tuple)):
            out: list[Any] = []
            for x in v:
                if isinstance(x, (list, tuple)):
                    out.extend(x)
                else:
                    out.append(x)
            return out
        return [v]

    ns: dict[str, Any] = {}

    # ── Analysis ───────────────────────────────────────────────────────────
    def deriv(f: Any, x: Any, n: int = 1) -> Any:
        return sy.diff(f, x, n)

    def integral_fn(f: Any, x: Any, a: Any = None, b: Any = None) -> Any:
        if a is None and b is None:
            return sy.integrate(f, x)
        return sy.integrate(f, (x, a, b))

    def taylor(f: Any, x: Any, a: Any = 0, n: int = 6) -> Any:
        return sy.series(f, x, a, n + 1).removeO()

    def _critical_points(f: Any, x: Any) -> list[Any]:
        df = sy.diff(f, x)
        sols = sy.solve(df, x)
        if not isinstance(sols, list):
            sols = [sols]
        return [s for s in sols if getattr(s, "is_real", None) is not False]

    def _in_interval(c: Any, a: Any, b: Any) -> bool:
        try:
            return float(a) <= float(c) <= float(b)
        except Exception:
            return True

    def fMin(f: Any, x: Any, a: Any = None, b: Any = None) -> Any:
        if a is not None and b is not None:
            cps = _critical_points(f, x)
            candidates = [c for c in cps if _in_interval(c, a, b)] + [a, b]
            values = [(c, sy.simplify(f.subs(x, c))) for c in candidates]
            values.sort(key=lambda t: float(t[1]))
            return values[0][0]
        d2 = sy.diff(f, x, 2)
        for c in _critical_points(f, x):
            if d2.subs(x, c) > 0:
                return c
        return sy.nan

    def fMax(f: Any, x: Any, a: Any = None, b: Any = None) -> Any:
        if a is not None and b is not None:
            cps = _critical_points(f, x)
            candidates = [c for c in cps if _in_interval(c, a, b)] + [a, b]
            values = [(c, sy.simplify(f.subs(x, c))) for c in candidates]
            values.sort(key=lambda t: float(t[1]), reverse=True)
            return values[0][0]
        d2 = sy.diff(f, x, 2)
        for c in _critical_points(f, x):
            if d2.subs(x, c) < 0:
                return c
        return sy.nan

    ns.update({
        "deriv": deriv, "integral": integral_fn,
        "taylor": taylor, "fMin": fMin, "fMax": fMax,
    })

    # ── Algebra und Gleichungen ────────────────────────────────────────────
    def nSolve(eq: Any, x: Any, x0: Any = 0) -> Any:
        try:
            return sy.nsolve(eq, x, x0)
        except Exception as e:
            return sy.S(f"nsolve_error: {e}")

    def zeros(f: Any, x: Any) -> Any:
        if isinstance(f, sy.Equality):
            return sy.solve(f, x)
        return sy.solve(f, x)

    def poly(coeffs: Any, x: Any) -> Any:
        cs = _to_flat_list(coeffs)
        n = len(cs)
        return sum(c * x ** (n - 1 - i) for i, c in enumerate(cs))

    ns.update({"nSolve": nSolve, "zeros": zeros, "poly": poly})

    # ── Vektoren und Matrizen ──────────────────────────────────────────────
    def dotP(a: Any, b: Any) -> Any:
        return _to_matrix(a).dot(_to_matrix(b))

    def crossP(a: Any, b: Any) -> Any:
        return _to_matrix(a).cross(_to_matrix(b))

    def norm(v: Any) -> Any:
        return _to_matrix(v).norm()

    def unitV(v: Any) -> Any:
        m = _to_matrix(v)
        return m / m.norm()

    def det(m: Any) -> Any:
        return _to_matrix(m).det()

    def trace(m: Any) -> Any:
        return _to_matrix(m).trace()

    def rank(m: Any) -> Any:
        return _to_matrix(m).rank()

    def inv(m: Any) -> Any:
        return _to_matrix(m).inv()

    def transp(m: Any) -> Any:
        return _to_matrix(m).T

    def eigVl(m: Any) -> list[Any]:
        eigs = _to_matrix(m).eigenvals()
        out: list[Any] = []
        for w, mult in eigs.items():
            out.extend([w] * mult)
        return out

    def eigVc(m: Any) -> Any:
        mat = _to_matrix(m)
        cols: list[Any] = []
        for _value, _mult, vecs in mat.eigenvects():
            for v in vecs:
                cols.append(v)
        if not cols:
            return matrix_cls.zeros(mat.rows, 0)
        return matrix_cls.hstack(*cols)

    def identity(n: Any) -> Any:
        return matrix_cls.eye(int(n))

    def zeroMat(n: Any, m: Any = None) -> Any:
        if m is None:
            m = n
        return matrix_cls.zeros(int(n), int(m))

    ns.update({
        "dotP": dotP, "crossP": crossP, "norm": norm, "unitV": unitV,
        "det": det, "trace": trace, "rank": rank, "inv": inv,
        "transp": transp, "eigVl": eigVl, "eigVc": eigVc,
        "identity": identity, "zeroMat": zeroMat,
    })

    # ── Statistik und Kombinatorik ─────────────────────────────────────────
    def mean(lst: Any) -> Any:
        xs = _to_flat_list(lst)
        return sum(xs) / sy.Integer(len(xs))

    def median(lst: Any) -> Any:
        xs = sorted(_to_flat_list(lst), key=lambda v: float(v))
        n = len(xs)
        if n % 2 == 1:
            return xs[n // 2]
        return (xs[n // 2 - 1] + xs[n // 2]) / sy.Integer(2)

    def variance(lst: Any) -> Any:
        xs = _to_flat_list(lst)
        m = mean(xs)
        n = len(xs)
        if n < 2:
            return sy.S.Zero
        return sum((x - m) ** 2 for x in xs) / sy.Integer(n - 1)

    def stdDev(lst: Any) -> Any:
        return sy.sqrt(variance(lst))

    def sumL(lst: Any) -> Any:
        return sum(_to_flat_list(lst))

    def prodL(lst: Any) -> Any:
        out: Any = sy.S.One
        for x in _to_flat_list(lst):
            out = out * x
        return out

    def nCr(n: Any, r_val: Any) -> Any:
        return sy.binomial(n, r_val)

    def nPr(n: Any, r_val: Any) -> Any:
        return sy.factorial(n) / sy.factorial(n - r_val)

    def mod(a: Any, b: Any) -> Any:
        return sy.Mod(a, b)

    ns.update({
        "mean": mean, "median": median, "variance": variance,
        "stdDev": stdDev, "sumL": sumL, "prodL": prodL,
        "nCr": nCr, "nPr": nPr, "mod": mod,
    })
    # ``gcd`` und ``lcm`` sind in SymPy bereits vorhanden. Keine Aliase noetig.

    # ── Sonstige Helfer und TI-Aliase ──────────────────────────────────────
    def round_fn(x: Any, n: Any = 0) -> Any:
        try:
            return sy.Float(x, max(int(n) + 5, 5)).round(int(n))
        except Exception:
            return sy.nsimplify(round(float(x), int(n)))

    ns.update({
        "ceil": sy.ceiling,     # TI-Alias.
        "conj": sy.conjugate,   # TI-Alias.
        "round": round_fn,
        # floor, sign, re, im, arg sind in SymPy bereits vorhanden.
    })

    return ns


# ── CAS-Engine ────────────────────────────────────────────────────────────────
class Engine:
    """Auswerte-Engine auf SymPy-Basis.

    Haelt den SymPy-Namespace inklusive Einheiten und TI-artiger
    Zusatz-Funktionen vor und evaluiert Multi-Line-Eingaben in einem
    Durchlauf. Unterstuetzt globale Zuweisungen mit Zyklus-Erkennung.
    """

    # Einheiten, auf die bevorzugt reduziert wird (Reihenfolge = Prioritaet).
    _PREFERRED_UNIT_NAMES: tuple[str, ...] = (
        "newton", "joule", "watt", "volt", "ohm", "farad",
        "hertz", "pascal", "coulomb", "tesla", "henry", "siemens", "weber",
    )
    # Kurzzeichen fuer die Darstellung.
    _UNIT_SYMBOL: dict[str, str] = {
        "meter": "_m", "kilogram": "_kg", "second": "_s", "ampere": "_A",
        "kelvin": "_K", "mole": "_mol", "candela": "_cd",
        "newton": "_N", "joule": "_J", "watt": "_W", "pascal": "_Pa",
        "hertz": "_Hz", "volt": "_V", "ohm": "_Ω", "farad": "_F",
        "coulomb": "_C", "tesla": "_T", "henry": "_H", "siemens": "_S",
        "weber": "_Wb", "gram": "_g", "liter": "_L",
        "minute": "_min", "hour": "_h", "day": "_d", "electronvolt": "_eV",
    }

    def __init__(self, settings: Settings | None = None) -> None:
        import sympy
        from sympy.parsing.sympy_parser import (
            parse_expr, standard_transformations,
        )
        self.sy: Any = sympy
        self._parse_expr: Callable[..., Any] = parse_expr
        self._transforms: tuple[Any, ...] = standard_transformations
        self.settings: Settings = settings or Settings()
        self._units_namespace = _build_units_namespace()

        # Referenzen auf bevorzugte Einheiten (fuer ``convert_to``).
        import sympy.physics.units as u
        self._preferred: list[Any] = [
            getattr(u, n) for n in self._PREFERRED_UNIT_NAMES if hasattr(u, n)
        ]
        self._si_base: list[Any] = [
            u.meter, u.kilogram, u.second, u.ampere,
            u.kelvin, u.mole, u.candela,
        ]
        # Komplexe Variablen nach der letzten Auswertung (für Phasor-Diagramm).
        self.last_user_vars: dict[str, Any] = {}

    # ── Namespace ─────────────────────────────────────────────────────────────
    def _base_namespace(self) -> dict[str, Any]:
        ns: dict[str, Any] = {
            n: getattr(self.sy, n) for n in dir(self.sy) if not n.startswith("_")
        }
        ns["__builtins__"] = {}
        ns.update(self._units_namespace)
        # Zusatz-Funktionen nach dem SymPy-Namespace einspielen, damit
        # eigene Implementierungen die Defaults gezielt ueberschreiben
        # (beispielsweise unser ``zeros`` statt ``Matrix.zeros``).
        ns.update(_build_extra_functions(self.sy))
        # ``aprox`` als transparente Funktion: kann ueberall im Ausdruck
        # stehen, ohne einen NameError auszuloesen.
        ns["aprox"] = lambda x: x

        # Mathematische Konstanten + imaginäre Einheit
        _sy = self.sy
        ns["e"]   = _sy.E             # Euler-Zahl 2.71828…
        ns["phi"] = _sy.GoldenRatio   # Goldener Schnitt 1.61803…
        ns["j"]   = _sy.I             # Imaginäre Einheit (j = √-1)

        # phasor(r, theta_deg) → r·e^(j·θ·π/180)
        ns["phasor"] = lambda r, theta, _s=_sy: (
            r * _s.exp(_s.I * theta * _s.pi / 180)
        )

        # Physikalische Konstanten (SI-2019) mit Einheiten
        _u   = self._units_namespace
        _m   = _u["_m"];  _s  = _u["_s"];   _kg  = _u["_kg"]
        _A   = _u["_A"];  _K  = _u["_K"];   _mol = _u["_mol"]
        _N   = _u["_N"];  _J  = _u["_J"];   _C   = _u["_C"]
        _W   = _u["_W"];  _F  = _u["_F"]

        ns["c"]       = _sy.Float("299792458")          * _m / _s
        ns["G"]       = _sy.Float("6.67430e-11")        * _m**3 / (_kg * _s**2)
        ns["g_n"]     = _sy.Float("9.80665")            * _m / _s**2
        ns["hP"]      = _sy.Float("6.62607015e-34")     * _J * _s
        ns["hbar"]    = _sy.Float("1.054571817e-34")    * _J * _s
        ns["kB"]      = _sy.Float("1.380649e-23")       * _J / _K
        ns["NA"]      = _sy.Float("6.02214076e23")      / _mol
        ns["qe"]      = _sy.Float("1.602176634e-19")    * _C
        ns["eps0"]    = _sy.Float("8.8541878128e-12")   * _F / _m
        ns["mu0"]     = _sy.Float("1.25663706212e-6")   * _N / _A**2
        ns["Rgas"]    = _sy.Float("8.314462618")        * _J / (_mol * _K)
        ns["sigmaSB"] = _sy.Float("5.670374419e-8")     * _W / (_m**2 * _K**4)
        ns["me"]      = _sy.Float("9.1093837015e-31")   * _kg
        ns["mp"]      = _sy.Float("1.67262192369e-27")  * _kg

        # DEG-Modus: Trigonometrie wrappen.
        if self.settings.angle_mode == "DEG":
            sy = self.sy
            deg_factor = sy.pi / 180

            def _wrap(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
                return lambda x, f=fn, d=deg_factor: f(x * d)  # type: ignore[misc]

            def _wrap_inv(fn: Callable[[Any], Any]) -> Callable[[Any], Any]:
                return lambda x, f=fn, d=deg_factor: f(x) / d  # type: ignore[misc]

            for name in ("sin", "cos", "tan", "cot", "sec", "csc"):
                if hasattr(sy, name):
                    ns[name] = _wrap(getattr(sy, name))
            for name in ("asin", "acos", "atan", "acot", "asec", "acsc"):
                if hasattr(sy, name):
                    ns[name] = _wrap_inv(getattr(sy, name))
            if hasattr(sy, "atan2"):
                ns["atan2"] = lambda y, x, f=sy.atan2, d=deg_factor: f(y, x) / d
        return ns

    def _parse(self, s: str, ns: dict[str, Any]) -> Any:
        s = rewrite_equals_as_eq(s)
        return self._parse_expr(
            s, local_dict=ns, transformations=self._transforms
        )

    # ── Hauptauswertung ──────────────────────────────────────────────────────
    def evaluate_all(
        self,
        expressions: list[str],
        force_approx: set[int] | None = None,
    ) -> list[tuple[str, bool, Any]]:
        """Wertet alle Zeilen gemeinsam aus.

        Args:
            expressions: Liste der serialisierten Ausdrucks-Zeilen.
            force_approx: Indices, die numerisch (aprox) ausgewertet
                werden sollen - z. B. via ``Ctrl+Enter``.

        Returns:
            Liste mit ``(text, is_error, raw_sympy_or_None)`` in gleicher
            Reihenfolge wie ``expressions``. Das dritte Element ist der rohe
            SymPy-Wert (für die 2D-Darstellung) oder ``None`` bei Fehlern,
            Kommentaren und Ausdrücken mit Einheiten.
        """
        force_approx = force_approx or set()
        n = len(expressions)
        results: list[tuple[str, bool, Any] | None] = [None] * n

        # 1) Parsen: Zuweisung, Ausdruck, Kommentar oder leer.
        parsed: list[dict[str, Any]] = []
        for raw in expressions:
            line = raw.strip()
            if not line:
                parsed.append({"kind": "empty"})
                continue
            if line.startswith("#"):
                parsed.append({"kind": "comment"})
                continue
            func_match = re.match(
                r"^([A-Za-z]\w*)\s*\(\s*"
                r"([A-Za-z]\w*(?:\s*,\s*[A-Za-z]\w*)*)\s*\)"
                r"\s*:=\s*(.+)$",
                line,
            )
            if func_match:
                args = [a.strip() for a in func_match.group(2).split(",")]
                parsed.append({
                    "kind": "func",
                    "name": func_match.group(1),
                    "args": args,
                    "expr": to_sympy(func_match.group(3).strip()),
                })
                continue
            match = re.match(r"^([A-Za-z]\w*)\s*:=\s*(.+)$", line)
            if match:
                rhs = match.group(2).strip()
                approx, inner = _extract_approx(rhs)
                parsed.append({
                    "kind":   "assign",
                    "var":    match.group(1),
                    "expr":   to_sympy(inner if approx else rhs),
                    "approx": approx,
                })
            else:
                approx, inner = _extract_approx(line)
                parsed.append({
                    "kind":   "expr",
                    "expr":   to_sympy(inner if approx else line),
                    "approx": approx,
                })

        # Approx-Override anwenden (von ``Ctrl+Enter``).
        for i in force_approx:
            if 0 <= i < n and parsed[i]["kind"] in ("assign", "expr"):
                parsed[i]["approx"] = True

        for i, p in enumerate(parsed):
            if p["kind"] in ("empty", "comment"):
                results[i] = ("", False, None)

        # 2) Doppelte ``:=``-Zuweisungen -> Konflikt melden.
        # Variablen- und Funktionsnamen teilen sich den Namensraum.
        assign_indices: dict[str, list[int]] = {}
        for i, p in enumerate(parsed):
            if p["kind"] == "assign":
                assign_indices.setdefault(p["var"], []).append(i)
            elif p["kind"] == "func":
                assign_indices.setdefault(p["name"], []).append(i)

        conflict_vars: set[str] = set()
        for var, idxs in assign_indices.items():
            if len(idxs) > 1:
                conflict_vars.add(var)
                for i in idxs:
                    results[i] = (
                        f"Konflikt: »{var}« wird {len(idxs)}× zugewiesen",
                        True,
                        None,
                    )

        # 3) Zyklus-Pruefung der Abhaengigkeiten. Funktionsdefinitionen
        # werden hier bewusst ausgeklammert: ihr rechter Ausdruck enthaelt
        # gebundene Parameter-Variablen.
        assignments: dict[str, str] = {}
        assign_box_idx: dict[str, int] = {}
        for var, idxs in assign_indices.items():
            if (
                len(idxs) == 1
                and var not in conflict_vars
                and parsed[idxs[0]]["kind"] == "assign"
            ):
                assignments[var] = parsed[idxs[0]]["expr"]
                assign_box_idx[var] = idxs[0]

        cycle = find_cycle(assignments)
        cycle_vars: set[str] = set(cycle) if cycle else set()
        if cycle:
            path_text = " → ".join(cycle)
            for v in cycle_vars:
                if v in assign_box_idx:
                    results[assign_box_idx[v]] = (
                        f"Zirkulär: {path_text}", True, None
                    )

        # 4) Zuweisungen topologisch evaluieren.
        user_vars: dict[str, Any] = {}
        open_vars = set(assignments) - cycle_vars
        progress = True
        while open_vars and progress:
            progress = False
            for var in list(open_vars):
                expr = assignments[var]
                deps = {
                    u for u in open_vars
                    if u != var and re.search(rf"\b{re.escape(u)}\b", expr)
                }
                if deps:
                    continue
                i = assign_box_idx[var]
                try:
                    ns = self._base_namespace()
                    ns.update(user_vars)
                    value = self._parse(expr, ns)
                    value = self._normalize_units(value)
                    if (
                        self._is_sympy(value)
                        and not value.has(self.sy.Float)
                        and not self._has_units(value)
                    ):
                        try:
                            value = self.sy.nsimplify(value, rational=True)
                        except Exception:
                            pass
                    user_vars[var] = value
                    if results[i] is None:
                        approx = parsed[i].get("approx", False)
                        raw = None if self._has_units(value) else value
                        results[i] = (
                            f"{var} := {self._format(value, approx=approx)}",
                            False,
                            raw,
                        )
                except Exception as e:
                    if results[i] is None:
                        results[i] = (self._err(e), True, None)
                open_vars.discard(var)
                progress = True

        for var in open_vars:
            i = assign_box_idx[var]
            if results[i] is None:
                results[i] = ("Konnte nicht aufgelöst werden", True, None)

        # 4b) Funktionsdefinitionen als SymPy-Lambda evaluieren.
        for i, p in enumerate(parsed):
            if p["kind"] != "func" or results[i] is not None:
                continue
            try:
                ns = self._base_namespace()
                ns.update(user_vars)
                arg_syms = tuple(self.sy.Symbol(a) for a in p["args"])
                for sym in arg_syms:
                    ns[str(sym)] = sym
                body = self._parse(p["expr"], ns)
                lam = self.sy.Lambda(arg_syms, body)
                user_vars[p["name"]] = lam
                arg_str = ", ".join(p["args"])
                results[i] = (
                    f"{p['name']}({arg_str}) := {body}", False, None
                )
            except Exception as e:
                results[i] = (self._err(e), True, None)

        # 5) Ausdruecke und Gleichungen evaluieren.
        for i, p in enumerate(parsed):
            if results[i] is not None:
                continue
            if p["kind"] == "expr":
                try:
                    ns = self._base_namespace()
                    ns.update(user_vars)
                    value = self._parse(p["expr"], ns)
                    value = self._normalize_units(value)
                    if self._is_sympy(value):
                        try:
                            value = self.sy.simplify(value)
                        except Exception:
                            pass
                    if (
                        self._is_sympy(value)
                        and not value.has(self.sy.Float)
                        and not self._has_units(value)
                    ):
                        try:
                            value = self.sy.nsimplify(value, rational=True)
                        except Exception:
                            pass
                    raw = None if self._has_units(value) else value
                    results[i] = (
                        self._format(value, approx=p.get("approx", False)),
                        False,
                        raw,
                    )
                except Exception as e:
                    results[i] = (self._err(e), True, None)

        for i in range(n):
            if results[i] is None:
                results[i] = ("", False, None)

        # Variablen für Phasor-Diagramm merken (nur skalare, nicht-komplexe
        # Lambdas werden hier automatisch herausgefiltert).
        self.last_user_vars = {
            k: v for k, v in user_vars.items()
            if not callable(v)
        }

        return results  # type: ignore[return-value]

    # ── Einheiten-Helfer ─────────────────────────────────────────────────────
    @staticmethod
    def _is_sympy(expr: Any) -> bool:
        """True, wenn ``expr`` ein SymPy-Expression-Objekt ist.

        ``solve`` kann Listen oder Dicts zurueckgeben - dafuer ist das
        False.
        """
        return hasattr(expr, "has") and hasattr(expr, "atoms")

    def _has_units(self, expr: Any) -> bool:
        if not self._is_sympy(expr):
            return False
        try:
            from sympy.physics.units import Quantity
            return bool(expr.atoms(Quantity))
        except Exception:
            return False

    def _normalize_units(self, expr: Any) -> Any:
        """Reduziert auf eine einzelne abgeleitete Einheit, wenn moeglich.

        Beispiele: ``J/m -> N``, ``V/A -> Ω``.
        """
        if not self._has_units(expr):
            return expr
        from sympy.physics.units import convert_to, Quantity
        best: Any = None
        for target_unit in self._preferred:
            try:
                candidate = convert_to(expr, target_unit)
                quants = candidate.atoms(Quantity)
                if quants == {target_unit}:
                    best = candidate
                    break
            except Exception:
                continue
        if best is not None:
            return best
        try:
            return convert_to(expr, self._si_base)
        except Exception:
            return expr

    def _split_coefficient_unit(self, expr: Any) -> tuple[Any, Any]:
        """Trennt ``expr`` in Koeffizient und Einheiten-Anteil."""
        from sympy.physics.units import Quantity
        if not expr.atoms(Quantity):
            return expr, self.sy.S.One
        if expr.is_Mul:
            with_units: list[Any] = []
            without_units: list[Any] = []
            for arg in expr.args:
                (with_units if arg.has(Quantity) else without_units).append(arg)
            coeff = self.sy.Mul(*without_units) if without_units else self.sy.S.One
            unit = self.sy.Mul(*with_units) if with_units else self.sy.S.One
            return coeff, unit
        return self.sy.S.One, expr

    def _unit_to_text(self, unit: Any) -> str:
        """Liefert eine kompakte Zeichenketten-Darstellung der Einheit."""
        s = str(unit)
        for long, short in self._UNIT_SYMBOL.items():
            s = re.sub(rf"\b{long}\b", short, s)
        s = s.replace("**", "^").replace("*", "·")
        return s

    # ── Formatierung ─────────────────────────────────────────────────────────
    def _format(self, value: Any, approx: bool = False) -> str:
        sy = self.sy
        try:
            if value is True or value is sy.S.true:
                return "True ✓"
            if value is False or value is sy.S.false:
                return "False ✗"
        except Exception:
            pass

        # Listen (z. B. von ``solve``) elementweise formatieren.
        if isinstance(value, list):
            return (
                "[" + ", ".join(self._format(e, approx=approx) for e in value) + "]"
            )
        if isinstance(value, tuple):
            return (
                "(" + ", ".join(self._format(e, approx=approx) for e in value) + ")"
            )
        if isinstance(value, dict):
            pairs = [
                f"{k}: {self._format(v, approx=approx)}"
                for k, v in value.items()
            ]
            return "{" + ", ".join(pairs) + "}"

        try:
            if isinstance(value, sy.Equality):
                return f"{value.lhs} = {value.rhs}"
        except Exception:
            pass

        has_unit = self._has_units(value)
        places = self.settings.decimal_places
        fmt = self.settings.number_format

        if approx:
            if has_unit:
                return self._format_numeric_with_unit(value, fmt, places)
            return self._format_numeric(value, fmt, places)

        # Exakt-Darstellung.
        if has_unit:
            coeff, unit = self._split_coefficient_unit(value)
            return f"{coeff} {self._unit_to_text(unit)}".strip()

        s = str(value)
        try:
            if (
                hasattr(value, "free_symbols")
                and not value.free_symbols
                and value.is_number
            ):
                num = float(value)
                num_s = f"{num:.{places}g}"
                if num_s != s:
                    return f"{s}  ≈  {num_s}"
        except Exception:
            pass
        return s

    def _format_numeric(self, value: Any, fmt: str, places: int) -> str:
        try:
            x = float(self.sy.N(value, places + 3))
        except Exception:
            return str(value)
        if fmt == "SIC":
            return format_number_scientific(x, places)
        if fmt == "ENG":
            mant_s, exp3 = format_number_engineering(x, places)
            if exp3 == 0:
                return mant_s
            return f"{mant_s}·10{_superscript(exp3)}"
        # auto
        return _format_mantissa(x, places)

    def _format_numeric_with_unit(
        self, value: Any, fmt: str, places: int
    ) -> str:
        coeff, unit = self._split_coefficient_unit(value)
        try:
            x = float(self.sy.N(coeff, places + 3))
        except Exception:
            return f"{coeff} {self._unit_to_text(unit)}"

        unit_text = self._unit_to_text(unit)

        if fmt == "SIC":
            return f"{format_number_scientific(x, places)} {unit_text}"

        if fmt == "ENG":
            mant_s, exp3 = format_number_engineering(x, places)
            # Praefix direkt anfuegen, wenn moeglich und die Einheit ein
            # einzelnes Basis-Kuerzel ist.
            if exp3 in _PREFIX_FOR_EXP3 and _unit_allows_prefix(unit_text):
                prefix = _PREFIX_FOR_EXP3[exp3]
                base = unit_text.lstrip("_")
                return f"{mant_s} _{prefix}{base}"
            if exp3 == 0:
                return f"{mant_s} {unit_text}"
            return f"{mant_s}·10{_superscript(exp3)} {unit_text}"

        # auto
        return f"{_format_mantissa(x, places)} {unit_text}"

    @staticmethod
    def _err(e: Exception) -> str:
        return re.sub(r"\s+", " ", str(e))[:140]


def _extract_approx(s: str) -> tuple[bool, str]:
    """Extrahiert den Inhalt eines ``aprox(...)``-Wrappers.

    Returns:
        ``(True, inner)``, wenn ``s`` der Form ``aprox(inner)`` entspricht,
        sonst ``(False, s)``. Klammern werden korrekt gezaehlt.
    """
    s = s.strip()
    if not s.startswith("aprox(") or not s.endswith(")"):
        return False, s
    depth = 0
    for i, c in enumerate(s[5:], start=5):
        if c == "(":
            depth += 1
        elif c == ")":
            depth -= 1
            if depth == 0:
                if i == len(s) - 1:
                    return True, s[6:-1]
                return False, s
    return False, s



# ── Einstellungs-Dialog ───────────────────────────────────────────────────────
class SettingsDialog(QDialog):
    """Modaler Dialog zur Anpassung der Laufzeit-Einstellungen."""

    def __init__(
        self, settings: Settings, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.settings: Settings = settings
        self.setWindowTitle("Einstellungen")
        self.setModal(True)
        self.setMinimumWidth(380)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 20, 22, 18)
        layout.setSpacing(6)

        # Winkelmodus -----------------------------------------------------
        layout.addWidget(self._make_heading("Winkelmodus"))
        self.rad_button = QRadioButton("RAD - Bogenmass")
        self.deg_button = QRadioButton("DEG - Grad")
        self._angle_group = QButtonGroup(self)
        self._angle_group.addButton(self.rad_button)
        self._angle_group.addButton(self.deg_button)
        layout.addWidget(self.rad_button)
        layout.addWidget(self.deg_button)
        (self.deg_button if settings.angle_mode == "DEG" else self.rad_button) \
            .setChecked(True)

        layout.addSpacing(10)

        # Zahlenformat ----------------------------------------------------
        layout.addWidget(self._make_heading("Zahlenformat bei aprox"))
        self.auto_button = QRadioButton("Standard - Dezimalbruch")
        self.sci_button = QRadioButton(
            "SIC - wissenschaftlich  (1,23·10⁵)"
        )
        self.eng_button = QRadioButton(
            "ENG - Ingenieur  (123·10³ oder Praefix)"
        )
        self._format_group = QButtonGroup(self)
        for button in (self.auto_button, self.sci_button, self.eng_button):
            self._format_group.addButton(button)
            layout.addWidget(button)
        {
            "SIC": self.sci_button, "ENG": self.eng_button,
        }.get(settings.number_format, self.auto_button).setChecked(True)

        layout.addSpacing(10)

        # Nachkommastellen -----------------------------------------------
        layout.addWidget(self._make_heading("Nachkommastellen"))
        places_row = QHBoxLayout()
        places_row.setContentsMargins(0, 0, 0, 0)
        self.places_spin = QSpinBox()
        self.places_spin.setRange(1, 15)
        self.places_spin.setValue(settings.decimal_places)
        places_row.addWidget(self.places_spin)
        places_row.addWidget(QLabel("  (1 - 15)"))
        places_row.addStretch()
        layout.addLayout(places_row)

        layout.addSpacing(16)

        # Knoepfe --------------------------------------------------------
        button_row = QHBoxLayout()
        button_row.addStretch()
        cancel_button = QPushButton("Abbrechen")
        cancel_button.setObjectName("cancelButton")
        cancel_button.setCursor(Qt.CursorShape.PointingHandCursor)
        cancel_button.clicked.connect(self.reject)
        ok_button = QPushButton("Übernehmen")
        ok_button.setObjectName("okButton")
        ok_button.setCursor(Qt.CursorShape.PointingHandCursor)
        ok_button.setDefault(True)
        ok_button.clicked.connect(self._apply)
        button_row.addWidget(cancel_button)
        button_row.addWidget(ok_button)
        layout.addLayout(button_row)

    def _make_heading(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setObjectName("settingsHeading")
        return label

    def _apply(self) -> None:
        self.settings.angle_mode = (
            "DEG" if self.deg_button.isChecked() else "RAD"
        )
        if self.sci_button.isChecked():
            self.settings.number_format = "SIC"
        elif self.eng_button.isChecked():
            self.settings.number_format = "ENG"
        else:
            self.settings.number_format = "auto"
        self.settings.decimal_places = self.places_spin.value()
        self.accept()


# ── 2D-Graph-Widget (ausgelagert in cas_plot) ─────────────────────────────────
# Das eigentliche Plot-Widget lebt in ``cas_plot.py``. Wir importieren es
# nur hier; die Split-Screen-Integration steht weiter unten in
# ``CasCalculator._build_ui``.
from cas_plot import PlotPanel  # noqa: E402


# ── ViewModel ────────────────────────────────────────────────────────────────
class CasViewModel:
    """ViewModel des CAS-Rechners.

    Haelt den Anwendungszustand (Einstellungen, Engine, Hilfe-Modus)
    und berechnet aufbereitete Werte fuer die View.
    Enthaelt keinerlei GUI-Abhaengigkeiten.

    Attributes:
        settings: Laufzeit-Einstellungen (Winkelmodus, Zahlenformat).
        engine: SymPy-Auswertungs-Engine; liest ``settings`` bei jeder
            Auswertung neu aus, sodass Aenderungen sofort wirken.
    """

    def __init__(self) -> None:
        self.settings: Settings = Settings()
        self.engine: Engine = Engine(self.settings)
        self._help_active: bool = False

    @property
    def help_active(self) -> bool:
        """True, wenn die Hilfe-Ansicht gerade sichtbar ist."""
        return self._help_active

    def toggle_help(self) -> bool:
        """Wechselt den Hilfe-Modus.

        Returns:
            Neuer Hilfe-Zustand (True = aktiv).
        """
        self._help_active = not self._help_active
        return self._help_active

    def status_text(self) -> str:
        """Liefert den Statustext fuer die Toolbar-Anzeige.

        Returns:
            Formatierter String, z. B. ``"RAD  ·  SIC"``.
        """
        fmt = self.settings.number_format
        fmt_label: str = {"auto": "\u00b7", "SIC": "SIC", "ENG": "ENG"}.get(
            fmt, fmt
        )
        return f"{self.settings.angle_mode}  \u00b7  {fmt_label}"


# ── Komplettwidget mit Toolbar ────────────────────────────────────────────────
class CasCalculator(QWidget):
    """Haupt-Widget des CAS-Rechners.

    Enthaelt den zweidimensionalen Math-Editor als einzigen Editor, eine
    Hilfe-Ansicht als ueberblendendes Panel und eine Toolbar.
    """

    # Stack-Indizes der beiden Ansichten.
    _IDX_EDITOR: int = 0
    _IDX_HELP: int = 1

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.view_model: CasViewModel = CasViewModel()
        # Attribute werden in _build_ui() initialisiert.
        self.editor: MathEditor
        self.stack: QStackedWidget
        self.help_view: LexiconWidget
        self.editor_scroll: QScrollArea
        self.help_button: QPushButton
        self.settings_button: QPushButton
        self.graph_button: QPushButton
        self.status_label: QLabel
        self.clear_button: QPushButton
        self.plot_widget: PlotPanel
        self.split: QSplitter
        self._build_ui()

    def _build_ui(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        toolbar = QWidget()
        toolbar.setObjectName("casToolbar")
        toolbar.setFixedHeight(46)
        toolbar_layout = QHBoxLayout(toolbar)
        toolbar_layout.setContentsMargins(16, 0, 16, 0)
        toolbar_layout.setSpacing(10)

        title = QLabel("CAS Rechner")
        title.setObjectName("casTitle")
        toolbar_layout.addWidget(title)

        separator = QFrame()
        separator.setObjectName("casSeparator")
        separator.setFrameShape(QFrame.Shape.VLine)
        toolbar_layout.addWidget(separator)

        self.help_button = QPushButton("?  Hilfe")
        self.help_button.setObjectName("helpButton")
        self.help_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.help_button.clicked.connect(self._toggle_help)
        toolbar_layout.addWidget(self.help_button)

        self.settings_button = QPushButton("Einstellungen")
        self.settings_button.setObjectName("settingsButton")
        self.settings_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.settings_button.clicked.connect(self._open_settings)
        toolbar_layout.addWidget(self.settings_button)

        self.graph_button = QPushButton("Graph")
        self.graph_button.setObjectName("graphButton")
        self.graph_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.graph_button.clicked.connect(self._open_plot_2d)
        toolbar_layout.addWidget(self.graph_button)

        # Status-Indikator (RAD/DEG, Zahlenformat).
        self.status_label = QLabel()
        self.status_label.setObjectName("statusLabel")
        toolbar_layout.addWidget(self.status_label)

        toolbar_layout.addStretch()

        self.clear_button = QPushButton("Leeren  (Ctrl+L)")
        self.clear_button.setObjectName("clearButton")
        self.clear_button.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clear_button.clicked.connect(lambda: self.editor.clear())
        toolbar_layout.addWidget(self.clear_button)

        layout.addWidget(toolbar)

        # Stack: Splitter(Editor | Plot) (Index 0), Hilfe (Index 1).
        self.stack = QStackedWidget()
        self.editor = MathEditor()
        self.editor.set_engine(self.view_model.engine)
        # ScrollArea, damit lange Dokumente vertikal scrollbar sind.
        self.editor_scroll = QScrollArea()
        self.editor_scroll.setWidget(self.editor)
        self.editor_scroll.setObjectName("editorScroll")
        self.editor_scroll.setWidgetResizable(True)
        self.editor_scroll.setFrameShape(QFrame.Shape.NoFrame)

        # Plot-Panel wird rechts ueber einen Splitter ein- und ausgeblendet.
        self.plot_widget = PlotPanel(
            self.editor, self.view_model.engine
        )
        self.plot_widget.hide()

        self.split = QSplitter(Qt.Orientation.Horizontal)
        self.split.setChildrenCollapsible(False)
        self.split.addWidget(self.editor_scroll)
        self.split.addWidget(self.plot_widget)
        self.split.setStretchFactor(0, 1)
        self.split.setStretchFactor(1, 1)

        self.stack.addWidget(self.split)  # Index 0
        self.help_view = LexiconWidget(
            on_send_formula=self.insert_formula,
            folder=HELP_FOLDER,
            title="CAS Rechner Hilfe",
        )
        self.stack.addWidget(self.help_view)  # Index 1
        layout.addWidget(self.stack, stretch=1)

        # Nach jeder Editor-Auswertung (z. B. Enter) den Graphen neu
        # zeichnen, sofern das Panel sichtbar ist. Wir umhuellen die
        # bestehende ``_evaluate``-Methode, ohne ``math_editor`` zu
        # veraendern.
        _orig_evaluate = self.editor._evaluate

        def _evaluate_and_plot(approx_current: bool = False) -> None:
            _orig_evaluate(approx_current)
            if self.plot_widget.isVisible():
                self.plot_widget._plot()

        self.editor._evaluate = _evaluate_and_plot

        shortcut = QShortcut(QKeySequence("Ctrl+L"), self)
        shortcut.activated.connect(lambda: self.editor.clear())

        self._refresh_status()

    def _open_plot_2d(self) -> None:
        """Blendet das Graph-Panel rechts vom Editor ein bzw. aus."""
        visible = self.plot_widget.isVisible()
        if visible:
            self.plot_widget.hide()
            self.graph_button.setText("Graph")
        else:
            self.plot_widget.show()
            self.graph_button.setText("Graph  ✕")
            total = self.split.width()
            if total > 0:
                self.split.setSizes([total // 2, total // 2])
            self.plot_widget._plot()

    def _open_settings(self) -> None:
        dialog = SettingsDialog(self.view_model.settings, self)
        if dialog.exec():
            self._refresh_status()
            # Alles im Editor neu auswerten, falls sich Winkelmodus oder
            # Zahlenformat geaendert haben - aber nur, wenn ueberhaupt
            # Inhalt vorhanden ist.
            if any(line.children for line in self.editor.lines):
                self.editor._evaluate()

    def _refresh_status(self) -> None:
        self.status_label.setText(self.view_model.status_text())

    def _toggle_help(self) -> None:
        is_active = self.view_model.toggle_help()
        if not is_active:
            self.stack.setCurrentIndex(self._IDX_EDITOR)
            self.help_button.setText("?  Hilfe")
            self.clear_button.setEnabled(True)
            self.settings_button.setEnabled(True)
            self.graph_button.setEnabled(True)
            self.editor.setFocus()
        else:
            self.stack.setCurrentIndex(self._IDX_HELP)
            self.help_button.setText("←  Zurück zum Editor")
            self.clear_button.setEnabled(False)
            self.settings_button.setEnabled(False)
            self.graph_button.setEnabled(False)

    def insert_formula(self, formula: str) -> None:
        """Fuegt eine Formel im Editor ein und bringt den Editor in den Fokus."""
        if self.view_model.help_active:
            self._toggle_help()
        self.editor.insert_formula(formula)


# ── Standalone-Test ───────────────────────────────────────────────────────────
def main() -> None:
    import sys
    from PySide6.QtWidgets import QApplication, QMainWindow

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = QMainWindow()
    window.setWindowTitle("CAS Rechner - Test")
    window.resize(960, 640)
    window.setCentralWidget(CasCalculator())
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
