"""
=============================================================
 BAD EXAMPLE: Without Dependency Injection
=============================================================

A notification service that creates its own dependencies.

Problems:
    1. EmailSender is hardcoded — can't swap to SMS or Slack
    2. Can't test NotificationService without sending real emails
    3. Tight coupling — changing EmailSender breaks everything
    4. No flexibility — one fixed configuration
=============================================================
"""


class EmailSender:
    def send(self, to: str, message: str):
        print(f"  📧 Sending email to {to}: '{message}'")


class BadNotificationService:
    def __init__(self):
        # Creates its OWN dependency — hardcoded!
        self.sender = EmailSender()

    def notify(self, user: str, message: str):
        self.sender.send(user, message)
        # Want to send via SMS instead? Must modify THIS class!
        # Want to test without sending real emails? Can't!


if __name__ == "__main__":
    service = BadNotificationService()
    service.notify("alice@mail.com", "Your order shipped!")
    service.notify("bob@mail.com", "Password reset requested")

    print()
    print("EmailSender is hardcoded inside NotificationService.")
    print("Can't swap, can't test, can't configure.")
    print("→ Dependency Injection fixes this.")
