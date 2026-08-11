class Engine :
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with ({self.horsepower}HP) started.")

    def stop(self):
        print(f"Engine stopped.")

class Car :
    def __init__(self, brand, horsepower):
        self.brand = brand
        self.engine = Engine(horsepower)

    def start(self):
        print(f"{self.brand} starting..")
        self.engine.start()

    def stop(self):
        print(f"{self.brand} stopped...")
        self.engine.stop()

car = Car( "Honda" , 120)
car.start()
car.stop()
