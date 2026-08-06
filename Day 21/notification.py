class Notification:
    def send(self, message):
        print("Sending notification:", message)


class Email(Notification):
    def send(self, message):
        print("Email sent:", message)


class SMS(Notification):
    def send(self, message):
        print("SMS sent:", message)


class PushNotification(Notification):
    def send(self, message):
        print("Push notification sent:", message)


if __name__ == "__main__":
    notifications = [
        Email(),
        SMS(),
        PushNotification()
    ]

    for notification in notifications:
        notification.send("Your order has been shipped.")