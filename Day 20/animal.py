class Animal:
    def speak(self):
        print("Animal is making a sound.")


class Dog(Animal):
    def speak(self):
        print("Dog barks: Woof!")


class Cat(Animal):
    def speak(self):
        print("Cat meows: Meow!")


if __name__ == "__main__":
    a = Animal()
    d = Dog()
    c = Cat()

    print("=== Animal ===")
    a.speak()

    print("\n=== Dog ===")
    d.speak()

    print("\n=== Cat ===")
    c.speak()

    print("\n=== Polymorphism ===")
    creatures = [a, d, c]
    for creature in creatures:
        creature.speak()