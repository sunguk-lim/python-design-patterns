"""
=============================================================
 DESIGN PATTERN #24: DEPENDENCY INJECTION (Bonus)
=============================================================

Category: Architectural / Creational
Intent:   Instead of a class creating its own dependencies,
          they are "injected" from outside. This inverts
          the control of dependency creation.

Real-world analogy:
    A restaurant chef doesn't grow their own vegetables.
    Ingredients (dependencies) are DELIVERED to the kitchen.
    The chef can work with any supplier — they just need
    ingredients that meet the spec.

Three types of injection:
    1. Constructor injection (most common, recommended)
    2. Method injection (per-call flexibility)
    3. Property injection (optional dependencies)

When to use:
    - You want loosely coupled, testable code
    - You need to swap implementations easily
    - You want configurable behavior without code changes

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Define abstractions (interfaces)
# ---------------------------------------------------------

class MessageSender(ABC):
    @abstractmethod
    def send(self, to: str, message: str) -> None:
        pass


class Logger(ABC):
    @abstractmethod
    def log(self, message: str) -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete implementations
# ---------------------------------------------------------

class EmailSender(MessageSender):
    def send(self, to: str, message: str) -> None:
        print(f"  📧 Email to {to}: '{message}'")


class SMSSender(MessageSender):
    def send(self, to: str, message: str) -> None:
        print(f"  📱 SMS to {to}: '{message}'")


class SlackSender(MessageSender):
    def send(self, to: str, message: str) -> None:
        print(f"  💬 Slack to {to}: '{message}'")


class ConsoleLogger(Logger):
    def log(self, message: str) -> None:
        print(f"  📝 LOG: {message}")


class NullLogger(Logger):
    """Silent logger — useful for tests."""
    def log(self, message: str) -> None:
        pass  # intentionally silent


# ---------------------------------------------------------
# STEP 3: Service with injected dependencies
# ---------------------------------------------------------

class NotificationService:
    # Constructor injection — dependencies provided from outside
    def __init__(self, sender: MessageSender, logger: Logger):
        self._sender = sender
        self._logger = logger

    def notify(self, user: str, message: str) -> None:
        self._sender.send(user, message)
        self._logger.log(f"Notified {user}: '{message}'")

    def broadcast(self, users: list[str], message: str) -> None:
        for user in users:
            self.notify(user, message)
        self._logger.log(f"Broadcast to {len(users)} users complete")


# ---------------------------------------------------------
# STEP 4: A simple DI container (optional, for larger apps)
# ---------------------------------------------------------

class Container:
    """A minimal dependency injection container."""
    def __init__(self):
        self._factories = {}

    def register(self, interface: type, factory) -> None:
        self._factories[interface] = factory

    def resolve(self, interface: type):
        if interface not in self._factories:
            raise KeyError(f"No registration for {interface}")
        return self._factories[interface]()


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    users = ["alice@mail.com", "bob@mail.com", "charlie@mail.com"]

    # --- Configuration 1: Email + Logging ---
    print("=== Email notifications with logging ===")
    service = NotificationService(
        sender=EmailSender(),
        logger=ConsoleLogger(),
    )
    service.notify("alice@mail.com", "Your order shipped!")

    # --- Configuration 2: SMS + No logging ---
    print("\n=== SMS notifications (silent logging) ===")
    service = NotificationService(
        sender=SMSSender(),
        logger=NullLogger(),  # no logging in production
    )
    service.notify("010-1234-5678", "Verification code: 1234")

    # --- Configuration 3: Slack + Logging ---
    print("\n=== Slack broadcast ===")
    service = NotificationService(
        sender=SlackSender(),
        logger=ConsoleLogger(),
    )
    service.broadcast(["#general", "#dev", "#ops"], "Deploy v2.0 complete!")

    # --- Using a DI Container ---
    print("\n=== Using DI Container ===")
    container = Container()
    container.register(MessageSender, lambda: EmailSender())
    container.register(Logger, lambda: ConsoleLogger())

    service = NotificationService(
        sender=container.resolve(MessageSender),
        logger=container.resolve(Logger),
    )
    service.notify("diana@mail.com", "Welcome!")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Dependencies are INJECTED, not created internally.")
    print("2. Same NotificationService works with Email, SMS, or Slack.")
    print("3. Testing: inject NullLogger or mock sender — no real I/O.")
    print("4. Configuration happens at the 'composition root' (main).")
    print("5. DI Container automates dependency wiring for large apps.")
    print("6. This is arguably THE most important pattern for")
    print("   writing maintainable, testable code.")
