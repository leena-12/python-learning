"""
Phone Book Application
--------------------------
Menu:
1. Add Contact
2. Search Contact
3. Update Number
4. Delete Contact
5. Display Contacts
6. Exit
Bonus: Prevents duplicate contact names.
"""

contacts = {}


def add_contact():
    name = input("Enter name: ")

    if name in contacts:
        print("Contact already exists.")
        return

    number = input("Enter phone number: ")
    contacts[name] = number
    print("Contact added.")


def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(name, ":", contacts[name])
    else:
        print("Contact not found.")


def update_number():
    name = input("Enter name to update: ")
    if name in contacts:
        number = input("Enter new number: ")
        contacts[name] = number
        print("Number updated.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


def display_contacts():
    for name, number in contacts.items():
        print(name, ":", number)


while True:
    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Update Number")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_number()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")