# Lesson 11: Factory Method Pattern

## Category
Creational

## Intent
Define an interface for creating an object, but let subclasses
decide which class to instantiate.

## Real-World Analogy
A hiring agency. You say "I need a developer" and the agency decides
which specific developer to send. Different agencies specialize in
different types.

## Structure

```
┌──────────────────┐         ┌───────────────┐
│    Logistics     │ creates │   Transport   │
│    (Creator)     │ ──────→ │   (Product)   │
│                  │         │   deliver()   │
│ create_transport()│         └───────────────┘
│ plan_delivery()  │            ▲    ▲    ▲
└──────────────────┘            │    │    │
     ▲    ▲    ▲          Truck  Ship  Drone
     │    │    │
  Road  Sea  Air
  Log.  Log. Log.
```

## When to Use
- You don't know in advance which class to instantiate
- You want subclasses to control object creation
- You want to decouple creation from usage

## Key Takeaways
1. Client works with interfaces, not concrete classes
2. Each creator subclass decides which product to create
3. Adding new types = new classes, no changes to existing code
4. The factory method is just one method — `create_transport()`
5. Follows Open/Closed Principle

## Files
- `bad_example.py` — if/elif factory function
- `factory_method.py` — subclass-driven creation
