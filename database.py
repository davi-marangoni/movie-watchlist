import datetime
import psycopg2

connection = psycopg2.connect(
    host='localhost',
    database='watchlist',
    user='postgres',
    password='postgres'
)
cursor = connection.cursor()

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_timestamp REAL
);
"""

CREATE_USERS_TABLE = """CREATE TABLE IF NOT EXISTS users(
    username TEXT PRIMARY KEY
);"""

CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched (
    username TEXT,
    movie_id INTEGER,
    FOREIGN KEY (username) REFERENCES users(username),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);"""

INSERT_MOVIES = """INSERT INTO movies (
    title,
    release_timestamp)
    VALUES (%s, %s);"""

INSERT_USER = "INSERT INTO users (username) VALUES (%s)"

SELECT_ALL_MOVIES = "SELECT * FROM movies;"

SELECT_MOVIE = "SELECT * FROM movies WHERE id = %s;"

SELECT_UPCOMING_MOVIES = """SELECT * FROM movies WHERE release_timestamp > %s;"""

SELECT_WATCHED_MOVIES = """SELECT movies.*
                            FROM movies
                            JOIN watched ON movies.id = watched.movie_id
                            WHERE username = %s;"""

SET_MOVIES_WATCHED = """UPDATE movies SET watched = 1 WHERE title = %s;"""

DELETE_MOVIE = "DELETE FROM movies WHERE title = %s"

INSERT_WATCHED_MOVIE = """INSERT INTO watched (username, movie_id) VALUES (%s, %s)"""

SEARCH_MOVIES = "SELECT * FROM movies WHERE title LIKE %s"

CREATE_RELEASE_INDEX = "CREATE INDEX IF NOT EXISTS idx_movies_release ON movies(release_timestamp);"

SELECT_ALL_USERS = "SELECT * FROM users;"

SELECT_USER = "SELECT * FROM users WHERE username = %s;"

DELETE_USER = "DELETE FROM users WHERE username = %s;"

DELETE_MOVIE = "DELETE FROM movies WHERE title = %s;"

def add_user(username):
    with connection:
        cursor.execute(INSERT_USER, (username,))


def add_movies(title, release_timestamp):
    with connection:
        cursor.execute(INSERT_MOVIES, (title, release_timestamp))


def get_movies(upcoming=False):
    with connection:
        if upcoming:
            today_timestamp = datetime.datetime.today().timestamp()
            cursor.execute(SELECT_UPCOMING_MOVIES, (today_timestamp,))
        else:
            cursor.execute(SELECT_ALL_MOVIES)
        return cursor.fetchall()


def search_movies(search_term):
    with connection:
        cursor.execute(SEARCH_MOVIES, (f"%{search_term}%",))
        return cursor.fetchall()


def watch_movies(username, movie_id):
    with connection:
        cursor.execute(INSERT_WATCHED_MOVIE, (username, movie_id))


def get_watched_movies(username):
    with connection:
        cursor.execute(SELECT_WATCHED_MOVIES, (username,))
        return cursor.fetchall()

def get_users():
    with connection:
        cursor.execute(SELECT_ALL_USERS)
        return cursor.fetchall()

def delete_user(username):
    with connection:
        cursor.execute(DELETE_USER, (username,))

def delete_movie(title):
    with connection:
        cursor.execute(DELETE_MOVIE, (title,))

def user_exists(username):
    with connection:
        cursor.execute(SELECT_USER, (username,))
        return cursor.fetchone() is not None

def movie_exists(movie_id):
    with connection:
        cursor.execute(SELECT_MOVIE, (movie_id,))
        return cursor.fetchone() is not None