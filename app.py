import prompt as p
import database

print(p.welcome)

while (user_input := input(p.menu)) != "11":
    if user_input == "1":
        p.prompt_add_movies()
    elif user_input == "2":
        movies = database.get_movies(True)
        p.print_movie_list("Upcoming", movies)
    elif user_input == "3":
        movies = database.get_movies()
        p.print_movie_list("All", movies)
    elif user_input == "4":
        p.prompt_watch_movie()
    elif user_input == "5":
        p.prompt_show_watched_movies()
    elif user_input == "6":
        p.prompt_add_user()
    elif user_input == "7":
        p.prompt_search_movies()
    elif user_input == "8":
        p.prompt_show_users()
    elif user_input == "9":
        p.prompt_delete_user()
    elif user_input == "10":
        p.prompt_delete_movie()
    else:
        print("\nInvalid option, please select another option!\n")
