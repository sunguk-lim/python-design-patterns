"""
=============================================================
 BAD EXAMPLE: Without the Bridge Pattern
=============================================================

Shapes that can be rendered in different ways (vector, raster).

Problems:
    1. Class explosion: CircleVector, CircleRaster, SquareVector,
       SquareRaster... M shapes × N renderers = M*N classes!
    2. Adding a new shape → N new classes (one per renderer)
    3. Adding a new renderer → M new classes (one per shape)
    4. Two independent dimensions locked together via inheritance
=============================================================
"""


class CircleVector:
    def draw(self):
        print("  Drawing circle as vector lines")

class CircleRaster:
    def draw(self):
        print("  Drawing circle as pixels")

class SquareVector:
    def draw(self):
        print("  Drawing square as vector lines")

class SquareRaster:
    def draw(self):
        print("  Drawing square as pixels")

# TriangleVector? TriangleRaster? 3D renderer?
# 3 shapes × 3 renderers = 9 classes!


if __name__ == "__main__":
    shapes = [CircleVector(), CircleRaster(), SquareVector(), SquareRaster()]
    for s in shapes:
        s.draw()

    print()
    print("2 shapes × 2 renderers = 4 classes.")
    print("5 shapes × 3 renderers = 15 classes!")
    print("→ The Bridge pattern fixes this.")
