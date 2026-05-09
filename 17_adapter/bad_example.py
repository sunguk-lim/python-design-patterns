"""
=============================================================
 BAD EXAMPLE: Without the Adapter Pattern
=============================================================

Your app uses a PaymentProcessor interface, but a third-party
library (StripeAPI) has a completely different interface.

Problems:
    1. Can't use StripeAPI directly — incompatible method names
    2. Modifying StripeAPI is impossible (it's a third-party lib)
    3. Client code would need ugly if/elif for each payment service
=============================================================
"""


class PaymentProcessor:
    """Your app's expected interface."""
    def pay(self, amount: float) -> str:
        raise NotImplementedError


class StripeAPI:
    """Third-party library — you can't modify this!"""
    def create_charge(self, amount_cents: int, currency: str) -> dict:
        return {"status": "success", "amount": amount_cents, "currency": currency}


class PayPalAPI:
    """Another third-party library with yet another interface."""
    def send_payment(self, recipient: str, value: float) -> bool:
        return True


if __name__ == "__main__":
    stripe = StripeAPI()
    # Can't do stripe.pay(10.00) — method doesn't exist!
    # Must use stripe.create_charge(1000, "usd") instead.

    result = stripe.create_charge(1000, "usd")
    print(f"  Stripe raw call: {result}")

    print()
    print("StripeAPI.create_charge() != PaymentProcessor.pay()")
    print("PayPalAPI.send_payment() != PaymentProcessor.pay()")
    print("Incompatible interfaces!")
    print("→ The Adapter pattern fixes this.")
