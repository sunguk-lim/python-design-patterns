"""
=============================================================
 BAD EXAMPLE: Without the Flyweight Pattern
=============================================================

A text editor rendering thousands of characters. Each character
object stores its own font, size, and color.

Problems:
    1. 10,000 characters = 10,000 font/size/color copies
    2. Most characters share the same formatting
    3. Massive memory waste for duplicate data
=============================================================
"""

import sys


class BadCharacter:
    def __init__(self, char: str, font: str, size: int, color: str):
        self.char = char
        self.font = font      # duplicated thousands of times!
        self.size = size       # duplicated thousands of times!
        self.color = color     # duplicated thousands of times!


if __name__ == "__main__":
    text = "Hello World! " * 1000  # 13,000 characters
    characters = []
    for ch in text:
        characters.append(BadCharacter(ch, "Arial", 12, "black"))

    print(f"  Characters created: {len(characters)}")
    print(f"  Each stores: char + font + size + color")
    print(f"  Memory per object: ~{sys.getsizeof(characters[0])} bytes")
    print(f"  Total objects: {len(characters)}")
    print()
    print("Every character stores its own copy of 'Arial', 12, 'black'")
    print("even though they're all the same!")
    print("→ The Flyweight pattern fixes this.")
