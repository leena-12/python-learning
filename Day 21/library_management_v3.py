class LibraryItem:
    def __init__(self, title, item_id):
        self.title = title
        self.item_id = item_id
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(self.title, "has been borrowed.")
        else:
            print(self.title, "is already borrowed.")

    def return_item(self):
        if not self.available:
            self.available = True
            print(self.title, "has been returned.")
        else:
            print(self.title, "was not borrowed.")

    def display_details(self):
        print("Title:", self.title)
        print("ID:", self.item_id)
        print("Available:", self.available)


class Book(LibraryItem):
    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def display_details(self):
        print("Book")
        print("Title:", self.title)
        print("ID:", self.item_id)
        print("Author:", self.author)
        print("Pages:", self.pages)
        print("Available:", self.available)
        print("--------------------")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_number):
        super().__init__(title, item_id)
        self.issue_number = issue_number

    def display_details(self):
        print("Magazine")
        print("Title:", self.title)
        print("ID:", self.item_id)
        print("Issue Number:", self.issue_number)
        print("Available:", self.available)
        print("--------------------")


class Newspaper(LibraryItem):
    def __init__(self, title, item_id, date):
        super().__init__(title, item_id)
        self.date = date

    def display_details(self):
        print("Newspaper")
        print("Title:", self.title)
        print("ID:", self.item_id)
        print("Date:", self.date)
        print("Available:", self.available)
        print("--------------------")


if __name__ == "__main__":
    library = [
        Book("Python Basics", "B001", "James", 300),
        Magazine("Tech World", "M001", 25),
        Newspaper("Daily News", "N001", "2026-08-06")
    ]

    print("=== Library Items ===")

    for item in library:
        item.display_details()

    print("=== Borrowing Book ===")
    library[0].borrow()
    library[0].borrow()

    print("\n=== Returning Book ===")
    library[0].return_item()