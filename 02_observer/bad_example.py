"""
=============================================================
 BAD EXAMPLE: Without the Observer Pattern
=============================================================

An online store that notifies customers when a product is back in stock.

Problems:
    1. The Store class must KNOW about every notification method
    2. Adding SMS notification → modify the Store class
    3. Adding push notification → modify the Store class again
    4. Store is tightly coupled to all notification logic
    5. Can't add/remove subscribers at runtime
=============================================================
"""


class BadStore:
    def __init__(self):
        self.customer_emails = []
        self.customer_phones = []

    def add_email_customer(self, email: str):
        self.customer_emails.append(email)

    def add_phone_customer(self, phone: str):
        self.customer_phones.append(phone)

    def restock(self, product: str):
        print(f"\n📦 '{product}' is back in stock!")

        # Store has to handle EVERY notification type itself
        for email in self.customer_emails:
            print(f"  📧 Sending email to {email}: '{product}' is available!")

        for phone in self.customer_phones:
            print(f"  📱 Sending SMS to {phone}: '{product}' is available!")

        # Want to add push notifications? Slack alerts? Webhook calls?
        # You have to modify THIS class every single time!


if __name__ == "__main__":
    store = BadStore()
    store.add_email_customer("alice@mail.com")
    store.add_email_customer("bob@mail.com")
    store.add_phone_customer("010-1234-5678")

    store.restock("PlayStation 6")

    print()
    print("Problems with this approach:")
    print("  - Store knows about emails, phones, and every future channel")
    print("  - Adding a new channel = modifying the Store class")
    print("  - Can't reuse notification logic elsewhere")
    print("  → The Observer pattern fixes this.")
