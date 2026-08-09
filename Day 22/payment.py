from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


class UPI(Payment):
    def __init__(self, upi_id):
        self.upi_id = upi_id

    def pay(self, amount):
        print(f"Paying Rs.{amount} via UPI ID {self.upi_id}")


class CreditCard(Payment):
    def __init__(self, card_number):
        self.card_number = card_number

    def pay(self, amount):
        print(f"Paying Rs.{amount} using Credit Card {self.card_number}")


class Cash(Payment):
    def pay(self, amount):
        print(f"Paying Rs.{amount} in cash.")


if __name__ == "__main__":
    payments = [
        UPI("user@upi"),
        CreditCard("1234-5678-9012"),
        Cash()
    ]

    for p in payments:
        p.pay(1000)