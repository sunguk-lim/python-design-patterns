"""
=============================================================
 BAD EXAMPLE: Without the Factory Method Pattern
=============================================================

A logistics app that creates different transports.

Problems:
    1. Client code is tightly coupled to concrete classes
    2. Adding a new transport = modify client code everywhere
    3. Object creation logic is scattered across the codebase
    4. Hard to test — can't substitute mock objects easily
=============================================================
"""


class Truck:
    def deliver(self):
        return "📦 Delivering by truck on the road"


class Ship:
    def deliver(self):
        return "🚢 Delivering by ship across the sea"


def create_transport(transport_type: str):
    """Creation logic scattered and coupled to concrete types."""
    if transport_type == "truck":
        return Truck()
    elif transport_type == "ship":
        return Ship()
    # elif transport_type == "drone": ...  ← modify HERE
    # elif transport_type == "train": ...  ← and HERE
    else:
        raise ValueError(f"Unknown transport: {transport_type}")


if __name__ == "__main__":
    for t in ["truck", "ship"]:
        transport = create_transport(t)
        print(f"  {transport.deliver()}")

    print()
    print("Client must know about 'truck', 'ship' as strings.")
    print("Adding 'drone' means changing the factory function")
    print("AND any code that calls it.")
    print("→ The Factory Method pattern fixes this.")
