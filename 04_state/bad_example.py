"""
=============================================================
 BAD EXAMPLE: Without the State Pattern
=============================================================

A vending machine with multiple states: idle, has_money, dispensing.

Problems:
    1. Every method has if/elif checks for the current state
    2. Adding a new state → modify EVERY method
    3. Easy to forget a state transition → bugs
    4. The class grows huge as states multiply
=============================================================
"""


class BadVendingMachine:
    def __init__(self):
        self.state = "idle"
        self.balance = 0

    def insert_money(self, amount: int):
        if self.state == "idle":
            self.balance = amount
            self.state = "has_money"
            print(f"  Inserted ${amount}. Balance: ${self.balance}")
        elif self.state == "has_money":
            self.balance += amount
            print(f"  Added ${amount}. Balance: ${self.balance}")
        elif self.state == "dispensing":
            print("  ⚠️ Please wait, dispensing in progress...")
        # elif self.state == "out_of_stock": ...
        # elif self.state == "maintenance": ...
        # Every new state = another elif HERE and in EVERY method!

    def select_product(self, price: int):
        if self.state == "idle":
            print("  ⚠️ Please insert money first.")
        elif self.state == "has_money":
            if self.balance >= price:
                self.state = "dispensing"
                print(f"  Dispensing product (${price})...")
                self.balance -= price
                self.state = "idle"
                if self.balance > 0:
                    print(f"  Change: ${self.balance}")
                    self.balance = 0
            else:
                print(f"  ⚠️ Not enough money. Need ${price}, have ${self.balance}")
        elif self.state == "dispensing":
            print("  ⚠️ Please wait, dispensing in progress...")

    def cancel(self):
        if self.state == "idle":
            print("  Nothing to cancel.")
        elif self.state == "has_money":
            print(f"  Returning ${self.balance}.")
            self.balance = 0
            self.state = "idle"
        elif self.state == "dispensing":
            print("  ⚠️ Cannot cancel during dispensing.")


if __name__ == "__main__":
    machine = BadVendingMachine()
    machine.select_product(5)
    machine.insert_money(3)
    machine.insert_money(2)
    machine.select_product(4)

    print()
    print("This works, but every method is full of if/elif state checks.")
    print("Adding a 'maintenance' or 'out_of_stock' state would mean")
    print("editing EVERY method. → The State pattern fixes this.")
