# Lesson 17: Adapter Pattern

## Category
Structural

## Intent
Convert the interface of a class into another interface clients expect.

## Real-World Analogy
A power adapter for travel. Your US plug doesn't fit a European outlet.
The adapter converts one to the other without modifying either.

## Structure

```
┌──────────┐  calls   ┌────────────────┐  translates  ┌───────────┐
│  Client  │ ───────→ │ StripeAdapter  │ ───────────→ │ StripeAPI │
│          │  pay()   │ (Adapter)      │  create_     │ (Adaptee) │
│checkout()│          │  pay() →       │  charge()    │           │
└──────────┘          └────────────────┘              └───────────┘
```

## When to Use
- Incompatible interface from a third-party library
- Can't modify the existing class
- Want a reusable bridge between interfaces

## Key Takeaways
1. Third-party APIs are NOT modified
2. Each adapter translates between interfaces
3. Client works uniformly with any adapted service
4. Handles all conversion logic (units, formats, etc.)

## Files
- `bad_example.py` — incompatible interfaces
- `adapter.py` — adapters bridge the gap
