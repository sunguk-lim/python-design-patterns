"""
=============================================================
 DESIGN PATTERN #16: DECORATOR
=============================================================

Category: Structural
Intent:   Attach additional responsibilities to an object dynamically.
          Decorators provide a flexible alternative to subclassing
          for extending functionality.

Real-world analogy:
    Wearing clothes. You (the base object) can add a shirt,
    then a jacket, then a scarf. Each layer adds functionality
    (warmth) without changing YOU. You can add/remove layers
    freely.

When to use:
    - You need to add behavior to objects dynamically
    - Subclassing would cause a class explosion
    - You want to combine behaviors freely (mix and match)

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Component interface
# ---------------------------------------------------------

class Beverage(ABC):
    @abstractmethod
    def cost(self) -> float:
        pass

    @abstractmethod
    def description(self) -> str:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete components (base objects)
# ---------------------------------------------------------

class Coffee(Beverage):
    def cost(self) -> float:
        return 2.00

    def description(self) -> str:
        return "Coffee"


class Tea(Beverage):
    def cost(self) -> float:
        return 1.50

    def description(self) -> str:
        return "Tea"


# ---------------------------------------------------------
# STEP 3: Decorator base class
# ---------------------------------------------------------
# A decorator IS a Beverage AND HAS a Beverage (wraps it).

class BeverageDecorator(Beverage, ABC):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage


# ---------------------------------------------------------
# STEP 4: Concrete decorators (toppings)
# ---------------------------------------------------------

class Milk(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 0.50

    def description(self) -> str:
        return self._beverage.description() + " + Milk"


class Sugar(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 0.20

    def description(self) -> str:
        return self._beverage.description() + " + Sugar"


class WhippedCream(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 0.70

    def description(self) -> str:
        return self._beverage.description() + " + Whipped Cream"


class Caramel(BeverageDecorator):
    def cost(self) -> float:
        return self._beverage.cost() + 0.60

    def description(self) -> str:
        return self._beverage.description() + " + Caramel"


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Build orders by wrapping decorators
    print("=== Orders ===")

    # Simple coffee
    order1 = Coffee()
    print(f"  {order1.description()}: ${order1.cost():.2f}")

    # Coffee with milk and sugar
    order2 = Sugar(Milk(Coffee()))
    print(f"  {order2.description()}: ${order2.cost():.2f}")

    # Fancy coffee: milk + sugar + whipped cream + caramel
    order3 = Caramel(WhippedCream(Sugar(Milk(Coffee()))))
    print(f"  {order3.description()}: ${order3.cost():.2f}")

    # Tea with milk
    order4 = Milk(Tea())
    print(f"  {order4.description()}: ${order4.cost():.2f}")

    # Double milk! (can apply same decorator twice)
    order5 = Milk(Milk(Coffee()))
    print(f"  {order5.description()}: ${order5.cost():.2f}")

    print(f"\n  Total classes: 2 bases + 4 decorators = 6")
    print(f"  Possible combinations: unlimited!")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. 4 toppings + 2 bases = 6 classes (not 32!).")
    print("2. Decorators wrap objects like layers of an onion.")
    print("3. Can apply the same decorator multiple times (double milk).")
    print("4. Add/remove behaviors dynamically at runtime.")
    print("5. Python also has @decorator syntax — same core idea!")
