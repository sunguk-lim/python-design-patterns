"""
=============================================================
 BAD EXAMPLE: Without the Proxy Pattern
=============================================================

A heavy database that loads ALL data on initialization,
and has no access control.

Problems:
    1. Expensive resource loaded even if never used
    2. No access control — anyone can read/write
    3. No caching — same query executed repeatedly
    4. No logging — can't track who accessed what
=============================================================
"""


class BadDatabase:
    def __init__(self):
        print("  🔌 Loading entire database into memory... (5 seconds)")
        self.data = {"users": 1000, "orders": 5000, "products": 300}

    def query(self, table: str) -> int:
        return self.data.get(table, 0)


if __name__ == "__main__":
    # Database loaded immediately, even if we only need one query
    db = BadDatabase()
    print(f"  Users: {db.query('users')}")

    # No access control
    print(f"  Orders: {db.query('orders')}")  # anyone can query anything

    # Same query again — no caching
    print(f"  Users again: {db.query('users')}")  # hits DB again

    print()
    print("Problems: eager loading, no access control, no caching.")
    print("→ The Proxy pattern fixes this.")
