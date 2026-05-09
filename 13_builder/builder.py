"""
=============================================================
 DESIGN PATTERN #13: BUILDER
=============================================================

Category: Creational
Intent:   Separate the construction of a complex object from its
          representation, allowing the same construction process
          to create different representations.

Real-world analogy:
    Ordering a custom pizza. You don't get a constructor with
    20 parameters. Instead: start with dough → add sauce →
    add cheese → add toppings, step by step.

When to use:
    - Object has many optional parameters
    - Construction involves multiple steps
    - You want readable, self-documenting creation code
    - You want to create different representations of the same thing

=============================================================
"""


# ---------------------------------------------------------
# STEP 1: The Product — what we're building
# ---------------------------------------------------------

class House:
    def __init__(self):
        self.floors = 1
        self.rooms = 1
        self.wall_material = "brick"
        self.roof_type = "flat"
        self.features: list[str] = []

    def __str__(self):
        return (f"  🏠 House: {self.floors}F, {self.rooms}R, "
                f"{self.wall_material} walls, {self.roof_type} roof\n"
                f"     Features: {self.features or 'none'}")


# ---------------------------------------------------------
# STEP 2: The Builder — step-by-step construction
# ---------------------------------------------------------

class HouseBuilder:
    def __init__(self):
        self._house = House()

    def floors(self, count: int) -> "HouseBuilder":
        self._house.floors = count
        return self  # return self for method chaining!

    def rooms(self, count: int) -> "HouseBuilder":
        self._house.rooms = count
        return self

    def walls(self, material: str) -> "HouseBuilder":
        self._house.wall_material = material
        return self

    def roof(self, roof_type: str) -> "HouseBuilder":
        self._house.roof_type = roof_type
        return self

    def with_garage(self) -> "HouseBuilder":
        self._house.features.append("garage")
        return self

    def with_pool(self) -> "HouseBuilder":
        self._house.features.append("pool")
        return self

    def with_garden(self) -> "HouseBuilder":
        self._house.features.append("garden")
        return self

    def with_solar(self) -> "HouseBuilder":
        self._house.features.append("solar panels")
        return self

    def with_security(self) -> "HouseBuilder":
        self._house.features.append("security system")
        return self

    def with_smart_home(self) -> "HouseBuilder":
        self._house.features.append("smart home")
        return self

    def build(self) -> House:
        house = self._house
        self._house = House()  # reset for reuse
        return house


# ---------------------------------------------------------
# STEP 3: Optional Director — predefined configurations
# ---------------------------------------------------------

class HouseDirector:
    """Predefined recipes for common house types."""

    @staticmethod
    def luxury_house(builder: HouseBuilder) -> House:
        return (builder
                .floors(3).rooms(8)
                .walls("marble").roof("mansard")
                .with_garage().with_pool().with_garden()
                .with_solar().with_security().with_smart_home()
                .build())

    @staticmethod
    def starter_home(builder: HouseBuilder) -> House:
        return (builder
                .floors(1).rooms(3)
                .walls("wood").roof("gable")
                .with_garden()
                .build())


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    builder = HouseBuilder()

    # Custom build — readable and self-documenting!
    print("=== Custom House (method chaining) ===")
    house = (builder
             .floors(2).rooms(5)
             .walls("wood").roof("gable")
             .with_garage().with_solar()
             .build())
    print(house)

    # Using the Director for predefined types
    print("\n=== Luxury House (via Director) ===")
    luxury = HouseDirector.luxury_house(builder)
    print(luxury)

    print("\n=== Starter Home (via Director) ===")
    starter = HouseDirector.starter_home(builder)
    print(starter)

    # Minimal house — just the defaults
    print("\n=== Minimal House (defaults only) ===")
    minimal = builder.build()
    print(minimal)

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. No telescoping constructor — each step is a named method.")
    print("2. Method chaining (.floors(2).rooms(5)) is readable.")
    print("3. Optional features are explicit: .with_pool(), .with_garage().")
    print("4. Director provides predefined recipes.")
    print("5. Same builder process, different results.")
