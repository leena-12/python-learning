# Aggregation: Cart holds Products, but Products exist independently
# (same product can be in multiple carts / catalog)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cart:
    def __init__(self):
        self.items = []

    def add_item(self, product):
        self.items.append(product)
        print(f"Added {product.name} to cart")

    def remove_item(self, product):
        if product in self.items:
            self.items.remove(product)
            print(f"Removed {product.name} from cart")

    def total(self):
        return sum(item.price for item in self.items)


p1 = Product("Keyboard", 1200)
p2 = Product("Mouse", 500)

cart = Cart()
cart.add_item(p1)
cart.add_item(p2)

print("Total:", cart.total())