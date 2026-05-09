"""
=============================================================
 DESIGN PATTERN #5: TEMPLATE METHOD
=============================================================

Category: Behavioral
Intent:   Define the skeleton of an algorithm in a base class,
          letting subclasses override specific steps without
          changing the algorithm's structure.

Real-world analogy:
    Building a house. The blueprint (template) defines the order:
    foundation → walls → roof → interior. Every house follows
    this order, but a wooden house and a brick house differ in
    HOW they build walls.

When to use:
    - Multiple classes follow the same algorithm structure
    - Only some steps vary between classes
    - You want to enforce an order of operations

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: The abstract base class with the "template method"
# ---------------------------------------------------------
# run() is the template method — it defines the skeleton.
# Subclasses CANNOT change the order, only the individual steps.

class DataProcessor(ABC):

    def run(self):
        """The template method — defines the algorithm skeleton."""
        data = self.read_data()
        processed = self.process_data(data)
        result = self.analyze(processed)
        self.report(data, result)

    # Abstract steps — subclasses MUST implement these
    @abstractmethod
    def read_data(self) -> list[dict]:
        pass

    @abstractmethod
    def process_data(self, data: list[dict]) -> list:
        pass

    # Concrete steps — shared by all subclasses (no duplication!)
    def analyze(self, values: list) -> float:
        avg = sum(values) / len(values)
        print(f"  📊 Average: {avg}")
        return avg

    def report(self, data: list, result: float) -> None:
        print(f"  📋 Report: Processed {len(data)} records. Average: {result}")


# ---------------------------------------------------------
# STEP 2: Concrete implementations — only override what differs
# ---------------------------------------------------------

class CSVProcessor(DataProcessor):
    def read_data(self) -> list[dict]:
        print("  📂 Reading CSV file...")
        return [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 75}]

    def process_data(self, data: list[dict]) -> list:
        print("  🔄 Parsing CSV rows...")
        return [row["score"] for row in data]


class JSONProcessor(DataProcessor):
    def read_data(self) -> list[dict]:
        print("  📂 Reading JSON file...")
        return [{"name": "Charlie", "score": 85}, {"name": "Diana", "score": 95}]

    def process_data(self, data: list[dict]) -> list:
        print("  🔄 Parsing JSON objects...")
        return [item["score"] for item in data]


class XMLProcessor(DataProcessor):
    """Adding a new format is trivial — just implement the varying steps."""
    def read_data(self) -> list[dict]:
        print("  📂 Reading XML file...")
        return [{"name": "Eve", "score": 88}, {"name": "Frank", "score": 92}]

    def process_data(self, data: list[dict]) -> list:
        print("  🔄 Parsing XML elements...")
        return [item["score"] for item in data]


# ---------------------------------------------------------
# STEP 3: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    for name, processor in [("CSV", CSVProcessor()),
                            ("JSON", JSONProcessor()),
                            ("XML", XMLProcessor())]:
        print(f"=== {name} Processing ===")
        processor.run()
        print()

    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. The algorithm structure (read→process→analyze→report)")
    print("   is defined ONCE in the base class.")
    print("2. Subclasses only override the steps that vary.")
    print("3. Common logic (analyze, report) is NOT duplicated.")
    print("4. The order of steps is enforced — can't accidentally skip one.")
    print("5. Hollywood Principle: 'Don't call us, we'll call you.'")
    print("   The base class calls the subclass, not the other way around.")
