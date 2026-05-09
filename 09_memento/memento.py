"""
=============================================================
 DESIGN PATTERN #9: MEMENTO
=============================================================

Category: Behavioral
Intent:   Capture and externalize an object's internal state
          so that it can be restored later, without violating
          encapsulation.

Real-world analogy:
    A save point in a video game. You save your progress before
    a boss fight. If you die, you load the save and try again.
    The save file captures your exact state without exposing
    the game's internal code.

Key terms:
    - Originator: the object whose state is saved (GameCharacter)
    - Memento:    the snapshot object (immutable state capsule)
    - Caretaker:  manages the history of mementos (SaveManager)

When to use:
    - You need save/restore (undo, checkpoints, snapshots)
    - You want to preserve encapsulation of internal state
    - You need a history of states

=============================================================
"""

from dataclasses import dataclass
from copy import deepcopy


# ---------------------------------------------------------
# STEP 1: The Memento — an immutable snapshot
# ---------------------------------------------------------
# Stores the state but doesn't expose setters.

@dataclass(frozen=True)  # frozen = immutable!
class GameMemento:
    level: int
    hp: int
    position: tuple
    inventory: list  # new field — no problem!
    label: str = ""


# ---------------------------------------------------------
# STEP 2: The Originator — creates and restores from mementos
# ---------------------------------------------------------

class GameCharacter:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.hp = 100
        self.position = (0, 0)
        self.inventory: list[str] = []

    def take_damage(self, dmg: int) -> None:
        self.hp = max(0, self.hp - dmg)
        print(f"  ⚔️  {self.name} took {dmg} damage. HP: {self.hp}")

    def level_up(self) -> None:
        self.level += 1
        self.hp = 100
        print(f"  ⬆️  {self.name} leveled up to {self.level}! HP restored.")

    def move(self, x: int, y: int) -> None:
        self.position = (x, y)
        print(f"  🚶 {self.name} moved to {self.position}")

    def pick_up(self, item: str) -> None:
        self.inventory.append(item)
        print(f"  🎒 {self.name} picked up '{item}'")

    def save(self, label: str = "") -> GameMemento:
        """Create a memento (snapshot) of current state."""
        return GameMemento(
            level=self.level,
            hp=self.hp,
            position=self.position,
            inventory=deepcopy(self.inventory),
            label=label,
        )

    def restore(self, memento: GameMemento) -> None:
        """Restore state from a memento."""
        self.level = memento.level
        self.hp = memento.hp
        self.position = memento.position
        self.inventory = deepcopy(memento.inventory)
        print(f"  💾 Restored to '{memento.label}': "
              f"Level {self.level}, HP {self.hp}, Pos {self.position}, "
              f"Items {self.inventory}")

    def status(self) -> str:
        return (f"  📊 {self.name}: Level {self.level}, HP {self.hp}, "
                f"Pos {self.position}, Items {self.inventory}")


# ---------------------------------------------------------
# STEP 3: The Caretaker — manages save history
# ---------------------------------------------------------

class SaveManager:
    def __init__(self):
        self._saves: list[GameMemento] = []

    def save(self, memento: GameMemento) -> None:
        self._saves.append(memento)
        print(f"  💾 Game saved: '{memento.label}'")

    def load(self, index: int = -1) -> GameMemento:
        return self._saves[index]

    def list_saves(self) -> None:
        print("  📂 Save files:")
        for i, m in enumerate(self._saves):
            print(f"     [{i}] '{m.label}' - Level {m.level}, HP {m.hp}")


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    hero = GameCharacter("Hero")
    saves = SaveManager()

    print("=== Adventure begins ===")
    hero.move(5, 3)
    hero.pick_up("Sword")
    hero.level_up()

    # Save before boss fight
    saves.save(hero.save("Before boss fight"))

    print("\n=== Boss fight (goes badly) ===")
    hero.take_damage(40)
    hero.take_damage(35)
    hero.pick_up("Poison")
    hero.take_damage(30)
    print(hero.status())

    print("\n=== Load save! ===")
    saves.list_saves()
    hero.restore(saves.load(0))
    print(hero.status())

    print("\n=== Boss fight (retry, goes well) ===")
    hero.take_damage(20)
    hero.pick_up("Boss Key")
    hero.level_up()
    saves.save(hero.save("After boss defeated"))

    print("\n=== All saves ===")
    saves.list_saves()

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Internal state is captured WITHOUT exposing it.")
    print("2. Mementos are immutable — can't be tampered with.")
    print("3. The Caretaker manages saves without knowing the details.")
    print("4. Adding new fields (inventory) doesn't break anything.")
    print("5. Different from Command: Command stores actions,")
    print("   Memento stores snapshots of state.")
