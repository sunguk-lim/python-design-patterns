"""
=============================================================
 DESIGN PATTERN #11: FACTORY METHOD
=============================================================

Category: Creational
Intent:   Define an interface for creating an object, but let
          subclasses decide which class to instantiate.

Real-world analogy:
    A hiring agency. You tell the agency "I need a developer"
    (the what), and the agency decides which specific developer
    to send (the how). Different agencies specialize in different
    types of developers.

When to use:
    - You don't know in advance which class to instantiate
    - You want subclasses to control object creation
    - You want to decouple creation from usage

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Product interface
# ---------------------------------------------------------

class Transport(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

    @abstractmethod
    def get_cost_per_km(self) -> float:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete products
# ---------------------------------------------------------

class Truck(Transport):
    def deliver(self) -> str:
        return "📦 Delivering by truck on the road"

    def get_cost_per_km(self) -> float:
        return 1.5


class Ship(Transport):
    def deliver(self) -> str:
        return "🚢 Delivering by ship across the sea"

    def get_cost_per_km(self) -> float:
        return 0.5


class Drone(Transport):
    def deliver(self) -> str:
        return "🤖 Delivering by drone through the air"

    def get_cost_per_km(self) -> float:
        return 5.0


# ---------------------------------------------------------
# STEP 3: Creator with the factory method
# ---------------------------------------------------------

class Logistics(ABC):
    @abstractmethod
    def create_transport(self) -> Transport:
        """The factory method — subclasses decide WHAT to create."""
        pass

    def plan_delivery(self, distance: int) -> None:
        """Uses the factory method — doesn't know the concrete type."""
        transport = self.create_transport()
        cost = transport.get_cost_per_km() * distance
        print(f"  {transport.deliver()}")
        print(f"    Distance: {distance}km, Cost: ${cost:.2f}")


# ---------------------------------------------------------
# STEP 4: Concrete creators
# ---------------------------------------------------------

class RoadLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Truck()


class SeaLogistics(Logistics):
    def create_transport(self) -> Transport:
        return Ship()


class AirLogistics(Logistics):
    """New logistics type — no existing code changed!"""
    def create_transport(self) -> Transport:
        return Drone()


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    logistics_options: list[Logistics] = [
        RoadLogistics(),
        SeaLogistics(),
        AirLogistics(),
    ]

    for logistics in logistics_options:
        print(f"=== {logistics.__class__.__name__} ===")
        logistics.plan_delivery(100)
        print()

    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. plan_delivery() doesn't know if it's a Truck or Drone.")
    print("2. Each creator subclass decides which product to make.")
    print("3. Adding AirLogistics = new class, zero changes elsewhere.")
    print("4. The 'factory method' is create_transport() — that's it.")
    print("5. Client code works with the Logistics interface,")
    print("   never with concrete classes directly.")
