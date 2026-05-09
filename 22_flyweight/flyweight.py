"""
=============================================================
 DESIGN PATTERN #22: FLYWEIGHT
=============================================================

Category: Structural
Intent:   Use sharing to support large numbers of fine-grained
          objects efficiently by separating intrinsic (shared)
          state from extrinsic (unique) state.

Real-world analogy:
    A forest in a video game. There are millions of trees, but
    only 5-10 tree TYPES (oak, pine, birch). Each tree shares
    the mesh/texture of its type (intrinsic) but has its own
    position/size (extrinsic).

Key terms:
    - Intrinsic state: shared, immutable (font, texture, mesh)
    - Extrinsic state: unique per instance (position, size)

When to use:
    - You have a HUGE number of similar objects
    - Objects share most of their state
    - Memory is a concern

=============================================================
"""


# ---------------------------------------------------------
# STEP 1: The Flyweight — stores shared (intrinsic) state
# ---------------------------------------------------------

class CharacterStyle:
    """Shared formatting — only created once per unique combination."""
    def __init__(self, font: str, size: int, color: str):
        self.font = font
        self.size = size
        self.color = color

    def render(self, char: str, x: int, y: int) -> str:
        return f"'{char}' at ({x},{y}) [{self.font} {self.size}px {self.color}]"


# ---------------------------------------------------------
# STEP 2: Flyweight Factory — manages shared instances
# ---------------------------------------------------------

class StyleFactory:
    _styles: dict[tuple, CharacterStyle] = {}

    @classmethod
    def get_style(cls, font: str, size: int, color: str) -> CharacterStyle:
        key = (font, size, color)
        if key not in cls._styles:
            cls._styles[key] = CharacterStyle(font, size, color)
            print(f"  ✨ Created new style: {font} {size}px {color}")
        return cls._styles[key]

    @classmethod
    def style_count(cls) -> int:
        return len(cls._styles)


# ---------------------------------------------------------
# STEP 3: The context — stores unique (extrinsic) state
# ---------------------------------------------------------

class Character:
    """Each character only stores its unique data + a reference to shared style."""
    def __init__(self, char: str, x: int, y: int, style: CharacterStyle):
        self.char = char
        self.x = x
        self.y = y
        self.style = style  # shared reference, not a copy!

    def render(self) -> str:
        return self.style.render(self.char, self.x, self.y)


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    StyleFactory._styles.clear()

    print("=== Creating characters ===")
    # Get shared styles (only created once each)
    normal = StyleFactory.get_style("Arial", 12, "black")
    bold = StyleFactory.get_style("Arial-Bold", 12, "black")
    heading = StyleFactory.get_style("Arial-Bold", 24, "blue")

    # Create many characters sharing the same styles
    characters = []
    text = "Hello World"
    for i, ch in enumerate(text):
        style = heading if i == 0 else normal
        characters.append(Character(ch, i * 10, 0, style))

    # Add more text with the same styles
    text2 = "Design Patterns"
    for i, ch in enumerate(text2):
        style = bold if ch.isupper() else normal
        characters.append(Character(ch, i * 10, 20, style))

    print(f"\n=== Rendering ===")
    for ch in characters[:5]:
        print(f"  {ch.render()}")
    print(f"  ... and {len(characters) - 5} more characters")

    print(f"\n=== Memory savings ===")
    print(f"  Total characters: {len(characters)}")
    print(f"  Unique styles created: {StyleFactory.style_count()}")
    print(f"  Without flyweight: {len(characters)} style objects")
    print(f"  With flyweight: {StyleFactory.style_count()} style objects")
    print(f"  Saving: {len(characters) - StyleFactory.style_count()} duplicate objects!")

    # Simulate a large document
    print(f"\n=== Large document simulation ===")
    StyleFactory._styles.clear()
    large_chars = []
    large_text = "Lorem ipsum dolor sit amet " * 1000
    for i, ch in enumerate(large_text):
        style = StyleFactory.get_style("Arial", 12, "black")
        large_chars.append(Character(ch, i % 80 * 10, i // 80 * 15, style))

    print(f"  Characters: {len(large_chars)}")
    print(f"  Unique styles: {StyleFactory.style_count()}")
    print(f"  Style objects saved: {len(large_chars) - StyleFactory.style_count()}")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Intrinsic (shared) state is stored ONCE in flyweights.")
    print("2. Extrinsic (unique) state is stored in each context.")
    print("3. Factory ensures flyweights are reused, not duplicated.")
    print("4. Huge memory savings with many similar objects.")
    print("5. Trade-off: slightly more complex code for big memory wins.")
