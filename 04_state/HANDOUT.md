# Lesson 4: State Pattern

## Category
Behavioral

## Intent
Allow an object to alter its behavior when its internal state changes.
The object will appear to change its class.

## Real-World Analogy
A traffic light. When it's green, cars go. When it's red, cars stop.
The light doesn't use if/elif — it simply switches between state objects.

## The Problem
A vending machine has multiple states: idle, has_money, dispensing.
Every method needs if/elif checks for the current state. Adding a new
state means modifying every method.

## Structure

```
┌────────────────┐  delegates to  ┌──────────────────┐
│ VendingMachine │ ─────────────→ │  VendingState     │ (interface)
│   (Context)    │                │  insert_money()   │
│                │                │  select_product() │
│ state ─────────┤                │  cancel()         │
└────────────────┘                └──────────────────┘
                                     ▲    ▲    ▲
                                     │    │    │
                              ┌──────┘    │    └───────┐
                              │           │            │
                        ┌──────────┐ ┌──────────┐ ┌───────────┐
                        │  Idle    │ │ HasMoney │ │Dispensing │
                        │  State   │ │  State   │ │  State    │
                        └──────────┘ └──────────┘ └───────────┘
```

## State vs Strategy

| | Strategy | State |
|---|---|---|
| **Who switches?** | The client sets the strategy | The state switches itself |
| **Awareness** | Strategies don't know about each other | States know about transitions |
| **Purpose** | Choose one algorithm | Model a state machine |

## When to Use
- An object behaves differently depending on its state
- You have many if/elif checks on a state variable
- State transitions are complex and error-prone

## Key Takeaways
1. No if/elif chains — each state is its own class
2. Adding a new state = just add a new class
3. State transitions are explicit and easy to trace
4. Each state class is small, focused, and testable
5. Very similar to Strategy, but the state decides when to transition

## Files
- `bad_example.py` — if/elif state checks in every method
- `state.py` — each state encapsulated in its own class
