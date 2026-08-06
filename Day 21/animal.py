class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")


class Cow(Animal):
    def speak(self):
        print("Cow says: Moo!")


if __name__ == "__main__":
    animals = [Dog(), Cat(), Cow()]

    for animal in animals:
        animal.speak()