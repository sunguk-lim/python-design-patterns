# Lesson 6: Iterator Pattern

## Category
Behavioral

## Intent
Provide a way to access elements of a collection sequentially
without exposing its underlying structure.

## Real-World Analogy
A TV remote with "next channel" and "previous channel" buttons.
You don't need to know how channels are stored internally.

## The Problem
A playlist stores songs. To iterate, the client must know the internal
data structure (list, index-based). If the structure changes, the client breaks.

## Structure

```
┌────────────┐  creates   ┌──────────────────┐
│  Playlist  │ ─────────→ │    Iterator       │ (interface)
│ (Collection)│            │  has_next()       │
│            │            │  next()           │
└────────────┘            └──────────────────┘
                              ▲          ▲
                              │          │
                     ┌────────────┐ ┌────────────┐
                     │  Forward   │ │  Reverse   │
                     │  Iterator  │ │  Iterator  │
                     └────────────┘ └────────────┘
```

## Python's Built-in Support
- `__iter__()` + `__next__()` → makes objects work with `for` loops
- `yield` (generators) → the most Pythonic way to create iterators

## When to Use
- You want to hide the internal structure of a collection
- You need multiple traversal strategies
- You want a uniform interface for different collection types

## Key Takeaways
1. Clients don't need to know the internal data structure
2. Multiple traversal strategies are easy to add
3. Python's `__iter__`/`__next__` IS the Iterator pattern
4. Generators (`yield`) are the most Pythonic iterators
5. Separates "how to traverse" from "what to store"

## Files
- `bad_example.py` — client coupled to internal list structure
- `iterator.py` — classic pattern + Pythonic approach
