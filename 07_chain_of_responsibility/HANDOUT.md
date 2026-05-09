# Lesson 7: Chain of Responsibility Pattern

## Category
Behavioral

## Intent
Pass a request along a chain of handlers. Each handler decides either
to process the request or pass it to the next handler.

## Real-World Analogy
A call center. You call tech support → they can't help → transferred to
specialist → still unresolved → escalated to manager. Each person either
handles it or passes it along.

## Structure

```
  Request
    │
    ▼
┌─────────┐  next  ┌─────────┐  next  ┌──────────┐  next  ┌─────┐
│  Basic  │ ─────→ │ Manager │ ─────→ │ Director │ ─────→ │ CEO │
│ Support │        │ Support │        │ Support  │        │     │
└─────────┘        └─────────┘        └──────────┘        └─────┘
```

## When to Use
- Multiple objects may handle a request
- The handler isn't known in advance
- You want to dynamically configure the chain

## Key Takeaways
1. Each handler only knows its own responsibility
2. The chain is configurable and extensible
3. Sender doesn't know who will handle its request
4. Follows Single Responsibility Principle

## Files
- `bad_example.py` — nested if/elif for all levels
- `chain_of_responsibility.py` — linked chain of handler objects
