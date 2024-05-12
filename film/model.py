import pickle
import os.path
class Film:
    def __init__(self, title, author, genre, description):
        self.title = title
        self.author = author
        self.genre = genre
        self.description = description

    def __str__(self):
        return f"{self.title} ({self.author})"

class FilmModel:
    def __init__(self):
        self.film_name = "film.txt"
        self.films = self.load_data()
    def add_film(self, dict_film):
        film = Film(*dict_film.values())
        self.films[film.title] = film

    def get_all_films(self):
        return self.films.values()

    def get_single_film(self, user_title):
        film = self.films[user_title]
        dict_film = {
            "название": film.title,
            "автор": film.author,
            "жанр": film.genre,
            "описание": film.description
        }
        return dict_film

    def remove_film(self, user_title):
        return self.films.pop(user_title)

    def save_data(self):
        with open(self.film_name, "wb") as f:
            pickle.dump(self.films, f)

    def load_data(self):
        if os.path.exists(self.film_name):
            with open(self.film_name, "rb") as f:
                return pickle.load(f)
        else:
            return dict()