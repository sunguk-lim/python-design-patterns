"""
Exercise stub generator.

Parses a pattern's good example and replaces concrete method bodies
with NotImplementedError, keeping class structure, __init__, abstract
classes, and the if __name__ == "__main__" block intact.
"""

import ast


def generate_exercise_stub(source: str) -> str:
    """Generate an exercise stub from a pattern's clean example.

    Keeps:
      - Imports, module docstring, comments
      - ABC / abstract classes unchanged
      - Dunder methods (__init__, __str__, __repr__, etc.)
      - The if __name__ == "__main__": block
    Replaces:
      - All other concrete method bodies with raise NotImplementedError
    """
    tree = ast.parse(source)
    lines = source.splitlines(keepends=True)

    # Ensure the last line ends with newline for consistent slicing
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"

    replacements: list[tuple[int, int, str, str]] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef):
            continue

        # Skip ABC / abstract base classes entirely
        is_abc = any(
            (isinstance(b, ast.Name) and b.id == "ABC")
            or (isinstance(b, ast.Attribute) and b.attr == "ABC")
            for b in node.bases
        )
        if is_abc:
            continue

        for item in node.body:
            if not isinstance(item, (ast.FunctionDef, ast.AsyncFunctionDef)):
                continue

            # Keep dunder methods (__init__, __str__, __repr__, …)
            if item.name.startswith("__") and item.name.endswith("__"):
                continue

            # Keep abstract methods
            is_abstract = any(
                (isinstance(d, ast.Name) and d.id == "abstractmethod")
                or (isinstance(d, ast.Attribute) and d.attr == "abstractmethod")
                for d in item.decorator_list
            )
            if is_abstract:
                continue

            body = item.body
            body_start_idx = 0

            # Preserve leading docstring if present
            if body and isinstance(body[0], ast.Expr) and isinstance(
                body[0].value, ast.Constant
            ):
                if isinstance(body[0].value.value, str):
                    body_start_idx = 1

            if body_start_idx >= len(body):
                continue  # method is only a docstring

            start_line = body[body_start_idx].lineno
            end_line = body[-1].end_lineno

            # Detect indentation from the first line being replaced
            first_line = lines[start_line - 1]
            indent = first_line[: len(first_line) - len(first_line.lstrip())]

            replacements.append((start_line, end_line, indent, item.name))

    # Apply replacements in reverse order so line numbers stay valid
    result = list(lines)
    for start, end, indent, name in sorted(
        replacements, key=lambda x: x[0], reverse=True
    ):
        todo_line = f'{indent}raise NotImplementedError("TODO: implement {name}")\n'
        result[start - 1 : end] = [todo_line]

    # Add a header comment
    header = (
        '"""\n'
        "CHALLENGE MODE\n"
        "\n"
        "The class structure and __init__ methods are provided.\n"
        "Implement the methods marked with TODO.\n"
        "When done, click 'Verify' to compare your output with the expected answer.\n"
        '"""\n\n'
    )

    stub = "".join(result)

    # Insert header after the original module docstring if present
    # Find end of original docstring
    for node in ast.iter_child_nodes(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant):
            if isinstance(node.value.value, str):
                # Replace the original docstring with the challenge header
                doc_end = node.end_lineno
                original_lines = stub.splitlines(keepends=True)
                return header + "".join(original_lines[doc_end:])
        break  # only check the very first statement

    return header + stub
