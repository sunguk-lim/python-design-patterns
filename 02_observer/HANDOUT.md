# Lesson 2: Observer Pattern

## Category
Behavioral

## Intent
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updated automatically.

## Real-World Analogy
YouTube subscriptions. You subscribe to a channel, and you get notified
when new content is uploaded. You don't have to keep checking.
You can also unsubscribe anytime.

## The Problem
Imagine you run an online store. When a product comes back in stock, you
need to notify customers who are waiting for it. You could check every
customer manually... or you could let them **subscribe** and get notified
automatically.

## Key Terms
- **Subject (Publisher):** the object being watched (e.g., Store)
- **Observer (Subscriber):** the object that reacts to changes (e.g., EmailSubscriber)

## Structure

```
                         subscribes
  EmailSubscriber  ──────────────┐
  SMSSubscriber    ──────────────┤
  SlackSubscriber  ──────────────┤
                                 ▼
                          ┌────────────┐
                          │   Store     │
                          │ (Subject)   │
                          │             │
                          │ restock()   │──→ notify_all()
                          │             │       │
                          └────────────┘       │
                                               ▼
                                    calls update() on
                                    every subscriber
```

## When to Use
- When changes in one object should trigger updates in others
- When you don't know in advance how many objects need updating
- When you want loose coupling between the sender and receivers

## Key Takeaways
1. The Subject doesn't know about email, SMS, or Slack specifics
2. Adding a new notification channel = just create a new Observer class
3. Subscribers can join and leave at runtime
4. Subject and Observers are loosely coupled
5. This is the foundation of event-driven programming

## Strategy vs Observer — Comparison

| | Strategy | Observer |
|---|---|---|
| **Relationship** | 1-to-1 (context → strategy) | 1-to-many (subject → observers) |
| **Purpose** | Swap **one** algorithm | Notify **many** listeners |
| **Direction** | Context calls strategy | Subject broadcasts to observers |

## Files
- `bad_example.py` — the "before" (why this pattern matters)
- `observer.py` — the clean solution using the Observer pattern
