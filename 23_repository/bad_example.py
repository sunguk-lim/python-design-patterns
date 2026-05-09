"""
=============================================================
 BAD EXAMPLE: Without the Repository Pattern
=============================================================

Business logic mixed directly with data access code.

Problems:
    1. SQL/database logic scattered throughout business code
    2. Can't switch databases without rewriting business logic
    3. Can't test business logic without a real database
    4. Violates Single Responsibility Principle
=============================================================
"""


class BadUserService:
    def __init__(self):
        # Pretend this is a real database
        self._db = {
            1: {"id": 1, "name": "Alice", "email": "alice@mail.com"},
            2: {"id": 2, "name": "Bob", "email": "bob@mail.com"},
        }

    def get_user(self, user_id: int):
        # Business logic mixed with data access!
        print(f"  SELECT * FROM users WHERE id = {user_id}")
        return self._db.get(user_id)

    def create_user(self, name: str, email: str):
        # More SQL mixed in...
        new_id = max(self._db.keys()) + 1
        print(f"  INSERT INTO users (name, email) VALUES ('{name}', '{email}')")
        self._db[new_id] = {"id": new_id, "name": name, "email": email}
        return self._db[new_id]

    def get_active_users(self):
        # What if we switch from SQL to MongoDB? Rewrite everything!
        print("  SELECT * FROM users WHERE active = true")
        return list(self._db.values())


if __name__ == "__main__":
    service = BadUserService()
    print(f"  User: {service.get_user(1)}")
    print(f"  New: {service.create_user('Charlie', 'charlie@mail.com')}")

    print()
    print("SQL is embedded in business logic.")
    print("Switch to MongoDB? Rewrite the entire service.")
    print("Write tests? Need a real database.")
    print("→ The Repository pattern fixes this.")
