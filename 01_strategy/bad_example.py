"""
=============================================================
 BAD EXAMPLE: Without the Strategy Pattern
=============================================================

This is how beginners often write it. It works, but it becomes
a nightmare as the project grows.

Problems:
    1. Every new transport mode → modify this class (violates Open/Closed)
    2. The class keeps growing with if/elif chains
    3. Hard to test individual routing algorithms
    4. If car routing has a bug, you risk breaking bicycle routing too
=============================================================
"""


class BadNavigator:
    def navigate(self, mode: str, origin: str, destination: str) -> str:
        if mode == "car":
            return f"Driving from {origin} to {destination}: Use highways."
        elif mode == "bicycle":
            return f"Cycling from {origin} to {destination}: Use bike lanes."
        elif mode == "walking":
            return f"Walking from {origin} to {destination}: Use sidewalks."
        # Imagine adding 10 more modes here...
        # elif mode == "bus":
        # elif mode == "train":
        # elif mode == "scooter":
        # elif mode == "helicopter":
        # This method becomes HUGE and fragile!
        else:
            raise ValueError(f"Unknown mode: {mode}")


if __name__ == "__main__":
    nav = BadNavigator()
    print(nav.navigate("car", "Home", "Office"))
    print(nav.navigate("bicycle", "Home", "Office"))
    print(nav.navigate("walking", "Home", "Office"))

    print()
    print("This works... but what happens when you need to:")
    print("  - Add 10 more transport modes?")
    print("  - Test car routing independently?")
    print("  - Let users create custom routing algorithms?")
    print("  - Reuse bicycle routing in another app?")
    print()
    print("→ The Strategy pattern solves ALL of these problems.")
