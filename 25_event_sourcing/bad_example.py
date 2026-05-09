"""
=============================================================
 BAD EXAMPLE: Without Event Sourcing
=============================================================

A bank account that only stores the current balance.

Problems:
    1. No history — can't see HOW you got to the current balance
    2. Can't audit: "who deposited $500 on Tuesday?"
    3. Can't undo or replay: state is overwritten each time
    4. If a bug corrupts the balance, data is lost forever
    5. Can't rebuild state from scratch
=============================================================
"""


class BadBankAccount:
    def __init__(self, owner: str):
        self.owner = owner
        self.balance = 0  # only stores current state!

    def deposit(self, amount: float):
        self.balance += amount
        print(f"  Deposited ${amount:.2f}. Balance: ${self.balance:.2f}")

    def withdraw(self, amount: float):
        self.balance -= amount
        print(f"  Withdrew ${amount:.2f}. Balance: ${self.balance:.2f}")


if __name__ == "__main__":
    account = BadBankAccount("Alice")
    account.deposit(1000)
    account.deposit(500)
    account.withdraw(200)
    account.deposit(300)
    account.withdraw(150)

    print(f"\n  Final balance: ${account.balance:.2f}")
    print()
    print("How did we get to $1450?")
    print("When was each transaction? Who authorized it?")
    print("Can we undo the $200 withdrawal?")
    print("If a bug sets balance to $0, can we recover?")
    print("→ Event Sourcing fixes this.")
