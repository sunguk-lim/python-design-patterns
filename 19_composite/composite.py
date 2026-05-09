"""
=============================================================
 DESIGN PATTERN #19: COMPOSITE
=============================================================

Category: Structural
Intent:   Compose objects into tree structures to represent
          part-whole hierarchies. Let clients treat individual
          objects and compositions uniformly.

Real-world analogy:
    An army. A general commands divisions, which contain brigades,
    which contain platoons, which contain soldiers. The order
    "attack" works the same whether given to a single soldier
    or an entire division — it cascades down the tree.

When to use:
    - You have a tree/hierarchy structure
    - You want to treat leaves and branches the same way
    - Operations should cascade down the tree

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Component interface — same for leaves and branches
# ---------------------------------------------------------

class FileSystemItem(ABC):
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def display(self, indent: int = 0) -> None:
        pass


# ---------------------------------------------------------
# STEP 2: Leaf — individual objects (files)
# ---------------------------------------------------------

class File(FileSystemItem):
    def __init__(self, name: str, size: int):
        super().__init__(name)
        self.size = size

    def get_size(self) -> int:
        return self.size

    def display(self, indent: int = 0) -> None:
        print(f"{'  ' * indent}📄 {self.name} ({self.size}B)")


# ---------------------------------------------------------
# STEP 3: Composite — contains other items (folders)
# ---------------------------------------------------------

class Folder(FileSystemItem):
    def __init__(self, name: str):
        super().__init__(name)
        self._children: list[FileSystemItem] = []

    def add(self, item: FileSystemItem) -> None:
        self._children.append(item)

    def remove(self, item: FileSystemItem) -> None:
        self._children.remove(item)

    def get_size(self) -> int:
        """Size cascades down the tree automatically."""
        return sum(child.get_size() for child in self._children)

    def display(self, indent: int = 0) -> None:
        print(f"{'  ' * indent}📁 {self.name}/ ({self.get_size()}B)")
        for child in self._children:
            child.display(indent + 1)


# ---------------------------------------------------------
# STEP 4: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Build a file tree
    root = Folder("project")

    src = Folder("src")
    src.add(File("main.py", 1200))
    src.add(File("utils.py", 800))

    models = Folder("models")
    models.add(File("user.py", 500))
    models.add(File("product.py", 600))
    src.add(models)

    tests = Folder("tests")
    tests.add(File("test_main.py", 900))
    tests.add(File("test_utils.py", 700))

    root.add(src)
    root.add(tests)
    root.add(File("README.md", 300))
    root.add(File(".gitignore", 50))

    # Display the tree
    print("=== File System Tree ===")
    root.display()

    # get_size() works the same on files AND folders
    print(f"\n=== Sizes ===")
    print(f"  Total project size: {root.get_size()}B")
    print(f"  src/ size: {src.get_size()}B")
    print(f"  models/ size: {models.get_size()}B")
    print(f"  Single file (main.py): {src._children[0].get_size()}B")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. File and Folder share the SAME interface.")
    print("2. get_size() works identically on both — no isinstance().")
    print("3. Tree structure with automatic cascading.")
    print("4. Client treats leaves and branches uniformly.")
    print("5. Perfect for: file systems, UI components, org charts.")
