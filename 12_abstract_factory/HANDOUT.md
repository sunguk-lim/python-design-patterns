# Lesson 12: Abstract Factory Pattern

## Category
Creational

## Intent
Provide an interface for creating families of related objects without
specifying their concrete classes.

## Real-World Analogy
A furniture catalog: "Modern", "Victorian". Pick a catalog and every
piece (chair, sofa, table) is guaranteed to match.

## Structure

```
┌───────────────┐  creates  ┌────────┐ ┌──────────┐ ┌───────────┐
│  UIFactory    │ ────────→ │ Button │ │ Checkbox │ │ TextField │
└───────────────┘           └────────┘ └──────────┘ └───────────┘
    ▲        ▲
    │        │
┌────────┐ ┌────────┐
│Windows │ │  Mac   │   Each factory creates a
│Factory │ │Factory │   CONSISTENT family
└────────┘ └────────┘
```

## Factory Method vs Abstract Factory

| | Factory Method | Abstract Factory |
|---|---|---|
| **Creates** | One product | Family of products |
| **Mechanism** | Subclass overrides one method | Object with multiple create methods |
| **Consistency** | N/A | Guarantees matching family |

## Key Takeaways
1. Client doesn't know concrete classes
2. Each factory guarantees a consistent family
3. Can't mix products from different families
4. Swap entire theme by changing one factory

## Files
- `bad_example.py` — manual coordination, easy to mix families
- `abstract_factory.py` — factory guarantees consistency
