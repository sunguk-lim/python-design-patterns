"""
=============================================================
 DESIGN PATTERN #12: ABSTRACT FACTORY
=============================================================

Category: Creational
Intent:   Provide an interface for creating FAMILIES of related
          objects without specifying their concrete classes.

Real-world analogy:
    A furniture store with catalogs: "Modern", "Victorian", "Art Deco".
    Each catalog has a matching chair, sofa, and table. You pick a
    catalog (factory) and everything you get is guaranteed to match.

Difference from Factory Method:
    - Factory Method: creates ONE product via subclassing
    - Abstract Factory: creates a FAMILY of related products

When to use:
    - You need to create families of related objects
    - You want to ensure consistency within a family
    - You want to swap entire families at once

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: Product interfaces (what each product must do)
# ---------------------------------------------------------

class Button(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> str:
        pass

class TextField(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


# ---------------------------------------------------------
# STEP 2: Concrete products — Windows family
# ---------------------------------------------------------

class WindowsButton(Button):
    def render(self) -> str:
        return "[ Windows Button ]"

class WindowsCheckbox(Checkbox):
    def render(self) -> str:
        return "[ Windows ☑ ]"

class WindowsTextField(TextField):
    def render(self) -> str:
        return "[ Windows _____ ]"


# ---------------------------------------------------------
# STEP 3: Concrete products — Mac family
# ---------------------------------------------------------

class MacButton(Button):
    def render(self) -> str:
        return "( Mac Button )"

class MacCheckbox(Checkbox):
    def render(self) -> str:
        return "( Mac ☑ )"

class MacTextField(TextField):
    def render(self) -> str:
        return "( Mac _____ )"


# ---------------------------------------------------------
# STEP 4: The Abstract Factory interface
# ---------------------------------------------------------

class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

    @abstractmethod
    def create_text_field(self) -> TextField:
        pass


# ---------------------------------------------------------
# STEP 5: Concrete factories — each produces a FAMILY
# ---------------------------------------------------------

class WindowsFactory(UIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

    def create_text_field(self) -> TextField:
        return WindowsTextField()


class MacFactory(UIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

    def create_text_field(self) -> TextField:
        return MacTextField()


# ---------------------------------------------------------
# STEP 6: Client code — works with ANY factory
# ---------------------------------------------------------

def render_ui(factory: UIFactory) -> None:
    """This function has NO idea if it's Windows or Mac."""
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    text_field = factory.create_text_field()

    print(f"  {button.render()}")
    print(f"  {checkbox.render()}")
    print(f"  {text_field.render()}")


# ---------------------------------------------------------
# STEP 7: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=== Windows UI ===")
    render_ui(WindowsFactory())

    print("\n=== Mac UI ===")
    render_ui(MacFactory())

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. render_ui() doesn't know Windows vs Mac.")
    print("2. Each factory guarantees a CONSISTENT family.")
    print("3. Can't accidentally mix Windows button + Mac checkbox.")
    print("4. Swap the entire theme by changing ONE factory object.")
    print("5. Factory Method = one product, Abstract Factory = family.")
