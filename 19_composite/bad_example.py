"""
=============================================================
 BAD EXAMPLE: Without the Composite Pattern
=============================================================

A file system with files and folders. You want to calculate
the total size.

Problems:
    1. Client must check type (file vs folder) everywhere
    2. Nested folders require recursive logic in the client
    3. Files and folders have different interfaces
    4. Adding new types (symlinks) breaks all client code
=============================================================
"""


class BadFile:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size


class BadFolder:
    def __init__(self, name: str):
        self.name = name
        self.children = []

    def add(self, item):
        self.children.append(item)


def calculate_size(item) -> int:
    """Client must know about EVERY type and handle recursion."""
    if isinstance(item, BadFile):
        return item.size
    elif isinstance(item, BadFolder):
        total = 0
        for child in item.children:
            total += calculate_size(child)  # manual recursion
        return total
    else:
        raise TypeError(f"Unknown type: {type(item)}")


if __name__ == "__main__":
    root = BadFolder("root")
    root.add(BadFile("readme.txt", 100))
    docs = BadFolder("docs")
    docs.add(BadFile("guide.pdf", 500))
    docs.add(BadFile("api.md", 200))
    root.add(docs)

    print(f"  Total size: {calculate_size(root)} bytes")
    print()
    print("Client must use isinstance() and handle recursion itself.")
    print("→ The Composite pattern fixes this.")
