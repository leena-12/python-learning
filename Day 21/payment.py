class Payment:
    def pay(self, amount):
        print("Payment of", amount, "is being processed.")


class UPI(Payment):
    def pay(self, amount):
        print("Paid", amount, "using UPI.")


class CreditCard(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Credit Card.")


class Cash(Payment):
    def pay(self, amount):
        print("Paid", amount, "using Cash.")


if __name__ == "__main__":
    payments = [
        UPI(),
        CreditCard(),
        Cash()
    ]

    for payment in payments:
        payment.pay(500)