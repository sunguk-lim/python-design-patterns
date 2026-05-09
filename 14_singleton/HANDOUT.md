# Lesson 14: Singleton Pattern

## Category
Creational

## Intent
Ensure a class has only one instance and provide a global access point.

## Real-World Analogy
A country has one president. Everyone asking "who is the president?"
gets the same answer.

## Three Ways in Python

```python
# 1. __new__ override
class DB:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# 2. Metaclass
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

# 3. Module-level instance (most Pythonic)
# config.py → settings = {"theme": "dark"}
# other.py  → from config import settings
```

## When to Use
- Exactly one instance needed (DB, config, logger)
- Global access point required
- Lazy initialization desired

## Caution
Singleton = global state. Overuse leads to tight coupling.
Prefer dependency injection when possible.

## Key Takeaways
1. Only one instance ever created
2. All callers get the same instance
3. Module-level instance is the most Pythonic way
4. Use sparingly — prefer dependency injection

## Files
- `bad_example.py` — multiple wasteful instances
- `singleton.py` — three Python approaches
