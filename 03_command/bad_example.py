"""
=============================================================
 BAD EXAMPLE: Without the Command Pattern
=============================================================

A simple text editor where actions are directly executed.

Problems:
    1. No way to undo/redo — actions are fire-and-forget
    2. No history of what was done
    3. Can't queue, schedule, or replay actions
    4. Adding undo means polluting the Editor with undo logic
       for every possible action
=============================================================
"""


class BadTextEditor:
    def __init__(self):
        self.text = ""

    def type_text(self, text: str):
        self.text += text
        print(f"  Typed: '{text}' → \"{self.text}\"")

    def delete_last(self, count: int):
        deleted = self.text[-count:]
        self.text = self.text[:-count]
        print(f"  Deleted: '{deleted}' → \"{self.text}\"")

    # Want undo? You'd have to track state for EACH method.
    # What about redo? What about macros?
    # This class would explode in complexity.


if __name__ == "__main__":
    editor = BadTextEditor()
    editor.type_text("Hello")
    editor.type_text(" World")
    editor.delete_last(5)

    print(f"\nFinal text: \"{editor.text}\"")
    print()
    print("Now try to undo the delete... you can't!")
    print("There's no history, no way to reverse actions.")
    print("→ The Command pattern fixes this.")
