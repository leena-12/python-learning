"""
Create a Rectangle class.

Methods:
Area
Perimeter
"""

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        a = self.length*self.breadth
        print("The area of rectangle is :", a)
        return a

    def perimeter(self):
        p = 2*(self.length + self.breadth)
        print("The perimeter of the rectangle is:", p)
        return p

rectangle1 = Rectangle(8, 23)
rectangle1.area()
rectangle1.perimeter()



"""
Create an Employee class.

Calculate annual salary.
"""

class Employee:
    def __init__(self, salary):
        self.salary = salary

    def annual(self):
        b = self.salary*12
        print("The annual salary is :",b)
        return b

employee1 = Employee(90000)
employee1.annual()



"""
Create a Book class.

Store:
Title
Author
Price
"""

class Book:
    def __init__(self, title, author, price ):
        self.title = title
        self.author = author
        self.price = price

    def print_title(self):
        print(" The title of the book is:",self.title)

    def print_author(self):
            print(" The author of the book is:",self.author)

    def print_price(self):
            print(" The price of the book is: Rs.",self.price)

book1 = Book("Scars","tyla",100)
book1.print_title()
book1.print_author()
book1.print_price()