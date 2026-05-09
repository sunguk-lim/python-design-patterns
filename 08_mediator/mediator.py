"""
=============================================================
 DESIGN PATTERN #8: MEDIATOR
=============================================================

Category: Behavioral
Intent:   Define an object that encapsulates how a set of objects
          interact. Promotes loose coupling by keeping objects from
          referring to each other explicitly.

Real-world analogy:
    An air traffic control tower. Planes don't communicate directly
    with each other — they all talk to the tower, and the tower
    coordinates everything. Without the tower, every plane would
    need to know about every other plane.

When to use:
    - Many objects communicate in complex ways
    - You want to centralize control logic
    - Objects should not refer to each other directly

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: The Mediator interface
# ---------------------------------------------------------

class ChatMediator(ABC):
    @abstractmethod
    def send_message(self, message: str, sender: "User") -> None:
        pass

    @abstractmethod
    def add_user(self, user: "User") -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete Mediator — the "control tower"
# ---------------------------------------------------------

class ChatRoom(ChatMediator):
    def __init__(self, name: str):
        self.name = name
        self._users: list["User"] = []

    def add_user(self, user: "User") -> None:
        self._users.append(user)
        user.chat_room = self
        print(f"  ✅ {user.name} joined #{self.name}")

    def send_message(self, message: str, sender: "User") -> None:
        print(f"  💬 [{self.name}] {sender.name}: '{message}'")
        for user in self._users:
            if user != sender:
                user.receive(message, sender.name)


# ---------------------------------------------------------
# STEP 3: The Colleague — each user only knows the mediator
# ---------------------------------------------------------

class User:
    def __init__(self, name: str):
        self.name = name
        self.chat_room: ChatMediator | None = None

    def send(self, message: str) -> None:
        if self.chat_room:
            self.chat_room.send_message(message, self)

    def receive(self, message: str, sender: str) -> None:
        print(f"    📩 {self.name} received from {sender}: '{message}'")


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Create the mediator (chat room)
    room = ChatRoom("general")

    # Create users — they DON'T know about each other
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    # Add users to the room
    print("=== Users joining ===")
    room.add_user(alice)
    room.add_user(bob)
    room.add_user(charlie)

    # Communication goes through the mediator
    print("\n=== Chatting ===")
    alice.send("Hello everyone!")
    bob.send("Hey Alice!")

    # Easy to add a new user — no changes to existing users
    print("\n=== New user joins ===")
    diana = User("Diana")
    room.add_user(diana)
    diana.send("Hi, I'm new here!")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Users don't know about each other — only the ChatRoom.")
    print("2. 10 users = 10 connections (to mediator), not 90.")
    print("3. Central place to add logging, filtering, etc.")
    print("4. New user joins? Just register with the mediator.")
    print("5. Similar to Observer, but Mediator is bidirectional")
    print("   and coordinates complex interactions.")
