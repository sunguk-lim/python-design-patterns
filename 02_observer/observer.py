"""
=============================================================
 DESIGN PATTERN #2: OBSERVER
=============================================================

Category: Behavioral
Intent:   Define a one-to-many dependency between objects so that
          when one object changes state, all its dependents are
          notified and updated automatically.

Real-world analogy:
    YouTube subscriptions. You subscribe to a channel, and you
    get notified when new content is uploaded. You can also
    unsubscribe anytime.

Key terms:
    - Subject (Publisher):  the object being watched
    - Observer (Subscriber): the object that reacts to changes

When to use:
    - When changes in one object should trigger updates in others
    - When you don't know in advance how many objects need updating
    - When you want loose coupling between the sender and receivers

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Define the Observer interface
# ---------------------------------------------------------
# Any class that wants to receive notifications must implement this.

class Observer(ABC):
    @abstractmethod
    def update(self, product: str) -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Define the Subject (Publisher)
# ---------------------------------------------------------
# The Subject doesn't know WHO is observing — it just knows
# that observers exist and they have an update() method.

class Store:
    def __init__(self):
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)
        print(f"  ✅ {observer} subscribed.")

    def unsubscribe(self, observer: Observer) -> None:
        self._observers.remove(observer)
        print(f"  ❌ {observer} unsubscribed.")

    def notify_all(self, product: str) -> None:
        for observer in self._observers:
            observer.update(product)

    def restock(self, product: str) -> None:
        print(f"\n📦 '{product}' is back in stock!")
        self.notify_all(product)


# ---------------------------------------------------------
# STEP 3: Implement concrete observers
# ---------------------------------------------------------
# Each observer decides HOW to react. The Store doesn't care.

class EmailSubscriber(Observer):
    def __init__(self, email: str):
        self.email = email

    def update(self, product: str) -> None:
        print(f"  📧 Email to {self.email}: '{product}' is now available!")

    def __str__(self):
        return f"EmailSubscriber({self.email})"


class SMSSubscriber(Observer):
    def __init__(self, phone: str):
        self.phone = phone

    def update(self, product: str) -> None:
        print(f"  📱 SMS to {self.phone}: '{product}' is now available!")

    def __str__(self):
        return f"SMSSubscriber({self.phone})"


class SlackSubscriber(Observer):
    """
    Look how easy it is to add a new notification channel!
    No modification to the Store class at all.
    """
    def __init__(self, channel: str):
        self.channel = channel

    def update(self, product: str) -> None:
        print(f"  💬 Slack #{self.channel}: '{product}' is now available!")

    def __str__(self):
        return f"SlackSubscriber(#{self.channel})"


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    store = Store()

    # Customers subscribe
    print("=== Subscribing ===")
    alice = EmailSubscriber("alice@mail.com")
    bob = SMSSubscriber("010-1234-5678")
    dev_team = SlackSubscriber("dev-alerts")

    store.subscribe(alice)
    store.subscribe(bob)
    store.subscribe(dev_team)

    # Product restocked → everyone gets notified
    store.restock("PlayStation 6")

    # Bob unsubscribes — he already bought one
    print("\n=== Bob unsubscribes ===")
    store.unsubscribe(bob)

    # Another restock → only remaining subscribers are notified
    store.restock("Nintendo Switch 2")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Store doesn't know about email, SMS, or Slack specifics.")
    print("2. Adding a new channel = just create a new Observer class.")
    print("3. Subscribers can join/leave at runtime.")
    print("4. Store and Observers are loosely coupled.")
    print("5. This is the foundation of event-driven programming!")
