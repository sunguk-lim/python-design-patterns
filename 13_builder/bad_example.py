"""
=============================================================
 BAD EXAMPLE: Without the Builder Pattern
=============================================================

Creating a complex object (a House) with many optional parameters.

Problems:
    1. Constructor with too many parameters (telescoping constructor)
    2. Hard to remember parameter order
    3. Many parameters are optional → lots of None defaults
    4. No way to enforce valid combinations
=============================================================
"""


class BadHouse:
    def __init__(self, floors=1, rooms=1, has_garage=False,
                 has_pool=False, has_garden=False, has_solar=False,
                 wall_material="brick", roof_type="flat",
                 has_security=False, has_smart_home=False):
        self.floors = floors
        self.rooms = rooms
        self.has_garage = has_garage
        self.has_pool = has_pool
        self.has_garden = has_garden
        self.has_solar = has_solar
        self.wall_material = wall_material
        self.roof_type = roof_type
        self.has_security = has_security
        self.has_smart_home = has_smart_home

    def __str__(self):
        features = []
        if self.has_garage: features.append("garage")
        if self.has_pool: features.append("pool")
        if self.has_garden: features.append("garden")
        if self.has_solar: features.append("solar")
        if self.has_security: features.append("security")
        if self.has_smart_home: features.append("smart home")
        return (f"House: {self.floors}F, {self.rooms}R, "
                f"{self.wall_material} walls, {self.roof_type} roof, "
                f"features: {features or 'none'}")


if __name__ == "__main__":
    # Which parameter is which?? This is unreadable!
    house = BadHouse(2, 5, True, True, False, True, "wood", "gable", True, False)
    print(f"  {house}")

    print()
    print("10 parameters in the constructor!")
    print("What does the 4th True mean? Nobody knows without checking.")
    print("→ The Builder pattern fixes this.")
