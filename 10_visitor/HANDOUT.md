# Lesson 10: Visitor Pattern

## Category
Behavioral

## Intent
Add new operations to existing object structures without modifying
those objects. Separate algorithms from the objects they operate on.

## Real-World Analogy
A tax inspector visiting businesses. The inspector applies different
tax rules to each business type, but businesses don't need to know
about tax rules — they just "accept" the inspection.

## Structure

```
┌────────────────┐  accepts   ┌───────────────────┐
│DocumentElement │ ─────────→ │ DocumentVisitor   │
│  accept()      │            │  visit_text()     │
└────────────────┘            │  visit_image()    │
    ▲    ▲    ▲               │  visit_table()    │
    │    │    │               └───────────────────┘
 ┌──┘    │    └──┐               ▲       ▲
 │       │       │               │       │
Text   Image   Table    HtmlVisitor  MarkdownVisitor
```

## The Double Dispatch Trick
1. Client calls `element.accept(visitor)`
2. Element calls `visitor.visit_text(self)` (or visit_image, etc.)
3. The correct method is called based on BOTH the element type AND visitor type

## Trade-off
- Easy to add new **operations** (new Visitor class)
- Hard to add new **element types** (must update all Visitors)
- Best when: elements are stable, operations change frequently

## When to Use
- You need to add operations without modifying classes
- You have a stable class hierarchy
- Related operations should be grouped together

## Key Takeaways
1. Element classes are NOT modified when adding operations
2. Each visitor groups related logic for all element types
3. Uses "double dispatch" to pick the right method
4. Trade-off: new elements require updating all visitors

## Files
- `bad_example.py` — operations scattered across element classes
- `visitor.py` — operations grouped in visitor classes
