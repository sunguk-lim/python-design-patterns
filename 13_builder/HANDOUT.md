# Lesson 13: Builder Pattern

## Category
Creational

## Intent
Separate the construction of a complex object from its representation,
allowing the same process to create different representations.

## Real-World Analogy
Ordering a custom pizza. You don't get a constructor with 20 parameters.
Instead: dough → sauce → cheese → toppings, step by step.

## Structure

```
┌──────────────┐  uses    ┌──────────────┐  builds  ┌─────────┐
│   Director   │ ───────→ │ HouseBuilder │ ───────→ │  House  │
│ (optional)   │          │              │          │(Product)│
│ luxury()     │          │ floors()     │          └─────────┘
│ starter()    │          │ rooms()      │
└──────────────┘          │ with_pool()  │
                          │ build()      │
                          └──────────────┘
```

## When to Use
- Object has many optional parameters
- Construction involves multiple steps
- You want readable creation code
- You want predefined configurations (Director)

## Key Takeaways
1. No telescoping constructor
2. Method chaining is readable and self-documenting
3. Optional features are explicit named methods
4. Director provides predefined recipes
5. Same builder, different results

## Files
- `bad_example.py` — 10-parameter constructor
- `builder.py` — step-by-step fluent builder
