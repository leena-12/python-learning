class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.is_available = True

    def display(self):
        print("Title      :", self.title)
        print("ID         :", self.item_id)
        print("Available  :", "Yes" if self.is_available else "No")

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_item(self):
        if not self.is_available:
            self.is_available = True
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display(self):
        super().display()
        print("Author     :", self.author)
        print("Pages      :", self.pages)


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display(self):
        super().display()
        print("Issue No   :", self.issue_number)


class Newspaper(LibraryItem):
    def __init__(self, title, item_id, date):
        super().__init__(title, item_id)
        self.date = date

    def display(self):
        super().display()
        print("Date       :", self.date)

if __name__ == "__main__":
    book = Book("Scars", "B001", "Taylor Swift", 250)
    magazine = Magazine("Tech Today", "M001", 42)
    newspaper = Newspaper("Daily News", "N001", "2026-08-03")

    print("=== Book ===")
    book.display()
    book.borrow()
    book.borrow()  
    book.return_item()

    print("\n=== Magazine ===")
    magazine.display()

    print("\n=== Newspaper ===")
    newspaper.display()