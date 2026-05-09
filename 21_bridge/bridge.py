"""
=============================================================
 DESIGN PATTERN #21: BRIDGE
=============================================================

Category: Structural
Intent:   Decouple an abstraction from its implementation so that
          the two can vary independently.

Real-world analogy:
    A remote control and a TV. The remote (abstraction) works with
    any TV brand (implementation). You can change remotes or TVs
    independently — they're connected by a "bridge".

When to use:
    - You have two independent dimensions that vary
    - Class explosion from combining dimensions via inheritance
    - You want to switch implementations at runtime

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Implementation interface (the "how")
# ---------------------------------------------------------

class Renderer(ABC):
    @abstractmethod
    def render_circle(self, x: int, y: int, radius: int) -> None:
        pass

    @abstractmethod
    def render_rectangle(self, x: int, y: int, w: int, h: int) -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete implementations
# ---------------------------------------------------------

class VectorRenderer(Renderer):
    def render_circle(self, x: int, y: int, radius: int) -> None:
        print(f"  🖊️  Vector circle at ({x},{y}) r={radius}")

    def render_rectangle(self, x: int, y: int, w: int, h: int) -> None:
        print(f"  🖊️  Vector rect at ({x},{y}) {w}x{h}")


class RasterRenderer(Renderer):
    def render_circle(self, x: int, y: int, radius: int) -> None:
        print(f"  🎨 Raster circle at ({x},{y}) r={radius} (pixels)")

    def render_rectangle(self, x: int, y: int, w: int, h: int) -> None:
        print(f"  🎨 Raster rect at ({x},{y}) {w}x{h} (pixels)")


class SVGRenderer(Renderer):
    """New renderer — no shape classes modified!"""
    def render_circle(self, x: int, y: int, radius: int) -> None:
        print(f"  📐 <circle cx='{x}' cy='{y}' r='{radius}'/>")

    def render_rectangle(self, x: int, y: int, w: int, h: int) -> None:
        print(f"  📐 <rect x='{x}' y='{y}' width='{w}' height='{h}'/>")


# ---------------------------------------------------------
# STEP 3: Abstraction (the "what") — holds a reference to impl
# ---------------------------------------------------------

class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self._renderer = renderer  # THE BRIDGE!

    @abstractmethod
    def draw(self) -> None:
        pass


# ---------------------------------------------------------
# STEP 4: Refined abstractions
# ---------------------------------------------------------

class Circle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, radius: int):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self) -> None:
        self._renderer.render_circle(self.x, self.y, self.radius)


class Rectangle(Shape):
    def __init__(self, renderer: Renderer, x: int, y: int, w: int, h: int):
        super().__init__(renderer)
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def draw(self) -> None:
        self._renderer.render_rectangle(self.x, self.y, self.w, self.h)


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    renderers = [
        ("Vector", VectorRenderer()),
        ("Raster", RasterRenderer()),
        ("SVG", SVGRenderer()),
    ]

    for name, renderer in renderers:
        print(f"=== {name} Renderer ===")
        circle = Circle(renderer, 10, 20, 5)
        rect = Rectangle(renderer, 0, 0, 100, 50)
        circle.draw()
        rect.draw()
        print()

    print(f"Total classes: 2 shapes + 3 renderers = 5 (not 6!)")
    print(f"5 shapes + 3 renderers = 8 classes (not 15!)")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Shape and Renderer vary INDEPENDENTLY.")
    print("2. M shapes + N renderers = M+N classes (not M×N).")
    print("3. The 'bridge' is the renderer reference in Shape.")
    print("4. Can swap renderers at runtime.")
    print("5. Two separate hierarchies connected by composition.")
