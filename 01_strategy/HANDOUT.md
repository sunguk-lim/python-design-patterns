# Lesson 1: Strategy Pattern

## Category
Behavioral

## Intent
Define a family of algorithms, encapsulate each one, and make them interchangeable at runtime.

## Real-World Analogy
Think of paying at a store. You can pay by cash, credit card, or mobile payment.
The store doesn't care HOW you pay — it just asks you to "pay".
Each payment method is a "strategy".

## The Problem
Imagine you're building a navigation app. Users can travel by car, bicycle, or walking.
Each mode calculates the route differently. How do you handle this without a mess of
`if/elif` statements?

## Structure

```
┌─────────────┐       uses        ┌──────────────────┐
│  Navigator   │ ───────────────→ │  RouteStrategy    │ (interface)
│  (Context)   │                  │  calculate_route()│
└─────────────┘                  └──────────────────┘
                                    ▲    ▲    ▲
                                    │    │    │
                              ┌─────┘    │    └─────┐
                              │          │          │
                        ┌─────────┐ ┌────────┐ ┌────────┐
                        │CarRoute │ │Bicycle │ │Walking │
                        │         │ │Route   │ │Route   │
                        └─────────┘ └────────┘ └────────┘
```

## The 3 Core Pieces
1. **Strategy** (interface) — defines what all algorithms must do
2. **Concrete Strategies** — each implements one algorithm
3. **Context** — holds a reference to a strategy and delegates work to it

## When to Use
- You have multiple ways to do the same thing
- You want to switch algorithms at runtime
- You want to avoid long if/elif/else chains

## Key Takeaways
1. The Context class doesn't contain any algorithm logic itself
2. Adding a new algorithm = just add a new class
3. No if/elif/else chains. No modification of existing code
4. Follows the **Open/Closed Principle**: open for extension, closed for modification

## Files
- `bad_example.py` — the "before" (why this pattern matters)
- `strategy.py` — the clean solution using the Strategy pattern
