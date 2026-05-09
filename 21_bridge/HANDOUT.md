# Lesson 21: Bridge Pattern

## Category
Structural

## Intent
Decouple an abstraction from its implementation so both can vary independently.

## Real-World Analogy
A remote control and a TV. Change remotes or TVs independently —
they're connected by a "bridge" (infrared signal).

## Structure

```
  Abstraction (Shape)          Implementation (Renderer)
  ┌──────────────┐             ┌────────────────┐
  │    Shape     │──bridge───→│   Renderer     │
  │   draw()    │             │ render_circle() │
  └──────────────┘             └────────────────┘
     ▲       ▲                    ▲    ▲    ▲
     │       │                    │    │    │
  Circle  Rectangle         Vector Raster  SVG
```

## The Math
- Without Bridge: M shapes × N renderers = M×N classes
- With Bridge: M shapes + N renderers = M+N classes

## Bridge vs Adapter
- **Adapter:** makes existing incompatible interfaces work together
- **Bridge:** designed upfront to let two dimensions vary independently

## Key Takeaways
1. Two dimensions vary independently
2. M+N classes instead of M×N
3. The "bridge" is composition (not inheritance)
4. Can swap implementations at runtime

## Files
- `bad_example.py` — class explosion from combining dimensions
- `bridge.py` — two independent hierarchies connected by composition
