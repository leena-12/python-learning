"""
Movie Collection Manager
--------------------------
Menu:
1. Add Movie
2. Remove Movie
3. Search Movie
4. Display Movies
5. Exit
"""

movies = [str(x) for x in input("enter the movie names to add in the list separated by spaces:").split()] 
print("The movies list is:",movies)

def add_movie():
    title = input("Enter movie title: ").strip()

    if title == "":
        print("Movie title cannot be empty. Try again.")
        return

    if title.lower() in [m.lower() for m in movies]:
        print(f"'{title}' already exists in your collection.")
        return

    movies.append(title)
    print(f"'{title}' added to your collection.")


def remove_movie():
    if not movies:
        print("Your collection is empty.")
        return

    title = input("Enter movie title to remove: ").strip()

    for movie in movies:
        if movie.lower() == title.lower():
            movies.remove(movie)
            print(f"'{movie}' removed from your collection.")
            return

    print(f"'{title}' not found in your collection.")


def search_movie():
    if not movies:
        print("Your collection is empty.")
        return

    keyword = input("Enter movie title (or part of it) to search: ").strip().lower()

    if keyword == "":
        print("Search text cannot be empty.")
        return

    results = [m for m in movies if keyword in m.lower()]

    if results:
        print("\n--- Search Results ---")
        for movie in results:
            print(movie)
        print("-----------------------")
    else:
        print(f"No movies found matching '{keyword}'.")


def display_movies():
    if not movies:
        print("Your collection is empty.")
        return

    print("\n--- Movie Collection ---")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie}")
    print(f"Total movies: {len(movies)}")
    print("-------------------------")


def get_menu_choice():
    print("\n===== Movie Collection Manager =====")
    print("1. Add Movie")
    print("2. Remove Movie")
    print("3. Search Movie")
    print("4. Display Movies")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ").strip()

    if choice not in ["1", "2", "3", "4", "5"]:
        print("Invalid input. Please enter a number between 1 and 5.")
        return None

    return choice


def main():
    while True:
        choice = get_menu_choice()

        if choice is None:
            continue
        elif choice == "1":
            add_movie()
        elif choice == "2":
            remove_movie()
        elif choice == "3":
            search_movie()
        elif choice == "4":
            display_movies()
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break


if __name__ == "__main__":
    main()