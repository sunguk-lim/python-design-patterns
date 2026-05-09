# Lesson 9: Memento Pattern

## Category
Behavioral

## Intent
Capture and externalize an object's internal state so it can be
restored later, without violating encapsulation.

## Real-World Analogy
A save point in a video game. Save before the boss fight, die,
load the save, try again. The save captures your exact state.

## Key Terms
- **Originator:** the object whose state is saved (GameCharacter)
- **Memento:** the snapshot (immutable state capsule)
- **Caretaker:** manages the history of mementos (SaveManager)

## Structure

```
┌──────────────┐  creates   ┌─────────────┐  stores   ┌─────────────┐
│GameCharacter │ ─────────→ │ GameMemento │ ←──────── │ SaveManager │
│ (Originator) │            │ (Snapshot)  │           │ (Caretaker) │
│              │ ←───────── │  level      │           │             │
│  save()      │  restores  │  hp         │           │ saves: []   │
│  restore()   │            │  position   │           │             │
└──────────────┘            └─────────────┘           └─────────────┘
```

## Command vs Memento

| | Command | Memento |
|---|---|---|
| **Stores** | Actions (do/undo) | State snapshots |
| **Undo approach** | Reverse the action | Restore full state |
| **Best for** | Action history | Checkpoint/rollback |

## When to Use
- You need save/restore (undo, checkpoints, snapshots)
- You want to preserve encapsulation
- You need a history of states

## Key Takeaways
1. Internal state captured without exposing it
2. Mementos are immutable
3. Caretaker manages saves without knowing details
4. Adding new fields doesn't break existing code

## Files
- `bad_example.py` — manual field copying, no encapsulation
- `memento.py` — proper snapshots with save/restore
