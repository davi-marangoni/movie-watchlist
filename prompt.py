import datetime
import database

welcome = "Welcome to the watchlist app!"
menu = """\nPlease select one of the following options:
1) Add new movie.
2) View upcoming movies.
3) View all movies
4) Watch a movie
5) View watched movies.
6) Add user to the app.
7) Search for a movie.
8) Show all users.
9) Delete a user.
10) Delete a movie.
11) Exit.

Your selection: """

def prompt_show_users():
    users = database.get_users()
    print("All Users:")
    for user in users:
        print(user)
    print("----\n")

def prompt_delete_user():
    username = input("Enter the username to delete: ")
    database.delete_user(username)
    print(f"{username} has been deleted from the app.\n")

def prompt_delete_movie():
    title = input("Enter the movie title to delete: ")
    database.delete_movie(title)
    print(f"{title} has been deleted from the database.\n")

def prompt_add_movies():
    title = input("movie title: ")
    release_date = input("Release date (dd-mm-yy): ")
    parsed_date = datetime.datetime.strptime(release_date, "%d-%m-%Y")
    timestamp = parsed_date.timestamp()

    database.add_movies(title, timestamp)

def print_movie_list(heading, movies):
    print(f"--{heading} movies--")
    for _id, title, release_date in movies:
        movie_date = datetime.datetime.fromtimestamp(release_date)
        human_date = movie_date.strftime("%b %d %Y")
        print(f"{_id}: {title} released on {human_date}")
    print("----\n")

def prompt_watch_movie():
    username = input("Username: ")
    if not database.user_exists(username):
        print(f"User '{username}' does not exist.")
        return
    movie_id = input("Movie ID: ")
    if not database.movie_exists(movie_id):
        print(f"Movie with ID '{movie_id}' does not exist.")
        return
    database.watch_movies(username, movie_id)
    print(f"Movie with ID '{movie_id}' has been marked as watched by user '{username}'\n")

def prompt_add_user():
    username = input("Username: ")
    database.add_user(username)

def prompt_show_watched_movies():
    username = input("Username: ")
    movies = database.get_watched_movies(username)
    if movies:
        print_movie_list(f"{username}'s watched movies", movies)
    else:
        print("This user has not watched anything yet!")

def prompt_search_movies():
    search_term = input("Enter partial movie title: ")
    movies = database.search_movies(search_term)
    if movies:
        print_movie_list("Movies found", movies)
    else:
        print("Found no movies for that search term")