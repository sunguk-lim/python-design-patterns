# Lesson 18: Facade Pattern

## Category
Structural

## Intent
Provide a simplified interface to a complex subsystem.

## Real-World Analogy
A hotel concierge. Tell them "plan my evening" and they handle
restaurant, taxi, and theater bookings behind the scenes.

## Structure

```
┌────────────┐  simple call  ┌─────────────────────────────┐
│   Client   │ ────────────→ │   HomeTheaterFacade         │
│            │ watch_movie() │                             │
└────────────┘               │  TV + Amp + Player + Lights │
                             └─────────────────────────────┘
                                  │    │    │    │
                              manages all subsystems
```

## Facade vs Adapter

| | Adapter | Facade |
|---|---|---|
| **Purpose** | Make incompatible interface compatible | Simplify a complex interface |
| **Scope** | Wraps ONE class | Wraps MANY classes |
| **Changes interface?** | Yes (translates) | Yes (simplifies) |

## Key Takeaways
1. One method replaces many complex steps
2. Subsystem unchanged and still directly accessible
3. Facade simplifies, doesn't add new functionality
4. Multiple facades can coexist

## Files
- `bad_example.py` — client orchestrates 7+ steps manually
- `facade.py` — one-method convenience interface
