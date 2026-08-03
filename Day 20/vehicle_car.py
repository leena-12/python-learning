class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Model:", self.model)
        print("Year :", self.year)


class Car(Vehicle):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type

    def display(self):
        super().display()
        print("Fuel Type:", self.fuel_type)


if __name__ == "__main__":
    v = Vehicle("Generic", "Basic", 2000)
    print("== Vehicle ==")
    v.display()

    c = Car("Toyota", "Corolla", 2022, "Petrol")
    print("\n== Car ==")
    c.display()