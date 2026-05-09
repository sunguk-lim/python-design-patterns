"""
=============================================================
 DESIGN PATTERN #14: SINGLETON
=============================================================

Category: Creational
Intent:   Ensure a class has only ONE instance, and provide a
          global point of access to it.

Real-world analogy:
    A country has one president at a time. No matter who asks
    "who is the president?", they all get the same person.

When to use:
    - You need exactly one instance (DB connection, config, logger)
    - You need a global access point to that instance
    - The instance should be created lazily (on first use)

CAUTION:
    Singleton is controversial! It's essentially a global variable.
    Overuse leads to tight coupling and hard-to-test code.
    Prefer dependency injection when possible.

=============================================================
"""


# ---------------------------------------------------------
# METHOD 1: Classic Singleton using __new__
# ---------------------------------------------------------

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True
        print("  🔌 Opening database connection (only once!)")
        self.connection_id = id(self)

    def query(self, sql: str) -> None:
        print(f"  [Conn #{self.connection_id}] Executing: {sql}")


# ---------------------------------------------------------
# METHOD 2: Singleton using a metaclass (more Pythonic)
# ---------------------------------------------------------

class SingletonMeta(type):
    """A metaclass that creates Singleton instances."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        print("  ⚙️  Loading app configuration (only once!)")
        self.settings = {"theme": "dark", "language": "en"}

    def get(self, key: str) -> str:
        return self.settings.get(key, "unknown")

    def set(self, key: str, value: str) -> None:
        self.settings[key] = value
        print(f"  ⚙️  Config updated: {key} = {value}")


# ---------------------------------------------------------
# METHOD 3: The simplest way — just use a module!
# ---------------------------------------------------------
# In Python, modules are singletons by nature.
# You can just create a module-level instance:
#
#   # config.py
#   settings = {"theme": "dark"}
#
#   # other files
#   from config import settings
#
# This is often the most Pythonic approach.


# ---------------------------------------------------------
# See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=== Database Singleton (__new__) ===")
    db1 = Database()
    db2 = Database()
    db3 = Database()

    print(f"  db1 is db2? {db1 is db2}")  # True!
    print(f"  db1 is db3? {db1 is db3}")  # True!
    db1.query("SELECT * FROM users")
    db2.query("INSERT INTO logs VALUES (...)")

    print("\n=== AppConfig Singleton (metaclass) ===")
    config1 = AppConfig()
    config2 = AppConfig()

    print(f"  config1 is config2? {config1 is config2}")  # True!
    config1.set("theme", "light")
    print(f"  config2 theme: {config2.get('theme')}")  # "light" — same instance!

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Only ONE instance is ever created.")
    print("2. All callers get the SAME instance.")
    print("3. Python offers 3 ways: __new__, metaclass, or module.")
    print("4. Module-level instance is often the most Pythonic.")
    print("5. CAUTION: Singletons are global state — use sparingly!")
    print("   Prefer dependency injection for testability.")
