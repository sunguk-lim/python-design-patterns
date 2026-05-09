# Lesson 25: Event Sourcing (Bonus)

## Category
Architectural

## Intent
Store a sequence of events instead of just current state.
Current state is derived by replaying events.

## Real-World Analogy
An accountant's ledger. Every transaction is recorded. The balance
is calculated from the ledger. Any dispute can be traced.

## Structure

```
  Commands           Events (append-only)         State
  ─────────         ──────────────────          ──────
  deposit(1000) →   [MoneyDeposited: 1000]  →   balance: 1000
  deposit(500)  →   [MoneyDeposited: 500]   →   balance: 1500
  withdraw(200) →   [MoneyWithdrawn: 200]   →   balance: 1300

  State = replay(all events)
  State at time T = replay(events up to T)
```

## Event Sourcing vs Traditional CRUD

| | CRUD | Event Sourcing |
|---|---|---|
| **Stores** | Current state only | All events |
| **History** | Lost on update | Complete audit trail |
| **Undo** | Difficult | Replay without that event |
| **Debugging** | "How did we get here?" | Replay and see |
| **Storage** | Less data | More data (append-only) |

## When to Use
- Need complete audit trail (banking, medical, legal)
- Want time-travel debugging
- Domain is naturally event-based
- Need to reconstruct state at any point

## Key Takeaways
1. Events are the source of truth
2. State is derived by replaying events
3. Complete audit trail
4. Time travel — state at any point in history
5. Events are immutable, append-only

## Files
- `bad_example.py` — only current balance, no history
- `event_sourcing.py` — full event log with replay and time travel
