# Lesson 8: Mediator Pattern

## Category
Behavioral

## Intent
Define an object that encapsulates how a set of objects interact.
Promotes loose coupling by keeping objects from referring to each other explicitly.

## Real-World Analogy
An air traffic control tower. Planes don't communicate directly — they
all talk to the tower, which coordinates everything.

## Structure

```
         ┌───────────────┐
         │   ChatRoom    │
         │  (Mediator)   │
         │               │
         │ send_message() │
         └───────────────┘
          ▲    ▲    ▲
          │    │    │       All communication
          │    │    │       goes through
          │    │    │       the mediator
       ┌──┘    │    └──┐
       │       │       │
   ┌───────┐ ┌─────┐ ┌─────────┐
   │ Alice │ │ Bob │ │ Charlie │
   └───────┘ └─────┘ └─────────┘
       (Users only know the mediator)
```

## Mediator vs Observer

| | Observer | Mediator |
|---|---|---|
| **Direction** | One-way broadcast | Bidirectional coordination |
| **Awareness** | Observers don't know each other | Colleagues don't know each other |
| **Complexity** | Simple notification | Complex interaction logic |

## When to Use
- Many objects communicate in complex ways
- You want to centralize control logic
- Objects should not refer to each other directly

## Key Takeaways
1. Colleagues only know the mediator, not each other
2. N objects = N connections instead of N*(N-1)
3. Central place for logging, filtering, validation
4. Easy to add new participants

## Files
- `bad_example.py` — users directly connected to each other
- `mediator.py` — all communication through a chat room
