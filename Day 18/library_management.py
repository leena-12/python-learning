
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Title :", self.title)
        print("Author:", self.author)
        print("Price :", self.price)
        print("-" * 20)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        price = float(input("Enter book price: "))
        book = Book(title, author, price)
        self.books.append(book)
        print("Book added.")

    def display_books(self):
        if not self.books:
            print("No books.")
            return
        for book in self.books:
            book.display()

    def search_book(self):
        keyword = input("Enter title or author to search: ").lower()
        found = False
        for book in self.books:
            if keyword in book.title.lower() or keyword in book.author.lower():
                book.display()
                found = True
        if not found:
            print("No matching book.")


def menu():
    lib = Library()
    while True:
        print("\n1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Exit")
        ch = input("Enter choice: ")

        if ch == "1":
            lib.add_book()
        elif ch == "2":
            lib.display_books()
        elif ch == "3":
            lib.search_book()
        elif ch == "4":
            print("Bye!")
            break
        else:
            print("Wrong choice.")


if __name__ == "__main__":
    menu()