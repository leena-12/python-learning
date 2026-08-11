# Composition: Library owns Books (catalog created by Library)
# Aggregation: Library uses Members (they exist independently)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []      # composition - library's own catalog
        self.members = []    # aggregation - members exist outside library too

    def add_book(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, member, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                member.borrowed_books.append(book)
                print(f"{member.name} borrowed '{title}'")
                return
        print(f"'{title}' not available")

    def return_book(self, member, title):
        for book in member.borrowed_books:
            if book.title == title:
                book.is_borrowed = False
                member.borrowed_books.remove(book)
                print(f"{member.name} returned '{title}'")
                return


lib = Library("City Library")
lib.add_book("Python Basics", "John Doe")
lib.add_book("Clean Code", "Robert Martin")

leena = Member("Leena")
lib.register_member(leena)

lib.borrow_book(leena, "Python Basics")
lib.return_book(leena, "Python Basics")