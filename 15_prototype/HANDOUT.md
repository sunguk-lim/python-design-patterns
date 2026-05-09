# Lesson 15: Prototype Pattern

## Category
Creational

## Intent
Create new objects by cloning existing ones, avoiding expensive creation.

## Real-World Analogy
Cell division. Instead of building from raw materials, a cell copies
itself and the copy can be modified.

## Structure

```
┌───────────────┐  clone()  ┌──────────────┐
│   Prototype   │ ────────→ │    Clone     │
│   (Goblin)    │           │  (new Goblin)│
│ hp=50, atk=10 │           │ hp=50, atk=10│
└───────────────┘           └──────────────┘

┌─────────────────┐
│  EnemyRegistry  │  register("goblin", prototype)
│                 │  create("goblin", hp=80)  → clone + override
└─────────────────┘
```

## When to Use
- Object creation is expensive
- Many similar objects with small variations needed
- Avoid subclassing just for different defaults

## Key Takeaways
1. Clone instead of create from scratch
2. Deep copy ensures independence
3. Registry catalogs reusable prototypes
4. Overrides allow easy variations
5. Python's `copy.deepcopy()` does the heavy lifting

## Files
- `bad_example.py` — repeating all parameters for each object
- `prototype.py` — clone from prototypes with overrides
