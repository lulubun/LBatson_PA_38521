import json

movie_database = {}

def main():
    while True:
        print('\n===== Movie Database Management System ==== \n')
        print('1. Add a movie')
        print('2. Edit a movie')
        print('3. Delete a movie')
        print('4. View all movies')
        print('5. Search movies')
        print('6. Save data to file')
        print('7. Load data from file')
        print('8 Exit \n')

        choice = input('Enter your choice: ')
        if choice == '1':
            add_movie()
        elif choice == '2':
            edit_movie()
        elif choice == '3':
            delete_movie()
        elif choice == '4':
            view_all_movies()
        elif choice == '5':
            search_movies()
        elif choice == '6':
            write_file()
        elif choice == '7':
            read_file()
        elif choice == '8':
            print('Goodbye')
            break
        else:
            print('Invalid Choice. Please Try Again')
def add_movie():
   title = input("Enter the movie title: ")
   genre = input("Enter the movie genre: ")
   director = input("Enter the movie director: ")
   release_date = input("Enter the movie release date as YYYY-MM-DD: ")
   actors = input("Enter the movie actors (comma separated): ").split(",")

   movie_database[title] = {
       "genre": genre,
       "director": director,
       "release_date": release_date,
       "actors": actors
   }

def edit_movie():
   title = input("Enter the movie title to edit: ")
   if title in movie_database:
       change = input("What do you want to change? (genre/director/release_date/actors): ")
       if change in movie_database[title]:
           new_value = input(f"Enter the new value for {change}: ")
           if change == "actors":
               new_value = new_value.split(",")
           movie_database[title][change] = new_value
       else:
           print("Invalid field. Please choose from genre, director, release_date, or actors.")

       movie_database[title][change] = new_value
   else:
       print("Movie not found in the database.")

def delete_movie():
   title = input("Enter the movie title to delete: ")
   if title in movie_database:
       del movie_database[title]
       print(f"{title} has been deleted from the database.")
   else:
       print("Movie not found in the database.")

def view_all_movies():
    if not movie_database:
        print("No movies in the database.")
        return
    for title, data in movie_database.items():
        print(f"{title}: {json.dumps(data, indent=4)}")


def write_file():
    with open("movie_database.json", "w") as file:
        json.dump(movie_database, file, indent=4)

def read_file():
    global movie_database
    try:
        with open("movie_database.json", "r") as file:
            movie_database = json.load(file)
            print("Data loaded successfully.", list(movie_database.keys())[:5])
    except FileNotFoundError:
        print("No saved data found. Starting with an empty database.")

def search_movies():
    search_term = input("Enter a search term (title, genre, director, or actor): ").lower()
    results = []
    for title, data in movie_database.items():
        if (search_term in title.lower() or
            search_term in data["genre"].lower() or
            search_term in data["director"].lower() or
            any(search_term in actor.lower() for actor in data["actors"])):
            results.append(title)

    if results:
        print("Search Results:")
        for result in results:
            print(result)
    else:
        print("No movies found matching the search term.")


if __name__ == "__main__":
    main()