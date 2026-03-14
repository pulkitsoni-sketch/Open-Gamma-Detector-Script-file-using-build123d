"""
Case_Lower.py — build123d script for Case_Lower.stl
CONFIRMED from STL vertex/normal analysis.

  Outer cuboid    : 142.8 x 72.8 x 5.0mm  ← BX corrected from 146.3 to 142.8
  Corner fillet   : R=3mm (vertical edges)
  4 corner holes  : Dia 3.5mm, centres 3.9mm from each edge
  6 standoffs     : OD=9mm, ID=5mm
    Col X centres: 14.4, 78.05, 128.37  (from local origin)
    Row Y centres: 15.42, 58.90
    Cylinder top Z=7.0mm (protrusion 2.0mm above base)
    Cavity bottom Z=1.5mm (cavity depth 5.5mm)
    Base fillet R=1mm at cylinder/cuboid junction
"""

from build123d import *

try:
    from ocp_vscode import show
    HAS_VIEWER = True
except ImportError:
    HAS_VIEWER = False

# ── Cuboid ────────────────────────────────────────────────────
BX = 142.8        # ← corrected from 146.3
BY =  72.8
BZ =   5.0
FR  =   3.0       # corner fillet radius

# ── Corner through-holes ──────────────────────────────────────
HOLE_D   = 3.5
HOLE_IN  = 3.9    # centre from each edge
HX = BX/2 - HOLE_IN   # ±67.5
HY = BY/2 - HOLE_IN   # ±32.5
CORNER_HOLES = [(-HX,-HY),(HX,-HY),(-HX,HY),(HX,HY)]

# ── Standoff cylinders ────────────────────────────────────────
CYL_OD   =  9.0
CYL_ID   =  5.0
CYL_TOP  =  7.0
CAV_BOT  =  1.5
CAV_D    = CYL_TOP - CAV_BOT   # 5.5mm
FILLET_R =  1.0

# Centres measured from STL local origin (X_min, Y_min corner)
COL_X = [14.40, 78.05, 128.37]
ROW_Y = [15.42, 58.90]

# Convert to build123d centred coords
STANDOFFS = [(x - BX/2, y - BY/2) for y in ROW_Y for x in COL_X]

# ── Build ─────────────────────────────────────────────────────
with BuildPart() as case_lower:

    # 1) Base cuboid with rounded corners
    with BuildSketch(Plane.XY):
        RectangleRounded(BX, BY, FR)
    extrude(amount=BZ)

    # 2) Standoff bosses
    with BuildSketch(Plane.XY):
        for cx, cy in STANDOFFS:
            with Locations((cx, cy)):
                Circle(CYL_OD / 2)
    extrude(amount=CYL_TOP)

    # 3) Fillet cylinder base edges
    try:
        base_edges = (
            case_lower.edges()
            .filter_by(GeomType.CIRCLE)
            .group_by(Axis.Z)[1]
            .filter_by(lambda e: abs(e.radius - CYL_OD/2) < 0.5)
        )
        fillet(base_edges, radius=FILLET_R)
    except (ValueError, IndexError):
        pass

    # 4) Blind cavity in each standoff
    with BuildSketch(Plane.XY.offset(CYL_TOP)):
        for cx, cy in STANDOFFS:
            with Locations((cx, cy)):
                Circle(CYL_ID / 2)
    extrude(amount=-CAV_D, mode=Mode.SUBTRACT)

    # 5) Corner through-holes
    with BuildSketch(Plane.XY.offset(BZ)):
        for cx, cy in CORNER_HOLES:
            with Locations((cx, cy)):
                Circle(HOLE_D / 2)
    extrude(amount=-BZ, mode=Mode.SUBTRACT)

export_stl(case_lower.part, "Case_Lower_rebuilt.stl")
print(f"Case_Lower volume : {case_lower.part.volume:.2f} mm³")
print("Exported → Case_Lower_rebuilt.stl")

if HAS_VIEWER:
    show(case_lower.part, names=["Case_Lower"])
