"""
=============================================================
 DESIGN PATTERN #17: ADAPTER
=============================================================

Category: Structural
Intent:   Convert the interface of a class into another interface
          that clients expect. Lets classes work together that
          couldn't otherwise because of incompatible interfaces.

Real-world analogy:
    A power adapter for international travel. Your laptop has a
    US plug, but the outlet is European. The adapter converts
    one interface to another without modifying either.

When to use:
    - You want to use a class with an incompatible interface
    - You can't modify the existing class (third-party library)
    - You want to create a reusable bridge between interfaces

=============================================================
"""

from abc import ABC, abstractmethod


# ---------------------------------------------------------
# STEP 1: The target interface (what YOUR code expects)
# ---------------------------------------------------------

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# ---------------------------------------------------------
# STEP 2: Third-party services (can't modify these!)
# ---------------------------------------------------------

class StripeAPI:
    def create_charge(self, amount_cents: int, currency: str) -> dict:
        return {"status": "success", "amount": amount_cents, "currency": currency}


class PayPalAPI:
    def send_payment(self, recipient: str, value: float) -> bool:
        return True


class SquareAPI:
    def process_transaction(self, amount: str) -> str:
        return f"APPROVED:{amount}"


# ---------------------------------------------------------
# STEP 3: Adapters — bridge incompatible interfaces
# ---------------------------------------------------------

class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe: StripeAPI):
        self._stripe = stripe

    def pay(self, amount: float) -> str:
        # Convert dollars to cents, add currency
        result = self._stripe.create_charge(int(amount * 100), "usd")
        return f"💳 Stripe: {result['status']} (${amount:.2f})"


class PayPalAdapter(PaymentProcessor):
    def __init__(self, paypal: PayPalAPI):
        self._paypal = paypal

    def pay(self, amount: float) -> str:
        # Adapt to PayPal's different method signature
        success = self._paypal.send_payment("merchant@shop.com", amount)
        status = "success" if success else "failed"
        return f"🅿️  PayPal: {status} (${amount:.2f})"


class SquareAdapter(PaymentProcessor):
    def __init__(self, square: SquareAPI):
        self._square = square

    def pay(self, amount: float) -> str:
        # Adapt to Square's string-based interface
        result = self._square.process_transaction(f"{amount:.2f}")
        return f"⬛ Square: {result}"


# ---------------------------------------------------------
# STEP 4: Client code — works with any PaymentProcessor
# ---------------------------------------------------------

def checkout(processor: PaymentProcessor, amount: float) -> None:
    """This function has NO idea which payment service is used."""
    result = processor.pay(amount)
    print(f"  {result}")


# ---------------------------------------------------------
# STEP 5: See it in action
# ---------------------------------------------------------

if __name__ == "__main__":
    # Wrap third-party APIs in adapters
    stripe = StripeAdapter(StripeAPI())
    paypal = PayPalAdapter(PayPalAPI())
    square = SquareAdapter(SquareAPI())

    # Client code uses the SAME interface for all!
    print("=== Processing payments ===")
    checkout(stripe, 29.99)
    checkout(paypal, 49.99)
    checkout(square, 19.99)

    # Can even loop through different processors
    print("\n=== Batch payment ===")
    processors = [stripe, paypal, square]
    for processor in processors:
        checkout(processor, 10.00)

    print()
    print("=" * 60)
    print("KEY TAKEAWAYS:")
    print("=" * 60)
    print("1. Third-party APIs were NOT modified.")
    print("2. Each adapter translates one interface to another.")
    print("3. Client code (checkout) works with ANY payment service.")
    print("4. Adding a new service = just write a new adapter.")
    print("5. The adapter handles all conversion (dollars→cents, etc.).")
