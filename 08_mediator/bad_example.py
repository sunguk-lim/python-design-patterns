"""
=============================================================
 BAD EXAMPLE: Without the Mediator Pattern
=============================================================

A chat room where users communicate directly with each other.

Problems:
    1. Every user must hold references to every other user
    2. Adding a new user → update ALL existing users
    3. N users = N*(N-1) connections (exponential complexity)
    4. Can't add features like logging or filtering centrally
=============================================================
"""


class BadUser:
    def __init__(self, name: str):
        self.name = name
        self.contacts: list["BadUser"] = []

    def add_contact(self, user: "BadUser"):
        self.contacts.append(user)

    def send(self, message: str):
        print(f"  {self.name} sends: '{message}'")
        for contact in self.contacts:
            contact.receive(message, self.name)

    def receive(self, message: str, sender: str):
        print(f"    {self.name} received from {sender}: '{message}'")


if __name__ == "__main__":
    alice = BadUser("Alice")
    bob = BadUser("Bob")
    charlie = BadUser("Charlie")

    # Every user must know about every other user!
    alice.add_contact(bob)
    alice.add_contact(charlie)
    bob.add_contact(alice)
    bob.add_contact(charlie)
    charlie.add_contact(alice)
    charlie.add_contact(bob)

    alice.send("Hello everyone!")

    print()
    print("3 users = 6 connections. 10 users = 90 connections!")
    print("→ The Mediator pattern fixes this.")
