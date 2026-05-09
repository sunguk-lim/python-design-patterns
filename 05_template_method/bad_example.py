"""
=============================================================
 BAD EXAMPLE: Without the Template Method Pattern
=============================================================

Data processing pipelines for CSV and JSON files.
Both follow the same steps: read → process → analyze → report.

Problems:
    1. Duplicated structure — both classes repeat the same workflow
    2. If you change the workflow order, you must edit EVERY class
    3. Easy to forget a step or get the order wrong
    4. Common steps (like reporting) are duplicated
=============================================================
"""


class BadCSVProcessor:
    def run(self):
        # Step 1: Read
        print("  Reading CSV file...")
        data = [{"name": "Alice", "score": 90}, {"name": "Bob", "score": 75}]

        # Step 2: Process
        print("  Parsing CSV rows...")
        processed = [row["score"] for row in data]

        # Step 3: Analyze
        avg = sum(processed) / len(processed)
        print(f"  Average score: {avg}")

        # Step 4: Report
        print(f"  Report: Processed {len(data)} records. Average: {avg}")


class BadJSONProcessor:
    def run(self):
        # Step 1: Read (same structure, different detail)
        print("  Reading JSON file...")
        data = [{"name": "Charlie", "score": 85}, {"name": "Diana", "score": 95}]

        # Step 2: Process
        print("  Parsing JSON objects...")
        processed = [item["score"] for item in data]

        # Step 3: Analyze
        avg = sum(processed) / len(processed)
        print(f"  Average score: {avg}")

        # Step 4: Report (exact duplicate!)
        print(f"  Report: Processed {len(data)} records. Average: {avg}")


if __name__ == "__main__":
    print("=== CSV Processing ===")
    BadCSVProcessor().run()
    print("\n=== JSON Processing ===")
    BadJSONProcessor().run()

    print()
    print("The workflow is identical. Only the 'read' and 'process'")
    print("steps differ. The rest is duplicated code.")
    print("→ The Template Method pattern fixes this.")
