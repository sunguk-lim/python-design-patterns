# Lesson 23: Repository Pattern (Bonus)

## Category
Architectural / Data Access

## Intent
Mediate between business logic and data access using a collection-like interface.

## Real-World Analogy
A library. You ask the librarian to find/add/remove books. You don't
go into the warehouse yourself.

## Structure

```
┌─────────────┐  uses     ┌────────────────┐
│ UserService │ ────────→ │ UserRepository │ (interface)
│ (business)  │           │  get_by_id()   │
│             │           │  save()        │
│ zero SQL!   │           │  delete()      │
└─────────────┘           └────────────────┘
                              ▲         ▲
                              │         │
                    ┌──────────┐  ┌──────────┐
                    │ InMemory │  │   File   │
                    │   Repo   │  │   Repo   │
                    └──────────┘  └──────────┘
```

## When to Use
- Separate business logic from data access
- Need to swap data sources
- Want testable code (mock the repo)

## Key Takeaways
1. Business logic has zero data access code
2. Swap storage by changing one line
3. Test with in-memory repo (no real DB)
4. Foundation of clean architecture

## Files
- `bad_example.py` — SQL mixed into business logic
- `repository.py` — clean separation via repository interface
