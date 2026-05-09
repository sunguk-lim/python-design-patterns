# Lesson 16: Decorator Pattern

## Category
Structural

## Intent
Attach additional responsibilities to an object dynamically.
A flexible alternative to subclassing.

## Real-World Analogy
Wearing clothes. You add a shirt, jacket, scarf — each layer adds
warmth without changing you. Add/remove layers freely.

## Structure

```
       Caramel( WhippedCream( Sugar( Milk( Coffee() ) ) ) )
          │          │          │       │       │
          └──wraps───┘──wraps───┘─wraps─┘─wraps─┘

  Each decorator IS a Beverage AND wraps a Beverage.
  cost() = own cost + wrapped.cost()
```

## The Math
- Without pattern: N toppings = 2^N classes
- With pattern: N toppings = N + base classes

## When to Use
- Add behavior dynamically at runtime
- Subclassing causes class explosion
- Mix and match behaviors freely

## Key Takeaways
1. Decorators wrap objects like layers of an onion
2. 4 toppings = 6 classes, not 32
3. Same decorator can be applied multiple times
4. Python's `@decorator` syntax is the same concept
5. Each decorator has the same interface as the wrapped object

## Files
- `bad_example.py` — class explosion with combinations
- `decorator.py` — layered wrapping with mix-and-match
