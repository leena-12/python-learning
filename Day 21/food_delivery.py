class FoodItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def calculate_price(self):
        return 0

    def display(self):
        print(self.name)
        print("Quantity:", self.quantity)
        print("Price:", self.calculate_price())
        print("--------------------")


class Pizza(FoodItem):
    def __init__(self, name, quantity, size):
        super().__init__(name, quantity)
        self.size = size

    def calculate_price(self):
        if self.size == "Small":
            return 200 * self.quantity
        elif self.size == "Medium":
            return 300 * self.quantity
        else:
            return 400 * self.quantity


class Burger(FoodItem):
    def calculate_price(self):
        return 150 * self.quantity


class Pasta(FoodItem):
    def calculate_price(self):
        return 180 * self.quantity


if __name__ == "__main__":
    food_items = [
        Pizza("Cheese Pizza", 2, "Medium"),
        Burger("Veg Burger", 3),
        Pasta("White Sauce Pasta", 1)
    ]

    for food in food_items:
        food.display()