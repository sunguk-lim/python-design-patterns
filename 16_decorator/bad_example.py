"""
=============================================================
 BAD EXAMPLE: Without the Decorator Pattern
=============================================================

A coffee shop with different toppings/extras.

Problems:
    1. Class explosion: Coffee, CoffeeWithMilk, CoffeeWithMilkAndSugar,
       CoffeeWithMilkAndSugarAndWhip... 2^N combinations!
    2. Can't add toppings dynamically at runtime
    3. Every new topping doubles the number of classes
=============================================================
"""


class Coffee:
    def cost(self): return 2.00
    def description(self): return "Coffee"

class CoffeeWithMilk:
    def cost(self): return 2.50
    def description(self): return "Coffee + Milk"

class CoffeeWithMilkAndSugar:
    def cost(self): return 2.70
    def description(self): return "Coffee + Milk + Sugar"

class CoffeeWithMilkAndSugarAndWhip:
    def cost(self): return 3.40
    def description(self): return "Coffee + Milk + Sugar + Whipped Cream"

# CoffeeWithSugar? CoffeeWithWhip? CoffeeWithMilkAndWhip?
# 4 toppings = 16 possible classes!!


if __name__ == "__main__":
    orders = [Coffee(), CoffeeWithMilk(), CoffeeWithMilkAndSugar()]
    for o in orders:
        print(f"  {o.description()}: ${o.cost():.2f}")

    print()
    print("4 toppings = 2^4 = 16 classes needed!")
    print("→ The Decorator pattern fixes this.")
