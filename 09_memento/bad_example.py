"""
=============================================================
 BAD EXAMPLE: Without the Memento Pattern
=============================================================

A game character whose state you want to save and restore.

Problems:
    1. To save state, you must expose ALL internal fields
    2. Other code can modify the saved state (no encapsulation)
    3. If you add a new field, you must update save/restore everywhere
    4. No structured history — just raw data floating around
=============================================================
"""


class BadGameCharacter:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.hp = 100
        self.position = (0, 0)

    def take_damage(self, dmg: int):
        self.hp -= dmg
        print(f"  {self.name} took {dmg} damage. HP: {self.hp}")

    def level_up(self):
        self.level += 1
        self.hp = 100
        print(f"  {self.name} leveled up to {self.level}! HP restored.")

    def move(self, x: int, y: int):
        self.position = (x, y)
        print(f"  {self.name} moved to {self.position}")


if __name__ == "__main__":
    hero = BadGameCharacter("Hero")
    hero.move(5, 3)
    hero.take_damage(40)

    # "Save" by manually copying fields — fragile!
    saved_level = hero.level
    saved_hp = hero.hp
    saved_pos = hero.position

    hero.take_damage(60)
    print(f"\n  💀 {hero.name} died! HP: {hero.hp}")

    # "Restore" by manually setting fields
    hero.level = saved_level
    hero.hp = saved_hp
    hero.position = saved_pos
    print(f"  Restored! Level: {hero.level}, HP: {hero.hp}, Pos: {hero.position}")

    print()
    print("This works, but it exposes internal state to outside code.")
    print("Add a new field (e.g., inventory)? Must update save/restore.")
    print("→ The Memento pattern fixes this.")
