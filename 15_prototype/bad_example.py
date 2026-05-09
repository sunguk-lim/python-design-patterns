"""
=============================================================
 BAD EXAMPLE: Without the Prototype Pattern
=============================================================

Creating game enemies. Each enemy type has complex setup.

Problems:
    1. Creating each enemy requires repeating all setup code
    2. If setup is expensive (loading assets), it's wasteful
    3. No easy way to create variations of existing objects
    4. Copy logic scattered and error-prone
=============================================================
"""


class BadEnemy:
    def __init__(self, name, hp, attack, defense, speed, abilities, sprite):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.abilities = abilities
        self.sprite = sprite  # imagine this loads a big file

    def __str__(self):
        return f"  {self.name}: HP={self.hp}, ATK={self.attack}, DEF={self.defense}"


if __name__ == "__main__":
    # Creating 3 goblins — repeating ALL parameters every time!
    goblin1 = BadEnemy("Goblin", 50, 10, 5, 7, ["scratch", "bite"], "goblin.png")
    goblin2 = BadEnemy("Goblin", 50, 10, 5, 7, ["scratch", "bite"], "goblin.png")
    goblin3 = BadEnemy("Goblin", 50, 10, 5, 7, ["scratch", "bite"], "goblin.png")

    # Want a slightly stronger goblin? Repeat everything + change one field
    goblin_chief = BadEnemy("Goblin Chief", 80, 15, 8, 7, ["scratch", "bite", "rally"], "goblin.png")

    for g in [goblin1, goblin2, goblin3, goblin_chief]:
        print(g)

    print()
    print("Repeated all 7 parameters for every goblin.")
    print("→ The Prototype pattern fixes this.")
