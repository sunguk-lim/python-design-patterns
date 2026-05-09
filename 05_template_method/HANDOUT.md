# Lesson 5: Template Method Pattern

## Category
Behavioral

## Intent
Define the skeleton of an algorithm in a base class, letting subclasses
override specific steps without changing the algorithm's structure.

## Real-World Analogy
Building a house. The blueprint defines the order: foundation → walls →
roof → interior. Every house follows this order, but a wooden house and
a brick house differ in HOW they build the walls.

## The Problem
You have data processors for CSV, JSON, XML. They all follow the same
workflow: read → process → analyze → report. But each duplicates the
workflow structure and shared logic (analyze, report).

## Structure

```
┌──────────────────────────────┐
│     DataProcessor (ABC)      │
│                              │
│  run()  ← template method    │
│    1. read_data()   abstract │
│    2. process_data() abstract│
│    3. analyze()     concrete │
│    4. report()      concrete │
└──────────────────────────────┘
          ▲         ▲
          │         │
   ┌────────────┐ ┌─────────────┐
   │CSVProcessor│ │JSONProcessor│
   │ read_data()│ │ read_data() │
   │ process()  │ │ process()   │
   └────────────┘ └─────────────┘
```

## When to Use
- Multiple classes follow the same algorithm structure
- Only some steps vary between classes
- You want to enforce an order of operations

## Key Takeaways
1. The algorithm skeleton is defined ONCE in the base class
2. Subclasses only override the steps that vary
3. Common logic is NOT duplicated
4. The order of steps is enforced
5. Hollywood Principle: "Don't call us, we'll call you"

## Files
- `bad_example.py` — duplicated workflow structure
- `template_method.py` — shared skeleton with varying steps
