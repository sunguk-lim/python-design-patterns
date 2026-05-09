"""
=============================================================
 DESIGN PATTERN #23: REPOSITORY (Bonus)
=============================================================

Category: Architectural / Data Access
Intent:   Mediate between the domain/business logic and data
          mapping layers using a collection-like interface.

Real-world analogy:
    A library. You don't go into the warehouse to find a book.
    You ask the librarian (repository) to find, add, or remove
    books. The librarian knows WHERE books are stored; you don't.

When to use:
    - You want to separate business logic from data access
    - You need to swap data sources (SQL → NoSQL → API → file)
    - You want testable code (mock the repository in tests)

=============================================================
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass


# ---------------------------------------------------------
# STEP 1: Domain model (pure business object)
# ---------------------------------------------------------

@dataclass
class User:
    id: int
    name: str
    email: str


# ---------------------------------------------------------
# STEP 2: Repository interface
# ---------------------------------------------------------

class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, user_id: int) -> User | None:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> None:
        pass


# ---------------------------------------------------------
# STEP 3: Concrete implementations
# ---------------------------------------------------------

class InMemoryUserRepository(UserRepository):
    """For development and testing."""
    def __init__(self):
        self._store: dict[int, User] = {}
        self._next_id = 1

    def get_by_id(self, user_id: int) -> User | None:
        return self._store.get(user_id)

    def get_all(self) -> list[User]:
        return list(self._store.values())

    def save(self, user: User) -> None:
        if user.id == 0:
            user.id = self._next_id
            self._next_id += 1
        self._store[user.id] = user
        print(f"  💾 [InMemory] Saved: {user}")

    def delete(self, user_id: int) -> None:
        if user_id in self._store:
            removed = self._store.pop(user_id)
            print(f"  🗑️  [InMemory] Deleted: {removed}")


class FileUserRepository(UserRepository):
    """Simulates file-based storage."""
    def __init__(self):
        self._data: dict[int, User] = {}

    def get_by_id(self, user_id: int) -> User | None:
        print(f"  📂 [File] Reading user {user_id} from disk...")
        return self._data.get(user_id)

    def get_all(self) -> list[User]:
        print(f"  📂 [File] Reading all users from disk...")
        return list(self._data.values())

    def save(self, user: User) -> None:
        self._data[user.id] = user
        print(f"  📂 [File] Wrote user to disk: {user}")

    def delete(self, user_id: int) -> None:
        if user_id in self._data:
            self._data.pop(user_id)
            print(f"  📂 [File] Deleted user {user_id} from disk")


# ---------------------------------------------------------
# STEP 4: Business logic — depends on interface, not impl
# ---------------------------------------------------------

class UserService:
    def __init__(self, repo: UserRepository):
        self._repo = repo  # depends on abstraction!

    def register_user(self, name: str, email: str) -> User:
        user = User(id=0, name=name, email=email)
        self._repo.save(user)
        return user

    def find_user(self, user_id: int) -> User | None:
        return self._repo.get_by_id(user_id)

    def remove_user(self, user_id: int) -> None:
        self._repo.delete(user_id)

    def list_users(self) -> list[User]:
        return self._repo.get_all()


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Using in-memory repository (for dev/test)
    print("=== InMemory Repository ===")
    repo = InMemoryUserRepository()
    service = UserService(repo)

    service.register_user("Alice", "alice@mail.com")
    service.register_user("Bob", "bob@mail.com")
    service.register_user("Charlie", "charlie@mail.com")

    print(f"\n  All users: {service.list_users()}")
    print(f"  Find #2: {service.find_user(2)}")

    service.remove_user(2)
    print(f"  After delete: {service.list_users()}")

    # Swap to file repository — business logic unchanged!
    print("\n=== File Repository (same business logic!) ===")
    file_repo = FileUserRepository()
    file_service = UserService(file_repo)

    file_service.register_user("Diana", "diana@mail.com")
    file_service.find_user(0)

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Business logic (UserService) has ZERO data access code.")
    print("2. Swap InMemory → File → SQL → API by changing one line.")
    print("3. Testing: use InMemoryRepository (no real DB needed).")
    print("4. Each repository handles its own storage details.")
    print("5. This is the foundation of clean architecture.")
