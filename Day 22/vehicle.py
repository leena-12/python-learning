from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started.")


class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started.")


class Truck(Vehicle):
    def start_engine(self):
        print("Truck engine started.")


if __name__ == "__main__":
    vehicles = [Car(), Bike(), Truck()]
    for v in vehicles:
        v.start_engine()