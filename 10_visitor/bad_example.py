"""
=============================================================
 BAD EXAMPLE: Without the Visitor Pattern
=============================================================

A document with different element types (Text, Image, Table).
You need to add operations: export to HTML, calculate size, etc.

Problems:
    1. Adding a new operation = modify EVERY element class
    2. Element classes get bloated with unrelated methods
    3. Violates Single Responsibility — elements shouldn't know
       about HTML export, PDF export, size calculation, etc.
=============================================================
"""


class BadText:
    def __init__(self, content: str):
        self.content = content

    def to_html(self):
        return f"<p>{self.content}</p>"

    def calculate_size(self):
        return len(self.content)

    # to_pdf()? to_markdown()? to_latex()?
    # Each new operation = modify THIS class!


class BadImage:
    def __init__(self, url: str, width: int, height: int):
        self.url = url
        self.width = width
        self.height = height

    def to_html(self):
        return f'<img src="{self.url}" width="{self.width}" height="{self.height}">'

    def calculate_size(self):
        return self.width * self.height

    # Same problem — every new operation goes here


if __name__ == "__main__":
    elements = [BadText("Hello World"), BadImage("cat.jpg", 800, 600)]

    print("=== HTML Export ===")
    for elem in elements:
        print(f"  {elem.to_html()}")

    print("\n=== Size Calculation ===")
    for elem in elements:
        print(f"  Size: {elem.calculate_size()}")

    print()
    print("Every new operation (PDF export, markdown, etc.)")
    print("requires modifying ALL element classes.")
    print("→ The Visitor pattern fixes this.")
