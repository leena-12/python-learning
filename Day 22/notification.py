from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):
    def __init__(self, email_address):
        self.email_address = email_address

    def send(self, message):
        print(f"Sending EMAIL to {self.email_address}: {message}")


class SMS(Notification):
    def __init__(self, phone_number):
        self.phone_number = phone_number

    def send(self, message):
        print(f"Sending SMS to {self.phone_number}: {message}")


class PushNotification(Notification):
    def __init__(self, device_id):
        self.device_id = device_id

    def send(self, message):
        print(f"Sending PUSH to device {self.device_id}: {message}")


if __name__ == "__main__":
    notifications = [
        Email("user@example.com"),
        SMS("+91-9999999999"),
        PushNotification("DEVICE123")
    ]

    for n in notifications:
        n.send("Hello from abstraction!")