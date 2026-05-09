"""
=============================================================
 DESIGN PATTERN #25: EVENT SOURCING (Bonus)
=============================================================

Category: Architectural
Intent:   Instead of storing just the current state, store a
          sequence of EVENTS that led to the current state.
          The current state is derived by replaying events.

Real-world analogy:
    An accountant's ledger. Instead of just writing "Balance: $1450",
    they record every transaction: deposit $1000, deposit $500,
    withdraw $200... The balance is CALCULATED from the ledger.
    If there's a dispute, you can trace every penny.

When to use:
    - You need a complete audit trail
    - You want to reconstruct state at any point in time
    - You need undo/redo or "time travel" debugging
    - Your domain is naturally event-based (banking, orders, etc.)

=============================================================
"""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


# ---------------------------------------------------------
# STEP 1: Define events
# ---------------------------------------------------------

class EventType(Enum):
    ACCOUNT_CREATED = "account_created"
    MONEY_DEPOSITED = "money_deposited"
    MONEY_WITHDRAWN = "money_withdrawn"
    ACCOUNT_FROZEN = "account_frozen"


@dataclass(frozen=True)
class Event:
    type: EventType
    data: dict
    timestamp: str = field(default_factory=lambda: datetime.now().strftime("%H:%M:%S"))

    def __str__(self):
        return f"[{self.timestamp}] {self.type.value}: {self.data}"


# ---------------------------------------------------------
# STEP 2: Event Store — the append-only log
# ---------------------------------------------------------

class EventStore:
    def __init__(self):
        self._events: list[Event] = []

    def append(self, event: Event) -> None:
        self._events.append(event)
        print(f"  📝 Event stored: {event}")

    def get_events(self) -> list[Event]:
        return list(self._events)

    def get_events_up_to(self, index: int) -> list[Event]:
        return self._events[:index + 1]


# ---------------------------------------------------------
# STEP 3: Aggregate — rebuilds state from events
# ---------------------------------------------------------

class BankAccount:
    def __init__(self, event_store: EventStore):
        self._store = event_store
        self.owner = ""
        self.balance = 0.0
        self.is_frozen = False

    # --- Commands (generate events) ---

    def create(self, owner: str) -> None:
        self._apply(Event(EventType.ACCOUNT_CREATED, {"owner": owner}))

    def deposit(self, amount: float) -> None:
        if self.is_frozen:
            print("  ❌ Account is frozen!")
            return
        self._apply(Event(EventType.MONEY_DEPOSITED, {"amount": amount}))

    def withdraw(self, amount: float) -> None:
        if self.is_frozen:
            print("  ❌ Account is frozen!")
            return
        if amount > self.balance:
            print(f"  ❌ Insufficient funds! Balance: ${self.balance:.2f}")
            return
        self._apply(Event(EventType.MONEY_WITHDRAWN, {"amount": amount}))

    def freeze(self) -> None:
        self._apply(Event(EventType.ACCOUNT_FROZEN, {}))

    # --- Event application ---

    def _apply(self, event: Event) -> None:
        """Store the event and update state."""
        self._store.append(event)
        self._handle(event)

    def _handle(self, event: Event) -> None:
        """Update state based on a single event."""
        if event.type == EventType.ACCOUNT_CREATED:
            self.owner = event.data["owner"]
        elif event.type == EventType.MONEY_DEPOSITED:
            self.balance += event.data["amount"]
        elif event.type == EventType.MONEY_WITHDRAWN:
            self.balance -= event.data["amount"]
        elif event.type == EventType.ACCOUNT_FROZEN:
            self.is_frozen = True

    # --- Rebuild state from events ---

    @classmethod
    def from_events(cls, event_store: EventStore) -> "BankAccount":
        """Reconstruct the account by replaying ALL events."""
        account = cls(event_store)
        for event in event_store.get_events():
            account._handle(event)
        return account

    @classmethod
    def from_events_at(cls, event_store: EventStore, index: int) -> "BankAccount":
        """Reconstruct state at a specific point in time."""
        account = cls(EventStore())  # empty store for replay
        for event in event_store.get_events_up_to(index):
            account._handle(event)
        return account

    def status(self) -> str:
        frozen = " [FROZEN]" if self.is_frozen else ""
        return f"  📊 {self.owner}: ${self.balance:.2f}{frozen}"


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    store = EventStore()
    account = BankAccount(store)

    print("=== Transactions ===")
    account.create("Alice")
    account.deposit(1000)
    account.deposit(500)
    account.withdraw(200)
    account.deposit(300)
    account.withdraw(150)

    print(f"\n{account.status()}")

    # Full audit trail!
    print("\n=== Audit Trail ===")
    for i, event in enumerate(store.get_events()):
        print(f"  [{i}] {event}")

    # Time travel — what was the state after event #3?
    print("\n=== Time Travel: State after event #3 ===")
    past_account = BankAccount.from_events_at(store, 3)
    print(past_account.status())

    # Rebuild from scratch — same result!
    print("\n=== Rebuild from events ===")
    rebuilt = BankAccount.from_events(store)
    print(rebuilt.status())

    # Try frozen account
    print("\n=== Freeze account ===")
    account.freeze()
    account.deposit(999)  # rejected!
    print(account.status())

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Events are the source of truth, not current state.")
    print("2. State is DERIVED by replaying events.")
    print("3. Complete audit trail — every change is recorded.")
    print("4. Time travel — reconstruct state at any point.")
    print("5. Events are immutable — append-only, never modified.")
    print("6. If state is corrupted, just replay events to rebuild.")
    print()
    print("🎓 CONGRATULATIONS! You've completed all 25 design patterns!")
