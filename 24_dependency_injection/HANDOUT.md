# Lesson 24: Dependency Injection (Bonus)

## Category
Architectural / Creational

## Intent
Instead of a class creating its own dependencies, they are provided
("injected") from outside.

## Real-World Analogy
A chef doesn't grow vegetables. Ingredients are delivered. The chef
works with any supplier — they just need ingredients that meet the spec.

## Three Types

```python
# 1. Constructor injection (recommended)
class Service:
    def __init__(self, sender: MessageSender):
        self._sender = sender

# 2. Method injection (per-call)
class Service:
    def send(self, sender: MessageSender, msg: str):
        sender.send(msg)

# 3. Property injection (optional deps)
service = Service()
service.logger = ConsoleLogger()
```

## Structure

```
┌────────────┐  injects  ┌─────────────────────┐
│   main()   │ ────────→ │NotificationService  │
│ (composer) │           │  sender: injected   │
│            │           │  logger: injected   │
└────────────┘           └─────────────────────┘
                              uses ↓
                         ┌──────────────┐
                         │MessageSender │ (interface)
                         └──────────────┘
                           ▲    ▲    ▲
                         Email SMS  Slack
```

## When to Use
- Want loosely coupled, testable code
- Need to swap implementations easily
- Want configurable behavior

## Key Takeaways
1. Dependencies injected, not created internally
2. Same service works with any implementation
3. Testing: inject mocks or nulls
4. Configuration at the "composition root"
5. Arguably THE most important pattern for maintainability

## Files
- `bad_example.py` — hardcoded internal dependency
- `dependency_injection.py` — injected dependencies + DI container
