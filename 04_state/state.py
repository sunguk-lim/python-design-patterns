"""
=============================================================
 DESIGN PATTERN #4: STATE
=============================================================

Category: Behavioral
Intent:   Allow an object to alter its behavior when its internal
          state changes. The object will appear to change its class.

Real-world analogy:
    A traffic light. When it's green, cars go. When it's red,
    cars stop. The light itself doesn't have if/elif logic —
    it simply switches between state objects.

When to use:
    - An object behaves differently depending on its state
    - You have many if/elif checks on a state variable
    - State transitions are complex and error-prone

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Define the State interface
# ---------------------------------------------------------
# Each state handles the SAME set of actions differently.

class VendingState(ABC):
    @abstractmethod
    def insert_money(self, machine: "VendingMachine", amount: int) -> None:
        pass

    @abstractmethod
    def select_product(self, machine: "VendingMachine", price: int) -> None:
        pass

    @abstractmethod
    def cancel(self, machine: "VendingMachine") -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Implement concrete states
# ---------------------------------------------------------
# Each state class is clean and focused on ONE state's behavior.

class IdleState(VendingState):
    def insert_money(self, machine: "VendingMachine", amount: int) -> None:
        machine.balance = amount
        print(f"  💰 Inserted ${amount}. Balance: ${machine.balance}")
        machine.set_state(HasMoneyState())

    def select_product(self, machine: "VendingMachine", price: int) -> None:
        print("  ⚠️ Please insert money first.")

    def cancel(self, machine: "VendingMachine") -> None:
        print("  Nothing to cancel.")

    def __str__(self):
        return "IdleState"


class HasMoneyState(VendingState):
    def insert_money(self, machine: "VendingMachine", amount: int) -> None:
        machine.balance += amount
        print(f"  💰 Added ${amount}. Balance: ${machine.balance}")

    def select_product(self, machine: "VendingMachine", price: int) -> None:
        if machine.balance >= price:
            machine.set_state(DispensingState())
            machine.state.dispense(machine, price)
        else:
            print(f"  ⚠️ Not enough. Need ${price}, have ${machine.balance}")

    def cancel(self, machine: "VendingMachine") -> None:
        print(f"  💰 Returning ${machine.balance}.")
        machine.balance = 0
        machine.set_state(IdleState())

    def __str__(self):
        return "HasMoneyState"


class DispensingState(VendingState):
    def insert_money(self, machine: "VendingMachine", amount: int) -> None:
        print("  ⚠️ Please wait, dispensing in progress...")

    def select_product(self, machine: "VendingMachine", price: int) -> None:
        print("  ⚠️ Please wait, dispensing in progress...")

    def cancel(self, machine: "VendingMachine") -> None:
        print("  ⚠️ Cannot cancel during dispensing.")

    def dispense(self, machine: "VendingMachine", price: int) -> None:
        print(f"  📦 Dispensing product (${price})...")
        machine.balance -= price
        if machine.balance > 0:
            print(f"  💰 Change: ${machine.balance}")
            machine.balance = 0
        machine.set_state(IdleState())

    def __str__(self):
        return "DispensingState"


# ---------------------------------------------------------
# STEP 3: The Context — delegates everything to current state
# ---------------------------------------------------------

class VendingMachine:
    def __init__(self):
        self.balance = 0
        self.state: VendingState = IdleState()

    def set_state(self, state: VendingState) -> None:
        print(f"    [State: {self.state} → {state}]")
        self.state = state

    def insert_money(self, amount: int) -> None:
        self.state.insert_money(self, amount)

    def select_product(self, price: int) -> None:
        self.state.select_product(self, price)

    def cancel(self) -> None:
        self.state.cancel(self)


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    machine = VendingMachine()

    print("=== Try to buy without money ===")
    machine.select_product(5)

    print("\n=== Insert money and buy ===")
    machine.insert_money(3)
    machine.insert_money(4)
    machine.select_product(5)

    print("\n=== Insert money and cancel ===")
    machine.insert_money(10)
    machine.cancel()

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. No if/elif chains — each state is its own class.")
    print("2. Adding 'MaintenanceState' = just add a new class.")
    print("3. State transitions are explicit and easy to trace.")
    print("4. Each state class is small, focused, and testable.")
    print("5. Very similar to Strategy, but the STATE decides")
    print("   when to transition (not the client).")
