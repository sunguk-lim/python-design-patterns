"""
=============================================================
 DESIGN PATTERN #1: STRATEGY
=============================================================

Category: Behavioral
Intent:   Define a family of algorithms, encapsulate each one,
          and make them interchangeable at runtime.

Real-world analogy:
    Think of paying at a store. You can pay by cash, credit card,
    or mobile payment. The store doesn't care HOW you pay —
    it just asks you to "pay". Each payment method is a "strategy".

When to use:
    - You have multiple ways to do the same thing
    - You want to switch algorithms at runtime
    - You want to avoid long if/elif/else chains

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Define the Strategy interface
# ---------------------------------------------------------
# This is the "contract" — every strategy must implement this.

class RouteStrategy(ABC):
    @abstractmethod
    def calculate_route(self, origin: str, destination: str) -> str:
        pass


# ---------------------------------------------------------
# STEP 2: Implement concrete strategies
# ---------------------------------------------------------
# Each class = one algorithm. Clean, isolated, testable.

class CarRoute(RouteStrategy):
    def calculate_route(self, origin: str, destination: str) -> str:
        return f"🚗 Driving route from {origin} to {destination}: Use highways, avoid tolls."


class BicycleRoute(RouteStrategy):
    def calculate_route(self, origin: str, destination: str) -> str:
        return f"🚲 Cycling route from {origin} to {destination}: Use bike lanes, avoid hills."


class WalkingRoute(RouteStrategy):
    def calculate_route(self, origin: str, destination: str) -> str:
        return f"🚶 Walking route from {origin} to {destination}: Use sidewalks, take shortcuts through parks."


# ---------------------------------------------------------
# STEP 3: The Context class — uses a strategy
# ---------------------------------------------------------
# The Navigator doesn't know HOW the route is calculated.
# It just delegates to whatever strategy it's given.

class Navigator:
    def __init__(self, strategy: RouteStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: RouteStrategy):
        """Change the strategy at runtime!"""
        self._strategy = strategy

    def navigate(self, origin: str, destination: str) -> str:
        return self._strategy.calculate_route(origin, destination)


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Create a navigator with a car strategy
    nav = Navigator(CarRoute())
    print(nav.navigate("Home", "Office"))

    # User switches to bicycle — just swap the strategy!
    nav.set_strategy(BicycleRoute())
    print(nav.navigate("Home", "Office"))

    # User switches to walking
    nav.set_strategy(WalkingRoute())
    print(nav.navigate("Home", "Office"))

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Navigator doesn't contain any routing logic itself.")
    print("2. Adding a new transport mode = just add a new class.")
    print("3. No if/elif/else chains. No modification of existing code.")
    print("4. This follows the Open/Closed Principle:")
    print("   → Open for extension, Closed for modification.")
