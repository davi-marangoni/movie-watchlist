# Movie Watchlist

## Description
Another simple prompt aplication to test some functions of python and psychopg2

### Technologies Used

- Python 3.10
- Psychopg2 2.9.6
- PostgreSQL 15.3
- Docker 24.0.2
- Docker Compose 2.18.1

## How to run

1. Clone this repository

```bash
$ git@github.com:davi-marangoni/movie-watchlist.git
```

2. Install the psycopg2 library

```bash
$ pip install psycopg2
```

3. Install Docker and Docker Compose

```bash
 $ sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
 $ sudo apt-get install docker-compose-plugin
```

4. Create the docker.compose.yml file and run

```bash
version: '3'
services:
  postgres:
    image: postgres:latest
    restart: always
    ports:
      - '5432:5432'
    environment:
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=postgres
      - POSTGRES_DB=postgres
    volumes:
      - ./data:/var/lib/postgresql/data
```
```bash
$ docker compose up -d
```

5. Create the database and table's

```bash
CREATE DATABASE watchlist;

CREATE TABLE public.movies (
	id serial4 NOT NULL,
	title text NULL,
	release_timestamp float4 NULL,
	CONSTRAINT movies_pkey PRIMARY KEY (id)
);
CREATE INDEX idx_movies_release ON public.movies USING btree (release_timestamp);

CREATE TABLE public.users (
	username text NOT NULL,
	CONSTRAINT users_pkey PRIMARY KEY (username)
);

CREATE TABLE public.watched (
	username text NULL,
	movie_id int4 NULL
);
ALTER TABLE public.watched ADD CONSTRAINT watched_movie_id_fkey FOREIGN KEY (movie_id) REFERENCES public.movies(id);
ALTER TABLE public.watched ADD CONSTRAINT watched_user_name_fkey FOREIGN KEY (username) REFERENCES public.users(username);
```