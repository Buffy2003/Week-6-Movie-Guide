# Rashelle Ward
# CIS261
# Week 6 - Movie List Program

FILENAME = "Movies.txt"

def write_movies(movies):
    with open(FILENAME, "w") as file:
        for movie in movies:
            file.write(f"{movie}\n")

def read_movies():
    movies = []
    with open(FILENAME) as file:
        for line in file:
            line = line.replace("\n", "")
            movies.append(line)
        return movies

def display_menu():
    print("The Movie List Program")
    print()
    print("Command Menu")
    print("List     -   List all movies")
    print("Add      -   Add a movie")
    print("Delete   -   Delete a movie")
    print("Exit     -   Exit program")
    print()

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()

def add_movie(movies):
    movie = input("Movie name: ")
    movies.append(movie)
    write_movies(movies)
    print(f"{movie} has been added.\n")

def delete_movie(movies):
    index = int(input("Number: "))
    if index < 1 or index > len(movies):
        print("This is an invalid movie number.\n")
    else:
        movie = movies.pop(index - 1)  # pop -1 because lists are zero based number 1 is actually position 0
        write_movies(movies)
        print(f"{movie} has been deleted.\n")

def main():
    display_menu()
    movies = read_movies()
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "delete":
            delete_movie(movies)
        elif command.lower() == "exit":
            print("Goodbye!")
            break
        else:
            print("This is not a valid command. Please try again.\n")

if __name__ == "__main__":
        main()
