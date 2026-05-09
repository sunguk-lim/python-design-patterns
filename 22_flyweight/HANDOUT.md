# Lesson 22: Flyweight Pattern

## Category
Structural

## Intent
Use sharing to support large numbers of objects efficiently by separating
shared (intrinsic) from unique (extrinsic) state.

## Real-World Analogy
A forest in a game. Millions of trees, but only 5-10 tree types.
Each tree shares its type's mesh/texture but has its own position.

## Key Terms
- **Intrinsic state:** shared, immutable (font, color, texture)
- **Extrinsic state:** unique per instance (position, size)

## Structure

```
┌───────────────┐  get_style()  ┌─────────────────┐
│ StyleFactory  │ ────────────→ │ CharacterStyle  │  (flyweight)
│               │               │  font, size,    │  ← shared!
│ _styles: {}   │               │  color          │
└───────────────┘               └─────────────────┘
                                       ▲
                                       │ reference
┌───────────────┐                      │
│  Character    │──────────────────────┘
│  char, x, y  │  ← unique per instance
└───────────────┘
```

## When to Use
- Huge number of similar objects
- Objects share most of their state
- Memory is a concern

## Key Takeaways
1. Shared state stored once in flyweights
2. Unique state stored in each context object
3. Factory ensures reuse, not duplication
4. Huge memory savings
5. Trade-off: complexity for memory efficiency

## Files
- `bad_example.py` — every object stores duplicate data
- `flyweight.py` — shared styles via factory
