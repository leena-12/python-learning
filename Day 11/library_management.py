# Library Book Management System using set

def add_book(books):
    title = input("Enter book title to add: ").strip()
    if not title:
        print("Title cannot be empty.")
        return
    if title in books:
        print("Book already exists in the library.")
    else:
        books.add(title)
        print("Book added successfully.")


def remove_book(books):
    if not books:
        print("No books in the library to remove.")
        return
    title = input("Enter book title to remove: ").strip()
    if title in books:
        books.remove(title)
        print("Book removed successfully.")
    else:
        print("Book not found in the library.")


def search_book(books):
    if not books:
        print("No books in the library.")
        return
    title = input("Enter book title to search: ").strip()
    if title in books:
        print("Book is available in the library.")
    else:
        print("Book is NOT available in the library.")


def display_books(books):
    if not books:
        print("No books in the library.")
        return
    print("Books in the library:")
    for book in sorted(books):
        print("-", book)


def count_books(books):
    print("Total number of books:", len(books))


def get_menu_choice():
    while True:
        print("\nLibrary Book Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display All Books")
        print("5. Count Books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        # Validate that input is a digit and in range 1-6
        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 6.")
            continue

        choice = int(choice)
        if 1 <= choice <= 6:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


def main():
    books = set()

    while True:
        choice = get_menu_choice()

        if choice == 1:
            add_book(books)
        elif choice == 2:
            remove_book(books)
        elif choice == 3:
            search_book(books)
        elif choice == 4:
            display_books(books)
        elif choice == 5:
            count_books(books)
        elif choice == 6:
            print("Exiting the program. Goodbye!")
            break


if __name__ == "__main__":
    main()