from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"Borrowed: {self.title}")
        else:
            print(f"{self.title} is already borrowed.")

    def return_item(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"Returned: {self.title}")
        else:
            print(f"{self.title} was not borrowed.")

    @abstractmethod
    def display_details(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[Book] {self.title} by {self.author} - {status}")


class Magazine(LibraryItem):
    def __init__(self, title, issue_number):
        super().__init__(title)
        self.issue_number = issue_number

    def display_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[Magazine] {self.title} (Issue {self.issue_number}) - {status}")


class Newspaper(LibraryItem):
    def __init__(self, title, date):
        super().__init__(title)
        self.date = date

    def display_details(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        print(f"[Newspaper] {self.title} ({self.date}) - {status}")


def display_items(items):
    print("\n--- Library Items ---")
    for index, item in enumerate(items, start=1):
        print(f"{index}. ", end="")
        item.display_details()   # polymorphism here


def borrow_item(items):
    display_items(items)
    choice = int(input("Enter item number to borrow: "))
    if 1 <= choice <= len(items):
        items[choice - 1].borrow()
    else:
        print("Invalid choice.")


def return_item(items):
    display_items(items)
    choice = int(input("Enter item number to return: "))
    if 1 <= choice <= len(items):
        items[choice - 1].return_item()
    else:
        print("Invalid choice.")


def main():
    items = [
        Book("Clean Code", "Robert C. Martin"),
        Magazine("Tech Today", 42),
        Newspaper("The Daily News", "2026-08-09")
    ]

    while True:
        print("\n=== Library Menu ===")
        print("1. Display Items")
        print("2. Borrow Item")
        print("3. Return Item")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_items(items)
        elif choice == "2":
            borrow_item(items)
        elif choice == "3":
            return_item(items)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()