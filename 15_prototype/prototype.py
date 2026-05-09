"""
=============================================================
 DESIGN PATTERN #15: PROTOTYPE
=============================================================

Category: Creational
Intent:   Create new objects by cloning existing ones, avoiding
          the cost of creation from scratch.

Real-world analogy:
    Cell division. Instead of building a new cell from raw
    materials, an existing cell copies itself and then the
    copy can be modified.

When to use:
    - Object creation is expensive (loading files, DB queries)
    - You need many similar objects with small variations
    - You want to avoid subclassing just to change defaults

=============================================================
"""

import copy


# ---------------------------------------------------------
# STEP 1: The Prototype — supports cloning
# ---------------------------------------------------------

class Enemy:
    def __init__(self, name: str, hp: int, attack: int,
                 defense: int, speed: int, abilities: list[str],
                 sprite: str):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.abilities = abilities
        self.sprite = sprite
        # Imagine expensive initialization here:
        # self._load_sprite(sprite)
        # self._calculate_stats()

    def clone(self) -> "Enemy":
        """Deep copy — the clone is fully independent."""
        return copy.deepcopy(self)

    def __str__(self):
        return (f"  {self.name}: HP={self.hp}, ATK={self.attack}, "
                f"DEF={self.defense}, SPD={self.speed}, "
                f"Abilities={self.abilities}")


# ---------------------------------------------------------
# STEP 2: A registry of prototypes (optional but useful)
# ---------------------------------------------------------

class EnemyRegistry:
    def __init__(self):
        self._prototypes: dict[str, Enemy] = {}

    def register(self, key: str, prototype: Enemy) -> None:
        self._prototypes[key] = prototype

    def create(self, key: str, **overrides) -> Enemy:
        """Clone a prototype and apply overrides."""
        if key not in self._prototypes:
            raise KeyError(f"No prototype registered for '{key}'")
        clone = self._prototypes[key].clone()
        for attr, value in overrides.items():
            setattr(clone, attr, value)
        return clone


# ---------------------------------------------------------
# STEP 3: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Create prototypes (expensive, done once)
    registry = EnemyRegistry()

    registry.register("goblin", Enemy(
        name="Goblin", hp=50, attack=10, defense=5,
        speed=7, abilities=["scratch", "bite"], sprite="goblin.png"
    ))

    registry.register("dragon", Enemy(
        name="Dragon", hp=500, attack=80, defense=50,
        speed=30, abilities=["fire_breath", "tail_swipe", "fly"],
        sprite="dragon.png"
    ))

    # Spawn enemies by cloning — fast and clean!
    print("=== Spawn Goblins (cloned from prototype) ===")
    for i in range(3):
        goblin = registry.create("goblin")
        print(goblin)

    print("\n=== Spawn Goblin Chief (clone + override) ===")
    chief = registry.create("goblin",
                            name="Goblin Chief", hp=80, attack=15,
                            abilities=["scratch", "bite", "rally"])
    print(chief)

    print("\n=== Spawn Dragons ===")
    dragon = registry.create("dragon")
    print(dragon)

    baby_dragon = registry.create("dragon",
                                  name="Baby Dragon", hp=100, attack=20)
    print(baby_dragon)

    # Verify clones are independent
    print("\n=== Independence check ===")
    g1 = registry.create("goblin")
    g2 = registry.create("goblin")
    g1.name = "Modified Goblin"
    g1.abilities.append("steal")
    print(f"  g1: {g1.name}, abilities={g1.abilities}")
    print(f"  g2: {g2.name}, abilities={g2.abilities}")  # unaffected!

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Clone existing objects instead of creating from scratch.")
    print("2. Deep copy ensures clones are fully independent.")
    print("3. Registry provides a catalog of reusable prototypes.")
    print("4. Overrides allow easy variations (Goblin → Goblin Chief).")
    print("5. Python's copy.deepcopy() does the heavy lifting.")
