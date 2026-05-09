# Design Patterns in Python — Syllabus

A hands-on course covering the classic Gang of Four (GoF) design patterns,
taught in an order that builds understanding progressively.

Each lesson includes:
- A real-world analogy
- A "bad example" showing the problem
- A clean solution using the pattern
- A HANDOUT.md with diagrams and key takeaways

---

## Part 1: Behavioral Patterns (How objects communicate)

| #  | Pattern                  | Folder              | Status |
|----|--------------------------|---------------------|--------|
| 01 | Strategy                 | `01_strategy/`      | ✅ Done |
| 02 | Observer                 | `02_observer/`      | ✅ Done |
| 03 | Command                  | `03_command/`       | ✅ Done |
| 04 | State                    | `04_state/`         | ✅ Done |
| 05 | Template Method          | `05_template_method/`| ✅ Done |
| 06 | Iterator                 | `06_iterator/`      | ✅ Done |
| 07 | Chain of Responsibility  | `07_chain_of_responsibility/` | ✅ Done |
| 08 | Mediator                 | `08_mediator/`      | ✅ Done |
| 09 | Memento                  | `09_memento/`       | ✅ Done |
| 10 | Visitor                  | `10_visitor/`       | ✅ Done |

## Part 2: Creational Patterns (How objects are created)

| #  | Pattern                  | Folder              | Status |
|----|--------------------------|---------------------|--------|
| 11 | Factory Method           | `11_factory_method/`| ✅ Done |
| 12 | Abstract Factory         | `12_abstract_factory/`| ✅ Done |
| 13 | Builder                  | `13_builder/`       | ✅ Done |
| 14 | Singleton                | `14_singleton/`     | ✅ Done |
| 15 | Prototype                | `15_prototype/`     | ✅ Done |

## Part 3: Structural Patterns (How objects are composed)

| #  | Pattern                  | Folder              | Status |
|----|--------------------------|---------------------|--------|
| 16 | Decorator                | `16_decorator/`     | ✅ Done |
| 17 | Adapter                  | `17_adapter/`       | ✅ Done |
| 18 | Facade                   | `18_facade/`        | ✅ Done |
| 19 | Composite                | `19_composite/`     | ✅ Done |
| 20 | Proxy                    | `20_proxy/`         | ✅ Done |
| 21 | Bridge                   | `21_bridge/`        | ✅ Done |
| 22 | Flyweight                | `22_flyweight/`     | ✅ Done |

## Bonus: Patterns Beyond GoF

| #  | Pattern                  | Folder              | Status |
|----|--------------------------|---------------------|--------|
| 23 | Repository               | `23_repository/`    | ✅ Done |
| 24 | Dependency Injection     | `24_dependency_injection/` | ✅ Done |
| 25 | Event Sourcing           | `25_event_sourcing/`| ✅ Done |

---

## How to use this repo

```bash
# Run any lesson
python 01_strategy/strategy.py

# See the "bad" version first, then the clean version
python 01_strategy/bad_example.py
python 01_strategy/strategy.py

# Each folder contains:
#   bad_example.py  — the problem (why the pattern matters)
#   <pattern>.py    — the clean solution
#   HANDOUT.md      — summary, diagrams, and key takeaways
```
