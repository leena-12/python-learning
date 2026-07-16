# Unique Visitor Tracker using a set

def add_visitor(visitors):
    username = input("Enter visitor username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return

    if username in visitors:
        print("This visitor is already recorded.")
    else:
        visitors.add(username)
        print("Visitor added successfully.")


def show_visitors(visitors):
    if not visitors:
        print("No visitors yet.")
        return

    print("List of unique visitors:")
    for user in sorted(visitors):
        print("-", user)


def count_visitors(visitors):
    print("Total unique visitors:", len(visitors))


def get_menu_choice():
    while True:
        print("\nUnique Visitor Tracker")
        print("1. Add Visitor")
        print("2. Show Visitors")
        print("3. Count Visitors")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()


        if not choice.isdigit():
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        choice = int(choice)
        if 1 <= choice <= 4:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


def main():
    visitors = set()   
    while True:
        choice = get_menu_choice()

        if choice == 1:
            add_visitor(visitors)
        elif choice == 2:
            show_visitors(visitors)
        elif choice == 3:
            count_visitors(visitors)
        elif choice == 4:
            print("Exiting. Goodbye!")
            break


if __name__ == "__main__":
    main()