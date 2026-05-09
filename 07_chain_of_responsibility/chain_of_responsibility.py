"""
=============================================================
 DESIGN PATTERN #7: CHAIN OF RESPONSIBILITY
=============================================================

Category: Behavioral
Intent:   Pass a request along a chain of handlers. Each handler
          decides either to process the request or pass it to
          the next handler in the chain.

Real-world analogy:
    A call center. You call tech support → if they can't help,
    they transfer you to a specialist → if still unresolved,
    they escalate to a manager. Each person in the chain either
    handles it or passes it along.

When to use:
    - Multiple objects may handle a request, and the handler
      isn't known in advance
    - You want to decouple the sender from the receiver
    - You want to dynamically configure the processing chain

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: The Handler interface
# ---------------------------------------------------------

class SupportHandler(ABC):
    def __init__(self):
        self._next_handler: SupportHandler | None = None

    def set_next(self, handler: "SupportHandler") -> "SupportHandler":
        """Chain this handler to the next one. Returns next for fluent API."""
        self._next_handler = handler
        return handler

    def handle(self, issue: str, severity: int) -> None:
        """Try to handle, or pass to next in chain."""
        if self.can_handle(severity):
            self.process(issue, severity)
        elif self._next_handler:
            self._next_handler.handle(issue, severity)
        else:
            print(f"  ❌ No handler available for '{issue}' (severity {severity})")

    @abstractmethod
    def can_handle(self, severity: int) -> bool:
        pass

    @abstractmethod
    def process(self, issue: str, severity: int) -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete handlers
# ---------------------------------------------------------

class BasicSupport(SupportHandler):
    def can_handle(self, severity: int) -> bool:
        return severity <= 1

    def process(self, issue: str, severity: int) -> None:
        print(f"  👤 Basic Support: Resolved '{issue}' with FAQ.")


class ManagerSupport(SupportHandler):
    def can_handle(self, severity: int) -> bool:
        return severity <= 3

    def process(self, issue: str, severity: int) -> None:
        print(f"  👔 Manager: Escalated and resolved '{issue}'.")


class DirectorSupport(SupportHandler):
    def can_handle(self, severity: int) -> bool:
        return severity <= 5

    def process(self, issue: str, severity: int) -> None:
        print(f"  🏢 Director: Emergency meeting for '{issue}'.")


class CEOSupport(SupportHandler):
    """Easy to add a new level — just create a new class!"""
    def can_handle(self, severity: int) -> bool:
        return severity <= 10

    def process(self, issue: str, severity: int) -> None:
        print(f"  👑 CEO: Personal intervention for '{issue}'.")


# ---------------------------------------------------------
# STEP 3: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Build the chain: Basic → Manager → Director → CEO
    basic = BasicSupport()
    basic.set_next(ManagerSupport()) \
         .set_next(DirectorSupport()) \
         .set_next(CEOSupport())

    tickets = [
        ("Password reset", 1),
        ("Billing dispute", 3),
        ("Data breach", 5),
        ("Alien invasion", 7),
    ]

    for issue, severity in tickets:
        print(f"\n🎫 Ticket: '{issue}' (severity: {severity})")
        basic.handle(issue, severity)

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Each handler only knows about its own responsibility.")
    print("2. The chain is configurable — reorder or extend easily.")
    print("3. Adding CEO level = new class, no existing code changed.")
    print("4. The sender (ticket) doesn't know who will handle it.")
    print("5. If no one handles it, you get a clear fallback message.")
