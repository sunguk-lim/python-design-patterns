# Lesson 3: Command Pattern

## Category
Behavioral

## Intent
Encapsulate a request as an object, thereby allowing you to parameterize,
queue, log, and undo/redo operations.

## Real-World Analogy
A restaurant order. You don't cook the food yourself — you write an order
(command object), hand it to the waiter (invoker), who passes it to the
chef (receiver). The order can be queued, cancelled, or logged.

## The Problem
You're building a text editor. Users can type, undo, redo, and record macros.
If actions are just direct method calls, there's no history, no way to reverse
them, and no way to replay them.

## Key Terms
- **Command:** the action object (what to do + how to undo)
- **Receiver:** the object that actually performs the work (e.g., TextEditor)
- **Invoker:** the object that triggers commands and keeps history (e.g., CommandManager)

## Structure

```
┌────────────────┐  executes   ┌───────────────┐  acts on   ┌────────────┐
│ CommandManager │ ──────────→ │   Command     │ ─────────→ │ TextEditor │
│   (Invoker)    │             │  execute()    │            │ (Receiver) │
│                │             │  undo()       │            │            │
│ history: []    │             └───────────────┘            └────────────┘
│ redo_stack: [] │                ▲         ▲
└────────────────┘                │         │
                           ┌──────┘         └──────┐
                           │                       │
                     ┌───────────┐          ┌────────────┐
                     │TypeCommand│          │DeleteCommand│
                     └───────────┘          └────────────┘
```

## When to Use
- You need undo/redo functionality
- You want to queue or schedule operations
- You want to log a history of actions
- You want to support macros (replay a sequence of commands)

## Key Takeaways
1. Each action is an object that knows how to do AND undo
2. The CommandManager keeps a history stack for undo/redo
3. New actions (e.g., BoldCommand) = just add a new class
4. The Receiver stays simple — no undo logic in it
5. Commands can be queued, logged, serialized, or replayed

## Comparison So Far

| Pattern | Relationship | Core Idea |
|---|---|---|
| Strategy | 1-to-1 | Swap one algorithm |
| Observer | 1-to-many | Notify many listeners |
| Command | 1-to-1 (with history) | Turn actions into objects |

## Files
- `bad_example.py` — direct method calls, no undo possible
- `command.py` — actions as objects with full undo/redo
