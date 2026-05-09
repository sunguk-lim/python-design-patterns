"""
=============================================================
 DESIGN PATTERN #3: COMMAND
=============================================================

Category: Behavioral
Intent:   Encapsulate a request as an object, thereby allowing you
          to parameterize, queue, log, and undo/redo operations.

Real-world analogy:
    A restaurant order. You don't cook the food yourself — you
    write an order (command object), hand it to the waiter (invoker),
    who passes it to the chef (receiver). The order can be queued,
    cancelled, or logged.

Key terms:
    - Command:   the action object (what to do + how to undo)
    - Receiver:  the object that actually performs the work
    - Invoker:   the object that triggers commands (and keeps history)

When to use:
    - You need undo/redo functionality
    - You want to queue or schedule operations
    - You want to log a history of actions
    - You want to support macros (replay a sequence of commands)

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: The Receiver — does the actual work
# ---------------------------------------------------------
# This is just a plain object. It doesn't know about commands.

class TextEditor:
    def __init__(self):
        self.text = ""

    def insert(self, text: str, position: int) -> None:
        self.text = self.text[:position] + text + self.text[position:]

    def delete(self, position: int, count: int) -> str:
        deleted = self.text[position:position + count]
        self.text = self.text[:position] + self.text[position + count:]
        return deleted


# ---------------------------------------------------------
# STEP 2: The Command interface
# ---------------------------------------------------------
# Every command must know how to execute AND how to undo.

class Command(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


# ---------------------------------------------------------
# STEP 3: Concrete Commands
# ---------------------------------------------------------
# Each command stores everything it needs to execute AND undo.

class TypeCommand(Command):
    def __init__(self, editor: TextEditor, text: str):
        self.editor = editor
        self.text = text
        self.position = len(editor.text)  # insert at end

    def execute(self) -> None:
        self.editor.insert(self.text, self.position)
        print(f"  ✏️  Typed '{self.text}' → \"{self.editor.text}\"")

    def undo(self) -> None:
        self.editor.delete(self.position, len(self.text))
        print(f"  ↩️  Undo type '{self.text}' → \"{self.editor.text}\"")


class DeleteCommand(Command):
    def __init__(self, editor: TextEditor, count: int):
        self.editor = editor
        self.count = count
        self.position = len(editor.text) - count
        self.deleted_text = ""  # saved during execute for undo

    def execute(self) -> None:
        self.deleted_text = self.editor.delete(self.position, self.count)
        print(f"  🗑️  Deleted '{self.deleted_text}' → \"{self.editor.text}\"")

    def undo(self) -> None:
        self.editor.insert(self.deleted_text, self.position)
        print(f"  ↩️  Undo delete '{self.deleted_text}' → \"{self.editor.text}\"")


# ---------------------------------------------------------
# STEP 4: The Invoker — manages command history
# ---------------------------------------------------------
# This is the "brain" that executes, undoes, and redoes.

class CommandManager:
    def __init__(self):
        self.history: list[Command] = []
        self.redo_stack: list[Command] = []

    def execute(self, command: Command) -> None:
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()  # new action clears redo history

    def undo(self) -> None:
        if not self.history:
            print("  ⚠️  Nothing to undo!")
            return
        command = self.history.pop()
        command.undo()
        self.redo_stack.append(command)

    def redo(self) -> None:
        if not self.redo_stack:
            print("  ⚠️  Nothing to redo!")
            return
        command = self.redo_stack.pop()
        command.execute()
        self.history.append(command)


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    editor = TextEditor()
    manager = CommandManager()

    print("=== Typing ===")
    manager.execute(TypeCommand(editor, "Hello"))
    manager.execute(TypeCommand(editor, " Beautiful"))
    manager.execute(TypeCommand(editor, " World"))

    print("\n=== Undo (3 times) ===")
    manager.undo()  # undo " World"
    manager.undo()  # undo " Beautiful"
    manager.undo()  # undo "Hello"

    print("\n=== Redo (2 times) ===")
    manager.redo()  # redo "Hello"
    manager.redo()  # redo " Beautiful"

    print("\n=== Type more, then delete ===")
    manager.execute(TypeCommand(editor, " Day"))
    manager.execute(DeleteCommand(editor, 4))  # delete " Day"

    print("\n=== Undo delete ===")
    manager.undo()  # undo the delete → " Day" comes back

    print(f"\n📄 Final text: \"{editor.text}\"")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Each action is an object that knows how to do AND undo.")
    print("2. The CommandManager keeps a history stack for undo/redo.")
    print("3. New actions (e.g., BoldCommand) = just add a new class.")
    print("4. The Editor (receiver) stays simple — no undo logic.")
    print("5. Commands can be queued, logged, serialized, or replayed.")
