# Lesson 20: Proxy Pattern

## Category
Structural

## Intent
Provide a surrogate or placeholder to control access to another object.

## Real-World Analogy
A credit card is a proxy for your bank account. Same "pay" interface,
but adds security checks, spending limits, and logging.

## Types of Proxies

| Type | Purpose | Example |
|---|---|---|
| Virtual | Lazy initialization | Load DB only when first queried |
| Protection | Access control | Check user role before allowing |
| Caching | Avoid repeated work | Store query results |
| Logging | Track interactions | Log every access |

## Structure

```
┌────────┐  same interface  ┌───────────┐  delegates  ┌──────────────┐
│ Client │ ───────────────→ │   Proxy   │ ──────────→ │ RealDatabase │
│        │  query()         │  query()  │             │   query()    │
└────────┘                  │ + control │             └──────────────┘
                            └───────────┘
```

## Proxy vs Decorator
- **Decorator:** adds new behavior dynamically
- **Proxy:** controls access to existing behavior
- Both wrap an object with the same interface

## Key Takeaways
1. Same interface as the real object
2. Multiple proxy types for different purposes
3. Proxies can be stacked
4. Client doesn't know it's using a proxy

## Files
- `bad_example.py` — eager loading, no control
- `proxy.py` — lazy, cached, and protected proxies
