class Shape:
    def area(self):
        return 0

    def display(self):
        print("This is a shape.")


class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def display(self):
        print("Shape: Rectangle")
        print("Length:", self.length)
        print("Breadth:", self.breadth)
        print("Area  :", self.area())

if __name__ == "__main__":
    s = Shape()
    r = Rectangle(5, 3)

    print("=== Shape ===")
    s.display()
    print("Area:", s.area())

    print("\n=== Rectangle ===")
    r.display()