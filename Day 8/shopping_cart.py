"""
Build a Shopping Cart Program.

Menu:

1. Add Item
2. Remove Item
3. Display Cart
4. Count Items
5. Exit
"""

cart = [str(cart) for cart in input("Enter items separated by spaces: ").split()]



def add_item():
    item = input("Enter item name to add: ").strip()
    if item == "":
        print("Item name cannot be empty.")
        return
    cart.append(item)
    print(f"'{item}' added to cart.")


def remove_item():
    if not cart:
        print("Cart is empty. Nothing to remove.")
        return
    item = input("Enter item name to remove: ").strip()
    if item in cart:
        cart.remove(item)
        print(f"'{item}' removed from cart.")
    else:
        print(f"'{item}' not found in cart.")


def display_cart():
    if not cart:
        print("Your cart is empty.")
        return
    print("Items in your cart:")
    for i, item in enumerate(cart, start=1):
        print(f"{i}. {item}")


def count_items():
    print(f"Total items in cart: {len(cart)}")


def show_menu():
    print("\n--- Shopping Cart ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Cart")
    print("4. Count Items")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_cart()
        elif choice == "4":
            count_items()
        elif choice == "5":
            print("Exiting Shopping Cart. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()