# Chain: Customer -> Order -> Cart -> Payment
# Cart/Payment composed inside Order (created by Order)
# Order aggregated by Customer (order tied to one customer but modeled as list)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)

    def total(self):
        return sum(item.price for item in self.items)


class Payment:
    def __init__(self, amount, method):
        self.amount = amount
        self.method = method

    def process(self):
        print(f"Paid {self.amount} via {self.method}")


class Order:
    def __init__(self, method):
        self.cart = Cart()               # composition
        self.payment = None
        self.method = method

    def add_product(self, product):
        self.cart.add_item(product)

    def checkout(self):
        self.payment = Payment(self.cart.total(), self.method)  # composition
        self.payment.process()


class Customer:
    def __init__(self, name):
        self.name = name
        self.orders = []   # aggregation - orders could be tracked elsewhere too

    def place_order(self, order):
        self.orders.append(order)
        print(f"{self.name} placing order...")
        order.checkout()


order = Order("UPI")
order.add_product(Product("Laptop Bag", 900))
order.add_product(Product("Mouse Pad", 200))

customer = Customer("Leena")
customer.place_order(order)