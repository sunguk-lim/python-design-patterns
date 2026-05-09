"""
=============================================================
 BAD EXAMPLE: Without the Chain of Responsibility Pattern
=============================================================

A support ticket system with levels: basic, manager, director.

Problems:
    1. One giant method with nested if/elif for every level
    2. Adding a new support level → modify the method
    3. Can't reorder or reconfigure the chain dynamically
    4. All logic crammed into one place
=============================================================
"""


class BadSupportSystem:
    def handle_ticket(self, issue: str, severity: int):
        print(f"\n🎫 Ticket: '{issue}' (severity: {severity})")

        if severity <= 1:
            print(f"  👤 Basic Support: Resolved '{issue}' with FAQ.")
        elif severity <= 3:
            print(f"  👔 Manager: Escalated and resolved '{issue}'.")
        elif severity <= 5:
            print(f"  🏢 Director: Emergency meeting for '{issue}'.")
        else:
            print(f"  ❌ No one can handle severity {severity}!")
        # Add VP level? CEO level? Edit this method again...


if __name__ == "__main__":
    system = BadSupportSystem()
    system.handle_ticket("Password reset", 1)
    system.handle_ticket("Billing dispute", 3)
    system.handle_ticket("Data breach", 5)
    system.handle_ticket("Alien invasion", 7)

    print()
    print("All logic is in one method with nested if/elif.")
    print("→ The Chain of Responsibility pattern fixes this.")
