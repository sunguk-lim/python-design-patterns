"""
=============================================================
 BAD EXAMPLE: Without the Abstract Factory Pattern
=============================================================

A UI toolkit that supports Windows and Mac styles.

Problems:
    1. Client must manually coordinate which button + checkbox to use
    2. Easy to mix Windows button with Mac checkbox (inconsistency)
    3. Adding a new OS theme = scattered changes everywhere
=============================================================
"""


class WindowsButton:
    def render(self): return "[Windows Button]"

class WindowsCheckbox:
    def render(self): return "[Windows ☑]"

class MacButton:
    def render(self): return "[Mac Button]"

class MacCheckbox:
    def render(self): return "[Mac ☑]"


def create_ui(os_type: str):
    if os_type == "windows":
        button = WindowsButton()
        checkbox = WindowsCheckbox()
    elif os_type == "mac":
        button = MacButton()
        checkbox = MacCheckbox()
    else:
        raise ValueError(f"Unknown OS: {os_type}")

    print(f"  {button.render()} {checkbox.render()}")


if __name__ == "__main__":
    create_ui("windows")
    create_ui("mac")

    print()
    print("What if someone accidentally mixes WindowsButton + MacCheckbox?")
    mixed_button = WindowsButton()
    mixed_checkbox = MacCheckbox()
    print(f"  Inconsistent: {mixed_button.render()} {mixed_checkbox.render()}")
    print("→ The Abstract Factory pattern prevents this.")
