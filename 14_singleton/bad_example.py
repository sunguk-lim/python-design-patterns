"""
=============================================================
 BAD EXAMPLE: Without the Singleton Pattern
=============================================================

A database connection and app configuration.

Problems:
    1. Multiple instances waste resources (multiple DB connections)
    2. Config changes in one instance don't reflect in others
    3. No guarantee of a single source of truth
=============================================================
"""


class BadDatabase:
    def __init__(self):
        print("  🔌 Opening NEW database connection...")
        self.connection_id = id(self)

    def query(self, sql: str):
        print(f"  [Conn #{self.connection_id}] Executing: {sql}")


if __name__ == "__main__":
    db1 = BadDatabase()
    db2 = BadDatabase()
    db3 = BadDatabase()

    print(f"\n  db1 is db2? {db1 is db2}")  # False!
    print(f"  Three separate connections created!")

    db1.query("SELECT * FROM users")
    db2.query("SELECT * FROM users")  # wasteful duplicate connection

    print()
    print("3 instances = 3 database connections. Wasteful!")
    print("In production, this can exhaust connection pools.")
    print("→ The Singleton pattern fixes this.")
