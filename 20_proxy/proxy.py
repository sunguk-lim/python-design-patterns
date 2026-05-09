"""
=============================================================
 DESIGN PATTERN #20: PROXY
=============================================================

Category: Structural
Intent:   Provide a surrogate or placeholder for another object
          to control access to it.

Real-world analogy:
    A credit card is a proxy for your bank account. It provides
    the same "pay" interface but adds security checks, spending
    limits, and transaction logging — all without modifying
    your actual bank account.

Types of proxies:
    - Virtual Proxy: lazy initialization (load when first used)
    - Protection Proxy: access control (check permissions)
    - Caching Proxy: store results to avoid repeated work
    - Logging Proxy: log all interactions

When to use:
    - You want lazy initialization of expensive objects
    - You need access control
    - You want caching, logging, or rate limiting
    - The proxy has the SAME interface as the real object

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Subject interface — same for real and proxy
# ---------------------------------------------------------

class Database(ABC):
    @abstractmethod
    def query(self, table: str) -> int:
        pass


# ---------------------------------------------------------
# STEP 2: Real subject — the expensive object
# ---------------------------------------------------------

class RealDatabase(Database):
    def __init__(self):
        print("  🔌 Loading entire database into memory...")
        self.data = {"users": 1000, "orders": 5000, "products": 300}

    def query(self, table: str) -> int:
        return self.data.get(table, 0)


# ---------------------------------------------------------
# STEP 3: Virtual Proxy — lazy loading
# ---------------------------------------------------------

class LazyDatabaseProxy(Database):
    def __init__(self):
        self._real_db: RealDatabase | None = None

    def query(self, table: str) -> int:
        if self._real_db is None:
            print("  ⏳ First access — initializing database...")
            self._real_db = RealDatabase()
        return self._real_db.query(table)


# ---------------------------------------------------------
# STEP 4: Protection Proxy — access control
# ---------------------------------------------------------

class ProtectedDatabaseProxy(Database):
    def __init__(self, db: Database, user_role: str):
        self._db = db
        self._user_role = user_role
        self._restricted = {"orders", "products"}

    def query(self, table: str) -> int:
        if table in self._restricted and self._user_role != "admin":
            print(f"  🚫 Access denied: '{self._user_role}' cannot query '{table}'")
            return -1
        return self._db.query(table)


# ---------------------------------------------------------
# STEP 5: Caching Proxy — avoid repeated work
# ---------------------------------------------------------

class CachingDatabaseProxy(Database):
    def __init__(self, db: Database):
        self._db = db
        self._cache: dict[str, int] = {}

    def query(self, table: str) -> int:
        if table in self._cache:
            print(f"  ⚡ Cache hit for '{table}'")
            return self._cache[table]
        print(f"  🔍 Cache miss for '{table}' — querying database...")
        result = self._db.query(table)
        self._cache[table] = result
        return result


# ---------------------------------------------------------
# STEP 6: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=== Virtual Proxy (lazy loading) ===")
    lazy_db = LazyDatabaseProxy()
    print("  Database NOT loaded yet!")
    print(f"  Users: {lazy_db.query('users')}")  # loads here
    print(f"  Orders: {lazy_db.query('orders')}")  # already loaded

    print("\n=== Caching Proxy ===")
    real_db = RealDatabase()
    cached_db = CachingDatabaseProxy(real_db)
    print(f"  Users: {cached_db.query('users')}")  # miss
    print(f"  Users: {cached_db.query('users')}")  # hit!
    print(f"  Orders: {cached_db.query('orders')}")  # miss
    print(f"  Orders: {cached_db.query('orders')}")  # hit!

    print("\n=== Protection Proxy ===")
    protected_db = ProtectedDatabaseProxy(real_db, "viewer")
    print(f"  Users: {protected_db.query('users')}")  # allowed
    print(f"  Orders: {protected_db.query('orders')}")  # denied!

    protected_admin = ProtectedDatabaseProxy(real_db, "admin")
    print(f"  Orders (admin): {protected_admin.query('orders')}")  # allowed

    print("\n=== Stacking Proxies (Lazy + Cached + Protected) ===")
    stacked = ProtectedDatabaseProxy(
        CachingDatabaseProxy(LazyDatabaseProxy()),
        "admin"
    )
    print(f"  Users: {stacked.query('users')}")
    print(f"  Users: {stacked.query('users')}")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Proxy has the SAME interface as the real object.")
    print("2. Virtual proxy: lazy init (load only when needed).")
    print("3. Protection proxy: access control.")
    print("4. Caching proxy: avoid repeated expensive operations.")
    print("5. Proxies can be stacked like decorators!")
