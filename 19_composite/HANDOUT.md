# Lesson 19: Composite Pattern

## Category
Structural

## Intent
Compose objects into tree structures. Let clients treat individual
objects and compositions uniformly.

## Real-World Analogy
An army. "Attack" works the same for a soldier or an entire division —
the command cascades down the hierarchy.

## Structure

```
         FileSystemItem (interface)
            get_size()
            display()
           /          \
      File (leaf)    Folder (composite)
      get_size()     get_size() → sum of children
                     add() / remove()
                     children: [FileSystemItem...]
```

## When to Use
- Tree/hierarchy structures
- Treat leaves and branches the same
- Operations cascade down the tree

## Key Takeaways
1. Leaf and Composite share the same interface
2. No isinstance() checks needed
3. Operations cascade automatically
4. Perfect for: file systems, UI trees, org charts, menus

## Files
- `bad_example.py` — isinstance checks and manual recursion
- `composite.py` — uniform tree with automatic cascading
