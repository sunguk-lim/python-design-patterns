"""
=============================================================
 DESIGN PATTERN #10: VISITOR
=============================================================

Category: Behavioral
Intent:   Add new operations to existing object structures without
          modifying those objects. Separate algorithms from the
          objects they operate on.

Real-world analogy:
    A tax inspector visiting different businesses. The inspector
    (visitor) applies a different tax calculation to each type
    of business (restaurant, shop, office), but the businesses
    don't need to know about tax rules — they just "accept"
    the inspector's visit.

When to use:
    - You need to add operations to classes without modifying them
    - You have a stable class hierarchy but frequently add operations
    - Related operations should be grouped together (not scattered)

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Element interface — just needs accept()
# ---------------------------------------------------------

class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: "DocumentVisitor") -> str:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete elements — stable, rarely change
# ---------------------------------------------------------

class Text(DocumentElement):
    def __init__(self, content: str):
        self.content = content

    def accept(self, visitor: "DocumentVisitor") -> str:
        return visitor.visit_text(self)


class Image(DocumentElement):
    def __init__(self, url: str, width: int, height: int):
        self.url = url
        self.width = width
        self.height = height

    def accept(self, visitor: "DocumentVisitor") -> str:
        return visitor.visit_image(self)


class Table(DocumentElement):
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols

    def accept(self, visitor: "DocumentVisitor") -> str:
        return visitor.visit_table(self)


# ---------------------------------------------------------
# STEP 3: Visitor interface
# ---------------------------------------------------------

class DocumentVisitor(ABC):
    @abstractmethod
    def visit_text(self, element: Text) -> str:
        pass

    @abstractmethod
    def visit_image(self, element: Image) -> str:
        pass

    @abstractmethod
    def visit_table(self, element: Table) -> str:
        pass


# ---------------------------------------------------------
# STEP 4: Concrete visitors — each is a complete operation
# ---------------------------------------------------------
# Adding a new operation = just add a new Visitor class!

class HtmlExportVisitor(DocumentVisitor):
    def visit_text(self, element: Text) -> str:
        return f"<p>{element.content}</p>"

    def visit_image(self, element: Image) -> str:
        return f'<img src="{element.url}" width="{element.width}" height="{element.height}">'

    def visit_table(self, element: Table) -> str:
        rows = "".join("<tr>" + "<td></td>" * element.cols + "</tr>"
                       for _ in range(element.rows))
        return f"<table>{rows}</table>"


class MarkdownExportVisitor(DocumentVisitor):
    """New operation — no changes to Text, Image, or Table!"""
    def visit_text(self, element: Text) -> str:
        return element.content

    def visit_image(self, element: Image) -> str:
        return f"![image]({element.url})"

    def visit_table(self, element: Table) -> str:
        header = "| " + " | ".join(f"Col{i+1}" for i in range(element.cols)) + " |"
        separator = "| " + " | ".join("---" for _ in range(element.cols)) + " |"
        row = "| " + " | ".join("..." for _ in range(element.cols)) + " |"
        rows = "\n".join([header, separator] + [row] * element.rows)
        return rows


class SizeCalculatorVisitor(DocumentVisitor):
    """Another operation — still no changes to element classes!"""
    def visit_text(self, element: Text) -> str:
        size = len(element.content)
        return f"Text: {size} chars"

    def visit_image(self, element: Image) -> str:
        size = element.width * element.height
        return f"Image: {size} pixels"

    def visit_table(self, element: Table) -> str:
        size = element.rows * element.cols
        return f"Table: {size} cells"


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Create document elements
    document = [
        Text("Hello World"),
        Image("cat.jpg", 800, 600),
        Table(3, 4),
    ]

    # Apply different visitors to the SAME elements
    print("=== HTML Export ===")
    html_visitor = HtmlExportVisitor()
    for elem in document:
        print(f"  {elem.accept(html_visitor)}")

    print("\n=== Markdown Export ===")
    md_visitor = MarkdownExportVisitor()
    for elem in document:
        print(f"  {elem.accept(md_visitor)}")

    print("\n=== Size Calculator ===")
    size_visitor = SizeCalculatorVisitor()
    for elem in document:
        print(f"  {elem.accept(size_visitor)}")

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Element classes (Text, Image, Table) were NOT modified.")
    print("2. Three operations added by creating three Visitor classes.")
    print("3. Each visitor groups related logic for ALL element types.")
    print("4. Trade-off: adding a new ELEMENT type requires updating")
    print("   all visitors. Best when elements are stable but")
    print("   operations change frequently.")
