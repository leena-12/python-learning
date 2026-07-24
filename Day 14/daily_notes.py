FILE_NAME = "notes_log.txt"


def write_note():
    note = input("Enter today's note: ")

    with open(FILE_NAME, "a") as file:
        file.write(note + "\n")

    print("Note saved.")


def read_notes():
    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        if not notes:
            print("No notes found.")
            return

        print("\n--- All Notes ---")
        for i, note in enumerate(notes, start=1):
            print(str(i) + ". " + note.strip())

        print("\nTotal notes stored:", len(notes))

    except FileNotFoundError:
        print("No notes found yet.")


def search_word():
    word = input("Enter word to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            notes = file.readlines()

        found = False
        for note in notes:
            if word.lower() in note.lower():
                print(note.strip())
                found = True

        if not found:
            print("Word not found in any note.")

    except FileNotFoundError:
        print("No notes found yet.")


while True:
    print("\n1. Write Today's Note")
    print("2. Read All Notes")
    print("3. Search a Word")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        search_word()
    elif choice == "4":
        print("Exiting the notes, byeeee!!")
        break
    else:
        print("Invalid choice.")